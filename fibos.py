# stockage des valeurs
memo = {0:0, 1:1}
memo 
# {0: 0, 1: 1}

def fibo(memo, n):
    '''
    Args:
        memo (dict): le dictionnaire qui mémorise les cacluls
        n (int): le chiffre dont on veut calculer le nbre de Fibonacci

    Returns:
        int : le résultat de Fibonacci
    '''
    
    if n<=1: 
        return n
    print(f"fibo({memo}, {n})")
    if n not in memo:
        memo[n] = fibo(memo, n-1) + fibo(memo, n-2)
    return memo[n]





##################################

def fib(n):
    """Calcule la suite de Fibonacci (récursif pur)
        
    Utilise une version sans résultats intermédiaires
    
    Args:
        n (int): le chiffre dont on veut calculer le nbre de Fibonacci

    Returns:
        int : le résultat de Fibonacci
    """
    print(f"fib({n})")
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)