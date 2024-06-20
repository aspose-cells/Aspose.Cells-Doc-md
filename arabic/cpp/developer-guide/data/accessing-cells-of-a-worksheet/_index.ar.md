---
title: الوصول إلى خلايا ورقة العمل
type: docs
weight: 10
url: /ar/cpp/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

نحن نعلم أن جميع ورق العمل قد تحتوي على بيانات يتم تخزينها أساسًا في الخلايا (التي يتكون منها ورق العمل). الخلية هي الجزء الأساسي من ورق العمل الذي يُستخدم لبناء الورقة بأكملها كسلسلة من الصفوف والأعمدة. قبل أن نحاول الوصول إلى البيانات من ورقة العمل، سيكون علينا الحصول على تحكم في خلاياها. لذا، في هذا الموضوع، سنناقش بعض الطرق الأساسية للوصول إلى خلايا ورقة العمل أثناء التشغيل باستخدام Aspose.Cells.

{{% /alert %}} 
## **الوصول إلى الخلايا**
توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح باستخدام كل ورقة عمل في ملف Excel. ورقة العمل ممثلة بفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) . توفر فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) التي تمثل جميع الخلايا في ورقة العمل.

يمكننا استخدام مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) للوصول إلى الخلايا في ورقة العمل. توفر Aspose.Cells ثلاثة طرق أساسية للوصول إلى الخلايا في ورقة العمل:

1. باستخدام اسم الخلية.
1. باستخدام فهرس صف الخلية والعمود.
1. باستخدام فهرس الخلية في مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

{{% alert color="primary" %}} 

لقد ذكرنا أن الطريقة الثالثة هي الأسرع والطريقة الأولى هي الأبطأ. الفرق في الأداء بين الطرق ضئيل جدًا لذا لا تقلق بشأن تدهور الأداء، مهما كانت الطريقة التي تستخدمها.

{{% /alert %}} 
### **استخدام اسم الخلية**
يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير اسم الخلية إلى مجموعة الـ [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) في فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) كمؤشر.

إذا قمت بإنشاء ورقة عمل فارغة في البداية، فإن عدد مجموعة الـ [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) هو صفر. عند استخدام هذا النهج للوصول إلى خلية، سيتحقق ما إذا كانت هذه الخلية موجودة في المجموعة أم لا. إذا كانت موجودة، سيُرجع كائن الخلية في المجموعة وإلا، سينشئ كائن خلية جديدًا، يضيف الكائن إلى مجموعة الـ [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) ومن ثم يُرجع ذلك الكائن. هذا النهج هو أسهل طريقة للوصول إلى الخلية إذا كنت على دراية بـ Microsoft Excel ولكنه الأبطأ بالمقارنة مع النهج الآخر.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
### **استخدام فهرس الصف والعمود للخلية**
يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير فهارس صفها وعمودها إلى مجموعة الـ [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) في فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ويعمل هذا النهج بنفس الطريقة كنهج الوصول الأول.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
## **الوصول إلى النطاق العرضي الأقصى لورقة العمل**
تسمح Aspose.Cells للمطورين بالوصول إلى النطاق العرض الأقصى لورق عمل. النطاق العرض الأقصى - نطاق الخلايا بين الخلية الأولى والأخيرة التي تحتوي على محتوى - مفيد عندما تحتاج إلى نسخ أو تحديد أو عرض المحتويات الكاملة لورق عمل في صورة.

يمكنك الوصول إلى النطاق العرض الأقصى لورق العمل باستخدام طريقة [MaxDisplayRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) في مجموعة الـ [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
