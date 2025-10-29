---
title: ضبط خيارات الطباعة
type: docs
weight: 40
url: /ar/python-net/setting-print-options/
description: توضح هذه المقالة كيفية تعيين إعدادات الطباعة بشكل برمجي باستخدام ميزة إعداد صفحة ورقة العمل في Excel باستخدام واجهة برمجة تطبيقات Aspose.Cells لـ Python via .NET. يمكنك تعيين منطقة الطباعة، عناوين الطباعة وترتيب الصفحة.
keywords: مكتبة بايثون Excel، إعداد منطقة الطباعة في Excel باستخدام بايثون، تعيين عناوين الطباعة في Excel بواسطة بايثون، كيفية تعيين ترتيب الصفحة في Excel بواسطة بايثون، كيفية تعيين خيارات الطباعة في بايثون، كيفية تعيين منطقة الطباعة في بايثون، كيفية تعيين عناوين الطباعة في بايثون. 
---

{{% alert color="primary" %}}

توفر إعدادات تهيئة الصفحة في ميكروسوفت إكسيل العديد من خيارات الطباعة التي تسمح للمستخدمين بالتحكم في كيفية طباعة صفحات ورق العمل.

{{% /alert %}}

## **كيفية تعيين خيارات الطباعة**

تسمح هذه الخيارات بالطباعة:

- تحديد منطقة طباعة معينة على ورقة عمل.
- طباعة العناوين.
- طباعة خطوط الشبكة.
- طباعة عناوين الصفوف/الأعمدة.
- تحقيق جودة مسودة.
- طباعة التعليقات.
- طباعة أخطاء الخلية.
- تعريف ترتيب الصفحات.

يدعم Aspose.Cells لـ Python via .NET جميع خيارات الطباعة التي تقدمها Microsoft Excel ويستطيع المطورون تكوين هذه الخيارات بسهولة لورقات العمل باستخدام الخصائص التي تقدمها فئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). يتم مناقشة كيفية استخدام هذه الخصائص بشكل أكثر تفصيلًا أدناه.

## **كيفية تعيين منطقة الطباعة**

اف فعل، منطقة الطباعة تشمل جميع مناطق ورقة العمل التي تحتوي على بيانات. يمكن للمطورين تحديد منطقة الطباعة المحددة لورقة العمل.

لتحديد منطقة الطباعة المحددة، استخدم خاصية [**print_area**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_area/) لفئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). قم بتعيين نطاق الخلايا الذي يعرف منطقة الطباعة لهذه الخاصية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintArea-1.py" >}}

## **كيفية تعيين عناوين الطباعة**

يسمح Aspose.Cells لـ Python via .NET بتحديد رؤوس الصفوف والأعمدة لتكرارها في جميع صفحات ورقة العمل المطبوعة. للقيام بذلك، استخدم خصائص فئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) [**print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) و [**print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows).

يتم تعريف الصفوف أو الأعمدة التي ستتكرر عن طريق تمرير أرقامها. على سبيل المثال، يتم تعريف الصفوف كـ $1:$2 والأعمدة كـ $A:$B.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintTitle-1.py" >}}

## **كيفية تعيين خيارات طباعة أخرى**

فئة [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) توفر أيضا عدة خصائص أخرى لتعيين خيارات الطباعة العامة على النحو التالي:

- [**print_grid_lines**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_gridlines/): خاصية بوليانية تعرف ما إذا كان سيتم طباعة خطوط الشبكة أم لا.
- [**print_headings**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_headings/): خاصية بوليانية تعرف ما إذا كان سيتم طباعة عناوين الصف والعمود أم لا.
- [**black_and_white**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/black_and_white/): خاصية بوليانية تعرف ما إذا كان سيتم طباعة ورقة العمل في وضع أسود وأبيض أم لا.
- [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/): يحدد ما إذا كان سيتم عرض التعليقات المطبوعة على ورقة العمل أم في نهايتها.
- [**print_draft**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_draft/): خاصية بوليانية تعرف ما إذا كان سيتم طباعة الورقة بدون الرسومات.
- [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors): يحدد ما إذا كان سيتم طباعة أخطاء الخلية كما هو معروض، فارغ، شرطة أو غير متوفر.

لتعيين الخصائص [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) و [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors)، توفر Aspose.Cells أيضا اثنين من التعدادات، [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) و [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) التي تحتوي على قيم محددة مسبقًا لتعيين الخصائص [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) و [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) على التوالي.

تتم إدراج القيم المحددة مسبقًا في تعداد [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) أدناه مع وصفها.

|**أنواع التعليقات المطبوعة**|**الوصف**|
| :- | :- |
|PRINT_IN_PLACE|تحديد طباعة التعليقات كما هو معروض على ورقة العمل.|
|PRINT_NO_COMMENTS|تحديد عدم طباعة التعليقات.|
|PRINT_SHEET_END|تحديد طباعة التعليقات في نهاية ورقة العمل.|

تم إدراج القيم المحددة مسبقًا لتعداد [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) أدناه مع وصفها.



| **أنواع أخطاء الطباعة** | **الوصف** |
| :- | :- |
|PRINT_ERRORS_BLANK|تحديد عدم طباعة الأخطاء.|
|PRINT_ERRORS_DASH|تحديد طباعة الأخطاء على شكل "--".|
|PRINT_ERRORS_DISPLAYED|تحديد طباعة الأخطاء كما تظهر.|
|PRINT_ERRORS_NA|تحديد طباعة الأخطاء كـ "#N/A".|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-OtherPrintOptions-1.py" >}}

## **كيفية تعيين ترتيب الصفحة**

توفر صفيف [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) خاصية [**Order**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/order) التي تستخدم لترتيب صفحات ورق العمل المتعددة المطبوعة. هناك احتمالان لترتيب الصفحات على النحو التالي.

- **اسفل ثم يمين:** يطبع جميع الصفحات أسفل الصفحة قبل طباعة أي صفحات على اليمين.
- **يمين ثم أسفل:** يطبع الصفحات من اليسار إلى اليمين قبل طباعة الصفحات أسفلها.

يوفّر Aspose.Cells تعدادًا، [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype)، يحتوي على جميع أنواع ترتيب محدد مسبقًا.

يتم سرد القيم المحددة مسبقًا لتعداد [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) أدناه.

| **أنواع ترتيب الطباعة** | **الوصف** |
| :- | :- |
|DOWN_THEN_OVER|يمثل ترتيب الطباعة على شكل نزول ثم انتقال أفقيًا.|
|OVER_THEN_DOWN|يمثل ترتيب الطباعة كفوق ثم أسفل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPageOrder-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
