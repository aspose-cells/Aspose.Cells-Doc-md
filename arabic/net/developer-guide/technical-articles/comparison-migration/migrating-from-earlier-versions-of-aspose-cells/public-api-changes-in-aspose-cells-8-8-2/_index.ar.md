---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.8.2
type: docs
weight: 280
url: /ar/net/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.8.1 إلى 8.8.2 التي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. يتضمن ليس فقط الأساليب العامة الجديدة والمحدثة والصفوف المضافة والمحذوفة إلخ، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تحديث المراجع تلقائيا أثناء حذف الصفوف والأعمدة الفارغة**
في 8.8.2، قدمت Aspose.Cells for .NET الإصدارات المُكثَّفة لأساليب Cells.DeleteBlankRows و Cells.DeleteBlankColumns. يمكن استخدام الأساليب الجديدة للتغلب على المواقف التي قد تحدث بسبب التقارير المحطمة في الصيغ وبيانات سلاسل الرسوم البيانية وما إلى ذلك. يحتوي فئة DeleteOptions حاليًا على عضو واحد فقط، وهو خاصية من نوع بوليان بإسم UpdateReference. إذا تم تعيين خاصية المحدد لتكون صحيحة وتم تمرير نموذج DeleteOptions إلى أساليب Cells.DeleteBlankRows و Cells.DeleteBlankColumns، سيقوم الواجهة بضبط المراجع الصيغية داخليًا (إن وجد) لاستيعاب التغييرات.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [حذف الصفوف والأعمدة الفارغة مع المراجع المحدثة](/cells/ar/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

var book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

var sheet = book.Worksheets[0];

//Access cells of the desired worksheet

var cells = sheet.Cells;

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.UpdateReference = true;

//Delete all blank rows and columns

cells.DeleteBlankColumns(options);

cells.DeleteBlankRows(options);

{{< /highlight >}}
