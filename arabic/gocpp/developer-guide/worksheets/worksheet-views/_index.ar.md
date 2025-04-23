---
title: عروض الورقة العمل
type: docs
weight: 40
url: /ar/go-cpp/worksheet-views/
---

## **معاينة كسر الصفحة**

يمكن عرض جميع الصفحات العمل في وضعين:

- العرض العادي.
- معاينة كسر الصفحة.

العرض العادي هو العرض الافتراضي لورقة العمل. معاينة كسر الصفحة هو عرض التحرير الذي يعرض ورقة العمل كما ستطبع. تعرض معاينة كسر الصفحة البيانات التي ستظهر على كل صفحة حتى تتمكن من ضبط منطقة الطباعة وكسور الصفحة. يمكن لمطوري Aspose.Cells تمكين العرض العادي أو وضع معاينة كسر الصفحة.

### **التحكم في أوضاع العرض**

توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) تتيح الوصول إلى كل ورقة عمل في الملف.

تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) مجموعة واسعة من الطرق لإدارة أوراق العمل. يمكن تفعيل وضع معاينة فواصل الصفحات أو وضع المعاينة العادي باستخدام طريقة [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) من فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). تراجِع [IsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/ispagebreakpreview/) قيمة بوليانية، مما يعني أنه يمكنها فقط تخزين قيمة **صحيح** أو **خاطئ**.

#### **تمكين العرض العادي**

قم بضبط ورقة العمل على عرض عادي عن طريق تعيين طريقة [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) من فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) إلى **خاطئ**.

#### **تمكين معاينة كسر الصفحة**

قم بضبط أي ورقة عمل على وضع معاينة فاصل الصفحات من خلال تعيين طريقة [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) من فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) إلى **صحيح**. يفعل ذلك تحويل ورقة العمل من الوضع العادي إلى معاينة فاصل الصفحات.

يوضح المثال الكامل التالي كيفية استخدام طريقة [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) لتمكين وضع معاينة فاصل الصفحات لأول ورقة عمل في ملف Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnablingPageBreakPreview.go" >}}

## **عامل التكبير**

### **استخدام Microsoft Excel**

يوفر Microsoft Excel ميزة تتيح للمستخدمين تعيين عامل تكبير أو تدرج الورقة العمل. تساعد هذه الميزة المستخدمين في رؤية محتويات ورقة العمل في عروض أصغر أو أكبر. يمكن للمستخدمين تعيين عامل التكبير إلى أي قيمة.

### **Aspose.Cells وعامل التكبير**

تسمح Aspose.Cells أيضًا للمطورين بضبط عامل تكبير ورقة العمل. توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) التي تمثل ملف Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) تتيح الوصول إلى كل ورقة عمل في الملف.

تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) مجموعة واسعة من الطرق لإدارة أوراق العمل. لضبط عامل تكبير ورقة العمل، استخدم طريقة [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) من فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). يتم تعيين عامل التكبير عن طريق إعطاء قيمة رقمية (صحيحة) لطريقة [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/).

يوضح المثال الكامل التالي كيفية استخدام طريقة [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) لضبط عامل تكبير أول ورقة عمل في ملف Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ZoomFactor.go" >}}

## **تجميد الألواح**

### **استخدام Microsoft Excel**

تجميد الألواح هو ميزة تقدمها مايكروسوفت إكسل. يتيح لك تجميد الألواح تحديد البيانات التي تظل مرئية عند التمرير في ورقة البيانات.

### **Aspose.Cells & تجميد الألواح**

تتيح Aspose.Cells أيضًا للمطورين تطبيق قوالب تجميد على أوراق العمل أثناء التشغيل. توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) تتيح الوصول إلى كل ورقة عمل في الملف.

تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) مجموعة واسعة من الطرق لإدارة أوراق العمل. لضبط تجميد الأجزاء، استدعِ طريقة [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) من فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). تتطلب الطريقة [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) المعلمات التالية:

- **الصف**، فهرس الصف للخلية التي سيبدأ منها التجميد.
- **العمود**، فهرس العمود للخلية التي سيبدأ منها التجميد.
- **الصفوف المجمدة**، عدد الصفوف المرئية في اللوحة العلوية.
- **الأعمدة المجمدة**، عدد الأعمدة المرئية في اللوحة اليسرى.

تم إعطاء مثال كامل أدناه يوضح كيفية استخدام طريقة [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) لتجميد الصفوف والأعمدة (ابتداءً من C4، ممثلة بالصف الرابع والعمود الثالث، حيث تبدأ الصفوف والأعمدة من الفهرس 0) في الورقة الأولى من ملف الإكسل.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FreezePanes.go" >}}

## **تقسيم الألواح**

إذا كنت بحاجة إلى تقسيم الشاشة للحصول على مناظر مختلفة في نفس ورقة البيانات، استخدم تقسيم الألواح. تقدم مايكروسوفت إكسل ميزة مفيدة تسمح لك بعرض أكثر من نسخة واحدة من ورقة البيانات الخاصة بك، وتمكنك من التمرير من خلال كل لوحة من ورقة البيانات بشكل مستقل: تقسيم الألواح.

الألواح تعمل بشكل متزامن. إذا قمت بإجراء تغيير في أحدها، فإن التغيير يظهر بشكل متزامن في الآخر. توفر Aspose.Cells ميزة تقسيم الألواح للمستخدمين.

### **تطبيق وإزالة تقسيم الألواح**

#### **تقسيم الألواح**

توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) التي تمثل ملف ميكروسوفت إكسل. تتيح فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) مجموعة واسعة من الطرق لإدارة ملف إكسل. لتنفيذ عرض مقسم، استخدم طريقة [Split](https://reference.aspose.com/cells/go-cpp/worksheet/split/) التابعة لفئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). لإزالة اللوحات المجزأة، استخدم طريقة [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/)

في المثال، نستخدم ملف قالب بسيط يتم تحميله، ثم يتم تطبيق ميزة تقسيم الألواح المحددة على خلية في الورقة البيانات الأولى. يتم حفظ الملف المحدث.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitPanes.go" >}}

#### **إزالة النوافذ**

إزالة اللوحات المجزأة باستخدام طريقة [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingPanes.go" >}}
