---  
title: تعيين والتحقق من التواقيع الرقمية باستخدام Node.js عبر C++  
linktitle: توقيع  
type: docs  
weight: 140  
url: /ar/nodejs-cpp/assign-and-validate-digital-signatures/  
description: توقيع والتحقق من التوقيع الرقمي لملف إكسل باستخدام Aspose.Cells for Node.js via C++. حماية أصالة محتوى المصنف بواسطة التواقيع الرقمية.  
keywords: توقيع رقمي لملف إكسل، إضافة توقيع رقمي لـ Node.js عبر C++، كيفية التحقق من التوقيع الرقمي Node.js عبر C++  
---  

{{% alert color="primary" %}}  
يوفر التوقيع الرقمي ضمانًا بأن ملف دفتر العمل صالح وأن أحدًا لم يعدله. يمكنك إنشاء توقيع رقمي شخصي باستخدام **Microsoft Selfcert.exe** أو أي أداة أخرى، أو يمكنك شراء توقيع رقمي. بعد انشاء توقيع رقمي، يجب عليك إرفاقه بدفتر العمل الخاص بك. إرفاق توقيع رقمي مماثل لختم مظروف. إذا وصل مظروف مختوم، فإن لديك بعض مستوى الثقة بأن أحدًا لم يحرك محتوياته.  
{{% /alert %}}  

## **مقدمة**  

استخدم مربع الحوار للتوقيع الرقمي لربط توقيع رقمي. يُدرِج مربع الحوار للتوقيع الرقمي الشهادات الصالحة. يمكنك استخدام مربع الحوار للتوقيع الرقمي لعرض الشهادات واختيار تلك التي تريد استخدامها. إذا كان لدى دفتر العمل توقيع رقمي، فإن اسم التوقيع يظهر في حقل **اسم الشهادة**. إذا قمت بالنقر على زر **إزالة** في مربع الحوار للتوقيع الرقمي، فإن Microsoft Excel يزيل التوقيع الرقمي أيضًا.  

## **كيفية إضافة توقيع رقمي لملف Excel**  

يوفر Aspose.Cells وحدة [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature/) لأداء المهمة (تعيين والتحقق من التواقيع الرقمية). تحتوي الوحدة على بعض الميزات المفيدة لإضافة والتحقق من التواقيع الرقمية.  

يرجى الاطلاع على الشفرة النموذجية التالية التي تصف كيفية أداء المهمة باستخدام واجهة برمجة تطبيقات Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const certPassword = "aa";

// dsc is signature collection that contains one or more signatures needed to sign
const dsc = new AsposeCells.DigitalSignatureCollection();

// Cert must contain a private key, it can be constructed from a cert file or Windows certificate collection.
const cert = new AsposeCells.DigitalSignature(dataDir + "mykey2.pfx", certPassword, "test for sign", new Date());
dsc.add(cert);

const wb = new AsposeCells.Workbook();

// wb.setDigitalSignature signs all signatures in dsc
wb.setDigitalSignature(dsc);
wb.save(path.join(dataDir, "newfile_out.xlsx"));

// open the file
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "newfile_out.xlsx"));
console.log(wb2.isDigitallySigned);

// Get digitalSignature collection from workbook
const dsc2 = wb2.getDigitalSignature();
const digitalSignatures = dsc2.getEnumerator();
for (var dst of digitalSignatures)
{
    console.log(dst.getComments()); // test for sign - OK
    console.log(dst.getSignTime()); // 11/25/2010 1:22:01 PM - OK
    console.log(dst.isValid()); // True - OK
}

```  

## **مواضيع متقدمة**  
- [إضافة توقيع رقمي إلى ملف إكسل تم توقيعه بالفعل](/cells/ar/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [إضافة خط توقيع إلى ورقة العمل](/cells/ar/nodejs-cpp/add-signature-line/)  
- [دعم لـ توقيع XAdES](/cells/ar/nodejs-cpp/support-for-xades-signature/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
