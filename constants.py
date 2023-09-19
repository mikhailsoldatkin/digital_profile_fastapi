from enum import unique, Enum, IntEnum

NO_DATA = 'Нет данных'
CACHE_TIME = 60 * 5

# Направленности программ
NATURAL = 1
SOCIAL = 2
TECH = 3
TRAVEL = 4
SPORT = 5
ART = 6

# Должности сотрудников
TEACHER = 2

PROGRAM_DIRECTIONS = {
    NATURAL: 'Естественнонаучная',
    SOCIAL: 'Социально-гуманитарная',
    TECH: 'Техническая',
    TRAVEL: 'Туристско-краеведческая',
    SPORT: 'Физкультурно-спортивная',
    ART: 'Художественная',
}

RF_CITIZEN = 1
DOUBLE_CITIZEN = 2
EXTERNAL_CITIZEN = 3
WITHOUT_CITIZEN = 4


CITIZENSHIP = {
    RF_CITIZEN: "Гражданин Российской Федерации",
    DOUBLE_CITIZEN: "Гражданин Российской Федерации и иностранного государства (двойное гражданство)",
    EXTERNAL_CITIZEN: "Иностранный гражданин",
    WITHOUT_CITIZEN: "Лицо без гражданства"
}

BIRTH_CERT = 1
PASSPORT = 2
DOC = 3
TEMP_CARD_IDENT_RF = 4
DOM_PERM_RF = 5
PASSPORT_ALIEN = 6
FOREIGN_PASSPORT = 7
ARMY_TICK = 8
DIP_PASS_RF = 11
PASSPORT_USSR = 13
PASSPORT_MINMOR = 15
PASSPORT_NAUTA = 16
TEMP_RF = 17
REFUGEE_RF = 18
BIRTH_CERT_INTR = 19
FROM_PRISON = 20
REFUGEE = 21
OFFICER = 22
MILLITARY_RF = 23
TEMP_MILLITARY = 24
WITHOUT_CITIZEN_RF = 25
DOC_CITIZEN_RF = 26
DOC_REFUGEE_RF = 27
DOC_TEMP_RF = 28
DOC_PERM_RF = 29
CERTIFICATE_PERM_RF = 30

DOC_TYPES = {
    BIRTH_CERT: 'Свидетельство о рождении',
    PASSPORT: 'Паспорт гражданина РФ',
    DOC: 'Другой документ, удостоверяющий личность',
    TEMP_CARD_IDENT_RF: 'Временное удостоверение личности гражданина РФ',
    PASSPORT_ALIEN: 'Паспорт иностранного гражданина',
    FOREIGN_PASSPORT: 'Загранпаспорт гражданина РФ',
    ARMY_TICK: 'Военный билет',
    DIP_PASS_RF: 'Дипломатический паспорт гражданина Российской Федерации',
    PASSPORT_USSR: 'Паспорт гражданина СССР',
    PASSPORT_MINMOR: 'Паспорт Минморфлота',
    PASSPORT_NAUTA: 'Паспорт моряка',
    TEMP_RF: 'Разрешение на временное проживание в Российской Федерации',
    REFUGEE_RF: 'Свидетельство о рассмотрении ходатайства о признании беженцем на территории Российской Федерации',
    BIRTH_CERT_INTR: 'Свидетельство о рождении, выданное уполномоченным органом иностранного государства',
    FROM_PRISON: 'Справка об освобождении из места лишения свободы',
    REFUGEE: 'Удостоверение личности лица, признанного беженцем',
    OFFICER: 'Удостоверение личности офицера',
    MILLITARY_RF: 'Удостоверение личности военнослужащего РФ',
    TEMP_MILLITARY: 'Временное удостоверение, выданное взамен военного билета',
    WITHOUT_CITIZEN_RF: 'Удостоверение личности лица без гражданства в РФ',
    DOC_CITIZEN_RF: 'Удостоверение личности отдельных категорий лиц, находящихся на территории РФ, подавших заявление о признании гражданами РФ или о приеме в гражданство РФ',
    DOC_REFUGEE_RF: 'Удостоверение личности лица, ходатайствующего о признании беженцем на территории РФ',
    DOC_TEMP_RF: 'Удостоверение личности лица, получившего временное убежище на территории РФ',
    DOC_PERM_RF: 'Вид на жительство в Российской Федерации',
    CERTIFICATE_PERM_RF: 'Свидетельство о предоставлении временного убежища на территории Российской Федерации',
}

PHONE = 1
FAX = 2
EMAIL = 3
WEBSITE = 4

CONTACT_TYPE_CHOICES = (
    (PHONE, 'Телефон'),
    (FAX, 'Факс'),
    (EMAIL, 'E-mail'),
    (WEBSITE, 'Сайт'),
)

# Группы здоровья
HEALTHY = 11
SLIGHT_DEVIATIONS = 12
CHRONIC_DISEASES_AND_WELLNESS = 13
CHRONIC_DISEASES_AND_POOR_HEALTH = 14
CHRONIC_DISEASE_AND_OBSERVED = 15
FIRST_GROUP_18_YEARS_OLD = 16
SECOND_GROUP_18_YEARS_OLD = 17
THIRD_GROUP_18_YEARS_OLD = 18

HEALTH_GROUPS = {
    HEALTHY: "Группа 1 - здоровые",
    SLIGHT_DEVIATIONS: "Группа 2 - с незначительными отклонениями",
    CHRONIC_DISEASES_AND_WELLNESS: "Группа 3 - с хроническими заболеваниями и хорошим самочувствием, либо с временными отклонениями в состоянии здоровья",
    CHRONIC_DISEASES_AND_POOR_HEALTH: "Группа 4 - с хроническими заболеваниями и плохим самочувствием",
    CHRONIC_DISEASE_AND_OBSERVED: "Группа 5 - с хроническими заболеваниями и наблюдаются в специальных лечебницах",
    FIRST_GROUP_18_YEARS_OLD: 'Группа 1 (18 лет и старше)',
    SECOND_GROUP_18_YEARS_OLD: 'Группа 2 (18 лет и старше)',
    THIRD_GROUP_18_YEARS_OLD: 'Группа 3 (18 лет и старше)',
}

# Трудные жизненные ситуации
DISABILITY = 2
LIMITED_ABILITIES = 3
DEAF = 301
BLINDLY = 302
MUTE = 303
IMMOBILIZE = 304
PARALYSIS = 305
INTELLIGENT_VIOLATION = 306
AUTISTIC = 307
IMPAIRED_MENTAL = 308
MENTAL_ILLNESS = 309
NERVOUS_SYSTEM_DISEASE = 310
COMPLEX_DEFECTS = 311

DIFFICULT_SITUATIONS = {
    101: "Дети, оставшиеся без попечения родителей по причине смерти родителей",
    102: "Дети, оставшиеся без попечения родителей по причине лишения родителей родительских прав",
    103: "Дети, оставшиеся без попечения родителей по причине ограничения родителей в родительских правах",
    104: "Дети, оставшиеся без попечения родителей по причине признания родителей недееспособными",
    105: "Дети, оставшиеся без попечения родителей по причине болезни родителей",
    106: "Дети, оставшиеся без попечения родителей по причине длительного отсутствия родителей",
    DISABILITY: "Дети-инвалиды",
    LIMITED_ABILITIES: "Дети с ограниченными возможностями здоровья",
    DEAF: "Дети с нарушениями слуха",
    BLINDLY: "Дети с нарушениями зрения",
    MUTE: "Дети с тяжелыми нарушениями речи",
    IMMOBILIZE: "Дети с нарушением опорно-двигательного аппарата",
    PARALYSIS: "Дети с детским церебральным параличом",
    INTELLIGENT_VIOLATION: "Дети с интеллектуальными нарушениями",
    AUTISTIC: "Дети с расстройством аутистического спектра",
    IMPAIRED_MENTAL: "Дети с задержкой психического развития",
    MENTAL_ILLNESS: "Дети с психическими заболеваниями",
    NERVOUS_SYSTEM_DISEASE: "Дети с заболеваниями нервной системы",
    COMPLEX_DEFECTS: "Дети со сложной структурой дефекта",
    4: "Дети - жертвы вооруженных и межнациональных конфликтов, экологических и техногенных катастроф, стихийных бедствий",
    5: "Дети - жертвы экологических и техногенных катастроф, стихийных бедствий",
    6: "Дети из семей беженцев и вынужденных переселенцев",
    7: "Дети, оказавшиеся в экстремальных условиях",
    8: "Дети - жертвы насилия",
    9: "Дети, отбывающие наказание в виде лишения свободы в воспитательных колониях",
    10: "Дети, с девиантным (общественно опасным) поведением",
    11: "Дети, проживающие в малоимущих семьях",
    12: "Дети с отклонениями в поведении",
    13: "Дети, жизнедеятельность которых объективно нарушена в результате сложившихся обстоятельств",
}

# Группы инвалидности
FIRST_GROUP = 11
SECOND_GROUP = 12
THIRD_GROUP = 13
DISABLED_CHILD = 14

DISABILITY_GROUPS = {
    FIRST_GROUP: "Первая группа",
    SECOND_GROUP: "Вторая группа",
    THIRD_GROUP: "Третья группа",
    DISABLED_CHILD: "Ребенок-инвалид (для лиц до 18 лет)"
}

DISABLED_SINCE_CHILDHOOD = 21
ARMY_INVALID = 22

DISABILITY_REASONS = {
    DISABLED_SINCE_CHILDHOOD: "Инвалид с детства",
    ARMY_INVALID: "Инвалид вследствие военной травмы или заболевания, полученного в период прохождения военной службы"
}

HALF_BLIND = 201
BLIND = 202
HALF_DEAF = 203
DEAF = 204
HALF_DEAF_HARD = 205
WEAK = 206
SPEECH_PATHOLOGY = 207
DELAYED = 208
RETARDED = 209
RETARDED_HARD = 210
OTHER = 211
AUTISTIC_DISORDER = 212

ADAPTATION_TYPES = {
    HALF_BLIND: "для слабовидящих обучающихся",
    BLIND: "для слепых обучающихся",
    HALF_DEAF: "для слабослышащих",
    DEAF: "для глухих",
    HALF_DEAF_HARD: "для слабослышащих обучающихся, имеющих сложную структуру дефекта (нарушение слуха и задержка психического развития)",
    WEAK: "для обучающихся, имеющих нарушения опорно-двигательного аппарата",
    SPEECH_PATHOLOGY: "для обучающихся, имеющих тяжелые нарушения речи",
    DELAYED: "для обучающихся с задержкой психического развития",
    RETARDED: "для обучающихся с умственной отсталостью",
    RETARDED_HARD: "для обучающихся с умственной отсталостью, имеющих сложную структуру дефекта",
    OTHER: "для обучающихся с иными ограничениями здоровья",
    AUTISTIC_DISORDER: "для обучающихся с расстройствами аутистического спектра",
}

IS_HOME_STUDY = 1
IS_MED_ORG_STUDY = 2
IS_HEALING_ORG_STUDY = 3

LONG_TERM_TREATMENT = {
    IS_HOME_STUDY: 'Обучение на дому',
    IS_MED_ORG_STUDY: 'Обучение в медицинской организации',
    IS_HEALING_ORG_STUDY: 'Обучение в организации, осуществляющей лечение, оздоровление и (или) отдых',
}

PROGRAM_TERM_REALIZATIONS = {
    1: 'краткосрочная',
    2: 'от 1 до 3 лет',
    3: 'до 1 года',
    4: 'от 3 и более лет'
}

PROGRAM_ADAPTATION_TYPES = {
    1: 'Для слабовидящих обучающихся',
    2: 'Для слепых обучающихся',
    3: 'Для глухих',
    4: 'Для слабослышащих обучающихся, имеющих сложную структуру дефекта (нарушение слуха и задержка психического развития)',
    5: 'Для обучающихся, имеющих нарушения опорно-двигательного аппарата',
    6: 'Для обучающихся, имеющих тяжелые нарушения речи',
    7: 'Для обучающихся с задержкой психического развития',
    8: 'Для обучающихся с умственной отсталостью',
    9: 'Для обучающихся с умственной отсталостью, имеющих сложную структуру дефекта',
    10: 'Для обучающихся с иными ограничениями здоровья'
}

PROGRAM_TYPES = {
    1: 'Типовая',
    2: 'Модифицированная',
    3: 'Адаптированная',
    4: 'Экспериментальная',
    5: 'Авторская',
}

PROGRAM_KINDS = {
    1: 'Дополнительные общеразвивающие программы',
    2: 'Дополнительные предпрофессиональные программы',
    3: 'Программы спортивной подготовки',
    4: 'Образовательные программы дошкольного образования',
    5: 'Программы профессиональной подготовки по профессиям рабочих, должностям служащих',
    6: 'Программы переподготовки рабочих, служащих',
    7: 'Программы повышения квалификации рабочих, служащих'
}

EDU_DOCUMENT_TYPE = {
    1: 'Справка об обучении',
    2: 'Свидетельство об обучении',
    3: 'Свидетельство об освоении предпрофессиональной программы в области искусств'
}

EXPEL_REASONS = {
    1: 'Изменение места жительства/Перевод в другое ОДО',
    2: 'Достижение 18 лет',
    3: 'В связи с окончанием ОДО',
    4: 'Изменение интересов обучающегося',
    5: 'Недостаток свободного времени',
    6: 'Переход в специальные (коррекционные) ОДО и группы для детей с ограниченными возможностями здоровья',
    7: 'Исключение за недостойное поведение',
    8: 'На основании медицинского заключения о состоянии здоровья; препятствующего дальнейшему обучению в ОДО',
    9: 'Переход в специальные учебно-воспитательные организации и воспитательно-трудовые колонии',
    10: 'Отчислен за неуспеваемость, систематические пропуски занятий',
    11: 'Систематические нарушения дисциплины',
    12: 'Призыв в Армию',
    13: 'Другие причины',
    14: 'По причине смерти обучающегося',
    15: 'Отчислен в связи с задолженностью по оплате',
}

RELATION_TYPES = {
    1: 'Родитель',
    2: 'Опекун',
    3: 'Попечитель',
    4: 'Орган опеки и попечительства',
    5: 'Приемный родитель',
    6: 'Руководитель воспитательной, лечебной и иной организации, в которой ребенок находится на полном государственном обеспечении'
}

RELATIONS = {
    1: 'Муж',
    2: 'Жена',
    3: 'Отец',
    4: 'Мать',
    5: 'Сын',
    6: 'Дочь',
    7: 'Дедушка',
    8: 'Бабушка',
    9: 'Внук',
    10: 'Внучка',
    11: 'Брат',
    12: 'Сестра',
    13: 'Отчим',
    14: 'Мачеха',
    15: 'Пасынок',
    16: 'Падчерица',
    17: 'Тесть',
    18: 'Теща',
    19: 'Свекор',
    20: 'Свекровь',
    21: 'Зять',
    22: 'Невестка (сноха)',
    23: 'Другая степень родства, свойства',
}

NO_EDUCATION = 1
EDUCATION_SECONDARY = 2
SECONDARY_VOCATIONAL = 3
HIGHER_INCOMPLETE = 4
BACHELOR_DEGREE = 5
EDUCATION_HIGHER = 6
HIGHEST_QUALIFICATION = 7
PRIMARY_PROFESSIONAL = 8

EDUCATION_TYPES = (
    (NO_EDUCATION, 'Нет'),
    (EDUCATION_SECONDARY, 'Среднее общее'),
    (SECONDARY_VOCATIONAL, 'Среднее профессиональное'),
    (HIGHER_INCOMPLETE, 'Неполное высшее'),
    (BACHELOR_DEGREE, 'Высшее образование - бакалавриат'),
    (EDUCATION_HIGHER, 'Высшее образование - специалитет, магистратура'),
    (HIGHEST_QUALIFICATION, 'Высшее образование - подготовка кадров высшей квалификации'),
    (PRIMARY_PROFESSIONAL, 'Начальное профессиональное'),
)

NO_DEGREE = 1
CANDIDATE = 2
PROFESSOR = 3

DEGREE_TYPES = (
    (NO_DEGREE, 'Нет степени'),
    (CANDIDATE, 'Кандидат'),
    (PROFESSOR, 'Доктор'),
)

NO_QUALIFICATION = 1
QUALIFICATION_FIRST_CATEGORY = 2
QUALIFICATION_SECOND_CATEGORY = 3
QUALIFICATION_HIGHEST_CATEGORY = 4
SUITABILITY_FOR_THE_POSITION = 5

QUALIFICATION_CATEGORIES = (
    (NO_QUALIFICATION, 'нет'),
    (QUALIFICATION_FIRST_CATEGORY, 'первая'),
    (QUALIFICATION_HIGHEST_CATEGORY, 'высшая'),
    (SUITABILITY_FOR_THE_POSITION, 'Соответствие на занимаемую должность')
)

INTERNET_NO = 1
INTERNET_MODEM = 2
INTERNET_LINE = 3
INTERNET_SATELLITE = 4

INTERNET_CHOICES = (
    (INTERNET_NO, 'Нет'),
    (INTERNET_MODEM, 'Модем'),
    (INTERNET_LINE, 'Выделенная линия'),
    (INTERNET_SATELLITE, 'Спутниковый')
)

DECLARATION_STATUS_REGISTERED = 2

DECLARATION_SOURCE_PORTAL = 1
DECLARATION_SOURCE_PERSONAL = 2
DECLARATION_SOURCE_MOBILEAPP = 4
DECLARATION_SOURCE_NAVIGATOR = 3
DECLARATION_SOURCE_EPGU = 5

DECLARATION_SOURCE_CHOICES = (
    (DECLARATION_SOURCE_PORTAL, 'from_portal'),
    (DECLARATION_SOURCE_PERSONAL, 'personal'),
    (DECLARATION_SOURCE_MOBILEAPP, 'from_mobile_app'),
)

MINISTRY = 1
ADMINISTRATION = 2
SCHOOL = 3

UNIT_TYPES = {
    MINISTRY: 'Министерство',
    ADMINISTRATION: 'Администрация',
    SCHOOL: 'Образовательная организация',
}

ADDITIONAL_EDU_ORGANIZATION = 1
GENERAL_EDU_ORGANIZATION = 2
PRESCHOOL_EDUCATIONAL_ORGANIZATION = 3

ADDRESS_TYPE_ACTUAL = 1
ADDRESS_TYPE_LEGAL = 2

ADDRESS_TYPE_CHOICES = (
    (ADDRESS_TYPE_ACTUAL, 'Фактический'),
    (ADDRESS_TYPE_LEGAL, 'Юридический'),
)

# статусы организации
FUNCTIONING = 1
CAPITAL_REPAIR = 2
RECONSTRUCTION = 3
ACTIVITY_STOPPED = 4
CONTINGENT_MISSING = 5
PENDING_THE_OPENING = 6
LIQUIDATED = 7
CLOSED = 8
JOINED_OTHER_ORGANIZATIONS = 9

UNIT_STATUS_CHOICES = (
    (FUNCTIONING, "Функционирует"),
    (CAPITAL_REPAIR, "Капитальный ремонт"),
    (RECONSTRUCTION, "Реконструкция"),
    (ACTIVITY_STOPPED, "Деятельность приостановлена"),
    (CONTINGENT_MISSING, "Контингент отсутствует"),
    (PENDING_THE_OPENING, "Ожидает открытия"),
    (LIQUIDATED, "Ликвидирована"),
    (CLOSED, "Закрыта"),
    (JOINED_OTHER_ORGANIZATIONS, "Присоединена к другой организации")
)

CITY = 1
RURAL = 2

AREA_TYPES = (
    (CITY, 'городская'),
    (RURAL, 'сельская'),
)

DOC_TYPE_OTHER = 1
DOC_TYPE_LICENSE = 2
DOC_TYPE_CHARTER = 3
DOC_TYPE_EXCERPT = 4

DOC_TYPE_CHOICES = (
    (DOC_TYPE_OTHER, 'Иные документы'),
    (DOC_TYPE_LICENSE, 'Лицензия'),
    (DOC_TYPE_CHARTER, 'Устав'),
    (DOC_TYPE_EXCERPT, 'Выписка из ЕГРЮЛ/ЕГРИП'),
)
