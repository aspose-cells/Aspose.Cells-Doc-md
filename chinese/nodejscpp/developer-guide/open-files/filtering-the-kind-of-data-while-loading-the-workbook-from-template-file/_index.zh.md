---  
title: 使用 C++ 通过 Node.js 在从模板文件加载工作簿时筛选特定类型的数据  
linktitle: 从模板文件加载工作簿时过滤数据类型  
type: docs  
weight: 400  
url: /zh/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/  
---  

{{% alert color="primary" %}}  
 有时，您希望在从模板文件构建工作簿时指定应加载的数据类型。筛选加载的数据可以提高您的特定目的的性能，特别是在使用 [LightCells API](/cells/zh/nodejs-cpp/using-lightcells-api/) 时。请使用 [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) 属性实现此目的。  
{{% /alert %}}  

 以下示例代码仅在加载工作簿时加载形状对象，工作簿来自给定链接中的 [模板文件](5115552.xlsx)。下图显示了 [模板文件](5115552.xlsx) 的内容，并说明因为设置了 [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) 属性为 [**Shape**](https://reference.aspose.com/cells/nodejs-cpp/shape/) ，所以红色和黄色背景的数据不会被加载。  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)  

下面的屏幕截图显示了您可以从给定链接下载的[输出PDF](5115555.pdf)。在这里，您可以看到红色和黄色背景中的数据不存在，但所有形状都在那里。  

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
