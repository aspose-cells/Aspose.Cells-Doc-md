---
title: إعداد خصائص ScaleCrop و LinksUpToDate لخصائص المستند المدمجة باستخدام Node.js عبر C++
linktitle: ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة
type: docs
weight: 320
url: /ar/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: تعلم كيفية تعيين خصائص ScaleCrop و LinksUpToDate لخصائص المستند المدمجة باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**
[مجمعة خصائص المستند المدمجة.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) و [مجمعة خصائص المستند المدمجة.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) هما خاصيتان موسعتان من خصائص المستند المدمجة المعرفتان داخل تنسيق OpenXml. الهدف من هذه الخصائص هو التالي.

## **1) ScaleCrop**
يشير هذا العنصر إلى وضع عرض الصورة المصغرة للمستند. قم بتعيين هذا العنصر إلى **TRUE** لتمكين تحجيم الصورة المصغرة للعرض. قم بتعيين هذا العنصر إلى **FALSE** لتمكين قص الصورة المصغرة لإظهار أقسام فقط تناسب العرض.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.

## **2) LinksUpToDate**
يشير هذا العنصر إلى ما إذا كانت الروابط الفائقة في مستند محدثة. قم بتعيين هذا العنصر إلى **TRUE** للإشارة إلى أن الروابط الفائقة تم تحديثها. قم بتعيين هذا العنصر إلى **FALSE** للدلالة على أن الروابط الفائقة قديمة.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.

## **لقطة شاشة تظهر هاتين الخاصيتين داخل ملف app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة**
 يحدد رمز النموذج التالي خصائص المستند المدمجة الموسعة getScaleCrop() و getLinksUpToDate() الخاصة بكتاب العمل. يرجى التحقق من ملف إكسل الناتج (5115500.xlsx) الذي تم إنشاؤه باستخدام هذا الرمز، غير امتداده إلى .zip وفك محتوياته، واطلع على الملف app.xml كما هو موضح في الصورة أعلاه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook();

// Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
workbook.getBuiltInDocumentProperties().getScaleCrop(true);
workbook.getBuiltInDocumentProperties().setLinksUpToDate(true);

// Saving the Excel file.
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Auto);
```
