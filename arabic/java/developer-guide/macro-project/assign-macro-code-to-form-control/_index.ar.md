---
title: تعيين رمز الماكرو لعنصر تحكم النموذج
type: docs
weight: 400
url: /ar/java/assign-macro-code-to-form-control/
---

{{% alert color="primary" %}} 

تسمح لك Aspose.Cells بتعيين كود ماكرو إلى عنصر تحكم نموذج مثل زر. يرجى استخدام طريقة [ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-) لتعيين كود ماكرو جديد إلى عنصر تحكم داخل المصنف.

{{% /alert %}} 
## **تعيين رمز ماكرو لعنصر تحكم باستخدام Aspose.Cells**
يلخي الكود العيني التالي دفتر عمل جديد، يعين رمز ماكرو لعنصر تحكم النموذج ويحفظ الناتج في تنسيق XLSM. بمجرد فتح ملف XLSM الناتج في Microsoft Excel سترى رمز الماكرو التالي.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

إليك كود عينة لإنشاء ملف XLSM الناتج مع رمز ماكرو.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
{{< app/cells/assistant language="java" >}}
