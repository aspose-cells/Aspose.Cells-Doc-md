---
title: API العام التغييرات في Aspose.Cells 8.8.2
type: docs
weight: 290
url: /ar/java/public-api-changes-in-aspose-cells-8-8-2/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.8.1 إلى 8.8.2 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تحديث المراجع تلقائيًا أثناء حذف الصفوف والأعمدة الفارغة**
 كشف Aspose.Cells for Java 8.8.2 الإصدارات المحملة بشكل زائد من Cells.deleteBlankRows & Cells.deleteBlankColumns طرق. يمكن للطرق الجديدة قبول مثيل لفئة DeleteOptions ويمكن استخدامها للتغلب على المواقف التي قد تنشأ بسبب المراجع المقطوعة في الصيغ وبيانات سلسلة المخطط وما إلى ذلك. تحتوي فئة DeleteOptions حاليًا على عضو واحد فقط ، وهي خاصية نوع منطقي بالاسم UpdateReference. إذا تم تعيين الخاصية المذكورة إلى true وتم تمرير مثيل الفئة DeleteOptions إلى Cells.deleteBlankRows & Cells.deleteBlankColumns ، فسوف يقوم API بضبط مراجع الصيغة داخليًا (إن وجدت) لاستيعاب التغييرات.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[حذف الصفوف والأعمدة الفارغة ذات المراجع المحدثة](/cells/ar/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
