---
title: ضبط خيارات الطباعة
type: docs
weight: 40
url: /ar/net/setting-print-options/
description: توضح هذه المقالة كيفية ضبط خيارات الطباعة لميزة تهيئة صفحة ورق العمل في Excel برمجياً باستخدام واجهة برمجة التطبيقات C# ومكتبة .NET. يمكنك ضبط منطقة الطباعة وعناوين الطباعة وترتيب الصفحات.
keywords: ضبط منطقة الطباعة في إكسيل بلغة السي #، تعيين عنواوين الطباعة في إكسل بلغة السي #، تعيين ترتيب الصفحات في إكسل بلغة السي #
---

{{% alert color="primary" %}}

توفر إعدادات تهيئة الصفحة في ميكروسوفت إكسيل العديد من خيارات الطباعة التي تسمح للمستخدمين بالتحكم في كيفية طباعة صفحات ورق العمل.

{{% /alert %}}

## **ضبط خيارات الطباعة**

تسمح هذه الخيارات بالطباعة:

- تحديد منطقة طباعة معينة على ورقة عمل.
- طباعة العناوين.
- طباعة خطوط الشبكة.
- طباعة عناوين الصفوف/الأعمدة.
- تحقيق جودة مسودة.
- طباعة التعليقات.
- طباعة أخطاء الخلية.
- تعريف ترتيب الصفحات.

تدعم Aspose.Cells جميع خيارات الطباعة التي تقدمها ميكروسوفت إكسيل ويمكن للمطورين تكوين هذه الخيارات بسهولة للورقات العمل باستخدام الخصائص التي توفرها فئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup). كيفية استخدام هذه الخصائص يتم مناقشتها أدناه بتفصيل أكثر.

### **تعيين منطقة الطباعة**

اف فعل، منطقة الطباعة تشمل جميع مناطق ورقة العمل التي تحتوي على بيانات. يمكن للمطورين تحديد منطقة الطباعة المحددة لورقة العمل.

لتحديد منطقة الطباعة المحددة، استخدم خاصية [**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea) لفئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup). قم بتعيين نطاق الخلايا الذي يعرف منطقة الطباعة لهذه الخاصية.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **تحديد عناوين الطباعة**

تسمح Aspose.Cells لك بتحديد عناوين الصف والعمود لتكرارها على جميع الصفحات لورقة العمل المطبوعة. للقيام بذلك، استخدم خاصية [**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) و [**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows) لفئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup).

يتم تعريف الصفوف أو الأعمدة التي ستتكرر عن طريق تمرير أرقامها. على سبيل المثال، يتم تعريف الصفوف كـ $1:$2 والأعمدة كـ $A:$B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **تحديد خيارات الطباعة الأخرى**

فئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) توفر أيضا عدة خصائص أخرى لتعيين خيارات الطباعة العامة على النحو التالي:

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): خاصية بوليانية تعرف ما إذا كان سيتم طباعة خطوط الشبكة أم لا.
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): خاصية بوليانية تعرف ما إذا كان سيتم طباعة عناوين الصف والعمود أم لا.
- [**BlackAndWhite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): خاصية بوليانية تعرف ما إذا كان سيتم طباعة ورقة العمل في وضع أسود وأبيض أم لا.
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): يحدد ما إذا كان سيتم عرض التعليقات المطبوعة على ورقة العمل أم في نهايتها.
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): خاصية بوليانية تعرف ما إذا كان سيتم طباعة الورقة بدون الرسومات.
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): يحدد ما إذا كان سيتم طباعة أخطاء الخلية كما هو معروض، فارغ، شرطة أو غير متوفر.

لتعيين الخصائص [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) و [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)، توفر Aspose.Cells أيضا اثنين من التعدادات، [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) و [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) التي تحتوي على قيم محددة مسبقًا لتعيين الخصائص [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) و [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) على التوالي.

تتم إدراج القيم المحددة مسبقًا في تعداد [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) أدناه مع وصفها.

|**أنواع التعليقات المطبوعة**|**الوصف**|
| :- | :- |
|PrintInPlace|تحدد طباعة التعليقات كما هي معروضة على ورقة العمل.|
|PrintNoComments|تحدد عدم طباعة التعليقات.|
|PrintSheetEnd|تحدد طباعة التعليقات في نهاية ورقة العمل.|

تم إدراج القيم المحددة مسبقًا لتعداد [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) أدناه مع وصفها.



| **أنواع أخطاء الطباعة** | **الوصف** |
| :- | :- |
|PrintErrorsBlank|يحدد عدم طباعة الأخطاء.
|PrintErrorsDash|يحدد طباعة الأخطاء على شكل "--".
|PrintErrorsDisplayed|يحدد طباعة الأخطاء على النحو الذي يتم عرضه.
|PrintErrorsNA|يحدد طباعة الأخطاء على شكل "#N/A".

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **تحديد ترتيب الصفحة**

توفر صفيف [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) خاصية [**Order**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order) التي تستخدم لترتيب صفحات ورق العمل المتعددة المطبوعة. هناك احتمالان لترتيب الصفحات على النحو التالي.

- **اسفل ثم يمين:** يطبع جميع الصفحات أسفل الصفحة قبل طباعة أي صفحات على اليمين.
- **يمين ثم أسفل:** يطبع الصفحات من اليسار إلى اليمين قبل طباعة الصفحات أسفلها.

يوفّر Aspose.Cells تعدادًا، [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)، يحتوي على جميع أنواع ترتيب محدد مسبقًا.

يتم سرد القيم المحددة مسبقًا لتعداد [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) أدناه.

| **أنواع ترتيب الطباعة** | **الوصف** |
| :- | :- |
|DownThenOver|يمثل ترتيب الطباعة كاسفل ثم يمين.
|OverThenDown|يمثل ترتيب الطباعة كيمين ثم أسفل.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
