---  
title: إدراج صورة مرتبطة من عنوان الويب باستخدام Node.js عبر C++  
linktitle: إدراج صورة ربط من عنوان الويب  
type: docs  
weight: 450  
url: /ar/nodejs-cpp/insert-a-linked-picture-from-web-address/  
description: تعلم كيفية إدراج صورة مرتبطة من عنوان ويب داخل ورقة عمل باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
 في بعض الأحيان تحتاج إلى إدراج صورة من الويب (http://) في ورقة عمل. للقيام بذلك، حدد عنوان URL للصورة، وسيتم تنزيل الصورة في كل مرة يتم فيها فتح جدول البيانات في إكسل. الصورة غير مضمنة فعليًا في مستند إكسل، ولكنها تشير إلى مصدر ويب.  
{{% /alert %}}  

## **استخدام Microsoft Excel**  

في Microsoft Excel (على سبيل المثال 2007):  

1. انقر فوق قائمة **إدراج** وحدد **صورة**.  
1. حدد عنوان الويب للصورة في مربع حوار إدراج صورة.  

## ** باستخدام Aspose.Cells for Node.js via C++**  

يدعم Aspose.Cells for Node.js via C++ إضافة صورة مرتبطة باستخدام [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). تعيد الطريقة كائن [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture).  

يظهر المثال التالي كيفية إضافة صورة مرتبطة من عنوان ويب إلى ورقة عمل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();
// Insert a linked picture (from Web Address) to B2 Cell.
const pic = workbook.getWorksheets().get(0).getShapes().addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");
// Set the height and width of the inserted image.
pic.setHeightInch(1.04);
pic.setWidthInch(2.6);
// Save the Excel file.
workbook.save(path.join(dataDir, "outLinkedPicture.out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
