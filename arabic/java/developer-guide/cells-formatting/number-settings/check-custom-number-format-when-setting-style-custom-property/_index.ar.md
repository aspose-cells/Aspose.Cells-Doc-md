---
title: تحقق من تنسيق الأرقام المخصص عند ضبط Style.Custom الملكية
type: docs
weight: 160
url: /ar/java/check-custom-number-format-when-setting-style-custom-property/
---
## **سيناريوهات الاستخدام الممكنة**

 إذا قمت بتعيين تنسيق رقم مخصص غير صالح إلى[**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)الخاصية ثم Aspose.Cells لن يطرح أي استثناء. ولكن إذا كنت تريد أن يتحقق Aspose.Cells مما إذا كان تنسيق الرقم المخصص المعين صالحًا أم لا ، فالرجاء تعيين[**المصنف.الإعدادات**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) الملكية ل**حقيقي**.

## **تحقق من تنسيق الأرقام المخصص عند تعيين خاصية Style.Custom**

 يعيّن نموذج التعليمات البرمجية التالي تنسيق رقم مخصص غير صالح لـ[**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) منشأه. منذ أن وضعنا بالفعل[**المصنف.الإعدادات**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) الملكية ل**حقيقي** ، لذلك فإن API سيرمي CellsException على سبيل المثال*تنسيق الرقم غير صالح*.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
