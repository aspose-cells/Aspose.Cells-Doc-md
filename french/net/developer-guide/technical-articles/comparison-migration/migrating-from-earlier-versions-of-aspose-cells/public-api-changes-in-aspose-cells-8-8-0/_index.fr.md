---
title: Modifications publiques de l API dans Aspose.Cells 8.8.0
type: docs
weight: 260
url: /fr/net/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.7.2 à 8.8.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques, les classes ajoutées et supprimées, etc., mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Obtenir les références de cellules pour la connexion externe**
Aspose.Cells for .NET 8.8.0 a exposé les nouvelles propriétés suivantes qui sont utiles pour récupérer les références de cellules cibles et de sortie pour les connexions externes stockées dans la feuille de calcul.

1. QueryTable.ConnectionId: Obtient l'identifiant de connexion de la table de requête.
1. ExternalConnection.Id: Obtient l'identifiant de la connexion externe.
1. ListObject.QueryTable: Obtient la QueryTable liée.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Trouver les tables de requête et les objets de liste liés aux connexions de données externes](/cells/fr/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Propriété HTMLLoadOptions.KeepPrecision ajoutée**
Aspose.Cells for .NET 8.8.0 a ajouté la propriété HTMLLoadOptions.KeepPrecision afin de contrôler la conversion des valeurs numériques longues en notation exponentielle lors de l'importation de fichiers HTML. Par défaut, toute valeur de plus de 15 chiffres est convertie en notation exponentielle si les données sont importées à partir d'une chaîne HTML ou d'un fichier. Cependant, les utilisateurs peuvent désormais contrôler ce comportement à l'aide de la propriété HTMLLoadOptions.KeepPrecision. Si ladite propriété est définie sur true, les valeurs seront importées telles qu'elles sont dans la source.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Éviter la conversion des grandes valeurs numériques en notation exponentielle](/cells/fr/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 string html = @" 

<table data-cache=""not-cached"" class=""sortable""> 

   <tbody> 

    <tr> 

     <td class=""even"">9999999999999999</td> 

     <td class=""odd"">10.8%</td> 

    </tr> 

   </tbody> 

</table> 

";

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Propriété HTMLLoadOptions.DeleteRedundantSpaces ajoutée**
Aspose.Cells for .NET 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Supprimer les espaces redondants de HTML](/cells/fr/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Le scénario d'utilisation simple ressemble à ce qui suit.

**C#**

{{< highlight csharp >}}

 string html = @" 

<html>

    <body>

        <table>

            <tr>

                <td>

                    <br>    This is sample data 

                    <br>    This is sample data

                    <br>    This is sample data

                </td>

            </tr>

        </table>

    </body>

</html>

";

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Propriété Style.QuotePrefix ajoutée**
Aspose.Cells for .NET 8.8.0 a exposé la propriété Style.QuotePrefix afin de détecter si la valeur d'une cellule commence par un symbole de guillemet simple.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Détecter une seule citation au début de la valeur de la cellule](/cells/fr/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Le scénario d'utilisation simple ressemble à ce qui suit.

**C#**

{{< highlight csharp >}}

 Workbook book = new Workbook();

Worksheet sheet = book.Worksheets[0];

Cell a1 = sheet.Cells["A1"];

Cell a2 = sheet.Cells["A2"];

a1.PutValue("sample");

a2.PutValue("'sample");

Console.WriteLine("String value of A1: " + a1.StringValue);

Console.WriteLine("String value of A2: " + a2.StringValue);

Style s1 = a1.GetStyle();

Style s2 = a2.GetStyle();

Console.WriteLine("A1 has a quote prefix: " + s1.QuotePrefix);

Console.WriteLine("A2 has a quote prefix: " + s2.QuotePrefix);

{{< /highlight >}}
## **APIs obsolètes**
### **Propriété LoadOptions.ConvertNumericData obsolète**
Aspose.Cells 8.8.0 a marqué la propriété LoadOptions.ConvertNumericData comme obsolète. Veuillez utiliser la propriété correspondante des classes HTMLLoadOptions ou TxtLoadOptions.
{{< app/cells/assistant language="csharp" >}}
