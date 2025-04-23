---  
title: Convertir une révision de XLSB en XLSM avec Node.js via C++  
linktitle: Convertir la révision des XLSB en XLSM  
type: docs  
weight: 290  
url: /fr/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/  
description: Apprenez comment convertir complètement les révisions de fichiers XLSB en format XLSM en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells prend désormais en charge la conversion complète des révisions de fichiers XLSB en fichiers XLSM. Les révisions se trouvent dans le chemin \xl\revisions. Vous pouvez les voir en changeant l'extension de votre fichier XLSB en ZIP. Le chemin \xl\revisions contient des fichiers se terminant par l’extension .bin.  

Lorsque vous convertissez votre fichier XLSB en fichier XLSM avec Aspose.Cells, ces fichiers .bin se convertissent avec succès en fichiers .xml comme montré dans ces deux captures d'écran.  

{{% /alert %}}  

L'exemple de code suivant vous montre comment convertir le fichier XLSB au format XLSM en utilisant Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsb");

// Open workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save Workbook to XLSM format
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```  

