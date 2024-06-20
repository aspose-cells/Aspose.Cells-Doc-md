---
title: الحصول على عرض وارتفاع الورق لإعداد الصفحة لورقة العمل
type: docs
weight: 50
url: /ar/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: ستكتشف في هذا المقال كيفية الحصول على عرض وارتفاع ورقة إعداد الصفحة في إكسل باستخدام كود C# بشكل برمجي باستخدام واجهة برمجة التطبيقات .NET أو المكتبة.
keywords: عرض الورق لإعداد الصفحة في إكسيل باستخدام C#، ارتفاع الورق لإعداد الصفحة في إكسيل باستخدام C#
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، تحتاج إلى معرفة عرض وارتفاع حجم الورق حسبما تم تعيينه في إعداد الصفحة لورقة العمل. يرجى استخدام الخصائص [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) و [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) لهذا الغرض.

## **الحصول على عرض وارتفاع الورق لإعداد الصفحة لورقة العمل**

الشيفرة المثالية التالية تشرح كيفية استخدام الخصائص [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) و [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight). فإنها أولاً تغير حجم الورق إلى *A2* ثم تجد عرض وارتفاع الورق، ثم تغييره إلى *A3*، *A4*، *Letter* وتجد عرض وارتفاع الورق على التوالي.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

### **مخرجات الوحدة**

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
