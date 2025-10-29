---
title: 用JavaScript通过C++设置内置文档属性的ScaleCrop和LinksUpToDate属性
linktitle: 设置内置文档属性的ScaleCrop和LinksUpToDate属性
type: docs
weight: 320
url: /zh/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: 学习如何使用Aspose.Cells for JavaScript通过C++设置内置文档属性的ScaleCrop和LinksUpToDate属性。
---

## **可能的使用场景**
[内置文档属性集合.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) 和 [内置文档属性集合.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) 是在OpenXml格式内部定义的两个扩展内置文档属性。 这些属性的目的如下。

## **1) ScaleCrop**
此元素指示文档缩略图的显示模式。将此元素设置为**TRUE**以启用文档缩略图的缩放以进行显示。将此元素设置为**FALSE**以启用文档缩略图的裁剪，以仅显示适合显示器的部分。

此元素的可能值由W3C XML Schema布尔数据类型定义。

## **2) LinksUpToDate**
此元素指示文档中的超链接是否为最新状态。将此元素设置为**TRUE**表示超链接已更新。将此元素设置为**FALSE**表示超链接已过时。

此元素的可能值由W3C XML Schema布尔数据类型定义。

## **截图显示了app.xml文件中的这些属性**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **设置内置文档属性的ScaleCrop和LinksUpToDate属性**
以下示例代码设置工作簿的[内置文档属性集合.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--)和[内置文档属性集合.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--)扩展内置文档属性。请查看用此代码生成的[输出Excel文件](5115500.xlsx)，将其扩展名更改为.zip，解压内容，并查看截图中的app.xml。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set BuiltIn Document Properties</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Accessing BuiltIn Document Properties and setting properties
            const builtInDocumentProperties = workbook.builtInDocumentProperties;
            // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
            builtInDocumentProperties.scaleCrop = true;
            builtInDocumentProperties.linksUpToDate = true;

            // Saving the Excel file.
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
