---
title: Public API Changements dans Aspose.Cells 8.6.1
type: docs
weight: 210
url: /fr/java/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.6.0 à 8.6.1 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour, des classes ajoutées, mais également une description de tout changement de comportement en coulisse dans Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge du type de cible de lien HTML**
 Cette version de Aspose.Cells for Java API a exposé une énumération à savoir HtmlLinkTargetType avec une nouvelle propriété HtmlSaveOptions.LinkTargetType qui, ensemble, permet de[définir le type de cible pour les liens dans la feuille de calcul lors de la conversion au format HTML](/cells/fr/java/change-the-html-link-target-type/). Les valeurs possibles de l'énumération HtmlLinkTargetType sont les suivantes, où la valeur par défaut est SELF.

1. HtmlLinkTargetType.BLANK : ouvre le document/la page liés dans une nouvelle fenêtre ou un nouvel onglet.
1. HtmlLinkTargetType.PARENT : Ouvre le document/la page liés dans le cadre parent.
1. HtmlLinkTargetType.SELF : Ouvre le document/la page lié(e) dans le même cadre où le lien a été cliqué.
1. HtmlLinkTargetType.TOP : Ouvre le document/la page lié(e) dans le corps entier de la fenêtre.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells for Java 8.6.1 a exposé une autre surcharge de la méthode VbaModuleCollection.remove qui peut désormais accepter une instance de Worksheet pour supprimer tous les modules VBA associés à la Worksheet spécifiée.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Méthode RangeCollection.add ajoutée**
Aspose.Cells for Java 8.6.1 a exposé la méthode RangeCollection.Add qui peut être utilisée pour ajouter des objets Range à la collection de plages pour une feuille de calcul particulière.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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
 La méthode Cell.setCharacters peut être utilisée pour[mettre à jour les parties du texte enrichi](/cells/fr/java/access-and-update-the-portions-of-rich-text-of-cell/) d'un objet Cell donné. La méthode Cell.getCharacters doit être utilisée pour accéder aux parties du texte, puis les modifications peuvent être effectuées à l'aide de la méthode Cell.setCharacters alors que la**obtenir** La méthode renvoie un tableau d'objets FontSetting qui peuvent être manipulés pour définir diverses propriétés nom de police, couleur de police, gras, etc. et**Positionner** peut être utilisée pour appliquer les modifications.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **Propriété VbaProject.isSigned ajoutée**
 Aspose.Cells for Java 8.6.1 a exposé la propriété VbaProject.isSigned qui peut être utilisée pour[tester si un VbaProject dans un classeur est signé ou non](/cells/fr/java/check-if-vba-project-in-a-workbook-is-signed/)La propriété de type booléen renvoie true si le projet est signé.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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
## **API modifiées**
### **Méthode Cell.getFormatConditions modifiée**
Avec la version v8.6.1, le Aspose.Cells for Java API a modifié le type de retour de la méthode Cell.getFormatConditions qui renvoie désormais un tableau de type FormatConditionCollection.
## **API obsolètes**
### **Méthode Workbook.checkWriteProtectedPassword Obsolète**
Avec la version v8.6.1, la méthode Workbook.checkWriteProtectedPassword a été marquée comme dépréciée. Il est conseillé d'utiliser la méthode WorkbookSettings.WriteProtection.validatePassword qui peut accepter une valeur String comme paramètre et renvoie Boolean si le mot de passe correspond au mot de passe prédéfini de la feuille de calcul.
