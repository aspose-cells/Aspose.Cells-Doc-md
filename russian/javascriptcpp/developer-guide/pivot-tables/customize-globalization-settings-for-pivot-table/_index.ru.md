---
title: Настройка параметров глобализации для сводной таблицы с помощью JavaScript через C++
linktitle: Настройка глобализации для сводной таблицы
type: docs
weight: 50
url: /ru/javascript-cpp/customize-globalization-settings-for-pivot-table/
---

## **Возможные сценарии использования**

Иногда вы хотите настроить текст *Общая сумма, Подитог, Общий итог, Все элементы, Множество элементов, Метки столбцов, Метки строк, Пустые значения* в соответствии с вашими требованиями. Скрипт Aspose.Cells for Java через C++ позволяет настроить параметры глобализации сводной таблицы для таких сценариев. Также вы можете использовать эту функцию для изменения ярлыков на другие языки, такие как арабский, хинди, польский и др.

## **Настройка глобализации для сводной таблицы**

Следующий пример кода показывает, как настроить параметры глобализации для сводной таблицы. Он создает класс *CustomPivotTableGlobalizationSettings*, унаследованный от базового класса [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/pivotglobalizationsettings/) и переопределяет все необходимые методы. Эти методы возвращают настроенный текст для *Итог свода, Итог подытога, Общий итог, Все элементы, Несколько элементов, Заголовки столбцов, Заголовки строк, Пустые значения*. Затем объект этого класса присваивается свойству [**WorkbookSettings.pivotSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#pivotSettings--). Код загружает [исходный файл Excel](40468488.xlsx), обновляет и вычисляет его данные и сохраняет результат в виде файла [PDF](40468487.pdf). Ниже приведен скриншот, показывающий эффект работы этого кода на итоговом PDF. Как видно на скриншоте, разные части сводной таблицы теперь содержат настроенный текст, возвращаемый переопределенными методами класса [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/pivotglobalizationsettings/).

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Globalization Settings Example</title>
    </head>
    <body>
        <h1>Pivot Table Globalization Settings Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

        class CustomPivotTableGlobalizationSettings extends AsposeCells.PivotGlobalizationSettings {
            // Gets the name of "Total" label in the PivotTable.
            getTextOfTotal() {
                console.log("---------GetPivotTotalName-------------");
                return "AsposeGetPivotTotalName";
            }

            // Gets the name of "Grand Total" label in the PivotTable.
            getTextOfGrandTotal() {
                console.log("---------GetPivotGrandTotalName-------------");
                return "AsposeGetPivotGrandTotalName";
            }

            // Gets the name of "(Multiple Items)" label in the PivotTable.
            getTextOfMultipleItems() {
                console.log("---------GetMultipleItemsName-------------");
                return "AsposeGetMultipleItemsName";
            }

            // Gets the name of "(All)" label in the PivotTable.
            getTextOfAll() {
                console.log("---------GetAllName-------------");
                return "AsposeGetAllName";
            }

            // Gets the name of "Column Labels" label in the PivotTable.
            getTextOfColumnLabels() {
                console.log("---------GetColumnLabelsOfPivotTable-------------");
                return "AsposeGetColumnLabelsOfPivotTable";
            }

            // Gets the name of "Row Labels" label in the PivotTable.
            getTextOfRowLabels() {
                console.log("---------GetRowLabelsNameOfPivotTable-------------");
                return "AsposeGetRowLabelsNameOfPivotTable";
            }

            // Gets the name of "(blank)" label in the PivotTable.
            getTextOfEmptyData() {
                console.log("---------GetEmptyDataName-------------");
                return "(blank)AsposeGetEmptyDataName";
            }

            // Gets the name of PivotFieldSubtotalType type in the PivotTable.
            getTextOfSubTotal(subTotalType) {
                console.log("---------GetSubTotalName-------------");

                switch (subTotalType) {
                    case AsposeCells.PivotFieldSubtotalType.Sum:
                        return "AsposeSum";

                    case AsposeCells.PivotFieldSubtotalType.Count:
                        return "AsposeCount";

                    case AsposeCells.PivotFieldSubtotalType.Average:
                        return "AsposeAverage";

                    case AsposeCells.PivotFieldSubtotalType.Max:
                        return "AsposeMax";

                    case AsposeCells.PivotFieldSubtotalType.Min:
                        return "AsposeMin";

                    case AsposeCells.PivotFieldSubtotalType.Product:
                        return "AsposeProduct";

                    case AsposeCells.PivotFieldSubtotalType.CountNums:
                        return "AsposeCount";

                    case AsposeCells.PivotFieldSubtotalType.Stdev:
                        return "AsposeStdDev";

                    case AsposeCells.PivotFieldSubtotalType.Stdevp:
                        return "AsposeStdDevp";

                    case AsposeCells.PivotFieldSubtotalType.Var:
                        return "AsposeVar";

                    case AsposeCells.PivotFieldSubtotalType.Varp:
                        return "AsposeVarp";
                }

                return "AsposeSubTotalName";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Apply globalization settings and custom pivot table globalization settings
            workbook.settings.globalizationSettings = new AsposeCells.GlobalizationSettings();
            workbook.settings.globalizationSettings.pivotSettings = new CustomPivotTableGlobalizationSettings();

            // Hide first worksheet that contains the data of the pivot table
            workbook.worksheets.get(0).isVisible = false;

            // Access second worksheet
            const ws = workbook.worksheets.get(1);

            // Access the pivot table, refresh and calculate its data
            const pt = ws.pivotTables.get(0);
            pt.refreshDataFlag = true;
            pt.refreshData();
            pt.calculateData();
            pt.refreshDataFlag = false;

            // Pdf save options - save entire worksheet on a single pdf page
            const options = new AsposeCells.PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the output pdf 
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputPivotTableGlobalizationSettings.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
