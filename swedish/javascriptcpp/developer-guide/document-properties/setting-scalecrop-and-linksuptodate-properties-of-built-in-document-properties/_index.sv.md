---
title: Ställa in ScaleCrop och LinksUpToDate egenskaper i inbyggda dokumentegenskaper med JavaScript via C++
linktitle: Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper
type: docs
weight: 320
url: /sv/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Lär dig hur du ställer in ScaleCrop och LinksUpToDate egenskaper i inbyggda dokumentegenskaper med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**
[BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) och [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) är två utökade inbyggda dokumentegenskaper definierade inom OpenXml-formatet. Syftet med dessa egenskaper är följande.

## **1) ScaleCrop**
Detta element indikerar visningsläget för miniatyrbilden av dokumentet. Ange detta element till **TRUE** för att aktivera skalning av miniatyrbilden av dokumentet. Ange detta element till **FALSE** för att aktivera urskärning av miniatyrbilden för att visa endast sektioner som passar i displayen.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.

## **2) LinksUpToDate**
Detta element indikerar om hyperlänkar i ett dokument är uppdaterade. Ange detta element till **TRUE** för att ange att hyperlänkar är uppdaterade. Ange detta element till **FALSE** för att ange att hyperlänkar är föråldrade.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.

## **Skärmbild som visar dessa egenskaper i app.xml-filen**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper**
Följande exempel kod ställer in de utökade inbyggda dokumentegenskaperna [BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) och [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) för arbetsboken. Kontrollera det genererade [utdataexcelfilen](5115500.xlsx) med denna kod, byt ut dess filändelse till .zip och extrahera dess innehåll samt visa app.xml som visas i skärmdumpen ovan.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set BuiltIn Document Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            const fileInput = document.getElementById('fileInput');

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Accessing BuiltIn Document Properties and setting properties
            const builtInDocumentProperties = workbook.builtInDocumentProperties;
            // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
            builtInDocumentProperties.scaleCrop = true;
            builtInDocumentProperties.linksUpToDate = true;

            // Saving the Excel file.
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
