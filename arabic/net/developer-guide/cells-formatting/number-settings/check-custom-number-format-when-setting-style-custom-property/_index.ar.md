---
title: تحقق من تنسيق الأرقام المخصص عند تعيين خاصية Style.Custom
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات، والتي تدعم التحقق من تنسيقات الأرقام المخصصة عند التصميم. ستوضح لك هذه المقالة كيفية استخدام مكتبة Aspose.Cells للتحقق من تنسيقات الأرقام المخصصة للتأكد من صحة التصميم.
keywords: Aspose.Cells, NET libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /ar/net/check-custom-number-format-when-setting-style-custom-property/
---
##  **سيناريوهات الاستخدام المحتملة**

 إذا قمت بتعيين تنسيق رقم مخصص غير صالح لـ[**مخصص**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) الملكية، فإن Aspose.Cells لن يرمي أي استثناء. ولكن إذا كنت تريد أن يتحقق Aspose.Cells مما إذا كان تنسيق الرقم المخصص صالحًا أم لا، فيرجى تعيين[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) الخاصية إلى *صحيح**.

##  **تحقق من تنسيق الأرقام المخصص عند تعيين خاصية Style.Custom**

 يقوم نموذج التعليمات البرمجية التالي بتعيين تنسيق أرقام مخصص غير صالح إلى[**مخصص**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) ملكية. منذ ذلك الحين، قمنا بتعيين بالفعل[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) الخاصية إلى *صحيح**، وبالتالي فإنها تطرح استثناءً، على سبيل المثال، تنسيق أرقام غير صالح. يرجى قراءة التعليقات داخل الكود لمزيد من المساعدة.

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
