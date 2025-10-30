---
title: Cómo establecer la propiedad AutoRecover del Libro de Trabajo con JavaScript mediante C++
linktitle: Cómo establecer la propiedad AutoRecover del Libro de trabajo
type: docs
weight: 220
url: /es/javascript-cpp/how-to-set-autorecover-property-of-workbook/
description: Aprende cómo establecer la propiedad AutoRecover de un libro de trabajo usando el Script Aspose.Cells for JavaScript mediante C++.
---

{{% alert color="primary" %}}  
Puedes usar Aspose.Cells para establecer la propiedad AutoRecover del libro de trabajo. El valor predeterminado de esta propiedad es **true**. Cuando lo estableces en **falso** en un libro de trabajo, Microsoft Excel desactiva AutoRecover (Autosave) en ese archivo de Excel.  

Aspose.Cells proporciona la propiedad [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) para activar o desactivar esta opción.  
{{% /alert %}}  

El siguiente código explica cómo usar la propiedad [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) del libro de trabajo. El código primero lee el valor predeterminado de esta propiedad, que es **true**, luego lo establece como **falso** y guarda el libro de trabajo. Luego lee el libro de trabajo nuevamente y obtiene el valor de esta propiedad, que en ese momento es **falso**.  

## Código JavaScript para establecer la propiedad AutoRecover del Libro de Trabajo  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoRecover</title>
    </head>
    <body>
        <h1>AutoRecover Property Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            // Create workbook object
            const workbook = new Workbook();

            // Read AutoRecover property
            const autoRecoverBefore = workbook.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover before: ${autoRecoverBefore}</p>`;

            // Set AutoRecover property to false
            workbook.settings.autoRecover = false;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download output_out.xlsx';

            // Read the saved workbook again from the saved data
            const workbook2 = new Workbook(new Uint8Array(outputData));

            // Read AutoRecover property
            const autoRecoverAfter = workbook2.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover after reload: ${autoRecoverAfter}</p>`;
        });
    </script>
</html>
```  

## **Salida**  



{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}
