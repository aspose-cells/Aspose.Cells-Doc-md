---
title: تعديل VBA أو Macro Code باستخدام Aspose.Cells
type: docs
weight: 90
url: /ar/java/modifying-vba-or-macro-code-using-aspose-cells/
---
{{% alert color="primary" %}} 

يمكنك تعديل VBA أو Macro Code باستخدام Aspose.Cells. قام Aspose.Cells بإضافة الفئات التالية لقراءة وتعديل مشروع VBA في ملف Excel.

- VbaProject
- مجموعة VbaModuleCollection
- VbaModule

ستوضح لك هذه المقالة كيفية تغيير VBA أو Macro Code داخل ملف Excel المصدر باستخدام Aspose.Cells.

{{% /alert %}} 
## **مثال**
يقوم نموذج التعليمات البرمجية التالي بتحميل ملف Excel المصدر الذي يحتوي على رمز VBA أو Macro التالي بداخله

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

بعد تنفيذ رمز عينة Aspose.Cells ، سيتم تعديل رمز VBA أو ماكرو بهذا الشكل

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

 يمكنك تنزيل ملف[ملف Excel المصدر](5472596.xlsm) و ال[إخراج ملف Excel](5472597.xlsm) من الروابط المعطاة.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






