---
title: Смарт-маркеры в заголовках и нижних колонтитулах | Aspose.Cells for Python via Java
linktitle: Smart Markers в колонтитулах | Aspose.Cells
description: Размещайте заполнители Smart Marker в заголовках и нижних колонтитулах страниц с помощью синтаксиса двойных угловых скобок и переключателя WorkbookDesigner.setEnableHeaderFooterMarkers, используя табличные строки или JSON-источники данных, а также связывайте изображения через data URI, в Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Aspose.Cells for Python via Java, Смарт-маркеры, заголовки, нижние колонтитулы, маркеры заголовков и нижних колонтитулов, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, ICellsDataTable, пользовательская табличная таблица, привязка данных, изображение, data URI, Python via Java
type: docs
weight: 196
url: /ru/python-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Заголовки и нижние колонтитулы страниц обычно содержат метаданные отчёта, такие как название отчёта, период отчёта, автор и отдел. Когда эта информация уже присутствует в источнике данных, используемом для заполнения рабочей книги, её ручное дублирование создаёт ненужную избыточность.  
Классический синтаксис Smart Marker, `&=Source.Field`, обрабатывается в ячейках тела **рабочего листа**. Если разместить классический маркер в заголовке или нижнем колонтитуле через `PageSetup.setHeader` или `PageSetup.setFooter`, он остаётся буквальным текстом, поскольку строки заголовка и нижнего колонтитула не входят в сетку ячеек листа, просматриваемую `WorkbookDesigner.process()`.  
Начиная с **Aspose.Cells for Python via Java 26.11**, переключатель `WorkbookDesigner.setEnableHeaderFooterMarkers`, который по умолчанию имеет значение `False`, заставляет `process()` разрешать заполнители, записанные как `<<Source.Field>>` в строках заголовка и нижнего колонтитула — установите его в `True` перед вызовом `process()`. Заполнители в заголовке и нижнем колонтитуле используют тот же источник данных, что и маркеры в теле.  
Каждый заголовок и нижний колонтитул содержит три адресных секции:  
- Секция `0` — левая.  
- Секция `1` — центральная.  
- Секция `2` — правая.  
Используйте `PageSetup.setHeader(int section, str value)` и `PageSetup.setFooter(int section, str value)` для записи этих секций. После обработки используйте `PageSetup.getHeader(int section)` и `PageSetup.getFooter(int section)` для получения готового текста.

{{% alert color="primary" %}}
Заполнитель вида `<<Source.Field>>` вставляет значение поля как текст в строку секции. Изображения привязываются с помощью суффикса `(picture)` и значения data-URI.
{{% /alert %}}

## **Включение маркеров заголовков/нижних колонтитулов с пользовательской табличной таблицей**
Используйте следующую последовательность для разрешения заполнителей заголовка и нижнего колонтитула с пользовательским табличным источником данных в **Aspose.Cells for Python via Java 26.11**:
1. Создайте объект `Workbook` и получите его первый `Worksheet` с индексом `0`, используя `workbook.getWorksheets().get(0)`.
2. Запишите заполнители `<<Source.Field>>` в необходимые секции заголовка и нижнего колонтитула с помощью `worksheet.getPageSetup().setHeader(section, value)` и `worksheet.getPageSetup().setFooter(section, value)`.
3. Определите небольшой класс, реализующий `ICellsDataTable`, чтобы предоставить табличные данные строк — имена столбцов, количество строк и курсор с методами `beforeFirst()`, `next()` и `get()` — и используйте имя источника, совпадающее с префиксом, используемым в заполнителях. Например, источник с именем `node` поддерживает заполнители вида `<<node.Name>>`. Обычный класс Python или список словарей НЕ привязываются на этой платформе; реализация `ICellsDataTable` является пользовательским объектным источником данных.
4. Создайте объект `WorkbookDesigner` для рабочей книги.
5. Вызовите `designer.setEnableHeaderFooterMarkers(True)` перед обработкой.
6. Привяжите таблицу и имя источника с помощью `designer.setDataSource("node", table)`.
7. Вызовите `designer.process()`.
8. После обработки заполнители исчезают из текста заголовка или нижнего колонтитула. Используйте `worksheet.getPageSetup().getHeader(section)` и `worksheet.getPageSetup().getFooter(section)`, чтобы получить завершённые строки секций.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name", "Author"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>")
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
print("Footer: " + worksheet.getPageSetup().getFooter(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
jpype.shutdownJVM()
```

## **Использование JSON-источника данных**
Вы можете использовать JSON вместо пользовательского `ICellsDataTable`, когда данные отчёта уже доступны в формате JSON. Вызовите `designer.setJsonDataSource(name, json)`, чтобы привязать источник.  
Аргумент `name` играет такую же роль, как имя источника, используемое с табличными данными. Например, имя `node` поддерживает заполнители `<<node.Company>>` и `<<node.Title>>`.  
Передайте данные строк непосредственно в `setJsonDataSource`:
- Массив строк, например JSON-массив, содержащий один или несколько объектов строки, поддерживается.
- Один объект строки также может быть передан напрямую.
- Не оборачивайте строки под именованным верхнего уровня ключом, например `{"rows":[...]}`. Такой обёртка не соответствует ожидаемому входному формату, ориентированному на строки, для данного рабочего процесса.  
Один JSON-источник может заполнять оба типа маркеров за один вызов `process()`. Он может разрешать классический маркер `&=` в ячейке тела листа и заполнители в двойных угловых скобках `<<>>` в секциях заголовка и нижнего колонтитула. По-прежнему необходимо включить `setEnableHeaderFooterMarkers`, чтобы заполнители в заголовке и нижнем колонтитуле были обработаны.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>")
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>")
worksheet.getCells().get("A1").putValue("&=node.Company")
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setJsonDataSource(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.getPageSetup().getHeader(0))
print("Right: " + worksheet.getPageSetup().getHeader(2))
print("Body: " + worksheet.getCells().get("A1").getStringValue())
workbook.save("HeaderFooterJsonMarkers.xlsx")
jpype.shutdownJVM()
```

## **Семантика переключателя и источника с несколькими строками**
Настройка маркеров заголовка и нижнего колонтитула имеет значение `False` по умолчанию, и `designer.setEnableHeaderFooterMarkers(True)` управляет только заполнителями `<<Source.Field>>` в заголовке и нижнем колонтитуле. Когда переключатель выключен, `process()` по-прежнему обрабатывает классические маркеры `&=` в теле листа, но заполнители `<<Source.Field>>` в заголовке или нижнем колонтитуле остаются буквальным текстом.  
Секция заголовка или нижнего колонтитула представляет собой одну строку, а не повторяющийся диапазон. Если источник данных содержит несколько строк, первая строка поставляет значения заголовка и нижнего колонтитула. После разрешения эти значения становятся обычным текстом заголовка или нижнего колонтитула. Они сохраняются в рабочей книге после вызова `workbook.save(...)` и присутствуют при последующей загрузке сохранённой книги.  
В следующем примере создаются две рабочие книги на основе одного и того же табличного источника с несколькими строками, чтобы сравнить поведение при отключённом и включённом переключателе. `plainDesigner` оставляет заполнитель без изменений, тогда как `enabledDesigner` разрешает его, используя первую строку.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
table = NodeTable([
    ("First Row",),
    ("Second Row",),
])
# Without the switch the placeholder stays literal text
plain_workbook = Workbook()
plain_sheet = plain_workbook.getWorksheets().get(0)
plain_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
plain_designer = WorkbookDesigner(plain_workbook)
plain_designer.setDataSource("node", table)
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = Workbook()
enabled_sheet = enabled_workbook.getWorksheets().get(0)
enabled_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
enabled_designer = WorkbookDesigner(enabled_workbook)
enabled_designer.setEnableHeaderFooterMarkers(True)
enabled_designer.setDataSource("node", table)
enabled_designer.process()
print("Without switch: " + plain_sheet.getPageSetup().getHeader(1))
print("With switch: " + enabled_sheet.getPageSetup().getHeader(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
jpype.shutdownJVM()
```

## **Привязка изображения к заголовку или нижнему колонтитулу**
Суффикс `(picture)` привязывает изображение к секции заголовка или нижнего колонтитула. Запишите `<<node.logo(picture)>>` там, где должно появиться изображение, и предоставьте значение поля в виде data URI – префикс `data:image/png;base64,`, за которым следует Base64-текст байтов изображения. Декодированное изображение обрабатывается как массив `byte[]`. Обычная строка Base64 без префикса `data:` не встраивает изображение.  
После `process()`:
1. Заполнитель заменяется на `&G` — стандартный код изображения для заголовка и нижнего колонтитула. Поскольку маркер превращается в код внутри строки секции, он может находиться внутри более длинного текста, например `Logo: <<node.logo(picture)>>`.
2. Байты изображения встраиваются в рабочую книгу как медиа-часть, прикреплённая к слою рисунков заголовка/нижнего колонтитула данного листа, поэтому изображение печатается вместе с заголовком или нижним колонтитулом.

```python
import base64
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["logo"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    image_bytes = image_file.read()
logo_data = "data:image/png;base64," + base64.b64encode(image_bytes).decode("ascii")
table = NodeTable([(logo_data,)])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
jpype.shutdownJVM()
```

Выводимый `&G` — это код изображения, который Excel интерпретирует при отрисовке заголовка; байты `logo.png` теперь находятся внутри `HeaderFooterPicture.xlsx`, и изображение печатается вместо кода.  
Чтобы использовать smart-маркеры в заголовках и нижних колонтитулах, запишите заполнители `<<Source.Field>>` в левую, центральную и правую секции заголовка или нижнего колонтитула с помощью `setHeader` и `setFooter`. Вызовите `designer.setEnableHeaderFooterMarkers(True)` перед вызовом `process()`, и предоставьте значения либо через `designer.setDataSource("node", table)` с пользовательской реализацией `ICellsDataTable`, либо через `designer.setJsonDataSource(name, json)`. Прочитайте завершённые секции с помощью `getHeader` и `getFooter`. Один и тот же источник данных может заполнять маркеры тела и заполнители заголовка или нижнего колонтитула за один проход обработки. Добавьте суффикс `(picture)` с значением data-URI, чтобы привязать изображение к секции.

## Сопутствующие статьи
- [Отображение массива из одной ячейки SmartMarker](/cells/ru/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python" >}}