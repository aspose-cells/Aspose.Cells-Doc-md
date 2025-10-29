---
title: Attribuer et valider les signatures numériques avec JavaScript via C++
linktitle: Signature
type: docs
weight: 140
url: /fr/javascript-cpp/assign-and-validate-digital-signatures/
description: Signature numérique et vérification du fichier Excel utilisant Aspose.Cells for JavaScript via C++. Protégez l authenticité du contenu du classeur avec des signatures numériques.
keywords: Signature numérique du fichier Excel, ajouter une signature numérique pour Excel JavaScript via C++, comment valider la signature numérique JavaScript via C++
---

{{% alert color="primary" %}}  
Une signature numérique garantit qu'un fichier de classeur est valide et qu'aucune altération n'a été apportée. Vous pouvez créer une signature numérique personnelle en utilisant Microsoft Selfcert.exe ou tout autre outil, ou vous pouvez en acheter une. Après avoir créé une signature numérique, vous devez la joindre à votre classeur. Joindre une signature numérique est similaire à sceller une enveloppe. Si une enveloppe arrive scellée, vous avez une certaine assurance que personne n'a trafiqué son contenu.  
{{% /alert %}}  

## **Introduction**  

Utilisez la boîte de dialogue Signature numérique pour joindre une signature numérique. La boîte de dialogue Signature numérique répertorie les certificats valides. Vous pouvez utiliser la boîte de dialogue Signature numérique pour afficher des certificats et sélectionner celui que vous souhaitez utiliser. Si un classeur a une signature numérique, le nom de la signature apparaît dans le champ **Nom du certificat**. Si vous cliquez sur le bouton **Supprimer** dans la boîte de dialogue Signature numérique, Microsoft Excel supprime également la signature numérique.  

## **Comment ajouter une signature numérique pour Excel**  

Aspose.Cells fournit le module [**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature/) pour effectuer la tâche (attribuer et valider des signatures numériques). Le module possède plusieurs fonctionnalités utiles pour ajouter et valider des signatures numériques.  

Veuillez voir l'exemple de code suivant qui décrit comment effectuer la tâche en utilisant le script Aspose.Cells for JavaScript via API C++.  

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

## **Sujets avancés**  
- [Ajouter une signature numérique à un fichier Excel déjà signé](/cells/fr/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Ajouter une ligne de signature au classeur](/cells/fr/javascript-cpp/add-signature-line/)  
- [Prise en charge de la signature XAdES](/cells/fr/javascript-cpp/support-for-xades-signature/)
