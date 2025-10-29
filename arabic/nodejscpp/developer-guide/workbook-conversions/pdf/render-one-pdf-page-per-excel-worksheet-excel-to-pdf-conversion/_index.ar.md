---  
title: عرض صفحة PDF واحدة لكل ورقة عمل في إكسيل  تحويل إكسيل إلى PDF عبر Node.js باستخدام C++  
linktitle: عرض صفحة PDF واحدة لكل ورقة Excel  تحويل Excel إلى صيغة PDF  
type: docs  
weight: 100  
url: /ar/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/  
---  

{{% alert color="primary" %}}  

عند العمل مع ملفات إكسيل كبيرة (على سبيل المثال، مصنف يحتوي على العديد من الأوراق، كل منها يحتوي على 50 عمودًا و300 أو أكثر من الصفوف), قد ترغب في أن يُظهر الناتج PDF صفحة واحدة لكل ورقة، بغض النظر عن حجم الورقة. هذا يعني أن كل صفحة من المحتمل أن يكون لديها حجم صفحة مختلف بشكل جذري. يمكن تحقيق ذلك باستخدام Aspose.Cells for Node.js via C++.  

{{% /alert %}}  

يرجى الاطلاع على الكود النموذجي التالي الذي يحول ملف Excel مع العديد من الأوراق إلى PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Implement one page per worksheet option
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setOnePagePerSheet(true);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile.out.pdf"), pdfSaveOptions);
```  

{{% alert color="primary" %}}  

إذا تم ضبط خاصية [PdfSaveOptions.getOnePagePerSheet()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) على **true**، سيتم عرض جميع محتويات الورقة على صفحة PDF واحدة.  

{{% /alert %}} {{% alert color="primary" %}}  

إذا كانت ورقة العمل تحتوي على صيغ، فمن الأفضل استدعاء [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) مباشرة قبل عرضها كملف PDF. يضمن ذلك إعادة حساب القيم المعتمدة على الصيغ، وعرض القيم الصحيحة في PDF.  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
