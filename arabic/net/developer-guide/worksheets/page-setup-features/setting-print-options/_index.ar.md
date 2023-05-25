---
title: ضبط خيارات الطباعة
type: docs
weight: 40
url: /ar/net/setting-print-options/
description: توضح هذه المقالة كيفية تعيين "خيارات الطباعة" لميزة "إعداد صفحة ورقة عمل Excel" برمجيًا باستخدام مكتبة C# API و .NET. يمكنك ضبط منطقة الطباعة وعناوين الطباعة وترتيب الصفحات.
keywords: set excel print area c#, set exce print titles c#, set excel page order c#
---
{{% alert color="primary" %}}

توفر إعدادات إعداد صفحة Microsoft في Excel العديد من خيارات الطباعة (يشار إليها أيضًا بخيارات الورقة) التي تسمح للمستخدمين بالتحكم في كيفية طباعة صفحات ورقة العمل.

{{% /alert %}}

##  **ضبط خيارات الطباعة**

تتيح خيارات الطباعة هذه للمستخدمين:

- حدد منطقة طباعة معينة في ورقة العمل.
- طباعة العناوين.
- طباعة خطوط الشبكة.
- طباعة عناوين الصفوف / الأعمدة.
- تحقيق جودة المسودة.
- طباعة التعليقات.
- طباعة أخطاء الخلية.
- تحديد ترتيب الصفحة.

 يدعم Aspose.Cells جميع خيارات الطباعة التي يوفرها Microsoft Excel ويمكن للمطورين بسهولة تكوين هذه الخيارات لأوراق العمل باستخدام الخصائص التي يوفرها[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)فصل. تتم مناقشة كيفية استخدام هذه الخصائص أدناه بمزيد من التفصيل.

###  **تعيين ناحية الطباعة**

بشكل افتراضي ، تدمج منطقة الطباعة جميع مناطق ورقة العمل التي تحتوي على بيانات. يمكن للمطورين إنشاء منطقة طباعة معينة من ورقة العمل.

 لتحديد منطقة طباعة معينة ، استخدم ملف[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) فصل'[**منطقة الطباعة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)ملكية. قم بتعيين نطاق خلايا يحدد منطقة الطباعة لهذه الخاصية.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

###  **تعيين عناوين الطباعة**

 Aspose.Cells يسمح لك بتعيين رؤوس الصفوف والأعمدة لتكرارها على كل صفحات ورقة العمل المطبوعة. للقيام بذلك ، استخدم ملف[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) فصل'[**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) و[**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)ملكيات.

يتم تحديد الصفوف أو الأعمدة التي سيتم تكرارها عن طريق تمرير أرقام الصفوف أو الأعمدة. على سبيل المثال ، يتم تعريف الصفوف على أنها $ 1: $ 2 ويتم تعريف الأعمدة على أنها $ A: $ B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

###  **قم بتعيين خيارات الطباعة الأخرى**

 ال[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)توفر class أيضًا العديد من الخصائص الأخرى لتعيين خيارات الطباعة العامة على النحو التالي:

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): خاصية منطقية تحدد ما إذا كنت تريد طباعة خطوط الشبكة أم لا.
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): خاصية منطقية تحدد ما إذا كنت تريد طباعة عناوين الصفوف والأعمدة أم لا.
- [**اسود و ابيض**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): خاصية منطقية تحدد ما إذا كنت تريد طباعة ورقة العمل في الوضع الأسود والأبيض أم لا.
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): يحدد ما إذا كان سيتم عرض تعليقات الطباعة على ورقة العمل أو في نهاية ورقة العمل.
- [**برينتدرافت**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): خاصية منطقية تحدد ما إذا كنت تريد طباعة الورقة بدون رسومات ..
- [**أخطاء الطباعة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): يحدد ما إذا كان سيتم طباعة أخطاء الخلية كما هي معروضة أو فارغة أو شرطة أو غير متوفرة.

 لتعيين[**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) و[**أخطاء الطباعة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)الخصائص ، يوفر Aspose.Cells أيضًا عددين ،[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) ، و[**نوع الطباعة**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) التي تحتوي على قيم محددة مسبقًا ليتم تعيينها إلى[**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) و[**أخطاء الطباعة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)خصائص على التوالي.

 القيم المحددة مسبقًا في ملف[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)التعداد مذكور أدناه مع أوصافها.

|**طباعة أنواع التعليقات**|**وصف**|
| :- | :- |
|PrintInPlace|يُحدد لطباعة التعليقات كما هو معروض في ورقة العمل.|
|طباعة لا تعليقات|يحدد عدم طباعة التعليقات.|
|PrintSheetEnd|يُحدد لطباعة التعليقات في نهاية ورقة العمل.|

 القيم المحددة مسبقًا لـ[**نوع الطباعة**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)التعداد مذكور أدناه مع أوصافها.



|**أنواع أخطاء الطباعة**|**وصف**|
| :- | :- |
|أخطاء الطباعة|يحدد عدم طباعة الأخطاء.|
|PrintErrorsDash (شرطة)|يُحدد طباعة الأخطاء كـ "-".|
|تم عرض أخطاء الطباعة|يحدد لطباعة الأخطاء كما هو معروض.|
|PrintErrorsNA|يُحدد طباعة الأخطاء كـ "# N / A".|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

###  **تعيين ترتيب الصفحة**

 ال[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) فئة توفر[**طلب**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)الخاصية المستخدمة لطلب طباعة صفحات متعددة من ورقة العمل الخاصة بك. هناك احتمالان لترتيب الصفحات على النحو التالي.

- **لأسفل ثم فوق:** يطبع كل الصفحات لأسفل قبل طباعة أي صفحات على اليمين.
- **فوق ثم لأسفل:** يطبع الصفحات من اليسار إلى اليمين قبل طباعة الصفحات أدناه.

 يوفر Aspose.Cells تعداد ،[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)يحتوي على جميع أنواع الطلبات المحددة مسبقًا.

 القيم المحددة مسبقًا لـ[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)التعداد مذكورة أدناه.

|**أنواع أوامر الطباعة**|**وصف**|
| :- | :- |
|أسفل بعد ذلك|يمثل أمر الطباعة على أنه لأسفل ثم فوق.|
|زيادة في الأسفل|يمثل أمر الطباعة على أنه فوق ثم لأسفل.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
