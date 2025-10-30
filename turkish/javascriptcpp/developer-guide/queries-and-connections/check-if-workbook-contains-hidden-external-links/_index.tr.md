---
title: JavaScript kullanarak C++ ile Çalışma kitabının gizli harici bağlantılar içerip içermediğini kontrol edin
linktitle: Çalışma Kitabı gizli Harici Bağlantıları içeriyorsa kontrol edin
type: docs
weight: 230
url: /tr/javascript-cpp/check-if-workbook-contains-hidden-external-links/
description: C++ kullanarak Aspose.Cells for JavaScript ile bir çalışma kitabında gizli harici bağlantıların olup olmadığını nasıl kontrol edeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**  
Bazen, çalışma kitabında gizli ve Microsoft Excel'de görüntülemeyen harici bağlantılar bulunur. Aspose.Cells tüm harici bağlantıları, görünür veya gizli olmalarına bakmadan alır. Ancak, harici bağlantının görünür olup olmadığını kontrol etmek için [ExternalLink.isVisible()](https://reference.aspose.com/cells/javascript-cpp/externallink/#isVisible--) özelliğini kullanabilirsiniz.

## **Çalışma Kitabı gizli Harici Bağlantıları içeriyorsa kontrol edin**  
Aşağıdaki örnek kod, gizli harici bağlantılar içeren [kaynak excel dosyasını](5115413.xlsx) yükler. Bu bağlantılar Microsoft Excel'de görüntülenemez, ancak çalışma kitabında bulunurlar. [ExternalLink.dataSource](https://reference.aspose.com/cells/javascript-cpp/externallink/#dataSource--) ve [ExternalLink.isReferred()](https://reference.aspose.com/cells/javascript-cpp/externallink/#isReferred--) özellikleri yazdırıldıktan sonra, [ExternalLink.isVisible()](https://reference.aspose.com/cells/javascript-cpp/externallink/#isVisible--) özelliği gösterilir. Aşağıdaki konsol çıktısında, tüm harici bağlantılarının görünmediği görülür.

### **Örnek Kod**  
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

### **Konsol Çıktısı**  


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
