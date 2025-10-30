---
title: Dijital İmzalar Ata ve Doğrula ile JavaScript kullanarak
linktitle: İmza
type: docs
weight: 140
url: /tr/javascript-cpp/assign-and-validate-digital-signatures/
description: Aspose.Cells for JavaScript kullanarak Excel dosyalarına dijital imza ekleyin ve doğrulayın. Çalışma kitabı içeriğinin özgünlüğünü dijital imzalarla koruyun.
keywords: Excel dosyasına dijital imza ekleme, C++ ile JavaScript kullanarak Dijital İmza doğrulama ve geçerliliğini kontrol etme
---

{{% alert color="primary" %}}  
Bir dijital imza, bir çalışma kitabı dosyasının geçerli olduğunu ve kimse tarafından değiştirilmediğini sağlar. Kişisel bir dijital imza, **Microsoft Selfcert.exe** veya herhangi bir diğer araç kullanılarak veya satın alınarak oluşturulabilir. Dijital bir imza oluşturduktan sonra, çalışma kitabınıza eklemelisiniz. Bir dijital imza eklemek, bir zarfı mühürlemekle benzerdir. Bir mühürlü zarf gelirse, içeriği kimseyle oynamadığınızın belirli bir düzeyde güvencesine sahipsiniz demektir.  
{{% /alert %}}  

## **Giriş**  

Dijital İmza penceresini kullanarak bir dijital imza ekleyin. Dijital İmza iletişim kutusu geçerli sertifikaları listeler. Dijital İmza iletişim kutusunu, sertifikaları görüntülemek ve kullanmak istediğiniz birini seçmek için kullanabilirsiniz. Bir çalışma kitabı dijital bir imzaya sahipse, imzanın adı **Sertifika Adı** alanında görünür. Dijital İmza iletişim kutusundaki **Kaldır** düğmesine tıklarsanız, Microsoft Excel dijital imzayı da kaldırır.  

## **Excel için Dijital İmza Ekleme**  

Aspose.Cells, işi yapmak için [**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature/) modülünü sağlar (dijital imzaları atma ve doğrulama). Bu modül, dijital imza ekleme ve doğrulama için kullanışlı özellikler içerir.  

Lütfen C++ API aracılığıyla Aspose.Cells for JavaScript kullanarak görevi nasıl gerçekleştirebileceğinizi anlatan aşağıdaki örnek kodu inceleyin.  

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

## **Gelişmiş Konular**  
- [Daha önceden imzalanmış Excel dosyasına Dijital İmza ekleme](/cells/tr/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Çalışma sayfasına İmza satırı eklemek](/cells/tr/javascript-cpp/add-signature-line/)  
- [XAdES İmzası Desteği](/cells/tr/javascript-cpp/support-for-xades-signature/)
