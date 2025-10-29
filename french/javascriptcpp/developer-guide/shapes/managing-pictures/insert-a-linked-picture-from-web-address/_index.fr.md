---
title: Insérer une image liée à partir d une adresse Web avec JavaScript via C++
linktitle: Insérer une image liée à partir de l adresse Web
type: docs
weight: 450
url: /fr/javascript-cpp/insert-a-linked-picture-from-web-address/
description: Découvrez comment insérer une image liée à partir d une adresse Web dans une feuille de calcul en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
Parfois, vous devez insérer une image provenant du web (http://) dans une feuille de calcul. Pour ce faire, spécifiez l'URL de l'image et l'image sera téléchargée à chaque ouverture du classeur dans Excel. L'image n'est pas physiquement intégrée dans le document Excel, mais pointe vers une ressource web.
{{% /alert %}}

## **Utilisation de Microsoft Excel**

Dans Microsoft Excel (par exemple 2007) :

1. Cliquez sur le menu **Insérer** et sélectionnez **Image**.  
1. Spécifiez l'adresse web de l'image dans la boîte de dialogue Insérer une image.

## ** Utilisation de Aspose.Cells for JavaScript via C++**

Aspose.Cells for JavaScript via C++ prend en charge l'ajout d'une image liée en utilisant [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). La méthode retourne un objet [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture).

L'exemple suivant montre comment ajouter une image liée depuis une adresse web dans une feuille de calcul.

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
