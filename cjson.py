from json import dump as jdump
ordb = {
    'converts': {
        'binary': [
            [
                "int->bin",
                "bc.intToBin({})"
            ],
            [
                "bin->int",
                "bc.binToInt('{}')"
            ]
        ],

        'IPv4': [
            [
                "toBinary",
                "ipc.IPv4ToIPv4B('{}')"
            ],
            [
                "toDecimal",
                "ipc.IPv4BToIPv4('{}')"
            ],
            [
                "getClass",
                "ipc.getClass('{}')"
            ]
        ],

        'other': [
            [
                "gb->mb",
                "{} * 1024"
            ],
            [
                "randint",
                "randint(0, {})"
            ]
        ]
    },

    'previous': [
        'convert',
        0,
        0
    ]
}
with open('conf.json', 'w', encoding='UTF-8') as f:
    jdump(ordb, f)
    f.close()
