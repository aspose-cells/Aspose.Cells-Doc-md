---
title: التحقق من تنسيق الرقم المخصص عند تعيين خاصية Style.Custom مع Golang عبر C++
description: مكتبة Aspose.Cells هي مكتبة C++ للعمل مع ملفات جداول البيانات، وتدعم فحص تنسيقات الأرقام المخصصة عند التنسق. ستوضح لك هذه المقالة كيفية استخدام مكتبة Aspose.Cells للتحقق من تنسيقات الأرقام المخصصة لضمان صحة التنسق.
keywords: مكتبة Aspose.Cells، مكتبات C++، جداول البيانات، التنسق، تنسيق الأرقام المخصصة، التحقق، التحقق من الصحة
type: docs
weight: 170
url: /ar/go-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **سيناريوهات الاستخدام المحتملة**

إذا قمت بتعيين تنسيق رقم مخصص غير صالح لخاصية [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/)، فلن ترمي مكتبة Aspose.Cells استثناءً. ولكن إذا كنت تريد أن تتحقق Aspose.Cells مما إذا كان التنسيق المخصص المعين صالحًا أم لا، يرجى ضبط الخاصية [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) على **true**.

## **فحص تنسيق الرقم المخصص عند ضبط خاصية Style.Custom**

يُظهر نموذج الشفرة التالي تعيين تنسيق رقم مخصص غير صالح لخاصية [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/). بما أننا قمنا بالفعل بضبط الخاصية [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) على **true**، فإنه يرمي استثناءً، مثلاً، صيغة رقم غير صالحة. اقرأ التعليقات داخل الشفرة للمساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckCustomNumberFormatWhenSettingStyleCustomProperty.go" >}}
