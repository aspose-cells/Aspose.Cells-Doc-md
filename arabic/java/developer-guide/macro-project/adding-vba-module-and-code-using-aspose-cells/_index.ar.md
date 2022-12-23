---
title: إضافة وحدة VBA والكود باستخدام Aspose.Cells
type: docs
weight: 20
url: /ar/java/adding-vba-module-and-code-using-aspose-cells/
---
{{% alert color="primary" %}}

 يسمح لك Aspose.Cells بإضافة وحدة جديدة لـ VBA وكود ماكرو باستخدام Aspose.Cells. الرجاء استخدام[**Workbook.getVbaProject (). getModules (). add (**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) لإضافة وحدة VBA النمطية الجديدة داخل المصنف

{{% /alert %}}

## **إضافة وحدة VBA والكود باستخدام Aspose.Cells**

ينشئ نموذج التعليمات البرمجية التالي مصنفًا جديدًا ويضيف وحدة VBA النمطية الجديدة ورمز الماكرو ويحفظ الإخراج بتنسيق XLSM. بمجرد فتح ملف الإخراج XLSM في Microsoft Excel والنقر فوق**المطور> Visual Basic** أوامر القائمة ، سترى وحدة تسمى "TestModule" وداخلها ، سترى رمز الماكرو التالي.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## عينة من الرموز

فيما يلي نموذج التعليمات البرمجية لإنشاء ملف الإخراج XLSM باستخدام وحدة VBA وكود الماكرو.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
