from tags import POSTag

BIMORPH_BY_POS = {
    POSTag.VERB: {
        ('обез', 'и'), ('про', 'и'), ('с', 'и'), ('у', 'ся'), ('из', 'е'), ('ис', 'и'), ('с', 'а'), ('пере', 'и'),
        ('разо', 'ся'), ('на', 'ся'), ('с', 'ива'), ('об', 'е'), ('раз', 'сь'), ('пере', 'ива'), ('за', 'е'),
        ('о', 'и'), ('обес', 'и'), ('вз', 'и'), ('про', 'ся'), ('с', 'ся'), ('по', 'е'), ('ото', 'ся'), ('при', 'и'),
        ('из', 'и'), ('в', 'ся'), ('пере', 'ыва'), ('разо', 'сь'), ('о', 'ся'), ('вз', 'ся'), ('об', 'и'),
        ('за', 'и'), ('от', 'и'), ('раз', 'и'), ('под', 'и'), ('обез', 'е'), ('вы', 'ся'), ('по', 'и'), ('при', 'ся'),
        ('рас', 'и'), ('из', 'ся'), ('ис', 'е'), ('до', 'ся'), ('у', 'и'), ('об', 'ся'), ('за', 'ся'), ('от', 'ся'),
        ('раз', 'ся'), ('с', 'я'), ('у', 'ива'), ('о', 'е')},
    POSTag.ADVB: {
        ('по', 'ому'), ('по', 'и'), ('по', 'ему')},
    POSTag.ADJF: {
        ('транс', 'н'), ('транс', 'ов'), ('про', 'ическ'), ('про', 'ск'), ('транс', 'альн'), ('про', 'анск'),
        ('со', 'н'), ('про', 'н'), ('транс', 'ск'), ('с', 'н')}}
