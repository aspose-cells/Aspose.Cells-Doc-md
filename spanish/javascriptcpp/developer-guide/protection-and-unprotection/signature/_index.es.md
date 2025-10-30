---
title: Asignar y validar firmas digitales con JavaScript vía C++
linktitle: Firma
type: docs
weight: 140
url: /es/javascript-cpp/assign-and-validate-digital-signatures/
description: Firma digital y verificación de archivos de Excel usando Aspose.Cells for JavaScript vía C++. Protege la autenticidad del contenido del libro con firmas digitales.
keywords: Firma digital de archivos de Excel, agregar firma digital a Excel con JavaScript vía C++, cómo validar firma digital con JavaScript vía C++
---

{{% alert color="primary" %}}  
Una firma digital proporciona garantía de que un archivo de libro de trabajo es válido y que nadie lo ha alterado. Puedes crear una firma digital personal usando el **Microsoft Selfcert.exe** u otra herramienta, o puedes comprar una firma digital. Después de crear una firma digital, debes adjuntarla a tu libro de trabajo. Adjuntar una firma digital es similar a sellar un sobre. Si un sobre llega sellado, tienes cierto nivel de seguridad de que nadie ha manipulado su contenido.  
{{% /alert %}}  

## **Introducción**  

Utilice el cuadro de diálogo de Firma digital para adjuntar una firma digital. El cuadro de diálogo de Firma digital lista los certificados válidos. Puede usar el cuadro de diálogo de Firma digital para ver certificados y seleccionar el que desea utilizar. Si un libro tiene una firma digital, el nombre de la firma aparece en el campo **Nombre del certificado**. Si hace clic en el botón **Quitar** en el cuadro de diálogo de Firma digital, Microsoft Excel también quita la firma digital.  

## **Cómo agregar firma digital para Excel**  

Aspose.Cells proporciona el módulo [**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature/) para realizar el trabajo (asignar y validar firmas digitales). El módulo tiene funciones útiles para agregar y validar firmas digitales.  

Por favor, vea el siguiente código de ejemplo que describe cómo puede realizar la tarea usando Aspose.Cells for JavaScript a través de la API de C++.  

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

## **Temas avanzados**  
- [Agregar firma digital a un archivo de Excel ya firmado](/cells/es/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Agregar línea de firma a la hoja de trabajo](/cells/es/javascript-cpp/add-signature-line/)  
- [Soporte para firma XAdES](/cells/es/javascript-cpp/support-for-xades-signature/)
