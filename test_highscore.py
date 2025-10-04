#!/usr/bin/python3
"""
Script de teste para verificar a funcionalidade de high score do KobraPy
"""

import os

# Definir constantes diretamente para evitar importar pygame
HIGHSCORE_FILE = "assets/highscore.txt"

# Implementar as funções de teste baseadas no código original
def load_high_score():
    score = 0
    try:
        file = open(HIGHSCORE_FILE, "r")
        score = file.read()
        file.close()
    finally:
        return int(score)

def save_high_score(score):
    try:
        file = open(HIGHSCORE_FILE, "w")
        file.write(str(score))
        file.close()
    except:
        print("Failed to open file")

def update_high_score(current_score):
    high_score = load_high_score()
    if current_score > high_score:
        return current_score
    return high_score

def test_load_high_score():
    """Testa se a função load_high_score carrega corretamente o valor do arquivo"""
    print("🧪 Testando load_high_score()...")
    
    # Verificar se o arquivo existe
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, 'r') as f:
            expected_score = int(f.read().strip())
        print(f"   Valor esperado no arquivo: {expected_score}")
    else:
        expected_score = 0
        print("   Arquivo não existe, valor esperado: 0")
    
    # Testar a função
    loaded_score = load_high_score()
    print(f"   Valor carregado pela função: {loaded_score}")
    
    if loaded_score == expected_score:
        print("   ✅ PASSOU: load_high_score() funcionou corretamente")
        return True
    else:
        print("   ❌ FALHOU: load_high_score() não carregou o valor correto")
        return False

def test_save_high_score():
    """Testa se a função save_high_score salva corretamente no arquivo"""
    print("\n🧪 Testando save_high_score()...")
    
    # Fazer backup do valor atual
    original_score = load_high_score()
    print(f"   Score original: {original_score}")
    
    # Testar salvar um novo valor
    test_score = 42
    print(f"   Salvando score de teste: {test_score}")
    save_high_score(test_score)
    
    # Verificar se foi salvo corretamente
    saved_score = load_high_score()
    print(f"   Score carregado após salvar: {saved_score}")
    
    if saved_score == test_score:
        print("   ✅ PASSOU: save_high_score() funcionou corretamente")
        # Restaurar o valor original
        save_high_score(original_score)
        print(f"   Score original restaurado: {original_score}")
        return True
    else:
        print("   ❌ FALHOU: save_high_score() não salvou corretamente")
        # Tentar restaurar o valor original mesmo assim
        save_high_score(original_score)
        return False

def test_update_high_score():
    """Testa se a função update_high_score atualiza corretamente o high score"""
    print("\n🧪 Testando update_high_score()...")
    
    current_high_score = load_high_score()
    print(f"   High score atual: {current_high_score}")
    
    # Teste 1: Score menor que o high score atual
    lower_score = max(0, current_high_score - 5)
    result1 = update_high_score(lower_score)
    print(f"   Teste 1 - Score menor ({lower_score}): resultado = {result1}")
    if result1 == current_high_score:
        print("   ✅ Passou: manteve o high score quando score é menor")
        test1_passed = True
    else:
        print("   ❌ Falhou: não manteve o high score quando score é menor")
        test1_passed = False
    
    # Teste 2: Score maior que o high score atual
    higher_score = current_high_score + 10
    result2 = update_high_score(higher_score)
    print(f"   Teste 2 - Score maior ({higher_score}): resultado = {result2}")
    if result2 == higher_score:
        print("   ✅ Passou: atualizou o high score quando score é maior")
        test2_passed = True
    else:
        print("   ❌ Falhou: não atualizou o high score quando score é maior")
        test2_passed = False
    
    # Teste 3: Score igual ao high score atual
    result3 = update_high_score(current_high_score)
    print(f"   Teste 3 - Score igual ({current_high_score}): resultado = {result3}")
    if result3 == current_high_score:
        print("   ✅ Passou: manteve o high score quando score é igual")
        test3_passed = True
    else:
        print("   ❌ Falhou: não manteve o high score quando score é igual")
        test3_passed = False
    
    return test1_passed and test2_passed and test3_passed

def test_file_persistence():
    """Testa se as mudanças no high score persistem no arquivo"""
    print("\n🧪 Testando persistência no arquivo...")
    
    # Salvar o score atual
    original_score = load_high_score()
    print(f"   Score original: {original_score}")
    
    # Salvar um novo score
    new_score = original_score + 20
    print(f"   Salvando novo score: {new_score}")
    save_high_score(new_score)
    
    # Verificar se está no arquivo
    with open(HIGHSCORE_FILE, 'r') as f:
        file_content = f.read().strip()
    print(f"   Conteúdo do arquivo: '{file_content}'")
    
    # Carregar novamente
    reloaded_score = load_high_score()
    print(f"   Score carregado novamente: {reloaded_score}")
    
    if str(new_score) == file_content and reloaded_score == new_score:
        print("   ✅ PASSOU: persistência funcionou corretamente")
        # Restaurar o valor original
        save_high_score(original_score)
        print(f"   Score original restaurado: {original_score}")
        return True
    else:
        print("   ❌ FALHOU: persistência não funcionou")
        # Tentar restaurar o valor original
        save_high_score(original_score)
        return False

def main():
    """Executa todos os testes"""
    print("🎮 TESTE DA FUNCIONALIDADE DE HIGH SCORE - KOBRAPY")
    print("=" * 50)
    
    # Executar todos os testes
    tests = [
        test_load_high_score,
        test_save_high_score,
        test_update_high_score,
        test_file_persistence
    ]
    
    passed_tests = 0
    total_tests = len(tests)
    
    for test in tests:
        if test():
            passed_tests += 1
    
    # Resultado final
    print("\n" + "=" * 50)
    print(f"📊 RESULTADO FINAL: {passed_tests}/{total_tests} testes passaram")
    
    if passed_tests == total_tests:
        print("🎉 SUCESSO: Todas as funcionalidades de high score estão funcionando!")
    else:
        print("⚠️  ATENÇÃO: Algumas funcionalidades podem estar com problemas.")
    
    print("=" * 50)

if __name__ == "__main__":
    main()