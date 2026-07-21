---
title: 获取数据透视表刷新日期和刷新者信息
type: docs
weight: 100
url: /zh/javascript-cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: 如何用Aspose.Cells for JavaScript通过C++获取数据透视表的刷新日期及由谁刷新信息。
keywords: 使用Aspose.Cells for JavaScript Excel、Excel JavaScript库，通过C++获取数据透视表的刷新日期及由谁刷新。
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript通过C++现支持从工作簿中获取刷新日期和由谁刷新信息。

{{% /alert %}}

## **如何获取数据透视表的刷新日期和刷新人信息**
[**PivotTable.refreshDate**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshDate--)返回上次刷新数据透视表报告的日期。类似地，[**PivotTable.refreshedByWho**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshedByWho--)属性返回上次刷新报告的用户姓名。以下示例演示此功能，示例文件可从以下链接下载。

[SourcePivotTable.xlsx](77496335.xlsx)

**示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Info</title>
    </head>
    <body>
        <h1>Pivot Table Information</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            const pivotTable = worksheet.pivotTables.get(0);

            const refreshedByWho = pivotTable.refreshedByWho;
            const refreshDate = pivotTable.refreshDate;

            console.log("Pivot table refresh by who = " + refreshedByWho);
            console.log("Pivot table refresh date = " + refreshDate);

            document.getElementById('result').innerHTML = `
                <p>Pivot table refresh by who = ${refreshedByWho}</p>
                <p>Pivot table refresh date = ${refreshDate}</p>
            `;
        });
    </script>
</html>
```
