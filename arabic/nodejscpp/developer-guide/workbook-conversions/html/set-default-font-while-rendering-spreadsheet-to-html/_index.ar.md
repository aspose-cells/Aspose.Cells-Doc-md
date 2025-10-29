---  
title: تعيين الخط الافتراضي عند عرض جدول البيانات كـ HTML مع Node.js عبر C++  
linktitle: تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML  
type: docs  
weight: 370  
url: /ar/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/  
---  

{{% alert color="primary" %}}  
يتيح Aspose.Cells لك تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML. يرجى استخدام [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) لهذا الغرض. هذا الخاصية مفيدة عندما تكون هناك خلايا في جدول البيانات تحتوي على خطوط خطأ أو غير موجودة. ثم سيتم عرض تلك الخلايا بالخط المحدد بالخاصية [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--).  
{{% /alert %}}  

## تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML  

الكود العيني التالي يقوم بإنشاء دفتر عمل وإضافة نص معين في الخلية B4 من أول ورقة عمل ويقوم بتعيين خطه إلى خط غير معروف / غير موجود. ثم يقوم بحفظ الدفتر العمل بتنسيق HTML عن طريق تعيين أسماء خط مختلفة كـ Courier New, Arial, Times New Roman وما إلى ذلك.  

تُظهر صورة لقطة الشاشة تأثير تعيين أسماء خطوط افتراضية مختلفة عبر خاصية [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--).  

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)  

يُولّد الكود ملف [HTML الناتج بخط Courier New](5115516), [HTML الناتج بخط Arial](5115518), و [HTML الناتج بخط Times New Roman](5115517).  

## كود عينة  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object and access first worksheet.
const wb = new AsposeCells.Workbook();
const ws = wb.getWorksheets().get(0);

// Access cell B4 and add some text inside it.
const cell = ws.getCells().get("B4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell B4 which is unknown.
const st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
cell.setStyle(st);

// Now save the workbook in html format and set the default font to Courier New.
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDefaultFontName("Courier New");
wb.save(path.join(dataDir, "out_courier_new_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Arial.
opts.setDefaultFontName("Arial");
wb.save(path.join(dataDir, "out_arial_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Times New Roman.
opts.setDefaultFontName("Times New Roman");
wb.save(path.join(dataDir, "times_new_roman_out.htm"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
