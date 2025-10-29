---  
title: حفظ كل ورقة عمل إلى ملف PDF مختلف باستخدام Node.js عبر C++  
linktitle: حفظ كل ورقة عمل في ملف PDF مختلف  
type: docs  
weight: 130  
url: /ar/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/  
---  

{{% alert color="primary" %}}  
يدعم Aspose.Cells تحويل ملفات XLS (التي تحتوي على الصور والمخططات، وما إلى ذلك) إلى مستندات PDF. يمكن لـ Aspose.Cells for Node.js via C++ العمل بشكل مستقل لتحويل لائحة البيانات إلى PDF، ولا تحتاج إلى استخدام Aspose.PDF لـ Node.js عبر C++ لهذا التحويل. لا يتطلب التحويل وجود أو استخدام أي ملفات مؤقتة، حيث يمكن تنفيذ العملية بالكامل في الذاكرة.  
{{% /alert %}}  

## **حفظ كل ورقة عمل في ملف PDF مختلف**  
إذا كنت بحاجة إلى حفظ كل ورقة عمل في ملف Excel الخاص بك لإنشاء ملفات PDF مختلفة، يمكنك تحقيق ذلك بسهولة. يمكنك محاولة تعيين فهرس ورقة واحدة إلى [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/nodejs-cpp/pdfs saveoptions/#sheetSet) على حدة لعرضها كـ PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Get the Excel file path
const filePath = path.join(dataDir, "input.xlsx");

// Instantiate a new workbook and open the Excel file from its location
const workbook = new AsposeCells.Workbook(filePath);

// Get the count of the worksheets in the workbook
const sheetCount = workbook.getWorksheets().getCount();

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Take PDFs of each sheet
for (let j = 0; j < sheetCount; j++) {
const ws = workbook.getWorksheets().get(j);

// set worksheet to output
const sheetSet = new AsposeCells.SheetSet([ws.getIndex()]);
pdfSaveOptions.setSheetSet(sheetSet);

workbook.save(path.join(dataDir, `worksheet-${ws.getName()}.out.pdf`), pdfSaveOptions);
}
```  

{{% alert color="primary" %}}  
إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
