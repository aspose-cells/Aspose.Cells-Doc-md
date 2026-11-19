---
title: Smart-маркеры в верхних и нижних колонтитулах | Aspose.Cells for Node.js via Java
linktitle: Smart Markers в колонтитулах | Aspose.Cells for Node.js via Java
description: Размещайте заполнители Smart Marker в верхних и нижних колонтитулах страниц с помощью синтаксиса двойных угловых скобок и переключателя WorkbookDesigner.setEnableHeaderFooterMarkers, используя JSON-источники данных, и привязывайте изображения через data URI, в Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells for Node.js via Java, Smart-маркеры, верхние колонтитулы, нижние колонтитулы, маркеры верхних и нижних колонтитулов, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, строки JSON, привязка данных, изображение, data URI, JavaScript
type: docs
weight: 196
url: /ru/nodejs-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Верхние и нижние колонтитулы страниц обычно содержат метаданные отчёта, такие как заголовок отчёта, период отчётности, автор и отдел. Когда эта информация уже присутствует в источнике данных, используемом для заполнения рабочей книги, её ручное повторение создаёт избыточное дублирование.  
Классический синтаксис Smart Marker, `&=Source.Field`, обрабатывается в ячейках тела листа. Если разместить классический маркер в верхнем или нижнем колонтитуле через `PageSetup.setHeader` или `PageSetup.setFooter`, он останется буквальным текстом, поскольку строки колонтитулов не находятся в сетке ячеек листа, сканируемой `WorkbookDesigner.process()`.  
Начиная с **Aspose.Cells for Node.js via Java 26.11**, параметр `WorkbookDesigner.setEnableHeaderFooterMarkers`, который по умолчанию имеет значение `false`, заставляет `process()` разрешать заполнители, записанные как `<<Source.Field>>`, в строках разделов верхних и нижних колонтитулов. Вызовите `designer.setEnableHeaderFooterMarkers(true)` перед вызовом `process()`. Заполнители в колонтитулах используют тот же источник данных, что и маркеры в теле.  
Каждый верхний и нижний колонтитул содержит три адресуемых раздела:
- Раздел `0` — левый.
- Раздел `1` — центр.
- Раздел `2` — правый.  
Используйте `PageSetup.setHeader(int section, String value)` и `PageSetup.setFooter(int section, String value)` для записи этих разделов. После обработки примените `PageSetup.getHeader(int section)` и `PageSetup.getFooter(int section)` для получения готового текста.

{{% alert color="primary" %}}
Заполнитель вроде `<<Source.Field>>` вставляет значение поля как текст в строку раздела. Изображения привязываются с помощью суффикса `(picture)` и значения data-URI.  
{{% /alert %}}

## **Включение маркеров верхних/нижних колонтитулов с данными строк JSON**
Используйте следующую последовательность для разрешения заполнителей в верхних и нижних колонтитулах с данными строк JSON в **Aspose.Cells for Node.js via Java 26.11**:
1. Создайте объект `Workbook` и получите его первый `Worksheet` с помощью `workbook.getWorksheets().get(0)`.
2. Запишите заполнители `<<Source.Field>>` в нужные разделы верхних и нижних колонтитулов с помощью `PageSetup.setHeader` и `PageSetup.setFooter`.
3. Подготовьте данные строк в виде JSON-массива объектов-строк и выберите имя источника, совпадающее с префиксом, используемым в заполнителях. Например, источник с именем `node` поддерживает заполнители `<<node.Name>>`. Обычные JavaScript-объекты и массивы, передаваемые в `setDataSource`, на этой платформе не привязываются — поддерживается только JSON-форма.
4. Создайте `WorkbookDesigner` для рабочей книги.
5. Вызовите `designer.setEnableHeaderFooterMarkers(true)` перед обработкой.
6. Присоедините JSON с помощью `designer.setJsonDataSource("node", '[{"Name":"...","Author":"..."}]')`.
7. Вызовите `designer.process()`.
8. После обработки заполнители более не присутствуют в тексте верхних и нижних колонтитулов. Используйте `getHeader` и `getFooter` для получения готовых строк разделов.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource(
  "node",
  '[{"Name":"Q4 2026","Author":"Aspose.Cells"}]'
);
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
console.log("Footer: " + worksheet.getPageSetup().getFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx");
```

## **Использование JSON-источника данных**
Когда данные отчёта уже доступны в виде JSON, один вызов `setJsonDataSource` может снабдить всеми типами маркеров. Вызовите `WorkbookDesigner.setJsonDataSource(String name, String json)` для привязки источника.  
Аргумент `name` — это имя источника, используемое заполнителями. Например, имя `node` поддерживает заполнители `<<node.Company>>` и `<<node.Title>>`.  
Передайте данные строк напрямую в `setJsonDataSource`:
- Массив строк, например JSON-массив, содержащий один или несколько объектов-строк, поддерживается.
- Также может быть передан один объект-строка напрямую.
- Не оборачивайте строки в именованный верхнеуровневый ключ типа `{"rows":[...]}`. Такой оболочкой ожидаемая форма ввода для данного рабочего процесса не является.
Один JSON-источник может заполнять оба типа маркеров за один вызов `process()`. Он может разрешать классический маркер `&=` в ячейке тела листа и заполнители `<<>>` в верхних и нижних колонтитулах. По-прежнему необходимо вызвать `designer.setEnableHeaderFooterMarkers(true)`, чтобы заполнители в колонтитулах были разрешены.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
worksheet.getCells().get("A1").putValue("&=node.Company");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]');
designer.process();
console.log("Left: " + worksheet.getPageSetup().getHeader(0));
console.log("Right: " + worksheet.getPageSetup().getHeader(2));
console.log("Body: " + worksheet.getCells().get("A1").getStringValue());
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx");
```

## **Семантика переключателя и источника с несколькими строками**
`setEnableHeaderFooterMarkers` — по умолчанию `false`, и параметр управляет только заполнителями `<<Source.Field>>` в верхних и нижних колонтитулах. Когда переключатель выключен, `process()` по-прежнему разрешает классические маркеры `&=` в теле, но заполнитель `<<Source.Field>>` в колонтитуле остаётся буквальным текстом.  
Раздел верхнего или нижнего колонтитула представляет собой одну строку, а не повторяющуюся полосу. Если источник данных содержит несколько строк, первая строка поставляет значения для колонтитулов. После разрешения значения становятся обычным текстом колонтитулов. Они остаются в рабочей книге после вызова `save` и присутствуют при повторной загрузке сохранённой книги.  
В следующем примере создаются две рабочие книги на основе одного многострочного JSON-источника, чтобы сравнить поведение при отключённом и включённом режиме. `plainDesigner` оставляет заполнитель без изменений, тогда как `enabledDesigner` разрешает его, используя первую строку.

```javascript
const AsposeCells = require("aspose.cells");
const table = '[{"Name":"First Row"},{"Name":"Second Row"}]';
// Without the switch the placeholder stays literal text
const plainWorkbook = new AsposeCells.Workbook();
const plainSheet = plainWorkbook.getWorksheets().get(0);
plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const plainDesigner = new AsposeCells.WorkbookDesigner(plainWorkbook);
plainDesigner.setJsonDataSource("node", table);
plainDesigner.process();
// With the switch on, the FIRST row of a multi-row source wins
const enabledWorkbook = new AsposeCells.Workbook();
const enabledSheet = enabledWorkbook.getWorksheets().get(0);
enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const enabledDesigner = new AsposeCells.WorkbookDesigner(enabledWorkbook);
enabledDesigner.setEnableHeaderFooterMarkers(true);
enabledDesigner.setJsonDataSource("node", table);
enabledDesigner.process();
console.log("Without switch: " + plainSheet.getPageSetup().getHeader(1));
console.log("With switch: " + enabledSheet.getPageSetup().getHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
```

## **Привязка изображения к верхнему или нижнему колонтитулу**
Суффикс `(picture)` привязывает изображение к разделу верхнего или нижнего колонтитула. Запишите `<<node.logo(picture)>>` в месте, где должно появиться изображение, и передайте значение поля как data-URI — префикс `data:image/png;base64,`, за которым следует Base64-текст байтов изображения. Обычная строка Base64 без префикса `data:` не будет встроена как изображение.  
После `process()`:
1. Заполнитель заменяется на `&G`, стандартный код изображения в верхних и нижних колонтитулах. Поскольку маркер становится кодом внутри строки раздела, он может находиться в более длинном тексте, например `Logo: <<node.logo(picture)>>`.
2. Байты изображения встраиваются в книгу как медиа-часть, прикреплённая к слою рисунков верхних/нижних колонтитулов данного листа, поэтому изображение печатается вместе с колонтитулом.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
const table = [
    {
        logo: "data:image/png;base64," + fs.readFileSync("logo.png").toString("base64")
    }
];
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", JSON.stringify(table));
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
// This prints:
// Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx");
```

Напечатанный `&G` — это код изображения, который Excel интерпретирует при рендеринге колонтитула; байты `logo.png` теперь находятся внутри `HeaderFooterPicture.xlsx`, и изображение выводится вместо кода. Чтобы использовать Smart Markers в верхних и нижних колонтитулах, запишите заполнители `<<Source.Field>>` в левый, центральный и правый разделы с помощью `setHeader` и `setFooter`. Вызовите `designer.setEnableHeaderFooterMarkers(true)` перед `process()` и задайте значения через `designer.setJsonDataSource(name, json)`. Прочитайте готовые разделы с помощью `getHeader` и `getFooter`. Один и тот же источник данных может заполнять маркеры в теле и заполнители в колонтитулах за один проход обработки. Добавьте суффикс `(picture)` с значением data-URI, чтобы привязать изображение к разделу.

## Связанные статьи
- [Отображение массива в одной ячейке SmartMarker](/cells/ru/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="nodejs-java" >}}