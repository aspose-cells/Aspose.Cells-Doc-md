---
title: تحقق من تنسيق الرقم المخصص عند ضبط خاصية Style.Custom
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جدول البيانات، تدعم فحص تنسيقات الأرقام المخصصة عند التنسيق. سيوضح هذا المقال كيفية استخدام مكتبة Aspose.Cells لفحص تنسيقات الأرقام المخصصة لضمان صحة التنسيق.
keywords: Aspose.Cells، مكتبات NET، جداول البيانات، تنسيق، تنسيق رقم مخصص، فحص، التحقق
type: docs
weight: 170
url: /ar/net/check-custom-number-format-when-setting-style-custom-property/
---

## **سيناريوهات الاستخدام المحتملة**

إذا قمت بتعيين تنسيق رقم مخصص غير صالح لخاصية [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)، فلن تقوم Aspose.Cells بإلقاء أي استثناء. ولكن إذا كنت ترغب في أن تقوم Aspose.Cells بالتحقق مما إذا كان التنسيق رقم مخصص المعين صالحًا أم لا، فيرجى ضبط الخاصية [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) إلى **صحيح**.

## **فحص تنسيق الرقم المخصص عند ضبط خاصية Style.Custom**

الكود العيني التالي يعين تنسيق رقم مخصص غير صالح لخاصية [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom). نظرًا لأننا قمنا بالفعل بضبط الخاصية [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) إلى **صحيح**، لذلك يلقي استثناء مثل تنسيق رقم غير صالح. يرجى قراءة التعليقات داخل الكود للمزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
