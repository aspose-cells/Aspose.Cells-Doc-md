---
title: Changements d API public dans Aspose.Cells 8.6.1
type: docs
weight: 200
url: /fr/net/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.6.0 à la 8.6.1 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement de nouvelles et des méthodes publiques mises à jour, des classes ajoutées, mais aussi une description de tout changement dans le comportement en arrière-plan d'Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Support du type de cible de lien HTML**
Cette version de l'API Aspose.Cells for .NET a exposé une énumération nommée HtmlLinkTargetType ainsi qu'une nouvelle propriété HtmlSaveOptions.LinkTargetType qui permettent ensemble de définir le type de cible pour les liens dans la feuille de calcul lors de la conversion au format HTML. Les valeurs possibles de l'énumération HtmlLinkTargetType sont les suivantes où la valeur par défaut est Self.

1. HtmlLinkTargetType.Blank : Ouvre le document/page lié dans une nouvelle fenêtre ou un nouvel onglet.
1. HtmlLinkTargetType.Parent : Ouvre le document/page lié dans le cadre parent.
1. HtmlLinkTargetType.Self : Ouvre le document/page lié dans le même cadre où le lien a été cliqué.
1. HtmlLinkTargetType.Top : Ouvre le document/page lié dans l'intégralité de la fenêtre.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **Ajout de la méthode VbaModuleCollection.Remove**
Aspose.Cells for .NET 8.6.1 a exposé une autre surcharge de la méthode VbaModuleCollection.Remove qui peut désormais accepter une instance de Worksheet pour supprimer tous les modules VBA associés à la feuille de calcul spécifiée.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Ajout de la méthode RangeCollection.Add**
Aspose.Cells for .NET 8.6.1 a exposé la méthode RangeCollection.Add qui peut être utilisée pour ajouter des objets Range à la collection de plages pour une feuille de calcul particulière.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **Ajout de la méthode Cell.SetCharacters**
La méthode Cell.SetCharacters peut être utilisée pour [mettre à jour les portions du texte enrichi](/cells/fr/net/access-and-update-the-portions-of-rich-text-of-cell/) d'un objet Cell donné. La méthode Cell.GetCharacters doit être utilisée pour accéder aux portions du texte, puis les modifications peuvent être apportées en utilisant la méthode Cell.SetCharacters, alors que la méthode **Get** renvoie un tableau d'objets FontSetting qui peuvent être manipulés pour définir diverses propriétés telles que le nom de la police, la couleur de la police, la graisse, etc. et la méthode **Set** peut être utilisée pour appliquer les changements.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **Propriété VbaProject.IsSigned ajoutée**
Aspose.Cells for .NET 8.6.1 a exposé la propriété VbaProject.IsSigned qui peut être utilisée pour [vérifier si un projet VBA dans un classeur est signé ou non](/cells/fr/net/check-if-vba-project-in-a-workbook-is-signed/). La propriété de type booléen renvoie true si le projet est signé.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.VbaProject;

//Test if VbaProject is signed

if (project.IsSigned)

{

    Console.WriteLine("VBA Project is Signed");

}

else

{

    Console.WriteLine("VBA Project is not Signed");

}

{{< /highlight >}}
## **APIs modifiées**
### **Méthode Cell.GetFormatConditions modifiée**
Avec la publication de v8.6.1, l'API Aspose.Cells for .NET a modifié le type de retour de la méthode Cell.GetFormatConditions qui renvoie désormais un tableau de type FormatConditionCollection.
## **APIs obsolètes**
### **Méthode Workbook.CheckWriteProtectedPassword obsolète**
Avec la publication de v8.6.1, la méthode Workbook.CheckWriteProtectedPassword a été marquée comme obsolète. Il est conseillé d'utiliser la méthode WorkbookSettings.WriteProtection.ValidatePassword qui peut accepter une valeur de chaîne en paramètre et renvoie un booléen si le mot de passe correspond au mot de passe prédéfini de la feuille de calcul.
{{< app/cells/assistant language="csharp" >}}
