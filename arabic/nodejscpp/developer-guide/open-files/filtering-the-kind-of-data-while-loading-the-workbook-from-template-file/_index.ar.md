---  
title: تصفيه نوع البيانات أثناء تحميل دفتر العمل من ملف القالب باستخدام Node.js عبر C++  
linktitle: تصفية نوع البيانات أثناء تحميل ورق العمل من ملف النموذج  
type: docs  
weight: 400  
url: /ar/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/  
---  

{{% alert color="primary" %}}  
في بعض الأحيان، تريد تحديد نوع البيانات التي يجب تحميلها عند بناء دفتر العمل من ملف القالب. يمكن أن تؤدي تصفية البيانات المحملة إلى تحسين الأداء لغرضك الخاص، خاصة عند استخدام [واجهات برمجة التطبيقات LightCells](/cells/ar/nodejs-cpp/using-lightcells-api/). يرجى استخدام الخاصية [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) لهذا الغرض.  
{{% /alert %}}  

يقوم الكود النموذجي التالي بتحميل كائنات الشكل فقط أثناء تحميل دفتر العمل من [ملف القالب](5115552.xlsx) والذي يمكنك تنزيله من الرابط المعطى. توضح الصورة التالية محتويات [ملف القالب](5115552.xlsx) كما تشرح أن البيانات باللون الأحمر والخلفية الصفراء لن يتم تحميلها لأن الخاصية [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) تم تعيينها إلى [**Shape**](https://reference.aspose.com/cells/nodejs-cpp/shape/)  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)  

تُظهر اللقطة الشاشية التالية ال [PDF الناتج](5115555.pdf) الذي يمكنك تحميله من الرابط المقدم. هنا يمكنك أن ترى، البيانات ذات اللون الأحمر والخلفية الصفراء غير موجودة لكن جميع الأشكال موجودة.  

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
