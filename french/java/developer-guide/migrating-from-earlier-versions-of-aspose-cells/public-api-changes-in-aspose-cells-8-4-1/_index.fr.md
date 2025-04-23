---
title: Modifications de l API publique dans Aspose.Cells 8.4.1
type: docs
weight: 150
url: /fr/java/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.4.0 à 8.4.1 qui pourraient intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques, [les classes ajoutées, etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-4-1/) et [les classes supprimées, etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-4-1/), mais aussi une description de tout changement dans le comportement en coulisse dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Mécanisme de modification de la connexion à la base de données**
La classe com.aspose.cells.ExternalConnection contenait déjà la méthode et les propriétés qui pouvaient être utilisées pour inspecter les détails de la connexion de base de données stockés dans une feuille de calcul. La plupart des propriétés associées à la classe ExternalConnection étaient en lecture seule jusqu'à la version Aspose.Cells for Java 8.4.1. Avec cette version, l'API a fourni le support pour manipuler les paramètres de connexion à la base de données.

Le code suivant montre comment modifier dynamiquement les paramètres de connexion à la base de données.

**Java**

{{< highlight csharp >}}

 //Create workbook object

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first data connection

com.aspose.cells.ExternalConnection conn = workbook.getDataConnections().get(0);

//Change a few properties

conn.setName("MyConnectionName");

conn.setOdcFile("MyDefaulConnection.odc");

conn.setConnectionDescription("Test Connection");

conn.setCredentials(com.aspose.cells.CredentialsMethodType.PROMPT);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

Voici quelques propriétés les plus importantes exposées par la classe {ExternalConnection}.

|**Nom de la propriété** |**Description** |
| :- | :- |
|BackgroundRefresh |Indique si la connexion peut être rafraîchie en arrière-plan (asynchrone). <br>true si l'utilisation préférée de la connexion est de se rafraîchir de manière asynchrone en arrière-plan; <br>false si l'utilisation préférée de la connexion est de se rafraîchir de manière synchrone en premier plan.
|ConnectionDescription |Spécifie la description de l'utilisateur pour cette connexion
|ConnectionId |Spécifie l'identifiant unique de cette connexion
|Credentials |Spécifie la méthode d'authentification à utiliser lors de l'établissement (ou de la réétablissement) de la connexion
|IsDeleted |Indique si la connexion de classeur associée a été supprimée. vrai si la connexion a été supprimée; sinon, faux.
|IsNew |Vrai si la connexion n'a pas été rafraîchie pour la première fois; sinon, faux. Cet état peut se produire lorsque l'utilisateur enregistre le fichier avant qu'une requête ait fini de retourner.
|KeepAlive |Vrai lorsque l'application de feuille de calcul doit faire des efforts pour maintenir la connexion ouverte. Lorsque c'est faux, l'application doit fermer la connexion après avoir récupéré les informations.
|Name |Spécifie le nom de la connexion. Chaque connexion doit avoir un nom unique.
|OdcFile |Spécifie le chemin complet vers le fichier de connexion externe à partir duquel cette connexion a été créée. Si une connexion échoue lors d'une tentative de rafraîchissement des données, et reconnectionMethod=1, alors l'application de feuille de calcul tentera à nouveau en utilisant les informations du fichier de connexion externe au lieu de l'objet de connexion intégré dans le classeur.
|OnlyUseConnectionFile |Indique si l'application de feuille de calcul doit toujours et uniquement utiliser les informations de connexion dans le fichier de connexion externe indiqué par l'attribut odcFile lorsque la connexion est rafraîchie. Si c'est faux, alors l'application de feuille de calcul doit suivre la procédure indiquée par l'attribut reconnectionMethod
|Parameters |Obtient ConnectionParameterCollection pour une requête ODBC ou web
|ReConnectionMethod |Spécifie le type de reconnectionMethod
|RefreshInternal|Spécifie le nombre de minutes entre les rafraîchissements automatiques de la connexion. |
|RefreshOnLoad |Vrai si cette connexion doit être actualisée lors de l'ouverture du fichier ; sinon, faux. |
|SaveData |Vrai si les données externes récupérées via la connexion pour alimenter un tableau doivent être enregistrées avec le classeur ; sinon, faux. |
|SavePassword |Vrai si le mot de passe doit être enregistré dans la chaîne de connexion ; sinon, faux. |
|SourceFile |Utilisé lorsque la source de données externe est basée sur un fichier. Lorsqu'une connexion à une telle source de données échoue, l'application de tableur tente de se connecter directement à ce fichier. Peut être exprimé en URI ou en notation de chemin de fichier spécifique au système. |
|SSOId|Identifiant pour Single Sign On (SSO) utilisé pour l'authentification entre un serveur intermédiaire de spreadsheetML et la source de données externe. |
|Type |Spécifie le type de source de données. |

### **Capacité à formater une sous-chaîne de texte des étiquettes de données.**
Aspose.Cells for Java 8.4.1 a exposé la méthode DataLabels.characters pour récupérer une instance de la classe FontSetting qui correspond à la sous-chaîne des DataLabels d'un ChartPoints. À son tour, l'instance de la classe FontSetting peut être utilisée pour formater la sous-chaîne des DataLabels avec différents paramètres de police et de couleur.

L'exemple de code suivant montre comment utiliser la méthode DataLabels.characters.

**Java**

{{< highlight csharp >}}

 //Create a workbook from source Excel file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first chart inside the sheet

com.aspose.cells.Chart chart = worksheet.getCharts().get(0);

//Access the data label of first series first point

com.aspose.cells.DataLabels labels = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

//Set data label text

labels.setText("Rich Text Label");

//Set the font setting of the first 10 characters

com.aspose.cells.FontSetting settings = labels.characters(0, 10);

settings.getFont().setColor(com.aspose.cells.Color.getRed());

settings.getFont().setBold(true);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Capacité à définir les dimensions d'image souhaitées pour l'exportation de feuilles de calcul et de graphiques.**
Aspose.Cells for Java 8.4.1 a exposé la méthode ImageOrPrintOptions.setDesiredSize pour définir les dimensions de l'image résultante lors de l'exportation de feuilles de calcul et de graphiques en images. La méthode ImageOrPrintOptions.setDesiredSize accepte deux paramètres de type entier, le premier étant la largeur souhaitée et le second la hauteur souhaitée.

L'exemple de code suivant montre comment définir les dimensions souhaitées lors de l'exportation de la feuille de calcul en PNG.

**Java**

{{< highlight csharp >}}

 com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set resultant image format

options.setImageFormat(com.aspose.cells.ImageFormat.getPng());

//Set desired dimensions as 400x400

options.setDesiredSize(400, 400);

//Render sheet to image

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.png");

{{< /highlight >}}

{{% alert color="primary" %}} 

La même méthode peut également être utilisée pour convertir des graphiques en images. 

{{% /alert %}} 

### **Rendu des commentaires en PDF**
Avec la sortie de la version 8.4.1, l'API Aspose.Cells a fourni la propriété PageSetup.PrintComments & l'énumération PrintCommentsType afin de faciliter le rendu des commentaires lors de la conversion de feuilles de calcul au format PDF. L'énumération PrintCommentsType a les constantes suivantes. 

- PrintCommentsType.PRINT_NO_COMMENTS: Les commentaires ne doivent pas être rendus.
- PrintCommentsType.PRINT_IN_PLACE: Les commentaires doivent être rendus à l'endroit où ils sont placés.
- PrintCommentsType.PRINT_SHEET_END: Les commentaires doivent être rendus à la fin de la feuille de calcul.

Le code d'exemple suivant démontre l'utilisation de la propriété PageSetup.PrintComments pour rendre les commentaires en utilisant toutes les valeurs d'énumération possibles de PrintCommentsType.

**Java**

{{< highlight csharp >}}

 //Create an instance of workbook

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Print no comments

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_NO_COMMENTS);

//Save workbook in PDF format without comments

workbook.save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_IN_PLACE);

//Save workbook in PDF format while rendering comments in place

workbook.save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_SHEET_END);

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.save("printsheetend.pdf");

{{< /highlight >}}

### **Propriété Workbook.isLicensed ajoutée**
Aspose.Cells for Java 8.4.1 a exposé la propriété Workbook.isLicensed qui pourrait être d'une grande aide pour déterminer si la licence a été chargée avec succès ou non. Si vous accédez à cette propriété avant de définir la licence, elle renverra faux et vice versa, cependant, la licence devrait être valide.

Le code d'exemple suivant démontre l'utilisation de la propriété Workbook.isLicensed.

**Java**

{{< highlight csharp >}}

 //Create workbook object before setting a license

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook();

//Check if the license is loaded or not

if (!workbook.isLicensed())

{

	//Set license

	com.aspose.cells.License license = new com.aspose.cells.License();

	lic.SetLicense(licPath);

}

else

{

  //do process

}

{{< /highlight >}}

### **Propriété ImageOrPrintOptions.SVGFitToViewPort ajoutée**
Aspose.Cells for Java 8.4.1 a exposé la propriété SVGFitToViewPort pour la classe ImageOrPrintOptions qui peut être utilisée pour activer l'attribut viewBox pour le format de fichier SVG lors de l'exportation de feuilles de calcul ou de graphiques au format SVG. La valeur par défaut de cette propriété est false, donc le XML de base pour le fichier SVG généré sans définir ladite propriété n'inclura pas l'attribut viewBox.

Le code d'exemple suivant démontre l'utilisation de la propriété ImageOrPrintOptions.SVGFitToViewPort.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set image format to SVG

options.setSaveFormat(com.aspose.cells.SaveFormat.SVG);

//Set the SVGFitToViewPort to true

options.setSVGFitToViewPort(true);

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.svg");

{{< /highlight >}}
## **APIs obsolètes**
### **Méthode Workbook.validateFormula obsolète**
Utilisez la propriété Cell.Formula pour valider la formule.
{{< app/cells/assistant language="java" >}}
