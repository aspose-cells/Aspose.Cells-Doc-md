---
title: Public API Changements dans Aspose.Cells 17.1.0
type: docs
weight: 380
url: /fr/java/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 16.12.0 à 17.1.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge des graphiques Excel 2016**
Les API Aspose.Cells ont ajouté la prise en charge de quelques graphiques Excel 2016 en améliorant l'énumération ChartType. Les nouveaux champs suivants ont été ajoutés avec la sortie de Aspose.Cells 17.1.0.

- ChartType.BOX_WHISKER : la série est présentée sous la forme d'une boîte et d'une moustache.
- ChartType.FUNNEL : la série est présentée sous forme d'entonnoir.
- ChartType.PARETO_LINE : la série est présentée sous forme de lignes de Pareto.
- ChartType.SUNBURST : la série est présentée sous la forme d'un rayon de soleil.
- ChartType.TREEMAP : la série est présentée sous forme de treemap.
- ChartType.WATERFALL : la série est présentée sous forme de cascade.
- ChartType.HISTOGRAM : la série est présentée sous forme d'histogramme.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Lecture des types de graphiques Excel 2016](/cells/fr/java/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Setter ajouté pour la propriété LoadFilter.LoadDataFilterOptions**
Aspose.Cells 17.1.0 a ajouté un setter pour la propriété LoadFilter.LoadDataFilterOptions pour remplacer la variable d'instance m_LoadDataFilterOptions. Les utilisateurs peuvent modifier la propriété LoadDataFilterOptions dans leur propre implémentation de la classe LoadFilter pour modifier le comportement de chargement des fichiers modèles.

Voici un scénario d'utilisation simple.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Filtrage de modèles personnalisés](/cells/fr/java/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 class CustomLoadFilter extends LoadFilter {

	public void startSheet(Worksheet sheet) {

		if (sheet.getName().equals("NoCharts")) {

			//Load everything and filter charts

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CHART);

		}

		if (sheet.getName().equals("NoShapes")) {

			//Load everything and filter shapes

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.SHAPE);

		}

		if (sheet.getName().equals("NoConditionalFormatting")) {

			//Load everything and filter conditional formatting

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CONDITIONAL_FORMATTING);

		}

	}

}

{{< /highlight >}}
### **Ajout de la propriété CellsHelper.SignificantDigits**
Aspose.Cells 17.1.0 a exposé la propriété SignificantDigits de la classe CellsHelper qui permet d'obtenir ou de définir le nombre de chiffres significatifs pour les valeurs numériques dans une feuille de calcul. La valeur par défaut de la propriété CellsHelper.SignificantDigits est 17 alors qu'elle n'est applicable que si le résultat doit être stocké au format de fichier XLSX.

Voici un scénario simple pour démontrer l'utilisation de la propriété CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Définition du nombre de chiffres significatifs](/cells/fr/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **Ajout de la propriété GlowEffect.Color**
Aspose.Cells 17.1.0 a ajouté la propriété GlowEffect.Color qui peut être utilisée pour récupérer la couleur de l'effet de lueur.

L'extrait de code suivant utilise la propriété GlowEffect.Color.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Lecture de la couleur de lueur de la forme](/cells/fr/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Read the source Excel file

Workbook book = new Workbook(dir + "sample.xlsx");

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access the first shape

Shape shape = sheet.getShapes().get(0);

//Read the glow effect color

GlowEffect glow = shape.getGlow();

CellsColor color = glow.getColor();

{{< /highlight >}}
### **Ajout des propriétés PageSetup.PaperWidth et PaperHeight**
Aspose.Cells 17.1.0 a exposé les propriétés PaperWidth et PaperHeight pour la classe PageSetup. Les propriétés PageSetup.PaperWidth & PageSetup.PaperHeight sont de type double représentant la largeur et la hauteur du papier en pouces tout en tenant compte de l'orientation de la page.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Récupération de la taille du papier de la feuille de calcul](/cells/fr/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **Ajout de la propriété WorkbookSettings.CheckCustomNumberFormat**
Aspose.Cells 17.1.0 a ajouté la propriété CheckCustomNumberFormat à la classe WorkbookSettings. Le CheckCustomNumberFormat est utile pour vérifier si la propriété Style.Custom a été définie correctement ou non. Dans le cas où la propriété Style.Custom a été définie de manière incorrecte, c'est-à-dire ; la valeur ne correspond pas à un modèle valide, les API Aspose.Cells lèveront CellsException avec le message approprié.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Vérification du format personnalisé](/cells/fr/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Set CheckCustomNumberFormat property to true

book.getSettings().setCheckCustomNumberFormat(true);

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access a cell

Cell cell = sheet.getCells().get("B5");

//Insert a value to the cell

cell.putValue(2347);

//Access cell's style

Style style = cell.getStyle();



//Set Custom property to an invalid pattern

style.setCustom("ggg @ fff");

//Set the modified style to the cell

cell.setStyle(style);

{{< /highlight >}}
### **Ajout du champ DisplayUnitType.PERCENTAGE**
Aspose.Cells 17.1.0 a également exposé le champ PERCENTAGE à l'énumération DisplayUnitType. Le champ DisplayUnitType.PERCENTAGE indique que les valeurs du graphique doivent être divisées par 0,01.
## **API supprimées**
### **Variable d'instance m_LoadDataFilterOptions supprimée**
Cette version a supprimé la variable d'instance m_LoadDataFilterOptions. Il est conseillé d'utiliser à la place la propriété LoadFilter.LoadDataFilterOptions.
