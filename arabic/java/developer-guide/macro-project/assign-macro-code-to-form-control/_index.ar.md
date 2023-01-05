---
title: تعيين رمز ماكرو للتحكم في النموذج
type: docs
weight: 400
url: /ar/java/assign-macro-code-to-form-control/
---
{{% alert color="primary" %}} 

 Aspose.Cells يسمح لك بتخصيص كود ماكرو لعنصر تحكم نموذج مثل الزر. الرجاء استخدام[ShapeCollection.addShape ()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) طريقة لتعيين رمز ماكرو جديد لعنصر تحكم النموذج داخل المصنف.

{{% /alert %}} 
## **تعيين رمز ماكرو للتحكم في النموذج باستخدام Aspose.Cells**
يقوم نموذج التعليمات البرمجية التالي بإنشاء مصنف جديد ، وتعيين "رمز ماكرو" إلى "نموذج زر" وحفظ الإخراج بتنسيق XLSM. بمجرد فتح ملف الإخراج XLSM في Microsoft Excel ، سترى رمز الماكرو التالي.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

فيما يلي نموذج التعليمات البرمجية لإنشاء ملف الإخراج XLSM برمز الماكرو.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
