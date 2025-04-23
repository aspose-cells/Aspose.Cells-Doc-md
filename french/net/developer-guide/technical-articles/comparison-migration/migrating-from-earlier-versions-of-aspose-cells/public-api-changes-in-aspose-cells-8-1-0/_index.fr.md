---
title: Changements de l API publique dans Aspose.Cells 8.1.0
type: docs
weight: 40
url: /fr/net/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.0.2 à la 8.1.0, qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement de nouvelles méthodes publiques et mises à jour, mais aussi une description de tout changement dans le comportement en arrière-plan d'Aspose.Cells.

{{% /alert %}} 
## **Propriété ExportHiddenWorksheet d'HtmlSaveOptions ajoutée**
La classe HtmlSaveOptions a exposé la propriété ExportHiddenWorksheet qui peut être utilisée pour spécifier si les feuilles de calcul masquées sont exportées au format HTML. La valeur par défaut est true, tandis que si elle est définie sur false, Aspose.Cells n'exportera pas le contenu de la feuille de calcul masquée.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Empêcher l'exportation des contenus de feuille de calcul masqués](/cells/fr/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Propriété Cell.StringValueWithoutFormat ajoutée**
La propriété StringValueWithoutFormat a été ajoutée à la classe Cell, afin de faciliter aux développeurs la récupération de la valeur de la cellule sans aucun format appliqué.

Le code ci-dessous montre comment utiliser la propriété Cell.StringValueWithoutFormat par rapport à cell.DisplayStringValue en créant une feuille de calcul à partir de zéro et en appliquant le format numérique à l'une des cellules.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.Worksheets[0];

//Access A1 cell

Cell cell = sheet.Cells["A1"];

//Put a value cell and convert it to number

cell.PutValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

Style style = book.Styles[book.Styles.Add()];

//Set Number format for Style object

style.Number = 3;

//Set the style of A1 cell

cell.SetStyle(style, new StyleFlag() { NumberFormat = true });

//Get formatted string value 

string formatted = cell.DisplayStringValue;

Console.WriteLine(formatted);

//Get un-formatted string value

string unformatted = cell.StringValueWithoutFormat;

Console.WriteLine(unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

La sortie du code ci-dessus est la suivante

123,456

123456

{{% /alert %}}
## **Propriétés Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs obsolètes**
De nombreuses propriétés de la classe BuiltInDocumentPropertyCollection ont été marquées comme obsolètes à partir de Aspose.Cells for .NET 8.1.0. Ces propriétés comprennent Bytes, Characters, CharactersWithSpaces, Lines & Paragraphs. La raison en est que ces propriétés susmentionnées ne sont d'aucune utilité dans la préservation des feuilles de calcul Excel car Excel les omet. Ces propriétés ont été initialement écrites pour les documents Word et les présentations PowerPoint.
{{< app/cells/assistant language="csharp" >}}
