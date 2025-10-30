---
title: Aspose.CellsでカスタムXMLパーツをJavaScript経由でC++で使用する
linktitle: Aspose.Cells でカスタムXMLパーツを使用する
type: docs
weight: 390
url: /ja/javascript-cpp/use-custom-xml-parts-in-aspose-cells/
description: C++経由でAspose.Cells for JavaScriptを使用してカスタムXMLパーツの使用方法を学習します。Excelファイルに外部XMLデータをシームレスに統合します。
---

## Aspose.Cells でカスタムXMLパーツを使用する

カスタムXMLパーツは、SharePointなどの異なるアプリケーションによってExcelファイルに保存されるXMLデータです。このデータはそれを必要とするさまざまなアプリケーションによって使用されます。Microsoft Excelはこのデータを利用しないためGUIから追加できません。このデータは、**.xlsx** の拡張子を **.zip** に変更し、その後 **WinZip** で開くことで閲覧可能です。また、WinRARやWinZipなどのサードパーティのWindows圧縮ユーティリティを使ってZIPファイルを開くこともできます。データは**customXml**フォルダ内に存在します。

 [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/)メソッドを使用してC++経由でAspose.Cells for JavaScriptを使ってカスタムXMLパーツを追加できます。

次のサンプルコードは、[**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) メソッドを使用し、**Book Store** という名前の **Book Catalog XML** を追加する例を示しています。以下の画像は、このコードの結果を示しています。ご覧の通り、Book Catalog XMLは、このプロパティの名前であるBookStoreノード内に追加されています。

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## カスタムXMLパーツを使用するJavaScriptコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Custom XML to Workbook Example</h1>
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

        const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create an instance of Workbook class
            const workbook = new Workbook();

            // Add Custom XML Part to ContentTypePropertyCollection
            workbook.contentTypeProperties.add("BookStore", booksXML);

            // Save the resultant spreadsheet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom XML added and file prepared. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## 関連記事

- [ドキュメント情報パネルで表示されるカスタムプロパティの追加](/cells/ja/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
