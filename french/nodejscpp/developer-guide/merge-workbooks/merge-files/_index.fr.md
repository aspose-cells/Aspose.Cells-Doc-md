---
title: Fusionner des fichiers avec Node.js via C++
linktitle: Fusionner des fichiers
type: docs
weight: 20
url: /fr/nodejs-cpp/merge-files/
---

## **Introduction**

Aspose.Cells offre plusieurs méthodes pour fusionner des fichiers. Pour des fichiers simples avec données, formatage, et formules, la méthode [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) peut être utilisée pour combiner plusieurs classeurs, et la méthode [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-) pour copier des feuilles de calcul dans un nouveau classeur. Ces méthodes sont faciles à utiliser et efficaces, mais si vous avez beaucoup de fichiers à fusionner, vous constaterez qu'elles consomment beaucoup de ressources système. Pour éviter cela, utilisez la méthode statique [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-), une façon plus efficace de fusionner plusieurs fichiers.

## **Fusionner des fichiers en utilisant Aspose.Cells for Node.js via C++**

Le code d'échantillon suivant illustre comment fusionner de grands fichiers en utilisant la méthode [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-). Il prend deux fichiers simples mais volumineux, Book1.xls et Book2.xls. Les fichiers contiennent uniquement des données formatées et des formules.

{{% alert color="primary" %}}

La méthode [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) prend uniquement en charge la fusion de données, de styles, de mises en forme et de formules. Des objets comme les graphiques, les images, les commentaires ou autres objets pourraient ne pas être fusionnés en utilisant cette méthode. De plus, un fichier mis en cache est utilisé pour stocker des données temporaires pour le processus.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an Array (length=2)
const files = new Array(2);
// Specify files with their paths to be merged
files[0] = path.join(dataDir, "book1.xls");
files[1] = path.join(dataDir, "Book2.xlsx");

// Create a cachedFile for the process
const cacheFile = path.join(dataDir, "test.txt");

// Output File to be created
const dest = path.join(dataDir, "output.xlsx");

// Merge the files in the output file. Supports only .xls files
AsposeCells.CellsHelper.mergeFiles(files, cacheFile, dest);
console.log(cacheFile);
// Now if you need to rename your sheets, you may load the output file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "output.xlsx"));

let i = 1;

// Browse all the sheets to rename them accordingly
const worksheets = workbook.getWorksheets();
for (let j = 0; j < worksheets.getCount(); j++) {
worksheets.get(j).setName(`Sheet1${i}`);
i++;
}

// Re-save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
