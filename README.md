# parsing of phone numbers

## Задание

Компания с острова Jost Van Dyke делает сайт: стандартный справочник организаций. Клиенты на сайте ищут номера телефонов организаций. Номера телефонов устаревают. Из-за этого компания теряет клиентов.

Для каждой организации в базе хранится ссылка на её сайт и путь к странице контактов. Страниц контактов на одном сайте может быть несколько. Есть модуль, который умеет распознавать неактуальный номер. На вход он получает список номеров в формате 8KKKNNNNNNN.

Вам нужно написать модуль, который скачивает web-страницы, находит в тексте и выводит все распознанные номера телефонов в этом формате.

Номера по формату российские. Если для номера не указан код города — номер московский. Чем выше доля распознаваемых реальных номеров на странице и чем быстрее работает модуль — тем он лучше.

Здесь: https://hands.ru/company/about модуль должен найти номер, здесь: https://repetitors.info тоже. Страниц в базе может быть очень много!

В задании не нужно использовать тяжелые фреймворки или сохранять найденные номера в базу. Задание ориентировано буквально на несколько часов.

## Анализ
- из-за возможности отсутсвия кода города, модуль соберет ложные номера из-за регулярного выражения 
- не смог на первом сайте найти верный номер телефона. При получения доступа к страницы находится номер +7 495 137-07-20
