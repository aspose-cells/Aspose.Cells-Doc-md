---
title: الوصول إلى Cells من ورقة العمل
type: docs
weight: 10
url: /ar/net/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}}

نعلم أن جميع أوراق العمل قد تحتوي على بيانات مخزنة بشكل أساسي في الخلايا (التي تتكون منها ورقة العمل). الخلية هي جزء أساسي من ورقة العمل تُستخدم لإنشاء ورقة العمل بأكملها كسلسلة من الصفوف والأعمدة. قبل أن نحاول الوصول إلى البيانات من ورقة عمل ، سنحتاج إلى الوصول إلى خلاياها. لذلك ، في هذا الموضوع ، سنناقش بعض الأساليب الأساسية للوصول إلى خلايا ورقة العمل في وقت التشغيل باستخدام Aspose.Cells.

{{% /alert %}}

## **الوصول إلى Cells**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تحتوي على[**ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)مجموعة تمثل جميع الخلايا في ورقة العمل.

 يمكننا ان نستخدم[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)جمع للوصول إلى الخلايا في ورقة عمل. يوفر Aspose.Cells ثلاث طرق أساسية للوصول إلى الخلايا في ورقة العمل:

1. باستخدام اسم الخلية.
1. استخدام فهرس صف وعمود الخلية.
1.  باستخدام فهرس الخلية في ملف[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)مجموعة

**الأهمية:**لقد ذكرنا أن الطريقة الثالثة هي الأسرع والأول هي الأبطأ. فرق الأداء بين الأساليب صغير جدًا ، لذا لا تقلق بشأن تدهور الأداء ، أيًا كان الأسلوب الذي تستخدمه.

### **باستخدام Cell الاسم**

 يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير اسم الخلية الخاص بها إلى[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) جمع[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)فئة كمؤشر.

 إذا قمت بإنشاء ورقة عمل فارغة في البداية ، فسيتم حساب عدد[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)المجموعة صفر. عند استخدام هذا الأسلوب للوصول إلى خلية ، فإنه سيتحقق مما إذا كانت هذه الخلية موجودة في المجموعة أم لا. إذا كانت الإجابة بنعم ، فإنه يعيد كائن الخلية في المجموعة وإلا فإنه ينشئ كائنًا جديدًا[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) كائن ، يضيف الكائن إلى[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)جمع ثم إرجاع الكائن. هذا النهج هو أسهل طريقة للوصول إلى الخلية إذا كنت معتادًا على Microsoft Excel ولكنه أبطأ مقارنة بالطرق الأخرى.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **باستخدام فهرس الصف والعمود Cell**

 يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير مؤشرات صفها وعمودها إلى ملف[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) جمع[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)صف دراسي.

يعمل هذا النهج بنفس الطريقة التي يعمل بها النهج الأول.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **استخدام الفهرس Cell في مجموعة Cells**

 يمكن أيضًا الوصول إلى خلية عن طريق تمرير فهرس الخلية الرقمي إلى ملف[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)مجموعة.

 إذا استخدمت هذا الأسلوب للوصول إلى الخلايا ، فيمكن طرح استثناء إذا كان الفهرس الرقمي للخلية خارج النطاق. هذا النهج هو الأسرع للوصول إلى الخلايا ولكن الشيء المهم الذي يجب معرفته هو أنه إذا استخدمت هذا الأسلوب للوصول إلى كائن خلية ، فقد يتغير الفهرس الرقمي بعد إضافة خلايا جديدة إلى[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة. كائنات الخلية في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)يتم فرز المجموعة داخليًا حسب فهارس الصفوف والأعمدة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **الوصول إلى أقصى نطاق عرض لورقة العمل**

Aspose.Cells يسمح للمطورين بالوصول إلى أقصى نطاق عرض لورقة العمل. يكون نطاق العرض الأقصى - نطاق الخلايا بين الخلية الأولى والأخيرة مع المحتوى - مفيدًا عندما تحتاج إلى نسخ أو تحديد أو عرض المحتويات الكاملة لورقة العمل في صورة.

 يمكنك الوصول إلى أقصى نطاق عرض لورقة العمل باستخدام[**ورقة العمل Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . يوضح نموذج التعليمات البرمجية التالي كيفية الوصول إلى ملف[**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)خاصية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
