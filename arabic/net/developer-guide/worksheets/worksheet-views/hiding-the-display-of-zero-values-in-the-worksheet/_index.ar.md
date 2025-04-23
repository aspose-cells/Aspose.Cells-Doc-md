---
title: إخفاء عرض القيم الصفرية في ورقة العمل
type: docs
weight: 50
url: /ar/net/hiding-the-display-of-zero-values-in-the-worksheet/
description: سوف يوضح هذا المقال لك رمزًا عينيًا يشرح كيفية إخفاء القيم الصفرية برمجيًا في جدول بيانات Excel باستخدام مكتبة C# أو واجهة برمجة التطبيقات .NET.
keywords: إخفاء القيم الصفرية لورقة العمل في c#
---

{{% alert color="primary" %}} 

في بعض الأحيان، تحتاج إلى إخفاء القيم الصفرية في جدول بيانات. قد يكون اختيار شخصي أو معيار تنسيق.

{{% /alert %}} 

لإخفاء القيم الصفرية في ورقة العمل في Microsoft Excel (على سبيل المثال Microsoft Excel 2003):

1. من قائمة **الأدوات**، حدد **الخيارات**، ثم حدد علامة تبويب **العرض**.
1. ألغِ تحديد خيار **قيم الصفر**.
1. انقر على **موافق**.

الرجاء رؤية الشيفرة المثالية التالية التي تظهر إخفاء الأصفار باستخدام Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HidingDisplayOfZeroValues-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
