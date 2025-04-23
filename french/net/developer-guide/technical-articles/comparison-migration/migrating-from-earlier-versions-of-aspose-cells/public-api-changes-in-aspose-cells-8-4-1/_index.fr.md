---
title: Modifications de l API publique dans Aspose.Cells 8.4.1
type: docs
weight: 140
url: /fr/net/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.4.0 à la 8.4.1 qui pourraient intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, [les classes ajoutées etc.](/cells/fr/net/public-api-changes-in-aspose-cells-8-4-1/) et [les classes supprimées etc.](/cells/fr/net/public-api-changes-in-aspose-cells-8-4-1/), mais également une description de tout changement dans le comportement en arrière-plan d'Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Mécanisme de modification de la connexion à la base de données**
La classe Aspose.Cells.ExternalConnections.ExternalConnection contenait déjà la méthode & les propriétés qui pouvaient être utilisées pour inspecter les détails de connexion à la base de données stockés dans une feuille de calcul. La plupart des propriétés associées à la classe Aspose.Cells.ExternalConnections.ExternalConnection étaient en lecture seule jusqu'à la version Aspose.Cells for .NET 8.4.1. Avec cette version, l'API a fourni le support pour manipuler également les paramètres de connexion à la base de données.

Le code suivant montre comment modifier dynamiquement les paramètres de connexion à la base de données.

**C#**

{{< highlight csharp >}}

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



Voici quelques propriétés les plus importantes exposées par la classe {Aspose.Cells.ExternalConnections.ExternalConnection}.

|**Nom de la propriété**|**Description**|
| :- | :- |
|BackgroundRefresh|Indique si la connexion peut être rafraîchie en arrière-plan (asynchroniquement). <br>true si l'utilisation préférée de la connexion est de se rafraîchir de manière asynchrone en arrière-plan; <br>false si l'utilisation préférée de la connexion est de se rafraîchir de manière synchrone en premier plan.|
|DescriptionConnexion|Spécifie la description utilisateur pour cette connexion|
|IdConnexion|Spécifie l'identifiant unique de cette connexion.|
|Credentials|Spécifie la méthode d'authentification à utiliser lors de l'établissement (ou de la réétablissement) de la connexion.|
|IsDeleted|Indique si la connexion de classeur associée a été supprimée. Vrai si la connexion a été supprimée ; sinon, faux.|
|IsNew|Vrai si la connexion n'a pas été actualisée pour la première fois ; sinon, faux. Cet état peut survenir lorsque l'utilisateur enregistre le fichier avant qu'une requête ne finisse de renvoyer des résultats.|
|KeepAlive|Vrai lorsque l'application tableur doit faire des efforts pour maintenir la connexion ouverte. Lorsque faux, l'application doit fermer la connexion après avoir récupéré les informations.|
|Name|Spécifie le nom de la connexion. Chaque connexion doit avoir un nom unique.|
|OdcFile|Spécifie le chemin complet vers le fichier de connexion externe à partir duquel cette connexion a été créée. Si une connexion échoue lors d'une tentative de rafraîchissement des données, et reconnectionMethod=1, alors l'application tableur essaiera à nouveau en utilisant les informations obtenues à partir du fichier de connexion externe au lieu de l'objet de connexion intégré au classeur.|
|OnlyUseConnectionFile|Indique si l'application tableur doit toujours et uniquement utiliser les informations de connexion dans le fichier de connexion externe indiqué par l'attribut odcFile lorsque la connexion est rafraîchie. Si faux, alors l'application tableur doit suivre la procédure indiquée par l'attribut reconnectionMethod.|
|Parameters|Obtient la collection de paramètres de connexion pour une requête ODBC ou web.|
|ReConnectionMethod|Spécifie le type de méthode de reconnexion.|
|RefreshInternal|Spécifie le nombre de minutes entre les rafraîchissements automatiques de la connexion.|
|RefreshOnLoad|Vrai si cette connexion doit être actualisée lors de l'ouverture du fichier ; sinon, faux.|
|SaveData|Vrai si les données externes extraites via la connexion pour peupler une table doivent être enregistrées avec le classeur ; sinon, faux.|
|SavePassword|Vrai si le mot de passe doit être enregistré dans la chaîne de connexion ; sinon, faux.|
|SourceFile|Utilisé lorsque la source de données externe est basée sur un fichier. Lorsqu'une connexion à une telle source de données échoue, l'application tableur tente de se connecter directement à ce fichier. Peut être exprimé en notation URI ou en notation spécifique au système de fichiers.|
|SSOId|Identifiant pour Single Sign On (SSO) utilisé pour l'authentification entre un serveur de feuille de calcul intermédiaire et la source de données externe.|
|Type|Spécifie le type de source de données.|

### **Capacité à formater une sous-chaîne de texte des étiquettes de données.**
Aspose.Cells for .NET8.4.1 a exposé la méthode DataLabels.Characters pour récupérer une instance de la classe FontSetting correspondant à la sous-chaîne d'une étiquette de données de graphique. À son tour, l'instance de la classe FontSetting peut être utilisée pour formater la sous-chaîne des étiquettes de données avec différents paramètres de police et couleur.

Le fragment de code suivant montre comment utiliser la méthode DataLabels.Characters.

**C#**

{{< highlight csharp >}}

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


### **Capacité à définir les dimensions d'image souhaitées pour l'exportation de feuilles de calcul et de graphiques.**
Aspose.Cells for .NET 8.4.1 a exposé la méthode ImageOrPrintOptions.SetDesiredSize pour définir les dimensions de l'image résultante lors de l'exportation de feuilles de calcul et de graphiques en images. La méthode ImageOrPrintOptions.SetDesiredSize accepte deux paramètres de type entier, où le premier est la largeur souhaitée et le second est la hauteur souhaitée.

L'exemple de code suivant montre comment définir les dimensions souhaitées lors de l'exportation de la feuille de calcul en PNG.

**C#**

{{< highlight csharp >}}

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

Cette même propriété peut également être utilisée pour convertir des graphiques en images.

{{% /alert %}} 


### **Rendu des commentaires en PDF**
Avec la sortie de la version 8.4.1, l'API Aspose.Cells a fourni la propriété PageSetup.PrintComments & l'énumération PrintCommentsType afin de faciliter le rendu des commentaires lors de la conversion de feuilles de calcul au format PDF. L'énumération PrintCommentsType a les constantes suivantes.

- PrintCommentsType.PrintNoComments: Les commentaires ne doivent pas être rendus.
- PrintCommentsType.PrintInPlace: Les commentaires doivent être rendus là où ils sont placés.
- PrintCommentsType.PrintSheetEnd: Les commentaires doivent être rendus à la fin de la feuille de calcul.

Le code d'exemple suivant démontre l'utilisation de la propriété PageSetup.PrintComments pour rendre les commentaires en utilisant toutes les valeurs d'énumération possibles de PrintCommentsType.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells.GridDesktop fournit la méthode WorksheetCollection.MoveTo, qui peut être utilisée pour déplacer une feuille de calcul vers l'index spécifié. Cette méthode prend les index (basés sur zéro) de la feuille de calcul source et de la feuille de calcul de destination en tant que paramètres.

Le code d'exemple suivant montre l'utilisation de la propriété WorksheetCollection.MoveTo.

**C#**

{{< highlight csharp >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Propriété Workbook.IsLicensed ajoutée**
Aspose.Cells for .NET 8.4.1 a exposé la propriété Workbook.IsLicensed qui pourrait être d'une grande aide pour déterminer si la licence a été chargée avec succès ou non. Si vous accédez à cette propriété avant de définir la licence, elle renverra false et vice versa, cependant, la licence devrait être valide.

Le code d'exemple suivant montre l'utilisation de la propriété Workbook.IsLicensed.

**C#**

{{< highlight csharp >}}

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


### **Propriété ImageOrPrintOptions.SVGFitToViewPort ajoutée**
Aspose.Cells for .NET 8.4.1 a exposé la propriété SVGFitToViewPort pour la classe ImageOrPrintOptions qui peut être utilisée pour activer l'attribut viewBox pour le format de fichier SVG lors de l'exportation de feuilles de calcul ou de graphiques au format SVG. La valeur par défaut de cette propriété est false, par conséquent, le XML de base pour le fichier SVG généré sans définir la propriété susmentionnée n'inclura pas l'attribut viewBox.

Le code d'exemple suivant démontre l'utilisation de la propriété ImageOrPrintOptions.SVGFitToViewPort.

**C#**

{{< highlight csharp >}}

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
### **Méthode Workbook.ValidateFormula obsolète**
Utilisez la méthode Cell.Formula pour valider la formule.
{{< app/cells/assistant language="csharp" >}}
