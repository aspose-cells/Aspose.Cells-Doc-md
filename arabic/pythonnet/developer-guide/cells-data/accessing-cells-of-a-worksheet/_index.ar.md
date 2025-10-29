---
title: الوصول إلى خلايا ورقة العمل
type: docs
weight: 10
url: /ar/python-net/accessing-cells-of-a-worksheet/
description: هذه المقالة توضح كيفية الحصول على نطاق العرض الأقصى لورقة العمل والوصول إلى الخلايا من خلال Aspose.Cells for Python via .NET API.
keywords: مكتبة بيثون لإكسل، الحصول على كائن الخلية، الوصول إلى الخلايا، كيفية الحصول على كائن الخلية بواسطة فهرس الصف والعمود للخلية، كيفية الحصول على كائن الخلية بواسطة فهرس الخلية في مجموعة الخلايا، كيفية الحصول على كائن الخلية بواسطة فهرس الصف والعمود للخلية، الحصول على النطاق الأقصى للعرض لورقة العمل. 
---

{{% alert color="primary" %}}

نحن نعلم أن جميع ورقات العمل قد تحتوي على بيانات يتم تخزينها أساسًا في الخلايا (التي تُكوّن ورقة عمل). الخلية هي جزء أساسي من ورقة عمل يتم استخدامه لبناء الورقة العمل بأكملها على شكل سلسلة من الصفوف والأعمدة. قبل أن نحاول الوصول إلى البيانات من ورقة عمل، سيتعين علينا الحصول على الوصول إلى خلاياها. لذلك، في هذا الموضوع، سنناقش بعض النهج الأساسية للوصول إلى خلايا ورقة العمل أثناء التشغيل باستخدام Aspose.Cells for Python via .NET.

{{% /alert %}}

## **كيفية الوصول إلى الخلايا**

توفر Aspose.Cells for Python via .NET فئةً، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) تمثل ملف Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). تقدم الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) تمثل جميع الخلايا في ورقة العمل.

يمكننا استخدام [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) المجموعة للوصول إلى الخلايا في ورقة العمل. Aspose.Cells for Python via .NET يوفر ثلاثة نهج أساسية للوصول إلى الخلايا في ورقة العمل:

1. باستخدام اسم الخلية.
1. باستخدام فهرس صف الخلية والعمود.
1. باستخدام فهرس الخلية في [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) المجموعة

**مهم:** لقد ذكرنا أن النهج الثالث هو الأسرع والنهج الأول هو الأبطأ. الفارق في الأداء بين النهجين صغير جدًا، لذا لا تقلق بشأن تدهور الأداء، أي نهج تختاره.

### **كيفية الحصول على كائن الخلية باسم الخلية**

يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير اسم الخلية إلى [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) المجموعة من فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) كفهرس.

إذا قمت بإنشاء ورقة عمل فارغة في البداية، فإن عدد [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) المجموعة هو صفر. عند استخدام هذا النهج للوصول إلى خلية، سيتحقق ما إذا كانت هذه الخلية موجودة في المجموعة أم لا. إذا كانت موجودة، فسيعيد كائن الخلية في المجموعة ، وإلا، سيقوم بإنشاء كائن [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) جديد، يضيف الكائن إلى [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) المجموعة ثم يعيد الكائن. هذا النهج هو أسهل طريقة للوصول إلى الخلية إذا كنت على دراية ببرنامج Microsoft Excel ولكنه الأبطأ مقارنةً بالنهجين الآخرين.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellName-1.py" >}}

### **كيفية الحصول على كائن الخلية باستخدام مؤشر صف وعمود الخلية**

يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير فهرس صفها وعمودها إلى [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) المجموعة من فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

يعمل هذا النهج بنفس الطريقة كطريقة الوصول الأولى.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.py" >}}

### **كيفية الحصول على كائن الخلية باستخدام فهرس الخلية في مجموعة الخلايا**

يمكن الوصول أيضًا إلى خلية عن طريق تمرير الفهرس الرقمي للخلية إلى [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) المجموعة.

إذا استخدمت هذا النهج للوصول إلى الخلايا، فقد يتم إثارة استثناء إذا كان الفهرس الرقمي للخلية خارج النطاق. هذا النهج هو الأسرع للوصول إلى الخلايا ولكن الشيء الهام لمعرفته هو أنه إذا استخدمت هذا النهج للوصول إلى كائن الخلية، فإن الفهرس الرقمي قد يتغير بعد إضافة خلايا جديدة إلى [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) المجموعة. يتم فرز كائنات الخلايا في [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) المجموعة داخلياً حسب فهارس الصف والعمود.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.py" >}}

## **كيفية الحصول على النطاق الأقصى لعرض ورقة العمل**

Aspose.Cells for Python via .NET يسمح للمطورين بالوصول إلى النطاق الأقصى لعرض ورقة العمل. النطاق الأقصى للعرض - نطاق الخلايا بين أول وآخر خلية تحتوي على محتوى - مفيد عند الحاجة إلى نسخ أو تحديد أو عرض محتويات الورقة بأكملها في صورة.

يمكنك الوصول إلى النطاق الأقصى لعرض ورقة العمل باستخدام [**Worksheet.cells.max_display_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/). يوضح الشيفرة البرمجية النموذجية التالية كيفية الوصول إلى الخاصية [**MaxDisplayRange**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
