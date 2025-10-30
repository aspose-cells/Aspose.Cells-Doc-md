---
title: Uppdatera ActiveX kombinationsrute kontroll med JavaScript via C++
linktitle: Uppdatera ActiveX ComboBox kontroll
type: docs
weight: 170
url: /sv/javascript-cpp/update-activex-combobox-control/
description: Lära dig hur man läser och skriver värden av ActiveX ComboBox kontroll med Aspose.Cells for JavaScript via C++. 
---

## **Möjliga användningsscenario**
Du kan läsa eller skriva värdena för ActiveX ComboBox kontroll med Aspose.Cells for JavaScript via C++. Vänligen få åtkomst till ActiveX-kontrollen via [Shape.activeXControl](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) egenskapen och kontrollera dess typ via [ActiveXControlBase.type](https://reference.aspose.com/cells/javascript-cpp/activexcontrolbase/#type--) egenskapen, den bör returnera värdet [ControlType.ComboBox](https://reference.aspose.com/cells/javascript-cpp/controltype/) och sedan konvertera det till [ComboBoxActiveXControl](https://reference.aspose.com/cells/javascript-cpp/comboboxactivexcontrol/) objekt och läsa eller ändra dess olika egenskaper.

Vänligen ladda ner den [provexemplet Excel-fil](5115124.xlsx) som används i följande provkod.
## **Uppdatera ActiveX ComboBox Control**
Följande skärmbild visar effekten av provkoden på den [provexemplet Excel-filen](5115124.xlsx). Som du kan se har ActiveX ComboBox-värdet uppdaterats till "Detta är kombinationsruta-kontroll".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Exempelkod**
Följande provkod uppdaterar värdet för ActiveX ComboBox Control som finns i [provexemplet Excel-filen](5115124.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update ActiveX ComboBox</title>
    </head>
    <body>
        <h1>Update ActiveX ComboBox in Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and first shape
            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            // Access ActiveX ComboBox Control and update its value
            if (shape.activeXControl != null) {
                const c = shape.activeXControl;

                if (c instanceof AsposeCells.ComboBoxActiveXControl) {
                    // Type cast ActiveXControl into ComboBoxActiveXControl and change its value
                    const comboBoxActiveX = new AsposeCells.ComboBoxActiveXControl(c);
                    comboBoxActiveX.value = "This is combo box control with updated value.";
                }
            }

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
