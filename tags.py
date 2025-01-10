class MorphemeTag:
    END = 'END'
    ROOT = 'ROOT'
    SUFF = 'SUFF'
    PREF = 'PREF'


class POSTag:
    """Часть речи"""
    NOUN = 'NOUN'
    """имя существительное"""
    ADJF = 'ADJF'
    """имя прилагательное(полное)"""
    ADJS = 'ADJS'
    """прилагательное(краткое)"""
    COMP = 'COMP'
    """компаратив"""
    VERB = 'VERB'
    """глагол(личная форма)"""
    INFN = 'INFN'
    """глагол(инфинитив)"""
    PRTF = 'PRTF'
    """причастие(полное)"""
    PRTS = 'PRTS'
    """причастие(краткое)"""
    GRND = 'GRND'
    """деепричастие"""
    NUMR = 'NUMR'
    """числительное"""
    ADVB = 'ADVB'
    """наречие"""
    NPRO = 'NPRO'
    """местоимение"""

    ALL = {NPRO, ADVB, NUMR, GRND, PRTS, PRTF, INFN, VERB, COMP, ADJS, ADJF, NOUN}
