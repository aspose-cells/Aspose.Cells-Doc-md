---
title: الحصول على عرض وارتفاع الورق لإعداد الصفحة لورقة العمل
type: docs
weight: 50
url: /ar/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: ستكتشف في هذا المقال كيفية الحصول على عرض الورق وارتفاع الورق بإعداد الصفحة لورقة عمل إكسل باستخدام كود بايثون برمجياً مع Aspose.Cells لـ Python via .NET API أو مكتبة.
keywords: مكتبة إكسل بايثون، بايثون إعداد صفحة إكسل، عرض الورق في إكسل ببايثون، ارتفاع الورق في إكسل ببايثون.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، تحتاج إلى معرفة عرض وارتفاع حجم الورق حسبما تم تعيينه في إعداد الصفحة لورقة العمل. يرجى استخدام الخصائص [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) و [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) لهذا الغرض.

## **الحصول على عرض وارتفاع الورق لإعداد الصفحة لورقة العمل**

يفسر رمز العينة التالي استخدام خصائص [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) و [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height). يقوم أولاً بتغيير حجم الورق إلى *A2* ثم يجد عرض وارتفاع الورق، ثم يغيره إلى *A3*، *A4*، *Letter* ويجد عرض وارتفاع الورق على التوالي.

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
