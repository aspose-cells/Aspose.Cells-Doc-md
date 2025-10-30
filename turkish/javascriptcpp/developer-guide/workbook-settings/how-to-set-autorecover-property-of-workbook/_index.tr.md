---
title: JavaScript ve C++ kullanarak Çalışma Kitabının Otomatik Kurtarma özelliğini nasıl ayarlayacağınızı öğrenin.
linktitle: Çalışma Kitabının Otomatik Kurtarma Özelliğini Ayarlamak
type: docs
weight: 220
url: /tr/javascript-cpp/how-to-set-autorecover-property-of-workbook/
description: C++ ve Aspose.Cells for JavaScript kullanarak çalışma kitabının Otomatik Kurtarma özelliğini nasıl ayarlayacağınızı öğrenin.
---

{{% alert color="primary" %}}  
Aspose.Cells kullanarak Çalışma Kitabı'nın Otomatik Kurtarma özelliğini ayarlayabilirsiniz. Bu özelliğin varsayılan değeri **true**'dur. Bir çalışma kitabında bunu **false** olarak ayarladığınızda, Microsoft Excel Otomatik Kurtarma (Otomatik Kaydet) devre dışı kalır.  

Aspose.Cells, bu seçeneği etkinleştirmek veya devre dışı bırakmak için [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) özelliğini sağlar.  
{{% /alert %}}  

Aşağıdaki kod, çalışma kitabının [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) özelliğinin nasıl kullanılacağını açıklar. Kod önce bu özelliğin varsayılan değeri olan **true**'yu okur, sonra bunu **false** yapar ve çalışma kitabını kaydeder. Ardından tekrar okur ve bu özelliğin değerinin şu anda **false** olduğunu gösterir.  

## Çalışma Kitabının Otomatik Kurtarma Özelliğini JavaScript ile Ayarlama  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoRecover</title>
    </head>
    <body>
        <h1>AutoRecover Property Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            // Create workbook object
            const workbook = new Workbook();

            // Read AutoRecover property
            const autoRecoverBefore = workbook.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover before: ${autoRecoverBefore}</p>`;

            // Set AutoRecover property to false
            workbook.settings.autoRecover = false;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download output_out.xlsx';

            // Read the saved workbook again from the saved data
            const workbook2 = new Workbook(new Uint8Array(outputData));

            // Read AutoRecover property
            const autoRecoverAfter = workbook2.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover after reload: ${autoRecoverAfter}</p>`;
        });
    </script>
</html>
```  

## **Çıktı**  



{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}
