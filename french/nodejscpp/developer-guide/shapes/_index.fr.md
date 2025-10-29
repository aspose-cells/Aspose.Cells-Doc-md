---  
title: Insérer des images et des formes dans les fichiers Excel avec Node.js via C++  
linktitle: Formes  
type: docs  
weight: 140  
url: /fr/nodejs-cpp/insert-shapes/  
description: Gérez les images, objets OLE et formes dans les fichiers Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Parfois, vous avez besoin d'insérer des formes nécessaires dans la feuille de calcul. Vous pouvez devoir insérer la même forme à différentes positions de la feuille. Ou vous devez insérer en batch des formes dans la feuille.  
Ne vous inquiétez pas! [Aspose.Cells](https://products.aspose.com/cells/) prend en charge toutes ces opérations.  
{{% /alert %}}  

Les formes dans Excel sont principalement divisées en types suivants :  
- **Images**  
- **Objets OLE**  
- **Lignes**  
- **Rectangles**  
- **Formes de base**  
- **Flèches de base**  
- **Formes d'équation**  
- **Organigrammes**  
- **Étoiles et bannières**  
- **Appels**  

Ce document guide sélectionnera une ou deux formes de chaque type pour faire des exemples. À travers ces exemples, vous apprendrez comment utiliser [Aspose.Cells](https://products.aspose.com/cells/) pour insérer la forme spécifiée dans la feuille.  

## **Ajout d'images dans la feuille Excel avec Node.js**  

Ajouter des images à une feuille de calcul est très facile. Il suffit de quelques lignes de code :  
Il suffit d'appeler la méthode [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) de la collection [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). La méthode [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) prend les paramètres suivants :  

- **Index de la ligne supérieure gauche**, l'index de la ligne supérieure gauche.  
- **Index de la colonne supérieure gauche**, l'index de la colonne supérieure gauche.  
- **Nom du fichier image**, le nom du fichier image, complet avec le chemin.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Insertion d'objets OLE dans une feuille Excel avec Node.js**  

Aspose.Cells prend en charge l'ajout, l'extraction et la manipulation d'objets OLE dans les feuilles de calcul. Pour cette raison, Aspose.Cells possède la classe [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection), utilisée pour ajouter un nouvel Objet OLE à la liste de collection. Une autre classe, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), représente un objet OLE. Elle possède quelques membres importants :  

- La propriété [**OleObject.getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) spécifie les données d'image (icône) de type tableau d'octets. L'image sera affichée pour montrer l'objet OLE dans la feuille de calcul.  
- La propriété [**OleObject.getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) spécifie les données de l'objet sous forme de tableau d'octets. Ces données seront affichées dans leur programme associé lors d'un double-clic sur l'icône de l'objet OLE.  

L'exemple suivant montre comment ajouter un ou des objets OLE dans une feuille de calcul.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const excelFilePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(excelFilePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Insertion d'une ligne dans une feuille Excel avec Node.js**  

La forme de la ligne appartient à la catégorie **lignes**.  

***Dans Microsoft Excel (par exemple 2007) :***  

- Sélectionnez la cellule où vous souhaitez insérer la ligne  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez la ligne dans 'Formes récemment utilisées' ou 'Lignes'  

![](line.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer une ligne dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
La méthode retourne un objet [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer une ligne dans une feuille de calcul.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line to the worksheet
sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// sheet.getShapes().addAutoShape(AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// sheet.getShapes().addShape(MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// Save. You can check your line in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](line2.png)  

## **Insertion d'une flèche de ligne dans une feuille Excel avec Node.js**  

La forme de la flèche de ligne appartient à la catégorie **Lignes**. C'est un cas particulier de ligne.  

***Dans Microsoft Excel (par exemple 2007) :***  

- Sélectionnez la cellule où vous souhaitez insérer la flèche de ligne  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez la flèche dans 'Formes récemment utilisées' ou 'Lignes'  

![](line_arrow1.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer une flèche de ligne dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
La méthode retourne un objet [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer une flèche de ligne dans une feuille de calcul.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line arrow to the worksheet
let s = sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// let s = sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// let s = sheet.getShapes().addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// add a arrow at the line begin
s.getLine().setBeginArrowheadStyle(AsposeCells.MsoArrowheadStyle.Arrow); // arrow type
s.getLine().setBeginArrowheadWidth(AsposeCells.MsoArrowheadWidth.Wide); // arrow width
s.getLine().setBeginArrowheadLength(AsposeCells.MsoArrowheadLength.Short); // arrow length

// add a arrow at the line end
s.getLine().setEndArrowheadStyle(AsposeCells.MsoArrowheadStyle.ArrowOpen); // arrow type
s.getLine().setEndArrowheadWidth(AsposeCells.MsoArrowheadWidth.Narrow); // arrow width
s.getLine().setEndArrowheadLength(AsposeCells.MsoArrowheadLength.Long); // arrow length

// Save. You can check your arrow in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](line_arrow2.png)  

## **Insertion d'un rectangle dans une feuille Excel en utilisant Node.js**  

La forme du rectangle appartient à la catégorie **Rectangles**.  

***Dans Microsoft Excel (par exemple 2007) :***  

- Sélectionnez la cellule où vous souhaitez insérer le rectangle  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez le rectangle dans 'Formes récemment utilisées' ou 'Rectangles'  

![](rectangle.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer un rectangle dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
La méthode retourne un objet [RectangleShape](https://reference.aspose.com/cells/nodejs-cpp/rectangleshape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer un rectangle dans une feuille de calcul.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the rectangle to the worksheet
sheet.getShapes().addRectangle(2, 0, 2, 0, 100, 300);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](rectangle2.png)  

## **Insertion d'un cube dans une feuille Excel en utilisant Node.js**  

La forme du cube appartient à la catégorie **Formes de base**.  

***Dans Microsoft Excel (par exemple 2007) :***  

- Sélectionnez la cellule où vous souhaitez insérer le cube  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez le Cube dans **Formes de base**  

![](cube.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer un cube dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
La méthode retourne un objet [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer un cube dans une feuille de calcul.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the cube to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

// Save. You can check your cube in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](cube2.png)  

## **Insertion d'une flèche de légende de type callout dans une feuille Excel en utilisant Node.js**  

La forme de la flèche de légende de type callout appartient à la catégorie **Flèches de bloc**.  

***Dans Microsoft Excel (par exemple 2007) :***  

- Sélectionnez la cellule où vous souhaitez insérer la flèche de callout quad  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez la flèche de légende de type callout dans **Flèches de bloc**  

![](callout_quad_arrow.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer une flèche de callout quad dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
La méthode retourne un objet [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer une flèche de légende de type callout dans une feuille de calcul.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the callout quad arrow to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

//Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](callout_quad_arrow2.png)  

## **Insertion d'un symbole de multiplication dans une feuille Excel en utilisant Node.js**  

La forme du symbole de multiplication appartient à la catégorie **Formes d'équation**.  

***Dans Microsoft Excel (par exemple 2007) :***  

- Sélectionnez la cellule où vous souhaitez insérer le signe de multiplication  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez le symbole de multiplication dans **Formes d'équation**  

![](multiplication_sign.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer un signe de multiplication dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
La méthode retourne un objet [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer un symbole de multiplication dans une feuille de calcul.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multiplication sign to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

// Save. You can check your multiplication in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](multiplication_sign2.png)  

## **Insertion d'un multidocument dans une feuille Excel en utilisant Node.js**  

La forme du multidocument appartient à la catégorie **Diagrammes de flux**.  

***Dans Microsoft Excel (par exemple 2007) :***  

- Sélectionnez la cellule où vous souhaitez insérer le multimédia  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez le multidocument dans **Diagrammes de flux**  

![](multidocument.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer un multimédia dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
La méthode retourne un objet [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer un multidocument dans une feuille de calcul.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multidocument to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](multidocument2.png)  

## **Insertion d'une étoile à cinq branches dans une feuille Excel en utilisant Node.js**  

La forme de l'étoile à cinq branches appartient à la catégorie **Étoiles et Bannières**.  

***Dans Microsoft Excel (par exemple 2007) :***  

- Sélectionnez la cellule où vous souhaitez insérer l'étoile à cinq branches  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez l'étoile à cinq branches dans **Étoiles et Bannières**  

![](star_5_points.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer une étoile à cinq branches dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
La méthode retourne un objet [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer une étoile à cinq branches dans une feuille de calcul.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the Five-pointed star to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

// Save. You can check your icon in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](star_5_points2.png)  

## **Insertion d'un nuage de bulle de pensée dans une feuille Excel en utilisant Node.js**  

La forme du nuage de bulle de pensée appartient à la catégorie **Callouts**.  

***Dans Microsoft Excel (par exemple 2007) :***  

- Sélectionnez la cellule où vous souhaitez insérer le nuage de bulles de pensée  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez le nuage de bulle de pensée dans **Callouts**  

![](thought_bubble_cloud.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer un nuage de bulles de pensée dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
La méthode retourne un objet [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer un nuage de bulle de pensée dans une feuille de calcul.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the thought bubble cloud to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](thought_bubble_cloud2.png)  

## **Sujets avancés**  
- [Modifier les valeurs d'ajustement de la forme](/cells/fr/nodejs-cpp/change-adjustment-values-of-the-shape/)  
- [Copier des formes entre les feuilles de calcul](/cells/fr/nodejs-cpp/copy-shapes-between-worksheets/)  
- [Données dans une forme non primitive](/cells/fr/nodejs-cpp/data-in-non-primitive-shape/)  
- [Trouver la position absolue de la forme dans la feuille de calcul](/cells/fr/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Obtenir les points de connexion de la forme](/cells/fr/nodejs-cpp/get-connection-points-from-shape/)  
- [Gestion des contrôles](/cells/fr/nodejs-cpp/managing-controls/)  
- [Ajouter des icônes à la feuille de calcul](/cells/fr/nodejs-cpp/insert-svg-to-excel/)  
- [Gestion des objets OLE](/cells/fr/nodejs-cpp/managing-ole-objects/)  
- [Gestion des images](/cells/fr/nodejs-cpp/managing-pictures/)  
- [Gérer les Smart Art](/cells/fr/nodejs-cpp/managing-smartart/)  
- [Gestion de la zone de texte](/cells/fr/nodejs-cpp/managing-textbox-of-excel/)  
- [Ajouter un filigrane WordArt à la feuille de calcul](/cells/fr/nodejs-cpp/add-wordart-watermark-to-worksheet/)  
- [Actualiser les valeurs des formes liées](/cells/fr/nodejs-cpp/refresh-values-of-linked-shapes/)  
- [Envoyer la forme à l'avant ou à l'arrière dans la feuille de calcul](/cells/fr/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Gérer les options de la forme](/cells/fr/nodejs-cpp/managing-shape-options/)  
- [Gérer les options de texte de la forme](/cells/fr/nodejs-cpp/managing-shape-text-options/)  
- [Extensions Web - Compléments Office](/cells/fr/nodejs-cpp/web-extensions-office-add-ins/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
