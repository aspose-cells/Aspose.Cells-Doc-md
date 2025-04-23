---  
title: Filtern der Art der Daten beim Laden der Arbeitsmappe aus einer Vorlage mit Node.js über C++  
linktitle: Filtern der Art der Daten beim Laden des Arbeitsbuches aus der Vorlagendatei  
type: docs  
weight: 400  
url: /de/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/  
---  

{{% alert color="primary" %}}  
Manchmal möchten Sie angeben, welche Art von Daten beim Erstellen der Arbeitsmappe aus der Vorlage geladen werden soll. Das Filtern der geladenen Daten kann die Leistung für Ihren speziellen Zweck verbessern, insbesondere bei Verwendung der [LightCells-APIs](/cells/de/nodejs-cpp/using-lightcells-api/). Bitte verwenden Sie zu diesem Zweck die Eigenschaft [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--).  
{{% /alert %}}  

Der folgende Beispielcode lädt nur Shape-Objekte beim Laden der Arbeitsmappe aus der [Vorlagendatei](5115552.xlsx), die Sie über den angegebenen Link herunterladen können. Der folgende Screenshot zeigt die Inhalte der [Vorlagendatei](5115552.xlsx) und erklärt auch, dass die in Rot gefärbten Daten und der gelbe Hintergrund nicht geladen werden, da die Eigenschaft [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) auf [**Shape**](https://reference.aspose.com/cells/nodejs-cpp/shape/) gesetzt wurde.  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)  

Der folgende Screenshot zeigt das [Ausgabe-PDF](5115555.pdf), das Sie aus dem angegebenen Link herunterladen können. Hier sehen Sie, dass die Daten in roter Farbe und gelbem Hintergrund nicht vorhanden sind, aber alle Formen sind vorhanden.  

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

