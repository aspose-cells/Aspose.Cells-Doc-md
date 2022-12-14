---
title: تحديد الهوامش
type: docs
weight: 20
url: /ar/net/setting-margins/
---
{{% alert color="primary" %}}

Aspose.Cells يدعم Microsoft خيارات إعداد صفحة Excel بشكل كامل. قد يحتاج المطورون إلى تكوين إعدادات إعداد الصفحة لأوراق العمل للتحكم في عملية الطباعة. يناقش هذا الموضوع كيفية استخدام Aspose.Cells لتكوين هوامش الصفحة.

{{% /alert %}}

## **تحديد الهوامش**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)صف دراسي.

 ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)فئة توفر[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) الخاصية المستخدمة لتعيين خيارات إعداد الصفحة لورقة العمل. ال[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) السمة كائن من[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) فئة تمكن المطورين من تعيين خيارات مختلفة لتخطيط الصفحة لورقة عمل مطبوعة. ال[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)توفر فئة الخصائص والأساليب المختلفة المستخدمة لتعيين خيارات إعداد الصفحة.

### **هوامش الصفحة**

 قم بتعيين هوامش الصفحة (يسار ، يمين ، أعلى ، أسفل) باستخدام[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)أعضاء الفصل. يتم سرد بعض الطرق أدناه والتي تُستخدم لتحديد هوامش الصفحة:

- [**الهامش الأيسر**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**الهامش الأيمن**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**الهامش العلوي**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**الهامش السفلي**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **توسيط في الصفحة**

من الممكن توسيط شيء ما على الصفحة أفقيًا ورأسيًا. لهذا ، هناك بعض الأعضاء المفيدين في[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) صف دراسي،[**توسيط أفقيًا**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) و[**مركز عموديا**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **هوامش الرأس والتذييل**

 قم بتعيين هوامش الرأس والتذييل باستخدام ملحق[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) أعضاء الفصل مثل[**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) و[**التذييل**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
