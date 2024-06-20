---
title: Changements de l API publique dans Aspose.Cells 8.0.2
type: docs
weight: 30
url: /fr/net/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.0.1 à la 8.0.2, qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement de nouvelles méthodes publiques et mises à jour, mais aussi une description de tout changement dans le comportement en arrière-plan d'Aspose.Cells.

{{% /alert %}} 
## **Propriété TextDirection ajoutée à la classe Shape**
La classe Shape expose la propriété TextDirection qui peut être utilisée pour obtenir ou définir la direction de l'écoulement du texte pour l'objet Shape. La propriété TextDirection peut également être utilisée pour définir la direction souhaitée du texte pour les commentaires dans une feuille de calcul, comme le montre l'exemple ci-dessous.

**C#**

{{< highlight csharp >}}

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

Veuillez consulter l'article détaillé sur [Changer la direction du texte du commentaire](/cells/fr/net/change-text-direction-of-the-comment/)

{{% /alert %}}
## **Propriété ConvertFormulasData ajoutée à la classe HTMLLoadOptions**
La propriété ConvertFormulasData a été ajoutée à la classe HTMLLoadOptions, afin de faciliter aux développeurs le chargement des formules Excel à partir de fichiers HTML. La propriété booléenne ConvertFormulasData indique si oui ou non convertir la chaîne en formule lorsque la valeur de la chaîne commence par le caractère '='.

**C#**

{{< highlight csharp >}}

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
## **Propriété ImageOptions ajoutée à la classe HtmlSaveOptions**
La propriété ImageOptions a été ajoutée à la classe HtmlSaveOptions. L'exposition de la propriété ImageOptions a permis aux développeurs de définir les préférences pour les images intégrées dans le HTML lors de l'exportation des feuilles de calcul.
## **Propriété ExportChartImageFormat d'HtmlSaveOptions obsolète**
HtmlSaveOptions.ExportChartImageFormat a été marquée obsolète à partir de Aspose.Cells for .NET 8.0.2. Il est conseillé d'utiliser HtmlSaveOptions.ImageOptions à la place pour les paramètres de format d'image lors de l'exportation des feuilles de calcul au format HTML.
