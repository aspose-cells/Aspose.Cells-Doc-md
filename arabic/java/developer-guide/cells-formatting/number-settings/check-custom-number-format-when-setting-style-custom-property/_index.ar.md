---
title: تحقق من تنسيق الرقم المخصص عند ضبط خاصية Style.Custom
type: docs
weight: 160
url: /ar/java/check-custom-number-format-when-setting-style-custom-property/
---

## **سيناريوهات الاستخدام المحتملة**

إذا قمت بتعيين تنسيق رقم مخصص غير صالح لخاصية [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) ، فلن يقوم Aspose.Cells بإطلاق أي استثناء. ولكن إذا كنت ترغب في أن تقوم Aspose.Cells بالتحقق مما إذا كان التنسيق المخصص للرقم المعين صالحًا أم لا ، فيرجى ضبط الخاصية [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) إلى **true**.

## **تحقق من تنسيق الرقم المخصص عند ضبط خاصية Style.Custom**

الكود النموذجي التالي يعين تنسيق رقم مخصص غير صالح لخاصية [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). نظرًا لأننا قمنا بالفعل بتعيين الخاصية [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) إلى **true** ، فإن الواجهة البرمجية ستطلق استثناء CellsException على سبيل المثال *تنسيق رقم غير صالح*.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
