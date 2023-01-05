---
title: إدارة أكواد VBA لمصنف Excel Macro-Enabled.
linktitle: مشروع ماكرو
type: docs
weight: 200
url: /ar/net/manage-vba-project/
description: إضافة وحدة VBA النمطية وتعديل VBA أو ماكرو مع مكتبة Aspose.Cells.
---
## **أضف وحدة VBA النمطية في C#**
{{% alert color="primary" %}}

 يسمح لك Aspose.Cells بإضافة وحدة جديدة لـ VBA وكود ماكرو باستخدام Aspose.Cells. الرجاء استخدام[**Workbook.VbaProject.Modules.Add ()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) طريقة لإضافة وحدة VBA النمطية الجديدة داخل المصنف

{{% /alert %}}

ينشئ نموذج التعليمات البرمجية التالي مصنفًا جديدًا ويضيف وحدة VBA النمطية الجديدة ورمز الماكرو ويحفظ الإخراج بتنسيق XLSM. بمجرد فتح ملف الإخراج XLSM في Microsoft Excel والنقر فوق**المطور> Visual Basic** أوامر القائمة ، سترى وحدة تسمى "TestModule" وداخلها ، سترى رمز الماكرو التالي.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

فيما يلي نموذج التعليمات البرمجية لإنشاء ملف الإخراج XLSM باستخدام وحدة VBA وكود الماكرو.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **قم بتعديل VBA أو Macro في C#**

{{% alert color="primary" %}} 

يمكنك تعديل VBA أو Macro Code باستخدام Aspose.Cells. قام Aspose.Cells بإضافة مساحة الاسم والفئات التالية لقراءة وتعديل مشروع VBA في ملف Excel.

- Aspose.Cells.Vba
- VbaProject
- مجموعة VbaModuleCollection
- VbaModule

ستوضح لك هذه المقالة كيفية تغيير VBA أو Macro Code داخل ملف Excel المصدر باستخدام Aspose.Cells.

{{% /alert %}} 

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

 يمكنك تنزيل ملف[ملف Excel المصدر](5112508.xlsm) و ال[إخراج ملف Excel](5112511.xlsm) من الروابط المعطاة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **موضوعات مسبقة**
- [أضف مرجع مكتبة إلى مشروع VBA في المصنف](/cells/ar/net/add-a-library-reference-to-vba-project-in-workbook/)
- [تعيين ماكرو للتحكم في النموذج](/cells/ar/net/assign-macro-to-form-control/)
- [تحقق مما إذا كان التوقيع الرقمي لرمز VBA صالحًا](/cells/ar/net/check-if-digital-signature-of-vba-code-is-valid/)
- [تحقق مما إذا كان رمز VBA قد تم توقيعه](/cells/ar/net/check-if-vba-code-is-signed/)
- [تحقق مما إذا كان مشروع VBA في مصنف تم توقيعه](/cells/ar/net/check-if-vba-project-in-a-workbook-is-signed/)
- [تحقق مما إذا كان VBA Project محميًا ومؤمنًا للعرض](/cells/ar/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [نسخ VBA ماكرو UserForm DesignerStorage من قالب إلى المصنف الهدف](/cells/ar/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [قم بالتوقيع رقميًا على مشروع رمز VBA باستخدام الشهادة](/cells/ar/net/digitally-sign-a-vba-code-project-with-certificate/)
- [تصدير شهادة VBA إلى ملف أو دفق](/cells/ar/net/export-vba-certificate-to-file-or-stream/)
- [قم بتصفية مشروع VBA أثناء تحميل مصنف](/cells/ar/net/filter-vba-project-while-loading-a-workbook/)
- [اكتشف ما إذا كان VBA Project محميًا](/cells/ar/net/find-out-if-vba-project-is-protected/)
- [حماية كلمة المرور لمشروع VBA من مصنف Excel](/cells/ar/net/password-protect-the-vba-project-of-excel-workbook/)

