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

    def badminton():
        def badminton_court():
            changer.insert_data(table='place', type='Летние площадки', subtype='Корты для игры в бадминтон',
                                name='Школа бадминтона «Мультиспорт»', description='Современный бадминтон центр',
                                subdescription='Покрытие кортов GerflorTaraflex, адаптированы к проведению международных соревнований. Освещение 1000 люкс. Четырехзонная система климат-контроля.\nИндивидуальные и групповые занятия для детей и взрослых под руководством профессиональных тренеров высокой квалификации.',
                                address='Лужники, 24, с 10, Москва',
                                rental_period=1, price=2500,
                                photo_path='../static/images/catalog/summer-sport/badminton/badminton-item-1.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

            changer.insert_data(table='place', type='Летние площадки', subtype='Корты для игры в бадминтон',
                                name='СК Newton Arena', description='Современный бадминтон комплекс',
                                subdescription='Групповые и индивидуальные тренировки для детей и взрослых, аренда корта.',
                                address='1-й Нагатинский, пр-д 10, стр.3, Москва',
                                rental_period=1, price=2000,
                                photo_path='../static/images/catalog/summer-sport/badminton/badminton-item-2.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

        badminton_court()

    def hockey():
        def hockey_in():
            changer.insert_data(table='place', type='Зимние площадки', subtype='Ледовые арены для игры в хоккей',
                                name='Хоккейный комплекс "Академия "Спартак"', description='Хоккейный комплекс',
                                subdescription='На территории хоккейного комплекса площадью 10 000 кв.м. расположены современные ледовые площадки: «финская» 60х26м и «канадская» 56х26м, площадки соответствуют стандартам IIHF для тренировок и соревнований хоккеистов и фигуристов. Одно из полей комплекса оснащено специальным оборудованием, предназначенным для комфортных тренировок команд по следж-хоккею. Площадки оборудованы системой игрового света и звука, что необходимо для качественного проведения матчей, турниров и других спортивных мероприятий. Раздевалка предоставляется за 30 минут до старта арендованного времени.',
                                address=' ул.Б.Тихоновская, дом 2, стр. 1',
                                rental_period=1, price=8000,
                                photo_path='../static/images/catalog/winter-sport/hockey/hockey-item-1.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')
            changer.insert_data(table='place', type='Зимние площадки', subtype='Ледовые арены для игры в хоккей',
                                name='"Южный лед"', description='Ледовая арена',
                                subdescription='«Южный лёд» — современный многофункциональный ледовый комплекс, оборудованный по последнему слову техники и отвечающий всем современным требованиям для проведения спортивных мероприятий любой сложности. Он ориентирован на проведение тренировок и соревнований как для хоккеистов, так и для фигуристов.',
                                address='ул. Маршала Савицкого, д. 7 ',
                                rental_period=1, price=2500,
                                photo_path='../static/images/catalog/winter-sport/hockey/hockey-item-2.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')
            changer.insert_data(table='place', type='Зимние площадки', subtype='Ледовые арены для игры в хоккей',
                                name='Академия Будущего', description='Ледовый комплекс',
                                subdescription='10 января 2022 г. открылся новый ледовый комплекс Академия Будущего, с двумя катками размером 58 на 26 и 30 Х 15 - это идеальная площадка для: тренировок, игр, турниров, товарищеских матчей а также для школ фигурного катания.\nВ комплексе имеется 6 просторных раздевалок с душевыми, бросковая зона. Предоставляются услуги по сушке хоккейной формы, заточке коньков а также услуги тренера по хоккею и организации хоккейных турниров.',
                                address=' 1-й нагатинский проезд 2с17 ',
                                rental_period=1, price=3500,
                                photo_path='../static/images/catalog/winter-sport/hockey/hockey-item-3.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')
        hockey_in()

    def curling():
        def curling_in():
            changer.insert_data(table='place', type='Зимние площадки', subtype='Ледовые арены для игры в керлинг',
                                name='СШОР «Москвич»', description='Керлинг-центр',
                                subdescription='Крытая площадка для игры в кёрлинг с раздевалками и всем необходимым инвентарем. В игровой зоне — четыре дорожки 5×25 метров с разметкой. Можно взять урок у тренера, в том числе и для детей, или поиграть самостоятельно.',
                                address='Волгоградский пр-кт., д. 46/15, стр. 10',
                                rental_period=1, price=3500,
                                photo_path='../static/images/catalog/winter-sport/curling/curling-item-1.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

            changer.insert_data(table='place', type='Зимние площадки', subtype='Ледовые арены для игры в керлинг',
                                name='«Московский керлинг-клуб»', description='Керлинг-центр',
                                subdescription='Самый большой керлинг-клуб в Москве. Находится недалеко от станции метро «Пролетарская». Здесь оборудовано пять дорожек с разметкой и есть ресторан. В клубе регулярно проводят групповые тренировки.',
                                address='Михайловский пр-д, 1с1',
                                rental_period=1, price=3250,
                                photo_path='../static/images/catalog/winter-sport/curling/curling-item-2.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')
            changer.insert_data(table='place', type='Зимние площадки', subtype='Ледовые арены для игры в керлинг',
                                name='Ледовый стадион «Лужки.клуб»', description='Центр зимних видов спорта',
                                subdescription='В загородном клубе есть две крытые арены «Олимпийский стандарт» и «Канадский стандарт» с дорожкой для керлинга. Одновременно могут играть десять человек. А для детей есть игровая комната с лабиринтом, настольными играми и зоной для творчества.',
                                address='Московская обл., г. о. Истра, Лужки.клуб',
                                rental_period=1, price=7500,
                                photo_path='../static/images/catalog/winter-sport/curling/curling-item-3.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

        curling_in()

    def swimmingpool():
        def sport_pool():
            changer.insert_data(table='place', type='Бассейны', subtype='Спортивные бассейны',
                                name='Московский олимпийский центр водного спорта', description='Олимпийский центр',
                                subdescription='Комплекс состоит из двух блоков — закрытого и открытого. В первом три бассейна: 50-метровый на восемь дорожек, 25-метровый на шесть дорожек и маленький 17-метровый. За дополнительную плату можно заниматься аквааэробикой или учиться плавать. Во втором блоке — открытый 50-метровый бассейн на восемь дорожек.',
                                address='Ибрагимова, 32',
                                rental_period=1, price=6300,
                                photo_path='../static/images/catalog/swimming-pool-sport/swimming-pool-sport/swimming-pool-sport-item-1.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')
            changer.insert_data(table='place', type='Бассейны', subtype='Спортивные бассейны',
                                name='Водный стадион «Динамо»', description='Cпорт-комплекс',
                                subdescription='В спорткомплексе один большой бассейн длиной 50 метров на десять дорожек. В 2013 году «Динамо» реконструировали: сделали свежий ремонт, установили панорамные окна в пол и обновили систему очистки воды — теперь в ней практически нет хлора, поэтому кожа меньше сохнет. В бассейне проводят занятия по аквааэробике, есть утренние и вечерние группы обучения плаванию для взрослых, также можно взять индивидуальные занятия с инструктором (все уроки оплачиваются отдельно). Из несовершенств — в «Динамо» часто проводят соревнования, поэтому могут отменять сеансы или закрывать половину дорожек. ',
                                address='Ленинградское шоссе, 39, стр. 53',
                                rental_period=1, price=7000,
                                photo_path='../static/images/catalog/swimming-pool-sport/swimming-pool-sport/swimming-pool-sport-item-2.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')
            changer.insert_data(table='place', type='Бассейны', subtype='Спортивные бассейны',
                                name='Royal Wellness Club', description='Велнес-клуб',
                                subdescription='Один из самых дорогих бассейнов Москвы находится в велнес-клубе гостиницы Radisson Royal. Плавательные дорожки построены по олимпийским стандартам — 50 метров. Также в клубе работают две гидромассажные ванны, русская баня, сауна, турецкий хаммам и зона отдыха с шезлонгами. По расписанию проводят аквааэробику, можно взять занятия с инструктором. Абонементов нет, только клубные карты. Медицинскую справку не требуют.',
                                address='Кутузовский просп., 2/1, стр. 1',
                                rental_period=1, price=30000,
                                photo_path='../static/images/catalog/swimming-pool-sport/swimming-pool-sport/swimming-pool-sport-item-3.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')

        sport_pool()
        def chill_pool():
            changer.insert_data(table='place', type='Бассейны', subtype='Бассейны для отдыха',
                                name='«The БАSSЕЙН»', description='Открытый бассейн в парке «Сокольники»',
                                subdescription='Каждый летний день с 10:00 до 22:00 посетители парка «Сокольники» могут не только поплавать в двух небольших бассейнах, но и потанцевать у открытой воды. С понедельника по субботу развлекательное пространство «The БАSSЕЙН» организует вечеринки, на которых играют гости из Gipsy, Space Moscow, Icon и других модных столичных заведений.\nК услугам отдыхающих – искусственные водоемы итальянского и немецкого производства, шезлонги, раздевалки и душевые, столы для пинг-понга, площадка для занятия йогой и аэробикой, кафе с летней верандой. Можно арендовать различный спортинвентарь – бадминтон, волейбольный мяч, нарды. \nВода в детском бассейне с водной горкой подогревается до 30 градусов, а чтобы гости могли отвлечься и не волноваться за ребенка, здесь всегда дежурит спасатель.',
                                address='Митьковский проезд, д. 1, стр. 1',
                                rental_period=1, price=5000,
                                photo_path='../static/images/catalog/swimming-pool-sport/swimming-pool-chill/swimming-pool-chill-item-1.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')
            changer.insert_data(table='place', type='Бассейны', subtype='Бассейны для отдыха',
                                name='«Флакон»', description='Пляж в экшн-парке дизайн-завода «Флакон»',
                                subdescription='Прямо скажем, своими размерами искусственный водоем, расположенный в экшн-парке дизайна-завода «Флакон», не впечатляет – всего-то 5 на 10 метров, хотя на здешней террасе есть и лежаки с гамаками, и душ, и зонтики от солнца. \nЧто вас наверняка впечатлит в этом фестивальном арт-пространстве – так это проходящие вокруг искусственного водоема всевозможные активности: можно поплавать на скимборде или поиграть в пинг-понг, потанцевать на пляжной вечеринке или послушать живой концерт, посидеть в кафе или пройтись по модным дизайнерским магазинам.',
                                address='ул. Большая Новодмитровская, д. 36',
                                rental_period=1, price=3000,
                                photo_path='../static/images/catalog/swimming-pool-sport/swimming-pool-chill/swimming-pool-chill-item-2.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='True')
        chill_pool()


    def parquet_sport():
        def ballroom_dance():
            changer.insert_data(table='place', type='Паркетные площадки', subtype='Бальные танцы',
                                name='Высшая школа танца', description='Школа бального танца для начинающих',
                                subdescription='Высшая школа танца ведет обучение бальным танцам с индивидуальным подходом к каждому ученику.\nНаша методика обучения взрослых людей направлена на быструю адаптацию тела к танцевальной технике и позволяет в кратчайшие сроки получить максимальные результаты.',
                                address='метро Преображенская площадь, Преображенская площадь, дом 12',
                                rental_period=1, price=7000,
                                photo_path='../static/images/catalog/parquet-sport/ballroom-dance/ballroom-dance-item-1.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='False')
            changer.insert_data(table='place', type='Паркетные площадки', subtype='Бальные танцы',
                                name='Galla Dance', description='Школа бального танца',
                                subdescription='Galla Dance предлагает занятия по бальным танцам европейской и латиноамериканской программы: вальсу, танго, фокстроту, квикстепу, ча-ча-ча, самбе, румбе, пасодоблю и джайву. ',
                                address='метро Новослободская, дом 52',
                                rental_period=1, price=8000,
                                photo_path='../static/images/catalog/parquet-sport/ballroom-dance/ballroom-dance-item-2.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='False')
            changer.insert_data(table='place', type='Паркетные площадки', subtype='Бальные танцы',
                                name='Time to Dance', description='Школа бального танца',
                                subdescription='В Time to Dance наглядно объяснят, как красиво танцевать в паре, даже если раньше бальными танцами вы никогда не занимались. Среди программ для начинающих танго, вальс, фокстрот и румба. Можно выбрать цикл из трех, пяти и десяти индивидуальных занятий – за 9900, 16 500 и 33 000 рублей соответственно. Занятия проходят в студии, расположенной в ТЦ «Авиапарк».',
                                address='м. ЦСКА',
                                rental_period=1, price=9500,
                                photo_path='../static/images/catalog/parquet-sport/ballroom-dance/ballroom-dance-item-3.jpg',
                                locker_rooms='True', shower='True', parking='True', inventory='False')
        ballroom_dance()


