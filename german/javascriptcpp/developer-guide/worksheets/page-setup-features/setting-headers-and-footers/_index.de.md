---
title: Header und Footer mit JavaScript über C++ festlegen
linktitle: Festlegen von Kopf und Fußzeilen
type: docs
weight: 30
url: /de/javascript-cpp/setting-headers-and-footers/
description: Dieser Artikel erklärt, wie man programmatisch ein Bild in den Header und Footer von Excel Arbeitsblättern mit Aspose.Cells for JavaScript über C++ einfügt. 
keywords: Bild in Excel Header/Footer JavaScript über C++, Excel Header Footer Skriptbefehle in JavaScript via C++ setzen
---

{{% alert color="primary" %}}

Header und Fußzeilen sind die Zeilen mit Text, die unterhalb des oberen Randes oder oberhalb des unteren Randes angezeigt werden. Es ist auch möglich, Header und Fußzeilen zu den Arbeitsblättern hinzuzufügen. Header und Fußzeilen können genutzt werden, um nützliche Informationen wie Seitenzahl, Autorname, Thema oder Datum und Uhrzeit anzuzeigen. Header und Fußzeilen werden über die Seiteneinrichtungseinstellungen verwaltet.

{{% /alert %}}

## **Kopf- und Fußzeilen einstellen**

Aspose.Cells for JavaScript über C++ ermöglicht das Hinzufügen von Headern und Fußzeilen zu Arbeitsblättern zur Laufzeit, wir empfehlen jedoch, Header und Footer manuell in einer vorgefertigten Datei für den Druck einzustellen. Sie können Microsoft Excel als GUI-Tool verwenden, um Header und Footer einzustellen, um Aufwand und Entwicklungszeit zu sparen. Aspose.Cells kann die Datei importieren und die Einstellungen speichern.

Um Header und Fußzeilen dynamisch hinzuzufügen, bietet Aspose.Cells spezielle API-Aufrufe und Skriptbefehle zur Formatierung von Header und Fußzeilen.

### **Skriptbefehle**

Skriptbefehle sind besondere Befehle, die es ermöglichen, die Formatierung von Header und Fußzeilen festzulegen.

|**Skriptbefehle**|**Beschreibung**|
| :- | :- |
|&P|Aktuelle Seitennummer|
|&G|Ein Bild|
|&N|Gesamtanzahl der Seiten|
|&D|Aktuelles Datum|
|&T|Aktuelle Uhrzeit|
|&A|Name des Arbeitsblatts|
|&F|Dateiname ohne Pfadangabe|
|&&Text|Zeigt &Text. Zum Beispiel: &&WO wird als &WO angezeigt|
|&"\<FontName>"|Stellt einen Schriftartnamen dar. Beispiel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Stellt Schriftartnamen mit Stil dar. Beispiel: &"Arial,Fett"|
|&\<FontSize>|Stellt die Schriftgröße dar. Zum Beispiel: “&14abc”. Wenn jedoch dieser Befehl von einer reinen Zahl gefolgt wird, die im Kopf gedruckt werden soll, sollte diese durch ein Leerzeichen von der Schriftgröße getrennt werden. Zum Beispiel: “&14 123”.|

### **Header und Fußzeilen festlegen**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) bietet zwei Methoden, [**header(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-string-) und [**footer(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-string-), mit denen ein Header und Footer zu einem Arbeitsblatt hinzugefügt werden. Diese Methoden benötigen nur zwei Parameter:

- **Abschnitt** – der Abschnitt, in dem der Header oder die Fußzeile platziert werden soll. Es gibt drei Abschnitte: links, zentriert und rechts, die jeweils durch 0, 1 und 2 dargestellt werden.
- **Skript** – das Skript, das für den Header oder die Fußzeile verwendet werden soll. Dieses Skript enthält Skriptbefehle zur Formatierung von Headern oder Fußzeilen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Set Headers and Footers Example</h1>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            // Setting worksheet name at the left section of the header
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[0] = "&A";

            // Setting current date and current time at the central section of the header
            // and changing the font of the header
            pageSetup.header[1] = "&\"Times New Roman,Bold\"&D-&T";

            // Setting current file name at the right section of the header and changing the
            // font of the header
            pageSetup.header[2] = "&\"Times New Roman,Bold\"&12&F";

            // Setting a string at the left section of the footer and changing the font
            // of a part of this string ("123")
            pageSetup.footer = pageSetup.footer || [];
            pageSetup.footer[0] = "Hello World! &\"Courier New\"&14 123";

            // Setting the current page number at the central section of the footer
            pageSetup.footer[1] = "&P";

            // Setting page count at the right section of footer
            pageSetup.footer[2] = "&N";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetHeadersAndFooters_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers and footers set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Fügen Sie ein Bild in einen Header oder eine Fußzeile ein**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) hat zwei weitere Methoden, [**headerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerPicture-number-numberarray-) und [**footerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerPicture-number-numberarray-), mit denen Bilder in den Header und Footer eingefügt werden. Diese Methoden nehmen die Parameter an:

- **Abschnitt** – der Header- oder Fußzeilenabschnitt, in den das Bild platziert wird. Es gibt drei Abschnitte, links, zentriert und rechts, die jeweils durch die Werte 0, 1 und 2 dargestellt werden.
- **Byte-Array** – die grafischen Daten (die Binärdaten sollten in den Puffer eines Byte-Arrays geschrieben werden).

Nach Ausführung des folgenden Codes und Öffnen der Datei überprüfen Sie den Kopfzeilenbereich des Arbeitsblatts:

1. Wählen Sie im Menü **Datei** die Option **Seitenlayout** aus. Es wird ein Dialogfeld angezeigt.
1. Wählen Sie den Tab **Kopfzeile/Fußzeile** aus.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Image in Header/Footer Example</title>
    </head>
    <body>
        <h1>Insert Image in Header/Footer Example</h1>
        <p>Select an existing Excel file to modify (optional). If none is selected, a new workbook will be used.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select an image to insert into the header:</p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Insert Image into Header</button>
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the header.</p>';
                return;
            }

            // Read image bytes
            const imageFile = imageInput.files[0];
            const imageBuffer = await imageFile.arrayBuffer();
            const binaryData = new Uint8Array(imageBuffer);

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const excelBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(excelBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet's page setup
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Set the header picture and header scripts (converted from setters to properties)
            pageSetup.headerPicture = binaryData;
            pageSetup.header = "&G";
            pageSetup.header = "&A";

            // Save the workbook as Excel97-2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertImageInHeaderFooter_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Image inserted into header successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
