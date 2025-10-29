---  
title: Définir la police par défaut lors du rendu d une feuille de calcul en HTML avec Node.js via C++  
linktitle: Définir la police par défaut lors du rendu de la feuille de calcul en HTML  
type: docs  
weight: 370  
url: /fr/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/  
---  

{{% alert color="primary" %}}  
Aspose.Cells vous permet de définir la police par défaut lors du rendu de la feuille de calcul en HTML. Veuillez utiliser [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) à cette fin. Cette propriété est utile lorsqu'il y a des cellules dans une feuille de calcul qui ont des polices invalides ou inexistantes. Alors, ces cellules seront rendues dans une police spécifiée avec la propriété [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--).  
{{% /alert %}}  

## Définir la police par défaut lors du rendu de la feuille de calcul en HTML  

Le code d'exemple suivant crée un classeur et ajoute un texte dans la cellule B4 de la première feuille de calcul et défini sa police sur une police inconnue/inexistante. Ensuite, il sauvegarde le classeur en HTML en définissant différents noms de police par défaut tels que Courier New, Arial, Times New Roman, etc.  

 La capture d'écran montre l'effet de la définition de différents noms de police par défaut via la propriété [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--).  

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)  

Le code génère le [fichier HTML de sortie avec Courier New](5115516), le [fichier HTML de sortie avec Arial](5115518), et le [fichier HTML de sortie avec Times New Roman](5115517).  

## Code d'exemple  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object and access first worksheet.
const wb = new AsposeCells.Workbook();
const ws = wb.getWorksheets().get(0);

// Access cell B4 and add some text inside it.
const cell = ws.getCells().get("B4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell B4 which is unknown.
const st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
cell.setStyle(st);

// Now save the workbook in html format and set the default font to Courier New.
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDefaultFontName("Courier New");
wb.save(path.join(dataDir, "out_courier_new_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Arial.
opts.setDefaultFontName("Arial");
wb.save(path.join(dataDir, "out_arial_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Times New Roman.
opts.setDefaultFontName("Times New Roman");
wb.save(path.join(dataDir, "times_new_roman_out.htm"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
