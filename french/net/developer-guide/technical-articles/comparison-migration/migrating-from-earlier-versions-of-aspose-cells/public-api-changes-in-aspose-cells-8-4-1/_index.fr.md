---
title: Public API Changements dans Aspose.Cells 8.4.1
type: docs
weight: 140
url: /fr/net/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.4.0 à 8.4.1 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour,[classes ajoutées, etc.](/cells/fr/net/public-api-changes-in-aspose-cells-8-4-1/) et[classes supprimées, etc.](/cells/fr/net/public-api-changes-in-aspose-cells-8-4-1/), mais aussi une description de tout changement de comportement dans les coulisses du Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Mécanisme pour modifier la connexion à la base de données**
La classe Aspose.Cells.ExternalConnections.ExternalConnection contenait déjà la méthode et les propriétés pouvant être utilisées pour inspecter les détails de connexion à la base de données stockés dans une feuille de calcul. La plupart des propriétés associées à la classe Aspose.Cells.ExternalConnections.ExternalConnection étaient en lecture seule jusqu'à la version Aspose.Cells for .NET 8.4.1. Avec cette version, le API a également fourni le support pour manipuler les paramètres de connexion à la base de données.

L'extrait de code suivant montre comment modifier dynamiquement les paramètres de connexion à la base de données.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first data connection

Aspose.Cells.ExternalConnections.ExternalConnection conn = workbook.DataConnections[0];

//Change a few properties

conn.Name = "MyConnectionName";

conn.OdcFile = "MyDefaulConnection.odc";

conn.ConnectionDescription = "Test Connection";

conn.Credentials = Aspose.Cells.ExternalConnections.CredentialsMethodType.Prompt;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}



Voici quelques propriétés les plus importantes exposées par la classe {Aspose.Cells.ExternalConnections.ExternalConnection}}.

|**Nom de la propriété**|**Description**|
|:- |:- |
|Actualisation de l'arrière-plan|Indique si la connexion peut être actualisée en arrière-plan (de manière asynchrone).<br> true si l'utilisation préférée de la connexion consiste à actualiser de manière asynchrone en arrière-plan ;<br>false si l'utilisation préférée de la connexion consiste à actualiser de manière synchrone au premier plan.|
|ConnexionDescription|Spécifie la description de l'utilisateur pour cette connexion|
|ID de connexion|Spécifie l'identifiant unique de cette connexion.|
|Identifiants|Spécifie la méthode d'authentification à utiliser lors de l'établissement (ou du rétablissement) de la connexion.|
|Est supprimé|Indique si la connexion de classeur associée a été supprimée. vrai si le<br>la connexion a été supprimée ; sinon, faux.|
|Est nouveau| True si la connexion n'a pas été actualisée pour la première fois ; sinon, faux. Cette<br>L'état peut se produire lorsque l'utilisateur enregistre le fichier avant qu'une requête n'ait fini de renvoyer.|
|Rester en vie|Vrai lorsque l'application de feuille de calcul doit faire des efforts pour maintenir la connexion<br> ouvrir. Si false, l'application doit fermer la connexion après avoir récupéré le<br>renseignements.|
|Nom|Spécifie le nom de la connexion. Chaque connexion doit avoir un nom unique.|
|OdcFile| Spécifie le chemin d'accès complet au fichier de connexion externe à partir duquel cette connexion a été<br> établi. Si une connexion échoue lors d'une tentative d'actualisation des données et que reconnectionMethod=1,<br> puis l'application de feuille de calcul essaiera à nouveau en utilisant les informations du fichier de connexion externe<br>au lieu de l'objet de connexion incorporé dans le classeur.|
|OnlyUseConnectionFile| Indique si le tableur doit toujours et uniquement utiliser le<br> informations de connexion dans le fichier de connexion externe indiqué par l'attribut odcFile<br> lorsque la connexion est actualisée. Si false, alors l'application de feuille de calcul<br>doit suivre la procédure indiquée par l'attribut reconnectionMethod|
|Paramètres|Obtient ConnectionParameterCollection pour une requête ODBC ou Web.|
|Méthode de reconnexion|Spécifiez le type de méthode de reconnexion|
|RafraîchirInterne|Spécifie le nombre de minutes entre les actualisations automatiques de la connexion.|
|Rafraîchir au chargement|Vrai si cette connexion doit être actualisée lors de l'ouverture du fichier ; sinon, faux.|
|Enregistrer des données|Vrai si les données externes récupérées via la connexion pour remplir une table doivent être enregistrées<br>avec le cahier d'exercices; sinon, faux.|
|Enregistrer le mot de passe|True si le mot de passe doit être enregistré dans le cadre de la chaîne de connexion ; sinon, Faux.|
|Fichier source| Utilisé lorsque la source de données externe est basée sur un fichier. Lorsqu'une connexion à de telles données<br> source échoue, le tableur tente de se connecter directement à ce fichier. Peut-être<br>exprimé en URI ou en notation de chemin de fichier spécifique au système.|
|ID SSOI|Identifiant pour Single Sign On (SSO) utilisé pour l'authentification entre un intermédiaire<br>serveur spreadsheetML et la source de données externe.|
|Taper|Spécifie le type de source de données.|

### **Possibilité de formater la sous-chaîne du texte de DataLabels**
Aspose.Cells for .NET 8.4.1 a exposé la méthode DataLabels.Characters pour récupérer une instance de la classe FontSetting qui correspond à la sous-chaîne d'un ChartPoints.DataLabels. À son tour, l'instance de la classe FontSetting peut être utilisée pour formater la sous-chaîne des DataLabels avec différents paramètres de police et couleur.

L'extrait de code suivant montre comment utiliser la méthode DataLabels.Characters.

**C#**

{{< highlight "csharp" >}}

 //Create a workbook from source Excel file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Access the first chart inside the sheet

Aspose.Cells.Charts.Chart chart = worksheet.Charts[0];

//Access the data label of first series first point

Aspose.Cells.Charts.DataLabels labels = chart.NSeries[0].Points[0].DataLabels;

//Set data label text

labels.Text = "Rich Text Label";

//Set the font setting of the first 10 characters

Aspose.Cells.FontSetting settings = labels.Characters(0, 10);

settings.Font.Color = System.Drawing.Color.Red;

settings.Font.IsBold = true;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Possibilité de définir les dimensions d'image souhaitées pour l'exportation de feuilles de calcul et de graphiques**
Aspose.Cells for .NET 8.4.1 a exposé la méthode ImageOrPrintOptions.SetDesiredSize pour définir les dimensions de l'image résultante lors de l'exportation de feuilles de calcul et de graphiques vers des images. La méthode ImageOrPrintOptions.SetDesiredSize accepte deux paramètres de type entier, où le premier est la largeur souhaitée et le second la hauteur souhaitée.

L'extrait de code suivant montre comment définir les dimensions souhaitées lors de l'exportation de la feuille de calcul vers PNG.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set resultant image format

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Png;

//Set desired dimensions as 400x400

options.SetDesiredSize(400, 400);

//Render sheet to image

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.png"); 

{{< /highlight >}}

{{% alert color="primary" %}} 

La même propriété peut également être utilisée pour convertir des graphiques en images.

{{% /alert %}} 


### **Rendu des commentaires au PDF**
Avec la version v8.4.1, le Aspose.Cells API a fourni la propriété PageSetup.PrintComments et l'énumération PrintCommentsType afin de faciliter le rendu des commentaires lors de la conversion des feuilles de calcul au format PDF. L'énumération PrintCommentsType a les constantes suivantes.

- PrintCommentsType.PrintNoComments : les commentaires ne doivent pas être affichés.
- PrintCommentsType.PrintInPlace : les commentaires doivent être rendus là où ils sont placés.
- PrintCommentsType.PrintSheetEnd : les commentaires doivent être rendus à la fin de la feuille de calcul.

L'exemple de code suivant illustre l'utilisation de la propriété PageSetup.PrintComments pour restituer les commentaires à l'aide de toutes les valeurs d'énumération PrintCommentsType possibles.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of workbook

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Print no comments

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintNoComments;

//Save workbook in PDF format without comments

workbook.Save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintInPlace;

//Save workbook in PDF format while rendering comments in place

workbook.Save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintSheetEnd;

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.Save("printsheetend.pdf");

{{< /highlight >}}


### **Déplacer des feuilles de calcul dans Aspose.Cells.GridDesktop**
Aspose.Cells.GridDesktop fournit la méthode WorksheetCollection.MoveTo, qui peut être utilisée pour déplacer une feuille de calcul vers l'index spécifié. La méthode susmentionnée prend les index (basés sur zéro) de la feuille de calcul source et de la feuille de calcul de destination comme paramètres.

L'exemple de code suivant illustre l'utilisation de la propriété WorksheetCollection.MoveTo.

**C#**

{{< highlight "csharp" >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Ajout de la propriété Workbook.IsLicensed**
Aspose.Cells for .NET 8.4.1 a exposé le Workbook.IsLicensed qui pourrait être d'une grande aide pour déterminer si la licence a été chargée avec succès ou non. Si vous accédez à cette propriété avant de définir la licence, elle renverra false et vice versa, cependant, la licence doit être valide.

L'exemple de code suivant illustre l'utilisation de la propriété Workbook.IsLicensed.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object before setting a license

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook();

//Check if the license is loaded or not

if (!workbook.IsLicensed)

{

    //Set license

    Aspose.Cells.License license = new Aspose.Cells.License();

    lic.SetLicense(licPath);

}

else

{

    //do process

}

{{< /highlight >}}


### **Ajout de la propriété ImageOrPrintOptions.SVGFitToViewPort**
Aspose.Cells for .NET 8.4.1 a exposé la propriété SVGFitToViewPort pour la classe ImageOrPrintOptions qui peut être utilisée pour activer l'attribut viewBox pour le format de fichier SVG lors de l'exportation de feuilles de calcul ou de graphiques au format SVG. La valeur par défaut de cette propriété est false. Par conséquent, le fichier XML de base pour SVG généré sans définir la propriété susmentionnée n'inclura pas l'attribut viewBox.

L'exemple de code suivant illustre l'utilisation de la propriété ImageOrPrintOptions.SVGFitToViewPort.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set image format to SVG

options.SaveFormat = Aspose.Cells.SaveFormat.SVG;

//Set the SVGFitToViewPort to true

options.SVGFitToViewPort = true;

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.svg");

{{< /highlight >}}
## **API obsolètes**
### **Method Workbook.ValidateFormula Obsolète**
Utilisez la méthode Cell.Formula pour valider la formule.
