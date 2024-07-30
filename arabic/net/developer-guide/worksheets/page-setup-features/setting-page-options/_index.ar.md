---
title: ضبط خيارات الصفحة
type: docs
weight: 10
url: /ar/net/setting-page-options/
description: يوفر هذا المقال رمزًا عينيًا لتعيين خيارات الصفحة لورق العمل في Excel برمجيًا باستخدام واجهة برمجة التطبيقات C# ومكتبة .NET. ستكون قادرًا على تعيين التوجيه الصفحة، عامل التحجيم، خيارات FitToPages، حجم الورق، جودة الطباعة، ورقم الصفحة الأولى.
keywords: تعيين توجيه صفحة اكسل c#، تعيين عامل التحجيم اكسل c#، تعيين حجم ورق ورقات اكسل c#
---

{{% alert color="primary" %}}

في بعض الأحيان، من الضروري تكوين إعدادات إعداد الصفحة لورقات العمل للتحكم في الطباعة. توفر هذه الإعدادات خيارات مختلفة.

{{% /alert %}}

## **ضبط خيارات الصفحة**

تدعم خيارات إعداد الصفحة بالكامل في Aspose.Cells. يشرح هذا المقال كيفية ضبط خيارات الصفحة مع Aspose.Cells ويعرض عينات الشفرة للضبط:

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تمثل ملف Microsoft Excel. فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تحتوي على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) الخاصية [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) التي تُستخدم لضبط خيارات إعداد صفحة الورقة العمل. في الواقع، تكون هذه الخاصية [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) كائن من فئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) المستخدمة لتعيين خيارات تخطيط الصفحة المختلفة لورقة عمل مُطبوعة. توفر فئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) خصائص مختلفة تُستخدم لضبط خيارات إعداد الصفحة. يتم مناقشة بعض هذه الخصائص أدناه.

### **اتجاه الصفحة**

يمكن تعيين توجيه الصفحة إما عموديًا أو أفقيًا باستخدام الخاصية [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) من الفئة [**Orientation**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation). تقبل الخاصية [**Orientation**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) واحدًا من القيم المحددة مسبقًا في تعداد [**PageOrientationType**](https://reference.aspose.com/cells/net/aspose.cells/pageorientationtype) المُدرجة أدناه.

|**أنواع توجيه الصفحة**|**الوصف**|
| :- | :- |
|Landscape| توجيه أفقي|
|Portrait| توجيه عمودي|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-PageOrientation-1.cs" >}}

### **عامل التحليل**

من الممكن تصغير أو تكبير حجم ورقة العمل عن طريق ضبط عامل التحجيم باستخدام الخاصية [**PageSetup.Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ScalingFactor-1.cs" >}}

### **خيارات FitToPages**

لتناسب محتويات ورقة العمل إلى عدد معين من الصفحات، استخدم الخاصية [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) و [**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) من فئة [**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide). يُستخدم هذه الخصائص أيضًا لتحجيم ورقات العمل.

{{% alert color="primary" %}}

يمكنك اختيار إما الخاصية [**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)/[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide) أو الخاصية [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)، ولكن ليس كليهما في نفس الوقت.

{{% /alert %}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-FitToPagesOptions-1.cs" >}}

### **حجم ورق**

ضبط حجم الورق الذي ستتم طباعة الأوراق عليه باستخدام الخاصية [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) من الفئة [**PaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize). تقبل الخاصية [**PaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) واحدًا من القيم المحددة مسبقًا في تعداد [**PaperSizeType**](https://reference.aspose.com/cells/net/aspose.cells/papersizetype) المُدرجة أدناه.

|**أنواع حجم الورق**|**الوصف**|
| :- | :- |
|PaperLetter|Letter (8-1/2 in. x 11 in.)|
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|
|PaperTabloid|Tabloid (11 in. x 17 in.)|
|PaperLedger|Ledger (17 in. x 11 in.)|
|PaperLegal|Legal (8-1/2 in. x 14 in.)|
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|
|PaperExecutive|Executive (7-1/4 in. x 10-1/2 in.)|
|PaperA3|A3 (297 mm x 420 mm)|
|PaperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PaperA5|A5 (148 mm x 210 mm)|
|PaperB4|JIS B4 (257 mm x 364 mm)|
|PaperB5|JIS B5 (182 mm x 257 mm)|
|PaperFolio|Folio (8-1/2 in. x 13 in.)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|Paper10x14|10 in. x 14 in.|
|Paper11x17|11 in. x 17 in.|
|PaperNote|Note (8-1/2 in. x 11 in.)|
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|
|PaperCSheet|C size sheet|
|PaperDSheet|D size sheet|
|PaperESheet|E size sheet|
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|
|PaperEnvelopeC6 |Envelope C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|
|PaperISOB4|B4 (ISO) 250 x 353 mm|
|PaperJapanesePostcard|Japanese Postcard (100mm x 148mm)|
|Paper9x11|9 in. x 11 in.|
|Paper10x11|10 in. x 11 in.|
|Paper15x11|15 in. x 11 in.|
|PaperEnvelopeInvite|Envelope Invite(220mm x 220mm)|
|PaperLetterExtra|US Letter Extra 9 \275 x 12 in|
|PaperLegalExtra|US Legal Extra 9 \275 x 15 in|
|PaperTabloidExtra|US Tabloid Extra 11.69 x 18 in|
|PaperA4Extra|A4 Extra 9.27 x 12.69 in|
|PaperLetterTransverse|Letter Transverse 8 \275 x 11 in|
|PaperA4Transverse|A4 Transverse 210 x 297 mm|
|PaperLetterExtraTransverse|Letter Extra Transverse 9\275 x 12 in|
|PaperSuperA|SuperA/SuperA/A4 227 x 356 mm|
|PaperSuperB|SuperB/SuperB/A3 305 x 487 mm|
|PaperLetterPlus|US Letter Plus 8.5 x 12.69 in|
|PaperA4Plus|A4 Plus 210 x 330 mm|
|PaperA5Transverse|A5 Transverse 148 x 210 mm|
|PaperJISB5Transverse|B5 (JIS) Transverse 182 x 257 mm|
|PaperA3Extra|A3 Extra 322 x 445 mm|
|PaperA5Extra|A5 Extra 174 x 235 mm|
|PaperISOB5Extra|B5 (ISO) Extra 201 x 276 mm|
|PaperA2|A2 420 x 594 mm|
|PaperA3Transverse|A3 Transverse 297 x 420 mm|
|PaperA3ExtraTransverse|A3 Extra Transverse 322 x 445 mm|
|PaperJapaneseDoublePostcard|Japanese Double Postcard 200 x 148 mm|
|PaperA6|A6 105 x 148 mm|
|PaperJapaneseEnvelopeKaku2|Japanese Envelope Kaku #2|
|PaperJapaneseEnvelopeKaku3|Japanese Envelope Kaku #3|
|PaperJapaneseEnvelopeChou3|Japanese Envelope Chou #3|
|PaperJapaneseEnvelopeChou4|Japanese Envelope Chou #4|
|PaperLetterRotated|11in x 8.5in|
|PaperA3Rotated|420mm x 297mm|
|PaperA4Rotated|297mm x 210mm|
|PaperA5Rotated|210mm x 148mm|
|PaperJISB4Rotated|B4 (JIS) Rotated 364 x 257 mm|
|PaperJISB5Rotated|B5 (JIS) Rotated 257 x 182 mm|
|PaperJapanesePostcardRotated|Japanese Postcard Rotated 148 x 100 mm|
|PaperJapaneseDoublePostcardRotated|Double Japanese Postcard Rotated 148 x 200 mm|
|PaperA6Rotated|A6 Rotated 148 x 105 mm|
|PaperJapaneseEnvelopeKaku2Rotated|Japanese Envelope Kaku #2 Rotated|
|PaperJapaneseEnvelopeKaku3Rotated|Japanese Envelope Kaku #3 Rotated|
|PaperJapaneseEnvelopeChou3Rotated|Japanese Envelope Chou #3 Rotated|
|PaperJapaneseEnvelopeChou4Rotated|Japanese Envelope Chou #4 Rotated|
|PaperJISB6|B6 (JIS) 128 x 182 mm|
|PaperJISB6Rotated|B6 (JIS) Rotated 182 x 128 mm|
|Paper12x11|12 x 11 in|
|PaperJapaneseEnvelopeYou4|Japanese Envelope You #4|
|PaperJapaneseEnvelopeYou4Rotated|Japanese Envelope You #4 Rotated|
|PaperPRC16K|PRC 16K 146 x 215 mm|
|PaperPRC32K|PRC 32K 97 x 151 mm|
|PaperPRCBig32K|PRC 32K(Big) 97 x 151 mm|
|PaperPRCEnvelope1|PRC Envelope #1 102 x 165 mm|
|PaperPRCEnvelope2|PRC Envelope #2 102 x 176 mm|
|PaperPRCEnvelope3|PRC Envelope #3 125 x 176 mm|
|PaperPRCEnvelope4|PRC Envelope #4 110 x 208 mm|
|PaperPRCEnvelope5|PRC Envelope #5 110 x 220 mm|
|PaperPRCEnvelope6|PRC Envelope #6 120 x 230 mm|
|PaperPRCEnvelope7|PRC Envelope #7 160 x 230 mm|
|PaperPRCEnvelope8|PRC Envelope #8 120 x 309 mm|
|PaperPRCEnvelope9|PRC Envelope #9 229 x 324 mm|
|PaperPRCEnvelope10|PRC Envelope #10 324 x 458 mm|
|PaperPRC16KRotated|PRC 16K Rotated|
|PaperPRC32KRotated|PRC 32K Rotated|
|PaperPRCBig32KRotated|PRC 32K(Big) Rotated|
|PaperPRCEnvelope1Rotated|PRC Envelope #1 Rotated 165 x 102 mm|
|PaperPRCEnvelope2Rotated|PRC Envelope #2 Rotated 176 x 102 mm|
|PaperPRCEnvelope3Rotated|PRC Envelope #3 Rotated 176 x 125 mm|
|PaperPRCEnvelope4Rotated|PRC Envelope #4 Rotated 208 x 110 mm|
|PaperPRCEnvelope5Rotated|PRC Envelope #5 Rotated 220 x 110 mm|
|PaperPRCEnvelope6Rotated|PRC Envelope #6 Rotated 230 x 120 mm|
|PaperPRCEnvelope7Rotated|PRC Envelope #7 Rotated 230 x 160 mm|
|PaperPRCEnvelope8Rotated|PRC Envelope #8 Rotated 309 x 120 mm|
|PaperPRCEnvelope9Rotated|PRC Envelope #9 Rotated 324 x 229 mm|
|PaperPRCEnvelope10Rotated|PRC Envelope #10 Rotated 458 x 324 mm|
|PaperB3|usual B3(13.9 x 19.7 in)|
|PaperBusinessCard|Business Card(90mm x 55 mm)|
|PaperThermal|Thermal(3 x 11 in)|
|Custom|Represents the custom paper size.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ManagePaperSize-1.cs" >}}

### **جودة الطباعة**

قم بتعيين جودة الطباعة لصفحات العمل التي يتم طباعتها باستخدام خصائص الفئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) والخاصية [**PrintQuality**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printquality). وحدة القياس لجودة الطباعة هي النقاط في البوصة (DPI).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintQuality-1.cs" >}}

### **رقم الصفحة الأولى**

ابدأ ترقيم صفحات ورق العمل باستخدام خاصية الفئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) والخاصية [**FirstPageNumber**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber). تقوم الخاصية [**FirstPageNumber**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber) بتعيين رقم الصفحة الأولى في ورق العمل ويتم ترقيم الصفحات التالية بترتيب تصاعدي.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetFirstPageNumber-1.cs" >}}
