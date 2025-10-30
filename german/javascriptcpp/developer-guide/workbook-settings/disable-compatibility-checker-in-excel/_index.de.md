---
title: Deaktivieren Sie den Kompatibilitätsprüfer in Excel mit JavaScript über C++
linktitle: Kompatibilitätsprüfung in Excel deaktivieren
type: docs
weight: 170
url: /de/javascript-cpp/disable-compatibility-checker-in-excel/
description: Erfahren Sie, wie Sie den Kompatibilitätsprüfer über das Aspose.Cells for JavaScript via C++ API deaktivieren.
keywords: JavaScript Deaktivieren des Kompatibilitätsprüfers, Excel Deaktivieren des Kompatibilitätsprüfers in JavaScript via C++, Deaktivieren des Kompatibilitätsprüfers in Arbeitsmappe.
---

## Deaktivieren Sie den Kompatibilitätsprüfer in Excel-Tabellen in JavaScript  

{{% alert color="primary" %}}  
Microsoft Excels Kompatibilitätsprüfer warnt, wenn das Speichern einer Datei in einem früheren Dateiformat zu Funktionsproblemen oder Qualitätsverlust führen könnte. Der Kompatibilitätsprüfer ist eine Funktion von Microsoft Office Excel 2007 und Microsoft Excel 2010.  

Wenn Sie eine Arbeitsmappe in einer früheren Version, Excel 97 bis Excel 2003, von Excel 2007 oder Excel 2010 speichern, durchsucht der Kompatibilitätsprüfer die Arbeitsmappe, um festzustellen, ob sie Funktionen enthält, die von der früheren Version nicht unterstützt werden. Um Ihnen bei Entscheidungen über den Umgang mit Kompatibilitätsproblemen zu helfen, zeigt der Kompatibilitätsprüfer Dialogfelder mit Optionen an. Er kann auch verwendet werden, um einen Bericht über Probleme in der Arbeitsmappe zu erstellen oder das Feature zu deaktivieren.  

Manchmal müssen Sie den Kompatibilitätsprüfer für eine bestimmte Tabelle deaktivieren. Mit den APIs von Aspose.Cells können Sie dies programmatisch tun, sodass Benutzer nicht durch das pop-up Fenster des Kompatibilitätsprüfers verwirrt oder frustriert werden, wenn sie die Datei in Microsoft Excel manuell erneut speichern.  
{{% /alert %}}  

## **Wie Sie den Kompatibilitätsprüfer in Microsoft Excel deaktivieren**  

Um den Kompatibilitätsprüfer in Microsoft Excel zu deaktivieren (z.B. Microsoft Excel 2007/2010):  

- (Excel 2007) Klicken Sie auf die Office-Schaltfläche, dann auf **Vorbereiten**, anschließend auf **Kompatibilitätsprüfung ausführen** und deaktivieren Sie die Option **Kompatibilität beim Speichern dieser Arbeitsmappe prüfen**.  
- (Excel 2010) Klicken Sie auf die Registerkarte **Datei**, dann auf **Info**, klicken Sie auf **Nach Problemen suchen**, klicken Sie auf **Kompatibilität prüfen** und deaktivieren Sie anschließend die Option **Kompatibilität prüfen, wenn Sie diese Arbeitsmappe speichern**.  

## **So deaktivieren Sie den Kompatibilitätsprüfer mithilfe von Aspose.Cells-APIs**  

Setzen Sie die Eigenschaft [**Workbook.checkCompatibility**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCompatibility--) auf **false**, um den Kompatibilitätsprüfer von Microsoft Excel zu deaktivieren.  

### **Codebeispiele**  

Die folgenden Codebeispiele zeigen, wie der Kompatibilitätsprüfer mit Aspose.Cells for JavaScript via C++ deaktiviert werden kann.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Compatibility Checker Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Disable the compatibility checker
            workbook.settings.checkCompatibility = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_BK_CompCheck.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Compatibility check disabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
