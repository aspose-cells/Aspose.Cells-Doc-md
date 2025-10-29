---
title: تحقق من تنسيق الرقم المخصص عند ضبط خاصية Style.Custom
linktitle: تحقق من تنسيق الرقم المخصص عند ضبط خاصية Style.Custom
description: Aspose.Cells مكتبة Node.js للعمل مع ملفات جداول البيانات، وتدعم التحقق من تنسيقات الأرقام المخصصة عند التصفيف. ستوضح لك هذه المقالة كيفية استخدام مكتبة Aspose.Cells للتحقق من تنسيقات الأرقام المخصصة لضمان صحة التصفيف.
keywords: Aspose.Cells، مكتبات Node.js، جداول البيانات، التصفيف، تنسيق الأرقام المخصصة، التحقق، التصديق
type: docs
weight: 170
url: /ar/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **سيناريوهات الاستخدام المحتملة**

إذا قمت بتعيين تنسيق رقم مخصص غير صالح لـ [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) طريقة، فلن ترمي Aspose.Cells for Node.js via C++ أي استثناء. ولكن إذا أردت أن تتحقق Aspose.Cells مما إذا كان تنسيق الرقم المخصص المعين صحيحًا أم لا، يرجى تعيين طريقة [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) إلى **true**.

## **التحقق من تنسيق الرقم المخصص عند تعيين طريقة Style.setCustom(string)**

يعين رمز النموذج التالي تنسيق رقم مخصص غير صالح إلى [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-). بما أننا قمنا بالفعل بتعيين [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) إلى **true**، يطلق ذلك استثناء، مثل رقم غير صالح. يرجى قراءة التعليقات داخل الكود لمزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-CheckCustomNumberFormat.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
