---
title: إدارة رموز VBA لمصنف العمل ذو الماكرو الممكن تمكينه.
linktitle: مشروع الماكرو
type: docs
weight: 200
url: /ar/net/manage-vba-project/
description: إضافة وحدة VBA وتعديل VBA أو الماكرو بمكتبة Aspose.Cells.
---

## **إضافة وحدة VBA في C#**
{{% alert color="primary" %}}

Aspose.Cells تسمح لك بإضافة وحدة VBA جديدة وكود الماكرو باستخدام Aspose.Cells. يُرجى استخدام الطريقة [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) لإضافة وحدة VBA جديدة داخل المصنف.

{{% /alert %}}

يُنشئ رمز العينة التالي مصنف عمل جديد ويضيف وحدة VBA جديدة وكود الماكرو الجديد ويحفظ الإخراج بتنسيق XLSM. بمجرد فتحك لملف الإكسيل الناتج XLSM والنقر على أوامر **تطوير > الأساسيات المرئية**، سترى وحدة تسمى "الوحدة الاختبارية" وبداخلها سترى كود الماكرو التالي.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

فيما يلي رمز العينة لإنشاء ملف إكسيل الناتج بتنسيق XLSM مع وحدة VBA وكود الماكرو.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **تعديل VBA أو الماكرو في C#**

{{% alert color="primary" %}} 

يمكنك تعديل الكود الخاص ب VBA أو الماكرو باستخدام Aspose.Cells. لقد قامت Aspose.Cells بإضافة مساحة الاسم التالية والفئات لقراءة وتعديل مشروع VBA في ملف الإكسيل.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

سيعرض هذا المقال لك كيفية تغيير رمز VBA أو الماكرو داخل ملف Excel المصدر باستخدام Aspose.Cells.

{{% /alert %}} 

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

يمكنك تنزيل [ملف Excel المصدر](5112508.xlsm) و[ملف Excel الناتج](5112511.xlsm) من الروابط المعطاة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **مواضيع متقدمة**
- [إضافة مرجع مكتبة إلى مشروع VBA في مصنف العمل](/cells/ar/net/add-a-library-reference-to-vba-project-in-workbook/)
- [تعيين الماكرو إلى عنصر تحكم النموذج](/cells/ar/net/assign-macro-to-form-control/)
- [التحقق مما إذا كان التوقيع الرقمي لرمز VBA صالحًا](/cells/ar/net/check-if-digital-signature-of-vba-code-is-valid/)
- [فحص ما إذا كان رمز VBA موقعًا](/cells/ar/net/check-if-vba-code-is-signed/)
- [التحقق مما إذا كان مشروع VBA في مصنف عمل موقعًا](/cells/ar/net/check-if-vba-project-in-a-workbook-is-signed/)
- [فحص ما إذا كان مشروع VBA محميًا ومقفلاً للعرض](/cells/ar/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [نسخ تصميم الاستوديو Form UserForm VBA Macro من القالب إلى دفتر العمل الهدف](/cells/ar/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [توقيع رقمي لمشروع رمز VBA باستخدام شهادة](/cells/ar/net/digitally-sign-a-vba-code-project-with-certificate/)
- [تصدير شهادة VBA إلى ملف أو تيار](/cells/ar/net/export-vba-certificate-to-file-or-stream/)
- [تصفية مشروع VBA أثناء تحميل مصنف عمل](/cells/ar/net/filter-vba-project-while-loading-a-workbook/)
- [معرفة ما إذا كان مشروع VBA محميًا](/cells/ar/net/find-out-if-vba-project-is-protected/)
- [حماية كلمة المرور لمشروع VBA لمصنف عمل Excel](/cells/ar/net/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="csharp" >}}
