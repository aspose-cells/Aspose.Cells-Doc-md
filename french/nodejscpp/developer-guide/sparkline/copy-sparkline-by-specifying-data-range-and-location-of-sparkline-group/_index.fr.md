---  
title: Copier une miniature en spécifiant la plage de données et l emplacement du groupe de miniatures avec Node.js via C++  
linktitle: Copier le mini graphique en spécifiant la plage de données et l emplacement du groupe de mini graphiques  
type: docs  
weight: 300  
url: /fr/nodejs-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/  
description: Apprenez comment copier une miniature dans Excel en spécifiant la plage de données et l emplacement du groupe de miniatures en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Microsoft Excel vous permet de copier une sparkline en spécifiant la plage de données et l'emplacement d'un groupe de sparkline. Aspose.Cells prend en charge cette fonctionnalité.  
{{% /alert %}}  

Pour copier une sparkline vers d'autres cellules dans Microsoft Excel:  

1. Sélectionnez la cellule contenant la sparkline.  
1. Sélectionnez **Modifier les données** dans la section **Sparkline** de l'onglet **Conception**.  
1. Sélectionnez **Modifier l'emplacement du groupe et les données**.  
1. Spécifiez la plage de données et l'emplacement.  
1. Cliquez sur **OK**.  

Aspose.Cells fournit la méthode `SparklineCollection.add(dataRange, row, column)` pour spécifier la plage de données et l'emplacement d'un groupe de miniatures. Le code d'exemple suivant charge le fichier Excel source comme montré dans la capture d'écran ci-dessus, puis accède au premier groupe de miniatures et ajoute des plages de données et des emplacements dans le groupe de miniatures. Enfin, il écrit le fichier Excel de sortie sur le disque, qui est également montré dans la capture d'écran.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "copy_sparkline.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first sparkline group
const group = worksheet.getSparklineGroups().get(0);

// Add Data Ranges and Locations inside this sparkline group
group.getSparklines().add("Sheet1!D5:O5", 4, 15);
group.getSparklines().add("Sheet1!D6:O6", 5, 15);
group.getSparklines().add("Sheet1!D7:O7", 6, 15);
group.getSparklines().add("Sheet1!D8:O8", 7, 15);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

