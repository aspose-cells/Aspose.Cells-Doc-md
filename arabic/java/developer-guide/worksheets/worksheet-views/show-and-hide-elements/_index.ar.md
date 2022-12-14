---
title: إظهار وإخفاء العناصر
type: docs
weight: 60
url: /ar/java/show-and-hide-elements/
---
{{% alert color="primary" %}}

Aspose.Cells يسمح للمستخدم بإظهار وإخفاء عناصر مصنف بما في ذلك أوراق العمل والصفوف والأعمدة وعلامات التبويب وأشرطة التمرير وخطوط الشبكة ،

{{% /alert %}}

## **إظهار وإخفاء ورقة العمل**

 يمكن أن يحتوي ملف Excel على ورقة عمل واحدة أو أكثر. عندما نقوم بإنشاء ملف Excel ، نضيف أوراق العمل إلى ملف Excel الذي نعمل فيه. كل ورقة عمل في ملف Excel مستقلة عن ورقة العمل الأخرى من خلال وجود بياناتها وإعدادات التنسيق الخاصة بها وما إلى ذلك. في بعض الأحيان ، قد يطلب المطورون إخفاء أوراق عمل قليلة والأخرى مرئية في ملف Excel لمصلحتهم الخاصة. لذا،**Aspose.Cells** يسمح للمطورين بالتحكم في رؤية أوراق العمل في ملفات Excel الخاصة بهم.

**التحكم في رؤية أوراق العمل:**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) يمثل ملف Excel.[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي.[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) توفر class مجموعة كبيرة من الخصائص والأساليب لإدارة ورقة العمل. ولكن للتحكم في رؤية ورقة العمل ، يمكن للمطورين استخدامها[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) طريقة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي.

### **جعل ورقة العمل مرئية**

 يمكن للمطورين جعل ورقة العمل مرئية بالمرور**حقيقي** كمعامل ل[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) طريقة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي.

### **إخفاء ورقة العمل**

 يمكن للمطورين إخفاء ورقة العمل بالتمرير**خاطئة** كمعامل ل[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) طريقة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي.

**مثال:**

 ويرد أدناه مثال كامل يوضح استخدام[**setVisible (خطأ)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) طريقة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) فئة لإخفاء ورقة العمل الأولى من ملف Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**ورقة عمل - قبل التعديل:**

 في لقطة الشاشة أدناه ، يمكنك رؤية ذلك**كتاب 1.xls** يحتوي الملف على ثلاث أوراق عمل:**الورقة 1** , **ورقة 2** و**ورقة 3** .

![ما يجب القيام به: image_بديل_نص](show-and-hide-elements_1.png)

**شكل:** عرض ورقة العمل قبل أي تعديل

**ورقة عمل - بعد تنفيذ كود المثال:**

**كتاب 1.xls** يتم فتح الملف باستخدام ملف[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة ثم ورقة العمل الأولى من**كتاب 1.xls** تم إخفاء الملف. يتم حفظ الملف المعدل كملف**الإخراج. xls**الملف الذي تظهر صورته أدناه:

![ما يجب القيام به: image_بديل_نص](show-and-hide-elements_2.png)

**شكل:** عرض ورقة العمل بعد التعديل

**تحديد نوع الرؤية**

 يمكنك أيضًا إخفاء أوراق العمل بطريقة خاصة. يمكن لهذه الميزة أن تحافظ على ورقة العمل بحيث تكون الطريقة الوحيدة لجعلها مرئية مرة أخرى هي العطاء[**نوع الرؤية. VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) كقيمة معلمة لـ[**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) الطريقة في الكود (تجدر الإشارة هنا ، لا يمكن للمستخدم أن يجعل الكائن مرئيًا في MS Excel مباشرة باستخدام خيارات القائمة الخاصة به). يمكن للمستخدمين أيضًا استخدام ملفات[**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) طريقة للتحقق مما إذا تم وضع علامة على ورقة العمل كـ VeryHidden أم لا.

## **إظهار أو إخفاء علامات التبويب**

إذا نظرت عن كثب إلى الجزء السفلي من ملف Excel Microsoft ، فسترى عددًا من عناصر التحكم. وتشمل هذه:

- علامات تبويب الأوراق.
- أزرار التمرير لعلامة التبويب.

تمثل علامات تبويب الأوراق أوراق العمل في ملف Excel. انقر فوق أي علامة تبويب للتبديل إلى ورقة العمل هذه. كلما زاد عدد أوراق العمل في المصنف ، زاد عدد علامات تبويب الأوراق. إذا كان ملف Excel يحتوي على عدد جيد من أوراق العمل ، فأنت بحاجة إلى أزرار للتنقل خلالها. لذلك ، يوفر Microsoft Excel أزرار تمرير علامة التبويب للتمرير عبر علامات تبويب الأوراق.

**علامات تبويب الأوراق وأزرار التمرير لعلامة التبويب**

![ما يجب القيام به: image_بديل_نص](show-and-hide-elements_3.png)

باستخدام Aspose.Cells ، يمكن للمطورين التحكم في رؤية علامات تبويب الأوراق وأزرار تمرير علامات التبويب في ملفات Excel.

**التحكم في رؤية علامات التبويب:**
 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) توفر class مجموعة كبيرة من الخصائص والأساليب لإدارة ملف Excel.

### **علامات التبويب الاختباء**

 إخفاء علامات التبويب في ملف Excel عن طريق تعيين الامتداد[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) صف دراسي'[**getSettings (). setShowTabs (خطأ)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) طريقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **جعل علامات التبويب مرئية**

 اجعل علامات التبويب مرئية بامتداد[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) صف دراسي'[**getSettings (). setShowTabs (صواب)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) طريقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**مثال رمز كامل:**

يوجد أدناه مثال كامل يفتح ملف Excel (book1.xls) ، ويخفي علامات التبويب الخاصة به ويحفظ الملف المعدل كـ output.xls.

يمكنك أن ترى أن ملف Book1.xls يحتوي على علامات تبويب في الشكل أدناه. بعد تنفيذ رمز المثال ، يتم إخفاء علامات التبويب ، كما ترى من لقطة شاشة ملف output.xls أدناه.

**book1.xls: ملف Excel قبل أي تعديل**

![ما يجب القيام به: image_بديل_نص](show-and-hide-elements_4.png)

**output.xls: ملف Excel بعد التعديل**

![ما يجب القيام به: image_بديل_نص](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **إظهار وإخفاء الصفوف والأعمدة**

تتكون جميع أوراق العمل في ملف Excel من خلايا مرتبة في صفوف وأعمدة. تحتوي جميع الصفوف والأعمدة على قيم فريدة تُستخدم لتعريفها ولتعريف الخلايا الفردية. على سبيل المثال ، يتم ترقيم الصفوف - 1 ، 2 ، 3 ، 4 ، وما إلى ذلك - ويتم ترتيب الأعمدة أبجديًا - A ، B ، C ، D ، إلخ. يتم عرض قيم الصفوف والأعمدة في الرؤوس. باستخدام Aspose.Cells ، يمكن للمطورين التحكم في رؤية رؤوس الصفوف والأعمدة هذه.

**التحكم في رؤية أوراق العمل:**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)، يمثل ملف Excel Microsoft. تحتوي فئة المصنف على مجموعة أوراق العمل التي تتيح الوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)صف دراسي. توفر فئة ورقة العمل نطاقًا واسعًا من الخصائص والأساليب لإدارة أوراق العمل. للتحكم في رؤية رؤوس الصفوف والأعمدة ، استخدم فئة ورقة العمل '[**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) طريقة.

### **إخفاء رؤوس الصفوف / الأعمدة**

 إخفاء رؤوس الصفوف والأعمدة باستخدام ملف[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[**setRowColumnHeadersVisible (خطأ)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) طريقة.

### **جعل رؤوس الصفوف / الأعمدة مرئية**

 اجعل رؤوس الصفوف والأعمدة مرئية باستخدام ملحق[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[**setRowColumnHeadersVisible (صواب)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) طريقة.

 ويرد أدناه مثال كامل يوضح كيفية استخدام[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[**setRowColumnHeadersVisible (خطأ)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) طريقة لإخفاء رؤوس الصفوف والأعمدة في ورقة العمل الأولى لملف Excel.

توضح لقطة الشاشة أدناه أن Book1.xls يحتوي على ثلاث أوراق عمل: Sheet1 و Sheet2 و Sheet3. تعرض كل ورقة عمل رؤوس الصفوف والأعمدة.

**Book1.xls: ورقة عمل قبل التعديل**

![ما يجب القيام به: image_بديل_نص](show-and-hide-elements_6.png)

 يتم فتح Book1.xls باستخدام ملحق[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class "ورؤوس الصفوف والأعمدة في ورقة العمل الأولى مخفية. يتم حفظ الملف المعدل كملف output.xls.

**عرض ورقة العمل بعد التعديل**

![ما يجب القيام به: image_بديل_نص](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **إظهار وإخفاء أشرطة التمرير**

تُستخدم أشرطة التمرير كثيرًا للتنقل في محتويات أي ملف. عادة ، هناك نوعان من أشرطة التمرير:

- أشرطة التمرير العمودية
- أشرطة التمرير الأفقية

يوفر Microsoft Excel أيضًا أشرطة تمرير أفقية ورأسية بحيث يمكن للمستخدمين التمرير عبر محتويات ورقة العمل. باستخدام Aspose.Cells ، يمكن للمطورين التحكم في رؤية كلا النوعين من أشرطة التمرير في ملفات Excel.

**التحكم في رؤية أشرطة التمرير:**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) يمثل ملف Excel.[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة ملف Excel. ولكن للتحكم في رؤية أشرطة التمرير في ملف Excel ، يمكن للمطورين استخدام ملفات[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) & [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) طرق[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) صف دراسي.

### **إخفاء أشرطة التمرير**

 إخفاء أشرطة التمرير عن طريق ضبط[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) صف دراسي'[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) أو[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) طرق ل**خاطئة**.

### **جعل أشرطة التمرير مرئية**

 اجعل أشرطة التمرير مرئية عن طريق تعيين فئة المصنف '[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) أو[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) طرق ل**حقيقي**.

**مثال رمز كامل:**

يوجد أدناه رمز كامل يفتح ملف Excel ، book1.xls ، ويخفي شريطي التمرير ثم يحفظ الملف المعدل كـ output.xls.

توضح لقطة الشاشة أدناه ملف Book1.xls الذي يحتوي على شريطي التمرير. يتم حفظ الملف المعدل كملف output.xls ، كما هو موضح أدناه.

**Book1.xls: ملف Excel قبل أي تعديل**

![ما يجب القيام به: image_بديل_نص](show-and-hide-elements_8.png)

**output.xls: ملف Excel بعد التعديل**

![ما يجب القيام به: image_بديل_نص](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **إظهار وإخفاء خطوط الشبكة**

تحتوي جميع أوراق عمل Microsoft Excel على خطوط شبكة بشكل افتراضي. إنها تساعد في تحديد الخلايا ، بحيث يسهل إدخال البيانات في خلايا معينة. تمكننا خطوط الشبكة من عرض ورقة العمل كمجموعة من الخلايا ، حيث يمكن التعرف على كل خلية بسهولة.

يسمح لك Aspose.Cells أيضًا بالتحكم في رؤية خطوط الشبكة.

### **التحكم في رؤية خطوط الشبكة**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) الذي يمثل ملف إكسل Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) يسمح بالوصول إلى كل ورقة عمل في الملف.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. للتحكم في رؤية خطوط الشبكة ، استخدم ملف[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) طريقة.

#### **جعل خطوط الشبكة مرئية**

 لجعل خطوط الشبكة مرئية ، استخدم ملف[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[**setGridlinesVisible (صواب)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) طريقة.

#### **إخفاء خطوط الشبكة**

 إخفاء خطوط الشبكة باستخدام ملف[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[**setGridlinesVisible (خطأ)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) طريقة.

{{% alert color="primary" %}}

يتم تطبيق خطوط الشبكة على الورقة بأكملها. لإخفاء خطوط الشبكة في قسم من ورقة العمل ، استخدم[تنسيق الحدود](/cells/ar/java/create-table-by-using-border-lines-for-a-range/) لتعيين الحدود إلى لون يندمج مع نظام ألوان الورقة.

{{% /alert %}}

**مثال: إخفاء خطوط الشبكة في ورقة عمل معينة**

 يوضح المثال أدناه استخدام امتداد[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[**setGridlinesVisible (خطأ)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) طريقة لإخفاء خطوط الشبكة في ورقة العمل الأولى من ملف Excel.

توضح لقطة الشاشة أدناه أن ملف Book1.xls يحتوي على ثلاث أوراق عمل: Sheet1 و Sheet2 و Sheet3. تحتوي كل أوراق العمل هذه على خطوط شبكية.

**عرض ورقة العمل قبل التعديل**

![ما يجب القيام به: image_بديل_نص](show-and-hide-elements_10.png)

 يتم فتح الملف Book1.xls باستخدام ملحق[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class ثم خطوط الشبكة الخاصة بورقة العمل الأولى مخفية. يتم حفظ الملف المعدل كملف output.xls.

**عرض ورقة العمل بعد التعديل**

![ما يجب القيام به: image_بديل_نص](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **مقالات ذات صلة**

{{% alert color="primary" %}}

- [ميزات إعداد الصفحة](/cells/ar/java/page-setup-features/).
- [إضافة حدود إلى الخلايا لإنشاء جدول](/cells/ar/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
