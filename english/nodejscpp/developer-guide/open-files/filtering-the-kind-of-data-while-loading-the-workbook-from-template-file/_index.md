---  
title: Filtering the kind of data while loading the workbook from template file with Node.js via C++  
linktitle: Filtering the kind of data while loading the workbook from template file  
type: docs  
weight: 400  
url: /nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/  
---  

{{% alert color="primary" %}}  
Sometimes, you want to specify which kind of data should be loaded when building the workbook from the template file. Filtering loaded data can improve the performance for your special purpose, especially when using [LightCells APIs](/cells/nodejs-cpp/using-lightcells-api/). Please use the [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) property for this purpose.  
{{% /alert %}}  

The following sample code loads only shape objects while loading the workbook from the [template file](5115552.xlsx) which you can download from the given link. The following screenshot shows the [template file](5115552.xlsx) contents and also explains that the data in Red color and Yellow background will not be loaded because [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) property has been set to [**Shape**](https://reference.aspose.com/cells/nodejs-cpp/shape/)  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)  

The following screenshot shows the [output PDF](5115555.pdf) which you can download from the given link. Here you can see, the data in Red color and Yellow background is not present but all shapes are there.  

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
  
{{< app/cells/assistant language="nodejs-cpp" >}}