from collections.abc import Sequence


nested = [1, 2, (3,
                 [4,
                  [5,
                   [6,
                    [11, 12,
                     [13,
                      [14,
                       [15,
                        [-1, -5]
                        ]
                       ]
                      ]
                     ]
                    ], 9]
                  ],
                 10),
          [8,
           [7]
           ]
          ]


def sum_recursive(arr):
    flat_sum = sum(i for i in arr if not isinstance(i, Sequence))
    nested_list = [sum_recursive(i) for i in arr if isinstance(i, Sequence)]
    return sum(nested_list) + flat_sum


def flatten_recursive(arr):
    flat = [i for i in arr if not isinstance(i, Sequence)]
    [flat.extend(flatten_recursive(i)) for i in arr if isinstance(i, Sequence)]
    return flat


def min_recursive(arr):
    m = min(i for i in arr if not isinstance(i, Sequence))
    mm = [min_recursive(i) for i in arr if isinstance(i, Sequence)]
    return min(m, mm[0]) if mm else m


def max_recursive(arr):
    m = max(i for i in arr if not isinstance(i, Sequence))
    mm = [max_recursive(i) for i in arr if isinstance(i, Sequence)]
    return max(m, mm[0]) if mm else m


max_res = max_recursive(nested)
print(max_res)
