---
title: ضبط خيارات الصفحة
type: docs
weight: 10
url: /ar/net/setting-page-options/
---
{{% alert color="primary" %}}

في بعض الأحيان ، من الضروري تكوين إعدادات إعداد الصفحة لأوراق العمل للتحكم في الطباعة. توفر إعدادات إعداد الصفحة هذه خيارات متنوعة.

{{% /alert %}}

## **ضبط خيارات الصفحة**

خيارات إعداد الصفحة مدعومة بالكامل في Aspose.Cells. تشرح هذه المقالة كيفية تعيين خيارات الصفحة مع Aspose.Cells وتعرض نماذج التعليمات البرمجية للإعداد:

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)صف دراسي.

 ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)فئة توفر[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) الخاصية المستخدمة لتعيين خيارات إعداد الصفحة لورقة العمل. في الواقع ، هذا[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) الخاصية هي كائن من[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) فئة تستخدم لتعيين خيارات تخطيط صفحة مختلفة لورقة عمل مطبوعة. ال[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)توفر فئة الخصائص المختلفة المستخدمة لتعيين خيارات إعداد الصفحة. تمت مناقشة بعض هذه الخصائص أدناه.

### **اتجاه الصفحة**

 يمكن ضبط اتجاه الصفحة على عمودي أو أفقي باستخدام امتداد[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) صف دراسي'[**توجيه**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) منشأه. ال[**توجيه**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) تقبل الخاصية إحدى القيم المحددة مسبقًا في ملف[**PageOrientationType**](https://reference.aspose.com/cells/net/aspose.cells/pageorientationtype)التعداد ، المدرجة أدناه.

|**أنواع اتجاه الصفحة**|**وصف**|
|:- |:- |
|المناظر الطبيعيه|اتجاه أفقي|
|لَوحَة|اتجاه عمودي|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-PageOrientation-1.cs" >}}

### **عامل التحجيم**

 من الممكن تصغير حجم ورقة العمل أو تكبيره عن طريق ضبط عامل التحجيم بامتداد[**PageSetup.Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)منشأه.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ScalingFactor-1.cs" >}}

### **خيارات FitToPages**

 لملاءمة محتويات ورقة العمل مع عدد محدد من الصفحات ، استخدم ملحق[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) صف دراسي'[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) و[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)الخصائص. تُستخدم هذه الخصائص أيضًا لتوسيع نطاق أوراق العمل.

{{% alert color="primary" %}}

 يمكنك إما اختيار[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)/[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide) أو ال[**تكبير**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom) ولكن ليس كلاهما في نفس الوقت.

{{% /alert %}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-FitToPagesOptions-1.cs" >}}

### **حجم الورق**

 عيّن حجم الورق الذي ستتم طباعة أوراق العمل عليه باستخدام ملف[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) صف دراسي'[**حجم الورق**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) منشأه. ال[**حجم الورق**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) تقبل الخاصية إحدى القيم المحددة مسبقًا في ملف[**حجم الورق**](https://reference.aspose.com/cells/net/aspose.cells/papersizetype)التعداد ، المدرجة أدناه.

|**أنواع أحجام الورق**|**وصف**|
|:- |:- |
|رسالة ورقية|Letter (8-1 / 2 بوصة × 11 بوصة)|
|PaperLetterSmall|حرف صغير (8-1 / 2 بوصة × 11 بوصة)|
|PaperTabloid|Tabloid (11 بوصة × 17 بوصة)|
|PaperLedger|ليدجر (17 بوصة × 11 بوصة)|
|PaperLegal|Legal (8-1 / 2 بوصة × 14 بوصة)|
|البيان الورقي|بيان (5-1 / 2 بوصة × 8-1 / 2 بوصة)|
|ورق تنفيذي|تنفيذي (7-1 / 4 بوصة × 10-1 / 2 بوصة)|
|الورق|A3 (297 مم × 420 مم)|
|الورق|A4 (210 مم × 297 مم)|
|PaperA4Small|A4 صغير (210 مم × 297 مم)|
|الورق|A5 (148 مم × 210 مم)|
|الورق|JIS B4 (257 مم × 364 مم)|
|الورق|JIS B5 (182 مم × 257 مم)|
|PaperFolio|فوليو (8-1 / 2 بوصة × 13 بوصة)|
|PaperQuarto|Quarto (215 مم × 275 مم)|
|ورق|10 بوصة × 14 بوصة.|
|ورق|11 بوصة × 17 بوصة.|
|ملاحظة الورق|ملاحظة (8-1 / 2 بوصة × 11 بوصة)|
|مغلف الورق 9|مغلف رقم 9 (3-7 / 8 بوصة × 8-7 / 8 بوصة)|
|مغلف الورق 10|مغلف رقم 10 (4-1 / 8 بوصة × 9-1 / 2 بوصة)|
|مغلف الورق 11|مغلف رقم 11 (4-1 / 2 بوصة × 10-3 / 8 بوصة)|
|مغلف الورق 12|مغلف رقم 12 (4-1 / 2 بوصة × 11 بوصة)|
|مغلف الورق 14|مغلف رقم 14 (5 بوصة × 11-1 / 2 بوصة)|
|PaperCSheet|ورقة بحجم C.|
|ورقة|ورقة بحجم D|
|ورقة|ورقة حجم E|
|PaperEnvelopeDL|مغلف DL (110 ملم × 220 ملم)|
|PaperEnvelopeC5|مغلف C5 (162 ملم × 229 ملم)|
|PaperEnvelopeC3|Envelope C3 (324 مم × 458 مم)|
|PaperEnvelopeC4|مغلف C4 (229 مم × 324 مم)|
|PaperEnvelopeC6|مغلف C6 (114 مم × 162 مم)|
|PaperEnvelopeC65|مغلف C65 (114 مم × 229 مم)|
|PaperEnvelopeB4|مغلف B4 (250 مم × 353 مم|
|PaperEnvelopeB5|مغلف B5 (176 مم × 250 مم)|
|PaperEnvelopeB6|مغلف B6 (176 مم × 125 مم)|
|PaperEnvelope إيطاليا|مغلف إيطاليا (110 مم × 230 مم)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7 / 8 بوصة × 7-1 / 2 بوصة)|
|PaperEnvelope شخصية|مغلف (3-5 / 8 بوصة × 6-1 / 2 بوصة)|
|طي الورق|مروحة قياسية أمريكية (14-7 / 8 بوصة × 11 بوصة)|
|PaperFanfoldStdGerman|مروحة قياسية ألمانية (8-1 / 2 بوصة × 12 بوصة)|
|PaperFanfold قانوني ألماني|مروحة قانونية ألمانية (8-1 / 2 بوصة × 13 بوصة)|
|الورق|B4 (ISO) 250 × 353 مم|
|الورق اليابانية|بطاقة بريدية يابانية (100 مم × 148 مم)|
|ورق|9 بوصة × 11 بوصة.|
|ورق|10 بوصة × 11 بوصة.|
|ورق|15 بوصة × 11 بوصة.|
|PaperEnvelopeInvite|دعوة مغلف (220 مم × 220 مم)|
|PaperLetterExtra|رسالة أمريكية إضافية 9 \ 275 × 12 بوصة|
|PaperLegalExtra|US Legal Extra 9 \ 275 × 15 بوصة|
|PaperTabloidExtra|US Tabloid Extra 11.69 × 18 بوصة|
|PaperA4Extra|A4 إضافي 9.27 × 12.69 بوصة|
|PaperLetterTransverse|مستعرضة للأحرف 8 \ 275 × 11 بوصة|
|PaperA4Transverse|A4 عرضي 210 × 297 مم|
|PaperLetterExtraTransverse|حرف مستعرض إضافي 9 \ 275 × 12 بوصة|
|الورق|SuperA / SuperA / A4 227 × 356 ملم|
|الورق|SuperB / SuperB / A3 305 × 487 مم|
|PaperLetterPlus|US Letter Plus 8.5 × 12.69 بوصة|
|PaperA4Plus|A4 Plus 210 × 330 مم|
|PaperA5 عرضية|A5 عرضي 148 × 210 مم|
|PaperJISB5 عرضية|B5 (JIS) عرضي 182 × 257 مم|
|PaperA3Extra|A3 Extra 322 x 445 ملم|
|PaperA5Extra|A5 Extra 174 x 235 ملم|
|PaperISOB5Extra|B5 (ISO) إضافي 201 × 276 مم|
|الورق|A2420 × 594 مم|
|ورقة A3 عرضية|A3 عرضي 297 × 420 مم|
|PaperA3ExtraTransverse|A3 عرضي إضافي 322 × 445 مم|
|PaperJapaneseDoublePostcard|بطاقة بريدية يابانية مزدوجة 200 × 148 مم|
|الورق|A6105 × 148 ملم|
|الورق الياباني EnvelopeKaku2|مغلف ياباني Kaku # 2|
|PaperJapanese EnvelopeKaku3|مغلف ياباني Kaku # 3|
|الورق الياباني EnvelopeChou3|المغلف الياباني Chou # 3|
|الورق الياباني EnvelopeChou4|المغلف الياباني Chou # 4|
|PaperLetterRotated|11in x 8.5in|
|PaperA3Rotated|420 مم × 297 مم|
|ورقة A4Rotated|297 مم × 210 مم|
|الورق A5Rotated|210 مم × 148 مم|
|PaperJISB4Rotated|B4 (JIS) استدارة 364 × 257 مم|
|PaperJISB5Rotated|B5 (JIS) استدارة 257 × 182 مم|
|PaperJapanesePostcardRotated|بطاقة بريدية يابانية استدارة 148 × 100 مم|
|ورقة يابانيةمزدوجة بريدية تدوير|بطاقة بريدية يابانية مزدوجة استدارة 148 × 200 مم|
|PaperA6Rotated|A6 استدارة 148 × 105 ملم|
|PaperJapanese EnvelopeKaku2Rotated|مغلف ياباني Kaku # 2 مستدير|
|PaperJapanese EnvelopeKaku3Rotated|مغلف ياباني Kaku # 3 مستدير|
|PaperJapanese EnvelopeChou3Rotated|المغلف الياباني Chou # 3 مستدير|
|PaperJapanese EnvelopeChou4Rotated|المغلف الياباني Chou # 4 مستدير|
|الورق|B6 (JIS) 128 × 182 ملم|
|PaperJISB6Rotated|B6 (JIS) استدارة 182 × 128 مم|
|ورق|12 × 11 بوصة|
|الورق الياباني EnvelopeYou4|مغلف ياباني You # 4|
|PaperJapanese EnvelopeYou4Rotated|مغلف ياباني You # 4 استدارة|
|الورق|PRC 16K 146 x 215 ملم|
|الورق|PRC 32K 97 × 151 ملم|
|الورق|PRC 32 كيلو (كبير) 97 × 151 مم|
|PaperPRCEnvelope1|مغلف PRC # 11102 × 165 مم|
|PaperPRCE مغلف 2|ظرف PRC # 2102 × 176 مم|
|PaperPRCE مغلف 3|مغلف PRC # 3125 × 176 مم|
|ورقة PRCEnvelope4|مغلف PRC # 4110 × 208 مم|
|ورقة PRCEnvelope5|ظرف PRC # 5110 × 220 مم|
|PaperPRCE مغلف 6|ظرف PRC # 6120 × 230 مم|
|PaperPRCE مغلف 7|ظرف PRC # 7160 × 230 مم|
|PaperPRCE مغلف 8|مغلف PRC # 8120 × 309 مم|
|ورقة PRCEnvelope9|مغلف PRC # 9229 × 324 مم|
|ورقة PRCEnvelope10|مغلف PRC # 10324 × 458 مم|
|الورق|PRC 16K مستدير|
|الورق|PRC 32K مستدير|
|الورق|PRC 32K (كبير) مستدير|
|PaperPRCEnvelope1Rotated|ظرف PRC رقم 1 استدارة 165 × 102 مم|
|PaperPRCEnvelope2Rotated|ظرف PRC # 2 مستدير 176 × 102 مم|
|PaperPRCEnvelope3Rotated|ظرف PRC # 3 مستدير 176 × 125 مم|
|PaperPRCEnvelope4Rotated|ظرف PRC # 4 مستدير 208 × 110 مم|
|PaperPRCEnvelope5Rotated|ظرف PRC # 5 مستدير 220 × 110 مم|
|PaperPRCEnvelope6Rotated|ظرف PRC # 6 مستدير 230 × 120 مم|
|PaperPRCEnvelope7Rotated|ظرف PRC # 7 مستدير 230 × 160 مم|
|PaperPRCEnvelope8Rotated|ظرف PRC رقم 8 مستدير 309 × 120 مم|
|PaperPRCEnvelope9Rotated|ظرف PRC # 9 مستدير 324 × 229 مم|
|PaperPRCEnvelope10Rotated|ظرف PRC # 10 مستدير 458 × 324 مم|
|الورق|عادي B3 (13.9 × 19.7 بوصة)|
|PaperBusinessCard|بطاقة عمل (90 مم × 55 مم)|
|ورق حراري|حراري (3 × 11 بوصة)|
|العادة|يمثل حجم الورق المخصص.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ManagePaperSize-1.cs" >}}

### **جودة الطباعة**

 اضبط جودة طباعة أوراق العمل التي ستتم طباعتها بامتداد[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) صف دراسي'[**جودة الطباعة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printquality)منشأه. وحدة قياس جودة الطباعة هي Dots Per Inches (DPI).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintQuality-1.cs" >}}

### **رقم الصفحة الأولى**

 ابدأ ترقيم صفحات ورقة العمل باستخدام ملف[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) صف دراسي'[**FirstPageNumber**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber) منشأه. ال[**FirstPageNumber**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)تحدد الخاصية رقم الصفحة في صفحة ورقة العمل الأولى ويتم ترقيم الصفحات التالية بترتيب تصاعدي.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetFirstPageNumber-1.cs" >}}
