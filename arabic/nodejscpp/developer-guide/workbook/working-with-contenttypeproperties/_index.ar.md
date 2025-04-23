---  
title: العمل مع ContentTypeProperties مع Node.js عبر C++  
linktitle: العمل مع خصائص نوع الوسائط  
type: docs  
weight: 150  
url: /ar/nodejs-cpp/working-with-contenttypeproperties/  
description: تعلّم كيف تعمل مع خصائص نوع المحتوى المخصصة في ملفات إكسل باستخدام Aspose.Cells for Node.js via C++.  
---  

يوفر Aspose.Cells طريقة [**Workbook.getContentTypeProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getContentTypeProperties--) لإضافة ContentTypeProperties مخصصة إلى ملف إكسل. يمكنك أيضًا جعل الخاصية اختيارية عن طريق تعيين خاصية [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/nodejs-cpp/contenttypeproperty/#isNillable--) إلى **true**. يوضح مقتطف الكود التالي كيف يتم إضافة Properties مخصصة اختيارية إلى ملف إكسل. تُظهر الصورة التالية كلا الخاصيتين اللتين تمت إضافتهما بواسطة الكود النموذجي.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

يتم إرفاق ملف الإخراج الذي تم إنشاؤه بواسطة مقتطف الكود للإشارة.

[ملف الإخراج](95584314.xlsx)

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

//source directory
const outputDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);
let index = workbook.getContentTypeProperties().add("MK31", "Simple Data");
workbook.getContentTypeProperties().get(index).setIsNillable(false);
index = workbook.getContentTypeProperties().add("MK32", new Date().toISOString(), "DateTime");
workbook.getContentTypeProperties().get(index).setIsNillable(true);
workbook.save(path.join(outputDir, "WorkingWithContentTypeProperties_out.xlsx"));
```  

