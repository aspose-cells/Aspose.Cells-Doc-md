---
title: Fournissez le chemin du fichier HTML de la feuille exportée via l interface IFilePathProvider avec Node.js via C++
linktitle: Fournir le chemin du fichier HTML de la feuille de calcul exportée via l interface IFilePathProvider
type: docs
weight: 70
url: /fr/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Scénarios d'utilisation possibles**
Supposons que vous ayez un fichier Excel avec plusieurs feuilles et que vous souhaitez exporter chaque feuille dans un fichier HTML individuel. Si l'une de vos feuilles contient des liens vers d'autres feuilles, ces liens seront brisés dans le HTML exporté. Pour résoudre ce problème, Aspose.Cells for Node.js via C++ fournit l'interface [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider), que vous pouvez implémenter pour corriger les liens cassés.

## **Fournir le chemin du fichier HTML de la feuille de calcul exportée via l'interface IFilePathProvider**
Veuillez télécharger le [fichier Excel d'exemple](5115213.zip) utilisé dans le code ci-dessous et ses fichiers HTML exportés. Tous ces fichiers se trouvent dans le répertoire Temp. Vous devriez l'extraire sur le lecteur C:. Ensuite, il deviendra le répertoire C:\Temp. Ensuite, vous ouvrirez le fichier Sheet1.html dans le navigateur et cliquerez sur les deux liens à l’intérieur. Ces liens font référence à ces deux feuilles HTML exportées qui se trouvent dans le répertoire C:\Temp\OtherSheets.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

La capture d'écran suivante montre à quoi ressemblent le C:\Temp\Sheet1.html et ses liens

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

La capture d'écran suivante montre le code source HTML. Comme vous pouvez le voir, les liens référencent maintenant le répertoire C:\Temp\OtherSheets. Cela a été réalisé en utilisant l'interface [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **Code d'exemple**
Veuillez noter que le répertoire C:\Temp est uniquement à titre d'illustration. Vous pouvez utiliser n'importe quel répertoire de votre choix et y placer le [fichier Excel d'exemple](5115211.xlsx) puis exécuter le code fourni. Cela créera alors un sous-répertoire OtherSheets dans votre répertoire et exportera le HTML des deuxième et troisième feuilles de calcul à l’intérieur. Veuillez modifier la variable dirPath dans le code fourni pour la faire pointer vers le répertoire de votre choix avant l'exécution.

{{% alert color="primary" %}} 

Le code d'exemple ne fonctionnera que lorsque vous aurez défini la licence Aspose.Cells. Si vous essayez d'exécuter le code sans définir la licence, il entrera dans une boucle infinie. C'est pourquoi nous avons ajouté une vérification pour afficher un message et arrêter l'exécution si la licence n’est pas définie. Vous pouvez soit acheter une licence, soit demander une licence temporaire de 30 jours à l'équipe Aspose.Purchase.

{{% /alert %}} 

Notez que commenter ces lignes dans le code annulera les liens dans Sheet1.html, et Sheet2.html ou Sheet3.html ne s'ouvriront pas lorsque leurs liens seront cliqués dans Sheet1.html.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// Implementation of IFilePathProvider interface
class FilePathProvider extends AsposeCells.IFilePathProvider
{
// Constructor
constructor() 
{
super();
}

// Gets the full path of the file by worksheet name when exporting worksheet to html separately.
// So the references among the worksheets could be exported correctly.
getFullName(sheetName) 
{
if (sheetName === "Sheet2")
{
return "file:///" + path.join("OtherSheets", "Sheet2.html");
} 
else if (sheetName === "Sheet3") 
{
return "file:///" + path.join("OtherSheets", "Sheet3.html");
}

return "";
}
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// If you will comment this line, then hyperlinks will be broken
const options = new AsposeCells.HtmlSaveOptions();
options.setFilePathProvider(new FilePathProvider());
```

Voici le code complet que vous pouvez exécuter avec le [fichier Excel d'exemple](5115211.xlsx) fourni.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Implementation of IFilePathProvider interface
class FilePathProvider extends AsposeCells.IFilePathProvider
{
// Constructor
constructor() 
{
super();
}

// Gets the full path of the file by worksheet name when exporting worksheet to html separately.
// So the references among the worksheets could be exported correctly.
getFullName(sheetName) 
{
if (sheetName === "Sheet2")
{
return "file:///" + path.join("OtherSheets", "Sheet2.html");
} 
else if (sheetName === "Sheet3") 
{
return "file:///" + path.join("OtherSheets", "Sheet3.html");
}

return "";
}
}

// This is the directory path which contains the sample.xlsx file
const dirPath = path.join(__dirname, "data");

// because Aspose.Cells will always make the warning worksheet as active sheet in Evaluation mode.
//setLicense();

// Check if license is set, otherwise do not proceed
const wb = new AsposeCells.Workbook();
if (!wb.isLicensed()) {
console.log("You must set the license to execute this code successfully.");
} else {
// Test IFilePathProvider interface
testFilePathProvider();
}

function setLicense() {
const licPath = "Aspose.Cells.lic";

const lic = new AsposeCells.License();
lic.setLicense(licPath);

console.log(AsposeCells.CellsHelper.getVersion());
console.debug(AsposeCells.CellsHelper.getVersion());

process.chdir(dirPath);
}

function testFilePathProvider() {
// Create subdirectory for second and third worksheets
const otherSheetsDir = path.join(dirPath, "OtherSheets");
if (!fs.existsSync(otherSheetsDir)) {
fs.mkdirSync(otherSheetsDir);
}

// Load sample workbook from your directory
const wb = new AsposeCells.Workbook(path.join(dirPath, "Sample_filepath.xlsx"));

// Save worksheets to separate html files
// Because of IFilePathProvider, hyperlinks will not be broken.
for (let i = 0; i < wb.getWorksheets().getCount(); i++)
{
// Set the active worksheet to current value of variable i
wb.getWorksheets().setActiveSheetIndex(i);

// Create html save option
const options = new AsposeCells.HtmlSaveOptions();
options.setExportActiveWorksheetOnly(true);
// If you will comment this line, then hyperlinks will be broken
options.setFilePathProvider(new FilePathProvider());
// Sheet actual index which starts from 1 not from 0
const sheetIndex = i + 1;

let filePath = "";

// Save first sheet to same directory and second and third worksheets to subdirectory
if (i === 0) 
{
filePath = path.join(dirPath, "Sheet1.html");
} 
else 
{
filePath = path.join(otherSheetsDir, `Sheet${sheetIndex}_out.html`);
}

// Save the worksheet to html file
wb.save(filePath, options);
}
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
