---
title: إزالة الأنماط الغير مستخدمة في دفتر العمل
type: docs
weight: 470
url: /ar/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

الأنماط غير المستخدمة في ملف Excel لا تأخذ مساحة فقط ولكنها تسبب أيضًا مشاكل في الأداء عند تحويلها إلى تنسيقات مختلفة مثل PDF، HTML، إلخ. توفر Aspose.Cells الطريقة [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\)) لإزالة جميع الأنماط غير المستخدمة داخل جدول البيانات.

{{% /alert %}} 
## **إزالة الأنماط غير المستخدمة داخل جدول البيانات**
الكود التالي يشرح استخدام [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\)). يقوم الكود بتحميل [ملف Excel القالبي](5473451.xlsx) الذي يمكنك تنزيله من الرابط المُقدم. يحتوي الملف على نمط غير مستخدم يُسمى **AsposeStyle**، سيتم إزالة هذا النمط وجميع الأنماط الأخرى غير المستخدمة بعد تنفيذ الكود. يرجى الرجوع إلى لقطة الشاشة التالية لمزيد من التوضيح.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
