---
title: XmlMapCollection.AddメソッドをJavaScriptとC++を使用してワークブック内にXMLマップを追加します。  
linktitle: XmlMapCollection.Addメソッドを使用してワークブックにXML Mapを追加する  
type: docs  
weight: 10  
url: /ja/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: C++のAspose.Cells for JavaScriptを使用して、ワークブック内にXMLマップを追加する方法を学びます。  
---  

## **可能な使用シナリオ**  

Aspose.CellsはXMLマップをブック内にインポートするために使用できる[**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/javascript-cpp/xmlmapcollection/#add-string-)メソッドを提供します。  

## **XmlMapCollection.Addメソッドを使用してワークブックにXML Mapを追加する**  

以下のサンプルコードは、[output excel file](5115434.xlsx)として保存される[サンプル.xml](5115433.xml)からインポートされたXMLマップをブック内に追加する[**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/javascript-cpp/xmlmapcollection/#add-string-)メソッドを使用しています。  

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
