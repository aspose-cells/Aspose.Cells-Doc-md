---
title: الوصول إلى خلايا ورقة العمل
type: docs
weight: 10
url: /ar/nodejs-cpp/accessing-cells-of-a-worksheet/
description: توضح هذه المقالة كيفية الحصول على أقصى مدى عرض للورقة والوصول إلى الخلايا من خلال واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: الحصول على كائن الخلية، الوصول إلى الخلايا، الحصول على النطاق الأقصى لعرض ورقة العمل. 
---

{{% alert color="primary" %}}

نعلم أن جميع أوراق العمل قد تحتوي على بيانات تُخزن بشكل أساسي في خلايا (التي تتكون منها ورقة العمل). الخلية هي جزء أساسي من ورقة العمل تُستخدم لبناء الورقة بأكملها كسلسلة من الصفوف والأعمدة. قبل محاولة الوصول إلى البيانات من ورقة العمل، نحتاج إلى الحصول على إذن للوصول إلى خلاياها. لذا، في هذا الموضوع، سنناقش بعض الأساليب الأساسية للوصول إلى خلايا ورقة العمل في وقت التشغيل باستخدام Aspose.Cells for Node.js via C++.

{{% /alert %}}

## **كيفية الوصول إلى الخلايا**

يوفر Aspose.Cells for Node.js via C++ فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) تتيح الوصول إلى كل ورقة عمل في ملف إكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) التي تمثل جميع الخلايا في ورقة العمل.

يمكننا استخدام مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) للوصول إلى الخلايا في ورقة العمل. يوفر Aspose.Cells for Node.js via C++ ثلاث أساليب أساسية للوصول إلى الخلايا في ورقة العمل:

1. باستخدام اسم الخلية.
1. باستخدام فهرس صف الخلية والعمود.
1. باستخدام فهرس الخلية في [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) المجموعة

**مهم:** لقد ذكرنا أن النهج الثالث هو الأسرع والنهج الأول هو الأبطأ. الفارق في الأداء بين النهجين صغير جدًا، لذا لا تقلق بشأن تدهور الأداء، أي نهج تختاره.

### **كيفية الحصول على كائن الخلية باسم الخلية**

يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير اسم الخلية إلى [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) المجموعة من فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) كفهرس.

إذا قمت بإنشاء ورقة عمل فارغة في البداية، فإن عدد [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) المجموعة هو صفر. عند استخدام هذا النهج للوصول إلى خلية، سيتحقق ما إذا كانت هذه الخلية موجودة في المجموعة أم لا. إذا كانت موجودة، فسيعيد كائن الخلية في المجموعة ، وإلا، سيقوم بإنشاء كائن [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) جديد، يضيف الكائن إلى [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) المجموعة ثم يعيد الكائن. هذا النهج هو أسهل طريقة للوصول إلى الخلية إذا كنت على دراية ببرنامج Microsoft Excel ولكنه الأبطأ مقارنةً بالنهجين الآخرين.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellName-1.js" >}}

### **كيفية الحصول على كائن الخلية باستخدام مؤشر صف وعمود الخلية**

يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير فهرس صفها وعمودها إلى [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) المجموعة من فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

يعمل هذا النهج بنفس الطريقة كطريقة الوصول الأولى.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.js" >}}

### **كيفية الحصول على كائن الخلية باستخدام فهرس الخلية في مجموعة الخلايا**

يمكن الوصول أيضًا إلى خلية عن طريق تمرير الفهرس الرقمي للخلية إلى [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) المجموعة.

إذا استخدمت هذا النهج للوصول إلى الخلايا، فقد يتم إثارة استثناء إذا كان الفهرس الرقمي للخلية خارج النطاق. هذا النهج هو الأسرع للوصول إلى الخلايا ولكن الشيء الهام لمعرفته هو أنه إذا استخدمت هذا النهج للوصول إلى كائن الخلية، فإن الفهرس الرقمي قد يتغير بعد إضافة خلايا جديدة إلى [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) المجموعة. يتم فرز كائنات الخلايا في [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) المجموعة داخلياً حسب فهارس الصف والعمود.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.js" >}}

## **كيفية الحصول على النطاق الأقصى لعرض ورقة العمل**

يتيح Aspose.Cells for Node.js via C++ لنود.js عبر C++ للمطورين الوصول إلى أقصى مدى عرض لورقة العمل. النطاق الأقصى للعرض - هو نطاق الخلايا بين أول وخلية تحتوي على محتوى - مفيد عندما تحتاج إلى نسخ أو تحديد أو عرض المحتويات الكاملة لورقة العمل كصورة.

يمكنك الوصول إلى النطاق الأقصى لعرض ورقة العمل باستخدام [**Cells.getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--). يوضح الشيفرة البرمجية النموذجية التالية كيفية الوصول إلى الخاصية [**getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
