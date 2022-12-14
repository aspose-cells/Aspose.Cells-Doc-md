---
title: API العام التغييرات في Aspose.Cells 8.0.0
type: docs
weight: 10
url: /ar/net/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

تسرد هذه الصفحة التغييرات العامة API التي تم تقديمها في Aspose.Cells 8.0.0. لا يشمل فقط الأساليب العامة الجديدة والمتقادمة ، ولكن أيضًا وصف أي تغييرات في السلوك خلف الكواليس في Aspose.Cells والتي قد تؤثر على الكود الحالي.

{{% /alert %}} 
## **تمت إضافة MemorySetting إلى LoadOptions & WorkbookSettings**
بدءًا من الإصدار 8.0.0 من Aspose.Cells for .NET ، قمنا بتوفير خيارات استخدام الذاكرة لاعتبارات الأداء. خاصية MemorySetting متاحة الآن في فئات LoadOptions & WorkbookSettings.
##### **مثال**
يوضح كيفية قراءة ملف Excel (كبير الحجم) في الوضع الأمثل.

**C#**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

يوضح كيفية كتابة مجموعة بيانات كبيرة إلى ورقة عمل في الوضع الأمثل.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[تحسين الذاكرة أثناء العمل مع الملفات الكبيرة](/cells/ar/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **تم تغيير تطبيقات Row & Cell**
 في الإصدارات السابقة ، تم الاحتفاظ بكائنات Row و Cell في الذاكرة لتمثيل الصف والخلية المطابقة في ورقة عمل. تم إرجاع نفس المثيل كلما**RowCollection [فهرس int]** أو**Cells [الصف الدولي ، العمود الدولي]** تم استرجاعها. للنظر في أداء الذاكرة ، سيتم الاحتفاظ بخصائص وبيانات صف و Cell فقط في الذاكرة الآن فصاعدًا. ومن ثم ، أصبح الكائن Row & Cell غلافًا للخصائص المذكورة سابقًا.
### **مثال**
يوضح كيفية مقارنة Cell وكائنات الصف من الآن فصاعدًا.

**C#**

{{< highlight "csharp" >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

نظرًا لأنه يتم تكوين كائنات الصف و Cell وفقًا للاستدعاء ، فلن يتم الاحتفاظ بها وإدارتها في الذاكرة بواسطة المكون Cells. لذلك بعد بعض عمليات الإدراج والحذف ، قد لا يتم تحديث فهارس الصف والعمود أو حتى أسوأ من ذلك ، تصبح هذه الكائنات غير صالحة.
### **مثال**
على سبيل المثال ، سيعرض مقتطف الشفرة التالي نتائج غير صالحة باستخدام 8.0.0 وما فوق ،

**C#**

{{< highlight "csharp" >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



مع الإصدار الجديد ، سيصبح الكائن Cell غير صالح أو يشير إلى A2 مع بعض القيمة غير المرغوب فيها. لتجنب مثل هذا الموقف ، احصل على صف أو Cell كائنات مرة أخرى من مجموعة الخلايا لاسترداد النتيجة الصحيحة.

**C#**

{{< highlight "csharp" >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

لم يعد RowCollection يرث CollectionBase لأنه لا يوجد كائن صف في قائمته الداخلية.

{{% /alert %}}
## **تغيير سلوك قيمة السلسلة Cell**
 في الإصدارات السابقة ، نمط خاص_تم تجاهله أثناء تنسيق قيم الخلية ، حيث ينتج الحرف الخاص * دائمًا حرفًا واحدًا في النتيجة المنسقة. من هذا الإصدار ، قمنا بتغيير المنطق للتعامل مع الأحرف الخاصة_ و* من أجل جعل النتيجة المنسقة مماثلة لتطبيق Excel. على سبيل المثال ، تنسيق الخلية المخصص "_ (\ $* #، ## 0.00_) "تستخدم لتمثيل القيمة 123 التي أنتجت النتيجة كـ" $ 123.00 ". مع الإصدارات الجديدة ، ستحتوي Cell.StringValue على النتيجة كـ" $ 123.00 "وهو نفس السلوك الذي يعرضه تطبيق Excel أثناء نسخ الخلية إلى نص أو التصدير إلى CSV.
## **تمت إضافة CreatedTime إلى PdfSaveOptions**
الآن يمكن للمستخدمين الحصول على وقت إنشاء PDF أو تعيينه أثناء حفظ جدول البيانات في PDF أثناء استخدام فئة PdfSaveOptions.
## **تمت إضافة صيغ العرض إلى ورقة العمل**
من الآن فصاعدًا ، يمكن للمستخدمين استخدام الخاصية المنطقية ShowFormulas التي تقدمها ورقة العمل لتغيير طريقة العرض من صيغة إلى قيمة ورقة عمل معينة.
## **تمت إضافة Ooxml إلى FileFormatType**
تمت إضافة Ooxml ثابت جديد إلى فئة FileFormatType لتمثيل ملف XML المفتوح المشفر في Office مثل XLSX و DOCX و PPTX والمزيد.
## **عامل التصفية المتقادم**
باستخدام Aspose.Cells for Java ، تم وضع علامة على خاصية FilterColumnCollection التي عفا عليها الزمن. يُقترح استخدام خاصية AuotFilter.FilterColumns بدلاً من ذلك.
## **تم استبدال SeriesCollection.SecondCatergoryData بـ SeriesCollection.SecondCategoryData**
لقد قمنا بشكل أساسي بتصحيح الخطأ المطبعي في اسم الخاصية SeriesCollection.SecondCatergoryData. يمكنك استخدام خاصية SeriesCollection.SecondCategoryData الآن فصاعدًا ، بينما تم وضع علامة على الخاصية الأصلية SeriesCollection.SecondCatergoryData قديمة.
