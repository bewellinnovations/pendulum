from .custom import translations as custom_translations


"""
ar locale file.

It has been generated automatically and must not be modified directly.
"""


locale = {
    'plural': lambda n: 'few' if ((n % 100) == (n % 100) and (((n % 100) >= 3 and (n % 100) <= 10))) else 'many' if ((n % 100) == (n % 100) and (((n % 100) >= 11 and (n % 100) <= 99))) else 'one' if (n == n and ((n == 1))) else 'two' if (n == n and ((n == 2))) else 'zero' if (n == n and ((n == 0))) else 'other',
    'ordinal': lambda n: 'other',
    'translations': {
        'days': {
            'abbreviated': {
                0: 'الأحد',
                1: 'الاثنين',
                2: 'الثلاثاء',
                3: 'الأربعاء',
                4: 'الخميس',
                5: 'الجمعة',
                6: 'السبت',
            },
            'narrow': {
                0: 'ح',
                1: 'ن',
                2: 'ث',
                3: 'ر',
                4: 'خ',
                5: 'ج',
                6: 'س',
            },
            'short': {
                0: 'أحد',
                1: 'إثنين',
                2: 'ثلاثاء',
                3: 'أربعاء',
                4: 'خميس',
                5: 'جمعة',
                6: 'سبت',
            },
            'wide': {
                0: 'الأحد',
                1: 'الاثنين',
                2: 'الثلاثاء',
                3: 'الأربعاء',
                4: 'الخميس',
                5: 'الجمعة',
                6: 'السبت',
            },
        },
        'months': {
            'abbreviated': {
                1: 'يناير',
                2: 'فبراير',
                3: 'مارس',
                4: 'أبريل',
                5: 'مايو',
                6: 'يونيو',
                7: 'يوليو',
                8: 'أغسطس',
                9: 'سبتمبر',
                10: 'أكتوبر',
                11: 'نوفمبر',
                12: 'ديسمبر',
            },
            'narrow': {
                1: 'ي',
                2: 'ف',
                3: 'م',
                4: 'أ',
                5: 'و',
                6: 'ن',
                7: 'ل',
                8: 'غ',
                9: 'س',
                10: 'ك',
                11: 'ب',
                12: 'د',
            },
            'wide': {
                1: 'يناير',
                2: 'فبراير',
                3: 'مارس',
                4: 'أبريل',
                5: 'مايو',
                6: 'يونيو',
                7: 'يوليو',
                8: 'أغسطس',
                9: 'سبتمبر',
                10: 'أكتوبر',
                11: 'نوفمبر',
                12: 'ديسمبر',
            },
        },
        'units': {
            'year': {
                'zero': '{0} سنة',
                'one': 'سنة',
                'two': 'سنتان',
                'few': '{0} سنوات',
                'many': '{0} سنة',
                'other': '{0} سنة',
            },
            'month': {
                'zero': '{0} شهر',
                'one': 'شهر',
                'two': 'شهران',
                'few': '{0} أشهر',
                'many': '{0} شهرًا',
                'other': '{0} شهر',
            },
            'week': {
                'zero': '{0} أسبوع',
                'one': 'أسبوع',
                'two': 'أسبوعان',
                'few': '{0} أسابيع',
                'many': '{0} أسبوعًا',
                'other': '{0} أسبوع',
            },
            'day': {
                'zero': '{0} يوم',
                'one': 'يوم',
                'two': 'يومان',
                'few': '{0} أيام',
                'many': '{0} يومًا',
                'other': '{0} يوم',
            },
            'hour': {
                'zero': '{0} ساعة',
                'one': 'ساعة',
                'two': 'ساعتان',
                'few': '{0} ساعات',
                'many': '{0} ساعة',
                'other': '{0} ساعة',
            },
            'minute': {
                'zero': '{0} دقيقة',
                'one': 'دقيقة',
                'two': 'دقيقتان',
                'few': '{0} دقائق',
                'many': '{0} دقيقة',
                'other': '{0} دقيقة',
            },
            'second': {
                'zero': '{0} ثانية',
                'one': 'ثانية',
                'two': 'ثانيتان',
                'few': '{0} ثوان',
                'many': '{0} ثانية',
                'other': '{0} ثانية',
            },
            'microsecond': {
                'zero': '{0} ميكروثانية',
                'one': '{0} ميكروثانية',
                'two': '{0} ميكروثانية',
                'few': '{0} ميكروثانية',
                'many': '{0} ميكروثانية',
                'other': '{0} ميكروثانية',
            },
        },
        'relative': {
            'year': {
                'future': {
                    'other': 'خلال {0} سنة',
                    'zero': 'خلال {0} سنة',
                    'one': 'خلال سنة واحدة',
                    'two': 'خلال سنتين',
                    'few': 'خلال {0} سنوات',
                    'many': 'خلال {0} سنة',
                },
                'past': {
                    'other': 'قبل {0} سنة',
                    'zero': 'قبل {0} سنة',
                    'one': 'قبل سنة واحدة',
                    'two': 'قبل سنتين',
                    'few': 'قبل {0} سنوات',
                    'many': 'قبل {0} سنة',
                },
            },
            'month': {
                'future': {
                    'other': 'خلال {0} شهر',
                    'zero': 'خلال {0} شهر',
                    'one': 'خلال شهر واحد',
                    'two': 'خلال شهرين',
                    'few': 'خلال {0} أشهر',
                    'many': 'خلال {0} شهرًا',
                },
                'past': {
                    'other': 'قبل {0} شهر',
                    'zero': 'قبل {0} شهر',
                    'one': 'قبل شهر واحد',
                    'two': 'قبل شهرين',
                    'few': 'قبل {0} أشهر',
                    'many': 'قبل {0} شهرًا',
                },
            },
            'week': {
                'future': {
                    'other': 'خلال {0} أسبوع',
                    'zero': 'خلال {0} أسبوع',
                    'one': 'خلال أسبوع واحد',
                    'two': 'خلال أسبوعين',
                    'few': 'خلال {0} أسابيع',
                    'many': 'خلال {0} أسبوعًا',
                },
                'past': {
                    'other': 'قبل {0} أسبوع',
                    'zero': 'قبل {0} أسبوع',
                    'one': 'قبل أسبوع واحد',
                    'two': 'قبل أسبوعين',
                    'few': 'قبل {0} أسابيع',
                    'many': 'قبل {0} أسبوعًا',
                },
            },
            'day': {
                'future': {
                    'other': 'خلال {0} يوم',
                    'zero': 'خلال {0} يوم',
                    'one': 'خلال يوم واحد',
                    'two': 'خلال يومين',
                    'few': 'خلال {0} أيام',
                    'many': 'خلال {0} يومًا',
                },
                'past': {
                    'other': 'قبل {0} يوم',
                    'zero': 'قبل {0} يوم',
                    'one': 'قبل يوم واحد',
                    'two': 'قبل يومين',
                    'few': 'قبل {0} أيام',
                    'many': 'قبل {0} يومًا',
                },
            },
            'hour': {
                'future': {
                    'other': 'خلال {0} ساعة',
                    'zero': 'خلال {0} ساعة',
                    'one': 'خلال ساعة واحدة',
                    'two': 'خلال ساعتين',
                    'few': 'خلال {0} ساعات',
                    'many': 'خلال {0} ساعة',
                },
                'past': {
                    'other': 'قبل {0} ساعة',
                    'zero': 'قبل {0} ساعة',
                    'one': 'قبل ساعة واحدة',
                    'two': 'قبل ساعتين',
                    'few': 'قبل {0} ساعات',
                    'many': 'قبل {0} ساعة',
                },
            },
            'minute': {
                'future': {
                    'other': 'خلال {0} دقيقة',
                    'zero': 'خلال {0} دقيقة',
                    'one': 'خلال دقيقة واحدة',
                    'two': 'خلال دقيقتين',
                    'few': 'خلال {0} دقائق',
                    'many': 'خلال {0} دقيقة',
                },
                'past': {
                    'other': 'قبل {0} دقيقة',
                    'zero': 'قبل {0} دقيقة',
                    'one': 'قبل دقيقة واحدة',
                    'two': 'قبل دقيقتين',
                    'few': 'قبل {0} دقائق',
                    'many': 'قبل {0} دقيقة',
                },
            },
            'second': {
                'future': {
                    'other': 'خلال {0} ثانية',
                    'zero': 'خلال {0} ثانية',
                    'one': 'خلال ثانية واحدة',
                    'two': 'خلال ثانيتين',
                    'few': 'خلال {0} ثوانٍ',
                    'many': 'خلال {0} ثانية',
                },
                'past': {
                    'other': 'قبل {0} ثانية',
                    'zero': 'قبل {0} ثانية',
                    'one': 'قبل ثانية واحدة',
                    'two': 'قبل ثانيتين',
                    'few': 'قبل {0} ثوانِ',
                    'many': 'قبل {0} ثانية',
                },
            },
        },
        'day_periods': {
            'am': 'ص',
            'pm': 'م',
            'morning1': 'فجرًا',
            'morning2': 'صباحًا',
            'afternoon1': 'ظهرًا',
            'afternoon2': 'بعد الظهر',
            'evening1': 'مساءً',
            'night1': 'منتصف الليل',
            'night2': 'ليلاً',
        },
    },
    'custom': custom_translations
}