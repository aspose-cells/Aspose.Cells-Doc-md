---  
title: Exporter la mise en forme conditionnelle DataBar, ColorScale et IconSet lors de la conversion Excel en HTML avec Node.js via C++  
linktitle: Exporter les formatages conditionnels DataBar, ColorScale et IconSet lors de la conversion d Excel en HTML  
type: docs  
weight: 30  
url: /fr/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/  
---  

{{% alert color="primary" %}} 

Vous pouvez exporter la mise en forme conditionnelle DataBar, ColorScale et IconSet lors de la conversion de votre fichier Excel en HTML. Cette fonctionnalité est partiellement supportée par Microsoft Excel mais Aspose.Cells for Node.js via C++ la supporte entièrement.

{{% /alert %}}  

## **Exporter les formatages conditionnels DataBar, ColorScale et IconSet lors de la conversion d'Excel en HTML**  
La capture d'écran suivante montre le [fichier Excel d'exemple](5115558.xlsx) avec des formatages conditionnels DataBar, ColorScale et IconSet. Vous pouvez télécharger le [fichier Excel d'exemple](5115558.xlsx) à partir du lien donné.  

![todo:image_alt_text](conversion_1.png)  

La capture d'écran suivante montre le fichier HTML de sortie Aspose.Cells montrant les formatages conditionnels DataBar, ColorScale et IconSet. Comme vous pouvez le voir, il ressemble exactement au [fichier Excel d'exemple](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **Code d'exemple**  
Le code d'exemple suivant convertit un fichier Excel d'exemple en HTML qui est simplement une conversion [Excel en HTML](/cells/fr/nodejs-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
