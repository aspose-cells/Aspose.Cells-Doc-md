---
title: تعديل رمز VBA أو ماكرو باستخدام Aspose.Cells
type: docs
weight: 90
url: /ar/java/modifying-vba-or-macro-code-using-aspose-cells/
---

{{% alert color="primary" %}} 

يمكنك تعديل رمز VBA أو ماكرو باستخدام Aspose.Cells. أضافت Aspose.Cells الفئات التالية لقراءة وتعديل مشروع VBA في ملف Excel.

- VbaProject
- VbaModuleCollection
- VbaModule

سيعرض هذا المقال لك كيفية تغيير رمز VBA أو الماكرو داخل ملف Excel المصدر باستخدام Aspose.Cells.

{{% /alert %}} 
## **مثال**
يقوم الرمز الخاص المعروض أدناه بتحميل ملف Excel المصدر الذي يحتوي على رمز VBA أو ماكرو التالي داخله

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

بعد تنفيذ رمز عينات Aspose.Cells، سيتم تعديل رمز VBA أو الماكرو مثل هذا

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

يمكنك تنزيل [ملف Excel المصدر](5472596.xlsm) و [ملف Excel الناتج](5472597.xlsm) من الروابط المعطاة.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






{{< app/cells/assistant language="java" >}}
