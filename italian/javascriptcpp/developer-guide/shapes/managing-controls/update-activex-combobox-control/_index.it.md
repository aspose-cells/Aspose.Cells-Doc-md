---
title: Aggiorna il controllo ComboBox ActiveX con JavaScript tramite C++
linktitle: Aggiorna il controllo ComboBox ActiveX
type: docs
weight: 170
url: /it/javascript-cpp/update-activex-combobox-control/
description: Impara come leggere e scrivere i valori del controllo ComboBox ActiveX usando Aspose.Cells for JavaScript tramite C++. 
---

## **Possibili Scenari di Utilizzo**
Puoi leggere o scrivere i valori del controllo ComboBox ActiveX usando Aspose.Cells for JavaScript tramite C++. Accedi al controllo ActiveX tramite la proprietà [Shape.activeXControl](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) e verifica il suo tipo tramite la proprietà [ActiveXControlBase.type](https://reference.aspose.com/cells/javascript-cpp/activexcontrolbase/#type--), che dovrebbe restituire il valore [ControlType.ComboBox](https://reference.aspose.com/cells/javascript-cpp/controltype/) e quindi tipizzarlo in [ComboBoxActiveXControl](https://reference.aspose.com/cells/javascript-cpp/comboboxactivexcontrol/) per leggere o modificare le sue varie proprietà.

Si prega di scaricare il [file Excel di esempio](5115124.xlsx) utilizzato nel seguente codice di esempio.
## **Aggiorna il controllo ComboBox ActiveX**
Lo screenshot seguente mostra l'effetto del codice di esempio sul [file Excel di esempio](5115124.xlsx). Come si può vedere, il valore del ComboBox ActiveX è stato aggiornato a "Questo è un controllo combobox".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Codice di Esempio**
Il seguente codice di esempio aggiorna il valore del controllo ActiveX ComboBox presente all'interno del [file Excel di esempio](5115124.xlsx).

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
