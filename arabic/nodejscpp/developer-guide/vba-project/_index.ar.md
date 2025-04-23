---
title: إدارة أكواد VBA لمصنف إكسل مشغل، مع ماكرو
linktitle: مشروع الماكرو
type: docs
weight: 200
url: /ar/nodejs-cpp/manage-vba-project/
description: إضافة وحدة VBA وتعديل VBA أو الماكرو باستخدام Aspose.Cells for Node.js via C++.
---

## **إضافة وحدة VBA في Node.js**
{{% alert color="primary" %}}

يسمح Aspose.Cells بإضافة وحدة VBA جديدة وكود الماكرو باستخدام Aspose.Cells for Node.js via C++. يرجى استخدام طريقة [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#add-worksheet-) لإضافة وحدة VBA الجديدة داخل المصنف

{{% /alert %}}

إن الكود النموذجي التالي ينشئ مصنفًا جديدًا ويضيف وحدة VBA جديدة وكود ماكرو ويحفظ الناتج بصيغة XLSM. بمجرد فتح ملف XLSM الناتج في Microsoft Excel والنقر على أوامر قائمة **المطور > Visual Basic**، سترى وحدة باسم "TestModule" وداخلها سترى كود الماكرو التالي.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}

إليك الكود النموذجي لتوليد ملف XLSM الناتج مع وحدة VBA وكود الماكرو.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add VBA Module
const idx = workbook.getVbaProject().getModules().add(worksheet);

// Access the VBA Module, set its name and codes
const module = workbook.getVbaProject().getModules().get(idx);
module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```

## **تعديل VBA أو ماكرو في Node.js**

{{% alert color="primary" %}} 

يمكنك تعديل كود VBA أو الماكرو باستخدام Aspose.Cells for Node.js via C++. أضافت Aspose.Cells الوحدة والفئات التالية لقراءة وتعديل مشروع VBA في ملف Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

سيعرض هذا المقال لك كيفية تغيير رمز VBA أو الماكرو داخل ملف Excel المصدر باستخدام Aspose.Cells.

{{% /alert %}} 

يحمّل الكود النموذجي التالي ملف Excel المصدر الذي يحتوي على كود VBA أو الماكرو التالي بداخله

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

بعد تنفيذ رمز عينات Aspose.Cells، سيتم تعديل رمز VBA أو الماكرو مثل هذا

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

يمكنك تنزيل [ملف Excel المصدر](5112508.xlsm) و[ملف Excel الناتج](5112511.xlsm) من الروابط المعطاة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsm"));

// Change the VBA Module Code
const modules = workbook.getVbaProject().getModules();
const moduleCount = modules.getCount();
for (let i = 0; i < moduleCount; i++) {
const module = modules.get(i);
const code = module.getCodes();
if (code.includes("This is test message.")) 
{
code = code.replace("This is test message.", "This is Aspose.Cells message.");
module.setCodes(code);
}
}


// Save the output Excel file
workbook.save(path.join(dataDir, "output_out.xlsm"));
```

## **مواضيع متقدمة**
- [إضافة مرجع مكتبة إلى مشروع VBA في مصنف العمل](/cells/ar/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [تعيين الماكرو إلى عنصر تحكم النموذج](/cells/ar/nodejs-cpp/assign-macro-to-form-control/)
- [التحقق مما إذا كان التوقيع الرقمي لرمز VBA صالحًا](/cells/ar/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [فحص ما إذا كان رمز VBA موقعًا](/cells/ar/nodejs-cpp/check-if-vba-code-is-signed/)
- [التحقق مما إذا كان مشروع VBA في مصنف عمل موقعًا](/cells/ar/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [فحص ما إذا كان مشروع VBA محميًا ومقفلاً للعرض](/cells/ar/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [نسخ تصميم الاستوديو Form UserForm VBA Macro من القالب إلى دفتر العمل الهدف](/cells/ar/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [توقيع رقمي لمشروع رمز VBA باستخدام شهادة](/cells/ar/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [تصدير شهادة VBA إلى ملف أو تيار](/cells/ar/nodejs-cpp/export-vba-certificate-to-file-or-stream/)
- [تصفية مشروع VBA أثناء تحميل مصنف عمل](/cells/ar/nodejs-cpp/filter-vba-project-while-loading-a-workbook/)
- [معرفة ما إذا كان مشروع VBA محميًا](/cells/ar/nodejs-cpp/find-out-if-vba-project-is-protected/)
- [حماية كلمة المرور لمشروع VBA لمصنف عمل Excel](/cells/ar/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/)

