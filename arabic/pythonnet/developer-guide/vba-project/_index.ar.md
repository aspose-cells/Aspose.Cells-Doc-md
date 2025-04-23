---
title: إدارة رموز VBA لمصنف العمل ذو الماكرو الممكن تمكينه.
linktitle: مشروع الماكرو
type: docs
weight: 200
url: /ar/python-net/manage-vba-project/
description: إضافة وحدة VBA وتعديل VBA أو Macro باستخدام مكتبة Aspose.Cells لبايثون via .NET.
---

## **إضافة وحدة VBA في بايثون**
{{% alert color="primary" %}}

يسمح لك Aspose.Cells بإضافة وحدة VBA جديدة وكود Macro باستخدام Aspose.Cells لبايثون via .NET. يرجى استخدام الأسلوب [**Workbook.vba_project.modules.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add/) لإضافة الوحدة VBA الجديدة داخل دفتر العمل

{{% /alert %}}

يُنشئ رمز العينة التالي مصنف عمل جديد ويضيف وحدة VBA جديدة وكود الماكرو الجديد ويحفظ الإخراج بتنسيق XLSM. بمجرد فتحك لملف الإكسيل الناتج XLSM والنقر على أوامر **تطوير > الأساسيات المرئية**، سترى وحدة تسمى "الوحدة الاختبارية" وبداخلها سترى كود الماكرو التالي.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

فيما يلي رمز العينة لإنشاء ملف إكسيل الناتج بتنسيق XLSM مع وحدة VBA وكود الماكرو.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AddVBAModuleOrCode.py" >}}

## **تعديل VBA أو Macro في بايثون**

{{% alert color="primary" %}} 

يمكنك تعديل كود VBA أو Macro باستخدام Aspose.Cells لبايثون via .NET. أضاف Aspose.Cells لبايثون via .NET المساحات الاسمية والفئات التالية لقراءة وتعديل مشروع VBA في ملف Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

سيُوضح لك هذا المقال كيفية تغيير كود VBA أو Macro داخل ملف Excel المصدر باستخدام Aspose.Cells لبايثون via .NET.

{{% /alert %}} 

يقوم الرمز الخاص المعروض أدناه بتحميل ملف Excel المصدر الذي يحتوي على رمز VBA أو ماكرو التالي داخله

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

بعد تنفيذ نموذج Aspose.Cells لبايثون via .NET، سيتم تعديل كود VBA أو Macro بهذا الشكل

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

يمكنك تنزيل [ملف Excel المصدر](5112508.xlsm) و[ملف Excel الناتج](5112511.xlsm) من الروابط المعطاة.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-ModifyingVBAOrMacroCode.py" >}}

## **مواضيع متقدمة**
- [إضافة مرجع مكتبة إلى مشروع VBA في مصنف العمل](/cells/ar/python-net/add-a-library-reference-to-vba-project-in-workbook/)
- [التحقق مما إذا كان التوقيع الرقمي لرمز VBA صالحًا](/cells/ar/python-net/check-if-digital-signature-of-vba-code-is-valid/)
- [فحص ما إذا كان رمز VBA موقعًا](/cells/ar/python-net/check-if-vba-code-is-signed/)
- [التحقق مما إذا كان مشروع VBA في مصنف عمل موقعًا](/cells/ar/python-net/check-if-vba-project-in-a-workbook-is-signed/)
- [فحص ما إذا كان مشروع VBA محميًا ومقفلاً للعرض](/cells/ar/python-net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [توقيع رقمي لمشروع رمز VBA باستخدام شهادة](/cells/ar/python-net/digitally-sign-a-vba-code-project-with-certificate/)
- [تصدير شهادة VBA إلى ملف أو تيار](/cells/ar/python-net/export-vba-certificate-to-file-or-stream/)
- [تصفية مشروع VBA أثناء تحميل مصنف عمل](/cells/ar/python-net/filter-vba-project-while-loading-a-workbook/)
- [معرفة ما إذا كان مشروع VBA محميًا](/cells/ar/python-net/find-out-if-vba-project-is-protected/)
- [حماية كلمة المرور لمشروع VBA لمصنف عمل Excel](/cells/ar/python-net/password-protect-the-vba-project-of-excel-workbook/)

