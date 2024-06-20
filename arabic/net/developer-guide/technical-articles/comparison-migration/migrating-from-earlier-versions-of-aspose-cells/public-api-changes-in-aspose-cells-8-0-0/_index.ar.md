---
title: تغييرات API العامة في Aspose.Cells 8.0.0
type: docs
weight: 10
url: /ar/net/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

تحتوي هذه الصفحة على تغييرات API العامة التي تم تقديمها في Aspose.Cells 8.0.0. تشمل ليس فقط الطرق العامة الجديدة والمهجورة، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells التي قد تؤثر على الشفرة الحالية.

{{% /alert %}} 
## **تم إضافة MemorySetting إلى LoadOptions وWorkbookSettings**
ابتداء من الإصدار 8.0.0 لـ Aspose.Cells for .NET، قمنا بتوفير خيارات استخدام الذاكرة للاعتبارات الأداء. تتوفر الخاصية MemorySetting الآن في فئتي LoadOptions و WorkbookSettings.
##### **مثال**
يوضح كيفية قراءة ملف Excel (ذو حجم كبير) في وضع محسَّن.

**C#**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

يوضح كيفية كتابة مجموعة بيانات كبيرة إلى ورقة عمل في وضع محسَّن.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [تحسين استخدام الذاكرة أثناء العمل مع ملف كبير](/cells/ar/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **تغيّرت تنفيذات الصفّ والخلية**
في الإصدارات السابقة، تم الاحتفاظ بكائنات الصف والخلية في الذاكرة لتمثيل الصف والخلية المقابلة في ورقة عمل. تم إرجاع نفس النموذج كلما تم استرداد **RowCollection[int index]** أو **Cells[int row, int column]**. لأسباب أداء الذاكرة، سيتم الاحتفاظ بالخصائص والبيانات فقط للصف والخلية في الذاكرة الآن. لذلك، أصبح كائن الصف والخلية مُغلَّف للخصائص المذكورة سابقًا.
### **مثال**
يوضح كيفية مقارنة كائنات الخلية والصف ابتداءً من الآن.

**C#**

{{< highlight csharp >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

نظرًا لأن كائنات الصف والخلية يتم تشكيلها وفقًا للاستدعاء، فإنها لن تتم الاحتفاظ بها وإدارتها في الذاكرة بواسطة مكون الخلايا. لذا بعد بعض عمليات الإدراج والحذف، قد لا تُحدَّث مؤشرات الصف والعمود أو حتى أسوأ، تصبح هذه الكائنات غير صالحة.
### **مثال**
على سبيل المثال ، سيُرجِع القطعة البرمجية التالية نتائج غير صحيحة باستخدام الإصدار 8.0.0 وما فوق

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



مع الإصدار الجديد ، سيصبح كائن الخلية غير صالح أو يشير إلى A2 بقيمة غير مرغوب فيها. من أجل تجنب مثل هذه الحالة ، احصل على كائنات الصف أو الخلية مرة أخرى من مجموعة الخلايا لاسترجاع النتيجة الصحيحة.

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

مجموعة الصفوف لم تعتمد على CollectionBase بعد الآن لأنه لا يوجد كائن صف في القائمة الداخلية لها.

{{% /alert %}}
## **تغير سلوك قيمة السلسلة في الخلية**
في الإصدارات السابقة، كان نمط _ التخصيصي يتم تجاهله أثناء تنسيق قيم الخلية، بينما كان الحرف الخاص * ينتج دائمًا حرفًا واحدًا في النتيجة المنسقة. ابتداءً من هذا الإصدار، قمنا بتغيير المنطق للتعامل مع الأحرف الخاصة _ و * من أجل جعل النتيجة المنسقة مطابقة تمامًا لتطبيق Excel. على سبيل المثال، يستخدم تنسيق الخلية المخصص "_(\$* #,##0.00_)" لتمثيل القيمة 123 النتيجة "$ 123.00". مع الإصدارات الجديدة، ستحتوي خاصية Cell.StringValue على النتيجة ك "$123.00" وهو نفس سلوك تطبيق Excel عند نسخ الخلية إلى نص أو تصديرها إلى CSV.
## **تمت إضافة CreatedTime إلى PdfSaveOptions**
يمكن الآن للمستخدمين الحصول على وضبط وقت إنشاء PDF أثناء حفظ الجدول الخلايا إلى PDF باستخدام فئة PdfSaveOptions.
## **تمت إضافة ShowFormulas إلى ورقة العمل**
من الآن فصاعدا، يمكن للمستخدمين استخدام خاصية بوليانية تسمى ShowFormulas المقدمة من الفئة Worksheet لتغيير العرض من الصيغة إلى القيمة لورقة البيانات المعطاة.
## **تمت إضافة Ooxml إلى FileFormatType**
تمت إضافة الثابت الجديد Ooxml إلى فئة FileFormatType لتمثيل ملف عنصري Office open XML المشفر مثل XLSX، DOCX، PPTX والمزيد.
## **تمت اهمال مجموعة FilterColumnCollection من AutoFilter**
مع Aspose.Cells for Java، تم تسجيل خاصية FilterColumnCollection كمنسوخة. من المقترح استخدام خاصية AuotFilter.FilterColumns بدلاً منها.
## **تم استبدال SeriesCollection.SecondCatergoryData بـ SeriesCollection.SecondCategoryData**
لقد قمنا بتصحيح الخطأ الطباعي في اسم الخاصية SeriesCollection.SecondCatergoryData. يمكنك الآن استخدام خاصية SeriesCollection.SecondCategoryData من الآن فصاعدا، في حين تم تسجيل الخاصية الأصلية SeriesCollection.SecondCatergoryData كمنسوخة.
