---
title: إضافة وحدة VBA وكود باستخدام Aspose.Cells
type: docs
weight: 20
url: /ar/java/adding-vba-module-and-code-using-aspose-cells/
---

{{% alert color="primary" %}}

تسمح لك Aspose.Cells بإضافة وحدة مايكرو VBA جديدة باستخدام Aspose.Cells. يرجى استخدام [**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add-com.aspose.cells.Worksheet-) لإضافة الوحدة الماكرو داخل المصنف.

{{% /alert %}}

## **إضافة وحدة VBA وكود باستخدام Aspose.Cells**

يُنشئ رمز العينة التالي مصنف عمل جديد ويضيف وحدة VBA جديدة وكود الماكرو الجديد ويحفظ الإخراج بتنسيق XLSM. بمجرد فتحك لملف الإكسيل الناتج XLSM والنقر على أوامر **تطوير > الأساسيات المرئية**، سترى وحدة تسمى "الوحدة الاختبارية" وبداخلها سترى كود الماكرو التالي.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## كود عينة

إليك كود عينة لإنشاء ملف XLSM الناتج بوحدة VBA ورمز ماكرو.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
{{< app/cells/assistant language="java" >}}
