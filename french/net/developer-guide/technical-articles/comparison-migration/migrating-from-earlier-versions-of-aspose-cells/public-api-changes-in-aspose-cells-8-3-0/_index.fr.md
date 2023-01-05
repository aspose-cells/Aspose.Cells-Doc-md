---
title: Public API Changements dans Aspose.Cells 8.3.0
type: docs
weight: 100
url: /fr/net/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.2.2 à 8.3.0 qui peuvent intéresser les développeurs de modules/applications.

{{% /alert %}} 
## **API ajoutées**
### **Propriété WorkbookSettings.AutoRecover ajouté**
La nouvelle propriété AutoRecover a été ajoutée à la classe WorkbookSettings afin de permettre aux développeurs de définir l'option de récupération automatique pour les feuilles de calcul dans leurs applications.

{{% alert color="primary" %}} 

 Veuillez vérifier l'article[Configuration de la récupération automatique de la feuille de calcul](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) pour plus d'informations.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Propriété WorkbookSettings.CrashSave ajouté**
Une propriété de type booléen CrashSave a été ajoutée à la classe WorkbookSettings qui indique si l'application a enregistré pour la dernière fois le fichier de classeur après un blocage.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Propriété WorkbookSettings.DataExtractLoad ajoutée**
La propriété DataExtractLoad a été ajoutée à la classe WorkbookSettings afin de permettre aux développeurs d'obtenir les informations concernant la dernière récupération. Si la propriété DataExtractLoad renvoie true, cela indique que la récupération des données a été effectuée sur la feuille de calcul.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Propriété WorkbookSettings.RepairLoad ajouté**
La propriété RepairLoad indique si la feuille de calcul a été réparée lors du dernier chargement avec l'application Excel.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Propriété TxtLoadOptions.KeepExactFormat ajoutée**
La propriété KeepExactFormat a été ajoutée à la classe TxtLoadOptions qui indique si la mise en forme exacte doit être conservée pour la valeur de la cellule lorsque la chaîne/le texte est converti en nombres ou en DateTime. Cette propriété a été ajoutée pour correspondre au comportement de l'application MS Excel pour le chargement de valeurs DateTime ou numériques à partir de fichiers CSV. Afin de simuler le comportement de MS Excel, définissez la propriété KeepExactFormat sur false, tandis que la valeur par défaut est true afin que la valeur de la cellule soit formatée comme la chaîne dans le fichier CSV.

**C#**

{{< highlight "csharp" >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Propriété Shape.Id ajoutée**
La propriété Id a été ajoutée à la classe Shape pour identifier de manière unique chaque objet forme dans une feuille de calcul donnée. Cette nouvelle propriété aide également à identifier les objets Chart dans une feuille de calcul, comme illustré ci-dessous.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Méthode PlotArea.SetPositionAuto ajoutée**
La méthode SetPositionAuto a été ajoutée à la classe PlotArea qui aide à définir la zone de tracé du graphique en mode automatique.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
