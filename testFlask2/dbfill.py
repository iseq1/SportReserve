import hashlib

from dbpush import DataPusher

with DataPusher('database.db') as changer:

    def tennis():
        def tennis_outdoor():
            changer.insert_data(table='place', type='Летние площадки', subtype='Теннисные площадки под открытым небом', name='Гольф-клуб «Раевский»', description='Элитный загородный гольф-парк', subdescription='На территории нашего клуба расположены 4 корта под открытым небом с профессиональным американским покрытием HARD – Grand Slam Premium (9 слоев), являющееся эталонным для теннисистов всего мира:\n – 2 теннисных корта;\n – 2 корта для игры в Pickleball; (новая для России игра, сочетающая в себе элементы большого тенниса, настольного тенниса и бадминтона).\n К Вашим услугам комфортные раздевалки и душевые.', address='ст. Натухаевская, гольф-деревня «Предгорье», Натухаевская, Краснодарский край', rental_period=1, price=5000, photo_path='../static/images/catalog/summer-sport/tennis-outdoor/tennis-indoor-item-2.jpg', locker_rooms='True', shower='True', parking='True', inventory='True')
            changer.insert_data(table='place', type='Летние площадки', subtype='Теннисные площадки под открытым небом', name='Комплекс «Авангард»', description='Приотельный спортивный комплекс', subdescription='"Авангард" на самом деле является целым комплексом, куда входят отель, ресторан, залы для банкетов и конференций, спортивно-оздоровительный блок и, разумеется, теннисные корты. Их в "Авангарде" пять - есть открытые и закрытые, а также vip-корт. Все корты по качеству отвечают нормам проведения турниров международного уровня. Набегавшись на корте, можно здесь же, продолжить силовые занятия в спортивном и тренажерном залах или расслабиться в бассейне с сауной.', address='ул. Урицкого, 17, Казань', rental_period=1, price=1500, photo_path='../static/images/catalog/summer-sport/tennis-outdoor/tennis-outdoors-item-3.jpg', locker_rooms='True', shower='True', parking='True', inventory='True')
            changer.insert_data(table='place', type='Летние площадки', subtype='Теннисные площадки под открытым небом', name='Лосево Парк', description='Загородная база отдыха', subdescription='БАЗА ОТДЫХА «ЛОСЕВО ПАРК» с большим номерным фондом в Ленинградской области. Берег озер Вуокса и Суходольского в окружении дикой красочной природы Карельского перешейка рядом с легендарными Лосевскими порогами, меккой любителей рафтинга, каякинга и гребли на байдарках. 120 номеров, коттедж на 10 человек.', address='База отдыха «ЛОСЕВО ПАРК», пос. Лосево', rental_period=1, price=3500, photo_path='../static/images/catalog/summer-sport/tennis-outdoor/tennis-outdoors-item-1.jpg', locker_rooms='False', shower='True', parking='True', inventory='True')

        def tennis_indoor():
            changer.insert_data(table='place', type='Летние площадки', subtype='Теннисные площадки под крытым небом', name='Гольф-клуб «Раевский»', description='Элитный загородный гольф-парк', subdescription='На территории нашего клуба расположены 4 корта под открытым небом с профессиональным американским покрытием HARD – Grand Slam Premium (9 слоев), являющееся эталонным для теннисистов всего мира:\n – 2 теннисных корта;\n – 2 корта для игры в Pickleball; (новая для России игра, сочетающая в себе элементы большого тенниса, настольного тенниса и бадминтона).\n К Вашим услугам комфортные раздевалки и душевые.', address='ст. Натухаевская, гольф-деревня «Предгорье», Натухаевская, Краснодарский край', rental_period=1, price=5000, photo_path='../static/images/catalog/summer-sport/tennis-indoor/tennis-indoor-item-2.jpg', locker_rooms='True', shower='True', parking='True', inventory='True')

        tennis_indoor()

    def golf():
        def golf_in_city():
            changer.insert_data(table='place', type='Летние площадки', subtype='Поля для игры в гольф в черте города',
                                name='Гольф-клуб «Сколково»', description='Элитный гольф-клуб в Москве',
                                subdescription='Гольф-клуб ‘Сколково’, плод совместной работы легендарного Джека Никлауса и инвестиционной компании Millhouse – место для самых взыскательных гольфистов. В распоряжении игроков есть все: от поля мирового уровня ‘Jack Nicklaus Signature’, спроектированного совместно с ландшафтным дизайнером Линдой Бёрд, до клубного дома, построенного по проекту выдающегося японского архитектора Шигеру Бана.',
                                address='121353,Москва,Сколковское шоссе, 50', rental_period=1, price=7500,
                                photo_path='../static/images/catalog/summer-sport/golf-incity/golf-incity-item-1.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')


        def golf_out_city():
            changer.insert_data(table='place', type='Летние площадки', subtype='Поля для игры в гольф за чертой города',
                                name='Гольф-клуб «Раевский»', description='Элитный загородный гольф-парк',
                                subdescription='На территории нашего клуба расположены 4 корта под открытым небом с профессиональным американским покрытием HARD – Grand Slam Premium (9 слоев), являющееся эталонным для теннисистов всего мира:\n – 2 теннисных корта;\n – 2 корта для игры в Pickleball; (новая для России игра, сочетающая в себе элементы большого тенниса, настольного тенниса и бадминтона).\n К Вашим услугам комфортные раздевалки и душевые.',
                                address='ст. Натухаевская, гольф-деревня «Предгорье», Натухаевская, Краснодарский край',
                                rental_period=1, price=5000,
                                photo_path='../static/images/catalog/summer-sport/golf-outcity/golf-outcity-item-1.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

            changer.insert_data(table='place', type='Летние площадки', subtype='Поля для игры в гольф за чертой города',
                                name='Гольф - клуб «Свияжские холмы»', description='Элитный загородный гольф-парк',
                                subdescription='На площади в 32 гектара прекрасно сочетаются естественные перепады высот, водоемы и песчаные зоны реки Волги и сказочный остров-град Свияжск. Поле имеет 18 лунок различных категорий сложности. Дизайн поля разработала швейцарской компанией «Harradine Golf AG, создающая лучшие гольф-поля в мире с 1929 года.',
                                address='422595, Республика Татарстан, Верхнеуслонский район, д. Савино',
                                rental_period=1, price=5000,
                                photo_path='../static/images/catalog/summer-sport/golf-outcity/golf-outcity-item-2.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

            changer.insert_data(table='place', type='Летние площадки', subtype='Поля для игры в гольф за чертой города',
                                name='Гольф-клуб «Пестово»', description='Элитный загородный гольф- и яхт-клуб',
                                subdescription='Гольф- и яхт-клуб «Пестово» — абсолютно новый для России загородный комплекс, сочетающий в себе традиции английского загородного клуба: гольф-поле чемпионского класса, элитную недвижимость с видом на поле клабхаус и современный яхт-клуб',
                                address='Никольская ул., 1, Румянцево, Московская обл., 141301',
                                rental_period=1, price=4500,
                                photo_path='../static/images/catalog/summer-sport/golf-outcity/golf-outcity-item-3.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

            changer.insert_data(table='place', type='Летние площадки', subtype='Поля для игры в гольф за чертой города',
                                name='Гольф-клуб «Завидово»', description='Курортная зона с полем для гольфа',
                                subdescription='Зави́дово — особо охраняемая природная территория федерального значения со статусом национального парка, относится к объектам общенационального достояния. Национальный парк расположен на территории Московской и Тверской областей, в пределах Верхневолжской низменности.',
                                address='Тверская область, Конаковский район, д.Шоша',
                                rental_period=1, price=3500,
                                photo_path='../static/images/catalog/summer-sport/golf-outcity/golf-outcity-item-4.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

        golf_in_city()
        golf_out_city()

    def football():
        def football_in():
            changer.insert_data(table='place', type='Летние площадки', subtype='Футбольные манежи',
                                name='Арена Новый Футбол', description='Современный футбольный центр',
                                subdescription='Играй в комфортных условиях, даже если на улице дождь или снегопад\n Пользуйся индивидуальными локерами, душевыми, фенами и отдельным санузлом\nЖди выхода на поле в местах с диванами для просмотра игр и тренировок\nВсегда доступные парковочные места для наших клиентов',
                                address='г. Москва, ул. Крылатская д. 2 стр. 22',
                                rental_period=1, price=6000,
                                photo_path='../static/images/catalog/summer-sport/football-indoor/football-indoor-item-1.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

            changer.insert_data(table='place', type='Летние площадки', subtype='Футбольные манежи',
                                name='РФЛ-Арена', description='Современный футбольный комплекс',
                                subdescription='РФЛ-Арена - это новые футбольные комплексы, где тепло зимой и комфортно летом! \n На каждом объекте есть: раздевалки, манишки, мячи, отличная искусственная трава последнего поколения, электронное табло со временем и счетом матча, ,удобное расположение полей в городе! \n Здесь вы можете уточнить свободные часы и стоимость аренды. \n РФЛ - это Регулярная Футбольная Любительская Лига в Самаре. Мы проводим регулярный чемпионат для любительских и корпоративных команд, а также турниры.',
                                address='г. Москва, Московское шоссе, 77',
                                rental_period=1, price=2000,
                                photo_path='../static/images/catalog/summer-sport/football-indoor/football-indoor-item-2.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

            changer.insert_data(table='place', type='Летние площадки', subtype='Футбольные манежи',
                                name='Академия будущего', description='Современный футбольный центр',
                                subdescription='Манеж Академия будущего находится в самом центре Москвы в 5 минутах от метро Киевская с покрытием искусственная трава последнего поколения и высотой ворса 6 см. Футбольное поле размером 45х22 метра подходит для формата игры 6х6 и 7х7. Помимо игр и тренировок площадка идеально подходит для турниров и мероприятий.',
                                address='г. Москва, Украинский бульвар, 9',
                                rental_period=1, price=3000,
                                photo_path='../static/images/catalog/summer-sport/football-indoor/football-indoor-item-3.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

        football_in()

        def football_out():
            changer.insert_data(table='place', type='Летние площадки', subtype='Открытые футбольные площадки',
                                name='Олимп Арена', description='Модерн футбольное поле',
                                subdescription='Олимп Арена находится на территории ЖК Золотые ключи-2. Арендовать можно с 07:00 утра до 00.00 ночи. Футбольное поле размером 60х30 оптимально подходит для игры в формате 8×8/7×7/6×6 игроков на всем поле с воротами 5×2 м. Для 8-10 игроков (формат 5х5) можно арендовать 1/2 поля и играть с воротами 3×2 м. Летняя раздевалка находится в 10 м от поля. Душевые находятся в теплой раздевалке в 150 м от поля. Бесплатная парковка рядом с полем. Для игры в вечернее время есть искусственное светодиодное освещение - 250 люкс.',
                                address=' г. Москва, ул. Минская 1Г',
                                rental_period=1, price=1750,
                                photo_path='../static/images/catalog/summer-sport/football-outdoor/football-outdoor-item-1.jpg',
                                locker_rooms='False', shower='False', parking='True', inventory='True')

            changer.insert_data(table='place', type='Летние площадки', subtype='Открытые футбольные площадки',
                                name='Футбольные поля «Под Мостом»', description='Модерн футбольное поле',
                                subdescription='«Под мостом» для футбола — это круглогодичная многофункциональная площадка в спортивном сердце города:\nмини-футбольные поля с искусственным газоном\nфутбольные коробки с качественным покрытием\nраздевалки, фуд-корт и огромное количество других удобств для вашего комфорта\nНа площадке проводятся футбольные турниры разного уровня. Технические характеристики пространства позволяют проводить и принимать мероприятия любого формата (спортивные зрелищные, выставочно-презентационные, корпоративные и другие)',
                                address=' г. Москва, Ул. Лужники 24, Под Мостом ',
                                rental_period=1, price=1500,
                                photo_path='../static/images/catalog/summer-sport/football-outdoor/football-outdoor-item-2.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

            changer.update_data(table='place', ID=17, type='Летние площадки', subtype='Открытые футбольные площадки',
                                name='Футбольное поле CitySport', description='Модерн футбольное поле',
                                subdescription='Футбольный стадион City Sport Красная Пресня – это основное футбольное поле размером 90*60, которое делится на 2 или 4 части. Данное футбольное поле с качественным покрытием искусственная трава 4 см последнего поколения, поэтому использовать его можно как в зимнее, так и в летнее время.',
                                address='г. Москва, ул. Дружинниковская, 18  ', rental_period=1, price=3300,
                                photo_path='../static/images/catalog/summer-sport/football-outdoor/football-outdoor-item-3.jpg',
                                locker_rooms='True', shower='False', parking='True', inventory='True')

        football_out()



