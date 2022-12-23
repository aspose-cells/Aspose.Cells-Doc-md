---
title: تعيين ماكرو للتحكم في النموذج
type: docs
weight: 60
url: /ar/net/assign-macro-to-form-control/
---
{{% alert color="primary" %}}

 Aspose.Cells يسمح لك بتخصيص كود ماكرو لعنصر تحكم نموذج مثل الزر. الرجاء استخدام[**الشكل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) لتعيين رمز ماكرو جديد لعنصر تحكم النموذج داخل المصنف.

{{% /alert %}}

يقوم نموذج التعليمات البرمجية التالي بإنشاء مصنف جديد وتعيين رمز ماكرو إلى "زر النموذج" وحفظ الإخراج بتنسيق XLSM. بمجرد فتح ملف الإخراج XLSM في Microsoft Excel ، سترى رمز الماكرو التالي.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **قم بتعيين ماكرو للتحكم في النموذج في C#**

فيما يلي نموذج التعليمات البرمجية لإنشاء ملف الإخراج XLSM برمز الماكرو.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
