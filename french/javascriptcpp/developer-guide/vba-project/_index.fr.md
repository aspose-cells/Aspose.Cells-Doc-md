---
title: Gérer les codes VBA du classeur Excel activé par macro
linktitle: Projet de macro
type: docs
weight: 200
url: /fr/javascript-cpp/manage-vba-project/
description: Ajouter un module VBA et modifier VBA ou la macro avec Aspose.Cells for JavaScript via C++.
---

## **Ajouter un module VBA en JavaScript via C++**
{{% alert color="primary" %}}

Aspose.Cells vous permet d'ajouter un nouveau module VBA et un code de macro en utilisant Aspose.Cells for JavaScript via C++. Veuillez utiliser la méthode [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#add-worksheet-) pour ajouter le nouveau module VBA dans le classeur

{{% /alert %}}

Le code d'exemple suivant crée un nouveau classeur et ajoute un nouveau module VBA ainsi qu'un code macro, puis enregistre le résultat au format XLSM. Une fois que vous ouvrez le fichier XLSM dans Microsoft Excel et que vous cliquez sur les commandes du menu **Developer > Visual Basic**, vous verrez un module nommé "TestModule" et à l'intérieur, vous verrez le code macro suivant.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add VBA Module</title>
    </head>
    <body>
        <h1>Add VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Create new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add VBA Module
            const idx = workbook.vbaProject.modules.add(worksheet);

            // Access the VBA Module, set its name and codes
            const module = workbook.vbaProject.modules.get(idx);
            module.name = "TestModule";
            module.codes = "Sub ShowMessage()\r\n" +
                           "    MsgBox \"Welcome to Aspose!\"\r\n" +
                           "End Sub";

            // Save the workbook as XLSM and prepare download
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel.sheet.macroEnabled.12" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Modifier VBA ou Macro en JavaScript via C++**

{{% alert color="primary" %}} 

Vous pouvez modifier le code VBA ou Macro en utilisant Aspose.Cells for JavaScript via C++. Aspose.Cells a ajouté les modules et classes suivants pour lire et modifier le projet VBA dans le fichier Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Cet article vous montrera comment modifier le code VBA ou Macro à l'intérieur du fichier Excel source en utilisant Aspose.Cells.

{{% /alert %}} 

Le code d'exemple suivant charge le fichier Excel source qui contient le code VBA ou Macro suivant.

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Après l'exécution du code d'exemple Aspose.Cells, le code VBA ou Macro sera modifié comme ceci

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Vous pouvez télécharger le [fichier Excel source](5112508.xlsm) et le [fichier Excel de sortie](5112511.xlsm) à partir des liens donnés.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change VBA Module Code Example</title>
    </head>
    <body>
        <h1>Change VBA Module Code Example</h1>
        <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access VBA project modules
            const modules = workbook.vbaProject.modules;
            const moduleCount = modules.count;
            for (let i = 0; i < moduleCount; i++) {
                const module = modules.get(i);
                let code = module.codes;
                if (code && code.includes("This is test message.")) {
                    code = code.replace("This is test message.", "This is Aspose.Cells message.");
                    module.codes = code;
                }
            }

            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">VBA module code updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Ajouter une référence de bibliothèque au projet VBA dans le classeur](/cells/fr/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Attribuer une macro à un contrôle de formulaire](/cells/fr/javascript-cpp/assign-macro-to-form-control/)
- [Vérifier si la signature numérique du code VBA est valide](/cells/fr/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Vérifier si le code VBA est signé](/cells/fr/javascript-cpp/check-if-vba-code-is-signed/)
- [Vérifier si le projet VBA dans un classeur est signé](/cells/fr/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Vérifier si le projet VBA est protégé et verrouillé pour la visualisation](/cells/fr/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copier le stockage de concepteur de formulaire utilisateur de macro VBA du modèle vers le classeur cible](/cells/fr/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Signer numériquement un projet de code VBA avec un certificat](/cells/fr/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Exporter le certificat VBA vers un fichier ou un flux](/cells/fr/javascript-cpp/export-vba-certificate-to-file-or-stream/)
- [Filtrer le projet VBA lors du chargement d'un classeur](/cells/fr/javascript-cpp/filter-vba-project-while-loading-a-workbook/)
- [Découvrir si le projet VBA est protégé](/cells/fr/javascript-cpp/find-out-if-vba-project-is-protected/)
- [Protéger par mot de passe le projet VBA du classeur Excel](/cells/fr/javascript-cpp/password-protect-the-vba-project-of-excel-workbook/)
