---
title: Einen vorhandenen Stil ändern
linktitle: Einen vorhandenen Stil ändern
description: Aspose.Cells ist eine JavaScript Bibliothek via C++ zur Arbeit mit Tabellenkalkulationsdateien, die es Benutzern ermöglicht, vorhandene Zellstile zu ändern. Dieser Artikel stellt vor, wie man einen bestehenden Zellstil mit der Aspose.Cells Bibliothek modifiziert, damit Benutzer das Erscheinungsbild der Zellen nach Bedarf ändern können.
keywords: Existierende Stile ändern, das Erscheinungsbild Ihrer Anwendung anpassen, Anleitungen, Tutorials, Hilfedokumentationen, Entwicklerdokumentationen, API Referenzen, Beispielcode, Downloads, Support.
type: docs
weight: 90
url: /de/javascript-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Um dieselben Formatierungsoptionen auf Zellen anzuwenden, erstellen Sie ein neues Formatierungsstil-Objekt. Ein Formatierungsstil-Objekt ist eine Kombination von Formatierungseigenschaften, wie Schriftart, Schriftgröße, Einzug, Nummer, Rand, Muster usw., benannt und als Satz gespeichert. Wenn angewendet, werden alle Formatierungen in diesem Stil angewendet.

Sie können auch einen vorhandenen Stil verwenden, diesen mit der Arbeitsmappe speichern und zur Formatierung von Informationen mit den gleichen Attributen verwenden.

Wenn Zellen nicht explizit formatiert sind, wird der **Normal**-Stil (der Standardstil der Arbeitsmappe) angewendet. Microsoft Excel definiert neben dem Normalstil mehrere Stile, darunter Komma, Währung und Prozent.

Aspose.Cells ermöglicht die Änderung aller dieser Stile oder eines anderen Stils, den Sie mit Ihren gewünschten Attributen definieren.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

So aktualisieren Sie einen Stil in Microsoft Excel 97-2003:

1. Klicken Sie im Menü **Format** auf **Stil**.
1. Wählen Sie den Stil aus, den Sie aus der Liste **Stilname** ändern möchten.
1. Klicken Sie auf **Ändern**.
1. Wählen Sie die Stiloptionen aus, die Sie mithilfe der Registerkarten im Dialogfeld Zellen formatieren möchten.
1. Klicken Sie auf **OK**.
1. Legen Sie unter **Stil enthält** die gewünschten Stileigenschaften fest.
1. Klicken Sie auf **OK**, um den Stil zu speichern und auf den ausgewählten Bereich anzuwenden.

## **Mit Aspose.Cells for JavaScript via C++ verwenden**

Die folgenden Beispiele zeigen, wie man die [**Style.update()**](https://reference.aspose.com/cells/javascript-cpp/style/#update--)-Methode verwendet.

### **Erstellen und Ändern eines Stils**

Dieses Beispiel erstellt ein [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt, wendet es auf einen Zellbereich an und ändert das [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt. Die Änderungen werden automatisch auf die Zellen und den Bereich angewendet, auf den die Stil angewendet wurde.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Style Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const resultDiv = document.getElementById('result');

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a new style object.
            const style = workbook.createStyle();

            // Set the number format.
            style.number = 14;

            // Set the font color to red color.
            style.font.color = AsposeCells.Color.Red;

            // Name the style.
            style.name = "Date1";

            // Get the first worksheet cells.
            const cells = workbook.worksheets.get(0).cells;

            // Specify the style (described above) to A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.style = style;

            // Create a range (B1:D1).
            const range = cells.createRange("B1", "D1");

            // Initialize styleflag object.
            const flag = new AsposeCells.StyleFlag();

            // Set all formatting attributes on.
            flag.all = true;

            // Apply the style (described above) to the range.
            range.applyStyle(style, flag);

            // Modify the style (described above) and change the font color from red to black.
            style.font.color = AsposeCells.Color.Black;

            // Done! Since the named style (described above) has been set to a cell and range, 
            // The change would be reflected(new modification is implemented) to cell(A1) and 
            // Range (B1:D1).
            style.update();

            // Save the excel file. 
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book_styles.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **Ändern eines vorhandenen Stils**

Dieses Beispiel verwendet eine einfache Vorlagendatei in Excel, auf die bereits ein Stil namens Prozent auf einen Bereich angewendet wurde. Das Beispiel:

1. holt den Stil,
1. erstellt ein Stil-Objekt und
1. ändert die Formatierung des Stils.

Die Änderungen werden automatisch auf den Bereich angewendet, auf den der Stil angewendet wurde.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Named Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, Utils } = AsposeCells;

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

            // Create a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the named style "Percent" via the styles collection
            const style = workbook.styles.get("Percent");

            // Change the number format to "0.00%".
            style.number = 11;

            // Set the font color.
            style.font.color = Color.Red;

            // Update the style so ranges using this named style are updated.
            style.update();

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book2.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Style updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
