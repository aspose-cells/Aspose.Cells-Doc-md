---
title: الحصول على الإشعارات أثناء دمج البيانات مع العلامات الذكية
type: docs
weight: 20
url: /ar/net/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

توفر واجهات برمجة التطبيقات Aspose.Cells [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)  للعمل مع العلامات الذكية حيث يتم وضع التنسيقات والصيغ في [أوراق التصميم](/cells/ar/net/what-is-a-designer-spreadsheet/) ومن ثم معالجتها باستخدام فئة [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) لملء البيانات وفقًا للعلامات الذكية المحددة. في بعض الأحيان، قد تكون هناك حاجة للحصول على الإشعارات حول الإشارة إلى الخلية أو العلامة الذكية المعينة. يمكن تحقيق ذلك باستخدام خاصية [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) و[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) الواجهة المكشوفة مع إصدار Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

توضح الجزء التالي من الكود استخدام [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) لتعريف فئة جديدة تتعامل مع استدعاء [WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



يتضمن باقي العملية تحميل ورقة العمل القالبية التي تحتوي العلامات الذكية باستخدام [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) ومعالجتها عن طريق تعيين مصدر البيانات. من أجل إبقاء المثال بسيطًا، لقد استخدمنا ورقة عمل قالبية محددة مسبقًا تحتوي فقط على علامتين ذكيتين كما هو موضح في اللقطة أدناه حيث يتم إنشاء مصدر البيانات بشكل ديناميكي لدمج البيانات وفقًا للعلامات الذكية المحددة.

|![todo:image_alt_text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
| :- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
