---
title: إدارة الضوابط
type: docs
weight: 150
url: /ar/python-net/managing-controls/
---

## **مقدمة**

يمكن للمطورين إضافة أشكال رسومية مختلفة مثل مربعات النص، مربعات الاختيار، أزرار الراديو، مربعات الاختيار، التسميات، الأزرار، الخطوط، المستطيلات، الأقواس، الدوائر، المفاتيح الدوارة، أشرطة التمرير، صناديق المجموعة، وغيرها. توفر Aspose.Cells لـ بايثون via .NET مساحة أسماء Aspose.Cells.Drawing التي تحتوي على جميع الأشكال الرسومية. ومع ذلك، هناك عدد قليل من الأشكال غير المدعومة بعد. قم بإنشاء هذه الأشكال في جدول تصميم باستخدام Microsoft Excel ثم استورد جدول التصميم إلى Aspose.Cells. تتيح لك Aspose.Cells لـ بايثون via .NET تحميل هذه الأشكال من جدول التصميم وكتابتها إلى ملف تم إنشاؤه.

## **إضافة مربع نص إلى ورقة العمل**

إحدى الطرق لإبراز المعلومات المهمة في تقرير هو استخدام مربع نص. على سبيل المثال، إضافة نص لتسليط الضوء على اسم الشركة أو للإشارة إلى المنطقة الجغرافية ذات أعلى مبيعات، وغيرها. توفر Aspose.Cells لـ بايثون via .NET الفئة [**TextBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textboxcollection)، المستخدمة لإضافة مربع نص جديد إلى المجموعة. هناك فئة أخرى، [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox)، تمثل مربع النص المستخدم لتعريف جميع أنواع الإعدادات. تحتوي على بعض الأعضاء المهمة:

- الخاصية [**text_frame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_frame) تُرجع كائن [**MsoTextFrame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msotextframe) يُستخدم لضبط محتويات صندوق النص.
- الخاصية [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) تُحدد نوع التوضع.
- الخاصية [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) تُحدد سمات الخط.
- الطريقة [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) تضيف ارتباطًا تشعبيًا لصندوق النص.
- الخاصية [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) ترجع كائن [**MsoFillFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msofillformat) يُستخدم لتعيين تنسيق التعبئة لصندوق النص.
- تُعيد الخاصية [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) كائن [**MsoLineFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msolineformat) المستخدم عادة لتنسيق ووزن خط مربع النص.
- الخاصية [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) تحدد النص الذي يُدخل في صندوق النص.

المثال التالي ينشئ مربعي نص في الورقة العمل الأولى من الدفتر. المربع النص الأول مؤثث جيدًا بإعدادات تنسيق مختلفة. الثاني بسيط.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingTextBoxControl-1.py" >}}

## **التحكم في صندوقات النص في جداول البيانات المصممة**

يمكنك أيضًا باستخدام Aspose.Cells لـ بايثون via .NET الوصول إلى مربعات النص في أوراق العمل المصممة والتعديل عليها. استخدم الخاصية [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/text_boxes) للحصول على مجموعة مربعات النص في الورقة.

يستخدم المثال التالي ملف Microsoft Excel الذي أنشأناه في المثال أعلاه. يحصل على سلاسل نصيّة لصندوقي النص ويغير نص الصندوق الثاني لحفظ الملف.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-ManipulatingTextBoxControls-1.py" >}}

## **إضافة عنصر تحكم خانة اختيار إلى ورقة العمل**

مربعات الاختيار مفيدة إذا كنت تريد توفير طريقة لمستخدم لاختيار بين خيارين، مثل صواب أو خطأ؛ نعم أم لا. تتيح لك Aspose.Cells لـ بايثون via .NET استخدام مربعات الاختيار في أوراق العمل. على سبيل المثال، ربما تكون قد أعددت ورقة توقعات مالية والتي يمكنك فيها إما حساب عملية استحواذ معينة أو عدمها. في هذه الحالة، قد ترغب في وضع مربع اختيار في أعلى ورقة العمل. يمكنك ربط حالة مربع الاختيار بخلية أخرى، بحيث إذا تم تحديد مربع الاختيار، تكون قيمة الخلية True؛ وإذا لم يتم تحديده، تكون قيمة الخلية False.

### **استخدام Microsoft Excel**

لوضع تحكم مربع الاختيار في ورقة العمل الخاصة بك، اتبع هذه الخطوات:

1. تأكد من عرض شريط الأدوات النماذج.
1. انقر على أداة **مربع اختيار** في شريط الأدوات النماذج.
1. في منطقة ورقة العمل الخاصة بك، انقر واسحب لتحديد المستطيل الذي سيحتوي على مربع الاختيار والتسمية بجانب مربع الاختيار.
1. بمجرد وضع مربع الاختيار، قم بتحريك مؤشر الماوس إلى منطقة التسمية وقم بتغيير التسمية.
1. في حقل **رابط الخلية**، حدد عنوان الخلية التي يجب ربط مربع الاختيار بها.
1. انقر فوق **موافق**.

### **باستخدام Aspose.Cells لبايثون via .NET**

يقدم Aspose.Cells for Python via .NET فئة [**CheckBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkboxcollection)، التي تُستخدم لإضافة مربع اختيار جديد إلى المجموعة. هناك فئة أخرى، [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox)، والتي تمثل مربع اختيار. لديها بعض الأعضاء المهمة:

- تحدد خاصية [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) خلية مرتبطة بخانة الاختيار.
- تحدد خاصية [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) السلسلة النصية المرتبطة بخانة الاختيار. إنها تسمية خانة الاختيار.
- تحدد خاصية [**value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox/value) ما إذا كانت خانة الاختيار محددة أم لا.

يوضح المثال التالي كيفية إضافة خانة اختيار إلى ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingCheckBoxControl-1.py" >}}

## **إضافة عنصر تحكم زر الراديو إلى ورقة العمل**

زر الراديو أو زر الخيار هو عنصر تحكم مكون من صندوق مستدير. يقوم المستخدم باتخاذ قراره عن طريق تحديد مربع المستدير. يتم عادةً ، إذا لم يكن دائمًا ، خيار زر الراديو مصحوبًا بآخرين. يظهر زر الراديو ويتصرف كمجموعة. يقرر المستخدم أي زر صالح عن طريق تحديد واحد فقط منها. عندما ينقر المستخدم على زر واحد ، يتم ملؤه. عند تحديد زر واحد في المجموعة ، تكون أزرار نفس المجموعة فارغة.

### **استخدام Microsoft Excel**

لوضع عنصر تحكم زر الراديو في ورقتك العمل ، اتبع هذه الخطوات:

1. تأكد من عرض شريط الأدوات **النماذج**.
1. انقر على أداة **Button الخيار**.
1. في ورقة العمل ، انقر واسحب لتحديد المستطيل الذي سيحتوي على زر الخيار والتسمية بجانب زر الخيار.
1. بمجرد وضع زر الراديو في ورقة العمل ، قم بتحريك مؤشر الماوس إلى منطقة التسمية وقم بتغيير التسمية.
1. في حقل **رابط الخلية** ، حدد عنوان الخلية التي يجب أن يكون مرتبطًا بها زر الراديو هذا.
1. انقر على **موافق**.

### **باستخدام Aspose.Cells لبايثون via .NET**

توفر الفئة [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) طريقة تسمى [**add_radio_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_radio_button)، والتي تُستخدم لإضافة عنصر تحكم زر الراديو إلى ورقة عمل. تُرجع الطريقة كائنًا [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton). تمثل الفئة [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton) زر اختيار. لها بعض الأعضاء الهامة:

- يُحدد خاصية [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) الخلية المرتبطة بزر الراديو.
- تُحدد خاصية [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) سلسلة النص المرتبطة بزر الراديو. إنها علامة زر الراديو.
- تُحدد خاصية [**is_checked**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton/is_checked) ما إذا كان زر الراديو محددًا أم لا.
- تُحدد خاصية [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) تنسيق التعبئة لزر الراديو.
- تُحدد خاصية [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) أنماط تنسيق الخط لزر الخيار.

المثال التالي يوضح كيفية إضافة أزرار الراديو إلى ورقة العمل. يضيف المثال ثلاثة أزرار راديو تمثل مجموعات عمرية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRadioButtonControl-1.py" >}}

## **إضافة عنصر تحكم مربع القائمة المنسدلة إلى ورقة العمل**

لتسهيل إدخال البيانات، أو لتقييد الإدخالات إلى بعض العناصر التي تعرفها، يمكنك إنشاء مربع قائمة منسدلة، أو قائمة منسدلة للإدخالات الصحيحة التي تتم تجميعها من خلايا في مكان آخر على ورقة العمل. عند إنشاء قائمة منسدلة لخلية، تظهر سهم بجانب تلك الخلية. لإدخال معلومات في تلك الخلية، انقر على السهم، ثم انقر على الإدخال الذي تريده.

### **استخدام Microsoft Excel**

لوضع عنصر تحكم مربع الجمع في ورقة العمل الخاصة بك، اتبع هذه الخطوات:

1. تأكد من عرض شريط الأدوات **النماذج**.
1. انقر على أداة **مربع الجمع**.
1. في منطقة ورقة العمل الخاصة بك، انقر واسحب لتعريف المستطيل الذي سيحمل مربع الجمع.
1. بمجرد أن يتم وضع مربع الجمع في ورقة العمل، انقر بزر الماوس الأيمن على عنصر التحكم ثم انقر على **تنسيق التحكم** وحدد نطاق الإدخال.
1. في حقل **ارتباط الخلية**، حدد عنوان الخلية التي يجب ربطها بهذا مربع الجمع.
1. انقر فوق **موافق**.

### **باستخدام Aspose.Cells لبايثون via .NET**

توفر فئة [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) طريقة تحمل اسم [**add_combo_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_combo_box)، والتي تُستخدم لإضافة عنصر تحكم مربع الجمع إلى ورقة العمل. تُعيد الطريقة كائن [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox). الفئة [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) تمثل مربع جمع. لديها بعض الأعضاء المهمة:

- يحدد الخاصية [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) خلية مرتبطة بمربع الجمع.
- تحدد الخاصية [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) نطاق ورقة العمل للخلايا المستخدمة لملء مربع الجمع.
- تحدد الخاصية [**drop_down_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/drop_down_lines) عدد خطوط القائمة المعروضة في الجزء المنسدل لمربع الجمع.
- تُشير الخاصية [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/shadow) ما إذا كان مربع الجمع له تظليل ثلاثي الأبعاد.

المثال التالي يوضح كيفية إضافة مربع الجمع إلى ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingComboBoxControl-1.py" >}}

## **إضافة عنصر تحكم تسمية إلى ورقة العمل**

التسميات هي وسيلة لإعطاء المستخدمين معلومات عن محتويات جدول البيانات. يتيح لك Aspose.Cells for Python via .NET إضافة وتعديل التسميات في ورقة العمل. توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) طريقة تسمى [**add_label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label)، تُستخدم لإضافة عنصر تحكم تصنيف إلى ورقة العمل. ترجع الطريقة كائن [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label). تمثل فئة [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) تصنيفًا في ورقة العمل. لديها بعض الأعضاء المهمة:

- تحدد الطريقة [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) سلسلة تسمية التسمية.
- تحدد الطريقة [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)، الطريقة التي يتم بها تثبيت التسمية على الخلايا في ورقة العمل.

المثال التالي يوضح كيفية إضافة تسمية إلى ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLabelControl-1.py" >}}

## **إضافة عنصر تحكم مربع القائمة إلى ورقة العمل**

ينشئ عنصر تحكم مربع القائمة عنصر تحكم يسمح باختيار عنصر واحد أو عدة عناصر.

### **استخدام Microsoft Excel**

لوضع عنصر تحكم مربع القائمة في ورقة العمل:

1. تأكد من عرض شريط الأدوات **النماذج**.
1. انقر على أداة **مربع القائمة**.
1. في منطقة ورقة العمل الخاصة بك، انقر واسحب لتعريف المستطيل الذي سيحتوي على مربع القائمة.
1. بمجرد وضع مربع القائمة في ورقة العمل، انقر بزر الماوس الأيمن على العنصر التحكم للنقر فوق **تنسيق العنصر التحكم** وتحديد نطاق الإدخال.
1. في حقل **رابط الخلية**، حدد عنوان الخلية التي يجب أن يكون مربع القائمة مرتبطًا بها وتعيين نوع الاختيار (فردي، متعدد، توسيع) السمة
1. انقر على **موافق**.

### **باستخدام Aspose.Cells لبايثون via .NET**

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) طريقة تُسمى [**add_list_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_list_box)، والتي تُستخدم لإضافة عنصر تحكم مربع قائمة إلى ورقة العمل. تعيد الطريقة كائنًا [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox). تُمثل الفئة [**ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox) مربع قائمة. لها بعض الأعضاء الهامة:

- تحدد الطريقة [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) خلية مقترنة بمربع القائمة.
- تحدد الطريقة [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) نطاق ورقة العمل للخلايا المستخدمة لملء مربع القائمة.
- تحدد الطريقة [**selection_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/selection_type) وضع تحديد مربع القائمة.
- تُشير الطريقة [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/shadow) ما إذا كان لمربع القائمة تظليل ثلاثي الأبعاد.

يوضح المثال التالي كيفية إضافة مربع قائمة إلى ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingListBoxControl-1.py" >}}

## **إضافة عنصر تحكم زر إلى ورقة العمل**

الأزرار مفيدة للقيام ببعض الإجراءات. في بعض الأحيان، من المفيد تعيين ماكرو VBA للزر أو تعيين ارتباط تشعبي لفتح صفحة ويب.

### **استخدام Microsoft Excel**

لوضع عنصر تحكم زر في ورقة العمل الخاصة بك:

1. تأكد من عرض شريط الأدوات **النماذج**.
1. انقر على أداة **الزر**.
1. في منطقة ورقة العمل الخاصة بك، انقر واسحب لتعريف المستطيل الذي سيحتوي على الزر.
1. بمجرد وضع مربع القائمة في ورقة العمل، انقر بزر الماوس الأيمن على العنصر التحكم واختر **تنسيق العنصر التحكم**، ثم حدد ماكرو VBA وسمات تتعلق بالخط، التوضيب، الحجم، الهامش وما إلى ذلك.
1. انقر فوق **موافق**.

### **باستخدام Aspose.Cells لبايثون via .NET**

الفئة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) توفر طريقة تسمى [**add_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_button)، تستخدم لإضافة عنصر تحكم زر إلى ورقة العمل. تعيد الطريقة كائن [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button). الفئة [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button) تمثل زرًا. لديها بعض الأعضاء الهامة:

- الخاصية [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) تحدد التسمية للزر.
- الخاصية [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) تحدد سمات الخط لتسمية عنصر تحكم الزر.
- الخاصية [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) تحدد [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)، الطريقة التي يتم بها ربط الزر بالخلايا في ورقة العمل.
- الخاصية [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) تضيف ارتباطًا تشعبيًا لعنصر تحكم الزر. بالنقر على الزر، سيتم التنقل إلى عنوان URL ذي الصلة.

المثال التالي يوضح كيفية إضافة زر إلى ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingButtonControl-1.py" >}}

## **إضافة عنصر تحكم الخط إلى ورقة العمل**

### **استخدام Microsoft Excel**

1. على شريط الأدوات **الرسم**، انقر على **أشكال تلقائية**, اشير إلى **الخطوط**, واختر نمط الخط الذي تريده.
1. اسحب لرسم الخط.
1. قم بإحدى الخطوتين أو كليهما:
   1. لتقييد رسم الخط لزوايا 15 درجة من نقطته الأولى، اضغط باستمرار على SHIFT أثناء السحب.
   1. لتمديد الخط في اتجاهين معاكسين من نقطة النهاية الأولى، اضغط باستمرار على CTRL أثناء السحب.

### **باستخدام Aspose.Cells لبايثون via .NET**

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) طريقة تسمى [**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line)، التي تُستخدم لإضافة شكل خط إلى ورقة العمل. تعيد الطريقة كائن [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape). الفئة [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) تمثل خطًا. لديها بعض الأعضاء الهامة:

- تحدد الطريقة [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) تنسيق الخط.
- تحدد الطريقة [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) الـ [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)، الطريقة التي يتم بها ربط الخط بالخلايا في ورقة العمل.

توضح الأمثلة التالية كيفية إضافة خطوط إلى ورقة العمل. يتم إنشاء ثلاث خطوط بأنماط مختلفة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLineControl-1.py" >}}

### **إضافة رأس سهم إلى خط**

يسمح لك Aspose.Cells for Python via .NET أيضًا برسم خطوط الأسهم. من الممكن إضافة رأس سهم على خط، وتنسيق الخط. على سبيل المثال، يمكنك تغيير لون الخط، أو تحديد وزن ونمط الخط.

توضح الأمثلة التالية كيفية إضافة رأس سهم إلى خط.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddinganArrowHead-1.py" >}}

## **إضافة تحكم مستطيل إلى ورقة عمل**

يسمح Aspose.Cells for Python via .NET برسم أشكال مستطيلة في أوراق العمل الخاصة بك. يمكنك إنشاء مستطيل، مربع، وما إلى ذلك. كما يُسمح لك بتنسيق لون التعبئة ولون خط الحد. على سبيل المثال، يمكنك تغيير لون المستطيل، وضبط لون التظليل، وتحديد وزن ونمط المستطيل حسب حاجتك.

### **استخدام Microsoft Excel**

1. في شريط الرسم، انقر فوق **المستطيل**.
1. اسحب لرسم المستطيل.
1. قم بإحدى الخطوتين أو كليهما:
   1. للقيد في رسم المستطيل لرسم مربع من نقطته البداية، اضغط باستمرار على SHIFT أثناء السحب.
   1. لرسم مستطيل من نقطة مركزية، اضغط باستمرار على CTRL أثناء السحب.

### **باستخدام Aspose.Cells لبايثون via .NET**

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) طريقة تسمى [**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle)، التي تُستخدم لإضافة شكل مستطيل إلى ورقة عمل. تعيد الطريقة كائن [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape). الفئة [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) تمثل مستطيلًا. لديها بعض الأعضاء الهامة:

- يحدد الخاصية [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) سمات تنسيق الخط لمستطيل.
- يحدد الخاصية [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) الـ [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)، الطريقة التي يتم بها ربط المستطيل بالخلايا في ورقة العمل.
- الخاصية [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) تحدد أساليب تنسيق التعبئة الخاصة بمستطيل.

المثال التالي يظهر كيفية إضافة مستطيل إلى ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRectangleControl-1.py" >}}

## **إضافة تحكم بالقوس إلى ورقة العمل**

يسمح Aspose.Cells for Python via .NET برسم أشكال قوس في أوراق العمل الخاصة بك. يمكنك إنشاء أقواس بسيطة ومملوءة. يُسمح لك بتنسيق لون التعبئة ولون خط الحد للتحكم. على سبيل المثال، يمكنك تحديد / تغيير لون القوس، وضبط لون التظليل، وتحديد وزن ونمط الشكل حسب حاجتك.

### **استخدام Microsoft Excel**

1. على شريط الأدوات **الرسم**، انقر على **القوس** في **الأشكال التلقائية**.
1. اسحب لرسم القوس.

### **باستخدام Aspose.Cells لبايثون via .NET**

توفر الفئة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) طريقة بعنوان [**add_arc**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_arc)، والتي تُستخدم لإضافة شكل قوس إلى ورقة عمل. تُرجع الطريقة كائنًا من النوع [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape). تُمثل الفئة [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape) قوسًا. ولها بعض الأعضاء المهمة:

- الخاصية [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) تحدد سمات تنسيق الخط الخاصة بشكل القوس.
- الخاصية [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) تحدد [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)، الطريقة التي يتم بها إرفاق القوس بالخلايا في ورقة العمل.
- خاصية [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) تحدد أنماط تنسيق التعبئة للشكل.
- تحدد خاصية [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) مؤشر الصف الأيمن الأدنى.
- تحدد خاصية [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) مؤشر العمود الأيمن الأدنى.

المثال التالي يظهر كيفية إضافة أشكال قوسية إلى ورقة العمل. ينشئ المثال شكلين قوسيين: أحدهما ممتلئ والآخر بسيط.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingArcControl-1.py" >}}

## **إضافة تحكم بالشكل البيضوي إلى ورقة عمل**

يسمح Aspose.Cells for Python via .NET برسم أشكال بيضاوية في أوراق العمل. إنشاء أشكال بيضاوية بسيطة ومملوءة وتنسيق لون التعبئة ولون خط الحد للتحكم. على سبيل المثال، يمكنك تحديد / تغيير لون الشكل البيضاوي، وضبط لون التظليل، وتحديد وزن ونمط الشكل حسب حاجتك.

### **استخدام Microsoft Excel**

- على شريط الأدوات *الرسم*، انقر على *البيضوي*.
- اسحب لرسم البيضوي.
- قم بأحد أو كل من الآتي:
- لتقييد الشكل البيضاوي لرسم دائرة من نقطته البدء، اضغط على مفتاح SHIFT أثناء سحبه.
- لرسم شكل بيضاوي من نقطة مركزية، اضغط على CTRL أثناء سحبه.

### **باستخدام Aspose.Cells لبايثون via .NET**

تقدم فئة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) طريقة تسمى [**add_oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_oval)، التي تُستخدم لإضافة شكل بيضوي إلى ورقة العمل. تُرجع الطريقة كائن [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval). الفئة [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval) تمثل شكل بيضوي. لها بعض الأعضاء الهامة:

- تحدد خاصية [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) سمات تنسيق الخط لشكل بيضوي.
- خاصية [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) تحدد [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)، الطريقة التي يتم فيها تعلق الشكل البيضاوي بالخلايا في ورقة العمل.
- خاصية [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) تحدد أنماط تنسيق التعبئة للشكل.
- تحدد خاصية [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) مؤشر الصف الأيمن الأدنى.
- تحدد خاصية [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) مؤشر العمود الأيمن الأدنى.

المثال التالي يوضح كيفية إضافة أشكال بيضوية إلى ورقة العمل. ينشئ المثال شكلين بيضويين: أحدهما ممتلئ والآخر هو دائرة بسيطة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingOvalControl-1.py" >}}

## **إضافة عنصر تحكم Spinner إلى ورقة العمل**

صندوق التدوير هو مربع نص مرتبط بزر (يسمى زر التدوير) يتكون من سهم لأعلى وسهم لأسفل يمكنك النقر عليه لتغيير القيمة تدريجيًا في مربع النص. باستخدام صناديق التدوير، يمكنك رؤية كيف ستؤثر تغييرات الإدخال على نموذجك المالي على مخرجات النموذج. يمكنك ربط زر التدوير بخلية إدخال معينة. أثناء النقر على السهم للأعلى أو لأسفل على زر التدوير، تزداد أو تتناقص القيمة الصحيحة في خلية الإدخال المستهدفة. *يسمح Aspose.Cells for Python via .NET* بإنشاء أزرار تدوير في أوراق العمل الخاصة بك.

### **استخدام Microsoft Excel**

لوضع عنصر تحكم مربع الدوران في ورقة العمل الخاصة بك:

- تأكد من عرض شريط الأدوات *النماذج*.
- انقر فوق أداة *Spinner*.
- في منطقة ورقة العمل، انقر واسحب لتحديد المستطيل الذي سيحتوي على عنصر التحكم.
- بمجرد وضع عنصر التحكم في ورقة العمل، انقر بزر الفأرة الأيمن على العنصر التحكم وانقر على *تنسيق التحكم* وحدد القيم القصوى والصغرى والقيم التزايدية.
- في حقل *ارتباط الخلية*، حدد عنوان الخلية التي يجب أن يكون مربع الدوران مرتبط بها.
- انقر فوق *موافق*.

### **باستخدام Aspose.Cells لبايثون via .NET**

فئة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) تُوفر طريقة تسمى [**add_spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_spinner)، والتي تُستخدم لإضافة عنصر تحكم مربع دوراني إلى ورقة العمل. تُرجِع الطريقة كائن [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner). الفئة [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner) تمثل مربع دوراني. لديها بعض الأعضاء الهامة:

- يحدد الخاصية [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) الخلية المرتبطة بمربع الدوران.
- يحدد الخاصية [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/max) القيمة القصوى لنطاق مربع الدوران.
- يحدد الخاصية [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/min) القيمة الدنيا لنطاق مربع الدوران.
- يحدد الخاصية [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/incremental_change) كمية القيمة التي يتم زيادتها عند التمرير بخطوة واحدة.
- تشير الخاصية [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/shadow) ما إذا كان مربع الدوران يحتوي على تظليل ثلاثي الأبعاد.
- يحدد الخاصية [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/current_value) القيمة الحالية لمربع الدوران.

المثال التالي يوضح كيفية إضافة مربع دوراني إلى ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingSpinnerControl-1.py" >}}

## **إضافة عنصر تحكم شريط التمرير إلى ورقة العمل**

يُستخدم عنصر التحكم بشريط التمرير لمساعدة في تحديد البيانات على ورقة العمل بشكل مماثل لعنصر تحكم مربع الدوران. من خلال إضافة العنصر التحكم إلى ورقة العمل وربطه بخلية، يكون من الممكن العودة بقيمة رقمية للموضع الحالي للعنصر التحكم.

### **استخدام Microsoft Excel**

- لإضافة شريط تمرير في Excel 2003 والإصدارات السابقة، انقر فوق زر *شريط التمرير* على شريط الأدوات *النماذج*، ثم أنشئ شريط تمرير يغطي الخلايا B2:B6 في الارتفاع ويكون بنسبة رُبع عرض العمود.
- لإضافة شريط تمرير في Excel 2007، انقر فوق علامة *المطور*، ثم انقر على *إدراج*، ومن ثم انقر على *شريط التمرير* في قسم عناصر النماذج.
- انقر بزر الماوس الأيمن على شريط التمرير، ومن ثم انقر فوق *تنسيق الضبط*.
- اكتب المعلومات التالية، وانقر فوق *موافق*:
  - في مربع القيمة الحالية، اكتب 1.
  - في مربع القيمة الدنيا، اكتب 1. يحدد هذا القيمة الحد الأقصى لشريط التمرير لأول عنصر في القائمة.
  - في مربع القيمة القصوى، اكتب 20. تُحدد هذه الرقم الحد الأقصى لعدد الإدخالات في القائمة.
  - في مربع التغيير التدريجي، اكتب 1. تحكم هذه القيمة في كم عدد الأرقام التي يزيد بها تحكم شريط التمرير القيمة الحالية.
  - في مربع تغيير الصفحة، اكتب 5. تحكم هذا الإدخال في مقدار زيادة القيمة الحالية إذا نقرت داخل شريط التمرير على أي جانب من جوانب المربع التمرير.
  - لوضع قيمة رقمية في الخلية G1 (تبعًا للعنصر المحدد في القائمة)، اكتب G1 في مربع الرابط الخلوي.
- انقر فوق أي خلية بحيث لا يتم تحديد شريط التمرير.

عندما تنقر فوق التحكم بتحريك لأعلى أو لأسفل على شريط التمرير، يتم تحديث الخلية G1 إلى الرقم الذي يشير إلى القيمة الحالية لشريط التمرير بالإضافة إلى أو ناقص تغيير التحكم التدريجي لشريط التمرير.

### **باستخدام Aspose.Cells لبايثون via .NET**

يوفر الفصيلة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) طريقة تُدعى [**add_scroll_bar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_scroll_bar)، والتي تُستخدم لإضافة تحكم شريط التمرير إلى ورقة العمل. تُرجع الطريقة كائن [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar). الفصيلة [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar) تُمثل تحكم شريط التمرير. لها بعض الأعضاء المهمة:

- تحدد الخاصية [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) الخلية المرتبطة بشريط التمرير.
- تحدد الخاصية [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/max) القيمة القصوى لنطاق شريط التمرير.
- تحدد الخاصية [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/min) القيمة الدنيا لنطاق شريط التمرير.
- تحدد الخاصية [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/incremental_change) مقدار القيمة الذي يتم به زيادة شريط التمرير بتمريرة.
- توضح الخاصية [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/shadow) ما إذا كان لشريط التمرير تظليل ثلاثي الأبعاد أم لا.
- تحدد الخاصية [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/current_value) القيمة الحالية لشريط التمرير.
- تحدد الخاصية [**page_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/page_change) مقدار زيادة القيمة الحالية إذا نقرت داخل شريط التمرير على أي جانب من جوانب المربع التمرير.

المثال التالي يظهر كيفية إضافة شريط تمرير إلى ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingScrollBarControl-1.py" >}}

## **إضافة تحكم مجموعة إلى تحكمات المجموعة في ورقة عمل**

في بعض الأحيان قد تحتاج إلى تنفيذ أزرار الراديو أو تحكمات أخرى تنتمي إلى مجموعة معينة، يمكنك تنفيذ ذلك من خلال تضمين إما مربع مجموعة أو تحكم مستطيل. يمكن لأي من هاتين الشكلين أن يكون محدد المجموعة. بعد إضافة أحد هاتين الشكلين، يمكنك بعد ذلك إضافة اثنين أو أكثر من أزرار الراديو أو أجهزة مجموعة أخرى.

### **استخدام Microsoft Excel**

لوضع تحكم مربع المجموعة في ورقة العمل الخاصة بك ووضع تحكمات فيه:

- لبدء النموذج، على القائمة الرئيسية، انقر فوق *عرض*، ثم *شرائط الأدوات*، ثم *نماذج*.
- في شريط الأدوات *النماذج*، انقر فوق *مربع التجميع* وارسم مستطيلًا على ورقة العمل.
- اكتب سلسلة تسمية للمربع.
- في شريط أدوات *النماذج*، انقر فوق *زر الاختيار* وانقر داخل *مربع التجميع* مباشرة تحت سلسلة التسمية.
- من شريط الأدوات *النماذج* مرة أخرى، انقر *زر الاختيار* وانقر داخل *مربع التجميع* تحت الزر الإشعاري الأول.
- مرة أخرى على شريط الأدوات *النماذج*، انقر فوق *زر الاختيار* وانقر داخل *مربع التجميع* تحت الزر الإشعاري السابق.

### **باستخدام Aspose.Cells لبايثون via .NET**

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) الأسلوب المسمى [**add_group_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_group_box)، والذي يُستخدم لإضافة عنصر تحكم مربع تجميع إلى ورقة العمل. يُرجع الأسلوب كائن [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox). علاوة على ذلك، فإن الأسلوب [**group**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/group) لفئة [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) يجمع بين الأشكال، حيث يأخذ مصفوفة [**Shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) كمعلمة ويُرجع كائن [**GroupShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape). تمثل الفئة [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox) مربع تجميع. تحتوي على بعض الأعضاء المهمة:

- تحدد الخاصية [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) سلسة تسمية مربع التجميع.
- تشير الخاصية [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox/shadow) ما إذا كان مربع التجميع لديه تظليل ثلاثي الأبعاد.

المثال التالي يُظهر كيفية إضافة مربع تجميع وتجميع عناصر التحكم في ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingGroupBoxControl-1.py" >}}

## **مواضيع متقدمة**
- [إضافة عناصر تحكم ActiveX](/cells/ar/python-net/add-activex-controls-using-aspose-cells/)
- [إزالة عنصر تحكم ActiveX](/cells/ar/python-net/remove-activex-control/)
- [تحديث عنصر تحكم ActiveX ComboBox](/cells/ar/python-net/update-activex-combobox-control/)
