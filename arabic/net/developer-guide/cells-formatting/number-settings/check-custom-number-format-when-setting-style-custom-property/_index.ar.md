---
title: تحقق من تنسيق الأرقام المخصص عند ضبط Style.Custom الملكية
type: docs
weight: 170
url: /ar/net/check-custom-number-format-when-setting-style-custom-property/
---
## **سيناريوهات الاستخدام الممكنة**

 إذا قمت بتعيين تنسيق رقم مخصص غير صالح إلى[**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)الخاصية ، فلن يطرح Aspose.Cells أي استثناء. ولكن إذا كنت تريد أن يتحقق Aspose.Cells مما إذا كان تنسيق الرقم المخصص المعين صالحًا أم لا ، فالرجاء تعيين[**المصنف.الإعدادات**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) ملكية ل**حقيقي**.

## **تحقق من تنسيق الأرقام المخصص عند تعيين خاصية Style.Custom**

 يعيّن نموذج التعليمات البرمجية التالي تنسيق رقم مخصص غير صالح لـ[**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) خاصية. منذ ذلك الحين ، قمنا بالفعل بتعيين[**المصنف.الإعدادات**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) ملكية ل**حقيقي**، لذلك فإنه يطرح استثناء ، على سبيل المثال تنسيق رقم غير صالح. يرجى قراءة التعليقات داخل الكود لمزيد من المساعدة.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
