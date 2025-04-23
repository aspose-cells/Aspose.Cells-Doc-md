---
title: تغييرات API العامة في Aspose.Cells 8.0.0
type: docs
weight: 20
url: /ar/java/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

تحتوي هذه الصفحة على تغييرات API العامة التي تم تقديمها في Aspose.Cells 8.0.0. تشمل ليس فقط الطرق العامة الجديدة والمهجورة، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells التي قد تؤثر على الشفرة الحالية.

{{% /alert %}} 
## **تم إضافة MemorySetting إلى LoadOptions وWorkbookSettings**
ابتداءً من الإصدار 8.0.0 من Aspose.Cells for Java، لقد قمنا بتوفير خيارات استخدام الذاكرة لأسباب أداء. الآن تتوفر خاصية MemorySetting في فئات LoadOptions وWorkbookSettings.
### **مثال**
يوضح كيفية قراءة ملف Excel (ذو حجم كبير) في وضع محسَّن.

**Java**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

يوضح كيفية كتابة مجموعة بيانات كبيرة إلى ورقة عمل في وضع محسَّن.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [تحسين استخدام الذاكرة أثناء العمل مع ملف كبير](/cells/ar/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **تغيّرت تنفيذات الصفّ والخلية**
في الإصدارات السابقة، تم الاحتفاظ بكائنات الصف والخلية في الذاكرة لتمثيل الصف والخلية المقابلة في ورقة عمل. تم إرجاع نفس النموذج كلما تم استرداد **RowCollection[int index]** أو **Cells[int row, int column]**. لأسباب أداء الذاكرة، سيتم الاحتفاظ بالخصائص والبيانات فقط للصف والخلية في الذاكرة الآن. لذلك، أصبح كائن الصف والخلية مُغلَّف للخصائص المذكورة سابقًا.
### **مثال**
يوضح كيفية مقارنة كائنات الخلية والصف ابتداءً من الآن.

**Java**

{{< highlight csharp >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

نظرًا لأن كائنات الصف والخلية يتم تشكيلها وفقًا للاستدعاء، فإنها لن تتم الاحتفاظ بها وإدارتها في الذاكرة بواسطة مكون الخلايا. لذا بعد بعض عمليات الإدراج والحذف، قد لا تُحدَّث مؤشرات الصف والعمود أو حتى أسوأ، تصبح هذه الكائنات غير صالحة.
### **مثال**
على سبيل المثال ، سيُرجِع القطعة البرمجية التالية نتائج غير صحيحة باستخدام الإصدار 8.0.0 وما فوق

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

مع الإصدار الجديد ، سيصبح كائن الخلية غير صالح أو يشير إلى A2 بقيمة غير مرغوب فيها. من أجل تجنب مثل هذه الحالة ، احصل على كائنات الصف أو الخلية مرة أخرى من مجموعة الخلايا لاسترجاع النتيجة الصحيحة.

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

مجموعة الصفوف لم تعتمد على CollectionBase بعد الآن لأنه لا يوجد كائن صف في القائمة الداخلية لها.

{{% /alert %}}
## **تغير سلوك قيمة السلسلة في الخلية**
في الإصدارات السابقة ، تم تجاهل النمط الخاص _ أثناء تنسيق قيم الخلية ، حيث أن الحرف الخاص * لا ينتج دائمًا حرفًا واحدًا في النتيجة المنسقة. ابتداءً من هذا الإصدار ، لقد قمنا بتغيير المنطق للتعامل مع الأحرف الخاصة _ و * من أجل جعل النتيجة المنسقة مماثلة لتطبيق Excel. كعرض ، فإن التنسيق المخصص للخلية "_(\$* #,##0.00_)" المستخدم لتمثيل القيمة 123 أنتج النتيجة "$ 123.00". مع الإصدارات الجديدة ، ستحتوي قيمة السلسلة  للخلية على النتيجة كـ "$123.00" وهو نفس السلوك الذي يُظهر تطبيق Excel عند نسخ الخلية إلى نص أو تصديرها إلى CSV.
## **تمت إضافة CreatedTime إلى PdfSaveOptions**
يمكن الآن للمستخدمين الحصول على وضبط وقت إنشاء PDF أثناء حفظ الجدول الخلايا إلى PDF باستخدام فئة PdfSaveOptions.
## **تمت إضافة ShowFormulas إلى ورقة العمل**
ابتداءً من الآن ، يمكن للمستخدمين استخدام خاصية القيمة المنطقية ShowFormulas المُقدمة من ورقة العمل لتبديل العرض بين الصيغة والقيمة في ورقة العمل المُعطاة.
## **تمت إضافة Ooxml إلى FileFormatType**
تمت إضافة الثابت الجديد Ooxml إلى فئة FileFormatType لتمثيل ملف عنصري Office open XML المشفر مثل XLSX، DOCX، PPTX والمزيد.
## **تمت اهمال مجموعة FilterColumnCollection من AutoFilter**
مع Aspose.Cells for Java ، تم تحديد الطريقة getFilterColumnCollection على أنها مهجورة. من المُقترح استخدام طريقة AuotFilter.getFilterColumns بدلاً من ذلك.
## **تم استبدال SeriesCollection.SecondCatergoryData بـ SeriesCollection.SecondCategoryData**
لقد قمنا بتصحيح خطأ الطباعة الأساسي في اسم الطريقة لـ SeriesCollection.getSecondCatergoryData. يمكنك الآن استخدام طريقة SeriesCollection.getSecondCategoryData ابتداءً من الآن ، في حين أن الطريقة الأصلية SeriesCollection.getSecondCatergoryData تم تحديدها على أنها مهجورة.
{{< app/cells/assistant language="java" >}}
