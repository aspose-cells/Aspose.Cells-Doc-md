```markdown
---
title: JavaScriptを使ってC++でカスタムXMLパーツを追加し、IDで選択します。
linktitle: カスタムXMLパーツの追加およびIDでの選択
type: docs
weight: 70
url: /ja/javascript-cpp/add-custom-xml-parts-and-select-them-by-id/
description: ExcelドキュメントにカスタムXMLパーツを追加し、IDで選択する方法をAspose.Cells for JavaScriptを使って学びます。
---

## **可能な使用シナリオ**  

カスタムXMLパーツはMicrosoft Excelドキュメント内に格納されているXMLデータで、これに扱うアプリケーションによって使用されます。現在のところ、Microsoft ExcelのUI経由で直接追加する方法はありません。ただし、VSTOやAspose.Cellsなど、さまざまな方法でプログラム的に追加できます。Aspose.Cells APIを使用してカスタムXMLパーツを追加したい場合は [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--) コレクションを使用してください。また、そのIDは [**CustomXmlPart.iD**](https://reference.aspose.com/cells/javascript-cpp/customxmlpart/#iD--) プロパティで設定できます。同様に、IDでカスタムXMLパーツを選択したい場合は [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--) コレクションを使用します。  

## **カスタムXMLパーツの追加およびIDでの選択**  

以下のサンプルコードは、まず[**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--)コレクションを使用して4つのカスタムXMLパーツを追加します。次に、そのIDを[**CustomXmlPart.iD**](https://reference.aspose.com/cells/javascript-cpp/customxmlpart/#iD--)プロパティを使って設定します。最後に、追加されたカスタムXMLパーツの一つを[**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--)コレクションを使って検索または選択します。以下のコードのコンソール出力も参考にしてください。  

## **サンプルコード**  

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

## **コンソール出力**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  
 ```
