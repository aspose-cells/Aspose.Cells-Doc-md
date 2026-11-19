---
title: Умные маркеры в верхних и нижних колонтитулах | Aspose.Cells .NET
linktitle: Умные маркеры в колонтитулах | Aspose.Cells
description: Размещайте заполнители Smart Marker в заголовках и нижних колонтитулах страниц с помощью синтаксиса двойных угловых скобок и переключателя WorkbookDesigner.EnableHeaderFooterMarkers, используя источники данных DataTable или JSON, а также привязывайте изображения через data URI в Aspose.Cells for .NET.
keywords: Aspose.Cells, Умные маркеры, заголовки, нижние колонтитулы, маркеры заголовков и нижних колонтитулов, EnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, SetHeader, SetFooter, SetJsonDataSource, DataTable, привязка данных, изображение, data URI, C#
type: docs
weight: 196
url: /ru/net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Верхние и нижние колонтитулы страниц обычно содержат метаданные отчёта, такие как название отчёта, период отчёта, автор и отдел. Когда эта информация уже присутствует в источнике данных, используемом для заполнения рабочей книги, её ручное дублирование создаёт ненужное повторение.  
Классический синтаксис Smart Marker, `&=Source.Field`, обрабатывается в ячейках тела рабочего листа. Если разместить классический маркер в заголовке или нижнем колонтитуле с помощью `PageSetup.SetHeader` или `PageSetup.SetFooter`, он останется дословным текстом, поскольку строки заголовков и нижних колонтитулов не являются частью сетки ячеек рабочего листа, сканируемой `WorkbookDesigner.Process()`.  
Начиная с **Aspose.Cells for .NET 26.11**, параметр `WorkbookDesigner.EnableHeaderFooterMarkers` по умолчанию имеет значение `false`. Установите его в `true` перед вызовом `Process()`, чтобы разрешить заполнители вида `<<Source.Field>>`, записанные в строках разделов верхних и нижних колонтитулов. Заполнители в заголовках и нижних колонтитулах используют тот же источник данных, что и маркеры в теле рабочего листа.  
Каждый заголовок и нижний колонтитул содержит три адресуемых раздела:
- Раздел `0` — левый раздел.
- Раздел `1` — центр.
- Раздел `2` — правый раздел.  
Используйте `PageSetup.SetHeader(int section, string value)` и `PageSetup.SetFooter(int section, string value)` для записи этих разделов. После обработки используйте `PageSetup.GetHeader(int section)` и `PageSetup.GetFooter(int section)` для получения готового текста.

{{% alert color="primary" %}}
Заполнитель вроде `<<Source.Field>>` вставляет значение поля как текст в строку раздела. Изображения привязываются с помощью суффикса `(picture)` и значения data-URI.
{{% /alert %}}

## **Включение маркеров заголовков/нижних колонтитулов с помощью DataTable**
Воспользуйтесь следующей последовательностью для разрешения заполнителей заголовков и нижних колонтитулов с помощью `DataTable` в **Aspose.Cells for .NET 26.11**:
1. Создайте объект `Workbook` и получите первый `Worksheet` с индексом `0`.
2. Запишите заполнители `<<Source.Field>>` в нужные разделы заголовков и нижних колонтитулов с помощью `PageSetup.SetHeader` и `PageSetup.SetFooter`.
3. Создайте `DataTable`, имя которой совпадает с префиксом источника, используемым в заполнителях. Например, таблица с именем `node` поддерживает заполнители вроде `<<node.Name>>`.
4. Создайте `WorkbookDesigner` для рабочей книги.
5. Установите `designer.EnableHeaderFooterMarkers` в `true` перед обработкой.
6. Присоедините таблицу с помощью `designer.SetDataSource(table)`.
7. Вызовите `designer.Process()`.
8. После обработки заполнители исчезнут из текста заголовков и нижних колонтитулов. Используйте `GetHeader` и `GetFooter` для получения готовых строк разделов.

```csharp
using System;
using System.Data;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.PageSetup.SetHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.PageSetup.SetFooter(1, "Prepared by <<node.Author>>");
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Columns.Add("Author");
table.Rows.Add("Q4 2026", "Aspose.Cells");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
Console.WriteLine("Footer: " + worksheet.PageSetup.GetFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.Save("HeaderFooterSmartMarkers.xlsx");
```

## **Использование JSON в качестве источника данных**
Вы можете использовать JSON вместо `DataTable`, когда данные отчёта уже доступны в формате JSON. Вызовите `WorkbookDesigner.SetJsonDataSource(string name, string json)`, чтобы присоединить источник.  
Аргумент `name` играет ту же роль, что и имя `DataTable`. Например, имя `node` поддерживает заполнители `<<node.Company>>` и `<<node.Title>>`.  
Передайте данные строк напрямую в `SetJsonDataSource`:
- Массив строк, например JSON-массив, содержащий один или несколько объектов строк, поддерживается.
- Можно также передать один объект строки напрямую.
- Не оборачивайте строки в именованный верхний ключ, например `{"rows":[...]}`. Такая обёртка не соответствует ожидаемой структуре ввода, ориентированной на строки, для данного процесса.  
Один JSON-источник может заполнять оба стиля маркеров за один вызов `Process()`. Он может разрешать классический маркер `&=` в ячейке тела рабочего листа и заполнители с двойными угловыми скобками `<<>>` в разделах заголовков и нижних колонтитулов. По-прежнему необходимо включить `EnableHeaderFooterMarkers`, чтобы заполнители в заголовках и нижних колонтитулах были разрешены.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.PageSetup.SetHeader(0, "<<node.Company>>");
worksheet.PageSetup.SetHeader(2, "Page <<node.Title>>");
worksheet.Cells["A1"].PutValue("&=node.Company");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
designer.Process();
Console.WriteLine("Left: " + worksheet.PageSetup.GetHeader(0));
Console.WriteLine("Right: " + worksheet.PageSetup.GetHeader(2));
Console.WriteLine("Body: " + worksheet.Cells["A1"].StringValue);
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.Save("HeaderFooterJsonMarkers.xlsx");
```

## **Семантика переключателя и источника с несколькими строками**
`EnableHeaderFooterMarkers` по умолчанию `false`, и переключатель управляет только заполнителями `<<Source.Field>>` в заголовках и нижних колонтитулах. Когда переключатель отключён, `Process()` всё равно разрешает классические маркеры `&=` в теле рабочего листа, но заполнитель `<<Source.Field>>` в заголовке или нижнем колонтитуле остаётся дословным текстом.  
Раздел заголовка или нижнего колонтитула представляет собой одну строку, а не повторяющийся диапазон. Если источник данных содержит несколько строк, первая строка предоставляет значения для заголовков и нижних колонтитулов. После разрешения значения становятся обычным текстом заголовка или нижнего колонтитула. Они сохраняются в рабочей книге после вызова `Save` и присутствуют при повторной загрузке сохранённой книги.  
В следующем примере создаются две рабочие книги на основе одного и того же `DataTable` с несколькими строками, чтобы сравнить поведение при отключённом и включённом переключателе. `plainDesigner` оставляет заполнитель без изменений, тогда как `enabledDesigner` разрешает его, используя первую строку.

```csharp
using System;
using System.Data;
using Aspose.Cells;
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Rows.Add("First Row");
table.Rows.Add("Second Row");
// Without the switch the placeholder stays literal text
Workbook plainWorkbook = new Workbook();
Worksheet plainSheet = plainWorkbook.Worksheets[0];
plainSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
plainDesigner.SetDataSource(table);
plainDesigner.Process();
// With the switch on, the FIRST row of a multi-row source wins
Workbook enabledWorkbook = new Workbook();
Worksheet enabledSheet = enabledWorkbook.Worksheets[0];
enabledSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
enabledDesigner.EnableHeaderFooterMarkers = true;
enabledDesigner.SetDataSource(table);
enabledDesigner.Process();
Console.WriteLine("Without switch: " + plainSheet.PageSetup.GetHeader(1));
Console.WriteLine("With switch: " + enabledSheet.PageSetup.GetHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.Save("HeaderFooterMarkersEnabled.xlsx");
```

## **Привязка изображения к заголовку или нижнему колонтитулу**
Суффикс `(picture)` привязывает изображение к разделу заголовка или нижнего колонтитула. Запишите `<<node.logo(picture)>>` в том месте, где должно появиться изображение, и передайте значение поля как data-URI — префикс `data:image/png;base64,`, за которым следует Base64-текст байтов изображения. Обычная строка Base64 без префикса `data:` не встраивает изображение.  
После `Process()`:
1. Заполнитель заменяется на `&G`, стандартный код изображения в заголовке и нижнем колонтитуле. Поскольку маркер становится кодом внутри строки раздела, он может находиться внутри более длинного текста, например `Logo: <<node.logo(picture)>>`.
2. Байты изображения встраиваются в рабочую книгу как медиа-часть, прикреплённая к слою рисунков заголовка/нижнего колонтитула этого листа, поэтому изображение печатается вместе с заголовком или нижним колонтитулом.

```csharp
using System;
using System.Data;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.PageSetup.SetHeader(1, "Logo: <<node.logo(picture)>>");
DataTable table = new DataTable("node");
table.Columns.Add("logo");
table.Rows.Add("data:image/png;base64," + Convert.ToBase64String(File.ReadAllBytes("logo.png")));
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
// This prints:
// Header: Logo: &G
workbook.Save("HeaderFooterPicture.xlsx");
```

Выведенный `&G` — это код изображения, который Excel интерпретирует при рендеринге заголовка — байты `logo.png` теперь находятся внутри `HeaderFooterPicture.xlsx`, и изображение печатается вместо кода.  
Чтобы использовать умные маркеры в заголовках и нижних колонтитулах, запишите заполнители `<<Source.Field>>` в левый, центральный и правый разделы заголовка или нижнего колонтитула с помощью `SetHeader` и `SetFooter`. Установите `EnableHeaderFooterMarkers` в `true` у `WorkbookDesigner` перед вызовом `Process()` и передайте значения либо через `SetDataSource(DataTable)`, либо через `SetJsonDataSource`. Прочитайте готовые разделы с помощью `GetHeader` и `GetFooter`. Один и тот же источник данных может заполнять маркеры в теле листа и заполнители в заголовках/нижних колонтитулах за один проход обработки. Добавьте суффикс `(picture)` со значением data-URI, чтобы привязать изображение к разделу.

## Сопутствующие статьи
- [Отображение одноклеточного массива с помощью SmartMarker](/cells/ru/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="csharp" >}}