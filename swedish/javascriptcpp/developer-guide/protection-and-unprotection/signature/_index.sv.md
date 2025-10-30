---
title: Tilldela och validera digitala signaturer med JavaScript via C++
linktitle: Signatur
type: docs
weight: 140
url: /sv/javascript-cpp/assign-and-validate-digital-signatures/
description: Digital signatur och verifikation av Excel fil med Aspose.Cells for JavaScript via C++. Skydda äktheten av arbetsbokens innehåll med digitala signaturer.
keywords: Excel fil digital signatur, lägg till digital signatur för Excel JavaScript via C++, hur man validerar digital signatur JavaScript via C++
---

{{% alert color="primary" %}}  
En digital signatur ger försäkran om att en arbetsboksfil är giltig och att ingen har ändrat den. Du kan skapa en personlig digital signatur med Microsoft Selfcert.exe eller något annat verktyg, eller så kan du köpa en digital signatur. När du har skapat en digital signatur måste du bifoga den till din arbetsbok. Att bifoga en digital signatur är liknande att försegla ett kuvert. Om ett kuvert kommer förseglad har du en viss nivå av försäkran om att ingen har manipulerat dess innehåll.  
{{% /alert %}}  

## **Introduktion**  

Använd Digital Signature dialogrutan för att bifoga en digital signatur. Digital Signature dialogrutan listar giltiga certifikat. Du kan använda Digital Signature dialogrutan för att visa certifikat och välja det du vill använda. Om en arbetsbok har en digital signatur, visas namnet på signaturen i fältet Certifikatnamn. Om du klickar på knappen Ta bort i Digital Signature dialogrutan, tar Microsoft Excel bort den digitala signaturen också.  

## **Så här lägger du till digital signatur för Excel**  

Aspose.Cells tillhandahåller modulen [**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature/) för att utföra jobbet (tilldela och validera digitala signaturer). Modulen har några användbara funktioner för att lägga till och validera digitala signaturer.  

Se följande exempel på kod som beskriver hur du kan utföra uppgiften med Aspose.Cells for JavaScript via C++ API.  

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

## **Fortsatta ämnen**  
- [Lägg till digital signatur i en redan signerad Excel-fil](/cells/sv/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Lägg till signaturraden i arbetsbladet](/cells/sv/javascript-cpp/add-signature-line/)  
- [Stöd för XAdES-signatur](/cells/sv/javascript-cpp/support-for-xades-signature/)
