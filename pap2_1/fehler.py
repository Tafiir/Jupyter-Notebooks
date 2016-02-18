import sympy as s

def fehler(func, *args):
    f = 0

    for var in args:
        d = s.symbols('d' + var.name)        #Symbole fuer die Fehler generieren

        partial = s.diff(func, var) * d  #Partielle Differentation und mit mit Fehlersymbol 'd' multiplizieren
        f = f + partial**2

        f_abs=s.simplify(s.sqrt(f))              #Latex Format fuer den absoluten Fehler
        f_rel=s.simplify(s.sqrt(f/func**2))  #Latex Format fuer den relativen Fehler

    return f_abs, f_rel
