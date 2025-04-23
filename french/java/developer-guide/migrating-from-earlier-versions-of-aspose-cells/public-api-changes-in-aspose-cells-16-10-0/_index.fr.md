---
title: Changements de l API publique dans Aspose.Cells 16.10.0
type: docs
weight: 350
url: /fr/java/public-api-changes-in-aspose-cells-16-10-0/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 9.0.0 à 16.10.0 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, etc., mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Prise en charge des effets de réflexion**
Aspose.Cells 16.10.0 a exposé la classe ReflectionEffect ainsi que la propriété Shape.Reflection afin de contrôler les effets de réflexion d'un objet Shape. La classe ReflectionEffect a les propriétés suivantes.

- ReflectionEffect.Blur : Obtient/définit le rayon de flou en unité de points.
- ReflectionEffect.Direction: Obtient/définit la direction du dégradé alpha par rapport à la forme elle-même.
- ReflectionEffect.Distance: Obtient/définit la distance de la réflexion en unité de points.
- ReflectionEffect.FadeDirection: Obtient/définit la direction pour décaler la réflexion.
- ReflectionEffect.RotWithShape: Obtient/définit si la réflexion doit tourner avec la forme.
- ReflectionEffect.Size: Obtient/définit la position finale (le long du dégradé alpha) de la valeur d'alpha finale en unité de pourcentage.
- ReflectionEffect.Transparency: Obtient/définit le degré de transparence de la réflexion initiale en une valeur de 0.0 (opaque) à 1.0 (clair).
- ReflectionEffect.Type: Obtient/définit l'effet de réflexion prédéfini.

Voici un scénario d'utilisation simple de la propriété Shape.Reflection.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Travailler avec les effets de réflexion](/cells/fr/java/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
Aspose.Cells 16.10.0 a exposé la propriété Shape.ShadowEffect ainsi que la classe ShadowEffect qui permettent ensemble de définir l'effet d'ombre sur un objet Shape. La classe ShadowEffect a les propriétés suivantes.

- ShadowEffect.Angle: Obtient/définit l'angle d'éclairage allant de 0 à 359,9 degrés.
- ShadowEffect.Blur: Obtient et définit le flou de l'ombre allant de 0 à 100 points.
- ShadowEffect.Color: Obtient/définit la couleur de l'ombre.
- ShadowEffect.Distance: Obtient/définit la distance de l'ombre allant de 0 à 200 points.
- ShadowEffect.PresetType: Obtient/définit le type d'ombre prédéfini de l'ombre.
- ShadowEffect.Size: Obtient/définit la taille de l'ombre allant de 0 à 2.0. Cela n'aura pas de sens en cas d'ombre interne.
- ShadowEffect.Transparency: Obtient/définit le degré de transparence de l'ombre allant de 0.0 (opaque) à 1.0 (clair).

Voici un scénario d'utilisation simple de la propriété susmentionnée.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Travailler avec les effets d'ombre](/cells/fr/java/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **Prise en charge des effets de lumière**
Aspose.Cells 16.10.0 a exposé la propriété Shape.Glow ainsi que la classe GlowEffect qui ensemble permettent de définir l'effet de lumière d'un objet Shape. La classe GlowEffect spécifie un effet de lumière, dans lequel un contour flou de couleur est ajouté à l'extérieur des bords de l'objet en utilisant les propriétés suivantes.

- GlowEffect.Size: Obtient/définit le rayon de la lumière en points.
- GlowEffect.Transparency: Obtient/définit le degré de transparence de l'effet de lumière allant de 0.0 (opaque) à 1.0 (clair).

Voici un scénario d'utilisation simple de la propriété Shape.Glow.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Travailler avec l'effet de lumière](/cells/fr/java/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
Aspose.Cells 16.10.0 a exposé la propriété Shape.ThreeDFormat ainsi que la classe ThreeDFormat qui peuvent être utilisées ensemble pour contrôler le format 3D de l'objet Shape. La classe ThreeDFormat représente la mise en forme tridimensionnelle d'une forme et possède les propriétés suivantes.

- ThreeDFormat.BottomBevelHeight: Obtient/définit la hauteur de l'aplatissement inférieur ou la distance à laquelle il est appliqué sur la forme, en points.
- ThreeDFormat.BottomBevelType: Obtient/définit le type de l'aplatissement inférieur ou la distance à laquelle il est appliqué, en points.
- ThreeDFormat.BottomBevelWidth: Obtient/définit la largeur de l'aplatissement inférieur ou la distance à laquelle il est appliqué, en points.
- ThreeDFormat.ContourColor: Obtient/définit la couleur du contour d'une forme.
- ThreeDFormat.ContourWidth: Obtient/définit la largeur du contour sur la forme, en points.
- ThreeDFormat.ExtrusionColor: Obtient la couleur d'extrusion sur une forme.
- ThreeDFormat.ExtrusionHeight: Obtient/définit la hauteur d'extrusion appliquée à la forme, en points.
- ThreeDFormat.LightAngle: Obtient/définit l'angle des lumières d'extrusion.
- ThreeDFormat.Lighting: Obtient/définit le type de dispositif d'éclairage.
- ThreeDFormat.LightingDirection : Obtient/définit la direction selon laquelle le système d'éclairage est orienté par rapport à la scène.
- ThreeDFormat.Material : Représente le matériau prédéfini combiné aux propriétés d'éclairage pour donner l'aspect final d'une forme.
- ThreeDFormat.Perspective : Obtient/définit l'angle sous lequel un objet ThreeDFormat peut être visualisé.
- ThreeDFormat.PresetCameraType : Obtient/définit la caméra prédéfinie d'extrusion.
- ThreeDFormat.RotationX : Obtient/définit la rotation de la forme extrudée autour de l'axe X en degrés.
- ThreeDFormat.RotationY : Obtient/définit la rotation de la forme extrudée autour de l'axe Y en degrés.
- ThreeDFormat.RotationZ : Obtient/définit la rotation de la forme extrudée autour de l'axe Z en degrés.
- ThreeDFormat.TopBevelHeight : Obtient/définit la hauteur du biseau supérieur ou sa profondeur dans la forme, en points.
- ThreeDFormat.TopBevelType : Obtient/définit le type du biseau supérieur ou sa profondeur dans la forme, en points.
- ThreeDFormat.TopBevelWidth : Obtient/définit la largeur du biseau supérieur ou sa profondeur dans la forme, en points.
- ThreeDFormat.Z : Définit la distance par rapport au sol pour la forme 3D.

Voici le scénario d'utilisation simple de la propriété Shape.ThreeDFormat.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Travailler avec le format 3D](/cells/fr/java/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
Aspose.Cells 16.10.0 a exposé les méthodes FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle afin de définir le style WordArt prédéfini pour le texte de l'objet Shape.

Voici un scénario d'utilisation simple des méthodes mentionnées ci-dessus.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Travailler avec les styles WordArt](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **Prise en charge des styles WordArt intégrés**
Aspose.Cells 16.10.0 a exposé la méthode ShapeCollection.AddWordArt ainsi que l'énumération PresetWordArtStyle afin de prendre en charge l'ajout d'objets WordArt prédéfinis depuis Excel 2007.

Voici un scénario d'utilisation simple de la méthode ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Ajouter WordArt avec des styles intégrés](/cells/fr/java/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
Aspose.Cells a exposé la méthode XmlMapCollection.Add qui permet d'ajouter une carte XML à une feuille de calcul. Voici un scénario d'utilisation simple de la méthode XmlMapCollection.Add.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Ajouter une carte XML à une feuille de calcul](/cells/fr/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Méthode Cells.LinkToXmlMap ajoutée**
Aspose.Cells a maintenant exposé la méthode Cells.LinkToXmlMap afin de lier les cellules aux éléments de la carte XML. Voici un scénario d'utilisation simple de la méthode Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Lier des cellules à des éléments de carte XML](/cells/fr/java/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **Propriété Formula de ListColumn ajoutée**
Aspose.Cells 16.10.0 a exposé la propriété ListColumn.Formula pour propager automatiquement la formule aux nouvelles lignes insérées.

Voici un scénario d'utilisation simple de la propriété ListColumn.Formula.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Propager automatiquement la formule dans un objet de liste](/cells/fr/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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

listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
