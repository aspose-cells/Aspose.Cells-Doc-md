---
title: Stil Nesnelerini Yeniden Kullanma
linktitle: Stil Nesnelerini Yeniden Kullanma
description: C++ kullanarak, yeniden kullanılabilir stil nesneleri oluşturarak ve kullanarak stil yönetimini basitleştirebilir ve kod verimliliğini artırabilirsiniz. Reusable stil nesnelerinin avantajlarından nasıl yararlanacağınızı ve bunları uygulamanıza nasıl entegre edeceğinizi rehberimizde bulabilirsiniz.
keywords: Aspose.Cells for JavaScript kullanarak C++, Stilleri yeniden kullanma, Stil yönetimi, Kod verimliliği, Yeniden kullanılabilir stiller, Uygulama geliştirme, API referansı, Örnek kod, İndirme, Destek.
type: docs
weight: 3000
url: /tr/javascript-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}  
Stil nesnelerini yeniden kullanmak, belleği boşaltabilir ve programı daha hızlı hale getirebilir.  
{{% /alert %}}  

Bir çalışsayfadaki geniş bir hücre aralığına bazı biçimlendirme uygulamak için:

1. Bir stil nesnesi oluşturun.
1. Öznitelikleri belirtin.
1. Stili aralıktaki hücrelere uygulayın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Font</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            // Creating a new workbook (empty)
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            const styleObject = workbook.createStyle();
            styleObject.font.color = Color.Red;
            styleObject.font.name = "Times New Roman";
            cell1.style = styleObject;
            cell2.style = styleObject;

            // Put the values inside the cell
            cell1.value = "Hello World!";
            cell2.value = "Hello World!!";

            // Save to XLSX
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleOutput_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}  
Çünkü [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) / [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) yaklaşımı daha az bellek kullanır ve daha verimlidir, eski Cell.style özelliği gereksiz yere çok bellek kullanması nedeniyle Aspose.Cells 7.1.0 sürümüyle kaldırılmıştır.  
{{% /alert %}}
