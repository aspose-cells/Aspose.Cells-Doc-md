---
title: Digitale Signaturen zuweisen und validieren mit JavaScript via C++
linktitle: Signatur
type: docs
weight: 140
url: /de/javascript-cpp/assign-and-validate-digital-signatures/
description: Digitale Signatur und Verifizierung der Excel Datei mit Aspose.Cells for JavaScript via C++. Schützen Sie die Echtheit des Arbeitsbuchinhalts mit digitalen Signaturen.
keywords: Digitale Signatur der Excel Datei, digitale Signatur für Excel mit JavaScript via C++, Validierung der digitalen Signatur mit JavaScript via C++
---

{{% alert color="primary" %}}  
Eine digitale Signatur gewährleistet, dass eine Arbeitsmappe gültig ist und niemand sie verändert hat. Sie können eine persönliche digitale Signatur mithilfe des **Microsoft Selfcert.exe** oder eines anderen Tools erstellen oder eine digitale Signatur erwerben. Nachdem Sie eine digitale Signatur erstellt haben, müssen Sie sie Ihrer Arbeitsmappe hinzufügen. Das Anhängen einer digitalen Signatur ähnelt dem Versiegeln eines Umschlags. Wenn ein versiegelter Umschlag ankommt, haben Sie eine gewisse Sicherheit, dass niemand seinen Inhalt manipuliert hat.  
{{% /alert %}}  

## **Einführung**  

Verwenden Sie den Digital Signature-Dialog, um eine digitale Signatur anzuhängen. Der Digital Signature-Dialog listet gültige Zertifikate auf. Sie können den Digital Signature-Dialog verwenden, um Zertifikate anzuzeigen und das gewünschte Zertifikat auszuwählen. Wenn eine Arbeitsmappe eine digitale Signatur hat, erscheint der Name der Signatur im **Zertifikatname**-Feld. Wenn Sie auf die Schaltfläche **Entfernen** im Digital Signature-Dialog klicken, entfernt Microsoft Excel auch die digitale Signatur.  

## **Wie man eine digitale Signatur für Excel hinzufügt**  

Aspose.Cells bietet das [**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature/) Modul, um die Aufgabe auszuführen (digitale Signaturen zuzuweisen und zu validieren). Das Modul verfügt über nützliche Funktionen zum Hinzufügen und Überprüfen digitaler Signaturen.  

Siehe den folgenden Beispielcode, der zeigt, wie Sie die Aufgabe mit dem Aspose.Cells for JavaScript über C++ API ausführen können.  

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

## **Erweiterte Themen**  
- [Fügen Sie eine digitale Signatur zu einer bereits signierten Excel-Datei hinzu](/cells/de/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Fügen Sie der Arbeitsmappe eine Signaturzeile hinzu](/cells/de/javascript-cpp/add-signature-line/)  
- [Unterstützung für XAdES-Signatur](/cells/de/javascript-cpp/support-for-xades-signature/)
