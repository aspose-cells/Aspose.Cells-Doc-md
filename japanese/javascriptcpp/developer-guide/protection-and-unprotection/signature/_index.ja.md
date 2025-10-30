---
title: デジタル署名の割り当てと検証（JavaScript/C++経由）
linktitle: 署名
type: docs
weight: 140
url: /ja/javascript-cpp/assign-and-validate-digital-signatures/
description: Aspose.Cells for JavaScriptを使用したExcelファイルのデジタル署名と検証。ブックの内容の真正性をデジタル署名で保護します。
keywords: Excelファイルのデジタル署名を追加し、JavaScriptをC++経由でデジタル署名の検証方法を学びます
---

{{% alert color="primary" %}}  
デジタル署名は、ブックファイルが有効であり、誰もがそれを変更していないことを保証します。 **Microsoft Selfcert.exe**または他のツールを使用して個人用のデジタル署名を作成したり、デジタル署名を購入したりすることができます。デジタル署名を作成した後は、それをブックに添付する必要があります。デジタル署名を添付することは、封筒を封印することと似ています。封がされた封筒が届いた場合、その内容が誰もが触れていないレベルの保証が得られます。  
{{% /alert %}}  

## **紹介**  

デジタル署名を添付するには、デジタル署名ダイアログを使用します。デジタル署名ダイアログには有効な証明書が一覧表示されます。デジタル署名ダイアログでは、証明書を表示し、使用する証明書を選択することができます。ブックにデジタル署名がある場合、署名の名前が**証明書名**フィールドに表示されます。デジタル署名ダイアログの**削除**ボタンをクリックすると、Microsoft Excelはデジタル署名も削除します。  

## **Excelにデジタル署名を追加する方法**  

Aspose.Cellsは[**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature/)モジュールを提供し、デジタル署名の割り当てと検証を行います。このモジュールには、デジタル署名を追加・検証するための便利な機能があります。  

C++ API経由でAspose.Cells for JavaScriptを使用してタスクを実行する方法を示すサンプルコードを以下に示します。  

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

## **高度なトピック**  
- [すでに署名されたExcelファイルにデジタル署名を追加する](/cells/ja/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [ワークシートに署名行を追加](/cells/ja/javascript-cpp/add-signature-line/)  
- [XAdES署名のサポート](/cells/ja/javascript-cpp/support-for-xades-signature/)
