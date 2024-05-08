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

    tennis()



    # changer.insert_data(table='reservation', )