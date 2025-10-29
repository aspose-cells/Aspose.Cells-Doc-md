---  
title: Spécifier le nom de la police Far East et Latin dans les options de texte de la forme avec Node.js via C++  
linktitle: Spécifier le nom Extrême Orient et Latin de la police dans les options de texte de la Forme  
type: docs  
weight: 1600  
url: /fr/nodejs-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/  
description: Apprenez à spécifier les noms des polices Far East et Latin dans les options de texte des formes en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Parfois, vous souhaitez afficher du texte en utilisant une police de langue Far East, par exemple Japonais, Chinois, Thaï, etc. Aspose.Cells for Node.js via C++ fournit la propriété [**TextOptions.getFarEastName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getFarEastName--) qui peut être utilisée pour spécifier le nom de la police de la langue Far East. De plus, vous pouvez également spécifier le nom de la police Latin en utilisant la propriété [**TextOptions.getLatinName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getLatinName--).  

## **Spécifier le nom Extrême-Orient et Latin de la police dans les options de texte de la Forme**  

Le code d'exemple suivant crée une zone de texte et y ajoute du texte japonais. Il spécifie ensuite les noms de polices Latin et Far East du texte, puis enregistre le classeur en tant que [fichier Excel de sortie](67338274.xlsx). La capture d'écran suivante montre les noms de police Latin et Far East de la zone de texte en sortie dans Microsoft Excel.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add textbox inside the worksheet.
const idx = ws.getTextBoxes().add(5, 5, 50, 200);
const tb = ws.getTextBoxes().get(idx);

// Set the text of the textbox.
tb.setText("こんにちは世界");

// Specify the Far East and Latin name of the font.
tb.getTextOptions().setLatinName("Comic Sans MS");
tb.getTextOptions().setFarEastName("KaiTi");

// Save the output Excel file.
wb.save("outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
