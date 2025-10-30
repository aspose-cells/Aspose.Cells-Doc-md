---
title: Wie man ein Bild in eine Zelle einfügt
type: docs
weight: 130
url: /de/javascript-cpp/how-to-insert-picture-in-cell/
description: Erfahren Sie, wie Sie ein Bild mit Aspose.Cells for JavaScript via C++ in eine Zelle einfügen.
keywords: Wie man ein Bild in einer Zelle einfügt, ein Bild über Zellen einfügt, ein Bild in einer Zelle platziert, ein Bild über Zellen platziert, wie man ein Bild in einer Zelle platziert, wie man ein Bild über Zellen platziert, zwischen Bild in Zelle und Bild über Zellen wechseln, zwischen Platz in Zelle und Platz über Zellen wechseln.
---

## **Mögliche Verwendungsszenarien**
Das Bild verleiht Ihrem Arbeitsblatt einen Hauch von Helligkeit und bietet eine visuelle Darstellung des Inhalts. Sie erleichtern es auch, die Daten zu verstehen und Erkenntnisse zu gewinnen. Obwohl Sie seit vielen Jahren Bilder in Excel verwenden konnten, hat Excel erst kürzlich die Funktion aktiviert, dass Bilder tatsächliche Zellwerte werden. Selbst wenn das Layout der Zeichnung geändert wird, bleibt sie weiterhin mit den Daten verbunden. Sie können sie in Tabellen verwenden, sortieren, filtern, in Formeln einbeziehen und so weiter!

## **Wie man ein Bild in eine Zelle einfügt mit Excel**
Zum Einfügen eines Bildes in eine Zelle in Excel befolgen Sie diese Schritte:

1. Gehen Sie zum Register 'Einfügen' und klicken Sie auf die Option 'Bilder'.
2. Wählen Sie **Platzieren in Zelle** aus. Wählen Sie eine der folgenden Quellen aus dem Dropdown-Menü 'Bild einfügen von' aus (**Dieses Gerät**, **Stockbilder** und **Online-Bilder**). Dieses Gerät zum Einfügen eines Bildes von Ihrem Gerät. Stockbilder zum Einfügen eines Bildes aus Stockbildern. Online-Bilder zum Einfügen eines Bildes aus dem Web.
<br>
<img src="1.png" width=60% />
3. Bild auswählen und Bild in Zelle einfügen.
<br>
<img src="8.png" width=60% />

## **Wie man ein Bild über Zellen in Excel einfügt**
Zum Einfügen eines Bildes über Zellen in Excel befolgen Sie diese Schritte:

1. Gehen Sie zum Register 'Einfügen' und klicken Sie auf die Option 'Bilder'.
2. Wählen Sie **Über Zellen platzieren** aus. Wählen Sie eine der folgenden Quellen aus dem Dropdown-Menü 'Bild einfügen von' aus (**Dieses Gerät**, **Stockbilder** und **Online-Bilder**). Dieses Gerät zum Einfügen eines Bildes von Ihrem Gerät. Stockbilder zum Einfügen eines Bildes aus Stockbildern. Online-Bilder zum Einfügen eines Bildes aus dem Web.
<br>
<img src="2.png" width=60% />
3. Bild auswählen und Bild über Zellen einfügen.
<br>
<img src="3.png" width=60% />

## **Wie man von Bild in Zelle zu Bild über Zellen in Excel wechselt**
Sie können ganz einfach von **Bild in Zelle** zu **Bild über Zellen** wechseln. Befolgen Sie bitte diese Schritte:
1. Klicken Sie mit der rechten Maustaste auf die Zelle und wählen Sie **Bild in Zelle** > **Über Zellen platzieren**. 
<br>
<img src="4.png" width=60% />
2. Das Ergebnis nach dem Umschalten lautet wie folgt:
<br>
<img src="5.png" width=60% />

## **Wie man von Bild über Zellen zu Bild in Zelle in Excel wechselt**
Sie können ganz einfach von **Bild über Zellen** zu **Bild in Zelle** wechseln. Befolgen Sie bitte diese Schritte:
1. Klicken Sie mit der rechten Maustaste auf das Bild und wählen Sie **In Zelle platzieren**. 
<br>
<img src="6.png" width=60% />
2. Das Ergebnis nach dem Umschalten lautet wie folgt:
<br>
<img src="7.png" width=60% />

## **Wie man ein Bild in die Zelle mit Aspose.Cells for JavaScript via C++ einfügt**
Bild in Zelle mit Aspose.Cells einfügen. Bitte beachten Sie den folgenden Beispielcode. Nach Ausführung des Beispielcodes wird ein Bild in eine Zelle eingefügt.
1. Erstellen Sie ein Workbook-Objekt. 
2. Holen Sie sich die Zelle, in die Sie das Bild einfügen möchten.
3. Setzen Sie die Eigenschaft Cell.EmbeddedImage. 
4. Schließlich wird die Arbeitsmappe im [XLSX-Ausgabeformat](out.xlsx) gespeichert. 

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Embed Image into New Workbook</h1>
        <p>Select an image file to embed into cell D8. A new workbook will be created with "Apple" in A2.</p>
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            // Create a new workbook
            const workbook = new Workbook();
            const cells = workbook.worksheets.get(0).cells;

            // Set A2 value to "Apple"
            const a2 = cells.get("A2");
            a2.value = "Apple";

            // Get D8 cell
            const d8 = cells.get("D8");

            // If an image file is selected, read it and embed into D8
            if (imageInput.files.length) {
                const file = imageInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const imgBuf = new Uint8Array(arrayBuffer);
                d8.embeddedImage = imgBuf;
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
