---  
title: Charger un classeur avec la taille de papier d’imprimante spécifiée via Node.js et C++  
linktitle: Charger le classeur avec la taille de papier de l imprimante spécifiée  
type: docs  
weight: 430  
url: /fr/nodejs-cpp/load-workbook-with-specified-printer-paper-size/  
description: Découvrez comment définir la taille du papier de l’imprimante lors du chargement d’un classeur avec Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Vous pouvez spécifier la taille de papier de l'imprimante de votre choix lors du chargement de votre classeur en utilisant la méthode [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-). Veuillez noter que si vous créez un nouveau fichier dans MS Excel, vous verrez que la taille de papier est la même que le réglage de l'imprimante par défaut sur votre machine.  
{{% /alert %}}  

Le code d’exemple suivant illustre l’utilisation de la méthode [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-). Il crée d’abord un classeur, puis le sauvegarde dans un flux mémoire au format XLSX. Ensuite, il le charge avec une taille de papier A5 et le sauvegarde au format PDF. Ensuite, il le recharge avec une taille de papier A3 et le sauvegarde à nouveau en PDF. Si vous ouvrez les PDFs de sortie et vérifiez leur taille de papier, vous remarquerez qu’elles sont différentes. L’un est en A5, l’autre en A3. Veuillez télécharger le [PDF de sortie A5](5115234.pdf) et le [PDF de sortie A3](5115233.pdf) générés par le code à titre de référence.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a sample workbook and add some data inside the first worksheet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("P30").putValue("This is sample data.");

// Save the workbook in memory stream
const ms = workbook.saveToStream();

// Now load the workbook from memory stream with A5 paper size
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA5);
let workbookA5 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA5.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a5_out.pdf"));

// Now load the workbook again from memory stream with A3 paper size
ms.position = 0;
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA3);
let workbookA3 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA3.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a3_out.pdf"));
```  

