def site_info():
    return {'401012': {'name': 'Murray River at Bigarra', 'lat': -36.319170, 'long': 148.051976, 'state': 'Victoria'},
        '401027': {'name': 'Murray River at Hume Dam', 'lat': -36.088037, 'long': 147.054394, 'state': 'NSW'},
        '409017': {'name': 'Murray River at Doctors Point', 'lat': -36.112871, 'long': 146.940113, 'state': 'NSW'},
        '425007': {'name': 'Darling River at Burtundy', 'lat': -33.746852, 'long': 142.266151, 'state': 'NSW'},
        '409001': {'name': 'Murray River at Albury (Union Bridge)', 'lat': -36.091367, 'long': 146.906928, 'state': 'NSW'},
        '410130': {'name': 'Murrumbidgee River at Balranald', 'lat': -34.664975, 'long': 143.491246, 'state': 'NSW'},
        '401549': {'name': 'Murray River at Bringenbrong Bridge', 'lat': -36.167919, 'long': 148.026249, 'state': 'Victoria'},
        '401211': {'name': 'Mitta Mitta River at Colemans', 'lat': -36.531381, 'long': 147.457739, 'state': 'NSW'},
        '41310022': {'name': 'Murray River at Colignan', 'lat': -34.567142, 'long': 142.406710, 'state': 'Victoria'},
        '409002': {'name': 'Murray River at Corowa', 'lat': -36.007022, 'long': 146.395029, 'state': 'NSW'},
        '401224A': {'name': 'Mitta Mirra River at Dartmouth Dam', 'lat': -36.556936, 'long': 147.529824, 'state': 'Victoria'},
        '409008': {'name': 'Edward River at Offtake', 'lat': -35.847738, 'long': 144.998120, 'state': 'NSW'},
        '409030': {'name': 'Gulpa Creek River at Offtake', 'lat': -35.848924, 'long': 144.988111, 'state': 'NSW'},
        '401013': {'name': 'Jingellic Creek at Jingellic', 'lat': -35.931540, 'long': 147.712355, 'state': 'NSW'},
        '409029': {'name': 'Mulwala Canal escape at Edwards River', 'lat': -35.564413, 'long': 145.008214, 'state': 'NSW'},
        '401014': {'name': 'Tooma River at Pinegrove', 'lat': -36.040152, 'long': 148.053198, 'state': 'NSW'},
        '41310025': {'name': 'Murray River at Redcliffs', 'lat': -34.244487, 'long': 142.243199, 'state': 'Victoria'},
        '409013': {'name': 'Wakool River at Stoney Crossing', 'lat': -35.037290, 'long': 143.570309, 'state': 'NSW'},
        '409023': {'name': "Edward River at Downstream Steven's Weir", 'lat': -35.434131, 'long': 144.759256, 'state': 'NSW'},
        '409101': {'name': "Edward River at Upstream Steven's Weir", 'lat': -35.438355, 'long': 144.763345, 'state': 'NSW'},
        '409204C': {'name': 'Murray River at Swan Hill', 'lat': -35.327498, 'long': 143.564008, 'state': 'Victoria'},
        '401204A': {'name': 'Mitta Mitta River at Tallandoon', 'lat': -36.407273, 'long': 147.231146, 'state': 'Victoria'},
        '409202A': {'name': 'Murray River at Tocumwal', 'lat': -35.813464, 'long': 145.556602, 'state': 'NSW'},
        '425012': {'name': 'Darling River at Weir 32', 'lat': -32.435644, 'long': 142.379776, 'state': 'NSW'},
        '409025': {'name': 'Murray River at Yarrawonga Downstream', 'lat': -36.011973, 'long': 145.991437, 'state': 'Victoria'},
        '409216A': {'name': 'Murray River at Yarrawonga Upstream', 'lat': -36.008850, 'long': 146.000870, 'state': 'Victoria'},
    }



#MURRAY DARLING SITES
'''
401012 - Murray @ Bigarra - Level (m), D.O., Discharge (ML/d), EC @ 25C, Temp(C), Rainfall (mm)
401027 - Murray @ Hume Dam - Res. Level (m), % Eff. Full Stor, Volume (ML)
409017 - Murray @ Doctors Point - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
409023 - Stevens Weir Downstream
425007 - Darling @ Burtundy  - Level (m), D.O., Discharge (ML/d), EC @ 25C, Temp(C), Rainfall (mm)
409001 - Murray @ Albury (Union Bridge) - water temp, level, EC
410130 - Murrumbidgee @ Balranald - Level (m), D.O., Discharge (ML/d), EC @ 25C, Temp(C)
401549 - Murray @ Bringenbong - level, discharge (mld)
401211 - Mitta Mitta @ Colemans - level, discharge (mld)
41310022 - Murray @ Colignan - EC, temp
409002 - Murray @ Corowa - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
401224A - Mitta Mirra @ Dartmouth Dam - Res. Level (m), % Eff. Full Stor, Volume (ML)
409008 - Edward @ Offtake - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
409030 - Gulpa Creek @ Offtake - level, discharge (mld)
401013 - Jingellic Creek @ Jingellic - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
409029 - Mulwala Canal escape @ Edwards River - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
401014 - Tooma River @ Pinegrove - Level (m), Discharge (ML/d), EC @ 25C, Temp(C), Rainfall (mm)
41310025 - Murray @ Redcliff - temp
409013 - Wakool River @ Stoney Crossing - Level (m), D.O., Discharge (ML/d), EC @ 25C, Temp(C)
409023 - Edward River @ Downstream Steven's Weir - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
409101 - Edward River @ Upstream Steven's Weir - Res leve (m), level (m)
409204C - Murray @ Swan Hill - no data
401204A - Mitta Mirra @ Tallandoon - no data
409202A - Murray @ Tocumwal - no data
425012 - Darling @ Weir 32 - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
409025 - Murray @ Yarrawonga Downstream - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
409216A - Murray @ Yarrawonga Upstream - level (m)
'''
