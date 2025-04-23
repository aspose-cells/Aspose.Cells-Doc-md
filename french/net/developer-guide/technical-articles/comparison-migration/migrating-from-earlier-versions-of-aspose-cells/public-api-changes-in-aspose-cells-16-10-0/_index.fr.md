---
title: Changements de l API publique dans Aspose.Cells 16.10.0
type: docs
weight: 340
url: /fr/net/public-api-changes-in-aspose-cells-16-10-0/
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

Consultez l'article détaillé sur [Working with Reflection Effects](/cells/fr/net/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ReflectionEffect from the Shape object

var reflection = shape.Reflection;

// Set its Blur, Size, Transparency and Distance properties

reflection.Blur = 30;

reflection.Size = 90;

reflection.Transparency = 0.5;

reflection.Distance = 80;

// Save the result in XLSX format

book.Save("output.xlsx");

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

Consultez l'article détaillé sur [Travailler avec des Effets d'Ombre](/cells/fr/net/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ShadowEffect from the Shape object

var shadow = shape.ShadowEffect;

// Set its Angle, Blur, Size, Transparency and Distance properties

shadow.Angle = 150;

shadow.Blur = 30;

shadow.Size = 90;

shadow.Transparency = 0.5;

shadow.Distance = 80;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Prise en charge des effets de lumière**
Aspose.Cells 16.10.0 a exposé la propriété Shape.Glow ainsi que la classe GlowEffect qui ensemble permettent de définir l'effet de lumière d'un objet Shape. La classe GlowEffect spécifie un effet de lumière, dans lequel un contour flou de couleur est ajouté à l'extérieur des bords de l'objet en utilisant les propriétés suivantes.

- GlowEffect.Size: Obtient/définit le rayon de la lumière en points.
- GlowEffect.Transparency: Obtient/définit le degré de transparence de l'effet de lumière allant de 0.0 (opaque) à 1.0 (clair).

Voici un scénario d'utilisation simple de la propriété Shape.Glow.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Travailler avec l'Effet Lumineux](/cells/fr/net/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of GlowEffect from the Shape object

var glow = shape.Glow;

// Set its Size & Transparency properties

glow.Size = 90;

glow.Transparency = 0.5;

// Save the result in XLSX format

book.Save("output.xlsx");

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

Consultez l'article détaillé sur [Travailler avec le format 3D](/cells/fr/net/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ThreeDFormat from the Shape object

var threeD = shape.ThreeDFormat;

// Set its ContourWidth & ExtrusionHeight properties

threeD.ContourWidth = 15;

threeD.ExtrusionHeight = 30;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Prise en charge des styles WordArt dans le texte de Shape**
Aspose.Cells 16.10.0 a exposé les méthodes FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle afin de définir le style WordArt prédéfini pour le texte de l'objet Shape.

Voici un scénario d'utilisation simple des méthodes mentionnées ci-dessus.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Travailler avec les styles WordArt](/cells/fr/net/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create workbook object

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Create a TextBox with some text

var textBox = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 700);

textBox.Text = "Aspose File Format APIs";

textBox.Font.Size = 44;

// Set preset WordArt style to the text of the shape

FontSetting fntSetting = textBox.GetCharacters()[0] as FontSetting;

fntSetting.SetWordArtStyle(PresetWordArtStyle.WordArtStyle3);

{{< /highlight >}}


### **Prise en charge des styles WordArt intégrés**
Aspose.Cells 16.10.0 a exposé la méthode ShapeCollection.AddWordArt ainsi que l'énumération PresetWordArtStyle afin de prendre en charge l'ajout d'objets WordArt prédéfinis depuis Excel 2007.

Voici un scénario d'utilisation simple de la méthode ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Ajouter WordArt avec des styles intégrés](/cells/fr/net/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access ShapeCollection of first worksheet

var shapes = sheet.Shapes;

// Add WordArt with built-in styles

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 00, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Méthode XmlMapCollection.Add ajoutée**
Aspose.Cells a exposé la méthode XmlMapCollection.Add qui permet d'ajouter une carte XML à une feuille de calcul. Voici un scénario d'utilisation simple de la méthode XmlMapCollection.Add.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Ajouter une carte XML à la feuille de calcul](/cells/fr/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **Méthode Cells.LinkToXmlMap ajoutée**
Aspose.Cells a maintenant exposé la méthode Cells.LinkToXmlMap pour lier les cellules avec les éléments de la carte XML.

Voici un scénario d'utilisation simple de la méthode Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Lier les cellules aux éléments de la carte XML](/cells/fr/net/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook("sample.xlsx");

// Access the XML Map from the spreadsheet

var map = book.Worksheets.XmlMaps[0];

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Map FIELD1 and FIELD2 to cell A1 and B2

sheet.Cells.LinkToXmlMap(map.Name, 0, 0, "/root/row/FIELD1");

sheet.Cells.LinkToXmlMap(map.Name, 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cell C3 and D4

sheet.Cells.LinkToXmlMap(map.Name, 2, 2, "/root/row/FIELD4");

sheet.Cells.LinkToXmlMap(map.Name, 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cell E5 and F6

sheet.Cells.LinkToXmlMap(map.Name, 4, 4, "/root/row/FIELD7");

sheet.Cells.LinkToXmlMap(map.Name, 5, 5, "/root/row/FIELD8");

{{< /highlight >}}


### **Propriété Formula de ListColumn ajoutée**
Aspose.Cells 16.10.0 a exposé la propriété ListColumn.Formula pour propager automatiquement la formule aux nouvelles lignes insérées.

Voici un scénario d'utilisation simple de la propriété ListColumn.Formula.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Propagation automatique de formule dans un objet de liste](/cells/fr/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add column headings in cell A1 and B1

sheet.Cells[0, 0].PutValue("Column A");

sheet.Cells[0, 1].PutValue("Column B");

// Add list object, set its name and style

var listObject = sheet.ListObjects[sheet.ListObjects.Add(0, 0, 1, sheet.Cells.MaxColumn, true)];

listObject.TableStyleType = TableStyleType.TableStyleMedium2;

listObject.DisplayName = "Table";

// Set the formula of second column so that it could automatically propagate to new rows while entering data

listObject.ListColumns[1].Formula = "=[Column A] + 1";

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Prise en charge du calcul des fonctions personnalisées avec GridWeb**
Aspose.Cells.GridWeb 16.10.0 a exposé la propriété GridWeb.CustomCalculationEngine avec la classe GridAbstractCalculationEngine, ce qui permet de définir et de calculer les fonctions personnalisées à partir du composant GridWeb.

Voici un scénario d'utilisation simple des API susmentionnées.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Calcul des fonctions personnalisées avec GridWeb](/cells/fr/net/calculate-custom-functions-in-gridweb/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 private class GridWebCustomCalculationEngine : GridAbstractCalculationEngine

{

    public override void Calculate(GridCalculationData data)

    {

        //  Calculate MYTESTFUNC() with your own logic.

        //For example, you can multiply MYTESTFUNC() parameter with 2 so

        // MYTESTFUNC(3.0) will return 6

        // MYTESTFUNC(4.0) will return 8

        // MYTESTFUNC(5.0) will return 10

        if ("MYTESTFUNC".Equals(data.FunctionName.ToUpper()))

        {

            data.CalculatedValue = (decimal)(2.0 * (double)data.GetParamValue(0));

        }

    }

}


if (Page.IsPostBack == false && GridWeb1.IsPostBack == false)

{

    // Assign your own custom calculation engine to GridWeb

    GridWeb1.CustomCalculationEngine = new GridWebCustomCalculationEngine();

    // Access the active worksheet and add your custom function in cell B3

    GridWorksheet sheet = GridWeb1.ActiveSheet;

    GridCell cell = sheet.Cells["B3"];

    cell.Formula = "=MYTESTFUNC(9.0)";

    // Calculate the GridWeb formula

    GridWeb1.CalculateFormula();

}

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
