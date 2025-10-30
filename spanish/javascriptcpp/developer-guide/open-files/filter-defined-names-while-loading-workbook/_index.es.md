---
title: Filtrar nombres definidos al cargar libro de trabajo con JavaScript a través de C++
linktitle: Filtrar nombres definidos al cargar el libro de trabajo
type: docs
weight: 50
url: /es/javascript-cpp/filter-defined-names-while-loading-workbook/
---

## **Escenarios de uso posibles**

Aspose.Cells le permite filtrar o eliminar nombres definidos presentes en el libro de trabajo. Por favor, utilice [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) para cargar nombres definidos y [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) para eliminarlos al cargar el libro. Tenga en cuenta que, si elimina los nombres definidos, las fórmulas dentro del libro pueden dejar de funcionar.

## **Filtrar nombres definidos al cargar el libro de trabajo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767860.xlsx) que tiene una fórmula en la celda **C1** que contiene los nombres definidos, es decir, *=SUM(MyName1, MyName2)*. Como estamos usando [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) para eliminar los nombres definidos al cargar el libro, la fórmula en la celda C1 en el [archivo de Excel de salida](61767861.xlsx) se rompe y muestra *#NAME?* en su lugar. Por favor, vea la siguiente captura de pantalla que muestra el efecto del código en el archivo de Excel de muestra.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Defined Names While Loading Workbook</title>
    </head>
    <body>
        <h1>Filter Defined Names While Loading Workbook</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify the load options
            let opts = new LoadOptions();
            // We do not want to load defined names
            opts.loadFilter = new LoadFilter(~LoadDataFilterOptions.DefinedNames);

            // Load the workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the output Excel file, it will break the formula in C1 if defined names were removed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFilterDefinedNamesWhileLoadingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">FilterDefinedNamesWhileLoadingWorkbook executed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
