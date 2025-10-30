---
title: Benutzerdefinierte XML Teile in Aspose.Cells mit JavaScript über C++ verwenden
linktitle: Verwenden von benutzerdefinierten XML Teilen in Aspose.Cells
type: docs
weight: 390
url: /de/javascript-cpp/use-custom-xml-parts-in-aspose-cells/
description: Erfahren Sie, wie Sie benutzerdefinierte XML Teile in Aspose.Cells for JavaScript über C++ verwenden. Integrieren Sie externe XML Daten nahtlos in Excel Dateien.
---

## Verwendung von benutzerdefinierten XML-Teilen in Aspose.Cells

Benutzerdefinierte XML-Teile sind XML-Daten, die von verschiedenen Anwendungen wie SharePoint usw. innerhalb der Excel-Datei gespeichert werden. Diese Daten werden von Anwendungen genutzt, die sie benötigen. Microsoft Excel verwendet diese Daten nicht, daher gibt es keine GUI, um sie hinzuzufügen. Sie können diese Daten anzeigen, indem Sie die Erweiterung **.xlsx** in **.zip** ändern und diese dann mit **WinZip** öffnen. Sie können die ZIP-Datei auch mit jedem Drittanbieter-Windows-Zip-Programm wie WinRAR oder WinZip öffnen. Die Daten befinden sich im **customXml**-Ordner.

Sie können benutzerdefinierte XML-Teile mit Aspose.Cells for JavaScript über C++ durch die [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/)-Methode hinzufügen.

Der folgende Beispielcode nutzt die [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) Methode und fügt den **Book Catalog XML** mit dem Namen **BookStore** hinzu. Das folgende Bild zeigt das Ergebnis dieses Codes. Wie Sie sehen können, wird der Book Catalog XML innerhalb des BookStore-Knotens hinzugefügt, der der Name dieser Eigenschaft ist.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## JavaScript-Code zur Verwendung benutzerdefinierter XML-Teile

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Custom XML to Workbook Example</h1>
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

        const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create an instance of Workbook class
            const workbook = new Workbook();

            // Add Custom XML Part to ContentTypePropertyCollection
            workbook.contentTypeProperties.add("BookStore", booksXML);

            // Save the resultant spreadsheet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom XML added and file prepared. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## Verwandter Artikel

- [Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind](/cells/de/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
