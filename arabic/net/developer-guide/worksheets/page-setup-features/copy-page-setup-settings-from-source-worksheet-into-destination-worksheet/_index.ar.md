---
title: نسخ إعدادات إعداد الصفحة من ورقة العمل المصدر إلى ورقة العمل الهدف
type: docs
weight: 80
url: /ar/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: تشرح هذه المقالة كيفية استخدام رمز عيني C# API أو مكتبة .NET لنسخ إعدادات إعداد الصفحة من ورقة العمل المصدر إلى ورقة العمل الهدف برمجياً.
keywords: نسخ إعدادات إعداد الصفحة c#، نسخ إعدادات إعداد الصفحة إلى ورقة العمل المستهدفة c#
---

## **سيناريوهات الاستخدام المحتملة**

عند إضافة ورقة جديدة إلى كتيب العمل، تحتوي على إعدادات إعداد الصفحة الافتراضية. قد تحتاج في بعض الأحيان إلى نقل الإعدادات ([**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) من ورقة عمل واحدة إلى أخرى. توضح هذه الوثيقة كيفية نسخ إعدادات إعداد الصفحة من ورقة عمل واحدة إلى أخرى باستخدام واجهات برمجة التطبيقات Aspose.Cells.

## **نسخ إعدادات إعداد الصفحة من ورقة العمل المصدر إلى ورقة العمل الوجهة**

الشيفرة النموذجية التالية توضح كيفية نسخ إعدادات إعداد الصفحة من ورقة عمل واحدة إلى أخرى باستخدام طريقة [**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy). يُرجى الاطلاع على الشيفرة النموذجية التالية وإخراجها إلى وحدة التحكم كمرجع.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
