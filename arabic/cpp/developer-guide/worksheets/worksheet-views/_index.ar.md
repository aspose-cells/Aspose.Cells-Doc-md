---
title: عروض الورقة العمل
type: docs
weight: 40
url: /ar/cpp/worksheet-views/
---

## **معاينة كسر الصفحة**
يمكن عرض جميع الصفحات العمل في وضعين:

- العرض العادي.
- معاينة كسر الصفحة.

العرض العادي هو العرض الافتراضي لورقة العمل. معاينة كسر الصفحة هو عرض التحرير الذي يعرض ورقة العمل كما ستطبع. تعرض معاينة كسر الصفحة البيانات التي ستظهر على كل صفحة حتى تتمكن من ضبط منطقة الطباعة وكسور الصفحة. يمكن لمطوري Aspose.Cells تمكين العرض العادي أو وضع معاينة كسر الصفحة.
### **التحكم في أوضاع العرض**
توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) . توفر فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة واسعة من الطرق لإدارة أوراق العمل. لتمكين العرض العادي أو وضع معاينة كسر الصفحة ، استخدم طريقة [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) لفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) . تُرجع [IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) قيمة منطقية ، والتي تعني أنه يمكنها فقط تخزين قيمة **صحيحة** أو **خاطئة**.
#### **تمكين العرض العادي**
قم بتعيين ورقة عمل إلى العرض العادي عن طريق تعيين طريقة [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) لفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) إلى **خاطئة**.
#### **تمكين معاينة كسر الصفحة**
قم بتعيين أي ورقة عمل إلى معاينة كسر الصفحة عن طريق تعيين طريقة [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) لفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) إلى **صحيحة**. بذلك يقوم الورقة العمل بالتبديل من العرض العادي إلى معاينة كسر الصفحة.

يعرض المثال الكامل أدناه كيفية استخدام طريقة [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) لتمكين وضع معاينة كسر الصفحة لأول ورقة عمل في ملف Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
## **عامل التكبير**
### **استخدام Microsoft Excel**
يوفر Microsoft Excel ميزة تتيح للمستخدمين تعيين عامل تكبير أو تدرج الورقة العمل. تساعد هذه الميزة المستخدمين في رؤية محتويات ورقة العمل في عروض أصغر أو أكبر. يمكن للمستخدمين تعيين عامل التكبير إلى أي قيمة.
### **Aspose.Cells وعامل التكبير**
تسمح Aspose.Cells أيضًا للمطورين بتعيين عامل تكبير الورقة العمل. توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

ورقة البيانات يتم تمثيلها بواسطة الفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). الفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) توفر مجموعة واسعة من الأساليب لإدارة ورقات البيانات. لتحديد عامل تكبير ورقة البيانات، استخدم أسلوب [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) من الفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). يتم تعيين عامل التكبير عن طريق تعيين قيمة رقمية (عدد صحيح) لأسلوب [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/).

يتم تقديم مثال كامل أدناه يوضح كيفية استخدام أسلوب [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) لتحديد عامل تكبير الورقة لأول ورقة في ملف إكسل.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
## **تجميد الألواح**
### **استخدام Microsoft Excel**
تجميد الألواح هو ميزة تقدمها مايكروسوفت إكسل. يتيح لك تجميد الألواح تحديد البيانات التي تظل مرئية عند التمرير في ورقة البيانات.
### **Aspose.Cells & تجميد الألواح**
تسمح Aspose.Cells أيضًا للمطورين بتطبيق تجميد الألواح لورقات البيانات أثناء التشغيل. توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) تتيح الوصول إلى كل ورقة بيانات في ملف Excel.

ورقة البيانات يتم تمثيلها بواسطة الفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). الفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) توفر مجموعة واسعة من الأساليب لإدارة ورقات البيانات. لتكوين تجميد الألواح، استدعي أسلوب [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) من الفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). يأخذ أسلوب [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) المعلمات التالية:

- **الصف**، فهرس الصف للخلية التي سيبدأ منها التجميد.
- **العمود**، فهرس العمود للخلية التي سيبدأ منها التجميد.
- **الصفوف المجمدة**، عدد الصفوف المرئية في اللوحة العلوية.
- **الأعمدة المجمدة**، عدد الأعمدة المرئية في اللوحة اليسرى.

يتم تقديم مثال كامل أدناه يوضح كيفية استخدام أسلوب [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) لتجميد الصفوف والأعمدة (ابتداءً من C4، الممثلة بالصف الرابع والعمود الثالث، حيث تبدأ الصفوف والأعمدة من الفهرس 0) لأول ورقة في ملف إكسل.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
## **تقسيم الألواح**
إذا كنت بحاجة إلى تقسيم الشاشة للحصول على مناظر مختلفة في نفس ورقة البيانات، استخدم تقسيم الألواح. تقدم مايكروسوفت إكسل ميزة مفيدة تسمح لك بعرض أكثر من نسخة واحدة من ورقة البيانات الخاصة بك، وتمكنك من التمرير من خلال كل لوحة من ورقة البيانات بشكل مستقل: تقسيم الألواح.

الألواح تعمل بشكل متزامن. إذا قمت بإجراء تغيير في أحدها، فإن التغيير يظهر بشكل متزامن في الآخر. توفر Aspose.Cells ميزة تقسيم الألواح للمستخدمين.
### **تطبيق وإزالة تقسيم الألواح**
#### **تقسيم الألواح**
توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Microsoft Excel. توفر الفئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) مجموعة واسعة من الأساليب لإدارة ملف Excel. لتنفيذ عرض مقسّمين، استخدم أسلوب [Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) من الفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). لإزالة ألواح الفصل، استخدم أسلوب [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/).

في المثال، نستخدم ملف قالب بسيط يتم تحميله، ثم يتم تطبيق ميزة تقسيم الألواح المحددة على خلية في الورقة البيانات الأولى. يتم حفظ الملف المحدث.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
#### **إزالة النوافذ**
إزالة النوافذ المقسمة باستخدام الطريقة [RemoveSplit] (https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
