---
title: Changements d API publics dans Aspose.Cells 8.7.0
type: docs
weight: 230
url: /fr/net/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.6.3 à la version 8.7.0 qui peuvent être d'intérêt pour les développeurs de modules/applications. Il inclut non seulement les nouvelles et mises à jour des méthodes publiques, des classes ajoutées et supprimées, etc., mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Prise en charge de la signature numérique, de la détection et de l'extraction de projets VBA**
Cette version de Aspose.Cells for .NET a exposé de nouvelles propriétés et méthodes pour aider les utilisateurs dans des tâches telles que la signature numérique d'un projet VBA, la détection si un projet VBA est signé et valide. De plus, la nouvelle API permet d'extraire le certificat sous forme de données brutes à partir d'un projet VBA signé numériquement dans un classeur.
###### **Signature numérique d'un projet VBA**
Aspose.Cells for .NET 8.7.0 a exposé la méthode VbaProject.Sign qui peut être utilisée pour signer numériquement le projet VBA dans un classeur.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **Détection du projet VBA signé numériquement**
La nouvelle propriété VbaProject.IsSigned permet de [détecter si le projet VBA dans un classeur est signé numériquement](/cells/fr/net/check-if-vba-code-is-signed/). La propriété VbaProject.IsSigned est de type booléen, elle retourne true si le projet VBA est signé numériquement et vice versa.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    Console.WriteLine("VbaProject is digitally signed");

}

else

{

    Console.WriteLine("VbaProject is not digitally signed");

}

{{< /highlight >}}


###### **Extraction de la signature numérique du projet VBA**
Cette révision de l'API a également exposé la propriété VbaProject.CertRawData qui permet d'[extraire les données brutes du certificat numérique du projet VBA](/cells/fr/net/export-vba-certificate-to-file-or-stream/). La propriété VbaProject.CertRawData est de type tableau d'octets, elle contiendra les données brutes du certificat si le projet VBA est signé numériquement, sinon ladite propriété sera nulle.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **Valider la signature numérique du projet VBA**
Un autre ajout à l'API publique est la propriété VbaProject.IsValidSigned qui pourrait être utile pour [valider la signature numérique du projet VBA](/cells/fr/net/check-if-digital-signature-of-vba-code-is-valid/). Cette propriété retourne true si la signature numérique est valide et false si la signature est invalide.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    //Check if signature is valid

    if (vbaProject.IsValidSigned)

    {

        Console.WriteLine("VbaProject is digitally signed & signature is valid");

    }

}

{{< /highlight >}}


### **Méthode Added Protection.VerifyPassword**
Aspose.Cells for .NET 8.7.0 a exposé la méthode Protection.VerifyPassword qui peut être utilisée pour [vérifier le mot de passe utilisé pour protéger la feuille de calcul](/cells/fr/net/verify-password-used-to-protect-the-worksheet/). Cette méthode accepte une instance de chaîne en tant que paramètre et retourne true si le mot de passe spécifié correspond au mot de passe utilisé pour protéger la feuille de calcul.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Verify the password for Worksheet

if (protection.VerifyPassword(password))

{

    Console.WriteLine("Password has matched");

}

else

{

    Console.WriteLine("Password did not match");

}

{{< /highlight >}}


### **Propriété Added Protection.IsProtectedWithPassword**
Cette version de l'API Aspose.Cells for .NET a également exposé la propriété Protection.IsProtectedWithPassword qui peut être utile pour [détecter si une feuille de calcul est protégée par mot de passe ou non](/cells/fr/net/detect-if-worksheet-is-password-protected/).

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Check if Worksheet is password protected

if (protection.IsProtectedWithPassword)

{

    Console.WriteLine("Worksheet is password protected");

}

else

{

    Console.WriteLine("Worksheet is not password protected");

}

{{< /highlight >}}


### **Propriété ColorScale.Is3ColorScale ajoutée**
Aspose.Cells for .NET 8.7.0 a exposé la propriété ColorScale.Is3ColorScale qui peut être utilisée pour créer un format conditionnel à échelle de 2 couleurs. La propriété ColorScale.Is3ColorScale est de type booléen avec une valeur par défaut de true, ce qui signifie que le format conditionnel sera par défaut à échelle de 3 couleurs. Cependant, passer la propriété ColorScale.Is3ColorScale à false va [générer un format conditionnel à échelle de 2 couleurs](/cells/fr/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

var sheet = book.Worksheets[0];

//Add FormatConditions to the collection

int index = sheet.ConditionalFormattings.Add();

//Access newly added formatConditionCollection via its index

var formatConditionCollection = sheet.ConditionalFormattings[index];

//Create a CellArea on which conditional formatting rule will be applied

var cellArea = CellArea.CreateCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.AddArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.AddCondition(FormatConditionType.ColorScale);

//Access newly added format condition via its index

var formatCondition = formatConditionCollection[index];

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.ColorScale.Is3ColorScale = false;

//Set other necessary properties

{{< /highlight >}}


### **Propriété HasFormula ajoutée à TxtLoadOptions**
Aspose.Cells for .NET 8.7.0 a apporté un support pour [identifier et analyser les formules lors du chargement de fichiers CSV/TXT contenant des données simples délimitées](/cells/fr/net/load-or-import-csv-file-with-formulas/). La nouvelle propriété TxtLoadOptions.HasFormula lorsque définie sur true dirige l'API pour analyser les formules du fichier délimité d'entrée et les définir aux cellules pertinentes sans nécessiter de traitement supplémentaire.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of TxtLoadOptions

var options = new TxtLoadOptions();

//Set HasFormula property to true

options.HasFormula = true;

//Set the Separator property as desired

options.Separator = ',';

//Load the CSV/TXT file using the instance of TxtLoadOptions

var book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.CalculateFormula();

//Write result in any of the supported formats

book.Save(outFilePath);

{{< /highlight >}}


### **Propriété DataLabels.IsResizeShapeToFitText ajoutée**
Une autre fonctionnalité utile exposée par la version Aspose.Cells for .NET 8.7.0 est la propriété DataLabels.IsResizeShapeToFitText qui peut activer la fonctionnalité [Redimensionner la forme pour s'adapter au texte](/cells/fr/net/resize-chart-s-data-label-shape-to-fit-text/) de l'application Excel pour les étiquettes de données du graphique.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook containing the Chart

var book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

var sheet = book.Worksheets[0];

//Access the desired Chart via its index or name

var chart = sheet.Charts[0];

//Access the DataLabels of desired NSeries

var labels = chart.NSeries[0].DataLabels;

//Set ResizeShapeToFitText property to true

labels.IsResizeShapeToFitText = true;

//Calculate Chart

chart.Calculate();

{{< /highlight >}}


### **Propriété PdfSaveOptions.OptimizationType ajoutée**
Aspose.Cells for .NET 8.7.0 a exposé la propriété PdfSaveOptions.OptimizationType ainsi que l'énumération PdfOptimizationType afin de faciliter aux utilisateurs de [choisir l'algorithme d'optimisation souhaité lors de l'exportation des feuilles de calcul au format PDF](/cells/fr/net/save-excel-into-pdf-with-standard-or-minimum-size/). Il y a 2 valeurs possibles pour la propriété PdfSaveOptions.OptimizationType comme détaillé ci-dessous.

1. PdfOptimizationType.MinimumSize : La qualité est compromise pour la taille du fichier résultant.
1. PdfOptimizationType.Standard : La qualité n'est pas compromise donc la taille du fichier résultant sera grande.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create an instance of PdfSaveOptions

var pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.OptimizationType = PdfOptimizationType.MinimumSize;

//Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.Save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
## **APIs supprimées**
### **Propriété Workbook.SaveOptions Supprimée**
La propriété Workbook.SaveOptions a été marquée obsolète il y a un certain temps. Avec cette version, elle a été complètement supprimée de l'API publique, il est donc conseillé d'utiliser la méthode Workbook.Save(Stream, SaveOptions) ou Workbook.Save(string, SaveOptions) en tant qu'alternative.
