---
title: JavaScript kullanarak Web Adresinden Bağlantılı Resim Ekleme C++ ile
linktitle: Web Adresinden Bağlantılı Bir Resim Eklemek
type: docs
weight: 450
url: /tr/javascript-cpp/insert-a-linked-picture-from-web-address/
description: Aspose.Cells for JavaScript kullanarak web adresinden bağlantılı resmi bir çalışma sayfasına nasıl ekleyeceğinizi öğrenin.
---

{{% alert color="primary" %}}
Bazen, bir çalışma sayfasına web'den (http://) bir resim eklemeniz gerekir. Bunun için, resmin URL'sini belirtin ve çalışma sayfası her açıldığında resmi indirir. Resim, Excel dokümanına fiziksel olarak gömülü değildir, ancak bir web kaynağına işaret eder.
{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de (örneğin 2007):

1. **Ekle** menüsünü tıklayın ve **Resim**'i seçin.  
1. Resim Ekle iletişim kutusunda resmin web adresini belirtin.

## ** C++ ile Aspose.Cells for JavaScript Kullanımı**

 Aspose.Cells for JavaScript C++ ile [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-) kullanarak bağlantılı resim eklemeyi destekler. Yöntem bir [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture) nesnesi döner.

Aşağıdaki örnek, bir web adresinden bağlı bir resmi çalışma sayfasına nasıl ekleyeceğinizi gösterir.

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
