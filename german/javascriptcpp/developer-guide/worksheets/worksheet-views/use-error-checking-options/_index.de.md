---
title: Fehlerprüfungseinstellungen mit JavaScript via C++ verwenden
linktitle: Verwenden von Fehlerüberprüfungsoptionen
type: docs
weight: 140
url: /de/javascript-cpp/use-error-checking-options/
description: Lernen Sie, wie Sie Fehlerüberprüfungsoptionen in Excel Arbeitsblättern mithilfe von Aspose.Cells for JavaScript via C++ programmatisch verwenden.
keywords: Zahl als Text in Excel speichern mit JavaScript via C++, Fehlerüberprüfung von Excel Optionen JavaScript via C++
---

{{% alert color="primary" %}}  
Microsoft Excel ermöglicht es Benutzern, Fehlerprüfoptionen und -regeln zu definieren. Benutzer sehen oft Fehlerprüfungen beim Erstellen von Formeln, ein kleines Dreieck in der oberen rechten Ecke einer Zelle markiert, wenn ein Problem mit einer Zelle vorliegt. Excel bietet Informationen, die den Benutzern helfen, häufige Probleme zu korrigieren.  
{{% /alert %}}  

## **Arten von Fehlern**  

Fehler, die bedeuten, dass die Formel kein Ergebnis zurückgeben kann – wie das Teilen einer Zahl durch Null – erfordern sofortige Aufmerksamkeit und eine Fehlermeldung im Zelle. Das Klicken auf das grüne Dreieck zeigt ein Ausrufezeichen; durch Klicken öffnet sich eine Optionsliste.  

Der Fehler kann mithilfe der Optionen behoben oder ignoriert werden. Das Ignorieren eines Fehlers bedeutet, dass dieser Fehler bei weiteren Fehlerprüfungen nicht angezeigt wird.  

Aspose.Cells bietet Funktionen für Fehlerüberprüfung. Die Klasse [**ErrorCheckOption**](https://reference.aspose.com/cells/javascript-cpp/errorcheckoption) verwaltet verschiedene Arten von Fehlerprüfungen, zum Beispiel Nummern, die als Text gespeichert sind, Formelfeld-Fehler und Validierungsfehler. Verwenden Sie die Aufzählung [**ErrorCheckType**](https://reference.aspose.com/cells/javascript-cpp/errorchecktype), um die gewünschte Fehlerüberprüfung festzulegen.  

## **Als Text gespeicherte Zahlen**  

Gelegentlich werden Zahlen formatiert und in Zellen als Text gespeichert. Dies kann Probleme bei Berechnungen verursachen oder irreführende Sortierreihenfolgen erzeugen. Zahlen, die als Text formatiert sind, sind in der Zelle linksbündig anstelle von rechtsbündig. Wenn eine Formel, die eine mathematische Operation mit Zellen durchführen sollte, kein Ergebnis zurückgibt, überprüfen Sie die Ausrichtung in den Zellen, auf die sich die Formel bezieht - einige oder alle diese Zellen könnten als Text formatierte Zahlen sein.  

Sie können die Fehlerprüfungsoptionen verwenden, um Zahlen, die als Text gespeichert sind, schnell in echte Zahlen umzuwandeln. In Microsoft Excel 2003:  

1. Klicken Sie im Menü **Extras** auf **Optionen**.  
1. Wählen Sie den Tab Fehlerüberprüfung aus.  
   Die Option **Als Text gespeicherte Zahl** ist standardmäßig aktiviert.  
1. Deaktivieren Sie es.  

Der folgende Beispielcode zeigt, wie Sie die Option zur Fehlerprüfung von als Text gespeicherten Zahlen für ein Arbeitsblatt in der Vorlage XLS-Datei mithilfe der Aspose.Cells-APIs deaktivieren.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Error Check Options</title>
    </head>
    <body>
        <h1>Error Check Options Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook by reading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Instantiate the error checking options
            const opts = sheet.errorCheckOptions;

            const index = opts.add();
            const opt = opts.get(index);
            // Disable the numbers stored as text option
            // Converted from opt.setErrorCheck(type, value) to a property-style assignment
            opt.errorCheck = opt.errorCheck || {};
            opt.errorCheck[AsposeCells.ErrorCheckType.NumberStoredAsText] = false;
            // Set the range
            opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

            // Save the Excel file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_test.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
