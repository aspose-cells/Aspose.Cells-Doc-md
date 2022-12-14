---
title: Public API Changements dans Aspose.Cells 16.12.0
type: docs
weight: 370
url: /fr/java/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 16.11.0 à 16.12.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Filtrer les objets au moment du chargement**
Aspose.Cells 16.12.0 a exposé la classe LoadFilter avec la propriété LoadOptions.LoadFilter qui, ensemble, peut contrôler le type de données à charger lors de l'initialisation d'une instance de Workbook à partir d'un fichier modèle.

Voici un scénario d'utilisation simple pour charger uniquement les propriétés du document à partir d'un fichier de modèle.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.DOCUMENT_PROPERTIES);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

L'extrait suivant charge tout à partir d'une feuille de calcul existante, à l'exception des graphiques.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Le code suivant charge uniquement les données de cellule (avec les formules) et la mise en forme à partir d'une feuille de calcul existante.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.CELL_DATA);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}
### **Ajout de l'énumération FileFormatType.OTS**
Aspose.Cells 16.12.0 a ajouté l'entrée OTS à l'énumération FileFormatType afin de détecter le format des fichiers OTS.

L'extrait de code suivant utilise FileFormatType.OTS.

**Java**

{{< highlight "csharp" >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **Ajout de la propriété BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 a ajouté la propriété ScaleCrop à la classe BuiltInDocumentPropertyCollection. Le ScaleCrop indique le mode d'affichage de la vignette du document. La définition de cet élément sur true permet la mise à l'échelle de la vignette du document selon l'affichage, tandis que la définition sur false permet le recadrage de la vignette du document pour afficher la section qui correspond à l'affichage.
### **Ajout de la propriété BuiltInDocumentPropertyCollection.LinksUpToDate**
 Aspose.Cells 16.12.0 a également exposé la propriété LinksUpToDate pour la classe BuiltInDocumentPropertyCollection. La propriété LinksUpToDate indique si les liens hypertexte d'un document sont à jour.
### **Ajout de la méthode Workbook.exportXml**
Aspose.Cells 16.12.0 a exposé la méthode Workbook.exportXml qui permet de stocker les données de carte XML dans le chemin de fichier spécifié. La méthode Workbook.exportXml accepte 2 paramètres où le premier paramètre de type chaîne doit être le nom de la carte XML et le second paramètre doit être l'emplacement du chemin d'accès au fichier pour stocker les données XML.
### **Ajout de la méthode WorksheetCollection.createRange**
Aspose.Cells 16.12.0 a ajouté la méthode WorksheetCollection.createRange qui permet de créer une plage basée sur une adresse (référence de zone de cellule) et un index de feuille de calcul.

L'extrait de code suivant utilise la méthode WorksheetCollection.createRange pour créer une plage de cellules s'étendant de A1 à A2 dans la première feuille de calcul (par défaut).

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

{{< /highlight >}}
## **API obsolètes**
### **Propriété LoadOptions.LoadDataOptions obsolète**
Veuillez utiliser la propriété LoadOptions.LoadFilter comme alternative.
### **Propriété LoadOptions.LoadDataFilterOptions obsolète**
Veuillez utiliser la propriété LoadOptions.LoadFilter à la place.
### **Propriété LoadOptions.OnlyLoadDocumentProperties obsolète**
Veuillez utiliser la propriété LoadOptions.LoadFilter comme alternative.
### **Propriété LoadOptions.LoadDataAndFormatting obsolète**
Veuillez utiliser la propriété LoadOptions.LoadFilter à la place.

{{% alert color="primary" %}} 

Des extraits de code pour toutes les API obsolètes ont été partagés ci-dessus.

{{% /alert %}}
## **API supprimées**
### **Propriété DataLabels.Rotation supprimée**
Veuillez utiliser la propriété DataLabels.RotationAngle à la place.
### **Propriété Title.Rotation supprimée**
Veuillez utiliser la propriété Title.RotationAngle comme alternative.
### **Propriété DataLabels.Background supprimée**
Il est conseillé d'utiliser à la place la propriété DataLabels.BackgroundMode.
### **Propriété DisplayUnitLabel.Rotation supprimée**
Veuillez envisager d'utiliser la propriété DisplayUnitLabel.RotationAngle pour atteindre le même objectif.
### **Méthode Title.getCharacters supprimée**
Veuillez utiliser la méthode Title.characters à la place.
