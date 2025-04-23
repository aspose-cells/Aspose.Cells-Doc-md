---  
title: Filtrering av data när arbetsboken laddas från mallfil med Node.js via C++  
linktitle: Filtrera vilken typ av data som ska laddas från mallfilen när arbetsboken laddas  
type: docs  
weight: 400  
url: /sv/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/  
---  

{{% alert color="primary" %}}  
Ibland vill du specificera vilken sorts data som ska laddas när du bygger arbetsboken från mallfilen. Filtrering av inläst data kan förbättra prestandan för ditt speciella syfte, särskilt när du använder [LightCells API]( /cells/sv/nodejs-cpp/using-lightcells-api/). Vänligen använd egenskapen [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) för detta ändamål.  
{{% /alert %}}  

Följande exempel laddar endast formobjekt när arbetsboken laddas från [mallfilen](5115552.xlsx) som du kan ladda ner via länken. Skärmbilden visar innehållet i [mallfilen](5115552.xlsx) och förklarar även att data i rött och med gul bakgrund inte kommer att laddas eftersom egenskapen [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) har satts till [**Shape**](https://reference.aspose.com/cells/nodejs-cpp/shape/)  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)  

Följande skärmbild visar [utdata PDF](5115555.pdf) som du kan ladda ned från länken. Här kan du se att datan i rött och gul bakgrund inte finns men alla former är där.  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Set the load options, we only want to load shapes and do not want to load data
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);            

loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Create workbook object from sample excel file using load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleFilterChars.xlsx"), loadOptions);

// Save the output in pdf format
workbook.save(outputDir + "sampleFilterChars_out.pdf", AsposeCells.SaveFormat.Pdf);
```  

