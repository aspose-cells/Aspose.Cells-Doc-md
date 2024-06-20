---
title: Changements de l API publique dans Aspose.Cells 8.3.0
type: docs
weight: 100
url: /fr/net/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.2.2 à la version 8.3.0 susceptibles d'intéresser les développeurs de modules/applications.

{{% /alert %}} 
## **APIs ajoutées**
### **Propriété WorkbookSettings.AutoRecover ajoutée**
La nouvelle propriété AutoRecover a été ajoutée à la classe WorkbookSettings afin de permettre aux développeurs de définir l'option de récupération automatique pour les feuilles de calcul dans leurs applications.

{{% alert color="primary" %}} 

Veuillez consulter l'article [Définir la récupération automatique de feuilles de calcul](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) pour plus d'informations.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Propriété WorkbookSettings.CrashSave ajoutée**
Une propriété de type booléen CrashSave a été ajoutée à la classe WorkbookSettings, indiquant si l'application a enregistré le fichier du classeur après un crash.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Propriété WorkbookSettings.DataExtractLoad ajoutée**
La propriété DataExtractLoad a été ajoutée à la classe WorkbookSettings afin de permettre aux développeurs d'obtenir des informations sur la dernière récupération. Si la propriété DataExtractLoad renvoie true, cela indique que la récupération des données a été effectuée sur la feuille de calcul.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Propriété WorkbookSettings.RepairLoad ajoutée**
La propriété RepairLoad indique si la feuille de calcul a été réparée lors du dernier chargement avec l'application Excel.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Ajout de la propriété TxtLoadOptions.KeepExactFormat**
La propriété KeepExactFormat a été ajoutée à la classe TxtLoadOptions et indique si le format exact doit être conservé pour la valeur de la cellule lors de la conversion de la chaîne/texte en chiffres ou en date/heure. Cette propriété a été ajoutée pour correspondre au comportement de l'application MS Excel lors du chargement de valeurs DateTime ou numériques à partir de fichiers CSV. Pour simuler le comportement de MS Excel, définissez la propriété KeepExactFormat sur false, alors que la valeur par défaut est true, afin que la valeur de la cellule soit formatée comme la chaîne dans le fichier CSV.

**C#**

{{< highlight csharp >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Ajout de la propriété Shape.Id**
La propriété Id a été ajoutée à la classe Shape pour identifier de manière unique chaque objet de forme dans une feuille de calcul donnée. Cette nouvelle propriété aide également à identifier les objets de graphique dans une feuille de calcul comme illustré ci-dessous.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Méthode SetPositionAuto ajoutée à la classe PlotArea**
La méthode SetPositionAuto a été ajoutée à la classe PlotArea pour aider à définir la zone de tracé du graphique en mode automatique.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
