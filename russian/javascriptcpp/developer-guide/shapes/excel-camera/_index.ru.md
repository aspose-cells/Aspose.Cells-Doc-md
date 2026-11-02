---
title: Камера Excel в Aspose.Cells for JavaScript via C++
linktitle: Камера Excel в Aspose.Cells for JavaScript via C++
description: Узнайте, как использовать камеру Excel в Aspose.Cells for JavaScript via C++, чтобы создать динамическое изображение, связанное с диапазоном ячеек, которое обновляется вместе с исходными данными и сохраняет все форматирование исходного диапазона.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, камера Excel, динамическое изображение, связанное изображение, picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /ru/javascript-cpp/excel-camera/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Камера Excel — это объект рабочего листа, который отображает текущее состояние диапазона ячеек в виде изображения и располагается на слое рисования как обычное изображение. Aspose.Cells поддерживает два режима создания: динамическое изображение, которое автоматически обновляется при изменении исходных данных, и статическое изображение, которое фиксирует однократный снимок диапазона. В этой статье рассматриваются оба подхода, чтобы вы могли выбрать подходящий для вашей компоновки.

## Что такое камера Excel?
Камера Excel, по сути, представляет собой объект изображения, привязанный к определенной строке и столбцу на слое рисования рабочего листа. В отличие от обычного вставленного изображения, камера связана с исходным диапазоном с помощью формулы в стиле A1, например `"A1:F10"`. При изменении любой ячейки в этом диапазоне изображение камеры автоматически обновляется, отражая новое содержимое. Камера сохраняет все форматирование исходной области — границы, цвета фона, шрифты и числовые форматы, — поэтому все, что видно в ячейках, отображается и на изображении камеры. Это делает камеру особенно полезной для информационных панелей, сводок, боковых панелей и макетов отчетов, где требуется видимый предварительный просмотр отдельной области без прокрутки или повторения данных. Следует учитывать два важных момента: перед сохранением рабочей книги необходимо вызвать `updateSelectedValue()`, а файл необходимо экспортировать в HTML или PDF, поскольку эти форматы полагаются на внедренные данные изображения, а не на пересчет формул в реальном времени.

## Метод 1 — добавление динамической камеры
Динамическая камера — наиболее распространенный подход и наиболее близкий аналог встроенного в Excel инструмента «Камера». Он работает путем добавления изображения без начального содержимого, после чего ему назначается свойство `formula`, ссылающееся на исходный диапазон. После назначения формулы вызов `updateSelectedValue()` обновляет внедренные данные изображения, обеспечивая их синхронизацию с ячейками, которые отражает камера. Камера не реализована с помощью отдельного класса — она полностью построена на стандартном типе `Picture`.
Основные API:
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, null)` — добавляет изображение, привязанное к указанной строке и столбцу. Передача `null` в качестве параметра изображения создает пустое изображение, служащее заполнителем для динамической камеры. Метод возвращает индекс нового изображения.
- `worksheet.getPictures().get(index)` — возвращает указанный объект `Picture` из коллекции.
- `picture.formula` — строковое свойство, содержащее ссылку в стиле A1 на исходный диапазон, который отражает камера, например `"A1:F10"`.
- `picture.updateSelectedValue()` — метод без возвращаемого значения, который обновляет внедренные данные изображения на основе ячеек, на которые ссылается `formula`.

{{% alert color="primary" %}}
При экспорте в HTML или PDF необходимо вызвать `updateSelectedValue()` перед сохранением рабочей книги; иначе экспортированный файл не будет содержать данные изображения, и камера будет отображаться пустой при визуализации результата.
Следующий код создает рабочую книгу, добавляет пустое изображение, привязанное к строке 10 и столбцу 6, связывает его с исходным диапазоном `A1:F10` через свойство `formula`, обновляет внедренные данные изображения и сохраняет рабочую книгу.
{{% /alert %}}

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Динамическая камера: добавить пустое изображение, связать его с A1:F10 через Formula, затем обновить
            const pictures = worksheet.pictures;
            const index = pictures.add(10, 6, null);
            const picture = pictures.get(0);
            picture.formula = "A1:F10";
            picture.updateSelectedValue();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_dynamic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Метод 2 — добавление статической камеры
Статическая камера — по сути, предварительный просмотр диапазона ячеек, полученный в результате однократной визуализации. Вместо поддержки динамической связи диапазон однократно преобразуется в байты изображения, эти байты оборачиваются в `Buffer`, а затем добавляются как обычное изображение. После этого содержимое изображения фиксируется в момент создания и не обновляется автоматически при изменении исходных ячеек.
Основные API:
- `cells.createRange(address)` — создает объект `Range` по адресу в стиле A1, например `"A1:F10"`.
- `range.toImage(options)` — формирует байты изображения для диапазона. При передаче `null` используются параметры визуализации по умолчанию; существуют перегруженные версии для более точного управления выводом.
- `Buffer.from(imageBytes)` — оборачивает визуализированные байты изображения в `Buffer`, который можно передать в `worksheet.getPictures().add`.
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, imageBuffer)` — добавляет изображение, привязанное к указанной строке и столбцу, при этом передается `Buffer`, полученный в результате визуализации.
Следующий код создает рабочую книгу, формирует объект `Range` для `A1:F10`, создает для него байты изображения с помощью `range.toImage(null)`, оборачивает байты в `Buffer`, добавляет изображение, привязанное к строке 10 и столбцу 6, и сохраняет рабочую книгу.

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Статическая камера: создать диапазон, отрисовать в байты, обернуть в MemoryStream, добавить как изображение
            const range = worksheet.cells.createRange("A1:F10");
            const imageData = range.toImage();
            const pictures = worksheet.pictures;
            pictures.add(10, 6, imageData);
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_static.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Выбор между динамической и статической камерами
- **Динамическая камера:** обновляется при каждом пересчете, поддерживает экспорт в HTML и PDF после вызова `updateSelectedValue()` и сохраняет динамическую связь с исходными данными на протяжении всего срока существования файла.
- **Статическая камера:** одноразовая визуализация, которая никогда не обновляется; она полезна, когда на этапе сборки необходимо встроить фиксированный визуальный снимок вместо динамического отражения данных.
Aspose.Cells поддерживает динамическую камеру с автоматическим обновлением, реализованную с использованием `picture.formula` и `updateSelectedValue()`, а также статическую одноразовую камеру на основе `range.toImage` и `Buffer`. Выберите динамический подход, если результат должен постоянно соответствовать исходным ячейкам, и статический подход, если на этапе сборки нужен только фиксированный визуальный снимок.

## Связанные статьи
- [Преобразование Sparkline в изображение и HTML в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Добавление полей фильтра в сводную таблицу в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/add-page-field-in-pivot-table/)
- [Применение стилей к сводным таблицам в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}