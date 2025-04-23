---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.8.2
type: docs
weight: 290
url: /ar/java/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.8.1 إلى 8.8.2 التي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. يتضمن ليس فقط الأساليب العامة الجديدة والمحدثة والصفوف المضافة والمحذوفة إلخ، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تحديث الإشارات تلقائيًا أثناء حذف الصفوف والأعمدة الفارغة**
تعرض Aspose.Cells for Java 8.8.2 الإصدارات المكدسة لطرق Cells.deleteBlankRows و Cells.deleteBlankColumns. يمكن للأساليب الجديدة قبول مثيل من فئة DeleteOptions ويمكن استخدامها للتغلب على المواقف التي قد تنشأ بسبب الإشارات المكسورة في الصيغ وبيانات سلاسل الرسم البياني وما إلى ذلك. تحتوي فئة DeleteOptions حالياً على عضو واحد فقط وهو خاصية من نوع بوليان تحت اسم UpdateReference. إذا تم تعيين الخاصية المذكورة إلى true وتم تمرير مثيل من فئة DeleteOptions إلى طرق Cells.deleteBlankRows و Cells.deleteBlankColumns، ستعدل واجهة برمجة التطبيقات الداخلية (إذا كانت موجودة) مراجع الصيغ لاستيعاب التغييرات. 

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [حذف الصفوف والأعمدة الفارغة مع الإشارات المحدثة](/cells/ar/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

Workbook book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

Worksheet sheet = book.getWorksheets().get(0);

//Access cells of the desired worksheet

Cells cells = sheet.getCells();

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.setUpdateReference(true);

//Delete all blank rows and columns

cells.deleteBlankColumns(options);

cells.deleteBlankRows(options);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
