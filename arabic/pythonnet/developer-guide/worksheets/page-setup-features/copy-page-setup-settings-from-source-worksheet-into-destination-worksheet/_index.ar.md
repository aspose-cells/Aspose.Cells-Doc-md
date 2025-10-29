---
title: نسخ إعدادات إعداد الصفحة من ورقة العمل المصدر إلى ورقة العمل الهدف
type: docs
weight: 80
url: /ar/python-net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: يشرح هذا المقال كيفية استخدام رمز النموذج Aspose.Cells لـ Python via .NET لنسخ إعدادات إعداد الصفحة من ورقة العمل المصدر إلى ورقة العمل الوجهة برمجياً.
keywords: مكتبة إكسل بايثون، بايثون نسخ إعدادات إعداد الصفحة، نسخ إعدادات إعداد الصفحة إلى ورقة العمل الهدف في بايثون.
---

## **سيناريوهات الاستخدام المحتملة**

عند إضافة ورقة جديدة إلى مصنف، فهي تحتوي على إعدادات إعداد الصفحة الافتراضية*. قد يكون هناك أوقات تحتاج فيها إلى نقل الإعدادات ([**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)) من ورقة عمل إلى أخرى. يوضح هذا المستند كيفية نسخ إعدادات إعداد الصفحة من ورقة عمل إلى أخرى باستخدام Aspose.Cells لـ Python via .NET APIs.

## **نسخ إعدادات إعداد الصفحة من ورقة العمل المصدر إلى ورقة العمل الوجهة**

الشيفرة النموذجية التالية توضح كيفية نسخ إعدادات إعداد الصفحة من ورقة عمل واحدة إلى أخرى باستخدام طريقة [**PageSetup.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/copy/#aspose.cells.PageSetup-aspose.cells.CopyOptions). يُرجى الاطلاع على الشيفرة النموذجية التالية وإخراجها إلى وحدة التحكم كمرجع.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.py" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
