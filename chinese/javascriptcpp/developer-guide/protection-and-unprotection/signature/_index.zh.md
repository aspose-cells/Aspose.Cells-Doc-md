---
title: 用 JavaScript 通过 C++ 赋予和验证数字签名
linktitle: 签名
type: docs
weight: 140
url: /zh/javascript-cpp/assign-and-validate-digital-signatures/
description: 使用 Aspose.Cells for JavaScript 通过 C++ 对 Excel 文件进行数字签名和验证。用数字签名保护工作簿内容的真实性。
keywords: Excel 文件数字签名，添加数字签名用于 JavaScript 通过 C++ 的 Excel，如何验证数字签名 JavaScript 通过 C++
---

{{% alert color="primary" %}}  
数字签名可以确保工作簿文件有效，并且没有人篡改它。您可以使用 Microsoft 的 Selfcert.exe 或其它工具创建个人数字签名，也可以购买数字签名。创建数字签名后，您必须将其附加到工作簿。附加数字签名类似于封口一个信封。若收到封好的信封，您可以一定程度上确保没有人篡改其内容。  
{{% /alert %}}  

## **介绍**  

使用数字签名对话框附加数字签名。数字签名对话框列出有效的证书。您可以使用数字签名对话框查看证书并选择要使用的证书。如果工作簿有数字签名，签名的名称会出现在 **证书名称** 栏中。如果在数字签名对话框中点击 **删除** 按钮，Microsoft Excel 也会删除数字签名。  

## **如何为Excel添加数字签名**  

Aspose.Cells提供[**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature/)模块以执行此任务（签署和验证数字签名）。该模块具有一些用于添加和验证数字签名的有用功能。  

请参考以下示例代码，描述如何使用 Aspose.Cells for JavaScript 通过 C++ API 执行该任务。  

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

## **高级主题**  
- [对已签名的 Excel 文件添加数字签名](/cells/zh/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [在工作表中添加签名行](/cells/zh/javascript-cpp/add-signature-line/)  
- [XAdES 签名的支持](/cells/zh/javascript-cpp/support-for-xades-signature/)
