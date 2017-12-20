import random

def pick(facts):
    if isinstance(facts, str):
        return facts
    if isinstance(facts, list):
        return ' '.join(pick(fact) for fact in facts)
    if isinstance(facts, tuple):
        return pick(random.choice(facts))
    assert(False)

facts = [
    'Did you know that',
    (
        [ 'the', ( 'fall', 'spring' ), 'equinox' ],
        [ 'the', ( 'winter', 'summer' ), ( 'solstice', 'Olympics' ) ],
        [ 'the', ( 'earliest', 'latest' ), ( 'sunrise', 'sunset' ) ],
        [ 'daylight', ( 'saving', 'savings' ), 'time' ],
        [ 'leap', ( 'day', 'year' ) ],
        'Easter',
        [ 'the', ( 'harvest', 'supert', 'blood' ), 'moon' ],
        'Toyota truck month',
        'shark week'
    ),
    (
        [ 'happens', ( 'earlier', 'later', 'at the wrong time' ), 'every year' ],
        [
            'drifts out of sync with the',
            (
                'sun',
                'moon',
                'zodiac',
                [
                    (
                        'Gregorian',
                        'Mayan',
                        'lunar',
                        'iPhone'
                    ),
                    'calendar'
                ],
                'atomic clock in Colorado'
            )
        ],
        [ 'might', ( 'not happen', 'happen twice' ), 'this year' ]
    ),
    'because of',
    (
        [ 'time zone legislation in', ( 'Indiana?', 'Arizona?', 'Russia?' ) ],
        'a decree by the Pope in the 1500s?',
        [
            (
                'precession',
                'libration',
                'nutation',
                'libation',
                'eccentricity',
                'obliquity'
            ),
            'of the',
            (
                'moon?',
                'sun?',
                'Earth\'s axis?',
                'equator?',
                'prime meridian?',
                [ ( 'international date', 'Mason-Dixon' ), 'line?' ]
            )
        ],
        'magnetic field reversal?',
        [
            'an arbitrary decision by',
            (
                'Benjamin Franklin?',
                'Isaac Newton?',
                'FDR?'
            )
        ]
    ),
    'Apparently',
    (
        'it causes a predictable increase in car accidents.',
        'that\'s why we have leap seconds.',
        'scientists are really worried.',
        [
            'it was even more extreme during the',
            (
                'Bronze Age.',
                'Ice Age.',
                'Cretaceous.',
                '1990s.'
            )
        ],
        [
            'there\'s a proposal to fix it, but it',
            (
                'will never happen.',
                'actually makes things worse.',
                'is stalled in Congress.',
                'might be unconstitutional.'
            )
        ],
        'it\'s getting worse and no one knows why.'
    )
]

fact = pick(facts)

print(fact)
