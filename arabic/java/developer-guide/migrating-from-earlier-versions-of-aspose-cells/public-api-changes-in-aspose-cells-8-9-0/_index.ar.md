---
title: API العام التغييرات في Aspose.Cells 8.9.0
type: docs
weight: 310
url: /ar/java/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.8.3 إلى 8.9.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة خاصية HtmlSaveOptions.DefaultFontName**
كشف Aspose.Cells for Java 8.9.0 الخاصية DefaultFontName لفئة HtmlSaveOptions التي تسمح بتحديد اسم الخط الافتراضي أثناء تحويل جداول البيانات إلى تنسيق HTML. سيتم استخدام الخط الافتراضي فقط في حالة عدم وجود خط النمط. القيمة الافتراضية لخاصية HtmlSaveOptions.DefaultFontName خالية مما يعني أن Aspose.Cells for Java API سيستخدم الخط العام الذي له نفس العائلة مع الخط الأصلي.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة على[تحديد الخط الافتراضي لتحويل جداول البيانات إلى نسق HTML](/cells/ar/java/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
 Aspose.Cells for Java 8.9.0 يسمح بتعيين اسم طاقم الطباعة الافتراضي لفئة ImageOrPrintOptions عن طريق كشف خاصية الخط الافتراضي. يمكن استخدام الخاصية المذكورة عندما لا يتم تعيين أحرف Unicode في جدول البيانات بالخط الصحيح في نمط الخلية ، وبالتالي قد تظهر هذه الأحرف ككتل في الصور الناتجة.

{{% alert color="primary" %}} 

 قم بتعيين خاصية الخط الافتراضي إلى MingLiu أو MS Gothic لإظهار أحرف Unicode. إذا لم يتم تعيين الخاصية المذكورة ، فسيستخدم Aspose.Cells الخط الافتراضي للنظام لإظهار أحرف Unicode.

{{% /alert %}} {{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة على[تعيين الخط الافتراضي لعرض جداول البيانات في تنسيقات الصورة](/cells/ar/java/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
### **تمت إضافة خاصية متوافقة مع PivotTable.Excel2003**
كشف Aspose.Cells for Java API الخاصية المتوافقة Excel2003 من النوع المنطقي لفئة PivotTable التي تسمح بتحديد ما إذا كان PivotTable متوافقًا مع Excel 2003 لأغراض التحديث. القيمة الافتراضية للخاصية المتوافقة في Excel2003 صحيحة ، وهذا يعني أن السلسلة يجب أن تكون أقل من أو تساوي 255 حرفًا. إذا كانت السلسلة أكبر من 255 حرفًا ، فسيتم قطعها. إذا كانت خاطئة ، فلن يتم فرض القيد المذكور أعلاه.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة على[التوافق مع Excel 2003 لتحديث الجداول المحورية](/cells/ar/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
