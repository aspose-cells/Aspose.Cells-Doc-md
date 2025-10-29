---
title: تعيين ماكرو إلى عنصر تحكم النموذج
type: docs
weight: 60
url: /ar/python-net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

يسمح Aspose.Cells لبايثون via .NET بتعيين كود الماكرو إلى عنصر تحكم نموذج مثل زر. يُرجى استخدام الخاصية [**Shape.macro_name**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/macro_name) لتعيين كود ماكرو جديد لعنصر تحكم النموذج داخل المصنف.

{{% /alert %}}

الشيفرة الزمنية العينية التالية تقوم بإنشاء سجل عمل جديد ، تعيين شيفر آلي إلى زر النموذج وحفظ الناتج بتنسيق XLSM. بمجرد فتحك لملف XLSM الناتج في Microsoft Excel سترى الشيفرة الزمنية التالية.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **تعيين ماكرو لعنصر تحكم النموذج في بايثون**

إليك الشيفرة الزمنية العينية لإنشاء ملف XLSM الناتج مع شيفر آلي.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AssignMacroToFormControl-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
