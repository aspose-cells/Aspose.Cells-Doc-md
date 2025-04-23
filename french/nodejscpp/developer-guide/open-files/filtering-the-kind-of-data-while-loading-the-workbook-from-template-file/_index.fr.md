---  
title: Filtrage du type de données lors du chargement du classeur à partir d’un fichier de modèle avec Node.js via C++  
linktitle: Filtrer le type de données lors du chargement du classeur à partir du fichier de modèle  
type: docs  
weight: 400  
url: /fr/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/  
---  

{{% alert color="primary" %}}  
Parfois, vous souhaitez spécifier quel type de données doit être chargé lors de la création du classeur à partir du fichier de modèle. Le filtrage des données chargées peut améliorer les performances pour votre usage particulier, surtout lorsque vous utilisez les [LightCells API](/cells/fr/nodejs-cpp/using-lightcells-api/). Veuillez utiliser la propriété [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) à cette fin.  
{{% /alert %}}  

Le code d’exemple suivant charge uniquement des objets de forme lors du chargement du classeur à partir du [fichier de modèle](5115552.xlsx) que vous pouvez télécharger à partir du lien donné. La capture d’écran montre le contenu du [fichier de modèle](5115552.xlsx) et explique également que les données en rouge sur fond jaune ne seront pas chargées car la propriété [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) a été définie sur [**Shape**](https://reference.aspose.com/cells/nodejs-cpp/shape/).  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)  

La capture d'écran suivante montre le [PDF de sortie](5115555.pdf) que vous pouvez télécharger à partir du lien donné. Ici, vous pouvez voir que les données en couleur rouge et arrière-plan jaune ne sont pas présentes mais que toutes les formes sont là.  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Set the load options, we only want to load shapes and do not want to load data
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);            

loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Create workbook object from sample excel file using load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleFilterChars.xlsx"), loadOptions);

// Save the output in pdf format
workbook.save(outputDir + "sampleFilterChars_out.pdf", AsposeCells.SaveFormat.Pdf);
```  

