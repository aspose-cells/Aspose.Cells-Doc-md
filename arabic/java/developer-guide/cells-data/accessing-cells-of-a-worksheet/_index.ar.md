---
title: الوصول إلى Cells من ورقة العمل
type: docs
weight: 10
url: /ar/java/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

نعلم أن جميع أوراق العمل قد تحتوي على بيانات مخزنة بشكل أساسي في الخلايا (التي تتكون منها ورقة العمل). الخلية هي جزء أساسي من ورقة العمل تُستخدم لإنشاء ورقة العمل بأكملها كسلسلة من الصفوف والأعمدة. قبل أن نحاول الوصول إلى البيانات من ورقة عمل ، سنحتاج إلى الوصول إلى خلاياها. لذلك ، في هذا الموضوع ، سنناقش بعض الأساليب الأساسية للوصول إلى خلايا ورقة العمل في وقت التشغيل باستخدام Aspose.Cells.

{{% /alert %}} 
## **الوصول إلى Cells**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فئة توفر أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)مجموعة تمثل جميع الخلايا في ورقة العمل.

 يمكننا استخدام[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)جمع للوصول إلى الخلايا في ورقة عمل. يوفر Aspose.Cells طرقًا أساسية مختلفة للوصول إلى الخلايا:

1. [باستخدام اسم الخلية](/cells/ar/java/accessing-cells-of-a-worksheet/).
1. [باستخدام فهرس الصف والعمود](/cells/ar/java/accessing-cells-of-a-worksheet/).
### **باستخدام Cell الاسم**
 يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير اسم الخلية الخاص بها إلى[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) جمع[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)صف دراسي.

 إذا قمت بإنشاء ورقة عمل فارغة في البداية ، فسيتم حساب عدد[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)المجموعة صفر. عند استخدام هذا الأسلوب للوصول إلى خلية ، فإنه سيتحقق مما إذا كانت هذه الخلية موجودة في المجموعة أم لا. إذا كانت الإجابة بنعم ، فإنه يعيد كائن الخلية في المجموعة وإلا فإنه ينشئ كائنًا جديدًا[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) كائن ، يضيف الكائن إلى[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)جمع ثم إرجاع الكائن. هذا الأسلوب هو أسهل طريقة للوصول إلى الخلية إذا كنت معتادًا على Microsoft Excel ولكنه أبطأ من الطرق الأخرى.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **باستخدام فهرس الصف والعمود Cell**
 يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير مؤشرات صفها وعمودها إلى ملف[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) جمع[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)صف دراسي.

يعمل هذا النهج بنفس الطريقة التي يعمل بها النهج الأول.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **مقالات ذات صلة**
{{% alert color="primary" %}} 

- [النطاقات المسماة](/cells/ar/java/named-ranges/)

{{% /alert %}} 
## **الوصول إلى أقصى نطاق عرض لورقة العمل**
Aspose.Cells يسمح للمطورين بالوصول إلى أقصى نطاق عرض لورقة العمل. يكون نطاق العرض الأقصى - نطاق الخلايا بين الخلية الأولى والأخيرة مع المحتوى - مفيدًا عندما تحتاج إلى نسخ أو تحديد أو عرض المحتويات الكاملة لورقة العمل في صورة.

 يمكنك الوصول إلى أقصى نطاق عرض لورقة العمل باستخدام[Worksheet.getCells (). getMaxDisplayRange ()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

في الشكل التالي ، الحد الأقصى لنطاق عرض ورقة العمل المحدد هو A1: G15.

**إظهار أقصى نطاق عرض لورقة العمل هذه** 

![ما يجب القيام به: image_بديل_نص](accessing-cells-of-a-worksheet_1.png)

 يوضح نموذج التعليمات البرمجية التالي كيفية الوصول إلى ملف[MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)خاصية. يولد الكود الناتج التالي.

{{< highlight "java" >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
