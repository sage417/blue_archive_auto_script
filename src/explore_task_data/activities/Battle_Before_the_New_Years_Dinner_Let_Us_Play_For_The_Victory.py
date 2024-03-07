stage_data = {
    "challenge2_sss": {
        'start': [
            ['burst1', (727, 300)],
            ['pierce1', (637, 224)]
        ],
        'action': [
            {'t': 'click', 'p': (521, 439), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (520, 277), 'ec': True, 'wait-over': True, "desc": "2 left"},

            {'t': 'exchange_and_click', 'p': (481, 384), 'ec': True, "desc": "2 lower left"},
            {'t': 'choose_and_change', 'p': (497, 384), "desc": "swap 1 2"},
            {'t': 'click', 'p': (376, 386), 'wait-over': True, "desc": "1 left"},

            {'t': 'click', 'p': (434, 476), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (884, 404), 'ec': True, 'wait-over': True, "desc": "2 right"},

            {'t': 'click', 'p': (553, 482), 'ec': True, "desc": "1 lower right"},
            {'t': 'click', 'p': (847, 473), 'ec': True, 'wait-over': True, "desc": "2 lower right"},

            {'t': 'exchange_and_click', 'p': (724, 461), 'ec': True, "desc": "2 lower left"},
            {'t': 'click', 'p': (554, 464), "desc": "1 lower right"},

        ]
    },
    "challenge2_task": {
        'start': [
            ['burst1', (727, 300)],
            ['pierce1', (637, 224)]
        ],
        'action': [
            {'t': 'click', 'p': (521, 439), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (520, 277), 'ec': True, 'wait-over': True, "desc": "2 left"},

            {'t': 'exchange_and_click', 'p': (481, 384), 'ec': True, "desc": "2 lower left"},
            {'t': 'choose_and_change', 'p': (497, 384), "desc": "swap 1 2"},
            {'t': 'click', 'p': (376, 386), 'wait-over': True, "desc": "1 left"},

            {'t': 'click', 'p': (434, 476), 'ec': True, "desc": "1 lower left"},
            {'t': 'end-turn'},

            {'t': 'click', 'p': (553, 482), 'ec': True, "desc": "1 lower right"},
            {'t': 'end-turn'},

            {'t': 'click', 'p': (656, 477), "desc": "1 lower right"},

        ]
    },
    "challenge4_sss": {
        'start': [
            ['burst1', (517, 428)],
            ['burst2', (712, 180)],
            ['pierce1', (992, 712)]
        ],
        'action': [
            {'t': 'click_and_teleport', 'p': (439, 440), 'ec': True, "desc": "1 lower left and tp"},
            {'t': 'choose_and_change', 'p': (718, 356), "desc": "swap 1 2"},
            {'t': 'click', 'p': (836, 354), 'ec': True, "desc": "2 right"},
            {'t': 'click', 'p': (601, 491), 'ec': True, 'wait-over': True, "desc": "3 left"},

            {'t': ['exchange', 'click_and_teleport'], 'p': (695, 410), 'wait-over': True, "desc": "2 choose self and tp"},
            {'t': 'click', 'p': (715, 455), 'ec': True, "desc": "2 right"},
            {'t': ['exchange_twice', 'choose_and_change'], 'p': (644, 411), "desc": "swap 2 3"},
            {'t': 'click', 'p': (701, 335), 'ec': True, "desc": "3 upper right"},
            {'t': 'click', 'p': (482, 280), 'wait-over': True, "desc": "1 left"},

            {'t': ['exchange', 'click_and_teleport'], 'p': (790, 398), 'ec': True, "desc": "2 upper right and tp"},
            {'t': 'choose_and_change', 'p': (529, 267), "desc": "swap 1 2"},
            {'t': 'click', 'p': (487, 384), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (823, 366), 'ec': True, 'wait-over': True, "desc": "3 upper right"},

            {'t': 'click', 'p': (503, 512), 'ec': True, "desc": "1 lower left"},
            {'t': 'exchange_and_click', 'p': (706, 254), 'ec': True, "desc": "3 upper left"},
            {'t': 'choose_and_change', 'p': (685, 280), "desc": "swap 2 3"},
            {'t': 'click', 'p': (743, 198), 'ec': True, 'wait-over': True, "desc": "2 upper right"},

            {'t': 'exchange_twice_and_click', 'p': (548, 553), 'ec': True, "desc": "3 lower left"},
            {'t': ['exchange', 'click_and_teleport'], 'p': (728, 300), 'wait-over': True, "desc": "2 choose self and tp"},
            {'t': 'click', 'p': (518, 365), 'ec': True, "desc": "2 upper left"},
            {'t': 'click', 'p': (521, 277), "desc": "1 left"},
        ]
    },
    "challenge4_task": {
        'start': [
            ['burst1', (695, 192)],
            ['pierce1', (992, 712)]
        ],
        'action': [
            {'t': 'exchange_and_click', 'p': (592, 492), 'ec': True, "desc": "2 left"},
            {'t': 'end-turn'},

            {'t': 'exchange_and_click', 'p': (626, 419), 'ec': True, "desc": "2 upper left"},
            {'t': 'click', 'p': (473, 281), 'wait-over': True, "desc": "1 left"},

            {'t': 'click', 'p': (403, 320), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (770, 408), 'ec': True, 'wait-over': True, "desc": "2 upper right"},

            {'t': 'click', 'p': (580, 404), 'ec': True, "desc": "1 lower left"},
            {'t': 'end-turn'},

            {'t': 'click', 'p': (445, 431), 'ec': True, "desc": "1 lower left"},
            {'t': 'end-turn'},

            {'t': 'click', 'p': (379, 377), "desc": "1 left"},
        ]
    }
}
