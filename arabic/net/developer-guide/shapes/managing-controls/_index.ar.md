---
title: إدارة الضوابط
type: docs
weight: 150
url: /ar/net/managing-controls/
---
## **مقدمة**

يمكن للمطورين إضافة كائنات رسم مختلفة مثل مربعات النص وخانات الاختيار وأزرار الاختيار ومربعات التحرير والسرد والتسميات والأزرار والخطوط والمستطيلات والأقواس والأشكال البيضاوية وأشرطة التمرير ومربعات المجموعة وما إلى ذلك ، يوفر Aspose.Cells Aspose.Cells. كل الكائنات الرسومية. ومع ذلك ، هناك عدد قليل من الكائنات الرسومية أو الأشكال التي لم يتم دعمها بعد. قم بإنشاء هذه الكائنات الرسومية في جدول بيانات مصمم باستخدام Microsoft Excel ثم قم باستيراد جدول بيانات المصمم إلى Aspose.Cells. يسمح لك Aspose.Cells بتحميل هذه الكائنات الرسومية من جدول بيانات مصمم وكتابتها في ملف تم إنشاؤه.

## **إضافة عنصر تحكم مربع نص إلى ورقة عمل**

 تتمثل إحدى طرق التأكيد على المعلومات المهمة في التقرير في استخدام مربع نص. على سبيل المثال ، أضف نصًا لتمييز اسم الشركة أو للإشارة إلى المنطقة الجغرافية ذات أعلى مبيعات وما إلى ذلك. يوفر Aspose.Cells[**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection) فئة ، تستخدم لإضافة مربع نص جديد إلى المجموعة. هناك فئة أخرى ،[**مربع الكتابة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)، والذي يمثل مربع نص يستخدم لتحديد جميع أنواع الإعدادات. لها بعض الأعضاء المهمين:

-  ال[**TextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) إرجاع الممتلكات أ[**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) كائن يستخدم لضبط محتويات مربع النص.
-  ال[**تحديد مستوى**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) تحدد الخاصية نوع الموضع.
-  ال[**الخط**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) تحدد الخاصية سمات الخط.
-  ال[**إضافة ارتباط تشعبي**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) أسلوب يضيف ارتباط تشعبي لمربع النص.
-  ال[**ملء**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) إرجاع الممتلكات[**تنسيق MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) المستخدم لتعيين تنسيق التعبئة لمربع النص.
-  ال[**تنسيق الخط**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) خاصية إرجاع ال[**تنسيق MsoLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) عادةً ما يتم استخدام الكائن في نمط سطر مربع النص ووزنه.
-  ال[**نص**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) تحدد الخاصية نص الإدخال لمربع النص.

يقوم المثال التالي بإنشاء مربعين نصيين في ورقة العمل الأولى من المصنف. تم تجهيز مربع النص الأول جيدًا بإعدادات تنسيق مختلفة. والثاني بسيط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **معالجة عناصر تحكم مربع النص في جداول بيانات المصمم**

 يتيح لك Aspose.Cells أيضًا الوصول إلى مربعات النص في أوراق عمل المصمم ومعالجتها. استخدم ال[**ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) للحصول على مجموعة مربعات النص في الورقة.

يستخدم المثال التالي ملف Excel Microsoft الذي أنشأناه في المثال أعلاه. يحصل على السلاسل النصية لمربعي النص ويغير نص مربع النص الثاني لحفظ الملف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **إضافة عنصر تحكم خانة اختيار إلى ورقة عمل**

تكون خانات الاختيار سهلة الاستخدام إذا كنت تريد توفير طريقة للمستخدم للاختيار بين خيارين ، مثل صواب أو خطأ ؛ نعم ام لا. Aspose.Cells يسمح لك باستخدام مربعات الاختيار في أوراق العمل. على سبيل المثال ، ربما تكون قد طورت ورقة عمل الإسقاط المالي حيث يمكنك إما حساب عملية استحواذ معينة أم لا. في هذه الحالة ، قد ترغب في وضع خانة اختيار أعلى ورقة العمل. يمكنك بعد ذلك ربط حالة خانة الاختيار هذه بخلية أخرى ، بحيث إذا تم تحديد خانة الاختيار ، فإن قيمة الخلية هي True ؛ إذا لم يتم تحديدها ، فإن قيمة الخلية هي False.

### **باستخدام Microsoft إكسل**

لوضع عنصر تحكم خانة اختيار في ورقة العمل الخاصة بك ، اتبع الخطوات التالية:

1. تأكد من عرض شريط أدوات النماذج.
1.  انقر على**خانة اختيار** أداة على شريط أدوات النماذج.
1. في منطقة ورقة العمل الخاصة بك ، انقر واسحب لتحديد المستطيل الذي سيحتفظ بخانة الاختيار والتسمية بجانب خانة الاختيار.
1. بمجرد وضع مربع الاختيار ، حرك مؤشر الماوس إلى منطقة الملصق وقم بتغيير التسمية.
1.  في ال**Cell رابط**، حدد عنوان الخلية التي يجب ربط خانة الاختيار هذه بها.
1.  انقر فوق**نعم**.

### **باستخدام Aspose.Cells**

 يوفر Aspose.Cells ملف[**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection) class ، والتي تُستخدم لإضافة خانة اختيار جديدة إلى المجموعة. هناك فئة أخرى ،[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox)، والذي يمثل خانة اختيار. لها بعض الأعضاء المهمين:

-  ال[**لينكدسل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) تحدد الخاصية خلية مرتبطة بخانة الاختيار.
-  ال[**نص**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) تحدد الخاصية سلسلة النص المرتبطة بخانة الاختيار. إنها تسمية خانة الاختيار.
-  ال[**قيمة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) تحدد الخاصية ما إذا تم تحديد خانة الاختيار أم لا.

يوضح المثال التالي كيفية إضافة خانة اختيار إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **إضافة عنصر تحكم زر الراديو إلى ورقة العمل**

زر الاختيار ، أو زر الخيار ، هو عنصر تحكم مصنوع من صندوق دائري. يتخذ المستخدم قراره عن طريق تحديد المربع الدائري. عادة ما يكون زر الاختيار مصحوبًا بآخرين ، إن لم يكن دائمًا. تظهر أزرار الاختيار هذه وتتصرف كمجموعة. يقرر المستخدم أي زر يكون صالحًا عن طريق اختيار زر واحد فقط. عندما ينقر المستخدم على زر واحد ، يتم ملؤه. عند تحديد زر واحد في المجموعة ، تكون أزرار المجموعة نفسها فارغة.

### **باستخدام Microsoft إكسل**

لوضع عنصر تحكم زر راديو في ورقة العمل الخاصة بك ، اتبع الخطوات التالية:

1.  تأكد من أن**نماذج** يتم عرض شريط الأدوات.
1.  انقر على**زر الخيارات** أداة.
1. في ورقة العمل ، انقر واسحب لتحديد المستطيل الذي سيحتفظ بزر الخيار والتسمية بجانب زر الخيار.
1. بمجرد وضع زر الاختيار في ورقة العمل ، حرك مؤشر الماوس إلى منطقة التسمية وقم بتغيير التسمية.
1.  في ال**Cell رابط** ، حدد عنوان الخلية التي يجب أن يرتبط بها زر الاختيار هذا.
1.  انقر**نعم**.

### **باستخدام Aspose.Cells**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddRadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton) ، والتي تُستخدم لإضافة عنصر تحكم زر اختيار إلى ورقة العمل. تقوم الطريقة بإرجاع ملف[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) هدف. الطبقة[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) يمثل زر الخيار. لها بعض الأعضاء المهمين:

-  ال[**لينكدسل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) تحدد الخاصية خلية مرتبطة بزر الاختيار.
-  ال[**نص**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)تحدد الخاصية سلسلة النص المرتبطة بزر الاختيار. إنها تسمية زر الاختيار.
-  ال[**مفحوص**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) تحدد الخاصية ما إذا كان زر الاختيار محددًا أم لا.
-  ال[**ملء**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) تحدد الخاصية تنسيق تعبئة زر الاختيار.
-  ال[**تنسيق الخط**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) تحدد الخاصية أنماط تنسيق الخط لزر الخيار.

يوضح المثال التالي كيفية إضافة أزرار اختيار إلى ورقة عمل. يضيف المثال ثلاثة أزرار اختيار تمثل الفئات العمرية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

## **إضافة عنصر تحكم مربع التحرير والسرد إلى ورقة عمل**

لتسهيل إدخال البيانات ، أو لتقييد الإدخالات لعناصر معينة تحددها ، يمكنك إنشاء مربع تحرير وسرد أو قائمة منسدلة للإدخالات الصالحة التي تم تجميعها من خلايا في مكان آخر بورقة العمل. عند إنشاء قائمة منسدلة لخلية ، فإنها تعرض سهمًا بجوار تلك الخلية. لإدخال معلومات في تلك الخلية ، انقر فوق السهم ، ثم انقر فوق الإدخال الذي تريده.

### **باستخدام Microsoft إكسل**

لوضع عنصر تحكم مربع تحرير وسرد في ورقة العمل الخاصة بك ، اتبع الخطوات التالية:

1.  تأكد من أن**نماذج** يتم عرض شريط الأدوات.
1.  اضغط على**صندوق التحرير** أداة.
1. في منطقة ورقة العمل الخاصة بك ، انقر واسحب لتحديد المستطيل الذي سيحتوي على مربع التحرير والسرد.
1.  بمجرد وضع مربع التحرير والسرد في ورقة العمل ، انقر بزر الماوس الأيمن فوق عنصر التحكم للنقر**تنسيق التحكم** وحدد نطاق الإدخال.
1.  في ال**Cell رابط** ، حدد عنوان الخلية التي يجب ربط مربع التحرير والسرد بها.
1.  انقر فوق**نعم**.

### **باستخدام Aspose.Cells**

 ال[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) ، والذي يستخدم لإضافة عنصر تحكم مربع تحرير وسرد إلى ورقة عمل. تقوم الطريقة بإرجاع ملف[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) هدف. الطبقة[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) يمثل مربع التحرير والسرد. لها بعض الأعضاء المهمين:

-  ال[**لينكدسل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) تحدد الخاصية خلية مرتبطة بمربع التحرير والسرد.
-  ال[**نطاق الإدخال**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) تحدد الخاصية نطاق خلايا ورقة العمل المستخدمة لتعبئة مربع التحرير والسرد.
-  ال[**خطوط منسدلة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) تحدد الخاصية عدد أسطر القائمة المعروضة في الجزء المنسدل من مربع التحرير والسرد.
-  ال[**ظل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) تشير الخاصية إلى ما إذا كان مربع التحرير والسرد به تظليل ثلاثي الأبعاد.

يوضح المثال التالي كيفية إضافة مربع تحرير وسرد إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **إضافة عنصر تحكم التسمية إلى ورقة عمل**

 الملصقات هي وسيلة لمنح المستخدمين معلومات حول محتويات ورقة speadsheet. يتيح Aspose.Cells إضافة ومعالجة التسميات في ورقة العمل. ال[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel) ، تستخدم لإضافة عنصر تحكم تسمية إلى ورقة العمل. تقوم الطريقة بإرجاع ملف[**مُلصَق**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) هدف. الطبقة[**مُلصَق**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) يمثل تسمية في ورقة العمل. لها بعض الأعضاء المهمين:

-  ال[**نص**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) الأسلوب يحدد سلسلة التسمية التوضيحية.
-  ال[**تحديد مستوى**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) تحدد الطريقة[**نوع الموضع**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)، طريقة إرفاق التسمية بالخلايا في ورقة العمل.

يوضح المثال التالي كيفية إضافة تسمية إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

## **إضافة عنصر تحكم مربع قائمة إلى ورقة عمل**

ينشئ عنصر تحكم مربع القائمة عنصر تحكم قائمة يسمح بتحديد عنصر واحد أو عدة عناصر.

### **باستخدام Microsoft إكسل**

لوضع عنصر تحكم مربع قائمه في ورقه عمل:

1.  تأكد من أن**نماذج** يتم عرض شريط الأدوات.
1.  اضغط على**مربع القائمة** أداة.
1. في منطقة ورقة العمل الخاصة بك ، انقر واسحب لتحديد المستطيل الذي سيحتوي على مربع القائمة.
1.  بمجرد وضع مربع القائمة في ورقة العمل ، انقر بزر الماوس الأيمن فوق عنصر التحكم للنقر**تنسيق التحكم** وحدد نطاق الإدخال.
1.  في ال**Cell رابط**، حدد عنوان الخلية التي يجب ربط مربع القائمة هذا بها وقم بتعيين نوع التحديد (فردي ، متعدد ، ممتد)
1.  انقر**نعم**.

### **باستخدام Aspose.Cells**

 ال[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox) ، والذي يستخدم لإضافة عنصر تحكم مربع قائمة إلى ورقة عمل. تقوم الطريقة بإرجاع ملف[**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) هدف. الطبقة[**ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) يمثل مربع قائمة. لها بعض الأعضاء المهمين:

-  ال[**لينكدسل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) الطريقة تحدد خلية مرتبطة بمربع القائمة.
-  ال[**نطاق الإدخال**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) تحدد الطريقة نطاق خلايا ورقة العمل المستخدمة لملء مربع القائمة.
-  ال[**نوع الاختيار**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype)طريقة تحديد وضع التحديد لمربع القائمة.
-  ال[**ظل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) يشير الأسلوب إلى ما إذا كان مربع القائمة يحتوي على تظليل ثلاثي الأبعاد.

يوضح المثال التالي كيفية إضافة مربع قائمة إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **إضافة زر التحكم إلى ورقة عمل**

الأزرار مفيدة لأداء بعض الإجراءات. في بعض الأحيان ، يكون من المفيد تعيين VBA Macro للزر أو تعيين ارتباط تشعبي لفتح صفحة ويب.

### **باستخدام Microsoft إكسل**

لوضع عنصر تحكم زر في ورقة العمل الخاصة بك:

1.  تأكد من أن**نماذج** يتم عرض شريط الأدوات.
1.  اضغط على**زر** أداة.
1. في منطقة ورقة العمل الخاصة بك ، انقر واسحب لتحديد المستطيل الذي سيحتفظ بالزر.
1.  بمجرد وضع مربع القائمة في ورقة العمل ، انقر بزر الماوس الأيمن فوق عنصر التحكم وحدد**تنسيق التحكم**، ثم حدد VBA Macro والسمات ذات الصلة بالخط والمحاذاة والحجم والهامش وما إلى ذلك.
1.  انقر فوق**نعم**.

### **باستخدام Aspose.Cells**

 ال[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton) ، تستخدم لإضافة عنصر تحكم زر إلى ورقة العمل. تقوم الطريقة بإرجاع ملف[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) هدف. الطبقة[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) يمثل زر. لها بعض الأعضاء المهمين:

-  ال[**نص**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) تحدد الخاصية التسمية التوضيحية للزر.
-  ال[**الخط**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) تحدد الخاصية سمات الخط لتسمية عنصر تحكم الزر.
-  ال[**تحديد مستوى**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) تحدد الخاصية[**نوع الموضع**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)، طريقة إرفاق الزر بالخلايا في ورقة العمل.
-  ال[**إضافة ارتباط تشعبي**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) تضيف الخاصية ارتباطًا تشعبيًا لعنصر التحكم في الزر. سيؤدي النقر فوق الزر إلى الانتقال إلى عنوان URL ذي الصلة.

يوضح المثال التالي كيفية إضافة زر إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **إضافة عنصر تحكم الخط إلى ورقة العمل**

### **باستخدام Microsoft إكسل**

1.  على ال**رسم** شريط الأدوات ، انقر فوق**أشكال تلقائية** ، يشير إلى**خطوط**، وحدد نمط الخط الذي تريده.
1. اسحب لرسم الخط.
1. قم بأحد الإجراءين التاليين أو كليهما:
 1. لتقييد الخط بالرسم بزاوية 15 درجة من نقطة البداية ، اضغط باستمرار على المفتاح SHIFT أثناء السحب.
 1. لإطالة الخط في اتجاهين متعاكسين من نقطة النهاية الأولى ، اضغط باستمرار على CTRL أثناء السحب.

### **باستخدام Aspose.Cells**

 ال[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline) ، والتي تستخدم لإضافة شكل خط إلى ورقة العمل. طريقة إرجاع أ[**شكل خط**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) هدف. الطبقة[**شكل خط**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) يمثل خط. لها بعض الأعضاء المهمين:

-  ال[**تنسيق الخط**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) تحدد الطريقة تنسيق الخط.
-  ال[**تحديد مستوى**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) تحدد الطريقة[**نوع الموضع**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)، طريقة إرفاق الخط بالخلايا في ورقة العمل.

يوضح المثال التالي كيفية إضافة أسطر إلى ورقة العمل. يقوم بإنشاء ثلاثة خطوط بأنماط مختلفة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **إضافة رأس سهم إلى خط**

يسمح لك Aspose.Cells أيضًا برسم خطوط الأسهم. من الممكن إضافة رأس سهم إلى خط ، وتنسيق الخط. على سبيل المثال ، يمكنك تغيير لون الخط أو تحديد سمك الخط ونمطه.

يوضح المثال التالي كيفية إضافة رأس سهم إلى خط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **إضافة عنصر تحكم مستطيل إلى ورقة عمل**

يسمح لك Aspose.Cells برسم أشكال مستطيلة في أوراق العمل الخاصة بك. يمكنك إنشاء مستطيل أو مربع وما إلى ذلك. يُسمح لك أيضًا بتنسيق لون التعبئة ولون خط الحدود لعنصر التحكم. على سبيل المثال ، يمكنك تغيير لون المستطيل وتعيين لون التظليل وتحديد وزن المستطيل ونمطه حسب حاجتك.

### **باستخدام Microsoft إكسل**

1.  على ال**رسم** شريط الأدوات ، انقر فوق**مستطيل**.
1. اسحب لرسم المستطيل.
1. قم بأحد الإجراءين التاليين أو كليهما:
 1. لتقييد المستطيل برسم مربع من نقطة البداية ، اضغط باستمرار على المفتاح SHIFT أثناء السحب.
 1. لرسم مستطيل من نقطة مركزية ، اضغط باستمرار على CTRL أثناء السحب.

### **باستخدام Aspose.Cells**

 ال[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**إضافة مستطيل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle) ، والتي تستخدم لإضافة شكل مستطيل إلى ورقة العمل. طريقة إرجاع[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) هدف. الطبقة[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) يمثل مستطيلاً. لها بعض الأعضاء المهمين:

-  ال[**تنسيق الخط**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) تحدد الخاصية سمات تنسيق الخط للمستطيل.
-  ال[**تحديد مستوى**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) تحدد الخاصية[**نوع الموضع**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)، طريقة إرفاق المستطيل بالخلايا في ورقة العمل.
-  ال[**ملء**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) تحدد الخاصية أنماط تنسيق التعبئة لمستطيل.

يوضح المثال التالي كيفية إضافة مستطيل إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **إضافة عنصر تحكم القوس إلى ورقة العمل**

Aspose.Cells يسمح لك برسم أشكال قوس في أوراق العمل الخاصة بك. يمكنك إنشاء أقواس بسيطة ومليئة. يُسمح لك بتنسيق لون التعبئة ولون خط الحدود لعنصر التحكم. على سبيل المثال ، يمكنك تحديد / تغيير لون القوس ، وتعيين لون التظليل ، وتحديد وزن الشكل ونمطه حسب حاجتك.

### **باستخدام Microsoft إكسل**

1.  على ال**رسم** شريط الأدوات ، انقر فوق**قوس** في ال**أشكال تلقائية**.
1. اسحب لرسم القوس.

### **باستخدام Aspose.Cells**

 ال[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc) ، والتي تستخدم لإضافة شكل قوس إلى ورقة العمل. تقوم الطريقة بإرجاع ملف[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) هدف. الطبقة[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) يمثل القوس. لها بعض الأعضاء المهمين:

-  ال[**تنسيق الخط**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) تحدد الخاصية سمات تنسيق الخط لشكل القوس.
-  ال[**تحديد مستوى**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) تحدد الخاصية[**نوع الموضع**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)، الطريقة التي يتم بها ربط القوس بالخلايا في ورقة العمل.
-  ال[**ملء**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)تحدد الخاصية أنماط تنسيق التعبئة للشكل.
-  ال[**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) تحدد الخاصية فهرس صف الركن الأيمن السفلي.
-  ال[**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) تحدد الخاصية فهرس عمود الركن الأيمن السفلي.

يوضح المثال التالي كيفية إضافة أشكال قوس إلى ورقة العمل. ينشئ المثال شكلين قوسين: أحدهما ممتلئ والآخر بسيط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **إضافة تحكم بيضاوي إلى ورقة عمل**

Aspose.Cells يسمح لك برسم أشكال بيضاوية في أوراق العمل. قم بإنشاء أشكال بيضاوية بسيطة ومعبأة وقم بتنسيق لون التعبئة ولون خط الحدود لعنصر التحكم. على سبيل المثال ، يمكنك تحديد / تغيير لون الشكل البيضاوي ، وتعيين لون التظليل ، وتحديد وزن الشكل ونمطه.

### **باستخدام Microsoft إكسل**

-  على ال*رسم* شريط الأدوات ، انقر فوق*بيضاوي*.
- اسحب لرسم الشكل البيضاوي.
- قم بأحد الإجراءين التاليين أو كليهما:
- لتقييد الشكل البيضاوي لرسم دائرة من نقطة البداية ، اضغط باستمرار على المفتاح SHIFT أثناء السحب.
- لرسم شكل بيضاوي من نقطة مركزية ، اضغط باستمرار على CTRL أثناء السحب.

### **باستخدام Aspose.Cells**

 ال[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval) ، والتي تستخدم لإضافة شكل بيضاوي إلى ورقة العمل. تقوم الطريقة بإرجاع ملف[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) هدف. الطبقة[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) يمثل شكل بيضاوي. لها بعض الأعضاء المهمين:

-  ال[**تنسيق الخط**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) تحدد الخاصية سمات تنسيق الخط للشكل البيضاوي.
-  ال[**تحديد مستوى**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) تحدد الخاصية[**نوع الموضع**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)، طريقة إرفاق الشكل البيضاوي بالخلايا في ورقة العمل.
-  ال[**ملء**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)تحدد الخاصية أنماط تنسيق التعبئة للشكل.
-  ال[**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) تحدد الخاصية فهرس صف الركن الأيمن السفلي.
-  ال[**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) تحدد الخاصية فهرس عمود الركن الأيمن السفلي.

يوضح المثال التالي كيفية إضافة أشكال بيضاوية إلى ورقة العمل. ينشئ المثال شكلين بيضاويين: أحدهما مملوء بشكل بيضاوي والآخر عبارة عن دائرة بسيطة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **إضافة عنصر تحكم Spinner إلى ورقة العمل**

 مربع الزيادة والنقصان هو مربع نص مرفق بزر (يسمى زر زيادة ونقصان) يتكون من سهم لأعلى وسهم لأسفل تنقر فوقه لتغيير القيمة في مربع النص بشكل تدريجي. باستخدام مربعات الدوران ، يمكنك أن ترى كيف ستؤدي تغييرات المدخلات في نموذجك المالي إلى تغيير مخرجات النموذج. يمكنك إرفاق زر زيادة ونقصان بخلية إدخال محددة. أثناء النقر فوق السهم لأعلى أو السهم لأسفل على زر زيادة ونقصان ، تزداد قيمة العدد الصحيح في خلية الإدخال المستهدفة أو تنقص.*Aspose.Cells* يسمح لك بإنشاء مغازل في أوراق العمل الخاصة بك.

### **باستخدام Microsoft إكسل**

لوضع عنصر تحكم في مربع التدوير في ورقة العمل الخاصة بك:

-  تأكد من أن*نماذج* يتم عرض شريط الأدوات.
-  انقر على*سبينر* أداة.
- في منطقة ورقة العمل الخاصة بك ، انقر واسحب لتحديد المستطيل الذي سيحمل القرص الدوار.
-  بمجرد وضع زر الزيادة والنقصان في ورقة العمل ، انقر بزر الماوس الأيمن فوق عنصر التحكم وانقر*تنسيق التحكم* وتحديد القيم القصوى والدنيا والتزايدية.
-  في ال*Cell رابط* ، حدد عنوان الخلية التي يجب ربط مربع الدوران هذا بها.
-  انقر فوق*نعم*.

### **باستخدام Aspose.Cells**

 ال[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner)، والذي يستخدم لإضافة عنصر تحكم مربع زيادة ونقصان إلى ورقة العمل. تقوم الطريقة بإرجاع ملف[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) هدف. الطبقة[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) يمثل مربع تدور. لها بعض الأعضاء المهمين:

-  ال[**لينكدسل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) تحدد الخاصية خلية مرتبطة بصندوق الدوران.
-  ال[**الأعلى**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) تحدد الخاصية الحد الأقصى لقيمة نطاق مربع الدوران.
-  ال[**دقيقة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) تحدد الخاصية الحد الأدنى لقيمة نطاق مربع الدوران.
-  ال[**تغيير تدريجي**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) تحدد الخاصية مقدار القيمة التي يتم فيها زيادة زر الزيادة والنقصان لتمرير سطر.
-  ال[**ظل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) تشير الخاصية إلى ما إذا كان مربع الدوران يحتوي على تظليل ثلاثي الأبعاد.
-  ال[**القيمة الحالية**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) تحدد الخاصية القيمة الحالية لمربع الدوران.

يوضح المثال التالي كيفية إضافة مربع زيادة ونقصان إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **إضافة عنصر تحكم شريط التمرير إلى ورقة عمل**

يتم استخدام عنصر تحكم شريط التمرير للمساعدة في تحديد البيانات في ورقة العمل بطريقة مشابهة لعنصر التحكم في مربع الدوران. بإضافة عنصر التحكم إلى ورقة عمل وربطه بخلية ، من الممكن إرجاع قيمة رقمية للموضع الحالي لعنصر التحكم.

### **باستخدام Microsoft إكسل**

- لإضافة شريط تمرير في Excel 2003 والإصدارات السابقة ، انقر فوق*شريط التمرير* زر على*نماذج* شريط الأدوات ، ثم قم بإنشاء شريط تمرير يغطي الخلايا B2: B6 في الارتفاع ويكون حوالي ربع عرض العمود.
-  لإضافة شريط تمرير في Excel 2007 ، انقر فوق*مطور* علامة التبويب ، انقر فوق*إدراج* ، ثم انقر فوق*شريط التمرير* في قسم ضوابط النموذج.
-  انقر بزر الماوس الأيمن فوق شريط التمرير ، ثم انقر فوق موافق*تنسيق التحكم*.
-  اكتب المعلومات التالية ، وانقر فوق*نعم*:
 - في ال*القيمة الحالية* مربع ، اكتب 1.
 - في ال*الحد الأدنى للقيمة* في المربع ، اكتب 1. تقيد هذه القيمة الجزء العلوي من شريط التمرير بالعنصر الأول في القائمة.
 - في ال*القيمة القصوى* ، اكتب 20. هذا الرقم يحدد الحد الأقصى لعدد الإدخالات في القائمة.
 - في ال*تغيير تدريجي* في المربع ، اكتب 1. تتحكم هذه القيمة في عدد الأرقام التي يزيد فيها عنصر التحكم في شريط التمرير من القيمة الحالية.
 - في ال*تغيير الصفحة* المربع ، اكتب 5. يتحكم هذا الإدخال في مقدار زيادة القيمة الحالية إذا نقرت داخل شريط التمرير على جانبي مربع التمرير.
 لوضع قيمة رقمية في الخلية G1 (بناءً على العنصر المحدد في القائمة) ، اكتب G1 في ملف*Cell رابط* علبة.
- انقر فوق أي خلية حتى لا يتم تحديد شريط التمرير.

عند النقر فوق عنصر التحكم لأعلى أو لأسفل في شريط التمرير ، يتم تحديث الخلية G1 إلى رقم يشير إلى القيمة الحالية لشريط التمرير بالإضافة إلى التغيير المتزايد لشريط التمرير أو طرحه.

### **باستخدام Aspose.Cells**

 ال[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar) ، والذي يستخدم لإضافة عنصر تحكم شريط التمرير إلى ورقة العمل. تقوم الطريقة بإرجاع ملف[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) هدف. الطبقة[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) يمثل شريط التمرير. لها بعض الأعضاء المهمين:

-  ال[**لينكدسل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) تحدد الخاصية خلية مرتبطة بشريط التمرير.
-  ال[**الأعلى**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) تحدد الخاصية الحد الأقصى لقيمة نطاق شريط التمرير.
-  ال[**دقيقة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) تحدد الخاصية الحد الأدنى لقيمة نطاق شريط التمرير.
-  ال[**تغيير تدريجي**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) تحدد الخاصية مقدار القيمة التي يتزايد بها شريط التمرير لتمرير سطر.
-  ال[**ظل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) تشير الخاصية إلى ما إذا كان شريط التمرير به تظليل ثلاثي الأبعاد.
-  ال[**القيمة الحالية**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) تحدد الخاصية القيمة الحالية لشريط التمرير.
-  ال[**تغيير الصفحة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange)تحدد الخاصية مقدار الزيادة في القيمة الحالية إذا نقرت داخل شريط التمرير على جانبي مربع التمرير.

يوضح المثال التالي كيفية إضافة شريط تمرير إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **إضافة عنصر تحكم GroupBox إلى مجموعة عناصر التحكم في ورقة عمل**

في بعض الأحيان تحتاج إلى تنفيذ أزرار الاختيار أو عناصر التحكم الأخرى التي تنتمي إلى مجموعة معينة ، يمكنك تنفيذها عن طريق تضمين إما مربع مجموعة أو عنصر تحكم مستطيل. أي من هذين الكائنين سيكون بمثابة محدد المجموعة. بعد إضافة أحد هذه الأشكال ، يمكنك بعد ذلك إضافة زري اختيار أو أكثر أو كائنات مجموعة أخرى.

### **باستخدام Microsoft إكسل**

لوضع عنصر تحكم مربع المجموعة في ورقة العمل الخاصة بك ووضع عناصر تحكم فيه:

-  لبدء نموذج ، في القائمة الرئيسية ، انقر فوق "نعم"*رأي* ، تليها*أشرطة الأدوات* و*نماذج*.
-  على ال*نماذج* شريط الأدوات ، انقر فوق*صندوق المجموعة* وارسم مستطيلاً على ورقة العمل.
- اكتب سلسلة تسمية توضيحية للمربع.
-  على ال*نماذج* شريط الأدوات ، انقر فوق*زر الخيارات* وانقر داخل ملف*صندوق المجموعة* فقط تحت سلسلة التسمية التوضيحية.
-  من*نماذج* شريط الأدوات مرة أخرى ، انقر فوق*زر الخيارات* وانقر داخل ملف*صندوق المجموعة*تحت زر الاختيار الأول.
-  مرة أخرى على*نماذج* شريط الأدوات ، انقر فوق*زر الخيارات* وانقر داخل ملف*صندوق المجموعة* تحت زر الاختيار السابق.

### **باستخدام Aspose.Cells**

 ال[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox) ، والذي يستخدم لإضافة عنصر تحكم مربع المجموعة إلى ورقة العمل. تقوم الطريقة بإرجاع ملف[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) هدف. وعلاوة على ذلك، فإن[**مجموعة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) طريقة[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) فئة المجموعات الأشكال ، يستغرق[**شكل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) صفيف كمعامل وإرجاع[**المجموعة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape) هدف. الطبقة[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) يمثل صندوق المجموعة. لها بعض الأعضاء المهمين:

-  ال[**نص**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) تحدد الخاصية سلسلة التسمية التوضيحية لمربع المجموعة.
-  ال[**ظل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) تشير الخاصية إلى ما إذا كان مربع المجموعة به تظليل ثلاثي الأبعاد.

يوضح المثال التالي كيفية إضافة مربع مجموعة وتجميع عناصر التحكم في ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **موضوعات مسبقة**
- [أضف عناصر تحكم ActiveX باستخدام Aspose.Cells](/cells/ar/net/add-activex-controls-using-aspose-cells/)
- [قم بإزالة عنصر تحكم ActiveX](/cells/ar/net/remove-activex-control/)
- [تحديث عنصر تحكم ActiveX ComboBox](/cells/ar/net/update-activex-combobox-control/)
