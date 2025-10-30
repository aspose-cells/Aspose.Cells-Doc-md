---
title: Einen verknüpften Bild vom Webadresse mit JavaScript via C++ einfügen
linktitle: Verknüpftes Bild aus Webadresse einfügen
type: docs
weight: 450
url: /de/javascript-cpp/insert-a-linked-picture-from-web-address/
description: Erfahren Sie, wie Sie mithilfe von Aspose.Cells for JavaScript via C++ ein verknüpftes Bild von einer Webadresse in ein Arbeitsblatt einfügen.
---

{{% alert color="primary" %}}
Manchmal müssen Sie ein Bild aus dem Web (http://) in ein Arbeitsblatt einfügen. Geben Sie dazu die URL des Bildes an, und jedes Mal, wenn die Tabelle in Excel geöffnet wird, wird das Bild heruntergeladen. Das Bild ist nicht physisch in das Excel-Dokument eingebettet, sondern verweist auf eine Webressource.
{{% /alert %}}

## **Verwendung von Microsoft Excel**

In Microsoft Excel (zum Beispiel 2007):

1. Klicken Sie auf das **Einfügen** Menü und wählen Sie **Bild** aus.  
1. Geben Sie die Webadresse für das Bild im Dialogfeld Bild einfügen an.

## **Mit Aspose.Cells for JavaScript via C++ verwenden**

Aspose.Cells for JavaScript via C++ unterstützt das Hinzufügen eines verknüpften Bildes mit [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). Die Methode gibt ein [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture)-Objekt zurück.

Das folgende Beispiel zeigt, wie man ein verknüpftes Bild von einer Webadresse in ein Arbeitsblatt einfügt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Insert Linked Picture Example</h1>
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

            if (fileInput.files.length) {
                // If file provided, use it as the base workbook
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Otherwise create a new workbook
                var workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Insert a linked picture (from Web Address) to B2 Cell.
            const pic = worksheet.shapes.addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");

            // Set the height and width of the inserted image.
            pic.heightInch = 1.04;
            pic.widthInch = 2.6;

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outLinkedPicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Linked picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
