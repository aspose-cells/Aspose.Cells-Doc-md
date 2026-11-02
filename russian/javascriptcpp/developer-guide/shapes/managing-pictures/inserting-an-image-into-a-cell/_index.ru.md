---
title: Вставка изображения в ячейку
linktitle: Вставка изображения в ячейку
description: Aspose.Cells for JavaScript via C++ — это библиотека для работы с файлами электронных таблиц. В этой статье объясняется, как точно вписать рисунок в одну ячейку, разместив плавающий рисунок поверх ячейки или встроив изображение непосредственно в ячейку.
keywords: Aspose.Cells, библиотека JavaScript via C++, электронная таблица, вставка изображения, встраивание изображения, рисунок в ячейке, вписывание изображения в ячейку, Pictures, EmbeddedImage
type: docs
weight: 80
url: /ru/javascript-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предлагает два различных способа связать изображение с одной ячейкой. Плавающий рисунок представляет собой фигуру на слое рисунков рабочего листа, визуально накладывающуюся на диапазон ячеек, а встроенное изображение хранится в самой ячейке и автоматически масштабируется в соответствии с областью отображения ячейки. Выберите подход, который лучше соответствует требованиям к макету.
{{% /alert %}}

## **Введение**
Точное вписывание рисунка в одну ячейку часто требуется при разработке электронных таблиц, используемых в качестве визуальных отчетов, каталогов продукции, справочников сотрудников, панелей мониторинга или списков запасов. Вместо растягивания изображения на несколько ячеек или его свободного размещения на рабочем листе может потребоваться аккуратное изображение, строго привязанное к ячейке и сохраняющее с ней выравнивание.
Aspose.Cells поддерживает этот сценарий двумя взаимодополняющими способами:
- **Подход 1 — разместить плавающий рисунок поверх ячейки.** Добавьте объект `Picture` на рабочий лист, задайте режим размещения с помощью `picture.setPlacement(PlacementType.MoveAndSize)` и настройте координаты привязки с помощью `picture.setUpperLeftRow()`, `picture.setUpperLeftColumn()`, `picture.setLowerRightRow()` и `picture.setLowerRightColumn()`, чтобы рисунок занимал ровно одну ячейку.
- **Подход 2 — встроить изображение непосредственно в ячейку.** Передайте ячейке `Buffer`, содержащий данные изображения, с помощью `cell.setEmbeddedImage(imageBuffer)`. Изображение автоматически масштабируется в соответствии с областью отображения ячейки и перемещается вместе с ней.
В остальной части статьи рассматриваются оба подхода, объясняются соответствующие API и показано, как использовать их в коде.

## **Подход 1: размещение рисунка поверх ячейки**
Плавающий рисунок представляет собой объект `Picture`, размещенный на слое рисунков рабочего листа. Хотя он не является частью какой-либо отдельной ячейки, он привязан к диапазону ячеек. Привязка рисунка к ячейкам, задаваемая его левым верхним и правым нижним углами, определяет визуальные границы рисунка на рабочем листе. По умолчанию только что добавленный рисунок занимает несколько ячеек.
Чтобы плавающий рисунок занимал **ровно одну ячейку**, необходимо:
1. Добавьте рисунок с помощью `worksheet.getPictures().add(row, column, imageBuffer)`, где `imageBuffer` — объект `Buffer`, содержащий данные изображения. Вызов привязывает новый рисунок к указанной ячейке.
2. Задайте четыре значения привязки так, чтобы ограничивающий прямоугольник рисунка совпадал с целевой ячейкой.
3. Вызовите `picture.setPlacement(PlacementType.MoveAndSize)`, чтобы рисунок перемещался и изменял размер вместе с соответствующей ячейкой при изменении пользователем ширины столбца или высоты строки.

### **Привязка рисунка к одной ячейке**
Для определения привязки рисунка используются четыре индекса, нумеруемых с нуля:
- `picture.getUpperLeftRow()` и `picture.setUpperLeftRow(value)` — индекс строки верхнего края рисунка.
- `picture.getUpperLeftColumn()` и `picture.setUpperLeftColumn(value)` — индекс столбца левого края рисунка.
- `picture.getLowerRightRow()` и `picture.setLowerRightRow(value)` — индекс строки нижнего края рисунка. Чтобы нижний край рисунка находился на нижней границе строки `r`, задайте для этого параметра значение `r + 1`.
- `picture.getLowerRightColumn()` и `picture.setLowerRightColumn(value)` — индекс столбца правого края рисунка. Чтобы правый край рисунка находился на правой границе столбца `c`, задайте для этого параметра значение `c + 1`.

{{% alert color="primary" %}}
Нумерация строк и столбцов в Aspose.Cells **начинается с нуля**. Для ячейки C6 индекс строки равен 5, а индекс столбца — 2. Ошибки «на единицу» при установке координат правой нижней границы привязки — наиболее частая причина появления рисунков, частично заходящих на соседнюю ячейку.
{{% /alert %}}

### **Управление поведением размещения**
`picture.getPlacement()` и `picture.setPlacement(value)` используют перечисление `PlacementType` для управления поведением рисунка, когда пользователь изменяет размер расположенной под ним строки или столбца. Для рисунка, занимающего одну ячейку, рекомендуется значение `PlacementType.MoveAndSize`: оно обеспечивает перемещение и изменение размера рисунка вместе с соответствующей ячейкой, сохраняя его точное вписывание.

### **Пошаговые инструкции**
1. Создайте новый объект `Workbook` (или откройте существующий).
2. Получите целевой объект `Worksheet` с помощью `workbook.getWorksheets().getAt(0)`.
3. Прочитайте файл изображения с диска в объект `Buffer`, например с помощью Node.js `fs.readFileSync`.
4. Вызовите `worksheet.getPictures().add(5, 2, imageBuffer)`, чтобы добавить рисунок, привязанный к ячейке C6. Метод возвращает индекс нового рисунка в коллекции `Pictures`; используйте его, чтобы получить соответствующий объект `Picture`.
5. Задайте четыре координаты привязки, чтобы рисунок занимал только ячейку C6: `picture.setUpperLeftRow(5)`, `picture.setUpperLeftColumn(2)`, `picture.setLowerRightRow(6)` и `picture.setLowerRightColumn(3)`.
6. Вызовите `picture.setPlacement(PlacementType.MoveAndSize)`, чтобы сохранить привязку рисунка к C6 при изменении размера столбца или строки.
7. При необходимости добавьте демонстрационный текст в соседние ячейки, чтобы показать, что рисунок размещен только в ячейке C6.
8. Сохраните рабочую книгу на диск в виде файла `.xlsx`.
Следующий код демонстрирует полную реализацию этого подхода.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,image/png" />
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
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];
            if (!file) {
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Please select a PNG image.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const imageData = new Uint8Array(await file.arrayBuffer());
            const picIndex = worksheet.pictures.add(5, 2, imageData);
            const picture = worksheet.pictures.get(picIndex);
            picture.upperLeftRow = 5;
            picture.upperLeftColumn = 2;
            picture.lowerRightRow = 6;
            picture.lowerRightColumn = 3;
            picture.placement = AsposeCells.Drawing.PlacementType.MoveAndSize;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Подход 2: встраивание изображения непосредственно в ячейку**
Aspose.Cells также предоставляет более простой механизм для изображений, связанных с ячейками: метод `cell.setEmbeddedImage(imageBuffer)`. Назначение данных изображения с помощью этого метода привязывает изображение к самой ячейке, как если бы оно было встроенным содержимым.

### **Как работают встроенные изображения**
- Изображение хранится как часть содержимого ячейки, а не как фигура на слое рисунков.
- Изображение автоматически масштабируется, чтобы поместиться в визуальных границах ячейки. Координаты привязки и параметры размещения не требуются.
- Ячейка по-прежнему является полноценной ячейкой с обычным адресом, на который могут ссылаться формулы; ее можно сортировать как часть строки и использовать в других операциях на уровне ячеек.
Таким образом, `cell.setEmbeddedImage(imageBuffer)` — наиболее лаконичный вариант, если требуется просто «изображение, которое находится внутри этой ячейки».

### **Пошаговые инструкции**
1. Создайте новый объект `Workbook` (или откройте существующий).
2. Получите целевой объект `Worksheet` с помощью `workbook.getWorksheets().getAt(0)`.
3. Прочитайте файл изображения с диска в объект `Buffer`, например с помощью Node.js `fs.readFileSync`.
4. Получите объект целевой ячейки — с помощью `worksheet.getCells().get("C6")` или `worksheet.getCells().get(5, 2)`.
5. Передайте `Buffer` ячейке с помощью `cell.setEmbeddedImage(imageBuffer)`.
6. При необходимости измените высоту целевой строки и ширину целевого столбца, чтобы увеличить область отображения встроенного изображения.
7. Сохраните рабочую книгу на диск в виде файла `.xlsx`.
Следующий код демонстрирует полную реализацию этого подхода.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,.jpg,.jpeg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const asposeReady = AsposeCells.onReady({
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
            if (!fileInput.files || fileInput.files.length === 0) {
                result.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Получить целевую ячейку C6
            const cell = worksheet.cells.get("C6");
            // Прочитать файл изображения в массив байтов
            const imageData = new Uint8Array(await fileInput.files[0].arrayBuffer());
            // Встроить изображение непосредственно в ячейку
            cell.embeddedImage = imageData;
            // При желании изменить высоту строки и ширину столбца, чтобы встроенное изображение было лучше видно
            worksheet.cells.setColumnWidth(2, 30); // Столбец C (индекс 2)
            worksheet.cells.setRowHeight(5, 100); // Строка 6 (индекс 5)
            // Сохранить полученную книгу в виде файла .xlsx
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Выбор подходящего подхода**
Оба подхода позволяют получить рисунок, помещающийся в пределах одной ячейки, но различаются способом хранения и поведением:
- **Используйте плавающий рисунок (подход 1), если:**
  - Требуется более тонкая настройка размещения, порядка наложения или выравнивания относительно других объектов слоя рисунков.
  - Рисунок должен вести себя как фигура, которую можно выделить, изменить порядок следования или сгруппировать с другими фигурами.
  - Требуется совместимость с устаревшим кодом, в котором уже используется коллекция `Pictures`, доступная через `worksheet.getPictures()`.
  - Координаты привязки необходимо рассчитывать динамически с учетом макета рабочего листа.
- **Используйте встроенное изображение (подход 2), если:**
  - Нужна максимально простая вставка изображения в ячейку.
  - Изображение должно перемещаться вместе с ячейкой, как любое другое содержимое ячейки.

## Связанные статьи
- [Камера Excel в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/excel-camera/)
- [Добавление полей фильтра в сводную таблицу в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/add-page-field-in-pivot-table/)
- [Применение стилей к сводным таблицам в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/apply-style-to-pivot-table/)
- [Преобразование спарклайна в изображение и HTML в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript-cpp" >}}