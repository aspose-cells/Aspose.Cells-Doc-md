---
title: 使用C++的XmlMapCollection.Add方法在工作簿中添加XML映射，配合JavaScript实现  
linktitle: 使用XmlMapCollection.Add方法在工作簿中添加XML映射  
type: docs  
weight: 10  
url: /zh/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: 学习如何在工作簿中使用C++的Aspose.Cells for JavaScript的XmlMapCollection.Add方法添加XML映射。  
---  

## **可能的使用场景**  

Aspose.Cells 提供了 [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/javascript-cpp/xmlmapcollection/#add-string-) 方法，您可以使用该方法将 XML 映射导入工作簿。  

## **使用XmlMapCollection.Add方法在工作簿中添加XML映射**  

以下示例代码使用 [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/javascript-cpp/xmlmapcollection/#add-string-) 方法向工作簿中添加 XML 映射，并将其保存为 [输出 Excel 文件](5115434.xlsx)。屏幕截图显示了已从 [sample.xml](5115433.xml) 中导入的 XML 映射。  

![add-xml-map](add-xml-map.png)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add XML Map to Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xml" />
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const xmlString = new TextDecoder().decode(arrayBuffer);

            // Create workbook object
            const wb = new Workbook();

            // Add xml map found inside the uploaded sample.xml into the workbook
            // Note: converted getter/setter usage to property access per universal conversion rules
            wb.worksheets.xmlMaps.add(xmlString);

            // Save the workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">XML map added and workbook saved. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
