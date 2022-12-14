---
title: الحصول على إخطارات أثناء دمج البيانات مع العلامات الذكية
type: docs
weight: 20
url: /ar/net/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 توفر واجهات برمجة التطبيقات Aspose.Cells امتداد[المصمم المصمم](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) الفئة الى[العمل مع العلامات الذكية](https://docs.aspose.com/cells/net/smart-markers/) حيث يتم وضع التنسيقات والصيغ في ملف[جداول بيانات المصمم](/cells/ar/net/what-is-a-designer-spreadsheet/) ثم يتم معالجتها باستخدام[المصمم المصمم](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) فئة لتعبئة البيانات وفقًا للعلامات الذكية المحددة. في بعض الأحيان ، قد يكون من الضروري الحصول على إعلامات حول مرجع الخلية أو العلامة الذكية المعينة التي تتم معالجتها. يمكن تحقيق ذلك باستخدام ملف[المصمم المصمم](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) الملكية و[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) الواجهة المكشوفة بإصدار Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

 يوضح الجزء التالي من التعليمات البرمجية استخدام[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) واجهة لتعريف فئة جديدة تتعامل مع معاودة الاتصال[المصنف المصمم. العملية](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)طريقة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



 تتضمن بقية العملية تحميل جدول بيانات المصمم الذي يحتوي على العلامات الذكية مع[المصمم المصمم](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)ومعالجتها عن طريق تحديد مصدر البيانات. من أجل الحفاظ على المثال بسيطًا ، استخدمنا جدول بيانات مصممًا محددًا مسبقًا يحتوي على اثنين فقط من العلامات الذكية كما هو موضح في اللقطة أدناه حيث يتم إنشاء مصدر البيانات ديناميكيًا لدمج البيانات وفقًا للعلامات الذكية المحددة.

|![ما يجب القيام به: image_بديل_نص](getting-notifications-while-merging-data-with-smart-markers_1.png)|
|:- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
