---
title: احصل على عرض الورق وارتفاعه في إعداد الصفحة لورقة العمل
type: docs
weight: 50
url: /ar/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: سوف تكتشف في هذه المقالة كيفية الحصول على عرض ورقة ورقة عمل Excel وارتفاع الورق باستخدام كود C# برمجيًا مع .NET API أو المكتبة.
keywords: excel page setup paper width c#, excel page setup paper height c#
---
##  **سيناريوهات الاستخدام الممكنة**

في بعض الأحيان ، تحتاج إلى معرفة عرض وارتفاع حجم الورق حيث تم تعيينه في إعداد الصفحة لورقة العمل. الرجاء استخدام[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)و[**PageSetup.PaperHeight. إعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)خصائص لهذا الغرض.

##  **احصل على عرض الورق وارتفاعه في إعداد الصفحة لورقة العمل**

 يشرح نموذج التعليمات البرمجية التالي استخدام[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) و[**PageSetup.PaperHeight. إعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) ملكيات. يقوم أولاً بتغيير حجم الورق إلى*A2*ثم يبحث عن عرض الورق وارتفاعه ، ثم يقوم بتغييره إلى*A3 * ، * A4 * ، * خطاب*ويجد عرض الورق وارتفاعه على التوالي.

###  **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

###  **إخراج وحدة التحكم**

هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
