---
title: Smart-маркеры в верхних и нижних колонтитулах | Aspose.Cells for Python via .NET
linktitle: Smart Markers в колонтитулах | Aspose.Cells
description: Разместите заполнители Smart Marker в верхних и нижних колонтитулах страниц с помощью синтаксиса двойных угловых скобок и переключателя WorkbookDesigner.enable_header_footer_markers, используя пользовательские реализации ICellsDataTable или JSON-источники данных, а также привяжите изображения через data-URI, в Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Smart-маркеры, верхние колонтитулы, нижние колонтитулы, маркеры верхних и нижних колонтитулов, enable_header_footer_markers, WorkbookDesigner, PageSetup, set_header, set_footer, set_json_data_source, set_data_source, ICellsDataTable, пользовательская табличная структура, привязка данных, изображение, data URI
type: docs
weight: 196
url: /ru/python-net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Варианты использования**
Верхние и нижние колонтитулы страниц обычно содержат метаданные отчёта, такие как название отчёта, период отчёта, автор и отдел. Когда эта информация уже присутствует в источнике данных, используемом для заполнения рабочей книги, её ручное дублирование создаёт ненужную избыточность.  
Классический синтаксис Smart Marker `&=Source.Field` обрабатывается в ячейках тела листа. Если разместить такой маркер в колонтитуле через `page_setup.set_header` или `page_setup.set_footer`, он останется буквальным текстом, поскольку строки колонтитулов не входят в сетку ячеек листа, сканируемую `workbook_designer.process()`.  
Начиная с **Aspose.Cells for Python via .NET 26.11**, переключатель `workbook_designer.enable_header_footer_markers` (по умолчанию `False`) заставляет `process()` заменять заполнители, записанные как `<<Source.Field>>`, в строках разделов колонтитулов — установите его в `True` перед вызовом `process()`. Заполнители колонтитулов используют тот же источник данных, что и маркеры в теле листа.  
Каждый колонтитул содержит три адресуемые секции:  
- Секция `0` — левая часть.  
- Секция `1` — центральная часть.  
- Секция `2` — правая часть.  
Используйте `page_setup.set_header(section, value)` и `page_setup.set_footer(section, value)` для записи этих секций. После обработки применяйте `page_setup.get_header(section)` и `page_setup.get_footer(section)` для получения готового текста.

{{% alert color="primary" %}}
Заполнитель вида `<<Source.Field>>` вставляет значение поля как текст в строку секции. Изображения привязываются с помощью суффикса `(picture)` и значения data-URI.  
{{% /alert %}}

## **Включение маркеров верхних/нижних колонтитулов с пользовательской табличной структурой**
Выполните следующую последовательность, чтобы разрешить заполнители колонтитулов с пользовательским табличным источником данных в **Aspose.Cells for Python via .NET 26.11**:  
1. Создайте объект `Workbook` и получите его первый `Worksheet` по индексу `0`.  
2. Запишите заполнители `<<Source.Field>>` в нужные секции колонтитулов с помощью `page_setup.set_header` и `page_setup.set_footer`.  
3. Определите небольший класс, реализующий `ICellsDataTable`, чтобы предоставить табличные данные строк — имена столбцов, количество строк и курсор с методами `before_first()`, `next()` и индексатором `__getitem__`. Используйте имя источника, соответствующее префиксу, используемому в заполнителях. Например, источник с именем `node` обслуживает заполнители `<<node.Name>>`. Обычный класс Python или список словарей НЕ привязываются в этой платформе; реализация `ICellsDataTable` — это пользовательский объект-источник данных.  
4. Создайте `WorkbookDesigner` для рабочей книги.  
5. Установите `designer.enable_header_footer_markers` в `True` перед обработкой.  
6. Привяжите таблицу и имя источника с помощью `designer.set_data_source("node", table)`.  
7. Вызовите `designer.process()`.  
8. После обработки заполнители исчезают из текста колонтитула. Используйте `get_header` и `get_footer` для получения готовых строк секций.  

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name", "Author"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.page_setup.set_header(1, "Quarterly Report - <<node.Name>>")
worksheet.page_setup.set_footer(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
print("Footer: " + worksheet.page_setup.get_footer(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
```

## **Использование JSON-источника данных**
Можно использовать JSON вместо пользовательского `ICellsDataTable`, когда данные отчёта уже доступны в JSON-формате. Вызовите `workbook_designer.set_json_data_source(name, json)`, чтобы присоединить источник.  
Аргумент `name` играет ту же роль, что и имя источника при работе с табличными данными. Например, имя `node` обслуживает заполнители `<<node.Company>>` и `<<node.Title>>`.  
Передайте данные строк непосредственно в `set_json_data_source`:  
- Массив строк, например JSON-массив, содержащий один или несколько объектов-строк, поддерживается.  
- Один объект-строка также может быть передан напрямую.  
- Не оборачивайте строки в верхний ключ, например `{"rows":[...]}`. Такой обёртка не соответствует ожидаемой форме ввода, ориентированной на строки, для данного рабочего процесса.  
Один JSON-источник может заполнять обе стилистики маркеров за один вызов `process()`. Он может разрешать классический маркер `&=` в ячейке тела листа и заполнители двойных угловых скобок `<<>>` в колонтитулах. Для разрешения заполнителей колонтитулов по-прежнему необходимо включить `enable_header_footer_markers`.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.page_setup.set_header(0, "<<node.Company>>")
worksheet.page_setup.set_header(2, "Page <<node.Title>>")
worksheet.cells.get("A1").put_value("&=node.Company")
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_json_data_source(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.page_setup.get_header(0))
print("Right: " + worksheet.page_setup.get_header(2))
print("Body: " + worksheet.cells.get("A1").string_value)
# This prints:
# Left: Aspose Pty Ltd
# Right: Page Half-Year Report
# Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx")
```

## **Семантика переключателя и многострочного источника**
`enable_header_footer_markers` по умолчанию `False`, и переключатель управляет только заполнителями `<<Source.Field>>` в колонтитулах. Когда переключатель выключен, `process()` всё равно обрабатывает классические маркеры `&=` в теле листа, но заполнитель `<<Source.Field>>` в колонтитуле остаётся буквальным текстом.  
Секция колонтитула представляет собой одну строку, а не повторяющийся блок. Если источник данных содержит несколько строк, первая строка обеспечивает значения колонтитулов. После разрешения значения становятся обычным текстом колонтитула. Они сохраняются в рабочей книге после вызова `save` и присутствуют при последующей загрузке книги.  
Ниже показан пример, создающий две рабочие книги на основе одного многострочного табличного источника, чтобы продемонстрировать различия при отключённом и включённом режиме. `plain_designer` оставляет заполнитель без изменений, тогда как `enabled_designer` заменяет его, используя первую строку.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
rows = [("First Row",), ("Second Row",)]
# Without the switch the placeholder stays literal text
plain_workbook = ac.Workbook()
plain_sheet = plain_workbook.worksheets[0]
plain_sheet.page_setup.set_header(1, "<<node.Name>>")
plain_designer = ac.WorkbookDesigner(plain_workbook)
plain_designer.set_data_source("node", NodeTable(rows))
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = ac.Workbook()
enabled_sheet = enabled_workbook.worksheets[0]
enabled_sheet.page_setup.set_header(1, "<<node.Name>>")
enabled_designer = ac.WorkbookDesigner(enabled_workbook)
enabled_designer.enable_header_footer_markers = True
enabled_designer.set_data_source("node", NodeTable(rows))
enabled_designer.process()
print("Without switch: " + plain_sheet.page_setup.get_header(1))
print("With switch: " + enabled_sheet.page_setup.get_header(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
```

## **Привязка изображения к колонтитулу**
Суффикс `(picture)` привязывает изображение к секции колонтитула. Запишите `<<node.logo(picture)>>` в месте, где должно появиться изображение, и передайте значение поля как data-URI — префикс `data:image/png;base64,`, за которым следует Base64-текст байтов изображения. Обычная строка Base64 без префикса `data:` не вставит изображение.  
После `process()`:  
1. Заполнитель заменяется на `&G` — стандартный код изображения в колонтитулах. Поскольку маркер превращается в код внутри строки секции, его можно разместить внутри более длинного текста, например `Logo: <<node.logo(picture)>>`.  
2. Байты изображения встраиваются в рабочую книгу как часть медиа, прикреплённая к слою рисунков колонтитулов соответствующего листа, поэтому изображение печатается вместе с колонтитулом.  

```python
import aspose.cells as ac
import base64
class LogoTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["logo"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.page_setup.set_header(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    logo_data_uri = "data:image/png;base64," + base64.b64encode(image_file.read()).decode("ascii")
table = LogoTable([(logo_data_uri,)])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
```

Печатный код `&G` — это код изображения, который Excel интерпретирует при рендеринге колонтитула; байты `logo.png` теперь находятся внутри файла `HeaderFooterPicture.xlsx`, и изображение печатается вместо кода.  
Чтобы использовать Smart Markers в колонтитулах, запишите заполнители `<<Source.Field>>` в левую, центральную и правую секции колонтитулов с помощью `set_header` и `set_footer`. Установите `enable_header_footer_markers` в `True` у `WorkbookDesigner` перед вызовом `process()` и передайте значения через `set_data_source("node", table)` с пользовательской реализацией `ICellsDataTable` или `set_json_data_source(name, json)`. Прочитайте готовые секции с помощью `get_header` и `get_footer`. Один и тот же источник данных может заполнять маркеры в теле листа и заполнители в колонтитулах за один проход обработки. Добавьте суффикс `(picture)` с значением data-URI, чтобы привязать изображение к секции.

## Сопутствующие статьи
- [Отображение массива в одной ячейке SmartMarker](/cells/ru/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python-net" >}}