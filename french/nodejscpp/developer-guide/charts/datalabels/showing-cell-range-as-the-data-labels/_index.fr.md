---  
title: Afficher la plage de cellules en tant qu étiquettes de données avec Node.js via C++  
linktitle: Afficher la plage de cellules en tant qu étiquettes de données  
description: Apprenez comment afficher une plage de cellules en tant qu étiquettes de données dans les graphiques en utilisant Aspose.Cells for Node.js via C++. Notre guide démontrera comment lier les étiquettes à votre source de données et les formater pour fournir des informations précises et significatives dans vos graphiques.  
keywords: Aspose.Cells for Node.js via C++, programmation de graphiques, étiquettes de données, plage de cellules, source de données, mise en forme, précision, informations significatives.  
type: docs  
weight: 130  
url: /fr/nodejs-cpp/showing-cell-range-as-the-data-labels/  
---  

{{% alert color="primary" %}}  
Dans Microsoft Excel 2013, vous pouvez afficher une plage de cellules pour les étiquettes de données. Aspose.Cells pour Node.js supporte cette fonctionnalité.  
{{% /alert %}}  

## **Case à cocher pour afficher la plage de cellules en tant qu'étiquettes de données**  

Pour afficher la plage de cellules en tant qu'étiquettes de données dans Microsoft Excel :  

1. Sélectionnez les étiquettes de données de la série et cliquez avec le bouton droit pour ouvrir le menu contextuel.  
1. Sélectionnez **Format des étiquettes de données**. Les options d'étiquetage sont affichées.  
1. Sélectionnez ou désélectionnez l'option **L'étiquette contient - Valeur à partir des cellules**.  

Le code d'exemple ci-dessous accède aux étiquettes de données d'une série de graphique et définit la propriété [**DataLabels.getShowCellRange()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getShowCellRange--) sur **true** pour sélectionner l'option **Label Contains - Value From Cells**.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source_show_range.xlsx");

// Create workbook from the source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Check the "Label Contains - Value From Cells"
const dataLabels = chart.getNSeries().get(0).getDataLabels();
dataLabels.setShowCellRange(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
