---  
title: إضافة مرجع مكتبة إلى مشروع VBA في دفتر العمل باستخدام Node.js عبر C++  
linktitle: أضف مرجعًا إلى مشروع VBA في سجل العمل  
type: docs  
weight: 80  
url: /ar/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/  
---  

{{% alert color="primary" %}}  

أحيانًا ، قد تحتاج إلى إضافة أو تسجيل مرجع المكتبة إلى مشروع VBA من خلال الكود. يمكنك القيام بذلك باستخدام طريقة Aspose.Cells [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-).  

{{% /alert %}}  

## **أضف مرجع مكتبة إلى مشروع VBA في Microsoft Excel**  

في Microsoft Excel ، يمكنك إضافة مرجع مكتبة إلى مشروع VBA عن طريق النقر على ** الأدوات > مراجع... ** يدوياً.  

## **إضافة مرجع مكتبة إلى مشروع VBA في مصنف باستخدام الرقم Aspose.Cells for Node.js via C++**  

يعرض المثال التالي إضافة أو تسجيل مرجعين للمكتبة إلى مشروع VBA للمصنف باستخدام طريقة [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputPath = path.join(dataDir, "Output_out.xlsm");

const workbook = new AsposeCells.Workbook();

const vbaProj = workbook.getVbaProject();
vbaProj.getReferences().addRegisteredReference("stdole", "*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation");
vbaProj.getReferences().addRegisteredReference("Office", "*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library");

workbook.save(outputPath);
```  

