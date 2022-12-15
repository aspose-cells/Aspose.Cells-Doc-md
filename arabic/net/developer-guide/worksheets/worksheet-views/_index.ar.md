---
title: طرق عرض ورقة العمل
type: docs
weight: 40
url: /ar/net/worksheet-views/
---
## **معاينة فاصل الصفحة**

يمكن عرض جميع أوراق العمل في وضعين:

- العرض العادي.
- معاينة فاصل الصفحة.

طريقة العرض العادية هي طريقة العرض الافتراضية لورقة العمل. معاينة فاصل الصفحة هي طريقة عرض تحرير تعرض ورقة عمل كما ستتم طباعتها. تُظهر معاينة فاصل الصفحة البيانات التي سيتم نقلها على كل صفحة حتى تتمكن من ضبط منطقة الطباعة وفواصل الصفحات. باستخدام Aspose.Cells يمكن للمطورين تمكين العرض العادي أو أوضاع معاينة فاصل الصفحة.

### **التحكم في أوضاع العرض**

يوفر Aspose.Cells أ[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لتمكين أوضاع المعاينة العادية أو أوضاع معاينة فاصل الصفحة ، استخدم ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) منشأه.[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) هي خاصية منطقية ، مما يعني أنه يمكنها فقط تخزين ملف**حقيقي** أو أ**خاطئة** القيمة.

#### **تمكين العرض العادي**

 قم بتعيين ورقة عمل إلى العرض العادي عن طريق تعيين ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) الملكية ل**خاطئة**.

#### **تمكين معاينة فاصل الصفحة**

 قم بتعيين أي ورقة عمل لمعاينة فاصل الصفحة عن طريق تعيين ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) الملكية ل**حقيقي**يؤدي القيام بذلك إلى تبديل ورقة العمل من العرض العادي إلى معاينة فاصل الصفحة.

 ويرد أدناه مثال كامل يوضح كيفية استخدام[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)الخاصية لتمكين وضع معاينة فاصل الصفحة لورقة العمل الأولى لملف Excel.

يتم فتح ملف book1.xls عن طريق إنشاء مثيل لملف[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) صف دراسي. يتم تبديل طريقة العرض إلى معاينة فاصل الصفحة لورقة العمل الأولى عن طريق تعيين ملف[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)الملكية ل**حقيقي**. يتم حفظ الملف المعدل كملف output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **عامل التكبير**

### **باستخدام Microsoft إكسل**

يوفر Microsoft Excel ميزة تتيح للمستخدمين تعيين تكبير / تصغير ورقة العمل أو عامل التحجيم. تساعد هذه الميزة المستخدمين على رؤية محتويات ورقة العمل في طرق عرض أصغر أو أكبر. يمكن للمستخدمين ضبط عامل التكبير / التصغير على أي قيمة.

### **Aspose.Cells & عامل التكبير**

Aspose.Cells يسمح للمطورين بتعيين عامل تكبير ورقة العمل.
يوفر Aspose.Cells أ[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لتعيين عامل التكبير / التصغير الخاص بورقة العمل ، استخدم ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي'[**تكبير**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)منشأه. يتم تعيين عامل التكبير / التصغير عن طريق تعيين قيمة رقمية (عدد صحيح) لملف[**تكبير**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) منشأه.

ويرد أدناه مثال كامل يوضح كيفية استخدام[**تكبير**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) لتعيين عامل التكبير / التصغير الخاص بورقة العمل الأولى لملف Excel.

يتم فتح ملف book1.xls عن طريق إنشاء مثيل لملف[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)صف دراسي. يتم تعيين عامل التكبير / التصغير الخاص بورقة العمل الأولى على 75 ويتم حفظ الملف المعدل على هيئة output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **أجزاء التجميد**

### **باستخدام Microsoft إكسل**

ألواح التجميد هي ميزة يوفرها Microsoft Excel. تسمح لك أجزاء التجميد بتحديد البيانات لتظل مرئية عند التمرير في ورقة العمل.

### **Aspose.Cells & تجميد الأجزاء**

Aspose.Cells يسمح للمطورين بتطبيق ألواح التجميد على أوراق العمل في وقت التشغيل.

يوفر Aspose.Cells أ[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لتكوين أجزاء التجميد ، اتصل بفئة ورقة العمل '[**أجزاء التجميد**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)طريقة. ال[**أجزاء التجميد**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)تأخذ الطريقة المعلمات التالية:

- **صف**، فهرس صف الخلية الذي سيبدأ التجميد منه.
- **عمودي**، فهرس العمود الخاص بالخلية التي سيبدأ التجميد منها.
- **صفوف مجمدة**، عدد الصفوف المرئية في الجزء العلوي.
- **أعمدة مجمدة**، عدد الأعمدة المرئية في الجزء الأيمن

يتم فتح ملف book1.xls عن طريق استدعاء ملف[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)منشئ class أثناء إنشائه وتم تجميد عدد قليل من الصفوف والأعمدة في ورقة العمل الأولى. يتم حفظ الملف المعدل كملف output.xls.

 ويرد أدناه مثال كامل يوضح كيفية استخدام ملف[**أجزاء التجميد**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)طريقة لتجميد الصفوف والأعمدة (بدءًا من C4 ، ممثلة بالصف الرابع والعمود الثالث ، حيث تبدأ الصفوف والأعمدة من فهرس 0) من ورقة العمل الأولى من ملف Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **تقسيم الأجزاء**

إذا كنت بحاجة إلى تقسيم الشاشة للحصول على عرضين مختلفين في نفس ورقة العمل ، فقم بتقسيم الألواح. يوفر Microsoft Excel ميزة مفيدة للغاية تتيح لك عرض أكثر من نسخة واحدة من ورقة العمل الخاصة بك ، ولتتمكن من التمرير عبر كل جزء من ورقة العمل بشكل مستقل: تقسيم الأجزاء.

تعمل الأجزاء في وقت واحد. إذا قمت بإجراء تغيير في أحدهما ، فسيظهر التغيير في الآخر في نفس الوقت. يوفر Aspose.Cells ميزة الأجزاء المنقسمة للمستخدمين.

### **تطبيق وإزالة الأجزاء المنقسمة**

#### **تقسيم الأجزاء**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) توفر class مجموعة كبيرة من الخصائص والأساليب لإدارة ملف Excel. لتنفيذ طرق العرض المقسمة ، استخدم ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي'[**انشق، مزق**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split) . لإزالة الأجزاء المنقسمة ، استخدم ملف[**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)طريقة.

في المثال ، نستخدم ملف قالب بسيط يتم تحميله ، ثم يتم تطبيق ميزة تقسيم الأجزاء المحددة على خلية في ورقة العمل الأولى. يتم حفظ الملف المحدث.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

بعد تشغيل الكود أعلاه ، سيكون للملف الذي تم إنشاؤه عرض مقسم.

#### **إزالة الأجزاء**

 قم بإزالة الأجزاء المنقسمة باستخدام[**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)طريقة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **موضوعات مسبقة**
- [إخفاء عرض القيم الصفرية في ورقة العمل](/cells/ar/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [تعيين لون علامة تبويب ورقة العمل](/cells/ar/net/set-worksheet-tab-color/)
- [إظهار وإخفاء خطوط الشبكة ورؤوس أعمدة الصفوف](/cells/ar/net/show-and-hide-gridlines-and-row-column-headers/)
- [إظهار وإخفاء أعمدة الصفوف وأشرطة التمرير](/cells/ar/net/show-and-hide-rows-columns-and-scroll-bars/)
- [إظهار وإخفاء أوراق العمل وعلامات التبويب](/cells/ar/net/show-and-hide-worksheets-and-tabs/)
- [إظهار الصيغ بدلاً من القيم في ورقة عمل](/cells/ar/net/show-formulas-instead-of-values-in-a-worksheet/)
- [استخدم خيارات تدقيق الأخطاء](/cells/ar/net/use-error-checking-options/)

