---
title: JavaScript経由でXMLをExcelワークブックにインポート
linktitle: XMLマップ
type: docs
weight: 210
url: /ja/javascript-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: XMLファイルからExcelへのデータインポートは、Aspose.Cells for JavaScriptを使用して行います。
---

{{% alert color="primary" %}}

Aspose.Cellsは[**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-)メソッドを使用してワークブック内にXMLマップをインポートすることができます。Microsoft ExcelでXMLマップをインポートする手順は次のとおりです：

- **開発**タブを選択
- XMLセクションで**インポート**をクリックし、必要な手順に従います。

インポートを完了するためにXMLデータを提供する必要があります。テストに使用できる[サンプルXMLデータ](5115037.txt)を以下に示します。

{{% /alert %}}

## **Microsoft Excelを使用してXML Mapをインポート**

以下のスクリーンショットは、Microsoft Excelを使用してXML Mapをインポートする方法を示しています。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **C++経由のAspose.Cells for JavaScriptを使用したXMLマップのインポート**

次のサンプルコードは、[**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-)の使用法を示しています。このスクリーンショットに示すように、[出力Excelファイル](5115036.xlsx)が生成されます。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Import XML</title>
    </head>
    <body>
        <h1>Import XML into Workbook Example</h1>
        <input type="file" id="xmlInput" accept=".xml,.txt" />
        <button id="runExample">Import XML and Save</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const fileInput = document.getElementById('xmlInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const xmlText = await file.text();

            // Create a workbook
            const workbook = new Workbook();

            // Import your XML Map data starting from cell A1 on Sheet1
            workbook.importXml(xmlText, "Sheet1", 0, 0);

            // Save workbook to XLSX and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">XML imported and workbook saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [XmlMapCollection.add()メソッドを使用してワークブック内にXMLマップを追加する](/cells/ja/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [ブック内のXMLマップにリンクされたXMLデータをエクスポート](/cells/ja/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [XMLマップのルート要素名を検出する](/cells/ja/javascript-cpp/find-the-root-element-name-of-xml-map/)
- [セルをXMLマップ要素にリンクする](/cells/ja/javascript-cpp/link-cells-to-xml-map-elements/)
