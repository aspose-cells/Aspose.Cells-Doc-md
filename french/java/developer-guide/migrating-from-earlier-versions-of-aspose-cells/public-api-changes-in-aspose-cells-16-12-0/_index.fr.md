---
title: Changements d API publics dans Aspose.Cells 16.12.0
type: docs
weight: 370
url: /fr/java/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 16.11.0 à la version 16.12.0 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement de nouvelles méthodes publiques et mises à jour, des classes ajoutées et supprimées, etc., mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Filtrer les objets au chargement**
Aspose.Cells 16.12.0 a exposé la classe LoadFilter ainsi que la propriété LoadOptions.LoadFilter qui ensemble peuvent contrôler le type de données à charger lors de l'initialisation d'une instance de Workbook à partir d'un fichier modèle.

Voici un scénario d'utilisation simple pour charger uniquement les propriétés du document à partir d'un fichier modèle.

**Java**

{{< highlight csharp >}}

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

L'extrait suivant charge tout sauf les graphiques à partir d'une feuille de calcul existante.

**Java**

{{< highlight csharp >}}

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

Le code suivant charge uniquement les données de cellule (ainsi que les formules) et la mise en forme d'une feuille de calcul existante.

**Java**

{{< highlight csharp >}}

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

L'extrait suivant utilise FileFormatType.OTS.

**Java**

{{< highlight csharp >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **Ajout de la propriété ScaleCrop de BuiltInDocumentPropertyCollection**
Aspose.Cells 16.12.0 a ajouté la propriété ScaleCrop à la classe BuiltInDocumentPropertyCollection. ScaleCrop indique le mode d'affichage de la vignette du document. Le fait de définir cet élément sur true permet de mettre à l'échelle la vignette du document conformément à l'affichage, tandis que le fait de le définir sur false permet de recadrer la vignette du document pour afficher la section qui correspond à l'affichage.
### **Ajout de la propriété LinksUpToDate de BuiltInDocumentPropertyCollection**
Aspose.Cells 16.12.0 a également exposé la propriété LinksUpToDate pour la classe BuiltInDocumentPropertyCollection. La propriété LinksUpToDate indique si les hyperliens dans un document sont à jour. 
### **Ajout de la méthode exportXml de Workbook**
Aspose.Cells 16.12.0 a exposé la méthode Workbook.exportXml qui permet de stocker les données de carte XML dans un emplacement de fichier spécifié. La méthode Workbook.exportXml accepte 2 paramètres où le premier paramètre de type string doit être le nom de la carte XML et le deuxième paramètre doit être l'emplacement du chemin du fichier pour stocker les données XML.
### **Ajout de la méthode createRange de WorksheetCollection**
Aspose.Cells 16.12.0 a ajouté la méthode WorksheetCollection.createRange qui permet de créer une plage basée sur une adresse (référence de zone de cellules) et l'index de la feuille de calcul.

Le snippet suivant utilise la méthode WorksheetCollection.createRange pour créer une plage de cellules s'étendant de A1 à A2 dans la première feuille de calcul (par défaut).

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

{{< /highlight >}}
## **APIs obsolètes**
### **Propriété Obsoleted LoadOptions.LoadDataOptions**
Veuillez utiliser la propriété LoadOptions.LoadFilter comme alternative.
### **Propriété Obsoleted LoadOptions.LoadDataFilterOptions**
Veuillez utiliser la propriété LoadOptions.LoadFilter à la place.
### **Propriété Obsoleted LoadOptions.OnlyLoadDocumentProperties**
Veuillez utiliser la propriété LoadOptions.LoadFilter comme alternative.
### **Propriété Obsoleted LoadOptions.LoadDataAndFormatting**
Veuillez utiliser la propriété LoadOptions.LoadFilter à la place.

{{% alert color="primary" %}} 

Des extraits de code pour toutes les APIs obsolètes ont été partagés ci-dessus.

{{% /alert %}}
## **APIs supprimées**
### **Propriété Deleted DataLabels.Rotation**
Veuillez utiliser la propriété DataLabels.RotationAngle à la place.
### **Propriété Deleted Title.Rotation**
Veuillez utiliser la propriété Title.RotationAngle comme alternative.
### **Propriété Deleted DataLabels.Background**
Il est conseillé d'utiliser la propriété DataLabels.BackgroundMode à la place.
### **Propriété Deleted DisplayUnitLabel.Rotation**
Veuillez envisager d'utiliser la propriété DisplayUnitLabel.RotationAngle pour atteindre le même objectif.
### **Méthode Title.getCharacters supprimée**
Veuillez utiliser la méthode Title.characters à la place.
