---
title: Как создавать динамический график с выпадающим списком с помощью JavaScript через C++
linktitle: Как создать динамическую диаграмму с выпадающим списком
description: Узнайте, как создать динамический график, который обновляется на основе выбора в выпадающем списке с помощью Aspose.Cells for JavaScript через C++. Наш пошаговый гид покажет, как интегрировать выпадающий список в ваш график для гибкой визуализации данных.
keywords: Aspose.Cells for JavaScript с помощью C++, динамический график, выпадающий список, визуализация данных, интеграция, гибкая визуализация.
type: docs
weight: 76
url: /ru/javascript-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Возможные сценарии использования**
Динамическая диаграмма с выпадающим списком в Excel - мощный инструмент, позволяющий пользователям создавать интерактивные диаграммы, которые могут динамически обновляться на основе выбранных данных. Эта функция особенно полезна в ситуациях, где необходимо проанализировать несколько наборов данных или сравнить различные сценарии.

Одно из распространенных применений динамической диаграммы с выпадающим списком - в финансовом анализе. Например, компания может иметь несколько наборов финансовых данных для разных лет или отделов. Используя выпадающий список, пользователи могут выбрать конкретный набор данных, который они хотят проанализировать, и диаграмма автоматически обновится, чтобы отобразить соответствующую информацию. Это позволяет легко сравнивать и идентифицировать тенденции или закономерности.

Еще одно применение - в продажах и маркетинге. У компании может быть данные о продажах различных товаров или регионов. С помощью динамической диаграммы с выпадающим списком пользователи могут выбрать конкретный товар или регион из выпадающего списка, и диаграмма будет динамически обновляться, чтобы показать результаты продаж для выбранной опции. Это помогает определить лучшие области или продукты и принимать решения на основе данных.

В заключение, динамическая диаграмма с выпадающим списком в Excel обеспечивает гибкий и интерактивный способ визуализации и анализа данных. Он ценен в ситуациях, где необходимо сравнивать несколько наборов данных или изучать различные сценарии, что делает его универсальным инструментом для финансового анализа, продаж и маркетинга, а также многих других приложений.

## **Используйте Aspose Cells для создания динамической диаграммы с выпадающим списком**
В следующих параграфах мы покажем, как создавать динамический график с выпадающим списком с помощью Aspose.Cells for JavaScript через C++. Мы покажем код для примера, а также созданный с этим кодом файл Excel.

## **Образец кода**
Следующий образец кода сгенерирует файл [Динамическая диаграмма с выпадающим списком](DynamicChartWithDropdownlist.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Chart with Dropdown List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, BackgroundType, Color, ChartType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A3").putValue("Tea");
            sheet.cells.get("A4").putValue("Coffee");
            sheet.cells.get("A5").putValue("Sugar");

            // In this example, we will add 12 months of data
            sheet.cells.get("B2").putValue("Jan");
            sheet.cells.get("C2").putValue("Feb");
            sheet.cells.get("D2").putValue("Mar");
            sheet.cells.get("E2").putValue("Apr");
            sheet.cells.get("F2").putValue("May");
            sheet.cells.get("G2").putValue("Jun");
            sheet.cells.get("H2").putValue("Jul");
            sheet.cells.get("I2").putValue("Aug");
            sheet.cells.get("J2").putValue("Sep");
            sheet.cells.get("K2").putValue("Oct");
            sheet.cells.get("L2").putValue("Nov");
            sheet.cells.get("M2").putValue("Dec");
            const allMonths = 12;
            const iCount = 3;
            for (let i = 0; i < iCount; i++) {
                for (let j = 0; j < allMonths; j++) {
                    const _row = i + 2;
                    const _column = j + 1; 
                    sheet.cells.get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
                }
            }

            // This is the Dropdownlist for Dynamic Data
            const ca = CellArea.createCellArea(9, 0, 9, 0);
            const _index = sheet.validations.add(ca);
            const _va = sheet.validations.get(_index);
            _va.type = ValidationType.List;
            _va.inCellDropDown = true;
            _va.formula1 = "=$B$2:$M$2";
            sheet.cells.get("A9").putValue("Current Month");
            sheet.cells.get("A10").putValue("Jan");
            const _style = sheet.cells.get("A10").style;
            _style.font.isBold = true;
            _style.pattern = BackgroundType.Solid;
            _style.foregroundColor = Color.Yellow;
            sheet.cells.get("A10").style = _style;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtMonthData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtXLabels");
            sheets.names.get(index).refersTo = "=Sheet1!$A$3:$A$5";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Column, 8, 2, 20, 8);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("month", true);
            chart.nSeries.get(0).name = "=Sheet1!$A$10";
            chart.nSeries.get(0).values = "Sheet1!ChtMonthData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtXLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicChartWithDropdownlist.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

## **Примечания**
В сгенерированном файле диаграмма динамически будет подсчитывать данные для выбранного месяца. Это делается с помощью формулы "OFFSET" в образцовом коде:
