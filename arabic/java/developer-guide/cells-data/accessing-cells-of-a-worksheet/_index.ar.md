---
title: الوصول إلى خلايا ورقة العمل
type: docs
weight: 10
url: /ar/java/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

نحن نعلم أن جميع ورق العمل قد تحتوي على بيانات يتم تخزينها أساسًا في الخلايا (التي يتكون منها ورق العمل). الخلية هي الجزء الأساسي من ورق العمل الذي يُستخدم لبناء الورقة بأكملها كسلسلة من الصفوف والأعمدة. قبل أن نحاول الوصول إلى البيانات من ورقة العمل، سيكون علينا الحصول على تحكم في خلاياها. لذا، في هذا الموضوع، سنناقش بعض الطرق الأساسية للوصول إلى خلايا ورقة العمل أثناء التشغيل باستخدام Aspose.Cells.

{{% /alert %}} 
## **الوصول إلى الخلايا**
توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على مجموعة [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). تقدم فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) التي تمثل جميع الخلايا في ورقة العمل.

يمكننا استخدام مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) للوصول إلى الخلايا في ورقة العمل. توفر Aspose.Cells طرقًا أساسية مختلفة للوصول إلى الخلايا:

1. [استخدام اسم الخلية](/cells/ar/java/accessing-cells-of-a-worksheet/).
1. [استخدام فهرس الصف والعمود](/cells/ar/java/accessing-cells-of-a-worksheet/).
### **استخدام اسم الخلية**
يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير اسم الخلية إلى مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) في فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

إذا قمت بإنشاء ورقة عمل فارغة في البداية، فإن عدد [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) في المجموعة هو صفر. عند استخدام هذه الطريقة للوصول إلى خلية، سيتم التحقق مما إذا كانت هذه الخلية موجودة في المجموعة أم لا. إذا كانت موجودة، فإنه سيُرجع كائن الخلية في المجموعة وإلا، فإنه سيقوم بإنشاء كائن [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) جديد، يضيف الكائن إلى مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)، ثم يعيد الكائن. هذه الطريقة هي أسهل طريقة للوصول إلى الخلية إذا كنت ملمًا ببرنامج Microsoft Excel ولكنها أبطأ من الطرق الأخرى.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **استخدام فهرس الصف والعمود للخلية**
يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير فهرس صفها وعمودها إلى مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) في فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

يعمل هذا النهج بنفس الطريقة كطريقة الوصول الأولى.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **مقالات ذات صلة**
{{% alert color="primary" %}} 

- [النطاقات المسماة](/cells/ar/java/named-ranges/)

{{% /alert %}} 
## **الوصول إلى النطاق العرضي الأقصى لورقة العمل**
يسمح Aspose.Cells للمطورين بالوصول إلى النطاق العرضي الأقصى لورقة العمل. النطاق العرضي الأقصى - نطاق الخلايا بين أول خلية تحتوي على محتوى وآخر خلية تحتوي على محتوى - مفيد عندما تحتاج إلى نسخ أو تحديد أو عرض محتوى كامل لورقة العمل في صورة.

يمكنك الوصول إلى نطاق العرض الأقصى لورقة العمل باستخدام [Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

في الشكل التالي، نطاق العرض الأقصى لورقة العمل المحددة هو A1:G15.

**عرض نطاق العرض الأقصى لهذه الورقة العمل** 

![todo:image_alt_text](accessing-cells-of-a-worksheet_1.png)

الكود النموذجي التالي يوضح كيفية الوصول إلى خاصية [MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange). يولد الكود الناتج التالي.

{{< highlight java >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
