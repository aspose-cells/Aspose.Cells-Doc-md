---  
title: Node.js kullanarak şablon dosyasından çalışma kitabını yüklerken veri türünü filtreleme  
linktitle: Şablon dosyasından çalışma kitabını yüklerken veri türünü filtreleme  
type: docs  
weight: 400  
url: /tr/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/  
---  

{{% alert color="primary" %}}  
B sometimes, you want to specify which kind of data should be loaded when building the workbook from the template file. Filtering loaded data can improve the performance for your special purpose, especially when using [LightCells APIs](/cells/tr/nodejs-cpp/using-lightcells-api/). Please use the [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) property for this purpose.  
{{% /alert %}}  

Aşağıdaki örnek kod, yükleme sırasında yalnızca şekil nesnelerini yükleyen ve indirilebilecek [şablon dosyasından](5115552.xlsx) yükler. Aşağıdaki ekran görüntüsü, [şablon dosyasını](5115552.xlsx) gösterir ve Kırmızı renk ve Sarı arka plan içeren verilerin yüklenmeyeceğini açıklar; çünkü [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) özelliği [**Shape**](https://reference.aspose.com/cells/nodejs-cpp/shape/) olarak ayarlanmıştır.  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)  

Aşağıdaki ekran görüntüsü, verilerin kırmızı renkli ve sarı arka planlı olmadığını, ancak tüm şekillerin olduğunu gösterir.  

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

