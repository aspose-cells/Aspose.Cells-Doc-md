---  
title: Afficher et masquer les lignes de grille et les en têtes de lignes et colonnes avec Node.js via C++  
linktitle: Afficher et masquer les quadrillages et les en têtes de ligne et de colonne  
type: docs  
weight: 30  
url: /fr/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/  
description: Cet article fournit un exemple de code pour utiliser l API Node.js via C++ afin de masquer ou afficher programmatique les lignes de grille, ainsi que les en têtes de lignes et de colonnes d une feuille Excel.  
---  

{{% alert color="primary" %}}  
Aspose.Cells prend en charge le masquage et l'affichage des quadrillages de la feuille de calcul qui sont visibles par défaut. Il permet également de contrôler la visibilité des en-têtes de lignes et de colonnes de la feuille de calcul.  
{{% /alert %}}  

## **Afficher et masquer les quadrillages**  

Toutes les feuilles de calcul Excel ont des quadrillages par défaut. Ils facilitent la délimitation des cellules afin de faciliter la saisie de données dans des cellules particulières. Les quadrillages nous permettent de visualiser une feuille de calcul comme une collection de cellules, où chaque cellule est facilement identifiable.  

### **Contrôler la visibilité des quadrillages**  

Aspose.Cells propose une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet aux développeurs d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre un large éventail de propriétés et méthodes pour gérer une feuille. Pour contrôler la visibilité des lignes de grille, utilisez la propriété [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--). [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) est une propriété boolean, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.  

#### **Rendre les quadrillages visibles**  

Rendez les lignes de grille visibles en définissant la propriété [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) sur **true**.  

#### **Masquer les quadrillages**  

Masquer les lignes de grille en définissant la propriété [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) sur **false**.  

Un exemple complet est donné ci-dessous, illustrant l'utilisation de la propriété [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) en ouvrant un fichier Excel (book1.xls), en masquant les lignes de grille sur la première feuille, puis en enregistrant le fichier modifié sous le nom output.xls.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileData = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file data
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the grid lines of the first worksheet of the Excel file
worksheet.setIsGridlinesVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Afficher et masquer les entêtes de ligne des colonnes**  

Toutes les feuilles de calcul d'un fichier Excel sont composées de cellules disposées en lignes et en colonnes. Toutes les lignes et colonnes ont des valeurs uniques qui sont utilisées pour les identifier et pour identifier les cellules individuelles. Par exemple, les lignes sont numérotées – 1, 2, 3, 4, etc. – et les colonnes sont ordonnées alphabétiquement – A, B, C, D, etc. Les valeurs de ligne et de colonne sont affichées dans les entêtes. En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité de ces entêtes de ligne et de colonne.  

### **Contrôler la visibilité des feuilles de calcul**  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) permettant aux développeurs d'accéder à chaque feuille du fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre de nombreuses propriétés et méthodes pour gérer une feuille. Pour contrôler la visibilité des en-têtes de lignes et de colonnes, utilisez la propriété [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--). [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.  

#### **Rendre les entêtes de ligne/colonne visibles**  

Rendez visibles les en-têtes des lignes et des colonnes en définissant la propriété [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) à **true**.  

#### **Masquer les entêtes de ligne/colonne**  

Masquez les en-têtes des lignes et des colonnes en définissant la propriété [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) à **false**.  

Un exemple complet est donné ci-dessous illustrant comment utiliser la propriété [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) en ouvrant un fichier Excel (book1.xls), en masquant les en-têtes des lignes et des colonnes sur la première feuille de calcul, puis en enregistrant le fichier modifié sous le nom output.xls.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file path
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the headers of rows and columns
worksheet.setIsRowColumnHeadersVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Il est également possible d'utiliser les méthodes [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) et [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) de la classe [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) pour rendre visibles plusieurs lignes et colonnes.  
{{% /alert %}}  

