---
title: C++経由のJavaScriptでブックに隠れた外部リンクが含まれているかどうかを確認する
linktitle: ワークブックに非表示の外部リンクが含まれているかどうかを確認
type: docs
weight: 230
url: /ja/javascript-cpp/check-if-workbook-contains-hidden-external-links/
description: C++経由のAspose.Cells for JavaScriptを使用して、ブックに隠された外部リンクが存在するかどうかを確認する方法を学びます。
---

## **可能な使用シナリオ**  
時々、ブックにはMicrosoft Excelでは表示できない隠された外部リンクが含まれています。Aspose.Cellsは外部リンクを可視・非可視に関係なくすべて取得します。ただし、[ExternalLink.isVisible()](https://reference.aspose.com/cells/javascript-cpp/externallink/#isVisible--) プロパティを使用して外部リンクが表示されているかどうかを確認できます。

## **ワークブックに非表示の外部リンクが含まれる [ソースExcelファイル](5115413.xlsx) をロードする以下のサンプルコードでは、Microsoft Excelで表示されない非表示の外部リンクが含まれています。 [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) および [ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) プロパティを出力した後、[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) プロパティを出力します。以下のコンソール出力では、すべての外部リンクが非表示であることがわかります。**  
次のサンプルコードは、隠された外部リンクを含む[ソースExcelファイル](5115413.xlsx)を読み込みます。これらのリンクはMicrosoft Excelでは表示できませんが、ワークブック内には存在しています。 [ExternalLink.dataSource](https://reference.aspose.com/cells/javascript-cpp/externallink/#dataSource--)と[ExternalLink.isReferred()](https://reference.aspose.com/cells/javascript-cpp/externallink/#isReferred--)プロパティを出力した後に、[ExternalLink.isVisible()](https://reference.aspose.com/cells/javascript-cpp/externallink/#isVisible--)プロパティも出力されます。以下のコンソール出力では、すべての外部リンクが非表示になっていることがわかります。

### **サンプルコード**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - External Links</title>
    </head>
    <body>
        <h1>External Links Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result" style="white-space: pre-wrap; margin-top: 1em;"></div>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the external link collection of the workbook
            const links = workbook.worksheets.externalLinks;

            // Print all the external links and check their IsVisible property
            let output = '';
            for (let i = 0; i < links.count; i++) {
                const link = links.get(i);
                output += "Data Source: " + link.dataSource + "\n";
                output += "Is Referred: " + link.isReferred + "\n";
                output += "Is Visible: " + link.isVisible + "\n\n";

                console.log("Data Source: " + link.dataSource);
                console.log("Is Referred: " + link.isReferred);
                console.log("Is Visible: " + link.isVisible);
                console.log();
            }

            document.getElementById('result').textContent = output || 'No external links found.';
        });
    </script>
</html>
```  

### **コンソール出力**  


{{< highlight java >}}  
 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls  

Is Referred: True  

Is Visible: False  
{{< /highlight >}}
