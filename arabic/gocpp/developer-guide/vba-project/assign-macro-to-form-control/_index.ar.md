---
title: تعيين الماكرو إلى عنصر تحكم النموذج باستخدام Golang عبر C++
linktitle: تعيين ماكرو إلى عنصر تحكم النموذج
type: docs
weight: 60
url: /ar/go-cpp/assign-macro-to-form-control/
description: تعلم كيفية تعيين رمز الماكرو إلى تحكم النموذج مثل زر باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

تسمح Aspose.Cells لك بتعيين شيفر آلي إلى عنصر تحكم النموذج مثل زر. يرجى استخدام الخاصية [**Shape.GetMacroName()**](https://reference.aspose.com/cells/go-cpp/shape/getmacroname/) لتعيين شيفر آلي جديد إلى عنصر تحكم النموذج داخل سجل العمل.

{{% /alert %}}

الكود النموذجي التالي ينشئ دفتر عمل جديد، يعين رمز الماكرو لزر النموذج، ويحفظ الناتج بتنسيق XLSM. عند فتح ملف XLSM الناتج في Microsoft Excel، ستشاهد رمز الماكرو التالي.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **تعيين ماكرو إلى تحكم النموذج في C++**

إليك الشيفرة الزمنية العينية لإنشاء ملف XLSM الناتج مع شيفر آلي.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AssignMacroToFormControl.go" >}}
