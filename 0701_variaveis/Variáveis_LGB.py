GLOBAL_VAR="valor global"
def exemplo_local():
    local_var="valor local"                                     #--- Variavel local, Só existe dentro desta funçao
    print("local_var:", local_var)
    print("GLOBAL_VAR:", GLOBAL_VAR)                            #--- acessar variavel global para leitura funciona sem declarar "global"
    print("Built-in len(\"abc\"):", len("abc"))                 #--- Usar um built-in (len)
def exemplo_modifica():
    global GLOBAL_VAR                                           #--- para modificar a variavel global dentro da função, declarar "global"
    GLOBAL_VAR="novo valor global"
    print("GLOBAL_VAR modificado para:", GLOBAL_VAR)
print("GLOBAL_VAR (antes):", GLOBAL_VAR)
exemplo_local()
exemplo_modifica()
print("GLOBAL_VAR (depois):", GLOBAL_VAR)