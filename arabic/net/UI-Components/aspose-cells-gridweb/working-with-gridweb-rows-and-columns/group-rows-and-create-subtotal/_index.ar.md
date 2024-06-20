---
title: تجميع الصفوف وإنشاء المجاميع الفرعية
type: docs
weight: 70
url: /ar/net/aspose-cells-gridweb/group-rows-and-create-subtotal/
keywords: GridWeb,subtotal,group,ungroup
description: هذا المقال يقدم كيفية تجميع/فك تجميع الصفوف/الأعمدة وكيفية العمل مع الإجمالي الفرعي في GridWeb.
---

{{% alert color="primary" %}} 

يمكن لـ Aspose.Cells.GridWeb إنشاء ملخص لبياناتك. يتيح لك ذلك عرض وإخفاء مستويات التفاصيل بالنقر فوق رموز الملخص "+" و "-" لعرض الصفوف فقط التي تقدم ملخصات أو عناوين للأقسام في ورقة العمل. يمكنك استخدام الرموز لرؤية التفاصيل تحت ملخص فردي أو عنوان.

عند تجميع الصفوف، من المهم اختيار الصفوف التفصيلية فقط التي تشكل المجموعة. لا تقم بتضمين الصف القصير ذي الصلة. على سبيل المثال، إذا كان الصف 6 يحتوي على إجماليات للبيانات في الصف 3 إلى 5، حدد الصفوف 3 إلى 5 فقط لتعريف المجموعة. يعرض عنصر التحكم Aspose.Cells.GridWeb رموز **اظهار التفاصيل** (+) و **اخفاء التفاصيل **(-) بجوار ترويسات الصفوف المحددة للمجموعات في ورقة العمل.

يتيح Aspose.Cells.GridWeb أيضاً لك إنشاء الاجماليات الفرعية استنادًا إلى أي حقل من البيانات. الاجمالي الفرعي ليس بالضرورة مجموعًا: يمكن أن يكون متوسطًا، عددًا، الحد الأدنى، الحد الأقصى أو عملية إحصائية أخرى.

يناقش هذا الموضوع تجميع الصفوف وإنشاء الاجماليات الفرعية باستخدام واجهة برمجة التطبيقات Aspose.Cells.GridWeb. يمكن للمطورين تجميع الصفوف بأي مستوى تضمين وإنشاء الاجماليات الفرعية بسهولة.

{{% /alert %}} 
## **تجميع الصفوف**
لتجميع عدد معين من الصفوف:

1. أضف تحكم Aspose.Cells.GridWeb إلى استمارة الويب.
1. الوصول إلى ورقة العمل.
3. حدد العدد المطلوب من الخلايا في الصفوف.
4. قم بتجميع الصفوف.

عند تجميع الصفوف، يتم عرض زر توسيع/طي في أعلى خطوط الملخص. يمكنك تغيير إعداد الاتجاه. خاصية WebWorksheet.IsSummaryRowBelow هي خاصية بوليانية. قم بتعيينها على القيمة البوليانية false (الافتراضي) وسيكون الصف القصير أعلاه. ضعها على true وستكون الصف القصير أسفل الصفوف التفصيلية. انقر فوق زر التوسيع/الطي لتوسيع أو طي الصفوف المجمعة.

المثال التالي يجمع الصفوف من الصف الثاني إلى العاشر.

**تجميع الصفوف** 

![todo:image_alt_text](group-rows-and-create-subtotal_1.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **ضم صفوف مجمعة**
يمكنك إنشاء مستويات من التنظيم أثناء تجميع مجموعة من الصفوف. يمكنك تجميع الصفوف بين الصفوف المجمعة. يوضح المثال التالي تجميع الصفوف متداخلة.

**تجميع الصفوف** 

![todo:image_alt_text](group-rows-and-create-subtotal_2.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **العملية الداخلية: كيفية عمل عنصر التحكم؟**
لكل صف في الورقة رقم تفصيلي. القيمة الافتراضية للرقم التفصيلي هي صفر. في كل مرة تقوم فيها بتجميع الصفوف، يتم زيادة الرقم التفصيلي بمقدار واحد. يمكنك الحصول على الرقم التفصيلي عن طريق استدعاء طريقة GridWorksheet.Cells.GetRowOutlineLevel().
## **إلغاء تجميع الصفوف**
يتيح Aspose.Cells.GridWeb لك إلغاء تجميع الصفوف المجموعة.

لإلغاء تجميع عدد محدد من الصفوف:

1. تحديد عدد من الخلايا في الصفوف في ورقة العمل لإلغاء تجميعها.
1. إلغاء تجميع الصفوف.

المثال التالي يلغي تجميع الصفوف من الصف الثاني إلى الصف العاشر.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

عند استدعاء طريقة GridWorksheet.Cells.UngroupRows(), يتم ضبط رقم الإطار للصفوف المجمعة بصفر.

{{% /alert %}} 
## **إنشاء المجموع الفرعي**
يمكن لميزة المجموع الفرعي للتحكم تجميع الصفوف في الورقة مع عمود محدد، وحساب موجز للأعمدة. يمكن لـ Aspose.Cells.GridWeb حساب قيم المجموع الفرعي تلقائيًا لقائمة. عند تطبيق المجموعات الفرعية، يقوم التحكم بتفصيل القائمة بحيث يمكنك عرض وإخفاء الصفوف التفصيلية لكل مجموع فرعي. قبل إضافة المجموعات الفرعية، قم بالفرز على الحقل الذي ترغب في تجميعه. لإنشاء مجموعات فرعية، استخدم أي إصدار من طريقة WebWorksheet.CreateSubtotal.



{{< highlight java >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[] subtotalColumnIndexList

);

{{< /highlight >}}
### **قائمة المعلمات**

|**لا.**|**اسم المعلمة**|**الوصف**|
| :- | :- | :- |
|1|columnNameRowIndex|فهرس الصف لصف الاسم.|
|2|dataRows|عدد الصفوف البيانات.|
|3|groupByColumnIndex|فهرس العمود ليتم تجميعه.|
|4|subtotalFunction|تصنيف دالة المجموع الفرعي.|
|5|subtotalColumnIndexList|فهرس الأعمدة المراد تجميعها.|
### **قائمة الوظائف الموجزة**
هناك عدة أنواع من وظائف الملخص مدعومة بواسطة سياق العد الفرعي: الباحثة تظهر.

|**لا.**|**اسم الدالة**|**الوصف**|
| :- | :- | :- |
|1|AVERAGE|تحسب متوسط القيم.|
|2|COUNT|يحسب القيم الرقمية في الخلايا|
|3|COUNTA|يحسب البيانات غير الرقمية في الخلايا|
|4|MAX|يحسب أكبر قيمة|
|5|MIN|يحسب أصغر قيمة|
|6|PRODUCT|يحسب الناتج من القيم|
|7|SUM|يحسب مجموع القيم|
المثال التالي يُنشئ المجاميع الفرعية التي تحسب القيم غير الرقمية التي تم تجميعها حسب العمود الثاني في ورقة العمل.

**المجاميع الفرعية** 

![todo:image_alt_text](group-rows-and-create-subtotal_3.png)



{{< highlight java >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[] { 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **إزالة المجموع الفرعي**
لإزالة مجموع فرعي، استخدم طريقة WebWorksheet.RemoveSubtotal. المثال التالي يزيل المجاميع الفرعية.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **حول وظيفة SUBTOTAL**
تستخدم عنصر التحكم GridWeb وظيفة الصيغة SUBTOTAL لحساب قيمة المجموع الفرعي.

الصيغة: SUBTOTAL(رقم الوظيفة، مرجع1، مرجع2، ...)

رقم الوظيفة هو رقم يُحدد نوع الوظيفة المستخدمة في حساب المجموع الفرعي.

|**1**|**متوسط**|
| :- | :- |
|2|COUNT|
|3|COUNTA|
|4|MAX|
|5|MIN|
|6|PRODUCT|
|7|SUM|
ref1 ، و ref2 ، مناطق يجب حساب المجاميع لها. إذا كانت ref1 ، و ref2 ، ... تحتوي على وظائف مجموع جزئي أخرى ، يتم تجاهل الخلايا المشار إليها لتجنب حساب مكرر.
