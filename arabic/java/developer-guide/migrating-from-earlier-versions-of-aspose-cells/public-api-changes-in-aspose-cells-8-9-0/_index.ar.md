---
title: التغييرات في واجهة برمجة التطبيقات العامة في Aspose.Cells 8.9.0
type: docs
weight: 310
url: /ar/java/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات العامة في Aspose.Cells من الإصدار 8.8.3 إلى 8.9.0 التي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. يتضمن الوثيقة ليس فقط الطرق العامة الجديدة والمحدثة والفئات المُضافة والمُزالة إلخ، بل وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة خاصية HtmlSaveOptions.DefaultFontName**
قامت Aspose.Cells for Java 8.9.0 بتعريض خاصية DefaultFontName لفئة HtmlSaveOptions التي تسمح بتحديد اسم الخط الافتراضي أثناء تقديم جداول البيانات إلى تنسيق HTML. سيتم استخدام الخط الافتراضي فقط عندما لا يكون الخط من النوع الذي تستخدمه النمط. القيمة الافتراضية لخاصية HtmlSaveOptions.DefaultFontName هي null وهذا يعني أن واجهة برمجة التطبيقات Aspose.Cells for Java ستستخدم الخط العالمي الذي يحمل نفس العائلة مع الخط الأصلي.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقالة حول [تعيين الخط الأساسي لتقديم جداول البيانات في تنسيق HTML](/cells/ar/java/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **تمت إضافة خاصية ImageOrPrintOptions.DefaultFont**
Aspose.Cells for Java 8.9.0 يسمح بتعيين اسم الخط الأساسي لفئة ImageOrPrintOptions عن طريق تعريض خاصية DefaultFont. يمكن استخدام الخاصية المذكورة عندما لا يتم تعيين الأحرف اليونيكود في جدول البيانات بالخط الصحيح في نمط الخلية وبالتالي قد تظهر هذه الأحرف كمربعات في الصور الناتجة. 

{{% alert color="primary" %}} 

قم بتعيين خاصية DefaultFont إلى MingLiu أو MS Gothic لعرض الأحرف اليونيكود. إذا لم يتم تعيين الخاصية المذكورة، فسوف يستخدم Aspose.Cells الخط الأساسي للنظام لعرض الأحرف اليونيكود. 

{{% /alert %}} {{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقالة حول [تعيين الخط الأساسي لتقديم جداول البيانات في تنسيقات الصور](/cells/ar/java/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of ImageOrPrintOptions

ImageOrPrintOptions options = new ImageOrPrintOptions();

//Set default font name for image rendering

options.setDefaultFont("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet to be rendered

Worksheet sheet = book.getWorksheets().get(0);

//Create an instance of SheetRender

SheetRender render = new SheetRender(sheet, options);

//Save spreadsheet to image

render.toImage(0, dir + "output.png");

{{< /highlight >}}
### **تمت إضافة خاصية PivotTable.Excel2003Compatible**
Aspose.Cells for Java API قد عرضت خاصية Excel2003Compatible من نوع Boolean لفئة PivotTable مما يسمح بتحديد ما إذا كانت جدول الأحصاء متوافقة مع Excel 2003 لأغراض التحديث. القيمة الافتراضية لخاصية Excel2003Compatible هي true، وهذا يعني أنه يجب أن تكون السلسلة أقل من أو تساوي 255 حرفًا. إذا كانت السلسلة أكبر من 255 حرفًا، فسيتم تقليصها. إذا تم تعيين القيمة على الخطأ، فإن القيود المذكورة سابقًا لن تكون منفذة.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقالة حول [التوافق مع Excel 2003 لتحديث جداول البيانات الخمولية](/cells/ar/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the desired Pivot Table from the spreadsheet

PivotTable pivot = book.getWorksheets().get(0).getPivotTables().get(0);

//Set Excel 2003 compatibility to false

pivot.setExcel2003Compatible(false);

//Refresh & recalculate Pivot Table

pivot.refreshData();

pivot.calculateData();

{{< /highlight >}}
