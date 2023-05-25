---
title: إخفاء عرض القيم الصفرية في ورقة العمل
type: docs
weight: 50
url: /ar/net/hiding-the-display-of-zero-values-in-the-worksheet/
description: ستعرض لك هذه المقالة نموذجًا لرمز يشرح كيفية إخفاء القيم الصفرية برمجيًا في جدول بيانات Excel باستخدام مكتبة C# أو .NET API.
keywords: hide zero values of excel worksheet in c#
---
{{% alert color="primary" %}} 

في بعض الأحيان ، تحتاج إلى إخفاء القيم الصفرية في جدول بيانات. قد يكون تفضيلًا شخصيًا أو معيار تنسيق.

{{% /alert %}} 

لإخفاء القيم الصفرية في ورقة عمل في Microsoft Excel (على سبيل المثال Microsoft Excel 2003):

1.  من**أدوات** القائمة ، حدد**خيارات ** ، ثم حدد ** عرض** فاتورة غير مدفوعة.
1.  قم بإلغاء تحديد ملف**قيم صفرية** خيار.
1. انقر فوق موافق**.

يرجى الاطلاع على نموذج الكود التالي الذي يوضح إخفاء الأصفار باستخدام Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HidingDisplayOfZeroValues-1.cs" >}}
