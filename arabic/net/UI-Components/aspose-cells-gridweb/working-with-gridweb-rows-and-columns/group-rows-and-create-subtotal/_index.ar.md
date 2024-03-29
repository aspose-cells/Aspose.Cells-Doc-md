﻿---
title: قم بتجميع الصفوف وإنشاء إجمالي فرعي
type: docs
weight: 70
url: /ar/net/group-rows-and-create-subtotal/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb يمكنه تكوين مخطط تفصيلي للبيانات الخاصة بك. يتيح لك ذلك إظهار مستويات التفاصيل وإخفائها بالنقر فوق رموز المخطط التفصيلي "+" و "-" لعرض الصفوف التي توفر ملخصات أو عناوين للأقسام في ورقة العمل فقط. يمكنك استخدام الرموز لمشاهدة التفاصيل تحت عنوان أو ملخص فردي.

عند تجميع الصفوف ، من المهم تحديد صفوف التفاصيل التي تتكون منها المجموعة فقط. لا تقم بتضمين صف الملخص ذي الصلة. على سبيل المثال ، إذا كان الصف 6 يحتوي على إجماليات البيانات الموجودة في الصف 3 إلى 5 ، فحدد الصف 3 إلى 5 فقط لتحديد المجموعة. يعرض عنصر التحكم Aspose.Cells.GridWeb ملف**أظهر تفاصيل** (+) و**إخفاء التفاصيل** (-) الرموز الموجودة بجانب رؤوس الصفوف التي تحدد المجموعات في ورقة العمل.

Aspose.Cells.GridWeb يسمح لك أيضًا بتكوين مجاميع فرعية بناءً على أي مجال من مجالات البيانات. الإجمالي الفرعي ليس بالضرورة مجموعًا: يمكن أن يكون متوسطًا أو عددًا أو حدًا أدنى أو حدًا أقصى أو حسابًا إحصائيًا آخر.

يناقش هذا الموضوع تجميع الصفوف وإنشاء مجاميع فرعية باستخدام Aspose.Cells.GridWeb API. يمكن للمطورين تجميع الصفوف بأي مستوى تداخل وإنشاء الإجماليات الفرعية بسهولة.

{{% /alert %}} 
## **صفوف التجمع**
لتجميع عدد محدد من الصفوف:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج ويب.
1. قم بالوصول إلى ورقة العمل.
1. حدد عدد الخلايا المطلوب في الصفوف.
1. قم بتجميع الصفوف.

عندما يتم تجميع الصفوف ، يتم عرض زر توسيع / طي أعلى سطر ملخص الصفوف. يمكنك تغيير إعدادات الاتجاه. الخاصية WebWorksheet.IsSummaryRowBelow هي خاصية منطقية. اضبطه على خطأ (افتراضي) وسيكون صف الملخص أعلى صفوف التفاصيل. قم بتعيينه على صحيح وسيكون صف الملخص أسفل صفوف التفاصيل. انقر فوق الزر توسيع / طي لتوسيع أو طي الصفوف المجمعة.

يقوم المثال التالي بتجميع الصفوف من الصف الثاني إلى الصف العاشر.

**صفوف التجمع** 

![ما يجب القيام به: image_بديل_نص](group-rows-and-create-subtotal_1.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **تعشيش صفوف مجمعة**
يمكنك إنشاء مستويات من التنظيم أثناء تجميع مجموعة من الصفوف. يمكنك تجميع الصفوف بين الصفوف المجمعة. يوضح المثال التالي تداخل صفوف مجمعة.

**صفوف التجمع** 

![ما يجب القيام به: image_بديل_نص](group-rows-and-create-subtotal_2.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **العملية الداخلية: كيف تعمل المراقبة؟**
يحتوي كل صف من الصفوف على رقم مخطط تفصيلي. القيمة الافتراضية لرقم المخطط التفصيلي هي صفر. في كل مرة تقوم فيها بتجميع الصفوف ، يتم زيادة رقم المخطط التفصيلي بمقدار 1. يمكنك الحصول على رقم المخطط التفصيلي عن طريق استدعاء طريقة GridWorksheet.Cells.GetRowOutlineLevel ().
## **فك تجميع الصفوف**
Aspose.Cells.GridWeb يسمح لك بفك تجميع الصفوف المجمعة.

لفك تجميع عدد معين من الصفوف:

1. حدد عددًا من الخلايا في الصفوف في ورقة العمل لفك التجميع.
1. فك تجميع الصفوف.

يقوم المثال التالي بفك تجميع الصفوف من الصف الثاني إلى الصف العاشر.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

عند استدعاء أسلوب GridWorksheet.Cells.UngroupRows () ، يتم تعيين رقم المخطط التفصيلي للصفوف المجمعة إلى الصفر.

{{% /alert %}} 
## **إنشاء المجموع الفرعي**
يمكن لميزة الإجمالي الفرعي لعنصر التحكم تجميع الصفوف في الورقة بعمود محدد ، وحساب ملخص الأعمدة. Aspose.Cells.GridWeb يمكنه آليا حساب القيم الإجمالية الفرعية لكشف. عند تنفيذ الإجماليات الفرعية ، يحدد عنصر التحكم القائمة بحيث يمكنك عرض وإخفاء صفوف التفاصيل لكل إجمالي فرعي. قبل إضافة المجاميع الفرعية ، قم بالفرز حسب الحقل الذي تريد المجموع الفرعي فيه. لإنشاء مجاميع فرعية ، استخدم أي إصدار من أسلوب WebWorksheet.CreateSubtotal المحمّل بشكل زائد.



{{< highlight "java" >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[]subtotalColumnIndexList

);

{{< /highlight >}}
### **قائمة المعلمات**

|**لا.**|**اسم المعلمة**|**وصف**|
|:- |:- |:- |
|1|العمودNameRowIndex|فهرس الصف الخاص بصف اسم العمود.|
|2|صفوف البيانات|عدد صفوف البيانات.|
|3|groupByColumnIndex|فهرس العمود الخاص بالعمود المراد تجميعه.|
|4|المجموع الفرعي|تعداد نوع دالة المجموع الفرعي.|
|5|subtotalColumnIndexList|فهارس العمود المراد حسابها حاصل جمعها فرعيًا.|
### **قائمة الوظائف الموجزة**
هناك عدة أنواع من الدالات التلخيصية التي يدعمها التعداد {[SubtotalFunction}}:

|**لا.**|**اسم وظيفة**|**وصف**|
|:- |:- |:- |
|1|معدل|تحسب متوسط القيم.|
|2|عدد|تحسب القيم الرقمية في الخلايا.|
|3|كونتا|تحسب البيانات غير الرقمية في الخلايا.|
|4|الأعلى|تحسب أكبر قيمة.|
|5|دقيقة|تحسب أصغر قيمة.|
|6|المنتج|تحسب حاصل ضرب القيم.|
|7|مجموع|تحسب مجموع القيم.|
ينشئ المثال التالي الإجماليات الفرعية التي تحسب القيم غير الرقمية المجمعة حسب العمود الثاني في ورقة العمل.

**المجاميع الجزئية** 

![ما يجب القيام به: image_بديل_نص](group-rows-and-create-subtotal_3.png)



{{< highlight "java" >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[]{ 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **إزالة المجموع الفرعي**
لإزالة مجموع فرعي ، استخدم أسلوب WebWorksheet.RemoveSubtotal. يزيل المثال التالي المجاميع الفرعية.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **حول وظيفة SUBTOTAL**
يستخدم عنصر التحكم GridWeb دالة الصيغة SUBTOTAL لحساب قيمة الإجمالي الفرعي.

بناء الجملة: SUBTOTAL (function_num ، ref1 ، ref2 ، ...)

function_num هو رقم يحدد نوع الوظيفة المستخدمة في حساب المجموع الفرعي.

|**1**|**معدل**|
|:- |:- |
|2|عدد|
|3|كونتا|
|4|الأعلى|
|5|دقيقة|
|6|المنتج|
|7|مجموع|
المرجع 1 ، المرجع 2 ، هي المناطق التي سيتم جمعها في المجموع الفرعي. إذا احتوت ref1، ref2، ... على دالات إجمالي فرعي أخرى ، فسيتم تجاهل الخلايا المشار إليها لتجنب الحساب المكرر.
