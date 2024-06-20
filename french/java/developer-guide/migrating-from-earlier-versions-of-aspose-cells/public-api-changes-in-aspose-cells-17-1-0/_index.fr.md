---
title: Changements de l API publique dans Aspose.Cells 17.1.0
type: docs
weight: 380
url: /fr/java/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 16.12.0 à la version 17.1.0 qui pourraient intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, mais aussi une description de tout changement de comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Prise en charge des graphiques Excel 2016**
Les APIs Aspose.Cells ont ajouté la prise en charge de quelques graphiques Excel 2016 en améliorant l'énumération ChartType. Les nouveaux champs suivants ont été ajoutés avec la version Aspose.Cells 17.1.0.

- ChartType.BOX_WHISKER: La série est disposée en boîte et en fouet.
- ChartType.FUNNEL: La série est disposée en entonnoir.
- ChartType.PARETO_LINE: La série est disposée en lignes de Pareto.
- ChartType.SUNBURST: La série est disposée en soleil levant.
- ChartType.TREEMAP: La série est disposée en treemap.
- ChartType.WATERFALL: La série est disposée en cascade.
- ChartType.HISTOGRAM: La série est disposée en histogramme.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Lecture des types de graphiques Excel 2016](/cells/fr/java/lire-et-manipuler-les-types-de-graphiques-excel-2016/)

{{% /alert %}} 
### **Setter ajouté pour la propriété LoadFilter.LoadDataFilterOptions**
Aspose.Cells 17.1.0 a ajouté un setter pour la propriété LoadFilter.LoadDataFilterOptions pour remplacer la variable d'instance m_LoadDataFilterOptions. Les utilisateurs peuvent changer la propriété LoadDataFilterOptions dans leur propre implémentation de la classe LoadFilter pour changer le comportement du chargement des fichiers de modèle.

Voici un scénario d'utilisation simple.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Filtrage de modèle personnalisé](/cells/fr/java/filtrer-des-objets-lors-du-chargement-d-un-classeur-ou-d-une-feuille-de-calcul/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
Aspose.Cells 17.1.0 a exposé la propriété SignificantDigits de la classe CellsHelper qui permet de récupérer ou définir le nombre de chiffres significatifs pour les valeurs numériques dans une feuille de calcul. La valeur par défaut de la propriété CellsHelper.SignificantDigits est 17, elle s'applique uniquement si le résultat doit être stocké au format de fichier XLSX.

Voici un scénario simple pour démontrer l'utilisation de la propriété CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur le [Réglage du nombre de chiffres significatifs](/cells/fr/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **Ajout de la propriété GlowEffect.Color**
Aspose.Cells 17.1.0 a ajouté la propriété GlowEffect.Color qui peut être utilisée pour récupérer la couleur de l'effet de lueur.

L'extrait suivant utilise la propriété GlowEffect.Color.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Lecture de la couleur de l'effet de lueur de la forme](/cells/fr/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **Ajout des propriétés PageSetup.PaperWidth & PaperHeight**
Aspose.Cells 17.1.0 a exposé les propriétés PaperWidth & PaperHeight pour la classe PageSetup. Les propriétés PageSetup.PaperWidth & PageSetup.PaperHeight sont de type double représentant la largeur et la hauteur du papier en pouces tout en considérant l'orientation de la page.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Récupération de la taille du papier de la feuille de calcul](/cells/fr/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **Ajout de la propriété WorkbookSettings.CheckCustomNumberFormat**
Aspose.Cells 17.1.0 a ajouté la propriété CheckCustomNumberFormat à la classe WorkbookSettings. CheckCustomNumberFormat est utile pour vérifier si la propriété Style.Custom a été correctement définie ou non. Si la propriété Style.Custom a été définie de manière incorrecte, c'est-à-dire si la valeur ne correspond pas à un motif valide, alors les API Aspose.Cells lèveront une CellsException avec le message approprié.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Vérification du format personnalisé](/cells/fr/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
Aspose.Cells 17.1.0 a également exposé le champ PERCENTAGE à l'énumération DisplayUnitType. Le champ DisplayUnitType.PERCENTAGE indique que les valeurs sur le graphique seront divisées par 0,01.
## **APIs supprimées**
### **Option m_LoadDataFilterOptions de l'instance supprimée**
Cette version a supprimé la variable d'instance m_LoadDataFilterOptions. Il est conseillé d'utiliser la propriété LoadFilter.LoadDataFilterOptions à la place.
