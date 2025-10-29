---  
title: Accéder à une table depuis une cellule et ajouter des valeurs à l intérieur en utilisant des décalages de lignes et de colonnes avec Node.js via C++  
linktitle: Accéder à un tableau depuis une cellule et ajouter des valeurs à l intérieur en utilisant des décalages de ligne et de colonne  
type: docs  
weight: 230  
url: /fr/nodejs-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
---  

{{% alert color="primary" %}}  

Normalement, vous ajoutez des valeurs à l'intérieur de l'objet Table ou Liste en utilisant la méthode [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-). Mais parfois, vous pourriez avoir besoin d'ajouter des valeurs à l'intérieur de l'objet Table ou Liste en utilisant les décalages de ligne et de colonne.  

Pour accéder à une table ou à un objet liste à partir d'une cellule, utilisez la méthode [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--). Pour ajouter des valeurs à l'intérieur en utilisant les décalages de ligne et de colonne, utilisez la méthode [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-).  

{{% /alert %}}  

La capture d'écran suivante montre le fichier Excel source utilisé dans le code. Il contient la table vide et met en évidence la cellule D5 qui se trouve dans la table. Nous accéderons à cette table à partir de la cellule D5 en utilisant la méthode [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--), puis ajouterons des valeurs à l'intérieur en utilisant les méthodes [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) et [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-).  

## Exemple  

### Captures d'écran comparant les fichiers source et de sortie  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

La capture d'écran suivante montre le fichier Excel de sortie généré par le code. Comme vous pouvez le voir, la cellule D5 a une valeur et la cellule F6, qui est située à l'emplacement 2,2 du tableau, a une valeur.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### Code Node.js pour accéder à une table depuis une cellule et y ajouter des valeurs en utilisant des décalages de ligne et de colonne  

Le code d'exemple suivant charge le fichier Excel source tel que montré dans la capture d'écran ci-dessus et ajoute des valeurs à l'intérieur du tableau, puis génère le fichier Excel de sortie tel qu'indiqué ci-dessus.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Accessing_Table.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell D5 which lies inside the table
const cell = worksheet.getCells().get("D5");

// Put value inside the cell D5
cell.putValue("D5 Data");

// Access the Table from this cell
const table = cell.getTable();

// Add some value using Row and Column Offset
table.putCellValue(2, 2, "Offset [2,2]");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
