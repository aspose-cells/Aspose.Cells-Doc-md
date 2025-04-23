---
title: ميزات إعداد الصفحة
type: docs
weight: 40
url: /ar/java/page-setup-features/
---

في بعض الأحيان، من الضروري تكوين إعدادات إعداد الصفحة لورقات العمل للتحكم في الطباعة. توفر هذه الإعدادات خيارات مختلفة.

خيارات الصفحة 

![todo:image_alt_text](page-setup-features_1.png)

تدعم خيارات إعداد الصفحة بشكل كامل في Aspose.Cells. يوضح هذا المقال كيفية تعيين خيارات الصفحة باستخدام Aspose.Cells.

## **ضبط خيارات الصفحة**

يوفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة Workbook على مجموعة Worksheets التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

توفر فئة Worksheet خاصية PageSetup، المستخدمة لتعيين خيارات إعداد الصفحة. في الواقع، تعتبر خاصية PageSetup كائنًا من فئة PageSetup الذي يجعل من الممكن تعيين خيارات تخطيط الصفحة لورقة عمل مطبوعة. توفر فئة PageSetup مجموعة متنوعة من الخصائص المستخدمة لتعيين خيارات إعداد الصفحة. تُناقش بعض هذه الخصائص أدناه.

### **اتجاه الصفحة**

يمكن تعيين اتجاه الصفحة إلى الوضع الطولي أو الأفقي باستخدام أسلوب [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) في فئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). يأخذ الأسلوب [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) تعداد [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) كمعلمة. يتم سرد أعضاء تعداد [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) أدناه.

|**أنواع توجيه الصفحة**|**الوصف**|
| :- | :- |
|[**LANDSCAPE**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|توجيه أفقي|
|[**PORTRAIT**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|توجيه طولي|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **عامل التحليل**

من الممكن تصغير أو تكبير حجم ورقة العمل عن طريق ضبط عامل التحجيم باستخدام أسلوب [**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) في فئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **خيارات FitToPages**

لتناسب محتويات الورقة إلى عدد معين من الصفحات، استخدم أساليب [**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) و [**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) في فئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). تُستخدم هذه الأساليب أيضًا لتحجيم الورقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **حجم ورق**

قم بتعيين حجم الورق الذي ستتم الطباعة إليه بواسطة خاصية [**PaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) في فئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). تقبل خاصية PaperSize واحدة من القيم المحددة مسبقًا في تعداد [**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType)، المُدرجة أدناه.

|**أنواع حجم الورق**|**الوصف**|
| :- | :- |
|Paper10x14|10 in. x 14 in.|
|Paper11x17|11 in. x 17 in.|
|PaperA3|A3 (297 mm x 420 mm)|
|PaperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PaperA5|A5 (148 mm x 210 mm)|
|PaperB3|B3 (13.9 x 19.7 inches)|
|PaperB4|B4 (250 mm x 354 mm)|
|PaperB5|B5 (182 mm x 257 mm)|
|PaperBusinessCard|Business Card (90 mm x 55 mm)|
|PaperCSheet|C size sheet|
|PaperDSheet|D size sheet|
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|
|PaperEnvelopeC6|Envelope C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|
|PaperESheet|E size sheet|
|PaperExecutive|Executive (7-1/2 in. x 10-1/2 in.)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|
|PaperFolio|Folio (8-1/2 in. x 13 in.)|
|PaperLedger|Ledger (17 in. x 11 in.)|
|PaperLegal|Legal (8-1/2 in. x 14 in.)|
|PaperLetter|Letter (8-1/2 in. x 11 in.)|
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|
|PaperNote|Note (8-1/2 in. x 11 in.)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|
|PaperTabloid|Tabloid (11 in. x 17 in.)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **جودة الطباعة**

قم بتعيين جودة الطباعة لصفحات العمل التي سيتم طباعتها باستخدام طريقة [**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) لفئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). وحدة قياس جودة الطباعة هي النقاط في البوصة (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **رقم الصفحة الأولى**

ابدأ ترقيم صفحات ورقة العمل باستخدام طريقة [**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) لفئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). تقوم طريقة setFirstPageNumber بتعيين رقم الصفحة الخاص بالورقة الأولى وترقيم الصفحات التالية بترتيب تصاعدي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **ضبط الهوامش**

تدعم Aspose.Cells تماماً خيارات إعداد الصفحة في Microsoft Excel. قد يحتاج المطورون إلى تكوين إعدادات إعداد الصفحة للوظائف للتحكم في عملية الطباعة. يناقش هذا الموضوع كيفية استخدام Aspose.Cells لتكوين هوامش الصفحة.

**الهوامش في Microsoft Excel**

![todo:image_alt_text](page-setup-features_2.png)

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة Workbook على مجموعة من ورقات العمل التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة العمل تُمثل بفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

توفر فئة Worksheet خاصية PageSetup، يُستخدم لتعيين خيارات إعداد الصفحة. PageSetup هو كائن من فئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) مما يجعل من الممكن تعيين خيارات تخطيط الصفحة المختلفة لورقة عمل مطبوعة. توفر فئة PageSetup خصائص وأساليب مختلفة تُستخدم لتعيين خيارات إعداد الصفحة.

### **هوامش الصفحة**

قم بتعيين الهوامش (اليسارية، والصحيحة، والعلوية، والسفلية) لصفحة باستخدام أعضاء فئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). يتم سرد بعض الأساليب المستخدمة لتحديد الهوامش أدناه:

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **توسيط على الصفحة**

من الممكن توسيط شيء ما على الصفحة أفقيًا ورأسيًا. فئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) تحتوي على أعضاء لهذا الغرض: [**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) و [**setCenterVertically**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **هوامش الرأس والتذييل**

قم بتعيين هوامش الرأس والتذييل بأعضاء [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) مثل [**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) و [**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **ضبط رؤساء الصفحات وتذايلها**

الرؤوس والتذاييل هي أقسام النصوص والصور فوق الهامش العلوي أو أسفل الهامش السفلي على الصفحة. من الممكن إضافة رؤوس وأذيال إلى ورقات العمل أيضًا. يمكن استخدام الرؤوس والأذيال لعرض أي نوع من المعلومات المفيدة، على سبيل المثال رقم الصفحة، اسم المؤلف، عنوان المستند أو التاريخ والوقت. كما يتم إدارة الرؤوس والتذاييل باستخدام مربع حوار إعداد الصفحة.

**مربع حوار إعداد الصفحة** 

![todo:image_alt_text](page-setup-features_3.png)

يسمح Aspose.Cells بإضافة رؤوس وتذاييل إلى ورقات العمل في وقت التشغيل ولكن من المستحسن تعيين الرؤوس والتذاييل يدويًا في ملف مصمم مسبقًا للطباعة. يمكنك استخدام Microsoft Excel كأداة واجهة المستخدم الرسومية لتعيين رؤوس وتذاييل بسهولة لتقليل وقت التطوير. يمكن لـ Aspose.Cells استيراد الملف واحتفاظ به بهذه الإعدادات.

لإضافة رؤوس وأذيال في وقت التشغيل، يوفر Aspose.Cells فئات خاصة وبعض الأوامر النصية للتحكم في التنسيق.

### **أوامر السكريبت**

أوامر النص هي أوامر خاصة توفرها Aspose.Cells التي تسمح للمطورين بتنسيق رؤوس الصفحات وتذييلها.

| **أوامر السكريبت** | **الوصف** |
| :- | :- |
|&P|رقم الصفحة الحالي.
|&G|صورة.
|&N|إجمالي عدد الصفحات.
|&D|التاريخ الحالي.
|&T|الوقت الحالي.
|&A|اسم ورقة العمل.
|&F|اسم الملف بدون المسار.
|&&Text|يعرض &Text. على سبيل المثال: &&WO سيتم عرضه كـ &WO|
|&"\<FontName>"|اسم الخط. على سبيل المثال: &"Arial"|
|&"\<FontName>, \<FontStyle>"|اسم الخط مع النمط. على سبيل المثال: &"Arial،Bold"|
|&\<FontSize>| - يمثل حجم الخط. على سبيل المثال: “&14abc”. ولكن، إذا تبعت هذه الأمر برقم عادي يتم طباعته في الرأس، يجب أن يتم فصله بحرف مسافة عن حجم الخط. على سبيل المثال: “&14 123”.

### **تعيين رؤوس وتذييلات**

توفر الـ [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) طريقة [**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader-int-java.lang.String-) لإضافة رأس و [**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter-int-java.lang.String-) لإضافة تذييل إلى صفحة العمل. يتم استخدام البرنامج النصي كوسيط لجميع الطرق المذكورة أعلاه. يُمثّل البرنامج النصي البرنامج النصي الذي سيُستخدم في رأس أو تذييل. يحتوي هذا البرنامج النصي على أوامر برمجية لتنسيق الرؤوس أو التذايلات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **إدراج رسم بياني في رأس أو تذييل**

تحتوي الـ [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) على الطرق [**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture-int-byte[]-) و [**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture-int-byte[]-) لإضافة صور إلى رأس وتذييل صفحة العمل. تأخذ هذه الطرق معلمتين:

- **القسم**, قسم الرأس أو التذييل الذي سيتم وضع الصورة فيه. هناك ثلاثة أقسام: اليسار، الوسط، واليمين، يتمثل في القيم الرقمية 0، 1، و2 على التوالي.
- **مدخل ملف التدفق**, البيانات الرسومية. يجب كتابة البيانات الثنائية في مخزن مصفوفة بايت.

بعد تنفيذ الشيفرة وفتح الملف، تحقق من رأس ورقة العمل في برنامج Microsoft Excel:

1. في قائمة **ملف**, حدد **إعداد الصفحة**.
1. في مربع حوار إعداد الصفحة، حدد علامة التبويب **رأس/تذييل**.

**إدراج رسم بياني في رأس/تذييل** 

![todo:image_alt_text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **إدراج رسم بياني في رأس الصفحة الأولى فقط**

تحتوي الـ [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) أيضاً على طرق مفيدة أخرى، على سبيل المثال [**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture-boolean-boolean-boolean-int-byte[]-)، [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader-int-java.lang.String-)، [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter-int-java.lang.String-)، لإضافة الصور إلى رأس/تذييل صفحة العمل الأولى. الصفحة الأولى هي صفحة خاصة: فمن مشترك أن ترغب في إظهار معلومات خاصة بها، على سبيل المثال شعار الشركة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **ضبط خيارات الطباعة**

إعدادات صفحة Microsoft Excel توفر العديد من خيارات الطباعة (المشار إليها أيضًا بخيارات الورقة) التي تتيح للمستخدمين التحكم في كيفية طباعة صفحات جداول البيانات. تتيح هذه الخيارات الطباعة للمستخدمين:

- تحديد منطقة طباعة معينة على ورقة عمل.
- طباعة العناوين.
- طباعة خطوط الشبكة.
- طباعة رؤوس الأعمدة والصفوف
- تحقيق جودة مسودة.
- طباعة التعليقات.
- طباعة أخطاء الخلية.
- تعريف ترتيب الصفحات.

تم إظهار جميع هذه خيارات الطباعة أدناه.

**خيارات الطباعة (الورقة)** 

![todo:image_alt_text](page-setup-features_5.png)

### **ضبط خيارات الطباعة والورقة**

تدعم spose.Cells جميع خيارات الطباعة المقدمة من Microsoft Excel ويمكن للمطورين تكوين هذه الخيارات بسهولة لجداول البيانات باستخدام الخصائص التي تقدمها فئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). يتم مناقشة كيفية استخدام هذه الخصائص بشيء من التفصيل أدناه.

### **تعيين منطقة الطباعة**

بشكل افتراضي، تشمل منطقة الطباعة فقط جميع مناطق ورق العمل التي تحتوي على بيانات. يمكن للمطورين إنشاء منطقة طباعة محددة لورق العمل.

لتحديد منطقة طباعة محددة، استخدم خاصية [**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) لفئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). قم بتعيين نطاق الخلايا الذي يحدد منطقة الطباعة لهذه الخاصية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **تحديد عناوين الطباعة**

تسمح Aspose.Cells لك بتعيين تكرار رؤوس الصف والعمود على جميع الصفحات من ورقة العمل المطبوعة. للقيام بذلك، استخدم خاصيتي [**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) و [**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) لفئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup).

يتم تعريف الصفوف أو الأعمدة التي ستتكرر عن طريق تمرير أرقامها. على سبيل المثال، يتم تعريف الصفوف كـ $1:$2 والأعمدة كـ $A:$B.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **تحديد خيارات الطباعة الأخرى**

توفر فئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) أيضًا عدة خصائص أخرى لتعيين خيارات الطباعة العامة على النحو التالي:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines)، خاصية بوليانية تحدد ما إذا كان سيتم طباعة خطوط الشبكة أم لا.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings)، خاصية بوليانية تحدد ما إذا كان سيتم طباعة رؤوس الصف والعمود أم لا.
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite)، خاصية بوليانية تحدد ما إذا كان سيتم طباعة ورقة العمل في وضع أبيض وأسود أم لا.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)، يحدد ما إذا كان سيتم عرض التعليقات على الورقة أم عند نهاية الورقة.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft)، خاصية بوليانية تحدد ما إذا كان سيتم طباعة ورقة العمل في جودة المسودة أم لا.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)، يحدد ما إذا كان سيتم طباعة أخطاء الخلية كما هو معروض، فارغ، شرطة أو N/A.

لتعيين الخصائص [**PrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) و [**PrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)، توفر Aspose.Cells أيضًا تعدادين، [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) و [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) التي تحتوي على قيم محددة مسبقًا لتعيين الخصائص [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) و [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) على التوالي.

توصف القيم المحددة مسبقاً في تعداد [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) أدناه.

|**أنواع التعليقات المطبوعة**|**الوصف**|
| :- | :- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-IN-PLACE)|تحدد طباعة التعليقات كما هو معروض على ورقة العمل.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-NO-COMMENTS)|تحدد عدم طباعة التعليقات.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-SHEET-END)|تحدد طباعة التعليقات في نهاية ورقة العمل.|

توصف القيم المحددة مسبقاً في تعداد [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) أدناه.

| **أنواع أخطاء الطباعة** | **الوصف** |
| :- | :- |
|[**PRINT_ERRORS_BLANK**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-BLANK)|تحدد عدم طباعة الأخطاء.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DASH)|تحدد طباعة الأخطاء على شكل "--".|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DISPLAYED)|تحدد طباعة الأخطاء كما هو معروض.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-NA)|تحدد طباعة الأخطاء على شكل "#N/A".|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **تحديد ترتيب الصفحة**

توفر فئة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) خاصية [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) التي تُستخدم لترتيب عدة صفحات من ورقة العمل الخاصة بك ليتم طباعتها. هناك احتمالين لترتيب الصفحات كما يلي:

- **أسفل ثم يمين** يطبع كل الصفحات لأسفل قبل طباعة أي صفحات لليمين.
- **يمين ثم أسفل** يطبع الصفحات من اليسار إلى اليمين قبل طباعة أي صفحات أسفل.

توفر Aspose.Cells تعدادًا، [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType)، يحتوي على جميع أنواع ترتيب محددة مسبقًا لتعيينها لوسيطة [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order).

تُوصف القيم المحددة مسبقًا لتعداد [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) أدناه.

| **أنواع ترتيب الطباعة** | **الوصف** |
| :- | :- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN-THEN-OVER)|طباعة إلى الأسفل، ثم إلى اليمين.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER-THEN-DOWN)|طباعة إلى اليمين، ثم إلى الأسفل.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **إزالة إعدادات الطابعة الحالية لورقات العمل في ملف Excel**

يرجى الاطلاع على هذه المقالة ذات الصلة بهذا الموضوع.

## **مواضيع متقدمة**
- [حساب معامل تكبير إعداد الصفحة](/cells/ar/java/calculate-page-setup-scaling-factor/)
- [نسخ إعدادات إعداد الصفحة من ورقة العمل المصدر إلى ورقة العمل الوجهة](/cells/ar/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [تحديد ما إذا كان حجم الورق للورقة تلقائي](/cells/ar/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [الحصول على عرض وارتفاع الورقة من تهيئة الصفحة لورقة العمل](/cells/ar/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [تنفيذ حجم ورق مخصص لورقة العمل للتقديم](/cells/ar/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [إعداد الصفحة وخيارات الطباعة](/cells/ar/java/page-setup-and-printing-options/)
- [إزالة إعدادات الطابعة الحالية لورقات العمل في ملف Excel](/cells/ar/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
{{< app/cells/assistant language="java" >}}
