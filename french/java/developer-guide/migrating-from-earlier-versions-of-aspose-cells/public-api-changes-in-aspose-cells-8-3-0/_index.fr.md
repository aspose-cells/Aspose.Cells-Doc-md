---
title: Changements de l API publique dans Aspose.Cells 8.3.0
type: docs
weight: 110
url: /fr/java/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.2.2 à la version 8.3.0 susceptibles d'intéresser les développeurs de modules/applications.

{{% /alert %}} 
## **APIs ajoutées**
### **Propriété WorkbookSettings.AutoRecover ajoutée**
Le getter/setter pour la propriété AutoRecover a été ajouté à la classe WorkbookSettings afin de permettre aux développeurs d'obtenir/définir l'option de récupération automatique pour les feuilles de calcul dans leurs applications. 

{{% alert color="primary" %}} 

Veuillez consulter l'article [Configuration de la récupération automatique de feuilles de calcul](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) pour plus d'informations.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Propriété WorkbookSettings.CrashSave ajoutée**
Le getter/setter pour la propriété CrashSave a été ajouté à la classe WorkbookSettings. La propriété de type booléen indique si l'application a sauvegardé le fichier de classeur après un crash.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Propriété WorkbookSettings.DataExtractLoad ajoutée**
Le getter/setter pour la propriété DataExtractLoad a été ajouté à la classe WorkbookSettings afin de permettre aux développeurs d'obtenir/définir les informations concernant la dernière récupération. Si la propriété DataExtractLoad retourne true, cela indique que la récupération des données a été effectuée sur le fichier de classeur.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Propriété WorkbookSettings.RepairLoad ajoutée**
Le getter/setter pour la propriété RepairLoad a été ajouté à la classe WorkbookSettings. La propriété de type booléen indique si la feuille de calcul a été réparée lors de la dernière session de chargement avec l'application Excel.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Ajout de la propriété TxtLoadOptions.KeepExactFormat**
La propriété KeepExactFormat a été ajoutée à la classe TxtLoadOptions et indique si le format exact doit être conservé pour la valeur de la cellule lors de la conversion de la chaîne/texte en chiffres ou en date/heure. Cette propriété a été ajoutée pour correspondre au comportement de l'application MS Excel lors du chargement de valeurs DateTime ou numériques à partir de fichiers CSV. Pour simuler le comportement de MS Excel, définissez la propriété KeepExactFormat sur false, alors que la valeur par défaut est true, afin que la valeur de la cellule soit formatée comme la chaîne dans le fichier CSV.

**Java**

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Ajout de la propriété Shape.Id**
La v8.3.0 a ajouté le getter/setter pour la propriété Shape.Id afin d'identifier de manière unique chaque objet de forme dans une feuille de calcul donnée. Cette nouvelle propriété aide également à identifier de manière unique les objets Chart dans une feuille de calcul comme démontré ci-dessous.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

ChartCollection charts = book.getWorksheets().get(0).getCharts();

for(int index = 0; index <= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **Ajout de la méthode PlotArea.setPositionAuto**
La méthode setPositionAuto a été ajoutée à la classe PlotArea et aide à définir la zone de tracé du graphique en mode automatique.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
