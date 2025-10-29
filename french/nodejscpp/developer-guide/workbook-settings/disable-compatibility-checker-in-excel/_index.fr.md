---  
title: Désactiver le Vérificateur de compatibilité dans Excel avec Node.js via C++  
linktitle: Désactiver le vérificateur de compatibilité dans Excel  
type: docs  
weight: 170  
url: /fr/nodejs-cpp/disable-compatibility-checker-in-excel/  
description: Apprenez comment désactiver le vérificateur de compatibilité via l’API Aspose.Cells for Node.js via C++.  
keywords: Node.js Désactiver le Vérificateur de compatibilité, Désactiver le Vérificateur de compatibilité dans Excel via Node.js en C++, Désactiver le Vérificateur de compatibilité dans le classeur.  
---  

## Désactiver le vérificateur de compatibilité dans les feuilles de calcul Excel avec Node.js  

{{% alert color="primary" %}}  
Le vérificateur de compatibilité de Microsoft Excel signale lorsque la sauvegarde d'un fichier dans un format de fichier antérieur pourrait entraîner des problèmes de fonctionnalité ou une perte de fidélité. Le vérificateur de compatibilité est une fonctionnalité de Microsoft Office Excel 2007 et de Microsoft Excel 2010.  

Lorsque vous enregistrez un classeur dans une version antérieure, Excel 97 à Excel 2003, à partir d'Excel 2007 ou d'Excel 2010, le vérificateur de compatibilité analyse le classeur pour voir s'il contient des fonctionnalités qui ne sont pas prises en charge par la version antérieure. Pour vous aider à prendre des décisions sur la manière de gérer les problèmes de compatibilité, le vérificateur de compatibilité affiche des boîtes de dialogue avec des options. Il peut également être utilisé pour créer un rapport sur les problèmes dans le classeur, ou désactiver la fonctionnalité.  

Parfois, vous avez besoin de désactiver le vérificateur de compatibilité pour une feuille de calcul particulière. Avec les API Aspose.Cells, vous pouvez le faire de manière programmatique afin que les utilisateurs ne soient pas frustrés ou confus par la boîte de dialogue du Vérificateur de compatibilité qui s'affiche lorsqu'ils sauvegardent manuellement le fichier dans Microsoft Excel.  
{{% /alert %}}  

## **Comment désactiver le vérificateur de compatibilité à l'aide de Microsoft Excel**  

Pour désactiver le vérificateur de compatibilité dans Microsoft Excel (par exemple Microsoft Excel 2007/2010) :  

- (Excel 2007) Sur le bouton Office, cliquez sur **Préparer**, puis sur **Exécuter le vérificateur de compatibilité**, puis désactivez l'option **Vérifier la compatibilité lors de l'enregistrement de ce classeur**.  
- (Excel 2010) Sur l'onglet **Fichier**, cliquez sur **Informations**, puis **Vérifier les problèmes**, cliquez sur **Vérifier la compatibilité**, et enfin, désélectionnez l'option **Vérifier la compatibilité lors de l'enregistrement de ce classeur**.  

## **Comment désactiver le vérificateur de compatibilité à l'aide des API Aspose.Cells**  

Définissez la propriété [**Workbook.getCheckCompatibility()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCheckCompatibility--) sur **false** pour désactiver le Vérificateur de compatibilité de Microsoft Excel.  

### **Exemples de code**  

Les exemples de code qui suivent montrent comment désactiver le Vérificateur de compatibilité avec Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Disable the compatibility checker
workbook.getSettings().setCheckCompatibility(false);

const outputFilePath = path.join(dataDir, "Output_BK_CompCheck.out.xlsx");
// Saving the Excel file
workbook.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
