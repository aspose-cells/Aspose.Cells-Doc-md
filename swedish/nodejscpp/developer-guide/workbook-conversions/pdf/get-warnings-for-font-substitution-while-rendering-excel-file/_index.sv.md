---  
title: Få varningar för font substitution vid rendering av Excel fil med Node.js via C++  
linktitle: Få varningar för teckensnittsersättning vid rendering av Excel fil  
type: docs  
weight: 230  
url: /sv/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/  
description: Lär dig hur du får varningar för font substitution när du renderar Excel filer till PDF med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Ibland, när du renderar en Microsoft Excel-fil till PDF, ersätter Aspose.Cells teckensnitt. Aspose.Cells tillhandahåller en funktion som låter utvecklare veta vilket specifikt teckensnitt som har ersatts genom att utlösa en varning. Detta är en användbar funktion som kan hjälpa dig att identifiera varför en Aspose.Cells-renderad PDF ser annorlunda ut jämfört med den ursprungliga Microsoft Excel-filen, så att du kan vidta lämpliga åtgärder. Till exempel att installera de saknade teckensnitten så att renderingen ser likadan ut.

{{% /alert %}}  

För att få varningar för font-substitution när du renderar Excel-filer till PDF, implementera IWarningCallback-gränssnittet och ställ in PdfSaveOptions.warningCallback med din implementerade gränssnitt.

Skärmbilden nedan visar en käll-Excel-fil som vi kommer att använda i följande kod. Den har lite text i cellerna A6 och A7 med teckensnitt som inte renderas korrekt av Microsoft Excel.

|**Inte alla teckensnitt renderas korrekt**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cells kommer att ersätta teckensnitten i cellerna A6 och A7 med lämpliga teckensnitt, som visas nedan.

|**Ersatta teckensnitt**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **Hämta källfilen och output-PDF**  
Du kan hämta den käll-Excel-filen och output-PDF från följande länkar

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **Kod**  
Följande kod implementerar IWarningCallback och ställer in PdfSaveOptions.warningCallback med den implementerade gränssnittet. Nu, när vilken font som än ersätts i någon cell, kommer Aspose.Cells att utlösa en varning inom WarningCallback.Warning() metoden.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class GetWarningsForFontSubstitution {
static warning(info) {
if (info.getType() === AsposeCells.WarningType.FontSubstitution) {
console.log("WARNING INFO: " + info.getDescription());
}
}

static run() {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setWarningCallback(GetWarningsForFontSubstitution);
const outputFilePath = path.join(dataDir, "output_out.pdf");
workbook.save(outputFilePath, options);
}
}
```  
## **Output**  
Efter att ha konverterat käll-Excel-filen till PDF kommer varningarna att skrivas ut till debuggkonsolen på detta sätt:

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

Om din kalkylblad innehåller formler är det bäst att kalla Workbook.calculateFormula metoden strax före rendering av kalkylbladet till PDF-format. Genom att göra det säkerställs att formla beroende värden omberäknas och de korrekta värdena renderas i PDF.

{{% /alert %}}  

