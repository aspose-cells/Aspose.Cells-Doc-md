---
title: JavaScriptをC++経由で、ドキュメント情報パネル内に表示されるカスタムプロパティを追加します。
linktitle: 文書情報パネル内で表示されるカスタムプロパティを追加する
type: docs
weight: 300
url: /ja/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Aspose.Cells for JavaScriptをC++で使用して、Workbookオブジェクトにカスタムプロパティを追加する方法を学びます。これらのプロパティはドキュメント情報パネルで表示されます。
---

## **ドキュメント情報パネルで表示されるカスタムプロパティの追加**

 Aspose.Cells for JavaScriptをC++で使用して、Workbook内にカスタムプロパティを追加し、ドキュメント情報パネル内に表示させることができます。Microsoft Excelでは、[ファイル] > [情報] > [プロパティ] > [ドキュメントパネルの表示]のメニューコマンドを使用してドキュメント情報パネルを開くことができます。

[**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/#add-string-string-)メソッドを使用して、ドキュメント情報パネルに表示されるカスタムプロパティを追加してください。

次のサンプルコードは、2つのカスタムプロパティを追加します。最初のプロパティにはタイプがなく、2つ目のプロパティにはDateTimeタイプがあります。このコードで生成されたExcelファイルを開くと、これらの2つのプロパティがドキュメント情報パネル内に表示されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook with Custom Properties</button>
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
            // Create workbook object
            const workbook = new Workbook();

            // Add simple property without any type
            workbook.contentTypeProperties.add("MK31", "Simple Data");

            // Add date time property with type
            workbook.contentTypeProperties.add("MK32", "04-Mar-2015", "DateTime");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingCustomPropertiesVisible_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **関連記事**

{{% alert color="primary" %}}

- [Aspose.CellsでカスタムXMLパーツを使用する](/cells/ja/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
