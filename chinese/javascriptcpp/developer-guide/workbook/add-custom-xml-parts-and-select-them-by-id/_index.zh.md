```markdown
---
title: 添加自定义XML部分并通过ID用JavaScript在C++中选择
linktitle: 添加自定义XML部件并按ID选择
type: docs
weight: 70
url: /zh/javascript-cpp/add-custom-xml-parts-and-select-them-by-id/
description: 学习如何向Excel文档添加自定义XML部分，并使用Aspose.Cells for JavaScript通过C++按ID选择它们。
---

## **可能的使用场景**  

 自定义XML部分是存储在Microsoft Excel文档内的XML数据，供处理该数据的应用使用。当前尚无直接通过Microsoft Excel UI添加的方法，但可以通过编程以各种方式添加，例如使用VSTO、Aspose.Cells等。请使用[**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--)集合通过Aspose.Cells API添加自定义XML部分，也可通过[**CustomXmlPart.iD**](https://reference.aspose.com/cells/javascript-cpp/customxmlpart/#iD--)属性设置其ID。同样，若要按ID选择自定义XML部分，可以使用[**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--)集合。  

## **添加自定义XML部件并按ID选择**  

以下示例代码首先通过[**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--)集合添加了四个自定义XML部分，然后使用[**CustomXmlPart.iD**](https://reference.aspose.com/cells/javascript-cpp/customxmlpart/#iD--)属性设置它们的ID，最后使用[**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--)集合查找或选择其中一个添加的自定义XML部分。请参考下面的控制台输出。  

## **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add and Select Custom XML Parts Example</title>
    </head>
    <body>
        <h1>Add and Select Custom XML Parts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Some data in the form of byte array.
            // Please use correct XML and Schema instead.
            const btsData = new Uint8Array([1, 2, 3]);
            const btsSchema = new Uint8Array([1, 2, 3]);

            // Create four custom xml parts.
            wb.customXmlParts.add(btsData, btsSchema);
            wb.customXmlParts.add(btsData, btsSchema);
            wb.customXmlParts.add(btsData, btsSchema);
            wb.customXmlParts.add(btsData, btsSchema);

            // Assign ids to custom xml parts.
            wb.customXmlParts.get(0).id = "Fruit";
            wb.customXmlParts.get(1).id = "Color";
            wb.customXmlParts.get(2).id = "Sport";
            wb.customXmlParts.get(3).id = "Shape";

            // Specify search custom xml part id.
            let srchID = "Fruit";
            srchID = "Color";
            srchID = "Sport";

            // Search custom xml part by the search id.
            const cxp = wb.customXmlParts.selectByID(srchID);

            // Print the found or not found message on console and UI.
            if (cxp.isNull()) {
                console.log(`Not Found: CustomXmlPart ID ${srchID}`);
                document.getElementById('result').innerHTML = `<p style="color: red;">Not Found: CustomXmlPart ID ${srchID}</p>`;
            } else {
                console.log(`Found: CustomXmlPart ID ${srchID}`);
                document.getElementById('result').innerHTML = `<p style="color: green;">Found: CustomXmlPart ID ${srchID}</p>`;
            }

            // Save the modified workbook and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            console.log("AddCustomXMLPartsAndSelectThemByID executed successfully.");
        });
    </script>
</html>
```  

## **控制台输出**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  
 ```
