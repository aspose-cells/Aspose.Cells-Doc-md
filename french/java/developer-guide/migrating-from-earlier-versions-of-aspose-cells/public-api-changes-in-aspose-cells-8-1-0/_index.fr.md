---
title: Public API Changements dans Aspose.Cells 8.1.0
type: docs
weight: 50
url: /fr/java/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.0.2 à 8.1.0, qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour, mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **Ajout de la propriété HtmlSaveOptions.ExportHiddenWorksheet**
La classe HtmlSaveOptions a exposé la propriété ExportHiddenWorksheet qui peut être utilisée pour spécifier si les feuilles de calcul masquées sont exportées au format HTML. La valeur par défaut est true. alors que s'il est défini sur false, le Aspose.Cells n'exportera pas le contenu masqué de la feuille de calcul.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Empêcher l'exportation de la feuille de calcul masquée](/cells/fr/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Ajout de la propriété Cell.StringValueWithoutFormat**
 La propriété StringValueWithoutFormat a été ajoutée à la classe Cell, afin de permettre aux développeurs de récupérer la valeur de la cellule sans aucune mise en forme appliquée.

L'extrait de code fourni ci-dessous illustre l'utilisation de la méthode Cell.getStringValueWithoutFormat par rapport à cell.getDisplayStringValue en créant une feuille de calcul à partir de zéro et en appliquant le format numérique à l'une des cellules.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access A1 cell

Cell cell = sheet.getCells().get("A1");

//Put a value cell and convert it to number

cell.putValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

int index = book.getStyles().add();

Style style = book.getStyles().get(index);

//Set Number format for Style object

style.setNumber(3);

//Create an instance of StyleFlag class

//and set NumberFormat to true

StyleFlag flag = new StyleFlag();

flag.setNumberFormat(true);

//Set the style of A1 cell

cell.setStyle(style, flag);

//Get formatted string value 

String formatted = cell.getDisplayStringValue();

System.out.println("Formatted String Value: " +formatted);

//Get un-formatted string value

String unformatted = cell.getStringValueWithoutFormat();

System.out.println("Un-formatted String Value: " + unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

La sortie du code ci-dessus est la suivante

Valeur de chaîne formatée : 123 456
Valeur de chaîne non formatée : 123456

{{% /alert %}}
## **Obsolètes Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs Properties**
 De nombreuses propriétés de la classe BuiltInDocumentPropertyCollection ont été marquées comme obsolètes à partir de Aspose.Cells for .NET 8.1.0. Ces propriétés incluent Bytes, Characters, CharactersWithSpaces, Lines & Paragraphs. La raison étant que les propriétés susmentionnées ne sont d'aucune utilité dans la préservation des feuilles de calcul Excel car Excel les omet. Alors que ces propriétés ont été écrites à l'origine pour les documents Word et les présentations PowerPoint.
