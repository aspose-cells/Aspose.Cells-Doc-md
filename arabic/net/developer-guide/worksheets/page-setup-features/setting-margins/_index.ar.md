---
title: ضبط الهوامش
type: docs
weight: 20
url: /ar/net/setting-margins/
description: في هذا المقال، ستتعلم كيفية تعيين الهوامش لورقة عمل Excel باستخدام الكود العيني. وستتعلم أيضا كيفية تعيين الهوامش برمجيا لوسط الصفحة، وهوامش الرأس والتذييل لـإعداد الصفحة باستخدام واجهة برمجة التطبيقات C# أو مكتبة .NET.
keywords: تعيين هوامش ورقة عمل Excel إلى الوسط C#، تعيين هوامش رأس وتذييل ورقة عمل C#
---

{{% alert color="primary" %}}

تدعم Aspose.Cells تماماً خيارات إعداد الصفحة في Microsoft Excel. قد يحتاج المطورون إلى تكوين إعدادات إعداد الصفحة للوظائف للتحكم في عملية الطباعة. يناقش هذا الموضوع كيفية استخدام Aspose.Cells لتكوين هوامش الصفحة.

{{% /alert %}}

## **ضبط الهوامش**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، التي تمثل ملف Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) الخاصية [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) المستخدمة لتعيين خيارات إعداد الصفحة لورقة عمل. السمة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) هي كائن من فئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) التي تمكّن المطورين من تعيين خيارات تخطيط الصفحة المختلفة لورقة العمل المطبوعة. الفئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) توفر خصائص وطرق مختلفة يمكن استخدامها لتعيين خيارات إعداد الصفحة.

### **هوامش الصفحة**

تعيين هوامش الصفحة (اليسار، اليمين، الأعلى، الأسفل) باستخدام أعضاء فئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup). ويُدرج بعض الطرق الواردة أدناه والتي تُستخدم لتحديد الهوامش الصفحية:

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**BottomMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **توسيط على الصفحة**

من الممكن توسيط شيء ما على الصفحة أفقيًا ورأسيًا. لهذا الغرض، هناك بعض الأعضاء المفيدة في الفئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) مثل [**CenterHorizontally**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) و [**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **هوامش الرأس والتذييل**

تعيين هوامش الرأس والتذييل باستخدام أعضاء فئة [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) مثل [**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) و [**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
