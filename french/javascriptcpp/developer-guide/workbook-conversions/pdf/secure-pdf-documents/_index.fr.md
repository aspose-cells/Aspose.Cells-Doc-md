---
title: Protégez les documents PDF avec JavaScript via C++
linktitle: Documents PDF sécurisés
type: docs
weight: 120
url: /fr/javascript-cpp/secure-pdf-documents/
description: Apprenez comment sécuriser les documents PDF en utilisant des mots de passe propriétaire et utilisateur, et définir les permissions pour les fichiers PDF en utilisant le script Aspose.Cells for Java via C++.
---

{{% alert color="primary" %}}

Parfois, les développeurs ont besoin de travailler avec des fichiers PDF cryptés. Par exemple :

- Sécuriser les documents avec des mots de passe propriétaire et utilisateur afin que n'importe qui ne puisse pas l'ouvrir.
- Définir des restrictions ou des autorisations sur le document après l'ouverture du document. par exemple, restreindre si le contenu du document peut être imprimé ou extrait.

Cet article explique comment passer des options de sécurité PDF lors de l'enregistrement des feuilles de calcul au format PDF.

{{% /alert %}}

Aspose.Cells fournit [**PdfSecurityOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/) pour travailler avec la sécurité. Vous pouvez définir des mots de passe propriétaire et utilisateur lors de l'enregistrement en PDF. Le mot de passe propriétaire ou utilisateur sera nécessaire pour ouvrir le PDF crypté pour la visualisation.

- Le mot de passe utilisateur peut être nul ou une chaîne vide ; dans ce cas, aucun mot de passe ne sera requis lors de l'ouverture du PDF.
- Ouvrir le document PDF avec le bon mot de passe propriétaire donne un accès complet (sans restrictions d'accès spécifiées) au document.
- Ouvrir le document PDF avec le bon mot de passe utilisateur (ou ouvrir un document qui n'a pas de mot de passe utilisateur) permet un accès limité comme les autorisations spécifiées.

Le code d'exemple ci-dessous décrit comment sécuriser des PDF avec Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Secure PDF Example</title>
    </head>
    <body>
        <h1>Secure PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PDF save options and security options
            const saveOption = new PdfSaveOptions();
            saveOption.securityOptions = new PdfSecurityOptions();

            // Set security options (converted from getters/setters to properties)
            saveOption.securityOptions.userPassword = "user";
            saveOption.securityOptions.ownerPassword = "owner";
            saveOption.securityOptions.extractContentPermission = false;
            saveOption.securityOptions.printPermission = false;

            // Save the workbook to PDF with security options
            const outputData = workbook.save(SaveFormat.Pdf, saveOption);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'securepdf_test.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Secure PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the secured PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Si le classeur contient des formules, il est préférable d'appeler [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) juste avant de le rendre au format PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
