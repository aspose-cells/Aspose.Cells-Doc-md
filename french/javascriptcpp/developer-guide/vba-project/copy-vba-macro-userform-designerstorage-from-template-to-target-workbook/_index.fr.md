---
title: Copiez le formulaire utilisateur de conception de macro VBA de la template vers le classeur cible avec JavaScript via C++
linktitle: Copier le UserForm DesignerStorage du macro VBA du modèle vers le classeur cible
type: docs
weight: 130
url: /fr/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: Apprenez comment copier un projet VBA, y compris le stockage de conception, d un fichier Excel à un autre en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

Aspose.Cells vous permet de copier un projet VBA d’un fichier Excel dans un autre fichier Excel. Un projet VBA comprend différents modules, c’est-à-dire Document, Procédural, Designer, etc. Tous les modules peuvent être copiés avec un code simple, mais pour le module Designer, il y a des données supplémentaires appelées Designer Storage qui doivent être accessibles ou copiées. Les deux méthodes suivantes traitent du Designer Storage.  

- [**VbaModuleCollection.designerStorage(string)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#designerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **Copier le stockage de concepteur de formulaire utilisateur de macro VBA du modèle vers le classeur cible**  

Veuillez voir le code d'exemple suivant. Il copie le projet VBA du [fichier Excel modèle](50528345.xlsm) dans un classeur vide et le sauvegarde sous le nom de [fichier Excel de sortie](50528346.xlsm). Si vous ouvrez le projet VBA dans le fichier Excel modèle, vous verrez un formulaire utilisateur comme illustré ci-dessous. Le formulaire utilisateur contient un Designer Storage, il sera donc copié en utilisant [**VbaModuleCollection.designerStorage(string)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#designerStorage-string-) et [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-) methods.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

La capture d'écran suivante montre le fichier Excel de sortie et son contenu, qui ont été copiés du fichier Excel modèle. Lorsque vous cliquez sur le bouton 1, cela ouvre le formulaire utilisateur VBA qui a lui-même un bouton de commande affichant une boîte de message lors du clic.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy VBA Designer UserForm Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, SheetType, VbaModuleType } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel macro-enabled (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create empty target workbook
            const target = new Workbook();

            // Load the Excel file containing VBA-Macro Designer User Form
            const templateFile = new Workbook(new Uint8Array(arrayBuffer));

            // Copy all template worksheets to target workbook
            const sheets = templateFile.worksheets;
            const sheetCount = sheets.count;
            for (let i = 0; i < sheetCount; i++) {
                const ws = sheets.get(i);
                if (ws.type === SheetType.Worksheet) {
                    const s = target.worksheets.add(ws.name);
                    s.copy(ws);

                    // Put message in cell A2 of the target worksheet
                    s.cells.get("A2").putValue("VBA Macro and User Form copied from template to target.");
                }
            }

            // Copy the VBA-Macro Designer UserForm from Template to Target 
            const modules = templateFile.vbaProject.modules;
            const moduleCount = modules.count;
            for (let i = 0; i < moduleCount; i++) {
                const vbaItem = modules.get(i);
                if (vbaItem.name === "ThisWorkbook") {
                    // Copy ThisWorkbook module code
                    target.vbaProject.modules.get("ThisWorkbook").codes = vbaItem.codes;
                } else {
                    console.log(vbaItem.name);

                    let vbaMod = 0;
                    const sheet = target.worksheets.sheetByCodeName(vbaItem.name);
                    if (sheet.isNull()) {
                        vbaMod = target.vbaProject.modules.add(vbaItem.type, vbaItem.name);
                    } else {
                        vbaMod = target.vbaProject.modules.add(sheet);
                    }

                    target.vbaProject.modules.get(vbaMod).codes = vbaItem.codes;

                    if (vbaItem.type === AsposeCells.VbaModuleType.Designer) {
                        // Get the data of the user form i.e. designer storage
                        const designerStorage = modules.getDesignerStorage(vbaItem.name);

                        // Add the designer storage to target Vba Project
                        target.vbaProject.modules.addDesignerStorage(vbaItem.name, designerStorage);
                    }
                }
            }

            // Saving the modified Excel file
            const outputData = target.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDesignerForm.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">VBA Designer UserForm copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
