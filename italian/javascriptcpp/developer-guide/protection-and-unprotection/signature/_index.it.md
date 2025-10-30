---
title: Assegna e convalida firme digitali con JavaScript via C++
linktitle: Firma
type: docs
weight: 140
url: /it/javascript-cpp/assign-and-validate-digital-signatures/
description: Firma digitale del file Excel e verifica usando Aspose.Cells for JavaScript via C++. Proteggi l autenticità del contenuto del workbook con firme digitali.
keywords: Firma digitale del file Excel, Aggiungi firma digitale per Excel JavaScript via C++, Come convalidare la firma digitale JavaScript via C++
---

{{% alert color="primary" %}}  
Una firma digitale garantisce che un file di cartella di lavoro sia valido e che nessuno lo abbia alterato. È possibile creare una firma digitale personale utilizzando **Microsoft Selfcert.exe** o qualsiasi altro strumento, oppure è possibile acquistare una firma digitale. Dopo aver creato una firma digitale, è necessario allegarla alla cartella di lavoro. Allegare una firma digitale è simile a sigillare una busta. Se una busta arriva sigillata, si ha un certo livello di garanzia che nessuno abbia manomesso i suoi contenuti.  
{{% /alert %}}  

## **Introduzione**  

Utilizzare il dialogo Firma digitale per allegare una firma digitale. Il dialogo Firma digitale elenca certificati validi. È possibile utilizzare il dialogo Firma digitale per visualizzare i certificati e selezionare quello che si desidera utilizzare. Se una cartella di lavoro ha una firma digitale, il nome della firma appare nel campo **Nome certificato**. Se si fa clic sul pulsante **Rimuovi** nel dialogo Firma digitale, Microsoft Excel rimuove anche la firma digitale.  

## **Come aggiungere una firma digitale per Excel**  

Aspose.Cells fornisce il modulo [**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature/) per eseguire il lavoro (assegnare e convalidare firme digitali). Il modulo ha alcune caratteristiche utili per aggiungere e validare firme digitali.  

Consulta il seguente esempio di codice che descrive come eseguire il task utilizzando Aspose.Cells for JavaScript tramite API C++.  

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

## **Argomenti avanzati**  
- [Aggiungi firma digitale a un file Excel già firmato](/cells/it/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Aggiungi linea di firma al foglio di calcolo](/cells/it/javascript-cpp/add-signature-line/)  
- [Supporto per la firma XAdES](/cells/it/javascript-cpp/support-for-xades-signature/)
