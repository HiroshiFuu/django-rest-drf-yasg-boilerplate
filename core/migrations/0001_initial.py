# Generated by Django 3.1.10 on 2021-05-29 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(blank=True, null=True, verbose_name='Modified At')),
                ('name', models.CharField(max_length=63, unique=True, verbose_name='Role Name')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='role_created', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='role_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
            options={
                'verbose_name': 'Role',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone Number')),
                ('timezone', models.CharField(choices=[('Africa/Abidjan', '(UTC +00:00) Africa/Abidjan'), ('Africa/Accra', '(UTC +00:00) Africa/Accra'), ('Africa/Addis_Ababa', '(UTC +03:00) Africa/Addis_Ababa'), ('Africa/Algiers', '(UTC +01:00) Africa/Algiers'), ('Africa/Asmara', '(UTC +03:00) Africa/Asmara'), ('Africa/Asmera', '(UTC +03:00) Africa/Asmera'), ('Africa/Bamako', '(UTC +00:00) Africa/Bamako'), ('Africa/Bangui', '(UTC +01:00) Africa/Bangui'), ('Africa/Banjul', '(UTC +00:00) Africa/Banjul'), ('Africa/Bissau', '(UTC +00:00) Africa/Bissau'), ('Africa/Blantyre', '(UTC +02:00) Africa/Blantyre'), ('Africa/Brazzaville', '(UTC +01:00) Africa/Brazzaville'), ('Africa/Bujumbura', '(UTC +02:00) Africa/Bujumbura'), ('Africa/Cairo', '(UTC +02:00) Africa/Cairo'), ('Africa/Casablanca', '(UTC +01:00) Africa/Casablanca'), ('Africa/Ceuta', '(UTC +01:00) Africa/Ceuta'), ('Africa/Conakry', '(UTC +00:00) Africa/Conakry'), ('Africa/Dakar', '(UTC +00:00) Africa/Dakar'), ('Africa/Dar_es_Salaam', '(UTC +03:00) Africa/Dar_es_Salaam'), ('Africa/Djibouti', '(UTC +03:00) Africa/Djibouti'), ('Africa/Douala', '(UTC +01:00) Africa/Douala'), ('Africa/El_Aaiun', '(UTC +01:00) Africa/El_Aaiun'), ('Africa/Freetown', '(UTC +00:00) Africa/Freetown'), ('Africa/Gaborone', '(UTC +02:00) Africa/Gaborone'), ('Africa/Harare', '(UTC +02:00) Africa/Harare'), ('Africa/Johannesburg', '(UTC +02:00) Africa/Johannesburg'), ('Africa/Juba', '(UTC +02:00) Africa/Juba'), ('Africa/Kampala', '(UTC +03:00) Africa/Kampala'), ('Africa/Khartoum', '(UTC +02:00) Africa/Khartoum'), ('Africa/Kigali', '(UTC +02:00) Africa/Kigali'), ('Africa/Kinshasa', '(UTC +01:00) Africa/Kinshasa'), ('Africa/Lagos', '(UTC +01:00) Africa/Lagos'), ('Africa/Libreville', '(UTC +01:00) Africa/Libreville'), ('Africa/Lome', '(UTC +00:00) Africa/Lome'), ('Africa/Luanda', '(UTC +01:00) Africa/Luanda'), ('Africa/Lubumbashi', '(UTC +02:00) Africa/Lubumbashi'), ('Africa/Lusaka', '(UTC +02:00) Africa/Lusaka'), ('Africa/Malabo', '(UTC +01:00) Africa/Malabo'), ('Africa/Maputo', '(UTC +02:00) Africa/Maputo'), ('Africa/Maseru', '(UTC +02:00) Africa/Maseru'), ('Africa/Mbabane', '(UTC +02:00) Africa/Mbabane'), ('Africa/Mogadishu', '(UTC +03:00) Africa/Mogadishu'), ('Africa/Monrovia', '(UTC +00:00) Africa/Monrovia'), ('Africa/Nairobi', '(UTC +03:00) Africa/Nairobi'), ('Africa/Ndjamena', '(UTC +01:00) Africa/Ndjamena'), ('Africa/Niamey', '(UTC +01:00) Africa/Niamey'), ('Africa/Nouakchott', '(UTC +00:00) Africa/Nouakchott'), ('Africa/Ouagadougou', '(UTC +00:00) Africa/Ouagadougou'), ('Africa/Porto-Novo', '(UTC +01:00) Africa/Porto-Novo'), ('Africa/Sao_Tome', '(UTC +00:00) Africa/Sao_Tome'), ('Africa/Timbuktu', '(UTC +00:00) Africa/Timbuktu'), ('Africa/Tripoli', '(UTC +02:00) Africa/Tripoli'), ('Africa/Tunis', '(UTC +01:00) Africa/Tunis'), ('Africa/Windhoek', '(UTC +02:00) Africa/Windhoek'), ('America/Adak', '(UTC -10:00) America/Adak'), ('America/Anchorage', '(UTC -09:00) America/Anchorage'), ('America/Anguilla', '(UTC -04:00) America/Anguilla'), ('America/Antigua', '(UTC -04:00) America/Antigua'), ('America/Araguaina', '(UTC -03:00) America/Araguaina'), ('America/Argentina/Buenos_Aires', '(UTC -03:00) America/Argentina/Buenos_Aires'), ('America/Argentina/Catamarca', '(UTC -03:00) America/Argentina/Catamarca'), ('America/Argentina/ComodRivadavia', '(UTC -03:00) America/Argentina/ComodRivadavia'), ('America/Argentina/Cordoba', '(UTC -03:00) America/Argentina/Cordoba'), ('America/Argentina/Jujuy', '(UTC -03:00) America/Argentina/Jujuy'), ('America/Argentina/La_Rioja', '(UTC -03:00) America/Argentina/La_Rioja'), ('America/Argentina/Mendoza', '(UTC -03:00) America/Argentina/Mendoza'), ('America/Argentina/Rio_Gallegos', '(UTC -03:00) America/Argentina/Rio_Gallegos'), ('America/Argentina/Salta', '(UTC -03:00) America/Argentina/Salta'), ('America/Argentina/San_Juan', '(UTC -03:00) America/Argentina/San_Juan'), ('America/Argentina/San_Luis', '(UTC -03:00) America/Argentina/San_Luis'), ('America/Argentina/Tucuman', '(UTC -03:00) America/Argentina/Tucuman'), ('America/Argentina/Ushuaia', '(UTC -03:00) America/Argentina/Ushuaia'), ('America/Aruba', '(UTC -04:00) America/Aruba'), ('America/Asuncion', '(UTC -04:00) America/Asuncion'), ('America/Atikokan', '(UTC -05:00) America/Atikokan'), ('America/Atka', '(UTC -10:00) America/Atka'), ('America/Bahia', '(UTC -03:00) America/Bahia'), ('America/Bahia_Banderas', '(UTC -06:00) America/Bahia_Banderas'), ('America/Barbados', '(UTC -04:00) America/Barbados'), ('America/Belem', '(UTC -03:00) America/Belem'), ('America/Belize', '(UTC -06:00) America/Belize'), ('America/Blanc-Sablon', '(UTC -04:00) America/Blanc-Sablon'), ('America/Boa_Vista', '(UTC -04:00) America/Boa_Vista'), ('America/Bogota', '(UTC -05:00) America/Bogota'), ('America/Boise', '(UTC -07:00) America/Boise'), ('America/Buenos_Aires', '(UTC -03:00) America/Buenos_Aires'), ('America/Cambridge_Bay', '(UTC -07:00) America/Cambridge_Bay'), ('America/Campo_Grande', '(UTC -04:00) America/Campo_Grande'), ('America/Cancun', '(UTC -05:00) America/Cancun'), ('America/Caracas', '(UTC -04:00) America/Caracas'), ('America/Catamarca', '(UTC -03:00) America/Catamarca'), ('America/Cayenne', '(UTC -03:00) America/Cayenne'), ('America/Cayman', '(UTC -05:00) America/Cayman'), ('America/Chicago', '(UTC -06:00) America/Chicago'), ('America/Chihuahua', '(UTC -07:00) America/Chihuahua'), ('America/Coral_Harbour', '(UTC -05:00) America/Coral_Harbour'), ('America/Cordoba', '(UTC -03:00) America/Cordoba'), ('America/Costa_Rica', '(UTC -06:00) America/Costa_Rica'), ('America/Creston', '(UTC -07:00) America/Creston'), ('America/Cuiaba', '(UTC -04:00) America/Cuiaba'), ('America/Curacao', '(UTC -04:00) America/Curacao'), ('America/Danmarkshavn', '(UTC +00:00) America/Danmarkshavn'), ('America/Dawson', '(UTC -07:00) America/Dawson'), ('America/Dawson_Creek', '(UTC -07:00) America/Dawson_Creek'), ('America/Denver', '(UTC -07:00) America/Denver'), ('America/Detroit', '(UTC -05:00) America/Detroit'), ('America/Dominica', '(UTC -04:00) America/Dominica'), ('America/Edmonton', '(UTC -07:00) America/Edmonton'), ('America/Eirunepe', '(UTC -05:00) America/Eirunepe'), ('America/El_Salvador', '(UTC -06:00) America/El_Salvador'), ('America/Ensenada', '(UTC -08:00) America/Ensenada'), ('America/Fort_Nelson', '(UTC -07:00) America/Fort_Nelson'), ('America/Fort_Wayne', '(UTC -05:00) America/Fort_Wayne'), ('America/Fortaleza', '(UTC -03:00) America/Fortaleza'), ('America/Glace_Bay', '(UTC -04:00) America/Glace_Bay'), ('America/Godthab', '(UTC -03:00) America/Godthab'), ('America/Goose_Bay', '(UTC -04:00) America/Goose_Bay'), ('America/Grand_Turk', '(UTC -05:00) America/Grand_Turk'), ('America/Grenada', '(UTC -04:00) America/Grenada'), ('America/Guadeloupe', '(UTC -04:00) America/Guadeloupe'), ('America/Guatemala', '(UTC -06:00) America/Guatemala'), ('America/Guayaquil', '(UTC -05:00) America/Guayaquil'), ('America/Guyana', '(UTC -04:00) America/Guyana'), ('America/Halifax', '(UTC -04:00) America/Halifax'), ('America/Havana', '(UTC -05:00) America/Havana'), ('America/Hermosillo', '(UTC -07:00) America/Hermosillo'), ('America/Indiana/Indianapolis', '(UTC -05:00) America/Indiana/Indianapolis'), ('America/Indiana/Knox', '(UTC -06:00) America/Indiana/Knox'), ('America/Indiana/Marengo', '(UTC -05:00) America/Indiana/Marengo'), ('America/Indiana/Petersburg', '(UTC -05:00) America/Indiana/Petersburg'), ('America/Indiana/Tell_City', '(UTC -06:00) America/Indiana/Tell_City'), ('America/Indiana/Vevay', '(UTC -05:00) America/Indiana/Vevay'), ('America/Indiana/Vincennes', '(UTC -05:00) America/Indiana/Vincennes'), ('America/Indiana/Winamac', '(UTC -05:00) America/Indiana/Winamac'), ('America/Indianapolis', '(UTC -05:00) America/Indianapolis'), ('America/Inuvik', '(UTC -07:00) America/Inuvik'), ('America/Iqaluit', '(UTC -05:00) America/Iqaluit'), ('America/Jamaica', '(UTC -05:00) America/Jamaica'), ('America/Jujuy', '(UTC -03:00) America/Jujuy'), ('America/Juneau', '(UTC -09:00) America/Juneau'), ('America/Kentucky/Louisville', '(UTC -05:00) America/Kentucky/Louisville'), ('America/Kentucky/Monticello', '(UTC -05:00) America/Kentucky/Monticello'), ('America/Knox_IN', '(UTC -06:00) America/Knox_IN'), ('America/Kralendijk', '(UTC -04:00) America/Kralendijk'), ('America/La_Paz', '(UTC -04:00) America/La_Paz'), ('America/Lima', '(UTC -05:00) America/Lima'), ('America/Los_Angeles', '(UTC -08:00) America/Los_Angeles'), ('America/Louisville', '(UTC -05:00) America/Louisville'), ('America/Lower_Princes', '(UTC -04:00) America/Lower_Princes'), ('America/Maceio', '(UTC -03:00) America/Maceio'), ('America/Managua', '(UTC -06:00) America/Managua'), ('America/Manaus', '(UTC -04:00) America/Manaus'), ('America/Marigot', '(UTC -04:00) America/Marigot'), ('America/Martinique', '(UTC -04:00) America/Martinique'), ('America/Matamoros', '(UTC -06:00) America/Matamoros'), ('America/Mazatlan', '(UTC -07:00) America/Mazatlan'), ('America/Mendoza', '(UTC -03:00) America/Mendoza'), ('America/Menominee', '(UTC -06:00) America/Menominee'), ('America/Merida', '(UTC -06:00) America/Merida'), ('America/Metlakatla', '(UTC -09:00) America/Metlakatla'), ('America/Mexico_City', '(UTC -06:00) America/Mexico_City'), ('America/Miquelon', '(UTC -03:00) America/Miquelon'), ('America/Moncton', '(UTC -04:00) America/Moncton'), ('America/Monterrey', '(UTC -06:00) America/Monterrey'), ('America/Montevideo', '(UTC -03:00) America/Montevideo'), ('America/Montreal', '(UTC -05:00) America/Montreal'), ('America/Montserrat', '(UTC -04:00) America/Montserrat'), ('America/Nassau', '(UTC -05:00) America/Nassau'), ('America/New_York', '(UTC -05:00) America/New_York'), ('America/Nipigon', '(UTC -05:00) America/Nipigon'), ('America/Nome', '(UTC -09:00) America/Nome'), ('America/Noronha', '(UTC -02:00) America/Noronha'), ('America/North_Dakota/Beulah', '(UTC -06:00) America/North_Dakota/Beulah'), ('America/North_Dakota/Center', '(UTC -06:00) America/North_Dakota/Center'), ('America/North_Dakota/New_Salem', '(UTC -06:00) America/North_Dakota/New_Salem'), ('America/Nuuk', '(UTC -03:00) America/Nuuk'), ('America/Ojinaga', '(UTC -07:00) America/Ojinaga'), ('America/Panama', '(UTC -05:00) America/Panama'), ('America/Pangnirtung', '(UTC -05:00) America/Pangnirtung'), ('America/Paramaribo', '(UTC -03:00) America/Paramaribo'), ('America/Phoenix', '(UTC -07:00) America/Phoenix'), ('America/Port-au-Prince', '(UTC -05:00) America/Port-au-Prince'), ('America/Port_of_Spain', '(UTC -04:00) America/Port_of_Spain'), ('America/Porto_Acre', '(UTC -05:00) America/Porto_Acre'), ('America/Porto_Velho', '(UTC -04:00) America/Porto_Velho'), ('America/Puerto_Rico', '(UTC -04:00) America/Puerto_Rico'), ('America/Punta_Arenas', '(UTC -03:00) America/Punta_Arenas'), ('America/Rainy_River', '(UTC -06:00) America/Rainy_River'), ('America/Rankin_Inlet', '(UTC -06:00) America/Rankin_Inlet'), ('America/Recife', '(UTC -03:00) America/Recife'), ('America/Regina', '(UTC -06:00) America/Regina'), ('America/Resolute', '(UTC -06:00) America/Resolute'), ('America/Rio_Branco', '(UTC -05:00) America/Rio_Branco'), ('America/Rosario', '(UTC -03:00) America/Rosario'), ('America/Santa_Isabel', '(UTC -08:00) America/Santa_Isabel'), ('America/Santarem', '(UTC -03:00) America/Santarem'), ('America/Santiago', '(UTC -04:00) America/Santiago'), ('America/Santo_Domingo', '(UTC -04:00) America/Santo_Domingo'), ('America/Sao_Paulo', '(UTC -03:00) America/Sao_Paulo'), ('America/Scoresbysund', '(UTC -01:00) America/Scoresbysund'), ('America/Shiprock', '(UTC -07:00) America/Shiprock'), ('America/Sitka', '(UTC -09:00) America/Sitka'), ('America/St_Barthelemy', '(UTC -04:00) America/St_Barthelemy'), ('America/St_Johns', '(UTC -03:30) America/St_Johns'), ('America/St_Kitts', '(UTC -04:00) America/St_Kitts'), ('America/St_Lucia', '(UTC -04:00) America/St_Lucia'), ('America/St_Thomas', '(UTC -04:00) America/St_Thomas'), ('America/St_Vincent', '(UTC -04:00) America/St_Vincent'), ('America/Swift_Current', '(UTC -06:00) America/Swift_Current'), ('America/Tegucigalpa', '(UTC -06:00) America/Tegucigalpa'), ('America/Thule', '(UTC -04:00) America/Thule'), ('America/Thunder_Bay', '(UTC -05:00) America/Thunder_Bay'), ('America/Tijuana', '(UTC -08:00) America/Tijuana'), ('America/Toronto', '(UTC -05:00) America/Toronto'), ('America/Tortola', '(UTC -04:00) America/Tortola'), ('America/Vancouver', '(UTC -08:00) America/Vancouver'), ('America/Virgin', '(UTC -04:00) America/Virgin'), ('America/Whitehorse', '(UTC -07:00) America/Whitehorse'), ('America/Winnipeg', '(UTC -06:00) America/Winnipeg'), ('America/Yakutat', '(UTC -09:00) America/Yakutat'), ('America/Yellowknife', '(UTC -07:00) America/Yellowknife'), ('Antarctica/Casey', '(UTC +11:00) Antarctica/Casey'), ('Antarctica/Davis', '(UTC +07:00) Antarctica/Davis'), ('Antarctica/DumontDUrville', '(UTC +10:00) Antarctica/DumontDUrville'), ('Antarctica/Macquarie', '(UTC +10:00) Antarctica/Macquarie'), ('Antarctica/Mawson', '(UTC +05:00) Antarctica/Mawson'), ('Antarctica/McMurdo', '(UTC +12:00) Antarctica/McMurdo'), ('Antarctica/Palmer', '(UTC -03:00) Antarctica/Palmer'), ('Antarctica/Rothera', '(UTC -03:00) Antarctica/Rothera'), ('Antarctica/South_Pole', '(UTC +12:00) Antarctica/South_Pole'), ('Antarctica/Syowa', '(UTC +03:00) Antarctica/Syowa'), ('Antarctica/Troll', '(UTC +00:00) Antarctica/Troll'), ('Antarctica/Vostok', '(UTC +06:00) Antarctica/Vostok'), ('Arctic/Longyearbyen', '(UTC +01:00) Arctic/Longyearbyen'), ('Asia/Aden', '(UTC +03:00) Asia/Aden'), ('Asia/Almaty', '(UTC +06:00) Asia/Almaty'), ('Asia/Amman', '(UTC +02:00) Asia/Amman'), ('Asia/Anadyr', '(UTC +12:00) Asia/Anadyr'), ('Asia/Aqtau', '(UTC +05:00) Asia/Aqtau'), ('Asia/Aqtobe', '(UTC +05:00) Asia/Aqtobe'), ('Asia/Ashgabat', '(UTC +05:00) Asia/Ashgabat'), ('Asia/Ashkhabad', '(UTC +05:00) Asia/Ashkhabad'), ('Asia/Atyrau', '(UTC +05:00) Asia/Atyrau'), ('Asia/Baghdad', '(UTC +03:00) Asia/Baghdad'), ('Asia/Bahrain', '(UTC +03:00) Asia/Bahrain'), ('Asia/Baku', '(UTC +04:00) Asia/Baku'), ('Asia/Bangkok', '(UTC +07:00) Asia/Bangkok'), ('Asia/Barnaul', '(UTC +07:00) Asia/Barnaul'), ('Asia/Beirut', '(UTC +02:00) Asia/Beirut'), ('Asia/Bishkek', '(UTC +06:00) Asia/Bishkek'), ('Asia/Brunei', '(UTC +08:00) Asia/Brunei'), ('Asia/Calcutta', '(UTC +05:30) Asia/Calcutta'), ('Asia/Chita', '(UTC +09:00) Asia/Chita'), ('Asia/Choibalsan', '(UTC +08:00) Asia/Choibalsan'), ('Asia/Chongqing', '(UTC +08:00) Asia/Chongqing'), ('Asia/Chungking', '(UTC +08:00) Asia/Chungking'), ('Asia/Colombo', '(UTC +05:30) Asia/Colombo'), ('Asia/Dacca', '(UTC +06:00) Asia/Dacca'), ('Asia/Damascus', '(UTC +02:00) Asia/Damascus'), ('Asia/Dhaka', '(UTC +06:00) Asia/Dhaka'), ('Asia/Dili', '(UTC +09:00) Asia/Dili'), ('Asia/Dubai', '(UTC +04:00) Asia/Dubai'), ('Asia/Dushanbe', '(UTC +05:00) Asia/Dushanbe'), ('Asia/Famagusta', '(UTC +02:00) Asia/Famagusta'), ('Asia/Gaza', '(UTC +02:00) Asia/Gaza'), ('Asia/Harbin', '(UTC +08:00) Asia/Harbin'), ('Asia/Hebron', '(UTC +02:00) Asia/Hebron'), ('Asia/Ho_Chi_Minh', '(UTC +07:00) Asia/Ho_Chi_Minh'), ('Asia/Hong_Kong', '(UTC +08:00) Asia/Hong_Kong'), ('Asia/Hovd', '(UTC +07:00) Asia/Hovd'), ('Asia/Irkutsk', '(UTC +08:00) Asia/Irkutsk'), ('Asia/Istanbul', '(UTC +03:00) Asia/Istanbul'), ('Asia/Jakarta', '(UTC +07:00) Asia/Jakarta'), ('Asia/Jayapura', '(UTC +09:00) Asia/Jayapura'), ('Asia/Jerusalem', '(UTC +02:00) Asia/Jerusalem'), ('Asia/Kabul', '(UTC +04:30) Asia/Kabul'), ('Asia/Kamchatka', '(UTC +12:00) Asia/Kamchatka'), ('Asia/Karachi', '(UTC +05:00) Asia/Karachi'), ('Asia/Kashgar', '(UTC +06:00) Asia/Kashgar'), ('Asia/Kathmandu', '(UTC +05:45) Asia/Kathmandu'), ('Asia/Katmandu', '(UTC +05:45) Asia/Katmandu'), ('Asia/Khandyga', '(UTC +09:00) Asia/Khandyga'), ('Asia/Kolkata', '(UTC +05:30) Asia/Kolkata'), ('Asia/Krasnoyarsk', '(UTC +07:00) Asia/Krasnoyarsk'), ('Asia/Kuala_Lumpur', '(UTC +08:00) Asia/Kuala_Lumpur'), ('Asia/Kuching', '(UTC +08:00) Asia/Kuching'), ('Asia/Kuwait', '(UTC +03:00) Asia/Kuwait'), ('Asia/Macao', '(UTC +08:00) Asia/Macao'), ('Asia/Macau', '(UTC +08:00) Asia/Macau'), ('Asia/Magadan', '(UTC +11:00) Asia/Magadan'), ('Asia/Makassar', '(UTC +08:00) Asia/Makassar'), ('Asia/Manila', '(UTC +08:00) Asia/Manila'), ('Asia/Muscat', '(UTC +04:00) Asia/Muscat'), ('Asia/Nicosia', '(UTC +02:00) Asia/Nicosia'), ('Asia/Novokuznetsk', '(UTC +07:00) Asia/Novokuznetsk'), ('Asia/Novosibirsk', '(UTC +07:00) Asia/Novosibirsk'), ('Asia/Omsk', '(UTC +06:00) Asia/Omsk'), ('Asia/Oral', '(UTC +05:00) Asia/Oral'), ('Asia/Phnom_Penh', '(UTC +07:00) Asia/Phnom_Penh'), ('Asia/Pontianak', '(UTC +07:00) Asia/Pontianak'), ('Asia/Pyongyang', '(UTC +09:00) Asia/Pyongyang'), ('Asia/Qatar', '(UTC +03:00) Asia/Qatar'), ('Asia/Qostanay', '(UTC +06:00) Asia/Qostanay'), ('Asia/Qyzylorda', '(UTC +05:00) Asia/Qyzylorda'), ('Asia/Rangoon', '(UTC +06:30) Asia/Rangoon'), ('Asia/Riyadh', '(UTC +03:00) Asia/Riyadh'), ('Asia/Saigon', '(UTC +07:00) Asia/Saigon'), ('Asia/Sakhalin', '(UTC +11:00) Asia/Sakhalin'), ('Asia/Samarkand', '(UTC +05:00) Asia/Samarkand'), ('Asia/Seoul', '(UTC +09:00) Asia/Seoul'), ('Asia/Shanghai', '(UTC +08:00) Asia/Shanghai'), ('Asia/Singapore', '(UTC +08:00) Asia/Singapore'), ('Asia/Srednekolymsk', '(UTC +11:00) Asia/Srednekolymsk'), ('Asia/Taipei', '(UTC +08:00) Asia/Taipei'), ('Asia/Tashkent', '(UTC +05:00) Asia/Tashkent'), ('Asia/Tbilisi', '(UTC +04:00) Asia/Tbilisi'), ('Asia/Tehran', '(UTC +03:30) Asia/Tehran'), ('Asia/Tel_Aviv', '(UTC +02:00) Asia/Tel_Aviv'), ('Asia/Thimbu', '(UTC +06:00) Asia/Thimbu'), ('Asia/Thimphu', '(UTC +06:00) Asia/Thimphu'), ('Asia/Tokyo', '(UTC +09:00) Asia/Tokyo'), ('Asia/Tomsk', '(UTC +07:00) Asia/Tomsk'), ('Asia/Ujung_Pandang', '(UTC +08:00) Asia/Ujung_Pandang'), ('Asia/Ulaanbaatar', '(UTC +08:00) Asia/Ulaanbaatar'), ('Asia/Ulan_Bator', '(UTC +08:00) Asia/Ulan_Bator'), ('Asia/Urumqi', '(UTC +06:00) Asia/Urumqi'), ('Asia/Ust-Nera', '(UTC +10:00) Asia/Ust-Nera'), ('Asia/Vientiane', '(UTC +07:00) Asia/Vientiane'), ('Asia/Vladivostok', '(UTC +10:00) Asia/Vladivostok'), ('Asia/Yakutsk', '(UTC +09:00) Asia/Yakutsk'), ('Asia/Yangon', '(UTC +06:30) Asia/Yangon'), ('Asia/Yekaterinburg', '(UTC +05:00) Asia/Yekaterinburg'), ('Asia/Yerevan', '(UTC +04:00) Asia/Yerevan'), ('Atlantic/Azores', '(UTC -01:00) Atlantic/Azores'), ('Atlantic/Bermuda', '(UTC -04:00) Atlantic/Bermuda'), ('Atlantic/Canary', '(UTC +00:00) Atlantic/Canary'), ('Atlantic/Cape_Verde', '(UTC -01:00) Atlantic/Cape_Verde'), ('Atlantic/Faeroe', '(UTC +00:00) Atlantic/Faeroe'), ('Atlantic/Faroe', '(UTC +00:00) Atlantic/Faroe'), ('Atlantic/Jan_Mayen', '(UTC +01:00) Atlantic/Jan_Mayen'), ('Atlantic/Madeira', '(UTC +00:00) Atlantic/Madeira'), ('Atlantic/Reykjavik', '(UTC +00:00) Atlantic/Reykjavik'), ('Atlantic/South_Georgia', '(UTC -02:00) Atlantic/South_Georgia'), ('Atlantic/St_Helena', '(UTC +00:00) Atlantic/St_Helena'), ('Atlantic/Stanley', '(UTC -03:00) Atlantic/Stanley'), ('Australia/ACT', '(UTC +10:00) Australia/ACT'), ('Australia/Adelaide', '(UTC +09:30) Australia/Adelaide'), ('Australia/Brisbane', '(UTC +10:00) Australia/Brisbane'), ('Australia/Broken_Hill', '(UTC +09:30) Australia/Broken_Hill'), ('Australia/Canberra', '(UTC +10:00) Australia/Canberra'), ('Australia/Currie', '(UTC +10:00) Australia/Currie'), ('Australia/Darwin', '(UTC +09:30) Australia/Darwin'), ('Australia/Eucla', '(UTC +08:45) Australia/Eucla'), ('Australia/Hobart', '(UTC +10:00) Australia/Hobart'), ('Australia/LHI', '(UTC +10:30) Australia/LHI'), ('Australia/Lindeman', '(UTC +10:00) Australia/Lindeman'), ('Australia/Lord_Howe', '(UTC +10:30) Australia/Lord_Howe'), ('Australia/Melbourne', '(UTC +10:00) Australia/Melbourne'), ('Australia/North', '(UTC +09:30) Australia/North'), ('Australia/NSW', '(UTC +10:00) Australia/NSW'), ('Australia/Perth', '(UTC +08:00) Australia/Perth'), ('Australia/Queensland', '(UTC +10:00) Australia/Queensland'), ('Australia/South', '(UTC +09:30) Australia/South'), ('Australia/Sydney', '(UTC +10:00) Australia/Sydney'), ('Australia/Tasmania', '(UTC +10:00) Australia/Tasmania'), ('Australia/Victoria', '(UTC +10:00) Australia/Victoria'), ('Australia/West', '(UTC +08:00) Australia/West'), ('Australia/Yancowinna', '(UTC +09:30) Australia/Yancowinna'), ('Brazil/Acre', '(UTC -05:00) Brazil/Acre'), ('Brazil/DeNoronha', '(UTC -02:00) Brazil/DeNoronha'), ('Brazil/East', '(UTC -03:00) Brazil/East'), ('Brazil/West', '(UTC -04:00) Brazil/West'), ('Canada/Atlantic', '(UTC -04:00) Canada/Atlantic'), ('Canada/Central', '(UTC -06:00) Canada/Central'), ('Canada/Eastern', '(UTC -05:00) Canada/Eastern'), ('Canada/Mountain', '(UTC -07:00) Canada/Mountain'), ('Canada/Newfoundland', '(UTC -03:30) Canada/Newfoundland'), ('Canada/Pacific', '(UTC -08:00) Canada/Pacific'), ('Canada/Saskatchewan', '(UTC -06:00) Canada/Saskatchewan'), ('Canada/Yukon', '(UTC -07:00) Canada/Yukon'), ('Chile/Continental', '(UTC -04:00) Chile/Continental'), ('Chile/EasterIsland', '(UTC -06:00) Chile/EasterIsland'), ('Europe/Amsterdam', '(UTC +01:00) Europe/Amsterdam'), ('Europe/Andorra', '(UTC +01:00) Europe/Andorra'), ('Europe/Astrakhan', '(UTC +04:00) Europe/Astrakhan'), ('Europe/Athens', '(UTC +02:00) Europe/Athens'), ('Europe/Belfast', '(UTC +00:00) Europe/Belfast'), ('Europe/Belgrade', '(UTC +01:00) Europe/Belgrade'), ('Europe/Berlin', '(UTC +01:00) Europe/Berlin'), ('Europe/Bratislava', '(UTC +01:00) Europe/Bratislava'), ('Europe/Brussels', '(UTC +01:00) Europe/Brussels'), ('Europe/Bucharest', '(UTC +02:00) Europe/Bucharest'), ('Europe/Budapest', '(UTC +01:00) Europe/Budapest'), ('Europe/Busingen', '(UTC +01:00) Europe/Busingen'), ('Europe/Chisinau', '(UTC +02:00) Europe/Chisinau'), ('Europe/Copenhagen', '(UTC +01:00) Europe/Copenhagen'), ('Europe/Dublin', '(UTC +01:00) Europe/Dublin'), ('Europe/Gibraltar', '(UTC +01:00) Europe/Gibraltar'), ('Europe/Guernsey', '(UTC +00:00) Europe/Guernsey'), ('Europe/Helsinki', '(UTC +02:00) Europe/Helsinki'), ('Europe/Isle_of_Man', '(UTC +00:00) Europe/Isle_of_Man'), ('Europe/Istanbul', '(UTC +03:00) Europe/Istanbul'), ('Europe/Jersey', '(UTC +00:00) Europe/Jersey'), ('Europe/Kaliningrad', '(UTC +02:00) Europe/Kaliningrad'), ('Europe/Kiev', '(UTC +02:00) Europe/Kiev'), ('Europe/Kirov', '(UTC +03:00) Europe/Kirov'), ('Europe/Lisbon', '(UTC +00:00) Europe/Lisbon'), ('Europe/Ljubljana', '(UTC +01:00) Europe/Ljubljana'), ('Europe/London', '(UTC +00:00) Europe/London'), ('Europe/Luxembourg', '(UTC +01:00) Europe/Luxembourg'), ('Europe/Madrid', '(UTC +01:00) Europe/Madrid'), ('Europe/Malta', '(UTC +01:00) Europe/Malta'), ('Europe/Mariehamn', '(UTC +02:00) Europe/Mariehamn'), ('Europe/Minsk', '(UTC +03:00) Europe/Minsk'), ('Europe/Monaco', '(UTC +01:00) Europe/Monaco'), ('Europe/Moscow', '(UTC +03:00) Europe/Moscow'), ('Europe/Nicosia', '(UTC +02:00) Europe/Nicosia'), ('Europe/Oslo', '(UTC +01:00) Europe/Oslo'), ('Europe/Paris', '(UTC +01:00) Europe/Paris'), ('Europe/Podgorica', '(UTC +01:00) Europe/Podgorica'), ('Europe/Prague', '(UTC +01:00) Europe/Prague'), ('Europe/Riga', '(UTC +02:00) Europe/Riga'), ('Europe/Rome', '(UTC +01:00) Europe/Rome'), ('Europe/Samara', '(UTC +04:00) Europe/Samara'), ('Europe/San_Marino', '(UTC +01:00) Europe/San_Marino'), ('Europe/Sarajevo', '(UTC +01:00) Europe/Sarajevo'), ('Europe/Saratov', '(UTC +04:00) Europe/Saratov'), ('Europe/Simferopol', '(UTC +03:00) Europe/Simferopol'), ('Europe/Skopje', '(UTC +01:00) Europe/Skopje'), ('Europe/Sofia', '(UTC +02:00) Europe/Sofia'), ('Europe/Stockholm', '(UTC +01:00) Europe/Stockholm'), ('Europe/Tallinn', '(UTC +02:00) Europe/Tallinn'), ('Europe/Tirane', '(UTC +01:00) Europe/Tirane'), ('Europe/Tiraspol', '(UTC +02:00) Europe/Tiraspol'), ('Europe/Ulyanovsk', '(UTC +04:00) Europe/Ulyanovsk'), ('Europe/Uzhgorod', '(UTC +02:00) Europe/Uzhgorod'), ('Europe/Vaduz', '(UTC +01:00) Europe/Vaduz'), ('Europe/Vatican', '(UTC +01:00) Europe/Vatican'), ('Europe/Vienna', '(UTC +01:00) Europe/Vienna'), ('Europe/Vilnius', '(UTC +02:00) Europe/Vilnius'), ('Europe/Volgograd', '(UTC +03:00) Europe/Volgograd'), ('Europe/Warsaw', '(UTC +01:00) Europe/Warsaw'), ('Europe/Zagreb', '(UTC +01:00) Europe/Zagreb'), ('Europe/Zaporozhye', '(UTC +02:00) Europe/Zaporozhye'), ('Europe/Zurich', '(UTC +01:00) Europe/Zurich'), ('Indian/Antananarivo', '(UTC +03:00) Indian/Antananarivo'), ('Indian/Chagos', '(UTC +06:00) Indian/Chagos'), ('Indian/Christmas', '(UTC +07:00) Indian/Christmas'), ('Indian/Cocos', '(UTC +06:30) Indian/Cocos'), ('Indian/Comoro', '(UTC +03:00) Indian/Comoro'), ('Indian/Kerguelen', '(UTC +05:00) Indian/Kerguelen'), ('Indian/Mahe', '(UTC +04:00) Indian/Mahe'), ('Indian/Maldives', '(UTC +05:00) Indian/Maldives'), ('Indian/Mauritius', '(UTC +04:00) Indian/Mauritius'), ('Indian/Mayotte', '(UTC +03:00) Indian/Mayotte'), ('Indian/Reunion', '(UTC +04:00) Indian/Reunion'), ('Mexico/BajaNorte', '(UTC -08:00) Mexico/BajaNorte'), ('Mexico/BajaSur', '(UTC -07:00) Mexico/BajaSur'), ('Mexico/General', '(UTC -06:00) Mexico/General'), ('Pacific/Apia', '(UTC +13:00) Pacific/Apia'), ('Pacific/Auckland', '(UTC +12:00) Pacific/Auckland'), ('Pacific/Bougainville', '(UTC +11:00) Pacific/Bougainville'), ('Pacific/Chatham', '(UTC +12:45) Pacific/Chatham'), ('Pacific/Chuuk', '(UTC +10:00) Pacific/Chuuk'), ('Pacific/Easter', '(UTC -06:00) Pacific/Easter'), ('Pacific/Efate', '(UTC +11:00) Pacific/Efate'), ('Pacific/Enderbury', '(UTC +13:00) Pacific/Enderbury'), ('Pacific/Fakaofo', '(UTC +13:00) Pacific/Fakaofo'), ('Pacific/Fiji', '(UTC +12:00) Pacific/Fiji'), ('Pacific/Funafuti', '(UTC +12:00) Pacific/Funafuti'), ('Pacific/Galapagos', '(UTC -06:00) Pacific/Galapagos'), ('Pacific/Gambier', '(UTC -09:00) Pacific/Gambier'), ('Pacific/Guadalcanal', '(UTC +11:00) Pacific/Guadalcanal'), ('Pacific/Guam', '(UTC +10:00) Pacific/Guam'), ('Pacific/Honolulu', '(UTC -10:00) Pacific/Honolulu'), ('Pacific/Johnston', '(UTC -10:00) Pacific/Johnston'), ('Pacific/Kiritimati', '(UTC +14:00) Pacific/Kiritimati'), ('Pacific/Kosrae', '(UTC +11:00) Pacific/Kosrae'), ('Pacific/Kwajalein', '(UTC +12:00) Pacific/Kwajalein'), ('Pacific/Majuro', '(UTC +12:00) Pacific/Majuro'), ('Pacific/Marquesas', '(UTC -09:30) Pacific/Marquesas'), ('Pacific/Midway', '(UTC -11:00) Pacific/Midway'), ('Pacific/Nauru', '(UTC +12:00) Pacific/Nauru'), ('Pacific/Niue', '(UTC -11:00) Pacific/Niue'), ('Pacific/Norfolk', '(UTC +11:00) Pacific/Norfolk'), ('Pacific/Noumea', '(UTC +11:00) Pacific/Noumea'), ('Pacific/Pago_Pago', '(UTC -11:00) Pacific/Pago_Pago'), ('Pacific/Palau', '(UTC +09:00) Pacific/Palau'), ('Pacific/Pitcairn', '(UTC -08:00) Pacific/Pitcairn'), ('Pacific/Pohnpei', '(UTC +11:00) Pacific/Pohnpei'), ('Pacific/Ponape', '(UTC +11:00) Pacific/Ponape'), ('Pacific/Port_Moresby', '(UTC +10:00) Pacific/Port_Moresby'), ('Pacific/Rarotonga', '(UTC -10:00) Pacific/Rarotonga'), ('Pacific/Saipan', '(UTC +10:00) Pacific/Saipan'), ('Pacific/Samoa', '(UTC -11:00) Pacific/Samoa'), ('Pacific/Tahiti', '(UTC -10:00) Pacific/Tahiti'), ('Pacific/Tarawa', '(UTC +12:00) Pacific/Tarawa'), ('Pacific/Tongatapu', '(UTC +13:00) Pacific/Tongatapu'), ('Pacific/Truk', '(UTC +10:00) Pacific/Truk'), ('Pacific/Wake', '(UTC +12:00) Pacific/Wake'), ('Pacific/Wallis', '(UTC +12:00) Pacific/Wallis'), ('Pacific/Yap', '(UTC +10:00) Pacific/Yap'), ('US/Alaska', '(UTC -09:00) US/Alaska'), ('US/Aleutian', '(UTC -10:00) US/Aleutian'), ('US/Arizona', '(UTC -07:00) US/Arizona'), ('US/Central', '(UTC -06:00) US/Central'), ('US/East-Indiana', '(UTC -05:00) US/East-Indiana'), ('US/Eastern', '(UTC -05:00) US/Eastern'), ('US/Hawaii', '(UTC -10:00) US/Hawaii'), ('US/Indiana-Starke', '(UTC -06:00) US/Indiana-Starke'), ('US/Michigan', '(UTC -05:00) US/Michigan'), ('US/Mountain', '(UTC -07:00) US/Mountain'), ('US/Pacific', '(UTC -08:00) US/Pacific'), ('US/Samoa', '(UTC -11:00) US/Samoa'), ('Etc/GMT', 'Etc/Greenwich')], default='Etc/GMT', max_length=63, verbose_name='Timezone')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='profiles', to='core.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
