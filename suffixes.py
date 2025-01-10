from tags import POSTag

PART_BY_SUFF = {'б': {'NOUN'}, 'об': {'NOUN'}, 'ытьб': {'NOUN'}, 'в': {'GRND', 'NOUN'}, 'ев': {'NOUN'},
                'ив': {'ADJF', 'NOUN'},
                'ов': {'ADJF', 'NOUN'}, 'овь': {'NOUN'}, 'тв': {'NOUN'}, 'ств': {'NOUN'}, 'овств': {'NOUN'},
                'еств': {'NOUN', 'VERB'},
                'инств': {'NOUN'}, 'тельств': {'NOUN'}, 'аг': {'NOUN'}, 'инг': {'NOUN'}, 'ург': {'NOUN'},
                'уг': {'NOUN'},
                'ыг': {'NOUN'}, 'д': {'NOUN'}, 'ад': {'NOUN'}, 'иад': {'NOUN'}, 'арад': {'NOUN'}, 'оид': {'NOUN'},
                'ядь': {'NOUN'},
                'аж': {'NOUN'}, 'ёжь': {'NOUN'}, 'оз': {'NOUN'}, 'ай': {'NOUN'}, 'атай': {'NOUN'},
                'o|вj': {'NOUN'}, 'а|дj': {'NOUN'}, 'ей': {'NOUN'}, 'алей': {'NOUN'}, 'ачей': {'NOUN'},
                'ий': {'ADJF', 'NOUN'}, 'j': {'NOUN'}, 'и|j': {'NOUN'}, 'стви|j': {'NOUN'}, 'ни|j': {'NOUN'},
                '|нj': {'NOUN'},
                'ани|j': {'NOUN'}, 'а|нj': {'NOUN'}, 'овани|j': {'NOUN'}, 'ени|j': {'NOUN'}, 'e|нj': {'NOUN'},
                'арий': {'NOUN'},
                'ери|j': {'NOUN'}, 'орий': {'NOUN'}, 'ти|j': {'NOUN'}, 'ци|j': {'NOUN'}, 'аци|j': {'NOUN'},
                'изаци|j': {'NOUN'}, 'ици|j': {'NOUN'}, 'нци|j': {'NOUN'}, 'енци|j': {'NOUN'}, 'a|нj': {'NOUN'},
                'е|нj': {'NOUN'},
                'уй': {'NOUN'}, 'тяй': {'NOUN'}, 'к': {'NOUN'}, 'ак': {'NOUN'}, 'чак': {'NOUN'}, 'авк': {'NOUN'},
                'овк': {'NOUN'},
                'ловк': {'NOUN'}, 'анек': {'NOUN'}, 'ышек': {'NOUN'}, 'ежк': {'NOUN'}, 'ик': {'ADVB', 'NOUN'},
                'евик': {'NOUN'},
                'ник': {'NOUN'}, 'овник': {'NOUN'}, 'еник': {'NOUN'}, 'ейник': {'NOUN'}, 'арник': {'NOUN'},
                'атник': {'NOUN'},
                'льник': {'NOUN'}, 'истик': {'NOUN'}, 'чик': {'NOUN'}, 'щик': {'NOUN'}, 'овщик': {'NOUN'},
                'льщик': {'NOUN'},
                'айк': {'NOUN'}, 'ейк': {'NOUN'}, 'лк': {'NOUN'}, 'анк': {'NOUN'}, 'инк': {'NOUN'}, 'онк': {'NOUN'},
                'унк': {'NOUN'},
                'ок': {'ADVB', 'NOUN'}, 'онок': {'NOUN'}, 'чонок': {'NOUN'}, 'ушок': {'NOUN'}, 'ерк': {'NOUN'},
                'урк': {'NOUN'},
                'етк': {'NOUN'}, 'отк': {'NOUN'}, 'ютк': {'NOUN'}, 'ук': {'NOUN'}, 'чук': {'NOUN'}, 'чк': {'NOUN'},
                'ачк': {'NOUN'},
                'ечк': {'NOUN'}, 'ичка': {'NOUN'}, 'очк': {'NOUN'}, 'шк': {'NOUN'}, 'ашк': {'NOUN'}, 'ёшк': {'NOUN'},
                'ишк': {'NOUN'},
                'ушк': {'NOUN'}, 'ышк': {'NOUN'}, 'ык': {'NOUN'}, 'ульк': {'NOUN'}, 'оньк': {'ADJF', 'NOUN'},
                'юк': {'NOUN'},
                'няк': {'NOUN'}, 'ль': {'NOUN'}, 'л': {'VERB', 'ADJF', 'NOUN'}, 'ал': {'NOUN'}, 'аль': {'NOUN'},
                'ёл': {'NOUN'},
                'ель': {'NOUN'}, 'ел': {'NOUN'}, 'тель': {'NOUN'}, 'итель': {'NOUN'}, 'ил': {'NOUN'}, 'ол': {'NOUN'},
                'оль': {'NOUN'},
                'ул': {'NOUN'}, 'ыль': {'NOUN'}, 'изм': {'NOUN'}, 'онизм': {'NOUN'}, 'им': {'PRTF', 'ADJF', 'NOUN'},
                'нь': {'NOUN'},
                'н': {'ADJF', 'NOUN'}, 'ан': {'ADJF', 'NOUN'}, 'уган': {'NOUN'}, 'иан': {'NOUN'}, 'овиан': {'NOUN'},
                '|ja|н': {'NOUN'},
                'лан': {'NOUN'}, 'ман': {'NOUN'}, 'овн': {'ADJF', 'NOUN'}, 'ень': {'NOUN'}, 'ён': {'ADJF', 'NOUN'},
                'мен': {'NOUN'},
                'смен': {'NOUN'}, 'знь': {'NOUN'}, 'изн': {'NOUN'}, 'овизн': {'NOUN'}, 'ин': {'ADJF', 'NOUN'},
                'бин': {'NOUN'},
                'овин': {'NOUN'}, 'лин': {'NOUN'}, 'елин': {'NOUN'}, 'анин': {'NOUN'}, 'жан': {'NOUN'}, 'чан': {'NOUN'},
                'овчан': {'NOUN'}, 'ичан': {'NOUN'}, 'инчан': {'NOUN'}, 'тян': {'NOUN'}, 'итян': {'NOUN'},
                'атин': {'NOUN'},
                'чин': {'NOUN'}, 'щин': {'NOUN'}, 'овщин': {'NOUN'}, 'льщин': {'NOUN'}, 'он': {'NOUN'}, 'сн': {'NOUN'},
                'снь': {'NOUN'}, 'отн': {'ADJF', 'NOUN'}, 'ятн': {'NOUN'}, 'ун': {'NOUN'}, 'иничн': {'NOUN'},
                'ышн': {'NOUN'},
                'льн': {'ADJF', 'NOUN'}, 'ынь': {'NOUN'}, 'иян': {'NOUN'}, 'ар': {'NOUN'}, 'арь': {'NOUN'},
                'атарь': {'NOUN'},
                'ер': {'NUMR', 'NOUN'}, 'иат': {'NOUN'}, 'чат': {'ADJF', 'NOUN'}, 'евт': {'NOUN'}, 'ет': {'NOUN'},
                'итет': {'NOUN'},
                'ит': {'ADJF', 'NOUN'}, 'нит': {'NOUN'}, 'инит': {'NOUN'}, 'ант': {'NOUN'}, 'ент': {'NOUN'},
                'амент': {'NOUN'},
                'емент': {'NOUN'}, 'от': {'NOUN'}, 'оть': {'NOUN'}, 'иот': {'NOUN'}, 'ист': {'ADJF', 'NOUN'},
                'ость': {'NOUN'},
                'имость': {'NOUN'}, 'ность': {'NOUN'}, 'нность': {'NOUN'}, 'енность': {'NOUN'}, 'тость': {'NOUN'},
                'ут': {'NOUN'},
                'х': {'NOUN'}, 'ах': {'ADVB', 'NOUN'}, 'ках': {'ADVB'}, 'их': {'ADVB', 'NOUN'}, 'ох': {'NOUN'},
                'ух': {'NOUN'},
                'ц': {'NOUN'}, 'ец': {'NOUN'}, 'авец': {'NOUN'}, 'овец': {'NOUN'}, 'лец': {'NOUN'}, 'омец': {'NOUN'},
                'нец': {'NOUN'},
                'енец': {'NOUN'}, 'инец': {'NOUN'}, 'иц': {'NOUN'}, 'овиц': {'NOUN'}, 'лиц': {'NOUN'}, 'ниц': {'NOUN'},
                'овниц': {'NOUN'}, 'ениц': {'NOUN'}, 'атниц': {'NOUN'}, 'униц': {'NOUN'}, 'ичниц': {'NOUN'},
                'очниц': {'NOUN'},
                'ешниц': {'NOUN'}, 'льниц': {'NOUN'}, 'тельниц': {'NOUN'}, 'льц': {'NOUN'}, 'ч': {'ADJF', 'NOUN'},
                'ач': {'ADJF', 'NOUN'}, 'ич': {'NOUN'}, 'евич': {'NOUN'}, 'ович': {'NOUN'}, 'ыч': {'NOUN'},
                'аш': {'NOUN'},
                'иш': {'NOUN'}, 'ошь': {'NOUN'}, 'ош': {'NOUN'}, 'уш': {'NOUN'}, 'оныш': {'NOUN'}, 'ищ': {'NOUN'},
                'бищ': {'NOUN'},
                'овищ': {'NOUN'}, 'лищ': {'NOUN'}, 'а': {'VERB', 'GRND'}, 'учи': {'GRND'}, 'ши': {'GRND'},
                'вши': {'GRND'},
                'ом': {'PRTF', 'ADVB', 'ADJF'}, 'нн': {'PRTF', 'ADJF'}, 'ённ': {'PRTF', 'ADJF'}, 'т': {'PRTF', 'ADJF'},
                'ш': {'PRTF', 'ADJF'}, 'вш': {'PRTF'}, 'ащ': {'PRTF', 'ADJF'}, 'ущ': {'PRTF', 'ADJF'}, 'ав': {'ADJF'},
                'ощав': {'ADJF'}, 'лив': {'ADJF'}, 'овлив': {'ADJF'}, 'елив': {'ADJF'}, 'члив': {'ADJF'},
                'чив': {'ADJF'},
                '|jo|в': {'ADJF'}, 'ляв': {'ADJF'}, 'овий': {'ADJF'}, 'ачий': {'ADJF'}, 'ичий': {'ADJF'},
                'енек': {'ADJF'},
                'онек': {'ADJF'}, 'ск': {'ADJF'}, 'вск': {'ADJF'}, 'евск': {'ADJF'}, 'овск': {'ADJF'},
                '|jo|вск': {'ADJF'},
                'еск': {'ADJF'}, 'ческ': {'ADJF'}, 'ическ': {'ADJF'}, 'истическ': {'ADJF'}, 'лезск': {'ADJF'},
                'эзск': {'ADJF'},
                'йск': {'ADJF'}, 'ейск': {'ADJF'}, 'ийск': {'ADJF'}, 'имск': {'ADJF'}, 'нск': {'ADJF'},
                'анск': {'ADJF'},
                'ианск': {'ADJF'}, '|jа|нск': {'ADJF'}, 'енск': {'ADJF'}, 'инск': {'ADJF'}, 'унск': {'ADJF'},
                'тельск': {'ADJF'},
                'ацк': {'ADJF'}, 'ецк': {'ADJF'}, 'усеньк': {'ADJF'}, 'ошеньк': {'ADJF'}, 'охоньк': {'ADJF'},
                'як': {'ADVB', 'ADJF'},
                'овал': {'ADJF'}, '|jo|м': {'ADVB'}, 'ебн': {'ADJF'}, 'обн': {'ADJF'}, 'евн': {'ADJF'}, 'ивн': {'ADJF'},
                'ен': {'ADJF'}, 'яжн': {'ADJF'}, 'езн': {'ADJF'}, 'озн': {'ADJF'}, 'иозн': {'ADJF'}, 'нин': {'ADJF'},
                'йн': {'ADJF'},
                'ейн': {'ADJF'}, 'анн': {'ADJF'}, 'ованн': {'ADJF'}, 'ированн': {'ADJF'}, 'енн': {'ADJF'},
                'овенн': {'ADJF'},
                'ственн': {'ADJF'}, 'менн': {'ADJF'}, 'онн': {'ADJF'}, 'ионн': {'ADJF'}, 'ационн': {'ADJF'},
                'арн': {'ADJF'},
                'орн': {'ADJF'}, 'ичн': {'ADJF'}, 'очн': {'ADJF'}, 'шн': {'ADJF'}, 'ашн': {'ADJF'}, 'ишн': {'ADJF'},
                'альн': {'ADJF'},
                'идальн': {'ADJF'}, 'иальн': {'ADJF'}, 'ональн': {'ADJF'}, 'уальн': {'ADJF'}, 'ельн': {'ADJF'},
                'абельн': {'ADJF'},
                'ибельн': {'ADJF'}, 'тельн': {'ADJF'}, 'ительн': {'ADJF'}, 'ильн': {'ADJF'}, 'ат': {'ADJF'},
                'оват': {'ADJF'},
                'овит': {'ADJF'}, 'мент': {'ADJF'}, 'аст': {'ADJF'}, 'нич': {'ADJF'}, 'уч': {'ADJF'}, 'айш': {'ADJF'},
                'ейш': {'ADJF'},
                'еющ': {'ADJF'}, 'е': {'ADVB', 'VERB'}, 'и': {'ADVB', 'VERB'}, 'ива': {'VERB'}, 'ова': {'VERB'},
                'ств-ова': {'VERB'},
                'из': {'VERB'}, 'ир': {'VERB'}, 'ка': {'ADVB', 'VERB'},
                'ича': {'VERB'}, 'нича': {'VERB'}, 'ну': {'VERB'}, 'ану': {'VERB'}, 'ое': {'ADVB'}, 'ые': {'ADVB'},
                'ства': {'ADVB'},
                'яка': {'ADVB'}, 'ки': {'ADVB'}, 'ой': {'ADVB'}, 'кой': {'ADVB'}, 'ами': {'ADVB'}, 'ками': {'ADVB'},
                'ком': {'ADVB'},
                'иком': {'ADVB'}, 'ышком': {'ADVB'}, 'няком': {'ADVB'}, 'уном': {'ADVB'}, 'ишом': {'ADVB'},
                'ым': {'ADVB'},
                'ы': {'ADVB'}, 'жды': {'ADVB'}, 'ажды': {'ADVB'}, 'ою': {'ADVB'}, 'ую': {'ADVB'}, 'остью': {'ADVB'},
                'мя': {'ADVB'},
                'о': {'ADVB'}, 'ко': {'ADVB'}, 'енько': {'ADVB'}, 'ошенько': {'ADVB'}, 'онько': {'ADVB'},
                'охонько': {'ADVB'},
                'но': {'ADVB'}, 'овато': {'ADVB'}, 'у': {'ADVB'}, '|jy|': {'ADVB'}, 'ку': {'ADVB'}, 'еньку': {'ADVB'},
                'оньку': {'ADVB'}, 'ому': {'ADVB'}, 'оту': {'ADVB'}, 'o': {'NUMR'}, 'дцать': {'NUMR'},
                'надцать': {'NUMR'}}

SUFF_BY_POS = {
    POSTag.ADJF: {'ав', 'ощав', 'ив', 'лив', 'овлив', 'елив', 'члив', 'чив', 'ов', 'ов', 'ляв', 'ий', 'овий', 'ачий',
                  'ичий',
                  'енек', 'онек', 'ск', 'вск', 'евск', 'овск', 'еск', 'ческ', 'ическ', 'лезск', 'эзск', 'йск', 'ейск',
                  'ийск',
                  'имск', 'нск', 'анск', 'ианск', 'енск', 'инск', 'унск', 'тельск', 'ацк', 'ецк', 'усеньк', 'ошеньк',
                  'оньк',
                  'охоньк', 'як', 'л', 'овал', 'им', 'ом', 'н', 'н', 'ан', 'ебн', 'обн', 'евн', 'ивн', 'овн', 'ен',
                  'ён',
                  'яжн', 'езн', 'озн', 'иозн', 'ин', 'ин', 'нин', 'йн', 'ейн', 'нн', 'анн', 'ованн', 'ированн', 'енн',
                  'ённ',
                  'овенн', 'ственн', 'менн', 'онн', 'ионн', 'ационн', 'арн', 'орн', 'сн', 'ичн', 'очн', 'шн', 'шн',
                  'ашн',
                  'ашн', 'ишн', 'льн', 'альн', 'идальн', 'иальн', 'ональн', 'уальн', 'ельн', 'абельн', 'ибельн',
                  'тельн',
                  'ительн', 'ильн', 'т', 'ат', 'оват', 'чат', 'ит', 'овит', 'мент', 'аст', 'ист', 'ч', 'ач', 'нич',
                  'уч', 'ш',
                  'ш', 'айш', 'ейш', 'ащ', 'ущ', 'еющ'},
    POSTag.NOUN: ['б', 'об', 'ытьб', 'в', 'ев', 'ив', 'ив', 'ов', 'овь', 'тв', 'тв', 'ств', 'овств', 'еств', 'инств',
                  'тельств', 'аг', 'инг', 'ург', 'уг', 'ыг', 'д', 'ад', 'ад', 'иад', 'арад', 'оид', 'ядь', 'аж', 'ёж',
                  'ёжь',
                  'из', 'оз', 'атай', 'ей', 'алей', 'ачей', 'ий', 'арий', 'орий', 'тяй', 'к', 'к', 'к', 'к', 'ак',
                  'ак',
                  'чак', 'авк', 'овк', 'ловк', 'анек', 'ышек', 'ежк', 'ик', 'ик', 'ик', 'евик', 'ник', 'овник', 'еник',
                  'ейник', 'арник', 'атник', 'льник', 'истик', 'чик', 'щик', 'овщик', 'льщик', 'айк', 'ейк', 'лк',
                  'лк',
                  'анк', 'инк', 'онк', 'унк', 'ок', 'онок', 'чонок', 'ушок', 'ерк', 'урк', 'етк', 'отк', 'ютк', 'ук',
                  'чук',
                  'чк', 'ачк', 'ечк', 'ечк', 'ичка', 'очк', 'шк', 'шк', 'ашк', 'ёшк', 'ишк', 'ушк', 'ушк', 'ышк',
                  'ышк', 'ык',
                  'ульк', 'оньк', 'юк', 'няк', 'ль', 'л', 'л', 'л', 'ал', 'аль', 'ёл', 'ель', 'ел', 'тель', 'итель',
                  'ил',
                  'ол', 'оль', 'ол', 'ул', 'ул', 'ыль', 'изм', 'онизм', 'им', 'им', 'нь', 'н', 'н', 'н', 'н', 'н',
                  'ан', 'ан',
                  'уган', 'иан', 'овиан', 'лан', 'ман', 'овн', 'ень', 'ень', 'ён', 'мен', 'смен', 'знь', 'изн',
                  'овизн', 'ин',
                  'ин', 'ин', 'ин', 'бин', 'овин', 'лин', 'елин', 'анин', 'анин', 'жанин', 'ианин', 'чанин', 'овчанин',
                  'ичанин', 'инчанин', 'тянин', 'итянин', 'атин', 'чин', 'щин', 'овщин', 'льщин', 'он', 'он', 'и снь',
                  'снь', 'отн', 'ятн', 'ун', 'ун', 'иничн', 'ышн', 'льн', 'ынь', 'иян', 'ар', 'арь', 'ар', 'атарь',
                  'ер',
                  'онер', 'мейстер', 'up', 'ор', 'вор', 'тор', 'атор', 'итор', 'ур', 'тур', 'amyp', 'итур', 'ырь',
                  'яр', 'с',
                  'ис', 'анс', 'есс', 'ус', 'ариус', 'ть', 'am', 'ат', 'ат', 'иат', 'чат', 'евт', 'ет', 'ет', 'итет',
                  'ит',
                  'ит', 'нит', 'инит', 'ант', 'ент', 'амент', 'емент', 'от', 'оть', 'от', 'иот', 'ист', 'ость',
                  'имость',
                  'ность', 'нность', 'енность', 'тость', 'ут', 'х', 'ах', 'их', 'ох', 'ух', 'ух', 'ц', 'ц', 'ц', 'ец',
                  'ец',
                  'ец', 'авец', 'овец', 'лец', 'омец', 'нец', 'енец', 'инец', 'иц', 'овиц', 'лиц', 'ниц', 'овниц',
                  'ениц',
                  'атниц', 'униц', 'ичниц', 'очниц', 'ешниц', 'льниц', 'тельниц', 'льц', 'ч', 'ач', 'ич', 'евич',
                  'ович',
                  'ыч', 'аш', 'аш', 'аш', 'иш', 'ошь', 'ош', 'уш', 'оныш', 'ищ', 'ищ', 'бищ', 'овищ', 'лищ', 'еньк'],
    POSTag.VERB: {
        'а', 'я', 'ова', 'ева', 'ну', 'е', 'ен', 'ва', 'ива', 'ыва', 'из', 'ир', 'ич', 'ик', 'и', 'л'

    },
    POSTag.PRTF: {
        'active': {'ущ', 'ющ', 'ащ', 'ящ', 'вш', 'ш'},
        'passive': {
            'енн', 'ённ', 'нн', 'т', 'им', 'ем', 'ом'
        }

    },
    POSTag.PRTS: {'ен', 'н', 'т'},

    POSTag.GRND: {'а', 'я', 'вши', 'ши', 'в', 'учи', 'ючи'},

    POSTag.ADVB: {
        'е', 'ее', 'ше', "еньк", "жды", "мя", "вмя", "оват", "онечк", "оньк", "енечк", "охоньк",
        "ехоньк", "ёхоньк", "ешеньк", "ёшеньк"
    }

}

PAST_TENSE_VERB_SUFFIX = 'л'


def get_possible_suff_by_pos(pos, current_suff_list, has_posfix=None):
    """Получить возможные суффиксы по части речи"""
    if not current_suff_list:
        return get_service_suff_by_pos(pos, has_posfix)

    return get_ancestor_suff_by_pos(pos)


def get_ancestor_suff_by_pos(pos):
    """Получить служебные суффиксы слова-предка (для причастий и деепричастий)"""
    if pos in (POSTag.PRTF, POSTag.GRND):
        return SUFF_BY_POS[POSTag.VERB].difference({PAST_TENSE_VERB_SUFFIX})
    return SUFF_BY_POS.get(pos, [])


def get_service_suff_by_pos(pos, has_postfix=None):
    """Получить список служебных суффиксов текущей части речи"""
    if pos == POSTag.PRTF:
        suffixes = SUFF_BY_POS[pos]
        if has_postfix:
            return suffixes['active']
        return suffixes['active'].union(suffixes['passive'])
    return SUFF_BY_POS.get(pos, [])
