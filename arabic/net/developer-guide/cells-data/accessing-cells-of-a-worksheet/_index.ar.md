---
title: الوصول إلى خلايا ورقة العمل
type: docs
weight: 10
url: /ar/net/accessing-cells-of-a-worksheet/
description: يوضح هذا المقال كيفية الحصول على النطاق الأقصى لعرض ورقة العمل والوصول إلى الخلايا من خلال واجهة البرمجة التطبيقية Aspose.Cells for .NET.
keywords: الحصول على كائن الخلية، الوصول إلى الخلايا، الحصول على النطاق الأقصى لعرض ورقة العمل. 
---

{{% alert color="primary" %}}

نحن نعلم أن جميع ورق العمل قد تحتوي على بيانات يتم تخزينها أساسًا في الخلايا (التي يتكون منها ورق العمل). الخلية هي الجزء الأساسي من ورق العمل الذي يُستخدم لبناء الورقة بأكملها كسلسلة من الصفوف والأعمدة. قبل أن نحاول الوصول إلى البيانات من ورقة العمل، سيكون علينا الحصول على تحكم في خلاياها. لذا، في هذا الموضوع، سنناقش بعض الطرق الأساسية للوصول إلى خلايا ورقة العمل أثناء التشغيل باستخدام Aspose.Cells.

{{% /alert %}}

## **كيفية الوصول إلى الخلايا**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تمثل ملف Excel. الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تحتوي على [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورقة في ملف Excel. يتم تمثيل ورقة العمل بفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) تمثل جميع الخلايا في ورقة العمل.

يمكننا استخدام مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) للوصول إلى الخلايا في ورقة عمل. تقدم Aspose.Cells ثلاثة طرق أساسية للوصول إلى الخلايا في ورقة عمل:

1. باستخدام اسم الخلية.
1. باستخدام فهرس صف الخلية والعمود.
1. باستخدام فهرس الخلية في [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة

**مهم:** لقد ذكرنا أن النهج الثالث هو الأسرع والنهج الأول هو الأبطأ. الفارق في الأداء بين النهجين صغير جدًا، لذا لا تقلق بشأن تدهور الأداء، أي نهج تختاره.

### **كيفية الحصول على كائن الخلية باسم الخلية**

يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير اسم الخلية إلى [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة من فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) كفهرس.

إذا قمت بإنشاء ورقة عمل فارغة في البداية، فإن عدد [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة هو صفر. عند استخدام هذا النهج للوصول إلى خلية، سيتحقق ما إذا كانت هذه الخلية موجودة في المجموعة أم لا. إذا كانت موجودة، فسيعيد كائن الخلية في المجموعة ، وإلا، سيقوم بإنشاء كائن [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) جديد، يضيف الكائن إلى [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة ثم يعيد الكائن. هذا النهج هو أسهل طريقة للوصول إلى الخلية إذا كنت على دراية ببرنامج Microsoft Excel ولكنه الأبطأ مقارنةً بالنهجين الآخرين.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **كيفية الحصول على كائن الخلية باستخدام مؤشر صف وعمود الخلية**

يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير فهرس صفها وعمودها إلى [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة من فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

يعمل هذا النهج بنفس الطريقة كطريقة الوصول الأولى.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **كيفية الحصول على كائن الخلية باستخدام فهرس الخلية في مجموعة الخلايا**

يمكن الوصول أيضًا إلى خلية عن طريق تمرير الفهرس الرقمي للخلية إلى [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة.

إذا استخدمت هذا النهج للوصول إلى الخلايا، فقد يتم إثارة استثناء إذا كان الفهرس الرقمي للخلية خارج النطاق. هذا النهج هو الأسرع للوصول إلى الخلايا ولكن الشيء الهام لمعرفته هو أنه إذا استخدمت هذا النهج للوصول إلى كائن الخلية، فإن الفهرس الرقمي قد يتغير بعد إضافة خلايا جديدة إلى [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة. يتم فرز كائنات الخلايا في [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة داخلياً حسب فهارس الصف والعمود.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **كيفية الحصول على النطاق الأقصى لعرض ورقة العمل**

يسمح Aspose.Cells للمطورين بالوصول إلى النطاق العرضي الأقصى لورقة العمل. النطاق العرضي الأقصى - نطاق الخلايا بين أول خلية تحتوي على محتوى وآخر خلية تحتوي على محتوى - مفيد عندما تحتاج إلى نسخ أو تحديد أو عرض محتوى كامل لورقة العمل في صورة.

يمكنك الوصول إلى النطاق الأقصى لعرض ورقة العمل باستخدام [**Worksheet.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange). يوضح الشيفرة البرمجية النموذجية التالية كيفية الوصول إلى الخاصية [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
