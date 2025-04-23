---
title: Changements d API public dans Aspose.Cells 8.6.1
type: docs
weight: 210
url: /fr/java/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.6.0 à la 8.6.1 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement de nouvelles et des méthodes publiques mises à jour, des classes ajoutées, mais aussi une description de tout changement dans le comportement en arrière-plan d'Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Support du type de cible de lien HTML**
Cette version de l'API Aspose.Cells for Java a exposé une énumération nommée HtmlLinkTargetType ainsi qu'une nouvelle propriété HtmlSaveOptions.LinkTargetType qui permettent ensemble de [définir le type de cible pour les liens dans la feuille de calcul lors de la conversion au format HTML](/cells/fr/java/change-the-html-link-target-type/). Les valeurs possibles de l'énumération HtmlLinkTargetType sont les suivantes où la valeur par défaut est SELF.

1. HtmlLinkTargetType.BLANK : Ouvre le document/page lié dans une nouvelle fenêtre ou un nouvel onglet.
1. HtmlLinkTargetType.PARENT : Ouvre le document/page lié dans le cadre parent.
1. HtmlLinkTargetType.SELF : Ouvre le document/page lié dans le même cadre où le lien a été cliqué.
1. HtmlLinkTargetType.TOP : Ouvre le document/page lié dans le corps complet de la fenêtre.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **Méthode VbaModuleCollection.remove ajoutée**
Aspose.Cells for Java 8.6.1 a exposé une autre surcharge de la méthode VbaModuleCollection.remove qui peut maintenant accepter une instance de Worksheet pour supprimer tous les modules VBA associés à la feuille de calcul spécifiée.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Méthode RangeCollection.add ajoutée**
Aspose.Cells for Java 8.6.1 a exposé la méthode RangeCollection.Add qui peut être utilisée pour ajouter des objets Range à la collection de plages pour une feuille de calcul spécifique.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **Méthode Cell.setCharacters ajoutée**
La méthode Cell.setCharacters peut être utilisée pour [mettre à jour les portions du texte enrichi](/cells/fr/java/access-and-update-the-portions-of-rich-text-of-cell/) d'un objet Cell donné. La méthode Cell.getCharacters est utilisée pour accéder aux portions du texte, puis les modifications peuvent être apportées à l'aide de la méthode Cell.setCharacters tandis que la **méthode get** renvoie un tableau d'objets FontSetting qui peuvent être manipulés pour définir différentes propriétés telles que le nom de la police, la couleur de la police, la mise en gras, etc. et la **méthode set** peut être utilisée pour appliquer les modifications.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **Propriété VbaProject.isSigned ajoutée**
Aspose.Cells for Java 8.6.1 a exposé la propriété VbaProject.isSigned qui peut être utilisée pour [tester si un projet VbaProject dans un classeur est signé ou non](/cells/fr/java/check-if-vba-project-in-a-workbook-is-signed/). La propriété de type booléen renvoie true si le projet est signé.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.getVbaProject();

//Test if VbaProject is signed

if (project.isSigned())

{

    System.out.println("VBA Project is Signed");

}

else

{

	System.out.println("VBA Project is not Signed");

}

{{< /highlight >}}
## **APIs modifiées**
### **Méthode Cell.getFormatConditions modifiée**
Avec la version 8.6.1, l'API Aspose.Cells for Java a modifié le type de retour de la méthode Cell.getFormatConditions qui renvoie désormais un tableau de type FormatConditionCollection.
## **APIs obsolètes**
### **Méthode Workbook.checkWriteProtectedPassword obsolète**
Avec la version 8.6.1, la méthode Workbook.checkWriteProtectedPassword a été marquée comme obsolète. Il est conseillé d'utiliser la méthode WorkbookSettings.WriteProtection.validatePassword qui peut accepter une valeur de type String en paramètre et renvoie un booléen si le mot de passe correspond au mot de passe prédéfini de la feuille de calcul.
{{< app/cells/assistant language="java" >}}
