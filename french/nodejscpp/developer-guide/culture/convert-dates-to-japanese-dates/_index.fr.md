---  
title: Convertir des dates en dates japonaises avec Node.js via C++  
linktitle: Convertir les dates en dates japonaises  
type: docs  
weight: 350  
url: /fr/nodejs-cpp/convert-dates-to-japanese-dates/  
description: Apprenez à convertir les dates grégoriennes en dates japonaises à l aide de Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Dans le calendrier japonais, une nouvelle ère commence avec le règne d'un nouvel empereur. Le 1er mai 2019, un nouvel empereur est entré en fonction, mettant fin à l'ère Heisei et marquant le début de l'ère Reiwa.  

{{% /alert %}}  

Aspose.Cells offre un moyen de convertir les dates grégoriennes en dates japonaises. Lors de cette conversion, les changements d'ère sont également pris en compte. Le fragment de code suivant convertit le fichier [Excel source](90112015.xlsx) contenant des dates grégoriennes en [PDF de sortie](90112016.pdf) avec des dates japonaises comme indiqué dans l'image ci-dessous.  

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const options = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
options.setLanguageCode(AsposeCells.CountryCode.Japan);
options.setRegion(AsposeCells.CountryCode.Japan);

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "JapaneseDates.xlsx"), options);
workbook.save(outputDir + "JapaneseDates.pdf", AsposeCells.SaveFormat.Pdf);
```  

