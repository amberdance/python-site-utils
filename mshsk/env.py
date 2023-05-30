import re

PHP_CLOSE_TAG = "?>"
WRAP_OPEN_TAG = "<div class='container'>"
WRAP_CLOSE_TAG = "</div>"
COUNT_OF_BLANK_LINES = 2
BACKUP_FILENAME_POSTFIX = "hrd2cd.bak"
SECTIONS_COMPONENT_TEMPLATE = '<?php \n\
$APPLICATION->IncludeComponent("bitrix:menu", "citsk_section_buttons", array( \n\
    "COMPONENT_TEMPLATE" => "citsk_section_buttons", \n\
    "ROOT_MENU_TYPE" => "left",    // Тип меню для первого уровня \n\
    "MENU_CACHE_TYPE" => "N",    // Тип кеширования \n\
    "MENU_CACHE_TIME" => "3600",    // Время кеширования (сек.) \n\
    "MENU_CACHE_USE_GROUPS" => "Y",    // Учитывать права доступа \n\
    "MENU_CACHE_GET_VARS" => "",    // Значимые переменные запроса \n\
    "MAX_LEVEL" => "1",    // Уровень вложенности меню \n\
    "CHILD_MENU_TYPE" => "left",    // Тип меню для остальных уровней \n\
    "USE_EXT" => "N",    // Подключать файлы с именами вида .тип_меню.menu_ext.php \n\
    "DELAY" => "N",    // Откладывать выполнение шаблона меню \n\
    "ALLOW_MULTI_SELECT" => "N",    // Разрешить несколько активных пунктов одновременно \n\
    "COMPOSITE_FRAME_MODE" => "A",    // Голосование шаблона компонента по умолчанию \n\
    "COMPOSITE_FRAME_TYPE" => "AUTO",    // Содержимое компонента \n\
), false \n\
); \n\
?>'

php_close_tag_pattern = re.compile("(?<=\?>).*")
line_insert_index = 1
