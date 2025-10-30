---
title: JavaScript kullanarak C++ ile TextBox Yönetimi
linktitle: Metin Kutusunu Yönet
type: docs
weight: 50
url: /tr/javascript-cpp/managing-textbox-of-excel/
description: C++ ile Aspose.Cells for JavaScript kullanarak Excel de TextBox yönetmeyi öğrenin. 
keywords: Excel de TextBox Yönetimi JavaScript C++ ile
---

## **Olası Kullanım Senaryoları**
Bazı durumlarda, bir Excel çalışma sayfasındaki TextBox nesnelerini eklemek, güncellemek veya manipüle etmek gerekebilir. Bu, açıklamalar, yönlendirme metinleri veya veri sunumuna yardımcı olacak herhangi bir ek bilgi eklemek için faydalı olabilir. C++ ile Aspose.Cells for JavaScript, Excel belgelerinde TextBox'u yönetmek için sağlam işlevsellik sağlar. 

## **Aspose.Cells for JavaScript kullanarak TextBox Yönetimi C++ ile**
Bu örnek aşağıdakileri göstermektedir:

1. Yeni bir çalışma kitabı oluşturun.
2. Bir TextBox şekli ekleyin.
3. Gerektiğinde TextBox özelliklerini değiştirin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox Example</title>
    </head>
    <body>
        <h1>TextBox Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding a TextBox shape
            const textBox = worksheet.shapes.addTextBox(2, 2, 100, 100);

            // Set TextBox properties (converted getters/setters to properties)
            textBox.text = "This is a TextBox.";
            textBox.fontSize = 12;
            textBox.fillColor = Color.fromArgb(255, 255, 255); // White background

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'TextBoxExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Bu kod, Excel çalışma sayfasında bir TextBox oluşturma ve yapılandırma yöntemini gösterir, boyutunu, konumunu ayarlamayı ve gereksinimlerinize göre biçimlendirmeyi gösterir.

Metin kutuları ile etkileşimlerin belirli kullanım durumlarına göre değişebileceğini unutmayın, bu yüzden ek yöntemler ve özellikler için C++ ile Aspose.Cells for JavaScript dokümantasyonuna başvurun.
