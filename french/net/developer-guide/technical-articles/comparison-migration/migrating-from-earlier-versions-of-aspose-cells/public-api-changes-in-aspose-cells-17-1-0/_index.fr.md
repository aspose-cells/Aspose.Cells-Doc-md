---
title: Public API Changements dans Aspose.Cells 17.1.0
type: docs
weight: 370
url: /fr/net/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 16.12.0 à 17.1.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge des graphiques Excel 2016**
Les API Aspose.Cells ont ajouté la prise en charge de quelques graphiques Excel 2016 en améliorant l'énumération ChartType. Les nouveaux champs suivants ont été ajoutés avec la sortie de Aspose.Cells 17.1.0.

- ChartType.BoxWhisker : la série est présentée sous la forme d'une boîte et d'une moustache.
- ChartType.Funnel : la série est présentée sous forme d'entonnoir.
- ChartType.ParetoLine : la série est présentée sous forme de lignes de Pareto.
- ChartType.Sunburst : la série est présentée sous la forme d'un rayon de soleil.
- ChartType.Treemap : la série est présentée sous forme de treemap.
- ChartType.Waterfall : la série est présentée sous forme de cascade.
- ChartType.Histogram : la série est présentée sous forme d'histogramme.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Lecture des types de graphiques Excel 2016](/cells/fr/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Setter ajouté pour la propriété LoadFilter.LoadDataFilterOptions**
Aspose.Cells 17.1.0 a ajouté un setter pour la propriété LoadFilter.LoadDataFilterOptions pour remplacer la variable d'instance m_LoadDataFilterOptions. Les utilisateurs peuvent modifier la propriété LoadDataFilterOptions dans leur propre implémentation de la classe LoadFilter pour modifier le comportement de chargement des fichiers modèles.

Voici un scénario d'utilisation simple.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Filtrage de modèles personnalisés](/cells/fr/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            this.LoadDataFilterOptions = LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            this.LoadDataFilterOptions = LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}


### **Ajout de la propriété CellsHelper.SignificantDigits**
Aspose.Cells 17.1.0 a exposé la propriété SignificantDigits de la classe CellsHelper qui permet d'obtenir ou de définir le nombre de chiffres significatifs pour les valeurs numériques dans une feuille de calcul. La valeur par défaut de la propriété CellsHelper.SignificantDigits est 17 alors qu'elle n'est applicable que si le résultat doit être stocké au format de fichier XLSX.

Voici un scénario simple pour démontrer l'utilisation de la propriété CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Définition du nombre de chiffres significatifs](/cells/fr/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **Ajout de la propriété GlowEffect.Color**
Aspose.Cells 17.1.0 a ajouté la propriété GlowEffect.Color qui peut être utilisée pour récupérer la couleur de l'effet de lueur.

L'extrait de code suivant utilise la propriété GlowEffect.Color.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Lecture de la couleur de lueur de la forme](/cells/fr/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Read the source excel file

var book = new Workbook(dir + "sample.xlsx");

// Access first worksheet

var sheet = book.Worksheets[0];

// Access the first shape

var shape = sheet.Shapes[0];

// Read the glow effect color

var glow = shape.Glow;

var color = glow.Color;

{{< /highlight >}}


### **Ajout des propriétés PageSetup.PaperWidth et PaperHeight**
Aspose.Cells 17.1.0 a exposé les propriétés PaperWidth et PaperHeight pour la classe PageSetup. Les propriétés PageSetup.PaperWidth & PageSetup.PaperHeight sont de type double représentant la largeur et la hauteur du papier en pouces tout en tenant compte de l'orientation de la page.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Récupération de la taille du papier de la feuille de calcul](/cells/fr/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **Ajout de la propriété WorkbookSettings.CheckCustomNumberFormat**
Aspose.Cells 17.1.0 a ajouté la propriété CheckCustomNumberFormat à la classe WorkbookSettings. Le CheckCustomNumberFormat est utile pour vérifier si la propriété Style.Custom a été définie correctement ou non. Dans le cas où la propriété Style.Custom a été définie de manière incorrecte, c'est-à-dire ; la valeur ne correspond pas à un modèle valide, les API Aspose.Cells lèveront CellsException avec le message approprié.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Vérification du format personnalisé](/cells/fr/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Set CheckCustomNumberFormat property to true

book.Settings.CheckCustomNumberFormat = true;

// Access first worksheet

var sheet = book.Worksheets[0];

// Access a cell

var cell = sheet.Cells["B5"];

// Insert a value to the cell

cell.PutValue(2347);

// Access cell's style

Style style = cell.GetStyle();



// Set Custom property to an invalid pattern

style.Custom = "ggg @ fff";

// Set the modified style to the cell

cell.SetStyle(style);

{{< /highlight >}}


### **Ajout du champ DisplayUnitType.Percentage**
Aspose.Cells 17.1.0 a également exposé le champ Percentage à l'énumération DisplayUnitType. Le champ DisplayUnitType.Percentage indique que les valeurs du graphique doivent être divisées par 0,01.
## **API supprimées**
### **Variable d'instance m_LoadDataFilterOptions supprimée**
Cette version a supprimé la variable d'instance m_LoadDataFilterOptions. Il est conseillé d'utiliser à la place la propriété LoadFilter.LoadDataFilterOptions.
