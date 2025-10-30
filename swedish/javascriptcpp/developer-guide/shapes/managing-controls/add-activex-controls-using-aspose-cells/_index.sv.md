---
title: Lägg till ActiveX kontroller med Aspose.Cells for JavaScript via C++
linktitle: Lägg till ActiveX kontroller med hjälp av Aspose.Cells
type: docs
weight: 260
url: /sv/javascript-cpp/add-activex-controls-using-aspose-cells/
description: Lära dig hur man lägger till ActiveX kontroller i ett kalkylblad med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Du kan lägga till ActiveX-kontroller med Aspose.Cells med metoden [**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-). Denna metod tar en parameter [**ControlType**](https://reference.aspose.com/cells/javascript-cpp/controltype/) som berättar vilken typ av ActiveX-kontroll som ska läggas till i ett kalkylblad. Den har följande värden.

- ControlType.CheckBox
- ControlType.ComboBox
- ControlType.CommandButton
- ControlType.Image
- ControlType.Label
- ControlType.ListBox
- ControlType.RadioButton
- ControlType.ScrollBar
- ControlType.SpinButton
- ControlType.TextBox
- ControlType.ToggleButton
- ControlType.Unknown

När du har lagt till ActiveX-kontrollen i formgruppen kan du sedan komma åt ActiveX-kontrollobjektet via [**Shape.activeXControl**](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) egenskapen och sedan ställa in dess olika egenskaper.

{{% /alert %}}

Följande exempelkod lägger till Toggle-knappen ActiveX-kontroll med hjälp av Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add ActiveX Control</title>
    </head>
    <body>
        <h1>Add ActiveX Control Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ControlType, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                // Create workbook object (empty workbook)
                const wb = new Workbook();

                // Access first worksheet
                const sheet = wb.worksheets.get(0);

                // Add Toggle Button ActiveX Control inside the Shape Collection
                const s = sheet.shapes.addActiveXControl(ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

                // Access the ActiveX control object and set its linked cell property
                const c = s.activeXControl;
                c.linkedCell = "A1";

                // Save the workbook in xlsx format and provide download link
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'AddActiveXControls_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">ActiveX control added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```
