---
title: Modifications publiques de l API dans Aspose.Cells 8.8.0
type: docs
weight: 270
url: /fr/java/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.7.2 à 8.8.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques, les classes ajoutées et supprimées, etc., mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Obtenir les références de cellules pour la connexion externe**
Aspose.Cells for Java 8.8.0 a exposé les nouvelles propriétés suivantes qui sont utiles pour récupérer les références des cellules cibles et de sortie pour les connexions externes stockées dans la feuille de calcul. 

1. QueryTable.ConnectionId: Obtient l'identifiant de connexion de la table de requête.
1. ExternalConnection.Id: Obtient l'identifiant de la connexion externe.
1. ListObject.QueryTable: Obtient la QueryTable liée.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Trouver les tables de requête et les objets de liste liés aux connexions de données externes](/cells/fr/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Propriété HTMLLoadOptions.KeepPrecision ajoutée**
Aspose.Cells for Java 8.8.0 a ajouté la propriété HTMLLoadOptions.KeepPrecision afin de contrôler la conversion des longues valeurs numériques en notation exponentielle lors de l'importation de fichiers HTML. Par défaut, toute valeur de plus de 15 chiffres est convertie en notation exponentielle si les données sont importées à partir d'une chaîne HTML ou d'un fichier. Cependant, les utilisateurs peuvent désormais contrôler ce comportement à l'aide de la propriété HTMLLoadOptions.KeepPrecision. Si ladite propriété est définie sur true, les valeurs seront importées telles qu'elles sont dans la source.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Éviter la conversion de grandes valeurs numériques en notation exponentielle](/cells/fr/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setKeepPrecision(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Propriété HTMLLoadOptions.DeleteRedundantSpaces ajoutée**
Aspose.Cells for Java 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Supprimer les espaces redondants de HTML](/cells/fr/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Le scénario d'utilisation simple ressemble à ce qui suit. 

**Java**

{{< highlight csharp >}}

 //Sample Html containing redundant spaces after <br> tag

String html = "<html>"

		+ "<body>"

			+ "<table>"

				+ "<tr>"

					+ "<td>"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

					+ "</td>"

				+ "</tr>"

			+ "</table>"

		+ "</body>"

	+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setDeleteRedundantSpaces(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output-" + loadOptions.getDeleteRedundantSpaces() + ".xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Propriété Style.QuotePrefix ajoutée**
Aspose.Cells for Java 8.8.0 a exposé la propriété Style.QuotePrefix afin de détecter si une valeur de cellule débute par un symbole de guillemet simple. 

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Détecter un guillemet simple au début de la valeur de la cellule](/cells/fr/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Le scénario d'utilisation simple ressemble à ce qui suit. 

**Java**

{{< highlight csharp >}}

 //Create an instance of workbook

Workbook workbook = new Workbook();

//Access first worksheet from the collection

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells A1 and A2

Cell a1 = worksheet.getCells().get("A1");

Cell a2 = worksheet.getCells().get("A2");

//Add simple text to cell A1 and text with quote prefix to cell A2

a1.putValue("sample");

a2.putValue("'sample");

//Print their string values, A1 and A2 both are same

System.out.println("String value of A1: " + a1.getStringValue());

System.out.println("String value of A2: " + a2.getStringValue());

//Access styles of cells A1 and A2

Style s1 = a1.getStyle();

Style s2 = a2.getStyle();

System.out.println();

//Check if A1 and A2 has a quote prefix

System.out.println("A1 has a quote prefix: " + s1.getQuotePrefix());

System.out.println("A2 has a quote prefix: " + s2.getQuotePrefix());

{{< /highlight >}}
## **APIs obsolètes**
### **Propriété LoadOptions.ConvertNumericData obsolète**
Aspose.Cells 8.8.0 a marqué la propriété LoadOptions.ConvertNumericData comme obsolète. Veuillez utiliser la propriété correspondante des classes HTMLLoadOptions ou TxtLoadOptions.
{{< app/cells/assistant language="java" >}}
