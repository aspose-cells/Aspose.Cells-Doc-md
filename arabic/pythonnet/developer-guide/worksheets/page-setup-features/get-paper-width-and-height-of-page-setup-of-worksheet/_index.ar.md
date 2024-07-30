---
title: الحصول على عرض وارتفاع الورق لإعداد الصفحة لورقة العمل
type: docs
weight: 50
url: /ar/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: ستكتشف في هذا المقال كيفية الحصول على عرض وارتفاع ورقة عمل Excel باستخدام كود Python برمجياً باستخدام API أو مكتبة Aspsoe.Cells لـ Python via .NET.
keywords: مكتبة Excel الخاصة ببيثون، بيثون تحديث عرض الورق لإعداد صفحة Excel، تحديث ارتفاع ورقة الإعداد في بيثون.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، تحتاج إلى معرفة عرض وارتفاع حجم الورق حسبما تم تعيينه في إعداد الصفحة لورقة العمل. يرجى استخدام الخصائص [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) و [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) لهذا الغرض.

## **الحصول على عرض وارتفاع الورق لإعداد الصفحة لورقة العمل**

يشرح رمز العينات التالي استخدام خاصية [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) و [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height). يقوم أولاً بتغيير حجم الورق إلى *A2* ثم يجد عرض وارتفاع الورق، ثم يقوم بتغييره إلى *A3*، *A4*، *Letter* ويجد عرض وارتفاع الورق على التوالي.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-GetPageDimensions.py" >}}

### **مخرجات الوحدة**

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
