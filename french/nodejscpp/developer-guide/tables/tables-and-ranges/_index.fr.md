---  
title: Tables et plages avec Node.js via C++  
linktitle: Tableaux et Plages  
type: docs  
weight: 50  
url: /fr/nodejs-cpp/tables-and-ranges/  
---  

## **Introduction**  

Parfois, vous créez un tableau dans Microsoft Excel et ne voulez pas continuer à travailler avec la fonctionnalité de tableau qu'il propose. À la place, vous voulez quelque chose qui ressemble à un tableau. Pour conserver les données dans un tableau sans perdre la mise en forme, convertissez le tableau en une plage de données ordinaire.  
Aspose.Cells prend en charge cette fonctionnalité de Microsoft Excel pour les tableaux et les objets liste.  

## **Utilisation de Microsoft Excel**  

Utilisez la fonctionnalité **Convertir en plage** pour convertir rapidement un tableau en une plage sans perdre le formatage. Dans Microsoft Excel 2007/2010 :  

1. Cliquez n'importe où dans le tableau pour vous assurer que la cellule active se trouve dans une colonne de tableau.  
1. Dans l'onglet **Création**, dans le groupe **Outils**, cliquez sur **Convertir en plage**.  

## **Utilisation d'Aspose.Cells**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");

// Open an existing file that contains a table/list object in it
const wb = new AsposeCells.Workbook(filePath);

// Convert the first table/list object (from the first worksheet) to normal range
wb.getWorksheets().get(0).getListObjects().get(0).convertToRange();

// Save the file
wb.save(path.join(dataDir, "output.xlsx"));
```  

{{% alert color="primary" %}}  

Les fonctionnalités du tableau ne sont plus disponibles après sa conversion en plage. Par exemple, les en-têtes de ligne n'incluent plus les flèches de tri et de filtre, et les références structurées (références utilisant des noms de table) utilisées dans les formules se transforment en références de cellule classiques.  

{{% /alert %}}  

## **Convertir un tableau en plage avec des options**  

Aspose.Cells propose des options supplémentaires lors de la conversion d'une table en plage via la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/). La classe [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) fournit la propriété [**getLastRow()**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/#getLastRow--) qui vous permet de définir le dernier index de la ligne de table. La mise en forme du tableau sera conservée jusqu'à l'index de ligne spécifié et le reste de la mise en forme sera supprimé.  

Le code d'exemple ci-dessous démontre l'utilisation de la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");
// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.TableToRangeOptions();
options.setLastRow(5);

// Convert the first table/list object (from the first worksheet) to normal range
workbook.getWorksheets().get(0).getListObjects().get(0).convertToRange(options);

// Save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
