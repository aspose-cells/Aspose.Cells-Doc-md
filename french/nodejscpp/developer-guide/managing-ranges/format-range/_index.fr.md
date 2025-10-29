---  
title: Formatage des plages avec Node.js via C++  
linktitle: Formater les plages  
type: docs  
weight: 105  
url: /fr/nodejs-cpp/how-to-format-a-range/  
description: Apprenez comment formater une plage de cellules dans Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  
Lorsque vous devez appliquer un style à une plage, vous pouvez utiliser le formatage des plages.  

## **Comment formater une plage dans Excel**  

Pour formater une plage de cellules dans Excel, vous pouvez utiliser les options de formatage intégrées fournies par Excel. Voici comment vous pouvez formater une plage de cellules directement dans Excel:  

1. Ouvrez Excel et ouvrez le classeur qui contient la plage que vous souhaitez formater.  

2. Sélectionnez la plage de cellules que vous souhaitez formater. Vous pouvez cliquer et faire glisser pour sélectionner la plage, ou vous pouvez utiliser des raccourcis clavier comme Maj + touches de direction pour étendre la sélection.  

3. Une fois la plage sélectionnée, faites un clic droit sur la plage sélectionnée et choisissez "Format de cellule" dans le menu contextuel. Alternativement, vous pouvez aller dans l'onglet Accueil dans le ruban Excel, cliquer sur la liste déroulante "Format" dans le groupe "Cellules", et sélectionner "Format de cellule".  

4. La boîte de dialogue "Format de cellule" apparaîtra. Ici, vous pouvez choisir différentes options de formatage à appliquer à la plage sélectionnée. Par exemple, vous pouvez changer le style de police, la taille de police, la couleur de police, le format de nombre, les bordures, la couleur de fond, etc. Explorez les différents onglets de la boîte de dialogue pour accéder à diverses options de formatage.  

5. Après avoir apporté les modifications de formatage souhaitées, cliquez sur le bouton "OK" pour appliquer le formatage à la plage sélectionnée.  

## **Comment formater une plage en utilisant Node.js**  

Pour formater une plage en utilisant Aspose.Cells for Node.js via C++, vous pouvez utiliser les méthodes suivantes :  
1. [Range.applyStyle(style, flag)](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  
3. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  

## **Code d'exemple**  
Dans cet exemple, nous créons un classeur Excel, ajoutons des données d'exemple, accédons à la première feuille de calcul, et définissons deux plages("A1:C3" et "A4:C5"). Ensuite, nous créons de nouveaux styles, définissons diverses options de formatage (par exemple, couleur de police, gras), et appliquons le style à la plage. Enfin, nous enregistrons le classeur dans un nouveau fichier.  
<br>  
![todo:image_alt_text](format-range.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = workbook.getWorksheets().get(0);

const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Access the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Define the range
const range = worksheet.getCells().createRange("A1:C3");

// Apply formatting to the range
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Red);
style.getFont().setIsBold(true);

const flag = new AsposeCells.StyleFlag();
flag.setFont(true);
range.applyStyle(style, flag);

// Define the range
const range2 = worksheet.getCells().createRange("A4:C5");

// Apply formatting to the range
const style2 = workbook.createStyle();
style2.getFont().setColor(AsposeCells.Color.Blue);
style2.getFont().setIsItalic(true);
range2.setStyle(style2);

// Save the modified workbook
workbook.save("output.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
