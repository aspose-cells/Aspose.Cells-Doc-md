---
title: Gérer les codes VBA du classeur Excel activé par macro
linktitle: Projet de macro
type: docs
weight: 200
url: /fr/nodejs-cpp/manage-vba-project/
description: Ajouter un module VBA et modifier le VBA ou la macro avec Aspose.Cells for Node.js via C++.
---

## **Ajouter un module VBA dans Node.js**
{{% alert color="primary" %}}

Aspose.Cells vous permet d’ajouter un nouveau module VBA et un code macro en utilisant Aspose.Cells for Node.js via C++. Veuillez utiliser la méthode [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#add-worksheet-) pour ajouter le nouveau module VBA dans le classeur

{{% /alert %}}

Le code d'exemple suivant crée un nouveau classeur et ajoute un nouveau module VBA ainsi qu'un code macro, puis enregistre le résultat au format XLSM. Une fois que vous ouvrez le fichier XLSM dans Microsoft Excel et que vous cliquez sur les commandes du menu **Developer > Visual Basic**, vous verrez un module nommé "TestModule" et à l'intérieur, vous verrez le code macro suivant.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}

Voici un exemple de code pour générer le fichier XLSM avec un module VBA et un code macro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add VBA Module
const idx = workbook.getVbaProject().getModules().add(worksheet);

// Access the VBA Module, set its name and codes
const module = workbook.getVbaProject().getModules().get(idx);
module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```

## **Modifier VBA ou Macro dans Node.js**

{{% alert color="primary" %}} 

Vous pouvez modifier le code VBA ou Macro en utilisant Aspose.Cells for Node.js via C++. Aspose.Cells a ajouté le module et les classes suivantes pour lire et modifier le projet VBA dans le fichier Excel.

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

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsm"));

// Change the VBA Module Code
const modules = workbook.getVbaProject().getModules();
const moduleCount = modules.getCount();
for (let i = 0; i < moduleCount; i++) {
const module = modules.get(i);
const code = module.getCodes();
if (code.includes("This is test message.")) 
{
code = code.replace("This is test message.", "This is Aspose.Cells message.");
module.setCodes(code);
}
}


// Save the output Excel file
workbook.save(path.join(dataDir, "output_out.xlsm"));
```

## **Sujets avancés**
- [Ajouter une référence de bibliothèque au projet VBA dans le classeur](/cells/fr/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Attribuer une macro à un contrôle de formulaire](/cells/fr/nodejs-cpp/assign-macro-to-form-control/)
- [Vérifier si la signature numérique du code VBA est valide](/cells/fr/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Vérifier si le code VBA est signé](/cells/fr/nodejs-cpp/check-if-vba-code-is-signed/)
- [Vérifier si le projet VBA dans un classeur est signé](/cells/fr/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Vérifier si le projet VBA est protégé et verrouillé pour la visualisation](/cells/fr/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copier le stockage de concepteur de formulaire utilisateur de macro VBA du modèle vers le classeur cible](/cells/fr/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Signer numériquement un projet de code VBA avec un certificat](/cells/fr/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Exporter le certificat VBA vers un fichier ou un flux](/cells/fr/nodejs-cpp/export-vba-certificate-to-file-or-stream/)
- [Filtrer le projet VBA lors du chargement d'un classeur](/cells/fr/nodejs-cpp/filter-vba-project-while-loading-a-workbook/)
- [Découvrir si le projet VBA est protégé](/cells/fr/nodejs-cpp/find-out-if-vba-project-is-protected/)
- [Protéger par mot de passe le projet VBA du classeur Excel](/cells/fr/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="nodejs-cpp" >}}
