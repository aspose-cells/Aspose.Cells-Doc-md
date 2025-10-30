---
title: Umwandlung von Tabellenblatt in Bild und Tabellenblatt in Bild nach Seite mit JavaScript via C++
linktitle: Arbeitsblatt in Bild und Arbeitsblatt in Bild pro Seite konvertieren
type: docs
weight: 80
url: /de/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}
Dieses Dokument soll Entwicklern ein detailliertes Verständnis darüber vermitteln, wie ein Arbeitsblatt in eine Bilddatei umgewandelt werden kann und wie man mehrere Seiten eines Arbeitsblatts in eine Bilddatei pro Seite umwandelt.

Manchmal müssen Arbeitsblätter als Bilder präsentiert werden, zum Beispiel um sie in Anwendungen oder Webseiten zu verwenden. Sie müssen die Bilder möglicherweise in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Im Grunde genommen möchten Sie das Arbeitsblatt als Bild rendern. Aspose.Cells unterstützt die Umwandlung von Arbeitsblättern in Microsoft Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells die Umwandlung eines Arbeitsmappen in mehrere Bilddateien, eine pro Seite.

Möglicherweise verwenden Sie Office Automation, um dies zu erreichen, aber Office-Automation hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme, beispielsweise Sicherheit, Stabilität, Skalierbarkeit/Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, aber der Hauptgrund ist, dass Microsoft selbst dringend von der Verwendung von Office-Automation abrät.
{{% /alert %}}

## ** Verwendung von Aspose.Cells for JavaScript via C++, um Tabellenblatt in Bilddatei umzuwandeln**

Dieser Artikel zeigt, wie man eine Konsolenanwendung erstellt, ein Arbeitsblatt in ein Bild umwandelt und ein Arbeitsblatt in ein Bild für jedes Arbeitsblatt mit wenigen und einfachen Zeilen Code mit der Aspose.Cells API übersetzt.

 Sie müssen mehrere wertvolle Klassen im Zusammenhang mit Rendering-Funktionalitäten in Ihr Programm oder Projekt importieren, z. B. [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender/) usw. Die Klasse [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) repräsentiert ein Tabellenblatt zum Rendern von Bildern für das Tabellenblatt und hat eine Überladung der [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)-Methode, die ein Tabellenblatt direkt mit beliebigen Attributen oder Optionen in Bilddateien umwandeln kann. Sie kann ein Bildobjekt zurückgeben, und Sie können eine Bilddatei auf die Festplatte/den Stream speichern. Mehrere Bildformate werden unterstützt, z. B. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF und andere.

Dieser Artikel erklärt, wie:

- Ein Arbeitsblatt in ein Bild konvertiert wird
- Jede Seite in einem Arbeitsblatt in ein Bild konvertiert wird

Diese Aufgabe zeigt, wie man Aspose.Cells verwendet, um ein Arbeitsblatt aus einer Vorlagenarbeitsmappe in eine Bilddatei zu konvertieren.

### **Setup-Projekt**

1. Laden Sie zuerst [Aspose.Cells for JavaScript via C++ herunter](https://downloads.aspose.com/cells/javascript-cpp).
1. Installieren Sie es auf Ihrem Entwicklungssystem. Alle [Aspose](http://www.aspose.com/) Komponenten funktionieren im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat keine zeitliche Begrenzung und fügt nur Wasserzeichen in die erstellten Dokumente ein. Starten Sie nun Ihre Entwicklungsumgebung und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel verwendet eine JavaScript-Konsole, aber Sie können jede Einrichtung verwenden, die mit JavaScript integriert ist. Fügen Sie einen Verweis auf Aspose.Cells in das erstellte Projekt ein.

### **Arbeitsblatt in Bilddatei konvertieren**

Ich habe eine neue Arbeitsmappe in Microsoft Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt: **Testbook.xlsx** (1 Arbeitsblatt). Konvertieren Sie als Nächstes das Arbeitsblatt Sheet1 der Vorlagendatei in eine Bilddatei namens SheetImage.jpg.

Nachfolgend ist der von der Komponente verwendete Code, um die Aufgabe zu erledigen. Es konvertiert Sheet1 in **Testbook.xlsx** in eine Bilddatei, um zu erklären, wie einfach diese Konvertierung ist.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Convert Worksheet to Image Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.onePagePerSheet = true;

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image data for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputConvertWorksheettoImageFile.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet converted to image successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```

## ** Verwendung von Aspose.Cells for JavaScript via C++ zur Umwandlung eines Tabellenblatts in eine Bilddatei nach Seite**

Dieses Beispiel zeigt, wie man Aspose.Cells verwendet, um ein Arbeitsblatt aus einer Vorlagenarbeitsmappe, die mehrere Seiten hat, in eine Bilddatei pro Seite zu konvertieren.

### **Arbeitsblatt seitenweise in Bild umwandeln**

Ich habe eine neue Arbeitsmappe in Microsoft Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt: **Testbook2.xlsx** (1 Arbeitsblatt).

Konvertieren Sie jetzt das Arbeitsblatt Sheet1 der Vorlagendatei in Bilddateien (eine Datei pro Seite). Da ich die Konsolenanwendung bereits erstellt habe, um die Kopieraufgabe auszuführen, werde ich diese Schritte zur Erstellung der Konsolenanwendung überspringen und direkt zu den Arbeitsblattkonvertierungsschritten übergehen.

Der folgende Code wird vom Component zum Erreichen der Aufgabe verwendet. Er wandelt Sheet1 in Testbook2.xlsx in Bilder nach Seitenzahl um.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet to Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet to Images By Page</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div id="downloadLinks"></div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender, Utils } = AsposeCells;

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
            const linksDiv = document.getElementById('downloadLinks');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Create image/print options and set properties
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);

            const pageCount = sr.pageCount;
            const createdLinks = [];

            for (let j = 0; j < pageCount; j++) 
            {
                // toImage returns image data for the specified page
                const outputData = sr.toImage(j);
                const blob = new Blob([outputData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                const pageNumber = j + 1;
                const fileName = 'outputConvertWorksheetToImageByPage_' + pageNumber + '.tif';
                link.href = url;
                link.download = fileName;
                link.textContent = 'Download ' + fileName;
                link.style.display = 'block';
                linksDiv.appendChild(link);
                createdLinks.push(url);
            }

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Click the links below to download the generated TIFF images.</p>';
        });
    </script>
</html>
```
