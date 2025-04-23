---  
title: Filtra il tipo di dati durante il caricamento del workbook da file modello con Node.js tramite C++  
linktitle: Filtrare il tipo di dati durante il caricamento della cartella di lavoro dal file di modello  
type: docs  
weight: 400  
url: /it/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/  
---  

{{% alert color="primary" %}}  
A volte, si desidera specificare quale tipo di dati dovrebbe essere caricato quando si crea il workbook dal file modello. Filtrare i dati caricati può migliorare le prestazioni per scopi specifici, soprattutto quando si utilizzano le API [LightCells](/cells/it/nodejs-cpp/using-lightcells-api/). Si usi la proprietà [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) a questo scopo.  
{{% /alert %}}  

Il seguente esempio carica soltanto oggetti forma durante il caricamento del workbook dal [file modello](5115552.xlsx), che si può scaricare dal link fornito. Il seguente screenshot mostra il contenuto del [file modello](5115552.xlsx) e spiega anche che i dati di colore rosso e sfondo giallo non saranno caricati perché la proprietà [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) è stata impostata su [**Shape**](https://reference.aspose.com/cells/nodejs-cpp/shape/)  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)  

Lo screenshot seguente mostra il [PDF di output](5115555.pdf) che è possibile scaricare dal link fornito. Qui si può vedere che i dati di colore rosso e sfondo giallo non sono presenti ma ci sono tutte le forme.  

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

