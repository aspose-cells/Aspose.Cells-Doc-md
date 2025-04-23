---
title: إزالة الأنماط الغير مستخدمة في دفتر العمل
type: docs
weight: 470
url: /ar/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

الأنماط غير المستخدمة في ملف إكسل لا تستهلك المساحة فحسب، بل تسبب أيضًا مشكلات في الأداء عند التحويل إلى صيغ مختلفة مثل PDF، HTML، وغيرها. يوفر Aspose.Cells وظيفة [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--) لإزالة جميع الأنماط غير المستخدمة داخل المصنف.

{{% /alert %}} 
## **إزالة الأنماط غير المستخدمة داخل جدول البيانات**
يشرح الكود التالي استخدام [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--). يحمي الكود ملف إكسل القالب [template excel file](5473451.xlsx) الذي يمكنك تنزيله من الرابط المقدم. يحتوي على نمط غير مستخدم باسم **AsposeStyle**، وسيتم حذف هذا النمط وجميع الأنماط غير المستخدمة الأخرى بعد تنفيذ الكود. يرجى الاطلاع على لقطة الشاشة التالية للمزيد من التوضيح.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
{{< app/cells/assistant language="java" >}}
