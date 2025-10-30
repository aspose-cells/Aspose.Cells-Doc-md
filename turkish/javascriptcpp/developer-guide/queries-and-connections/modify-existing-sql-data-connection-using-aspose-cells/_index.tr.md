---
title: Mevcut SQL Veri Bağlantısını Aspose.Cells for JavaScript kullanarak C++ ile değiştirin
linktitle: Mevcut SQL Veri Bağlantısını Değiştirme Aspose.Cells ile
type: docs
weight: 20
url: /tr/javascript-cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Mevcut SQL Veri Bağlantısı özelliklerini Aspose.Cells for JavaScript kullanarak C++ ile nasıl değiştireceğinizi öğrenin.
---

{{% alert color="primary" %}}
Aspose.Cells, mevcut SQL Veri Bağlantısını değiştirme işlemini destekler. Bu makale, Aspose.Cells'ı kullanarak SQL Veri Bağlantısının farklı özelliklerini değiştirmeyi açıklamaktadır.  
Microsoft Excel içinde Veri > Bağlantılar menü komutunu kullanarak Veri Bağlantılarını ekleyebilir veya görüntüleyebilirsiniz.  
Benzer şekilde, Aspose.Cells çalışma kitabı.dataConnections koleksiyonunu kullanarak Veri Bağlantılarına erişim ve değiştirme sağlar.
{{% /alert %}}

## Aspose.Cells ile Mevcut SQL Veri Bağlantısını Değiştirme

Aşağıdaki örnek, çalışma kitabının SQL Veri Bağlantısını değiştirmek için C++ üzerinden Aspose.Cells for JavaScript kullanımını gösterir. Bu kodda kullanılan orijinal Excel dosyasını ve kod tarafından oluşturulan çıktı Excel dosyasını aşağıdaki bağlantılardan indirebilirsiniz.

- [Kaynak Excel Dosyası](5112357.xlsx)  
- [Çıktı Excel Dosyası](5112356.xlsx)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Data Connection Example</title>
    </head>
    <body>
        <h1>Data Connection Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first Data Connection
            const conn = workbook.dataConnections.get(0);

            // Change the Data Connection Name and Odc file
            conn.name = "MyConnectionName";
            conn.odcFile = "C:\\Users\\MyDefaulConnection.odc";

            // Change the Command Type, Command and Connection String
            const dbConn = conn;
            dbConn.commandType = AsposeCells.OLEDBCommandType.SqlStatement;
            dbConn.command = "Select * from AdminTable";
            dbConn.connectionString = "Server=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Trusted_Connection=False";

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Data connection updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
