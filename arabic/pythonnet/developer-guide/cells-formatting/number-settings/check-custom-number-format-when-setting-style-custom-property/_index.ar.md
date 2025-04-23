---
title: تحقق من تنسيق الرقم المخصص عند ضبط خاصية Style.Custom
description: Aspose.Cells مكتبة بايثون للعمل مع ملفات جدول البيانات، والتي تدعم التحقق من تنسيقات الأرقام المخصصة عند تطبيق الأنماط. ستوضح هذه المقالة كيف تستخدم Aspose.Cells للتحقق من التنسيقات المخصصة للأرقام لضمان صحة التنسيق.
keywords: Aspose.Cells، مكتبات بايثون، جداول البيانات، التنسيق، تنسيق الأرقام المخصص، التحقق، التوثيق
type: docs
weight: 170
url: /ar/python-net/check-custom-number-format-when-setting-style-custom-property/
---

## **سيناريوهات الاستخدام المحتملة**

إذا قمت بتعيين تنسيق رقم مخصص غير صالح لخاصية [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom)، فلن تقوم Aspose.Cells بإلقاء أي استثناء. ولكن إذا كنت ترغب في أن تقوم Aspose.Cells بالتحقق مما إذا كان التنسيق رقم مخصص المعين صالحًا أم لا، فيرجى ضبط الخاصية [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) إلى **صحيح**.

## **فحص تنسيق الرقم المخصص عند ضبط خاصية Style.Custom**

الكود العيني التالي يعين تنسيق رقم مخصص غير صالح لخاصية [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom). نظرًا لأننا قمنا بالفعل بضبط الخاصية [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) إلى **صحيح**، لذلك يلقي استثناء مثل تنسيق رقم غير صالح. يرجى قراءة التعليقات داخل الكود للمزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CheckCustomFormatPattern.py" >}}

