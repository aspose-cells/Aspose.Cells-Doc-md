---
title: 通过JavaScript与C++查找XML映射的根元素名称
linktitle: 查找 XML 地图的根元素名称
type: docs
weight: 30
url: /zh/javascript-cpp/find-the-root-element-name-of-xml-map/
description: 学习如何使用C++的Aspose.Cells for JavaScript在Excel中查找XML映射的根元素名称。
---

## **可能的使用场景**

您可以使用C++的Aspose.Cells for JavaScript的[**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--)属性查询XML映射的*根元素名称*。以下截图显示了Microsoft Excel中XML映射的根元素名称。

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **示例代码**

以下示例代码加载[示例 Excel 文件](55541789.xlsx)，访问第一个 XML 映射并打印其 [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--) 属性。请查看下面提供的控制台输出。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Root Element Name Of Xml Map</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Get Root Element Name</button>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first Xml Map inside the Workbook
            const xmap = workbook.worksheets.xmlMaps.get(0);

            // Get Root Element Name of Xml Map
            const rootName = xmap.rootElementName;

            // Display result
            resultDiv.innerHTML = `<p>Root Element Name Of Xml Map: ${rootName}</p>`;
            console.log("Root Element Name Of Xml Map: " + rootName);
        });
    </script>
</html>
```

## **控制台输出**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
