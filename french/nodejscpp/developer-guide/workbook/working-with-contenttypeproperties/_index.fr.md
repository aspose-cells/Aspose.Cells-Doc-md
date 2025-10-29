---  
title: Travailler avec ContentTypeProperties avec Node.js via C++  
linktitle: Travailler avec ContentTypeProperties  
type: docs  
weight: 150  
url: /fr/nodejs-cpp/working-with-contenttypeproperties/  
description: Apprenez comment travailler avec des ContentTypeProperties personnalisés dans les fichiers Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells fournit la méthode [**Workbook.getContentTypeProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getContentTypeProperties--) pour ajouter des ContentTypeProperties personnalisés à un fichier Excel. Vous pouvez également rendre la propriété facultative en définissant la propriété [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/nodejs-cpp/contenttypeproperty/#isNillable--) à **true**. Le code suivant montre comment ajouter des ContentTypeProperties personnalisés optionnels à un fichier Excel. L’image suivante montre les deux propriétés ajoutées par le code.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Le fichier de sortie généré par le code d'exemple est joint pour référence.

[Fichier de sortie](95584314.xlsx)

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

//source directory
const outputDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);
let index = workbook.getContentTypeProperties().add("MK31", "Simple Data");
workbook.getContentTypeProperties().get(index).setIsNillable(false);
index = workbook.getContentTypeProperties().add("MK32", new Date().toISOString(), "DateTime");
workbook.getContentTypeProperties().get(index).setIsNillable(true);
workbook.save(path.join(outputDir, "WorkingWithContentTypeProperties_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
