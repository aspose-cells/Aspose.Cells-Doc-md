---
title: Wie verhindert man, dass Benutzer Excel Dateien drucken, mit JavaScript über C++
linktitle: Wie verhindert man, dass Benutzer eine Excel Datei drucken
type: docs
weight: 600
url: /de/javascript-cpp/how-to-prevent-printing-excel/
description: Erfahren Sie, wie Sie verhindern, dass Benutzer Excel Dateien mit Aspose.Cells for JavaScript über C++ drucken.
keywords: Excel Druck, Excel Druck verhindern, wie man das Drucken von Excel verhindert, Excel Druck verhindern, das Drucken des gesamten Arbeitsmappens mit VBA verhindern
---

## **Mögliche Verwendungsszenarien**  
In unserer täglichen Arbeit können wichtige Informationen in der Excel-Datei enthalten sein; um die Verbreitung interner Daten zu verhindern, erlaubt die Firma keinen Druck. Dieses Dokument zeigt, wie Sie andere vom Drucken von Excel-Dateien abhalten können.  

## **Wie man das Drucken einer Datei in MS-Excel verhindert**  
Sie können den folgenden VBA-Code anwenden, um Ihre spezifische Datei vor dem Drucken zu schützen.  
1. Öffnen Sie Ihre Arbeitsmappe, die Sie anderen nicht erlauben möchten zu drucken.  
1. Wählen Sie die Registerkarte **Entwicklertools** im Excel-Ribbon und klicken Sie auf die Schaltfläche **Code anzeigen** im Abschnitt **Steuerelemente**. Alternativ können Sie die Tasten ALT + F11 drücken, um das Microsoft Visual Basic for Applications Fenster zu öffnen.  
<br>  
<img src="1.png" width=70% />  
1. Und dann im linken Projekt-Explorer doppelklicken Sie auf ThisWorkbook, um das Modul zu öffnen, und fügen Sie einige VBA-Codes hinzu.  
<br>  
<img src="2.png" width=70% />  
1. Speichern und schließen Sie dieses Codefenster, kehren Sie zum Arbeitsbuch zurück, und wenn Sie die Beispiel-Datei drucken, wird dies nicht erlaubt, und Sie erhalten folgende Warnmeldung:  
<br>  
<img src="3.png" width=70% />  

## **Wie man verhindert, dass Benutzer Excel-Dateien mit Aspose.Cells for JavaScript über C++ drucken**  

Das folgende Beispiel zeigt, wie man das Drucken einer Excel-Datei durch Benutzer verhindert:  

1. Laden Sie die [Beispieldatei](sample.xlsx).  
1. Holen Sie sich das VbaModuleCollection-Objekt aus der VbaProject-Eigenschaft der Arbeitsmappe.  
1. Holen Sie sich das VbaModule-Objekt über den Namen "ThisWorkbook".  
1. Setzen Sie die Eigenschaften des VbaModule-Codes.  
1. Speichern Sie die Beispieldatei im [xlsm-Format](out.xlsm).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update VBA Module Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing VBA project and its modules
            const modules = workbook.vbaProject.modules;
            const module = modules.get("ThisWorkbook");

            // Setting module codes (converted from setCodes -> codes assignment)
            module.codes = "Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n";

            // Saving the modified workbook as macro-enabled workbook
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
