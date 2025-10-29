---
title: 使用 C++ 通过JavaScript检查工作簿是否包含隐藏的外部链接
linktitle: 检查工作簿是否包含隐藏的外部链接
type: docs
weight: 230
url: /zh/javascript-cpp/check-if-workbook-contains-hidden-external-links/
description: 学习如何使用 C++ 通过 Aspose.Cells for JavaScript 检查工作簿是否包含隐藏的外部链接。
---

## **可能的使用场景**  
有时候，工作簿中包含隐藏且在Microsoft Excel中无法查看的外部链接。Aspose.Cells可以检索所有外部链接，无论它们是否可见。然而，您可以使用 [ExternalLink.isVisible()](https://reference.aspose.com/cells/javascript-cpp/externallink/#isVisible--) 属性来检查外部链接是否可见。

## **检查工作簿是否包含隐藏的外部链接**  
以下示例代码加载包含隐藏外部链接的 [源Excel文件](5115413.xlsx)。这些链接不能在Microsoft Excel中查看，但存在于工作簿中。在打印 [ExternalLink.dataSource](https://reference.aspose.com/cells/javascript-cpp/externallink/#dataSource--) 和 [ExternalLink.isReferred()](https://reference.aspose.com/cells/javascript-cpp/externallink/#isReferred--) 属性后，它会输出 [ExternalLink.isVisible()](https://reference.aspose.com/cells/javascript-cpp/externallink/#isVisible--) 属性。在下面的控制台输出中，您可以看到所有外部链接都不可见。

### **示例代码**  
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

### **控制台输出**  


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
