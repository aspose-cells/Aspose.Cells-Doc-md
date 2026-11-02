---
title: Преобразование спарклайна в изображение и HTML с помощью Aspose.Cells for JavaScript via C++
linktitle: Преобразование спарклайна в изображение и HTML с помощью Aspose.Cells for JavaScript via C++
description: Узнайте, как отрисовывать спарклайны Aspose.Cells в отдельные изображения для встраивания в ячейки и экспортировать рабочие листы со спарклайнами в HTML с помощью HtmlSaveOptions.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, спарклайн, sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, отрисовка спарклайна, преобразование спарклайна в изображение, экспорт спарклайна в HTML
type: docs
weight: 120
url: /ru/javascript-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Спарклайны — это миниатюрные диаграммы, размещаемые в ячейках рабочего листа. Aspose.Cells позволяет извлекать каждый спарклайн в виде отдельного изображения для встраивания в другую ячейку или внешний отчет, а также экспортировать весь рабочий лист со спарклайнами в HTML для распространения и просмотра в браузере. Свойство `cell.embeddedImage`, используемое в этой статье, доступно в **Aspose.Cells 26.5 и более поздних версиях**.
{{% /alert %}}

## **Введение**
Спарклайны — компактный способ визуализировать тенденции непосредственно на рабочем листе. Несмотря на то что пользователи Excel видят спарклайны непосредственно в ячейках, во многих реальных сценариях требуется вынести их за пределы ячейки, например, чтобы встроить в другую ячейку в виде статического изображения, добавить в автоматизированное электронное письмо или отрисовать в составе HTML-отчета, опубликованного в Интернете.
Aspose.Cells поддерживает обе операции. Метод `sparkline.toImage` отрисовывает отдельный спарклайн и возвращает его в виде `Buffer`, а полученные байты можно присвоить `cell.embeddedImage`, чтобы сохранить изображение в одной ячейке рабочей книги. Кроме того, `HtmlSaveOptions` позволяет преобразовать всю рабочую книгу со спарклайнами в один автономный HTML-файл. В этой статье пошагово рассматриваются оба сценария.

## **Сценарий 1 — Отрисовка спарклайнов в изображения и их встраивание в ячейки**
В рамках этого сценария создайте рабочий лист с небольшим диапазоном исходных значений, привяжите к нему три различные группы спарклайнов (`Line`, `Column` и `Stacked`/`Win-Loss`), оттрисуйте каждую группу в формате PNG и сохраните полученные байты PNG в соседних ячейках в качестве встроенных изображений. Итоговый результат — один файл `.xlsx`, содержащий как нативные спарклайны, так и соответствующие им статичные изображения.

### **Пошаговые инструкции**
1. Создайте новый `Workbook` и получите ссылку на первый `Worksheet`.
2. Заполните ячейки `A1`–`E1` пятью тестовыми числовыми значениями, например ежедневными объемами продаж или показателями температуры.
3. Добавьте три объекта `SparklineGroup` в рабочий лист, вызвав `worksheet.getSparklineGroups().add(...)`:
   - Группу `SparklineType.Line` с ячейкой привязки `F1` и диапазоном данных `A1:E1`.
   - Группу `SparklineType.Column` с ячейкой привязки `G1` и диапазоном данных `A1:E1`.
   - Группу `SparklineType.Stacked` (выигрыш/проигрыш) с ячейкой привязки `H1` и диапазоном данных `A1:E1`.
4. Создайте экземпляр `ImageOrPrintOptions` и установите его свойство `imageType` в `ImageType.Png`, чтобы каждый спарклайн можно было отрисовать в формате PNG.
5. Сохраните книгу как `output_with_sparklines.xlsx`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, CellArea, ImageOrPrintOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Создать новую книгу и получить доступ к первому листу
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Заполнить ячейки A1:E1 образцами данных
            cells.get("A1").value = 5;
            cells.get("B1").value = -3;
            cells.get("C1").value = 8;
            cells.get("D1").value = -2;
            cells.get("E1").value = 6;
            // Добавить группу линейных спарклайнов, привязанную к F1 (столбец 5, строка 0)
            const lineArea = new CellArea();
            lineArea.startColumn = 5;
            lineArea.endColumn = 5;
            lineArea.startRow = 0;
            lineArea.endRow = 0;
            const lineIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Line,
                "A1:E1",
                false,
                lineArea
            );
            // Добавить группу столбчатых спарклайнов, привязанную к G1 (столбец 6, строка 0)
            const columnArea = new CellArea();
            columnArea.startColumn = 6;
            columnArea.endColumn = 6;
            columnArea.startRow = 0;
            columnArea.endRow = 0;
            const columnIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Column,
                "A1:E1",
                false,
                columnArea
            );
            // Добавить группу спарклайнов Win/Loss (Stacked), привязанную к H1 (столбец 7, строка 0)
            const stackedArea = new CellArea();
            stackedArea.startColumn = 7;
            stackedArea.endColumn = 7;
            stackedArea.startRow = 0;
            stackedArea.endRow = 0;
            const stackedIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Stacked,
                "A1:E1",
                false,
                stackedArea
            );
            // Настроить параметры изображения для вывода в формате PNG
            const imageOptions = new ImageOrPrintOptions();
            imageOptions.imageType = AsposeCells.ImageType.Png;
            // Преобразовать линейный спарклайн в изображение и встроить его в ячейку F2
            const lineSp = worksheet.sparklineGroups.get(lineIdx).sparklines.get(0);
            cells.get("F2").embeddedImage = lineSp.toImage(imageOptions);
            // Преобразовать столбчатый спарклайн в изображение и встроить его в ячейку G2
            const columnSp = worksheet.sparklineGroups.get(columnIdx).sparklines.get(0);
            cells.get("G2").embeddedImage = columnSp.toImage(imageOptions);
            // Преобразовать спарклайн Win/Loss в изображение и встроить его в ячейку H2
            const stackedSp = worksheet.sparklineGroups.get(stackedIdx).sparklines.get(0);
            cells.get("H2").embeddedImage = stackedSp.toImage(imageOptions);
            // Сохранить книгу на диск
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_with_sparklines.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

Приведенный выше код создает рабочую книгу, в которой каждое визуальное представление спарклайна представлено в двух формах: нативным спарклайном, привязанным к строке 1, и статичным рисунком PNG, встроенным непосредственно в соседнюю ячейку строки 2. Поскольку рисунки хранятся внутри самого файла, рабочая книга остается единым автономным файлом, который можно отправить по электронной почте или поместить в архив без нарушения ссылок на встроенные изображения.

{{% alert color="primary" %}}
Поскольку каждая группа спарклайнов привязана к одной ячейке, к ней можно обращаться через индексатор `group.getSparklines()[0]`, не перебирая коллекцию. Это позволяет сократить код отрисовки и соответствует типичной схеме «один спарклайн на одну ячейку привязки». Для хранения байтов изображения через `cell.embeddedImage` требуется Aspose.Cells 26.5 или более поздняя версия.
{{% /alert %}}

## **Сценарий 2 — Экспорт рабочего листа со спарклайнами в HTML**
После того как рабочая книга содержит нативные спарклайны и, при необходимости, соответствующие им встроенные изображения, весь рабочий лист можно опубликовать в Интернете, сохранив его в формате HTML. Класс `HtmlSaveOptions` предоставляет необходимые параметры управления экспортом. В этом сценарии будет повторно использован файл `output_with_sparklines.xlsx`, созданный в сценарии 1, и преобразован в аккуратно оформленный одностраничный HTML-документ.

### **Пошаговые инструкции**
1. Убедитесь, что файл `output_with_sparklines.xlsx`, созданный в сценарии 1, доступен на диске в рабочем каталоге.
2. Загрузите этот файл в новый экземпляр `Workbook`.
3. Создайте экземпляр `HtmlSaveOptions` и установите для него свойство `exportActiveWorksheetOnly` равным `true`, чтобы итоговый HTML-файл содержал только активный рабочий лист, а не всю рабочую книгу.
4. Вызовите `workbook.save("sparklines.html", htmlOptions)`, чтобы сохранить HTML-файл на диске.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const htmlOptions = new HtmlSaveOptions();
                htmlOptions.exportActiveWorksheetOnly = true;
                const outputData = workbook.save(AsposeCells.SaveFormat.Html, htmlOptions);
                const blob = new Blob([outputData], { type: "text/html" });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "sparklines.html";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

Приведенный выше код преобразует рабочую книгу со спарклайнами из сценария 1 в переносимый HTML-файл. Группы спарклайнов отрисовываются как встроенные изображения внутри сгенерированной HTML-таблицы, поэтому конечные пользователи могут просматривать тенденции в любом современном браузере без необходимости устанавливать Excel. Устанавливая `exportActiveWorksheetOnly` в `true`, вы предотвращаете случайную публикацию скрытых листов или вспомогательных данных: экспортируется только рабочий лист, который в данный момент виден пользователю.

{{% alert color="primary" %}}
Класс `HtmlSaveOptions` предоставляет дополнительные свойства для детальной настройки вывода, например `exportHiddenWorksheet`, `exportImagesAsBase64` и `encoding`. При необходимости настройте их с учетом требований целевой среды развертывания.
{{% /alert %}}

## **Сводка API**
В описанных выше сценариях используется небольшой набор API Aspose.Cells.
- `SparklineGroup` и метод доступа к коллекции `worksheet.getSparklineGroups()` используются для задания типа (`Line`, `Column`, `Stacked`), диапазона данных и ячейки привязки каждой группы спарклайнов. В этой статье каждая группа привязана к одной ячейке, поэтому доступ к ней осуществляется через `worksheet.getSparklineGroups()[i]`.
- `Sparkline` и индексатор `group.getSparklines()[0]` позволяют получить отдельный спарклайн внутри группы. Поскольку в примере каждая группа содержит ровно один спарклайн, цикл обхода не требуется.
- `sparkline.toImage(imageOrPrintOptions)` — метод отрисовки, возвращающий изображение спарклайна в виде `Buffer`. Возвращенные байты можно напрямую присвоить `cell.embeddedImage`.
- `HtmlSaveOptions.exportActiveWorksheetOnly` (логическое значение) ограничивает экспорт в HTML только активным рабочим листом. Это одно из наиболее часто используемых свойств `HtmlSaveOptions` при создании одностраничных отчетов.
- `ImageOrPrintOptions.imageType` задает формат изображения, например `ImageType.Png`, используемый при отрисовке с помощью `toImage` и при печати рабочих листов в изображения.

{{< app/cells/assistant language="javascript-cpp" >}}