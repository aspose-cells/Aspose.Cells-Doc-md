---
title: ميزات إعداد الصفحة
type: docs
weight: 40
url: /ar/java/page-setup-features/
---
في بعض الأحيان ، من الضروري تكوين إعدادات إعداد الصفحة لأوراق العمل للتحكم في الطباعة. توفر إعدادات إعداد الصفحة هذه خيارات متنوعة.

**خيارات الصفحة** 

![ما يجب القيام به: image_بديل_نص](page-setup-features_1.png)

خيارات إعداد الصفحة مدعومة بالكامل في Aspose.Cells. تشرح هذه المقالة كيفية تعيين خيارات الصفحة مع Aspose.Cells.

## **ضبط خيارات الصفحة**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. تحتوي فئة المصنف على مجموعة أوراق عمل تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي.

توفر فئة ورقة العمل خاصية PageSetup المستخدمة لتعيين خيارات إعداد الصفحة. في الواقع ، تعد خاصية PageSetup أحد عناصر فئة PageSetup التي تجعل من الممكن تعيين خيارات تخطيط الصفحة لورقة عمل مطبوعة. توفر فئة PageSetup خصائص متنوعة تُستخدم لتعيين خيارات إعداد الصفحة. تمت مناقشة بعض هذه الخصائص أدناه.

### **اتجاه الصفحة**

يمكن ضبط اتجاه الصفحة على عمودي أو أفقي باستخدام امتداد[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) صف دراسي'[**setOrientation (PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) طريقة. ال[**setOrientation (PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) طريقة يأخذ[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) التعداد كمعامل. أعضاء[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) التعداد مذكور أدناه.

|**أنواع اتجاه الصفحة**|**وصف**|
|:- |:- |
|[**المناظر الطبيعيه**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|اتجاه أفقي|
|[**لَوحَة**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|اتجاه عمودي|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **عامل التحجيم**

 من الممكن تصغير حجم ورقة العمل أو تكبيره عن طريق ضبط عامل التحجيم بامتداد[**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) طريقة[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) صف دراسي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **خيارات FitToPages**

 لملاءمة محتويات ورقة العمل مع عدد محدد من الصفحات ، استخدم ملحق[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) صف دراسي'[**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) و[**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) أساليب. تُستخدم هذه الطرق أيضًا لتوسيع نطاق أوراق العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **حجم الورق**

 عيّن حجم الورق الذي ستتم طباعة أوراق العمل عليه باستخدام ملف[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) صف دراسي'[**حجم الورق**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) خاصية. تقبل الخاصية PaperSize إحدى القيم المحددة مسبقًا في ملف[**حجم الورق**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType) التعداد ، المدرجة أدناه.

|**أنواع أحجام الورق**|**وصف**|
|:- |:- |
|ورق|10 بوصة × 14 بوصة.|
|ورق|11 بوصة × 17 بوصة.|
|الورق|A3 (297 مم × 420 مم)|
|الورق|A4 (210 مم × 297 مم)|
|PaperA4Small|A4 صغير (210 مم × 297 مم)|
|الورق|A5 (148 مم × 210 مم)|
|الورق|B3 (13.9 × 19.7 بوصة)|
|الورق|B4 (250 مم × 354 مم)|
|الورق|B5 (182 مم × 257 مم)|
|PaperBusinessCard|بطاقة عمل (90 مم × 55 مم)|
|PaperCSheet|ورقة بحجم C.|
|ورقة|ورقة بحجم D|
|مغلف الورق 10|مغلف رقم 10 (4-1 / 8 بوصة × 9-1 / 2 بوصة)|
|مغلف الورق 11|مغلف رقم 11 (4-1 / 2 بوصة × 10-3 / 8 بوصة)|
|مغلف الورق 12|مغلف رقم 12 (4-1 / 2 بوصة × 11 بوصة)|
|مغلف الورق 14|مغلف رقم 14 (5 بوصة × 11-1 / 2 بوصة)|
|مغلف الورق 9|مغلف رقم 9 (3-7 / 8 بوصة × 8-7 / 8 بوصة)|
|PaperEnvelopeB4|مغلف B4 (250 مم × 353 مم)|
|PaperEnvelopeB5|مغلف B5 (176 مم × 250 مم)|
|PaperEnvelopeB6|مغلف B6 (176 مم × 125 مم)|
|PaperEnvelopeC3|Envelope C3 (324 مم × 458 مم)|
|PaperEnvelopeC4|مغلف C4 (229 مم × 324 مم)|
|PaperEnvelopeC5|مغلف C5 (162 ملم × 229 ملم)|
|PaperEnvelopeC6|مغلف C6 (114 مم × 162 مم)|
|PaperEnvelopeC65|مغلف C65 (114 مم × 229 مم)|
|PaperEnvelopeDL|مغلف DL (110 ملم × 220 ملم)|
|PaperEnvelope إيطاليا|مغلف إيطاليا (110 مم × 230 مم)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7 / 8 بوصة × 7-1 / 2 بوصة)|
|PaperEnvelope شخصية|مغلف (3-5 / 8 بوصة × 6-1 / 2 بوصة)|
|ورقة|ورقة حجم E|
|ورق تنفيذي|تنفيذي (7-1 / 2 بوصة × 10-1 / 2 بوصة)|
|PaperFanfold قانوني ألماني|مروحة قانونية ألمانية (8-1 / 2 بوصة × 13 بوصة)|
|PaperFanfoldStdGerman|مروحة قياسية ألمانية (8-1 / 2 بوصة × 12 بوصة)|
|طي الورق|مروحة قياسية أمريكية (14-7 / 8 بوصة × 11 بوصة)|
|PaperFolio|فوليو (8-1 / 2 بوصة × 13 بوصة)|
|PaperLedger|ليدجر (17 بوصة × 11 بوصة)|
|PaperLegal|Legal (8-1 / 2 بوصة × 14 بوصة)|
|رسالة ورقية|Letter (8-1 / 2 بوصة × 11 بوصة)|
|PaperLetterSmall|حرف صغير (8-1 / 2 بوصة × 11 بوصة)|
|ملاحظة الورق|ملاحظة (8-1 / 2 بوصة × 11 بوصة)|
|PaperQuarto|Quarto (215 مم × 275 مم)|
|البيان الورقي|بيان (5-1 / 2 بوصة × 8-1 / 2 بوصة)|
|PaperTabloid|Tabloid (11 بوصة × 17 بوصة)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **جودة الطباعة**

 اضبط جودة طباعة أوراق العمل التي ستتم طباعتها بامتداد[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) صف دراسي'[**تعيين طباعة الجودة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) طريقة. وحدة قياس جودة الطباعة هي نقطة في البوصة (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **رقم الصفحة الأولى**

 ابدأ ترقيم صفحات ورقة العمل باستخدام ملف[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) صف دراسي'[**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) طريقة. تحدد طريقة setFirstPageNumber رقم صفحة صفحة ورقة العمل الأولى ويتم ترقيم الصفحات التالية بترتيب تصاعدي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **تحديد الهوامش**

Aspose.Cells يدعم Microsoft خيارات إعداد صفحة Excel بشكل كامل. قد يحتاج المطورون إلى تكوين إعدادات إعداد الصفحة لأوراق العمل للتحكم في عملية الطباعة. يناقش هذا الموضوع كيفية استخدام Aspose.Cells لتكوين هوامش الصفحة.

**هوامش الصفحة في Microsoft Excel**

![ما يجب القيام به: image_بديل_نص](page-setup-features_2.png)

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) يمثل ملف Excel Microsoft. تحتوي فئة المصنف على مجموعة أوراق العمل التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي.

 توفر فئة ورقة العمل خاصية PageSetup المستخدمة لتعيين خيارات إعداد الصفحة. السمة PageSetup هي كائن من[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) فئة تجعل من الممكن تعيين خيارات مختلفة لتخطيط الصفحة لورقة عمل مطبوعة. توفر فئة PageSetup العديد من الخصائص والأساليب المستخدمة لتعيين خيارات إعداد الصفحة.

### **هوامش الصفحة**

 عيّن الهوامش (يسار ، يمين ، أعلى ، أسفل) الصفحة باستخدام[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) أعضاء الفصل. يتم سرد بعض الطرق المستخدمة لتحديد هوامش الصفحة أدناه:

- [**setLeftMargin (int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin (int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin (int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin (int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **توسيط في الصفحة**

 من الممكن توسيط شيء ما على الصفحة أفقيًا ورأسيًا. ال[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) الصف لديه أعضاء لهذا الغرض:[**setCenter أفقيًا**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) و[**عموديا**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **هوامش الرأس والتذييل**

 تعيين هوامش الرأس والتذييل باستخدام[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) أعضاء مثل[**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) و[**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **تعيين الرؤوس والتذييلات**

الرؤوس والتذييلات هي أقسام النص والصور أعلى الهامش العلوي أو أسفل الهامش السفلي في الصفحة. من الممكن إضافة رؤوس وتذييلات إلى أوراق العمل أيضًا. يمكن استخدام الرؤوس والتذييلات لعرض أي نوع من المعلومات المفيدة ، على سبيل المثال رقم الصفحة أو اسم المؤلف أو عنوان المستند أو التاريخ والوقت. تتم أيضًا إدارة الرؤوس والتذييلات باستخدام مربع حوار إعداد الصفحة.

**مربع حوار إعداد الصفحة** 

![ما يجب القيام به: image_بديل_نص](page-setup-features_3.png)

يسمح Aspose.Cells بإضافة رؤوس وتذييلات إلى أوراق العمل في وقت التشغيل ولكن يوصى بتعيين الرؤوس والتذييلات يدويًا في ملف مصمم مسبقًا للطباعة. يمكنك استخدام Microsoft Excel كأداة واجهة المستخدم الرسومية لضبط الرؤوس والتذييلات بسهولة لتقليل وقت التطوير. يمكن Aspose.Cells استقبال الملف وحجز هذه المحددات.

لإضافة رؤوس وتذييلات في وقت التشغيل ، يوفر Aspose.Cells فئات خاصة وبعض أوامر البرنامج النصي للتحكم في التنسيق.

### **أوامر البرنامج النصي**

أوامر البرنامج النصي هي أوامر خاصة يوفرها Aspose.Cells تسمح للمطورين بتنسيق الرؤوس والتذييلات.

|**أوامر البرنامج النصي**|**وصف**|
|:- |:- |
|& ص|رقم الصفحة الحالية.|
|& ج|صورة.|
|&ن|العدد الإجمالي للصفحات.|
|&د|التاريخ الحالي.|
|& ت|الوقت الحالي.|
|&أ|اسم ورقة العمل.|
|&F|اسم الملف بدون المسار.|
|&"\<FontName>"|اسم الخط. على سبيل المثال: & "Arial"|
|&"\<FontName>, \<FontStyle>"|اسم خط بنمط. على سبيل المثال: & "Arial، Bold"|
|&\<FontSize>|يمثل حجم الخط. على سبيل المثال: "& 14abc". ولكن ، إذا كان هذا الأمر متبوعًا برقم عادي ليتم طباعته في الرأس ، فيجب فصله بمسافة عن حجم الخط. على سبيل المثال: "& 14123".|

### **تعيين الرؤوس والتذييلات**

 ال[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) فئة توفر الطريقة[**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String) لإضافة رأس و[**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)) لإضافة تذييل إلى ورقة العمل. يستخدم البرنامج النصي كوسيطة لجميع الأساليب المذكورة أعلاه. يمثل البرنامج النصي الذي سيتم استخدامه للرأس أو التذييل. يحتوي هذا البرنامج النصي على أوامر نصية لتنسيق الرؤوس أو التذييلات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **قم بإدراج رسم في رأس أو تذييل الصفحة**

 ال[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) الصف لديه الأساليب[**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[]) ) و[**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])) لإضافة صور إلى رأس ورقة العمل وتذييلها. تأخذ هذه الطرق معلمتين:

- **الجزء**، قسم الرأس أو التذييل حيث سيتم وضع الصورة. هناك ثلاثة أقسام: اليسار والوسط واليمين ممثلة بالقيم الرقمية 0 و 1 و 2 على التوالي.
- **ملف InputStream**، البيانات الرسومية. يجب كتابة البيانات الثنائية في المخزن المؤقت لصفيف بايت.

بعد تنفيذ الكود وفتح الملف ، تحقق من رأس ورقة العمل في Microsoft Excel:

1.  على ال**ملف** القائمة ، حدد**اعداد الصفحة**.
1.  في مربع الحوار إعداد الصفحة ، حدد ملف**تذييل الرأس** التبويب.

**إدراج رسم في رأس / تذييل الصفحة** 

![ما يجب القيام به: image_بديل_نص](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **قم بإدراج رسم في رأس الصفحة الأولى فقط**

 ال[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) يحتوي class أيضًا على طرق مفيدة أخرى ، على سبيل المثال[**تعيين الصورة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)) ، لإضافة الصور إلى رأس / تذييل الصفحة الأولى لورقة العمل. الصفحة الأولى هي صفحة خاصة: من الشائع أن تريد أن تعرض معلومات خاصة ، على سبيل المثال شعار شركة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **ضبط خيارات الطباعة**

توفر إعدادات إعداد صفحة Microsoft في Excel العديد من خيارات الطباعة (يشار إليها أيضًا بخيارات الورقة) التي تسمح للمستخدمين بالتحكم في كيفية طباعة صفحات ورقة العمل. تتيح خيارات الطباعة هذه للمستخدمين:

- حدد منطقة طباعة معينة في ورقة العمل.
- طباعة العناوين.
- طباعة خطوط الشبكة.
- طباعة عناوين الصفوف والأعمدة
- تحقيق جودة المسودة.
- طباعة التعليقات.
- طباعة أخطاء الخلية.
- تحديد ترتيب الصفحة.

كل خيارات الطباعة هذه موضحة أدناه.

**خيارات الطباعة (الورقة)** 

![ما يجب القيام به: image_بديل_نص](page-setup-features_5.png)

### **ضبط خيارات الطباعة والورقة**

 spose.Cells يدعم جميع خيارات الطباعة التي يقدمها Microsoft Excel ويمكن للمطورين بسهولة تكوين هذه الخيارات لأوراق العمل باستخدام الخصائص التي تقدمها[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)صف دراسي. تتم مناقشة كيفية استخدام هذه الخصائص أدناه بمزيد من التفصيل.

### **تعيين ناحية الطباعة**

بشكل افتراضي ، تدمج منطقة الطباعة فقط جميع مناطق ورقة العمل التي تحتوي على بيانات. يمكن للمطورين إنشاء منطقة طباعة معينة من ورقة العمل.

 لتحديد منطقة طباعة معينة ، استخدم ملف[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) صف دراسي'[**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) خاصية. قم بتعيين نطاق خلايا يحدد منطقة الطباعة لهذه الخاصية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **تعيين عناوين الطباعة**

 Aspose.Cells يسمح لك بتعيين رؤوس الصفوف والأعمدة لتكرارها على كل صفحات ورقة العمل المطبوعة. للقيام بذلك ، استخدم ملف[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) صف دراسي'[**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) و[**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) الخصائص.

يتم تحديد الصفوف أو الأعمدة التي سيتم تكرارها عن طريق تمرير أرقام الصفوف أو الأعمدة. على سبيل المثال ، يتم تعريف الصفوف على أنها $ 1: $ 2 ويتم تعريف الأعمدة على أنها $ A: $ B.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **قم بتعيين خيارات الطباعة الأخرى**

 ال[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) توفر class أيضًا العديد من الخصائص الأخرى لتعيين خيارات الطباعة العامة على النحو التالي:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines)، وهي خاصية منطقية تحدد ما إذا كنت تريد طباعة خطوط الشبكة أم لا.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings)، خاصية منطقية تحدد ما إذا كنت تريد طباعة عناوين الصفوف والأعمدة أم لا.
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite)، خاصية منطقية تحدد ما إذا كنت تريد طباعة ورقة العمل في الوضع الأسود والأبيض أم لا.
- [**setPrint التعليقات**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)، يحدد ما إذا كان سيتم عرض تعليقات الطباعة في ورقة العمل أو في نهاية ورقة العمل.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft)، خاصية منطقية تحدد ما إذا كنت تريد طباعة ورقة العمل بجودة المسودة أم لا.
- [**setPrintErors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)، يحدد ما إذا كان سيتم طباعة أخطاء الخلية كما هي معروضة أو فارغة أو شرطة أو غير متوفرة.

 لتعيين[**PrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) و[**أخطاء الطباعة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) الخصائص ، يوفر Aspose.Cells أيضًا عددين ،[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) و[**نوع الطباعة**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) التي تحتوي على قيم محددة مسبقًا ليتم تعيينها إلى[**setPrint التعليقات**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) و[**setPrintErors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) خصائص على التوالي.

 القيم المحددة مسبقًا في ملف[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) التعداد موصوف أدناه.

|**طباعة أنواع التعليقات**|**وصف**|
|:- |:- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|يُحدد لطباعة التعليقات كما هو معروض في ورقة العمل.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|يحدد عدم طباعة التعليقات.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|يُحدد لطباعة التعليقات في نهاية ورقة العمل.|

 القيم المحددة مسبقًا لـ[**نوع الطباعة**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) التعداد موصوف أدناه.

|**أنواع أخطاء الطباعة**|**وصف**|
|:- |:- |
|[*PRINT_ERRORS_BLANK*](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|يحدد عدم طباعة الأخطاء.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|يُحدد طباعة الأخطاء كـ "-".|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|يُحدد لطباعة الأخطاء كما هو معروض.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|يُحدد طباعة الأخطاء كـ "# N / A".|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **تعيين ترتيب الصفحة**

 ال[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) فئة توفر[**سن أمرا**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) الخاصية المستخدمة لطلب طباعة صفحات متعددة من ورقة العمل الخاصة بك. هناك احتمالان لترتيب الصفحات على النحو التالي:

- **ثم إلى أسفل** يطبع كل الصفحات لأسفل قبل طباعة أي صفحات على اليمين.
- **مر ثم لأسفل** يطبع الصفحات من اليسار إلى اليمين قبل طباعة أية صفحات أدناه.

 يوفر Aspose.Cells تعداد ،[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) ، التي تحتوي على جميع أنواع الطلبات المحددة مسبقًا التي سيتم تعيينها لها[**سن أمرا**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) طريقة.

 القيم المحددة مسبقًا لـ[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) التعداد موصوف أدناه.

|**أنواع أوامر الطباعة**|**وصف**|
|:- |:- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|اطبع لأسفل ، ثم أكرر.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|اطبع ثم لأسفل.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **قم بإزالة إعدادات PrinterSettings الموجودة من أوراق العمل في ملف Excel**

يرجى الاطلاع على هذه المقالة المتعلقة بهذا الموضوع.

## **موضوعات مسبقة**
- [حساب عامل تحجيم إعداد الصفحة](/cells/ar/java/calculate-page-setup-scaling-factor/)
- [انسخ إعدادات إعداد الصفحة من ورقة عمل المصدر إلى ورقة عمل الوجهة](/cells/ar/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [حدد ما إذا كان حجم الورق الخاص بورقة العمل تلقائيًا](/cells/ar/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [احصل على عرض الورق وارتفاعه من PageSetup of Worksheet](/cells/ar/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [تنفيذ حجم الورق المخصص لورقة العمل للعرض](/cells/ar/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [خيارات إعداد الصفحة والطباعة](/cells/ar/java/page-setup-and-printing-options/)
- [قم بإزالة إعدادات PrinterSettings الموجودة من أوراق العمل في ملف Excel](/cells/ar/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
