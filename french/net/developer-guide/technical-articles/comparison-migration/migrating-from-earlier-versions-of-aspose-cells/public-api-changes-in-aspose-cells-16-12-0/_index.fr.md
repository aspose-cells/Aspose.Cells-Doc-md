---
title: Changements d API publics dans Aspose.Cells 16.12.0
type: docs
weight: 360
url: /fr/net/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 16.11.0 à la version 16.12.0 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement de nouvelles méthodes publiques et mises à jour, des classes ajoutées et supprimées, etc., mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Filtrer les objets au chargement**
Aspose.Cells 16.12.0 a exposé la classe LoadFilter ainsi que la propriété LoadOptions.LoadFilter qui ensemble peuvent contrôler le type de données à charger lors de l'initialisation d'une instance de Workbook à partir d'un fichier modèle.

Voici un scénario d'utilisation simple pour charger uniquement les propriétés du document à partir d'un fichier modèle.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



L'extrait suivant charge tout sauf les graphiques à partir d'une feuille de calcul existante.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Le code suivant charge uniquement les données de cellule (ainsi que les formules) et la mise en forme d'une feuille de calcul existante.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



La classe LoadFilter permet également de personnaliser le processus de chargement en fonction des propriétés de la feuille de calcul. Pour personnaliser le processus de chargement par feuille de calcul, il faut substituer la méthode LoadFilter.StartSheet comme démontré ci-dessous.

**C#**

{{< highlight csharp >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}



Le snippet suivant utilise la classe CustomFilter définie ci-dessus.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Ajout de l'énumération FileFormatType.OTS**
Aspose.Cells 16.12.0 a ajouté l'entrée OTS à l'énumération FileFormatType afin de détecter le format des fichiers OTS.

L'extrait suivant utilise FileFormatType.OTS.

**C#**

{{< highlight csharp >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **Propriété PreferSystemFontSubstitutes ajoutée à FontConfigs.**
Aspose.Cells 16.12.0 a exposé la propriété PreferSystemFontSubstitutes pour la classe FontConfigs. La propriété FontConfigs.PreferSystemFontSubstitutes est de type booléen, indiquant si l'API doit d'abord utiliser le mécanisme de substitution de polices du système, au cas où une police requise n'est pas présente et aucune substitution pour cette police particulière n'a été définie. La valeur par défaut de la propriété FontConfigs.PreferSystemFontSubstitutes est fausse.
### **Ajout de la propriété ScaleCrop de BuiltInDocumentPropertyCollection**
Aspose.Cells 16.12.0 a ajouté la propriété ScaleCrop à la classe BuiltInDocumentPropertyCollection. ScaleCrop indique le mode d'affichage de la vignette du document. Le fait de définir cet élément sur true permet de mettre à l'échelle la vignette du document conformément à l'affichage, tandis que le fait de le définir sur false permet de recadrer la vignette du document pour afficher la section qui correspond à l'affichage.
### **Ajout de la propriété LinksUpToDate de BuiltInDocumentPropertyCollection**
Aspose.Cells 16.12.0 a également exposé la propriété LinksUpToDate pour la classe BuiltInDocumentPropertyCollection. La propriété LinksUpToDate indique si les hyperliens dans un document sont à jour.
### **Méthode ExportXml ajoutée à Workbook.**
Aspose.Cells 16.12.0 a exposé la méthode Workbook.ExportXml qui permet de stocker les données de la carte XML à l'emplacement de fichier spécifié. La méthode Workbook.ExportXml accepte 2 paramètres où le premier paramètre de type string doit être le nom de la carte XML et le second paramètre doit être l'emplacement de fichier pour stocker les données XML.
### **Méthode CreateRange ajoutée à WorksheetCollection.**
Aspose.Cells 16.12.0 a ajouté la méthode CreateRange à la classe WorksheetCollection qui permet de créer une plage basée sur une adresse (référence de plage de cellules) et l'index de feuille de calcul.

Le fragment suivant utilise la méthode CreateRange de WorksheetCollection pour créer une plage de cellules s'étendant de A1 à A2 dans la première feuille de calcul (par défaut).

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

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
