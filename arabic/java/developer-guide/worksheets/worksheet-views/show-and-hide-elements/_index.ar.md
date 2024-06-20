---
title: عرض وإخفاء العناصر
type: docs
weight: 60
url: /ar/java/show-and-hide-elements/
---

{{% alert color="primary" %}}

تسمح Aspose.Cells للمستخدم بعرض وإخفاء عناصر دفتر العمل بما في ذلك ورق العمل والصفوف والأعمدة والعلامات التبويب وأشرطة التمرير وخطوط الشبكة.

{{% /alert %}}

## **إظهار وإخفاء ورقة عمل**

يمكن أن يحتوي ملف إكسل على ورقة عمل واحدة أو أكثر. كلما أنشأنا ملف إكسل، نضيف أوراق عمل إلى الملف إكسل الذي نعمل فيه. تكون كل ورقة عمل في ملف إكسل مستقلة عن الورقة العمل الأخرى بوجود بياناتها الخاصة وإعدادات التنسيق وما إلى ذلك. في بعض الأحيان، قد يحتاج المطورون إلى إخفاء بعض الأوراق العمل وجعل البعض الآخر مرئية في ملف إكسل لمصلحتهم الخاصة. لذا، **Aspose.Cells** يتيح للمطورين التحكم في رؤية أوراق العمل في ملفاتهم إكسل.

**التحكم في ظهور أوراق العمل:**

يوفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

تُمثل ورقة عمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. ومع ذلك، للتحكم في رؤية ورقة العمل، يمكن للمطورين استخدام [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) الطريقة لفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **جعل ورقة العمل مرئية**

يمكن للمطورين جعل ورقة العمل مرئية عن طريق تمرير **صح** كمعلمة إلى [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) الطريقة لفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **إخفاء ورقة عمل**

يمكن للمطورين إخفاء ورقة العمل عن طريق تمرير **خطأ** كمعلمة إلى [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) الطريقة لفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

**مثال:**

يتم تقديم مثال كامل أدناه يوضح استخدام [**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) الطريقة لفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) لإخفاء الورقة العمل الأولى في ملف Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**ورقة العمل - قبل التعديل:**

في اللقطة أدناه، يمكنك رؤية أن ملف **Book1.xls** يحتوي على ثلاث ورقات عمل: **Sheet1** و**Sheet2** و**Sheet3**.

![todo:image_alt_text](show-and-hide-elements_1.png)

**الشكل:** عرض ورقة العمل قبل أي تعديل

**ورقة العمل - بعد تنفيذ الشفرة المثال:**

تم فتح ملف **Book1.xls** باستخدام فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ثم تم جعل ورقة العمل الأولى في ملف **Book1.xls** مخفية. يتم حفظ الملف المعدل كملف **output.xls** والذي يظهر عرضه البياني كما هو موضح أدناه:

![todo:image_alt_text](show-and-hide-elements_2.png)

**الشكل:** عرض ورقة العمل بعد التعديل

**ضبط نوع الرؤية**

يمكنك أيضًا إخفاء ورقات العمل بطريقة خاصة. يمكن أن تخفي هذه الميزة ورقة العمل بحيث الطريقة الوحيدة لجعلها مرئية مرة أخرى هي من خلال إعطاء [**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) كقيمة معلمة لطريقة [**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) في الشفرة (من الجدير بالذكر هنا، لا يمكن للمستخدمين جعل الكائن مرئيًا في MS Excel مباشرة باستخدام خيارات القائمة الخاصة به). يمكن للمستخدمين أيضًا استخدام طريقة [**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) للتحقق مما إذا كانت ورقة العمل مُعدَّلة على أنها مخفية جدًا أم لا.

## **إظهار أو إخفاء علامات التبويب**

إذا نظرت عن كثب في أسفل ملف Microsoft Excel، سترى عددًا من الضوابط. تشمل هذه:

- ألسنة الصفحات.
- أزرار تمرير الألسنة.

تمثل ألسنة الصفحات الأوراق العمل في ملف الإكسل. انقر على أي علامة تبويب للانتقال إلى تلك الورقة العمل. كلما زاد عدد الأوراق العمل في الدفتر الحسابي، زادت ألسنة الصفحة. إذا كان لديك عدد جيد من الأوراق العمل في دفتر العمل، يلزمك الأزرار للتنقل خلالها. لذا، يوفر مايكروسوفت إكسل أزرار تمرير الألسنة للتمرير من خلال ألسنة الصفحات.

**علامات الورقة وأزرار تمرير العلامة التبويبية**

![todo:image_alt_text](show-and-hide-elements_3.png)

باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية علامات الجدول وأزرار التمرير في ملفات Excel.

**التحكم في رؤية العلامات:**
توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Microsoft Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) مجموعة واسعة من الخصائص والأساليب لإدارة ملف Excel.

### **إخفاء علامات التبويب**

إخفاء العلامات في ملف Excel عن طريق تعيين طريقة [**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) لفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **جعل علامات التبويب مرئية**

جعل العلامات مرئية باستخدام طريقة [**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) لفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**مثال شفرة كامل:**

أدناه مثال كامل يفتح ملف Excel (book1.xls)، يخفي علامات تبويبه ويحفظ الملف المعدل بوصفه output.xls.

يمكنك أن ترى أن ملف Book1.xls يحتوي على علامات تبويب في الشكل أدناه. بعد تنفيذ كود المثال، تم إخفاء الألسنة، كما يمكنك رؤية من لقطة الشاشة للملف output.xls أدناه.

**Book1.xls: ملف Excel قبل أي تعديل**

![todo:image_alt_text](show-and-hide-elements_4.png)

**output.xls: ملف Excel بعد التعديل**

![todo:image_alt_text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **إظهار وإخفاء الصفوف والأعمدة**

جميع ورقات العمل في ملف Excel مكونة من خلايا مرتبة في صفوف وأعمدة. جميع الصفوف والأعمدة لها قيم فريدة يتم استخدامها لتحديدها، وتحديد الخلايا الفردية. على سبيل المثال، يتم ترقيم الصفوف – 1، 2، 3، 4، إلخ – وترتيب الأعمدة ترتيباً أبجديا – A، B، C، D، إلخ. تعرض القيم الصف والعمود في الرؤوس. باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤوس الصف والعمود هؤلاء.

**التحكم في ظهور أوراق العمل:**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)، تمثل ملف Microsoft Excel. تحتوي فئة Workbook على مجموعة من ورق العمل التي تسمح بالوصول إلى كل ورق عمل في ملف إكسل.

يُمثل ورق العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر فئة Worksheet مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. للتحكم في رؤية رؤوس الصفوف والأعمدة، استخدم أسلوب [**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) في فئة Worksheet.

### **إخفاء رؤوس الصف/العمود**

إخفاء رؤوس الصف والعمود باستخدام أسلوب [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) في الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **جعل رؤوس الصف/العمود مرئية**

جعل رؤوس الصف والعمود مرئية بواسطة أسلوب [**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) في الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

يتم تقديم مثال كامل أدناه يوضح كيفية استخدام أسلوب [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) في فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) لإخفاء رؤوس الصف والعمود في الورقة العمل الأولى من ملف Excel.

تُظهر اللقطة الشاشية أدناه أن ملف Book1.xls يحتوي على ثلاث ورقات عمل: Sheet1، Sheet2 وSheet3. يُعرض في كل ورقة عمل رؤوس الصف والعمود.

**Book1.xls: ورقة العمل قبل التعديل**

![todo:image_alt_text](show-and-hide-elements_6.png)

يتم فتح Book1.xls باستخدام فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ويتم إخفاء رؤوس الصف والعمود في الورقة العمل الأولى. يتم حفظ الملف المعدل بصيغة output.xls.

**عرض ورقة العمل بعد التعديل**

![todo:image_alt_text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **إظهار وإخفاء شريط التمرير**

شريطي التمرير يُستخدمان بشكل كبير لتصفح محتويات أي ملف. عادةً، هناك نوعان من شريطي التمرير:

- شرائط التمرير العمودية
- شرائط التمرير الأفقية

توفر Microsoft Excel أيضًا شرائط تمرير أفقية وعمودية بحيث يمكن للمستخدمين التمرير من خلال محتويات ورقة العمل. باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية كلا أنواع شرائط التمرير في ملفات Excel.

**التحكم في رؤية شريطي التمرير:**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Excel. توفر الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) مجموعة واسعة من الخصائص والطرق لإدارة ملف Excel. ومع ذلك، للتحكم في رؤية شريطي التمرير في ملف Excel، قد يستخدم المطورون أساليب [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) و [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) لفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

### **إخفاء أشرطة التمرير**

إخفاء أشرطة التمرير عن طريق ضبط أساليب [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) أو [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) لفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) إلى **false**.

### **جعل أشرطة التمرير مرئية**

إظهار أشرطة التمرير عن طريق ضبط أساليب [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) أو [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) لفئة Workbook إلى **true**.

**مثال شفرة كامل:**

بالأسفل يوجد شيفرة كاملة تفتح ملف إكسل، book1.xls، ثم تخفي كلتي الشريطين وتحفظ الملف المعدل بشكل output.xls.

يُظهر اللقطة الشاشية أدناه ملف Book1.xls الذي يحتوي على كلا شريطي التمرير. الملف المعدل يتم حفظه بصيغة output.xls كما هو موضح أدناه أيضًا.

**Book1.xls: ملف Excel قبل أي تعديل**

![todo:image_alt_text](show-and-hide-elements_8.png)

**output.xls: ملف Excel بعد التعديل**

![todo:image_alt_text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **إظهار وإخفاء خطوط الشبكة**

تحتوي جميع ورقات عمل Microsoft Excel على خطوط شبكة افتراضياً. إنها تساعد في تحديد الخلايا، بحيث يكون من السهل إدخال البيانات في خلايا معينة. تمكننا خطوط الشبكة من عرض ورقة عمل كمجموعة من الخلايا، حيث يمكن تحديد كل خلية بسهولة.

تسمح Aspose.Cells أيضًا لك بالتحكم في رؤية خطوط الشبكة.

### **التحكم في رؤية خطوط الشبكة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) يسمح بالوصول إلى كل ورقة عمل في الملف.

يتم تمثيل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة الأوراق العمل. للتحكم في رؤية خطوط الشبكة، استخدم أسلوب [**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) لفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

#### **جعل خطوط الشبكة مرئية**

لجعل الخطوط الشبكية مرئية، استخدم الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) والطريقة [**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible).

#### **إخفاء خطوط الشبكة**

إخفاء الخطوط الشبكية باستخدام الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) والطريقة [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible).

{{% alert color="primary" %}}

تُطبق الخطوط الشبكية على الورقة بأكملها. لـ 'إخفاء' الخطوط الشبكية على قسم من ورقة العمل، استخدم [تنسيق الحدود](/cells/ar/java/create-table-by-using-border-lines-for-a-range/) لتعيين الحدود بلون يمتزج مع مخطط الألوان للورقة.

{{% /alert %}}

**مثال: إخفاء الخطوط الشبكية في ورقة عمل معينة**

يوضح المثال أدناه استخدام الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) والطريقة [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) لإخفاء الخطوط الشبكية في الورقة العمل الأولى من ملف Excel.

تُظهر اللقطة السفلية أن ملف Book1.xls يحتوي على ثلاث ورقات عمل: Sheet1، Sheet2 و Sheet3. جميع هذه الورقات العمل لديها خطوط شبكية.

**عرض ورقة العمل قبل التعديل**

![todo:image_alt_text](show-and-hide-elements_10.png)

يتم فتح ملف Book1.xls باستخدام الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ثم يتم إخفاء الخطوط الشبكية للورقة العمل الأولى. يتم حفظ الملف المعدل بشكل خروج.xls.

**عرض ورقة العمل بعد التعديل**

![todo:image_alt_text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **مقالات ذات صلة**

{{% alert color="primary" %}}

- [ميزات إعداد الصفحة](/cells/ar/java/page-setup-features/).
- [إضافة حدود إلى الخلايا لإنشاء جدول](/cells/ar/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
