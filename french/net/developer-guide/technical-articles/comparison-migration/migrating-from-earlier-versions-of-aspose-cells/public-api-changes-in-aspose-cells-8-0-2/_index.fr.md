---
title: Public API Changements dans Aspose.Cells 8.0.2
type: docs
weight: 30
url: /fr/net/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.0.1 à 8.0.2, qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour, mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **Ajout de la propriété TextDirection à la classe Shape**
La classe Shape a une propriété TextDirection exposée qui peut être utilisée pour obtenir ou définir la direction du flux de texte pour l'objet Shape. La propriété TextDirection peut également être utilisée pour définir la direction de texte souhaitée pour les commentaires dans une feuille de calcul, comme illustré ci-dessous.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

var book = new Workbook();

//Get the first worksheet

var sheet = book.Worksheets[0];

//Add a comment to A1 cell

var comment = sheet.Comments[sheet.Comments.Add("A1")];

//Set its vertical alignment setting            

comment.CommentShape.TextVerticalAlignment  = TextAlignmentType.Center;

//Set its horizontal alignment setting

comment.CommentShape.TextHorizontalAlignment = TextAlignmentType.Right;

//Set the Text Direction - Right-to-Left

comment.CommentShape.TextDirection = TextDirectionType.RightToLeft;

//Set the Comment note

comment.Note = "This is my Comment Text. This is test";

//Save the Excel file

book.Save(myDir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Modification de la direction du texte du commentaire](/cells/fr/net/change-text-direction-of-the-comment/)

{{% /alert %}}
## **Ajout de la propriété ConvertFormulasData à la classe HTMLLoadOptions**
La propriété ConvertFormulasData a été ajoutée à la classe HTMLLoadOptions, afin de faciliter aux développeurs le chargement de formules Excel à partir de fichiers HTML. La propriété booléenne ConvertFormulasData indique s'il faut ou non convertir la chaîne en formule lorsque la valeur de la chaîne commence par le caractère '='.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.ConvertFormulasData = true;

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

La valeur par défaut de la propriété ConvertFormulasData est false.

{{% /alert %}}
## **Ajout de la propriété ImageOptions à la classe HtmlSaveOptions**
La propriété ImageOptions a été ajoutée à la classe HtmlSaveOptions. L'exposition de la propriété ImageOptions a permis aux développeurs de définir les préférences pour les images intégrées dans le code HTML lors de l'exportation des feuilles de calcul.
## **Propriété HtmlSaveOptions.ExportChartImageFormat obsolète**
HtmlSaveOptions.ExportChartImageFormat a été marqué comme obsolète à partir de Aspose.Cells for .NET 8.0.2. Il est conseillé d'utiliser plutôt HtmlSaveOptions.ImageOptions pour les paramètres de format d'image lors de l'exportation de feuilles de calcul au format HTML.
