---
title: 使用 Aspose.Cells for JavaScript 通过 C++ 修改现有的SQL数据连接
linktitle: 使用Aspose.Cells修改现有的SQL数据连接
type: docs
weight: 20
url: /zh/javascript-cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: 学习如何用 Aspose.Cells for JavaScript 通过 C++ 修改现有的SQL数据连接属性。
---

{{% alert color="primary" %}}
Aspose.Cells支持修改现有的SQL数据连接。本文将解释如何使用Aspose.Cells修改SQL数据连接的不同属性。  
你可以通过**数据 > 连接**菜单命令在Microsoft Excel中添加或查看数据连接。  
同样，Aspose.Cells提供了访问和修改数据连接的方法，使用Workbook.dataConnections集合。
{{% /alert %}}

## 使用Aspose.Cells修改现有的SQL数据连接

 以下示例演示了如何使用 C++ 通过 Aspose.Cells for JavaScript 修改工作簿的SQL数据连接。您可以从以下链接下载用于此代码的源Excel文件以及代码生成的输出Excel文件。

- [源Excel文件](5112357.xlsx)  
- [输出Excel文件](5112356.xlsx)  

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
