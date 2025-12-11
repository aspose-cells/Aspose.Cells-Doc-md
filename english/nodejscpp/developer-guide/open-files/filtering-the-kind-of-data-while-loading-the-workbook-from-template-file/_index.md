---  
title: Filtering the kind of data while loading the workbook from a template file with Node.js via C++  
linktitle: Filtering the kind of data while loading the workbook from a template file  
type: docs  
weight: 400  
url: /nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
Sometimes you want to specify which kind of data should be loaded when building the workbook from the template file. Filtering loaded data can improve performance for your specific purpose, especially when using [LightCells APIs](/cells/nodejs-cpp/using-lightcells-api/). Please use the [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) property for this purpose.  
{{% /alert %}}  

The following sample code loads only shape objects while loading the workbook from the [template file](5115552.xlsx), which you can download from the given link. The next screenshot shows the contents of the [template file](5115552.xlsx) and also explains that the data in red text and yellow background will not be loaded because the [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) property has been set to [**Shape**](https://reference.aspose.com/cells/nodejs-cpp/shape/).  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)  

The following screenshot shows the [output PDF](5115555.pdf), which you can download from the given link. Here you can see that the data in red text and yellow background is not present, but all shapes are present.  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Set the load options; we only want to load shapes and do not want to load data
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);            

loadOptions.setLoadFilter(
    new AsposeCells.LoadFilter(
        AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart
    )
);

// Create a workbook object from the sample Excel file using load options
const workbook = new AsposeCells.Workbook(
    path.join(sourceDir, "sampleFilterChars.xlsx"),
    loadOptions
);

// Save the output in PDF format
workbook.save(outputDir + "sampleFilterChars_out.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
