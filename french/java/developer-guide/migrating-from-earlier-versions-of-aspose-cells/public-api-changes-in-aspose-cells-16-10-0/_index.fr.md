---
title: Public API Changements dans Aspose.Cells 16.10.0
type: docs
weight: 350
url: /fr/java/public-api-changes-in-aspose-cells-16-10-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 9.0.0 à 16.10.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge des effets de réflexion**
Aspose.Cells 16.10.0 a exposé la classe ReflectionEffect avec la propriété Shape.Reflection afin de contrôler les effets de réflexion d'un objet Shape. La classe ReflectionEffect a les propriétés suivantes.

- ReflectionEffect.Blur : obtient/définit le rayon de flou en unités de points.
- ReflectionEffect.Direction : obtient/définit la direction de la rampe de dégradé alpha par rapport à la forme elle-même.
- ReflectionEffect.Distance : obtient/définit la distance de la réflexion en unités de points.
- ReflectionEffect.FadeDirection : Obtient/définit la direction pour décaler la réflexion.
- ReflectionEffect.RotWithShape : Obtient/définit si la réflexion doit tourner avec la forme.
- ReflectionEffect.Size : Obtient/définit la position finale (le long de la rampe de dégradé alpha) de la valeur alpha finale en unité de pourcentage .
- ReflectionEffect.Transparency : obtient/définit le degré de transparence de la réflexion de départ sous la forme d'une valeur comprise entre 0,0 (opaque) et 1,0 (clair).
- ReflectionEffect.Type : obtient/définit l'effet de réflexion prédéfini.

Voici un scénario d'utilisation simple de la propriété Shape.Reflection.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Travailler avec des effets de réflexion](/cells/fr/java/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ReflectionEffect from the Shape object

ReflectionEffect reflection = shape.getReflection();

//Set its Blur, Size, Transparency and Distance properties

reflection.setBlur(30);

reflection.setSize(90);

reflection.setTransparency(0.5);

reflection.setDistance(80);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Prise en charge des effets d'ombre**
Aspose.Cells 16.10.0 a exposé la propriété Shape.ShadowEffect avec la classe ShadowEffect qui, ensemble, permet de définir l'effet d'ombre sur un objet Shape. La classe ShadowEffect a les propriétés suivantes.

- ShadowEffect.Angle : Obtient/définit l'angle d'éclairage allant de 0 à 359,9 degrés.
- ShadowEffect.Blur : Obtient et définit le flou de l'ombre allant de 0 à 100 points.
- ShadowEffect.Color : obtient/définit la couleur de l'ombre.
- ShadowEffect.Distance : Obtient/définit la distance de l'ombre allant de 0 à 200 points.
- ShadowEffect.PresetType : obtient/définit le type d'ombre prédéfini de l'ombre.
- ShadowEffect.Size : Obtient/définit la taille de l'ombre allant de 0 à 2,0. Cela n'aura aucun sens en cas d'ombre intérieure.
- ShadowEffect.Transparency : obtient/définit le degré de transparence de l'ombre allant de 0,0 (opaque) à 1,0 (clair).

Voici un scénario d'utilisation simple de la propriété susmentionnée.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Travailler avec des effets d'ombre](/cells/fr/java/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ShadowEffect from the Shape object

ShadowEffect shadow = shape.getShadowEffect();

//Set its Angle, Blur, Size, Transparency and Distance properties

shadow.setAngle(150);

shadow.setBlur(30);

shadow.setSize(90);

shadow.setTransparency(0.5);

shadow.setDistance(80);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Prise en charge des effets lumineux**
Aspose.Cells 16.10.0 a exposé la propriété Shape.Glow avec la classe GlowEffect qui, ensemble, permet de définir l'effet de lueur d'un objet Shape. La classe GlowEffect spécifie un effet de lueur, dans lequel un contour flou de couleur est ajouté à l'extérieur des bords de l'objet à l'aide des propriétés suivantes.

- GlowEffect.Size : Obtient/définit le rayon de la lueur en unités de points.
- GlowEffect.Transparency : obtient/définit le degré de transparence de l'effet de lueur allant de 0,0 (opaque) à 1,0 (clair).

Voici un scénario d'utilisation simple de la propriété Shape.Glow.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Travailler avec l'effet lumineux](/cells/fr/java/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of GlowEffect from the Shape object

GlowEffect glow = shape.getGlow();

//Set its Size & Transparency properties

glow.setSize(90);

glow.setTransparency(0.5);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Prise en charge du format 3D**
Aspose.Cells 16.10.0 a exposé la propriété Shape.ThreeDFormat avec la classe ThreeDFormat qui, ensemble, peuvent être utilisées pour contrôler la mise en forme 3D de l'objet Shape. La classe ThreeDFormat représente la mise en forme tridimensionnelle d'une forme et possède les propriétés suivantes.

- ThreeDFormat.BottomBevelHeight : obtient/définit la hauteur du biseau inférieur ou la distance à laquelle il est appliqué dans la forme, en unités de points.
- ThreeDFormat.BottomBevelType : obtient/définit le type de biseau inférieur ou la distance à laquelle il est appliqué dans la forme, en unités de points.
- ThreeDFormat.BottomBevelWidth : obtient/définit la largeur du biseau inférieur ou la distance à laquelle il est appliqué dans la forme, en unités de points.
- ThreeDFormat.ContourColor : obtient/définit la couleur de contour d'une forme.
- ThreeDFormat.ContourWidth : obtient/définit la largeur du contour de la forme, en unités de points.
- ThreeDFormat.ExtrusionColor : Obtient la couleur d'extrusion sur une forme.
- ThreeDFormat.ExtrusionHeight : Obtient/définit la hauteur d'extrusion appliquée à la forme, en unités de points.
- ThreeDFormat.LightAngle : Obtient/définit l'angle des lumières d'extrusion.
- ThreeDFormat.Lighting : Obtient/définit le type d'éclairage.
- ThreeDFormat.LightingDirection : Obtient/définit la direction à partir de laquelle le système d'éclairage est orienté par rapport à la scène.
- ThreeDFormat.Material : Représente le matériau prédéfini qui est combiné avec les propriétés d'éclairage pour donner l'aspect final d'une forme.
- ThreeDFormat.Perspective : Obtient/définit l'angle auquel un objet ThreeDFormat peut être visualisé.
- ThreeDFormat.PresetCameraType : Obtient/définit la caméra prédéfinie d'extrusion.
- ThreeDFormat.RotationX : obtient/définit la rotation de la forme extrudée autour de l'axe X en degrés.
- ThreeDFormat.RotationY : obtient/définit la rotation de la forme extrudée autour de l'axe Y en degrés.
- ThreeDFormat.RotationZ : obtient/définit la rotation de la forme extrudée autour de l'axe Z en degrés.
- ThreeDFormat.TopBevelHeight : obtient/définit la hauteur du biseau supérieur ou la distance à laquelle il est appliqué dans la forme, en unités de points.
- ThreeDFormat.TopBevelType : obtient/définit le type de biseau supérieur ou la distance à laquelle il est appliqué dans la forme, en unités de points.
- ThreeDFormat.TopBevelWidth : obtient/définit la largeur du biseau supérieur ou la distance à laquelle il est appliqué dans la forme, en unités de points.
- ThreeDFormat.Z : Définit la distance du sol pour la forme 3D.

Voici le scénario d'utilisation simple de la propriété Shape.ThreeDFormat.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Travailler avec le formatage 3D](/cells/fr/java/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ThreeDFormat from the Shape object

ThreeDFormat threeD = shape.getThreeDFormat();

//Set its ContourWidth & ExtrusionHeight properties

threeD.setContourWidth(15);

threeD.setExtrusionHeight(30);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Prise en charge des styles WordArt dans le texte de Shape**
Aspose.Cells 16.10.0 a exposé les méthodes FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle afin de définir le style WordArt prédéfini sur le texte de l'objet Shape.

Voici un scénario d'utilisation simple des méthodes susmentionnées.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Travailler avec des styles WordArt](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Create a TextBox with some text

int index = sheet.getTextBoxes().add(0, 0, 100, 700);

TextBox textBox = (TextBox)sheet.getShapes().get(index);

textBox.setText("Aspose File Format APIs");

textBox.getFont().setSize(44);

//Set preset WordArt style to the text of the shape

FontSetting fntSetting = (FontSetting)textBox.getCharacters().get(0);

fntSetting.setWordArtStyle(PresetWordArtStyle.WORD_ART_STYLE_15);

{{< /highlight >}}
### **Prise en charge des styles intégrés WordArt**
Aspose.Cells 16.10.0 a exposé la méthode ShapeCollection.AddWordArt avec l'énumération PresetWordArtStyle afin de fournir la prise en charge de l'ajout d'objets WordArt prédéfinis depuis Excel 2007.

Voici un scénario d'utilisation simple de la méthode ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Ajouter WordArt avec des styles intégrés](/cells/fr/java/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access ShapeCollection of first worksheet

ShapeCollection shapes = sheet.getShapes();

//Add WordArt with built-in styles

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_1, "Aspose File Format APIs", 00, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Méthode XmlMapCollection.Add ajoutée**
Aspose.Cells a exposé la méthode XmlMapCollection.Add qui permet d'ajouter Xml Map à une feuille de calcul. Voici un scénario d'utilisation simple de la méthode XmlMapCollection.Add.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Ajouter une carte XML à la feuille de calcul](/cells/fr/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Ajout de la méthode Cells.LinkToXmlMap**
Aspose.Cells a maintenant exposé la méthode Cells.LinkToXmlMap afin de lier les cellules aux éléments de carte XML. Voici un scénario d'utilisation simple de la méthode Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Lien Cells vers les éléments de carte XML](/cells/fr/java/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook("sample.xlsx");

//Access the XML Map from the spreadsheet

XmlMap map = book.getWorksheets().getXmlMaps().get(0);

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Map FIELD1 and FIELD2 to cell A1 and B2

sheet.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");

sheet.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

//Map FIELD4 and FIELD5 to cell C3 and D4

sheet.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");

sheet.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

//Map FIELD7 and FIELD8 to cell E5 and F6

sheet.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");

sheet.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

{{< /highlight >}}
### **Ajout de la propriété ListColumn.Formula**
Aspose.Cells 16.10.0 a exposé la propriété ListColumn.Formula afin de propager automatiquement la formule aux lignes nouvellement insérées.

Voici un scénario d'utilisation simple de la propriété ListColumn.Formula.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Propager automatiquement la formule dans l'objet de liste](/cells/fr/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add column headings in cell A1 and B1

sheet.getCells().get(0, 0).putValue("Column A");

sheet.getCells().get(0, 1).putValue("Column B");

//Add list object, set its name and style

ListObject listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));

listObject.setTableStyleType(TableStyleType.TABLE_STYLE_MEDIUM_14);

listObject.setDisplayName("Table");

//Set the formula of second column so that it could automatically propagate to new rows while entering data

listObject.getListColumns().get(1).setFormula("=[Column A]+ 1");

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
