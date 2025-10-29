---
title: تعيين والتحقق من التوقيعات الرقمية باستخدام JavaScript عبر C++
linktitle: توقيع
type: docs
weight: 140
url: /ar/javascript-cpp/assign-and-validate-digital-signatures/
description: توقيع مستندات ملف إكسل والتحقق منها باستخدام Aspose.Cells for JavaScript عبر C++. حماية أصالة محتوى دفتر العمل باستخدام التوقيعات الرقمية.
keywords: التوقيع الرقمي لملف إكسل، إضافة توقيع رقمي لملف إكسل باستخدام JavaScript عبر C++، كيفية التحقق من التوقيع الرقمي باستخدام JavaScript عبر C++
---

{{% alert color="primary" %}}  
يوفر التوقيع الرقمي ضمانًا بأن ملف دفتر العمل صالح وأن أحدًا لم يعدله. يمكنك إنشاء توقيع رقمي شخصي باستخدام **Microsoft Selfcert.exe** أو أي أداة أخرى، أو يمكنك شراء توقيع رقمي. بعد انشاء توقيع رقمي، يجب عليك إرفاقه بدفتر العمل الخاص بك. إرفاق توقيع رقمي مماثل لختم مظروف. إذا وصل مظروف مختوم، فإن لديك بعض مستوى الثقة بأن أحدًا لم يحرك محتوياته.  
{{% /alert %}}  

## **مقدمة**  

استخدم مربع الحوار للتوقيع الرقمي لربط توقيع رقمي. يُدرِج مربع الحوار للتوقيع الرقمي الشهادات الصالحة. يمكنك استخدام مربع الحوار للتوقيع الرقمي لعرض الشهادات واختيار تلك التي تريد استخدامها. إذا كان لدى دفتر العمل توقيع رقمي، فإن اسم التوقيع يظهر في حقل **اسم الشهادة**. إذا قمت بالنقر على زر **إزالة** في مربع الحوار للتوقيع الرقمي، فإن Microsoft Excel يزيل التوقيع الرقمي أيضًا.  

## **كيفية إضافة توقيع رقمي لملف Excel**  

يوفر Aspose.Cells وحدة [**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature/) لأداء المهمة (تعيين والتحقق من التواقيع الرقمية). تحتوي الوحدة على بعض الميزات المفيدة لإضافة والتحقق من التواقيع الرقمية.  

يرجى الاطلاع على عينة الكود التالية التي تصف كيفية أداء المهمة باستخدام Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات C++.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Digital Signature: Sign and Verify Workbook</h1>

        <label for="pfxInput">Select PFX Certificate (.pfx):</label>
        <input type="file" id="pfxInput" accept=".pfx" />
        <br /><br />

        <label for="certPassword">Certificate Password:</label>
        <input type="text" id="certPassword" value="aa" />
        <br /><br />

        <label for="signatureComment">Signature Comment:</label>
        <input type="text" id="signatureComment" value="test for sign" />
        <br /><br />

        <button id="runExample">Sign Workbook and Verify</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, DigitalSignature, DigitalSignatureCollection } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const pfxInput = document.getElementById('pfxInput');
            if (!pfxInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .pfx certificate file.</p>';
                return;
            }

            const password = document.getElementById('certPassword').value || "";
            const comment = document.getElementById('signatureComment').value || "";

            // Read the PFX file
            const pfxFile = pfxInput.files[0];
            const pfxArrayBuffer = await pfxFile.arrayBuffer();
            const pfxBytes = new Uint8Array(pfxArrayBuffer);

            // dsc is signature collection that contains one or more signatures needed to sign
            const dsc = new DigitalSignatureCollection();

            // Cert must contain a private key, constructed from the PFX bytes
            const cert = new DigitalSignature(pfxBytes, password, comment, new Date());
            dsc.add(cert);

            // Create a new workbook
            const wb = new Workbook();

            // wb.setDigitalSignature signs all signatures in dsc -> converted to property assignment
            wb.digitalSignature = dsc;

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'newfile_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Signed Excel File';

            // Open the file from the generated data to verify signatures
            const wb2 = new Workbook(new Uint8Array(outputData));

            // isDigitallySigned property
            const signedStatus = wb2.isDigitallySigned;

            // Get digitalSignature collection from workbook
            const dsc2 = wb2.digitalSignature;
            let detailsHtml = `<p style="color: green;">Workbook signed: ${signedStatus}</p>`;

            if (dsc2 && dsc2.count > 0) {
                detailsHtml += '<h3>Signatures:</h3><ul>';
                for (let i = 0; i < dsc2.count; i++) {
                    const dst = dsc2.get(i);
                    const dstComments = dst.comments;
                    const dstSignTime = dst.signTime;
                    const dstIsValid = dst.isValid ? dst.isValid() : "N/A";
                    detailsHtml += `<li>
                        <strong>Signature ${i + 1}:</strong><br/>
                        Comments: ${dstComments}<br/>
                        Sign Time: ${dstSignTime}<br/>
                        Is Valid: ${dstIsValid}
                    </li>`;
                }
                detailsHtml += '</ul>';
            } else {
                detailsHtml += '<p>No digital signatures found in the workbook.</p>';
            }

            document.getElementById('result').innerHTML = detailsHtml;
        });
    </script>
</html>
```  

## **مواضيع متقدمة**  
- [إضافة توقيع رقمي إلى ملف إكسل تم توقيعه بالفعل](/cells/ar/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [إضافة خط توقيع إلى ورقة العمل](/cells/ar/javascript-cpp/add-signature-line/)  
- [دعم لـ توقيع XAdES](/cells/ar/javascript-cpp/support-for-xades-signature/)
