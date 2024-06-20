---
title: إدارة الضوابط
type: docs
weight: 150
url: /ar/net/managing-controls/
---

## **مقدمة**

يمكن للمطورين إضافة أجسام رسم مختلفة مثل صناديق النص، صناديق الاختيار، أزرار الراديو، صناديق الاختيار المتعدد، تسميات الأزرار، الخطوط، المستطيلات، الأقواس، البيضاويات، الدوارات، شرائط التمرير، صور المجموعات الخ. Aspose.Cells توفر مساحة اسم Aspose.Cells.Drawing التي تحتوي على جميع أجسام الرسم. ومع ذلك، هناك بعض أجسام الرسم أو الأشكال التي لم يتم دعمها بعد. أنشئ هذه الأجسام الرسم في ورقة عمل مصممة باستخدام Microsoft Excel ثم استوردها إلى Aspose.Cells. تتيح لك Aspose.Cells تحميل هذه الأجسام الرسم من ورقة عمل مصممة وكتابتها إلى ملف مولد.

## **إضافة مربع نص إلى ورقة العمل**

الطريقة الوحيدة لتوضيح المعلومات الهامة في تقرير هو استخدام صندوق نص. على سبيل المثال، إضافة نص لتسليط الضوء على اسم الشركة أو للإشارة إلى المنطقة الجغرافية التي تحقق أعلى مبيعات وما إلى ذلك. توفر Aspose.Cells الفئة [**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection)، المستخدمة لإضافة صندوق نص جديد إلى المجموعة. هناك فئة أخرى، [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)، التي تمثل صندوق نص يتم استخدامه لتحديد جميع أنواع الإعدادات. يحتوي على بعض الأعضاء الهامة:

- الخاصية [**TextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) تُرجع كائن [**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) يُستخدم لضبط محتويات صندوق النص.
- الخاصية [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) تُحدد نوع التوضع.
- الخاصية [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) تُحدد سمات الخط.
- الطريقة [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) تضيف ارتباطًا تشعبيًا لصندوق النص.
- الخاصية [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) ترجع كائن [**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) يُستخدم لتعيين تنسيق التعبئة لصندوق النص.
- تُعيد الخاصية [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) كائن [**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) المستخدم عادة لتنسيق ووزن خط مربع النص.
- الخاصية [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) تحدد النص الذي يُدخل في صندوق النص.

المثال التالي ينشئ مربعي نص في الورقة العمل الأولى من الدفتر. المربع النص الأول مؤثث جيدًا بإعدادات تنسيق مختلفة. الثاني بسيط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **التحكم في صندوقات النص في جداول البيانات المصممة**

تتيح Aspose.Cells أيضًا لك الوصول إلى مربعات النص في جداول البيانات المصممة والتلاعب بها. استخدم الخاصية [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) للحصول على مجموعة مربعات النص في الورقة.

يستخدم المثال التالي ملف Microsoft Excel الذي أنشأناه في المثال أعلاه. يحصل على سلاسل نصيّة لصندوقي النص ويغير نص الصندوق الثاني لحفظ الملف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **إضافة عنصر تحكم خانة اختيار إلى ورقة العمل**

تكون مربعات الاختيار مفيدة إذا كنت ترغب في توفير طريقة للمستخدم لاختيار بين خيارين، مثل صحيح أو خطأ؛ نعم أو لا. تسمح Aspose.Cells لك باستخدام مربعات الاختيار في جداول البيانات. على سبيل المثال، قد تكون قد وضعت ورقة عمل للتنبؤ المالي يمكنك فيها إما أن تأخذ في الاعتبار استحواذ معين أو لا. في هذه الحالة، قد ترغب في وضع مربع اختيار في أعلى الورقة. يمكنك بعد ذلك ربط حالة هذا المربع بخلية أخرى، بحيث إذا تم تحديده، يكون قيمة الخلية صحيحة؛ إذا لم يتم تحديده، تكون قيمة الخلية خاطئة.

### **استخدام Microsoft Excel**

لوضع تحكم مربع الاختيار في ورقة العمل الخاصة بك، اتبع هذه الخطوات:

1. تأكد من عرض شريط الأدوات النماذج.
1. انقر على أداة **مربع اختيار** في شريط الأدوات النماذج.
1. في منطقة ورقة العمل الخاصة بك، انقر واسحب لتحديد المستطيل الذي سيحتوي على مربع الاختيار والتسمية بجانب مربع الاختيار.
1. بمجرد وضع مربع الاختيار، قم بتحريك مؤشر الماوس إلى منطقة التسمية وقم بتغيير التسمية.
1. في حقل **رابط الخلية**، حدد عنوان الخلية التي يجب ربط مربع الاختيار بها.
1. انقر فوق **موافق**.

### **استخدام Aspose.Cells**

توفر Aspose.Cells الفئة [**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection) ، التي تُستخدم لإضافة مربع اختيار جديد إلى المجموعة. هناك فئة أخرى ، [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox) ، التي تمثل مربع اختيار. لديها بعض الأعضاء المهمين:

- تحدد خاصية [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) خلية مرتبطة بخانة الاختيار.
- تحدد خاصية [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) السلسلة النصية المرتبطة بخانة الاختيار. إنها تسمية خانة الاختيار.
- تحدد خاصية [**Value**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) ما إذا كانت خانة الاختيار محددة أم لا.

يوضح المثال التالي كيفية إضافة خانة اختيار إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

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

### **استخدام Aspose.Cells**

توفر الفئة [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) طريقة تسمى [**AddRadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton)، والتي تُستخدم لإضافة عنصر تحكم زر الراديو إلى ورقة عمل. تُرجع الطريقة كائنًا [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton). تمثل الفئة [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) زر اختيار. لها بعض الأعضاء الهامة:

- يُحدد خاصية [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) الخلية المرتبطة بزر الراديو.
- تُحدد خاصية [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) سلسلة النص المرتبطة بزر الراديو. إنها علامة زر الراديو.
- تُحدد خاصية [**IsChecked**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) ما إذا كان زر الراديو محددًا أم لا.
- تُحدد خاصية [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) تنسيق التعبئة لزر الراديو.
- تُحدد خاصية [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) أنماط تنسيق الخط لزر الخيار.

المثال التالي يوضح كيفية إضافة أزرار الراديو إلى ورقة العمل. يضيف المثال ثلاثة أزرار راديو تمثل مجموعات عمرية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

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

### **استخدام Aspose.Cells**

توفر فئة [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) طريقة تحمل اسم [**AddComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox)، والتي تُستخدم لإضافة عنصر تحكم مربع الجمع إلى ورقة العمل. تُعيد الطريقة كائن [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox). الفئة [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) تمثل مربع جمع. لديها بعض الأعضاء المهمة:

- يحدد الخاصية [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) خلية مرتبطة بمربع الجمع.
- تحدد الخاصية [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) نطاق ورقة العمل للخلايا المستخدمة لملء مربع الجمع.
- تحدد الخاصية [**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) عدد خطوط القائمة المعروضة في الجزء المنسدل لمربع الجمع.
- تُشير الخاصية [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) ما إذا كان مربع الجمع له تظليل ثلاثي الأبعاد.

المثال التالي يوضح كيفية إضافة مربع الجمع إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **إضافة عنصر تحكم تسمية إلى ورقة العمل**

التسميات هي وسيلة لتزويد المستخدمين بمعلومات حول محتويات جدول البيانات. يجعل Aspose.Cells من الممكن إضافة وتلاعب بالتسميات في ورقة العمل. توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) طريقة تحمل اسم [**AddLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel)، تستخدم لإضافة عنصر تحكم تسمية إلى ورقة العمل. تُعيد الطريقة كائن [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label). الفئة [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) تمثل تسمية في ورقة العمل. لديها بعض الأعضاء المهمة:

- تحدد الطريقة [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) سلسلة تسمية التسمية.
- تحدد الطريقة [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)، الطريقة التي يتم بها تثبيت التسمية على الخلايا في ورقة العمل.

المثال التالي يوضح كيفية إضافة تسمية إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

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

### **استخدام Aspose.Cells**

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) طريقة تُسمى [**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox)، والتي تُستخدم لإضافة عنصر تحكم مربع قائمة إلى ورقة العمل. تعيد الطريقة كائنًا [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox). تُمثل الفئة [**ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) مربع قائمة. لها بعض الأعضاء الهامة:

- تحدد الطريقة [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) خلية مقترنة بمربع القائمة.
- تحدد الطريقة [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) نطاق ورقة العمل للخلايا المستخدمة لملء مربع القائمة.
- تحدد الطريقة [**SelectionType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype) وضع تحديد مربع القائمة.
- تُشير الطريقة [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) ما إذا كان لمربع القائمة تظليل ثلاثي الأبعاد.

يوضح المثال التالي كيفية إضافة مربع قائمة إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **إضافة عنصر تحكم زر إلى ورقة العمل**

الأزرار مفيدة للقيام ببعض الإجراءات. في بعض الأحيان، من المفيد تعيين ماكرو VBA للزر أو تعيين ارتباط تشعبي لفتح صفحة ويب.

### **استخدام Microsoft Excel**

لوضع عنصر تحكم زر في ورقة العمل الخاصة بك:

1. تأكد من عرض شريط الأدوات **النماذج**.
1. انقر على أداة **الزر**.
1. في منطقة ورقة العمل الخاصة بك، انقر واسحب لتعريف المستطيل الذي سيحتوي على الزر.
1. بمجرد وضع مربع القائمة في ورقة العمل، انقر بزر الماوس الأيمن على العنصر التحكم واختر **تنسيق العنصر التحكم**، ثم حدد ماكرو VBA وسمات تتعلق بالخط، التوضيب، الحجم، الهامش وما إلى ذلك.
1. انقر فوق **موافق**.

### **استخدام Aspose.Cells**

الفئة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر طريقة تسمى [**AddButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton)، تستخدم لإضافة عنصر تحكم زر إلى ورقة العمل. تعيد الطريقة كائن [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button). الفئة [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) تمثل زرًا. لديها بعض الأعضاء الهامة:

- الخاصية [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) تحدد التسمية للزر.
- الخاصية [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) تحدد سمات الخط لتسمية عنصر تحكم الزر.
- الخاصية [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) تحدد [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)، الطريقة التي يتم بها ربط الزر بالخلايا في ورقة العمل.
- الخاصية [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) تضيف ارتباطًا تشعبيًا لعنصر تحكم الزر. بالنقر على الزر، سيتم التنقل إلى عنوان URL ذي الصلة.

المثال التالي يوضح كيفية إضافة زر إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **إضافة عنصر تحكم الخط إلى ورقة العمل**

### **استخدام Microsoft Excel**

1. على شريط الأدوات **الرسم**، انقر على **أشكال تلقائية**, اشير إلى **الخطوط**, واختر نمط الخط الذي تريده.
1. اسحب لرسم الخط.
1. قم بإحدى الخطوتين أو كليهما:
   1. لتقييد رسم الخط لزوايا 15 درجة من نقطته الأولى، اضغط باستمرار على SHIFT أثناء السحب.
   1. لتمديد الخط في اتجاهين معاكسين من نقطة النهاية الأولى، اضغط باستمرار على CTRL أثناء السحب.

### **استخدام Aspose.Cells**

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) طريقة تسمى [**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)، التي تُستخدم لإضافة شكل خط إلى ورقة العمل. تعيد الطريقة كائن [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape). الفئة [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) تمثل خطًا. لديها بعض الأعضاء الهامة:

- تحدد الطريقة [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) تنسيق الخط.
- تحدد الطريقة [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) الـ [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)، الطريقة التي يتم بها ربط الخط بالخلايا في ورقة العمل.

توضح الأمثلة التالية كيفية إضافة خطوط إلى ورقة العمل. يتم إنشاء ثلاث خطوط بأنماط مختلفة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **إضافة رأس سهم إلى خط**

تسمح Aspose.Cells أيضًا برسم خطوط سهم. من الممكن إضافة رأس سهم إلى خط وتنسيق الخط. على سبيل المثال، يمكنك تغيير لون الخط أو تحديد وزن ونمط الخط.

توضح الأمثلة التالية كيفية إضافة رأس سهم إلى خط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **إضافة تحكم مستطيل إلى ورقة عمل**

تسمح Aspose.Cells لك برسم أشكال مستطيلة في ورقة عملك. قد تقوم بإنشاء مستطيل، مربع وما إلى ذلك. كما يُسمح لك بتنسيق لون الملء ولون خط الحدود للتحكم. على سبيل المثال، يمكنك تغيير لون المستطيل، تحديد لون التظليل، تحديد وزن ونمط المستطيل حسب احتياجاتك.

### **استخدام Microsoft Excel**

1. في شريط الرسم، انقر فوق **المستطيل**.
1. اسحب لرسم المستطيل.
1. قم بإحدى الخطوتين أو كليهما:
   1. للقيد في رسم المستطيل لرسم مربع من نقطته البداية، اضغط باستمرار على SHIFT أثناء السحب.
   1. لرسم مستطيل من نقطة مركزية، اضغط باستمرار على CTRL أثناء السحب.

### **استخدام Aspose.Cells**

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) طريقة تسمى [**AddRectangle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)، التي تُستخدم لإضافة شكل مستطيل إلى ورقة عمل. تعيد الطريقة كائن [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape). الفئة [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) تمثل مستطيلًا. لديها بعض الأعضاء الهامة:

- يحدد الخاصية [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) سمات تنسيق الخط لمستطيل.
- يحدد الخاصية [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) الـ [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)، الطريقة التي يتم بها ربط المستطيل بالخلايا في ورقة العمل.
- الخاصية [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) تحدد أساليب تنسيق التعبئة الخاصة بمستطيل.

المثال التالي يظهر كيفية إضافة مستطيل إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **إضافة تحكم بالقوس إلى ورقة العمل**

تسمح Aspose.Cells لك برسم أشكال القوس في ورقة العمل الخاصة بك. يمكنك إنشاء أقواس بسيطة وممتلئة. يُسمح لك بتنسيق لون التعبئة ولون الخط الحدودي للتحكم. على سبيل المثال، يمكنك تحديد / تغيير لون القوس، تحديد لون الظلال، تحديد الوزن والنمط للشكل حسب احتياجك.

### **استخدام Microsoft Excel**

1. على شريط الأدوات **الرسم**، انقر على **القوس** في **الأشكال التلقائية**.
1. اسحب لرسم القوس.

### **استخدام Aspose.Cells**

توفر الفئة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) طريقة بعنوان [**AddArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc)، والتي تُستخدم لإضافة شكل قوس إلى ورقة عمل. تُرجع الطريقة كائنًا من النوع [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape). تُمثل الفئة [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) قوسًا. ولها بعض الأعضاء المهمة:

- الخاصية [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) تحدد سمات تنسيق الخط الخاصة بشكل القوس.
- الخاصية [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) تحدد [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)، الطريقة التي يتم بها إرفاق القوس بالخلايا في ورقة العمل.
- خاصية [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) تحدد أنماط تنسيق التعبئة للشكل.
- تحدد خاصية [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) مؤشر الصف الأيمن الأدنى.
- تحدد خاصية [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) مؤشر العمود الأيمن الأدنى.

المثال التالي يظهر كيفية إضافة أشكال قوسية إلى ورقة العمل. ينشئ المثال شكلين قوسيين: أحدهما ممتلئ والآخر بسيط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **إضافة تحكم بالشكل البيضوي إلى ورقة عمل**

تسمح Aspose.Cells لك برسم أشكال بيضوية في ورقات العمل. يمكنك إنشاء أشكال بيضوية بسيطة وممتلئة وتنسيق لون التعبئة ولون الخط الحدودي للتحكم. على سبيل المثال، يمكنك تحديد / تغيير لون الشكل البيضوي، تحديد لون الظلال، تحديد الوزن والنمط للشكل حسب احتياجك.

### **استخدام Microsoft Excel**

- على شريط الأدوات *الرسم*، انقر على *البيضوي*.
- اسحب لرسم البيضوي.
- قم بأحد أو كل من الآتي:
- لتقييد الشكل البيضاوي لرسم دائرة من نقطته البدء، اضغط على مفتاح SHIFT أثناء سحبه.
- لرسم شكل بيضاوي من نقطة مركزية، اضغط على CTRL أثناء سحبه.

### **استخدام Aspose.Cells**

تقدم فئة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) طريقة تسمى [**AddOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval)، التي تُستخدم لإضافة شكل بيضوي إلى ورقة العمل. تُرجع الطريقة كائن [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval). الفئة [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) تمثل شكل بيضوي. لها بعض الأعضاء الهامة:

- تحدد خاصية [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) سمات تنسيق الخط لشكل بيضوي.
- خاصية [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) تحدد [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)، الطريقة التي يتم فيها تعلق الشكل البيضاوي بالخلايا في ورقة العمل.
- خاصية [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) تحدد أنماط تنسيق التعبئة للشكل.
- تحدد خاصية [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) مؤشر الصف الأيمن الأدنى.
- تحدد خاصية [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) مؤشر العمود الأيمن الأدنى.

المثال التالي يوضح كيفية إضافة أشكال بيضوية إلى ورقة العمل. ينشئ المثال شكلين بيضويين: أحدهما ممتلئ والآخر هو دائرة بسيطة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **إضافة عنصر تحكم Spinner إلى ورقة العمل**

مربع الدوران هو مربع نص مرتبط بزر (يسمى زر دوران) يتكون من سهمين لأعلى ولأسفل تنقر فوقهما لتغيير القيمة بشكل تدريجي في مربع النص. يمكنك من خلال استخدام مربعات الدوران أن ترى كيف تؤثر التغييرات في المدخلات على نموذجك المالي على إخراج النموذج. يمكنك ربط زر دوران بخلية مدخل معينة. أثناء النقر على زر الصعود أو النزول على زر الفاصل الزمني، تزداد قيمة العدد الصحيح في الخلية المدخل المستهدفة أو تنقص. *Aspose.Cells* يتيح لك إنشاء مربعات دوران في أوراق العمل الخاصة بك.

### **استخدام Microsoft Excel**

لوضع عنصر تحكم مربع الدوران في ورقة العمل الخاصة بك:

- تأكد من عرض شريط الأدوات *النماذج*.
- انقر فوق أداة *Spinner*.
- في منطقة ورقة العمل، انقر واسحب لتحديد المستطيل الذي سيحتوي على عنصر التحكم.
- بمجرد وضع عنصر التحكم في ورقة العمل، انقر بزر الفأرة الأيمن على العنصر التحكم وانقر على *تنسيق التحكم* وحدد القيم القصوى والصغرى والقيم التزايدية.
- في حقل *ارتباط الخلية*، حدد عنوان الخلية التي يجب أن يكون مربع الدوران مرتبط بها.
- انقر فوق *موافق*.

### **استخدام Aspose.Cells**

فئة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) تُوفر طريقة تسمى [**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner)، والتي تُستخدم لإضافة عنصر تحكم مربع دوراني إلى ورقة العمل. تُرجِع الطريقة كائن [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner). الفئة [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) تمثل مربع دوراني. لديها بعض الأعضاء الهامة:

- يحدد الخاصية [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) الخلية المرتبطة بمربع الدوران.
- يحدد الخاصية [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) القيمة القصوى لنطاق مربع الدوران.
- يحدد الخاصية [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) القيمة الدنيا لنطاق مربع الدوران.
- يحدد الخاصية [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) كمية القيمة التي يتم زيادتها عند التمرير بخطوة واحدة.
- تشير الخاصية [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) ما إذا كان مربع الدوران يحتوي على تظليل ثلاثي الأبعاد.
- يحدد الخاصية [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) القيمة الحالية لمربع الدوران.

المثال التالي يوضح كيفية إضافة مربع دوراني إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

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

### **استخدام Aspose.Cells**

يوفر الفصيلة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) طريقة تُدعى [**AddScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar)، والتي تُستخدم لإضافة تحكم شريط التمرير إلى ورقة العمل. تُرجع الطريقة كائن [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar). الفصيلة [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) تُمثل تحكم شريط التمرير. لها بعض الأعضاء المهمة:

- تحدد الخاصية [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) الخلية المرتبطة بشريط التمرير.
- تحدد الخاصية [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) القيمة القصوى لنطاق شريط التمرير.
- تحدد الخاصية [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) القيمة الدنيا لنطاق شريط التمرير.
- تحدد الخاصية [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) مقدار القيمة الذي يتم به زيادة شريط التمرير بتمريرة.
- توضح الخاصية [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) ما إذا كان لشريط التمرير تظليل ثلاثي الأبعاد أم لا.
- تحدد الخاصية [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) القيمة الحالية لشريط التمرير.
- تحدد الخاصية [**PageChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange) مقدار زيادة القيمة الحالية إذا نقرت داخل شريط التمرير على أي جانب من جوانب المربع التمرير.

المثال التالي يظهر كيفية إضافة شريط تمرير إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

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

### **استخدام Aspose.Cells**

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) الأسلوب المسمى [**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox)، والذي يُستخدم لإضافة عنصر تحكم مربع تجميع إلى ورقة العمل. يُرجع الأسلوب كائن [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox). علاوة على ذلك، فإن الأسلوب [**Group**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) لفئة [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) يجمع بين الأشكال، حيث يأخذ مصفوفة [**Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) كمعلمة ويُرجع كائن [**GroupShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape). تمثل الفئة [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) مربع تجميع. تحتوي على بعض الأعضاء المهمة:

- تحدد الخاصية [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) سلسة تسمية مربع التجميع.
- تشير الخاصية [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) ما إذا كان مربع التجميع لديه تظليل ثلاثي الأبعاد.

المثال التالي يُظهر كيفية إضافة مربع تجميع وتجميع عناصر التحكم في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **مواضيع متقدمة**
- [إضافة عناصر تحكم ActiveX باستخدام Aspose.Cells](/cells/ar/net/add-activex-controls-using-aspose-cells/)
- [إزالة عنصر تحكم ActiveX](/cells/ar/net/remove-activex-control/)
- [تحديث عنصر تحكم ActiveX ComboBox](/cells/ar/net/update-activex-combobox-control/)
