---
title: Public API Changements dans Aspose.Cells 16.12.0
type: docs
weight: 360
url: /fr/net/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 16.11.0 à 16.12.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Filtrer les objets au moment du chargement**
Aspose.Cells 16.12.0 a exposé la classe LoadFilter avec la propriété LoadOptions.LoadFilter qui, ensemble, peut contrôler le type de données à charger lors de l'initialisation d'une instance de Workbook à partir d'un fichier modèle.

Voici un scénario d'utilisation simple pour charger uniquement les propriétés du document à partir d'un fichier de modèle.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



L'extrait suivant charge tout à partir d'une feuille de calcul existante, à l'exception des graphiques.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Le code suivant charge uniquement les données de cellule (avec les formules) et la mise en forme à partir d'une feuille de calcul existante.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



La classe LoadFilter permet également de personnaliser le processus de chargement selon les propriétés de la feuille de calcul. Afin de personnaliser le processus de chargement selon la feuille de calcul, il faut remplacer la méthode LoadFilter.StartSheet comme illustré ci-dessous.

**C#**

{{< highlight "csharp" >}}

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



L'extrait de code suivant utilise la classe CustomFilter définie ci-dessus.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Ajout de l'énumération FileFormatType.OTS**
Aspose.Cells 16.12.0 a ajouté l'entrée OTS à l'énumération FileFormatType afin de détecter le format des fichiers OTS.

L'extrait de code suivant utilise FileFormatType.OTS.

**C#**

{{< highlight "csharp" >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **Ajout de la propriété FontConfigs.PreferSystemFontSubstitutes**
Aspose.Cells 16.12.0 a exposé la propriété PreferSystemFontSubstitutes pour la classe FontConfigs. La propriété FontConfigs.PreferSystemFontSubstitutes est de type booléen, indiquant si le API doit d'abord utiliser le mécanisme de substitution de police du système, dans le cas où une police requise n'est pas présente et qu'aucune substitution pour la police particulière n'a été définie. La valeur par défaut de la propriété FontConfigs.PreferSystemFontSubstitutes est false.
### **Ajout de la propriété BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 a ajouté la propriété ScaleCrop à la classe BuiltInDocumentPropertyCollection. Le ScaleCrop indique le mode d'affichage de la vignette du document. La définition de cet élément sur true permet la mise à l'échelle de la vignette du document selon l'affichage, tandis que la définition sur false permet le recadrage de la vignette du document pour afficher la section qui correspond à l'affichage.
### **Ajout de la propriété BuiltInDocumentPropertyCollection.LinksUpToDate**
Aspose.Cells 16.12.0 a également exposé la propriété LinksUpToDate pour la classe BuiltInDocumentPropertyCollection. La propriété LinksUpToDate indique si les liens hypertexte d'un document sont à jour.
### **Ajout de la méthode Workbook.ExportXml**
Aspose.Cells 16.12.0 a exposé la méthode Workbook.ExportXml qui permet de stocker les données de carte XML dans le chemin de fichier spécifié. La méthode Workbook.ExportXml accepte 2 paramètres où le premier paramètre de type chaîne doit être le nom de la carte XML et le second paramètre doit être l'emplacement du chemin d'accès au fichier pour stocker les données XML.
### **Ajout de la méthode WorksheetCollection.CreateRange**
Aspose.Cells 16.12.0 a ajouté la méthode WorksheetCollection.CreateRange qui permet de créer une plage basée sur une adresse (référence de zone de cellule) et un index de feuille de calcul.

L'extrait de code suivant utilise la méthode WorksheetCollection.CreateRange pour créer une plage de cellules s'étendant de A1 à A2 dans la première feuille de calcul (par défaut).

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

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
