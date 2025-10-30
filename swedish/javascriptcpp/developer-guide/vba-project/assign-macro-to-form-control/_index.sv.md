---
title: Tilldela makro till formulärkontroll med JavaScript via C++
linktitle: Tilldela Makro till Formulärkontroll
type: docs
weight: 60
url: /sv/javascript-cpp/assign-macro-to-form-control/
description: Lär dig hur du tilldelar en makkod till en formulärkontroll som en knapp med Aspose.Cells for JavaScript via C++. 
keywords: Tilldela makro till formulärkontroll JavaScript via C++, makkod för formulärkontroll JavaScript via C++, integrerad makro i XLSM JavaScript via C++
---

{{% alert color="primary" %}}

Aspose.Cells låter dig tilldela ett makro kod till en formulärkontroll som en knapp. Använd [**Shape.macroName**](https://reference.aspose.com/cells/javascript-cpp/shape/#macroName--) -egenskapen för att tilldela en ny makro kod till en formulärkontroll i arbetsboken.

{{% /alert %}}

Följande kodexempel skapar en ny arbetsbok, tilldelar ett makrokod till en formulärknapp och sparar resultatet i XLSM-format. När du öppnar XLSM-filen i Microsoft Excel, kommer du att se följande makrokod.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Tilldela makro till formulärkontroll i JavaScript**



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add VBA Module and Button</title>
    </head>
    <body>
        <h1>Add VBA Module and Button Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (fileInput.files.length && fileInput.files[0]) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                var workbook = new Workbook();
            }

            // Accessing the first worksheet in the workbook
            const sheet = workbook.worksheets.get(0);

            // Adding a VBA module to the workbook tied to the sheet
            const moduleIdx = workbook.vbaProject.modules.add(sheet);
            const module = workbook.vbaProject.modules.get(moduleIdx);
            module.codes = "Sub ShowMessage()\r\n" +
                           "    MsgBox \"Welcome to Aspose!\"\r\n" +
                           "End Sub";

            // Adding a button shape to the sheet
            const button = sheet.shapes.addButton(2, 0, 2, 0, 28, 80);
            button.placement = AsposeCells.PlacementType.FreeFloating;
            button.font.name = "Tahoma";
            button.font.isBold = true;
            button.font.color = AsposeCells.Color.Blue;
            button.text = "Aspose";

            // Assigning the macro name to the button
            button.macroName = sheet.name + ".ShowMessage";

            // Saving the modified workbook as an XLSM file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel.sheet.macroEnabled.12' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified XLSM File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module and button added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
