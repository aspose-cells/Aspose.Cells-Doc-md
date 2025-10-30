---
title: ActiveX ComboBox Steuerelement mit JavaScript über C++ aktualisieren
linktitle: Aktualisieren Sie die ActiveX ComboBox Steuerelemente
type: docs
weight: 170
url: /de/javascript-cpp/update-activex-combobox-control/
description: Lernen Sie, wie Sie Werte des ActiveX ComboBox Steuerelements mit Aspose.Cells for JavaScript über C++ lesen und schreiben. 
---

## **Mögliche Verwendungsszenarien**
Sie können die Werte des ActiveX-ComboBox-Steuerelements mit Aspose.Cells for JavaScript über C++ lesen oder schreiben. Greifen Sie auf das ActiveX-Steuerelement über die [Shape.activeXControl](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) Eigenschaft zu und prüfen Sie den Typ über die [ActiveXControlBase.type](https://reference.aspose.com/cells/javascript-cpp/activexcontrolbase/#type--) Eigenschaft. Es sollte den Wert [ControlType.ComboBox](https://reference.aspose.com/cells/javascript-cpp/controltype/) zurückgeben und dann in ein [ComboBoxActiveXControl](https://reference.aspose.com/cells/javascript-cpp/comboboxactivexcontrol/) Objekt umgewandelt werden, um verschiedene Eigenschaften zu lesen oder zu modifizieren.

Bitte laden Sie die im folgenden Beispielcode verwendete [Beispieldatei](5115124.xlsx) herunter.
## **Aktualisieren Sie das ActiveX-ComboBox-Steuerelement**
Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die [Beispieldatei](5115124.xlsx). Wie Sie sehen können, wurde der Wert der ActiveX-ComboBox auf "Dies ist die Kombinationsfeldsteuerung" aktualisiert.

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Beispielcode**
Der folgende Beispielcode aktualisiert den Wert des ActiveX-ComboBox-Steuerungselements, das sich in der [Beispieldatei Excel](5115124.xlsx) befindet.

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
