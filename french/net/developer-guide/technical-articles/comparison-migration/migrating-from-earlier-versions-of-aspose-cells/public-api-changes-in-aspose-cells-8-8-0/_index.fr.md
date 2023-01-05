---
title: Public API Changements dans Aspose.Cells 8.8.0
type: docs
weight: 260
url: /fr/net/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.7.2 à 8.8.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Obtenir les références Cell pour la connexion externe**
Aspose.Cells for .NET 8.8.0 a exposé les nouvelles propriétés suivantes qui sont utiles pour récupérer les références de cellule cible et de sortie pour les connexions externes stockées dans la feuille de calcul.

1. QueryTable.ConnectionId : obtient l'ID de connexion de la table de requête.
1. ExternalConnection.Id : Obtient l'ID de la connexion externe.
1. ListObject.QueryTable : obtient le QueryTable lié.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Rechercher des tables de requête et des objets de liste liés aux connexions de données externes](/cells/fr/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Ajout de la propriété HTMLLoadOptions.KeepPrecision**
Aspose.Cells for .NET 8.8.0 a ajouté la propriété HTMLLoadOptions.KeepPrecision afin de contrôler la conversion des valeurs numériques longues en notation exponentielle lors de l'importation de fichiers HTML. Par défaut, toute valeur supérieure à 15 chiffres est convertie en notation exponentielle si les données sont importées à partir de la chaîne ou du fichier HTML. Cependant, les utilisateurs peuvent maintenant contrôler ce comportement à l'aide de la propriété HTMLLoadOptions.KeepPrecision. Si ladite propriété est définie sur true, les valeurs seront importées telles qu'elles sont dans la source.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[ Éviter la conversion de grandes valeurs numériques en notation exponentielle](/cells/fr/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

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

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Ajout de la propriété HTMLLoadOptions.DeleteRedundantSpaces**
Aspose.Cells for .NET 8.8.0 a exposé la propriété HTMLLoadOptions.DeleteRedundantSpaces afin de conserver ou de supprimer les espaces supplémentaires après la balise de saut de ligne (<br>Tag) lors de l'importation des données à partir de la chaîne ou du fichier HTML. La propriété HTMLLoadOptions.DeleteRedundantSpaces a la valeur par défaut false, ce qui signifie que tous les espaces supplémentaires seront conservés et importés dans l'objet Workbook. Cependant, lorsqu'il est défini sur true, le API supprimera tous les espaces redondants après la balise de saut de ligne.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Supprimer les espaces redondants de HTML](/cells/fr/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Le scénario d'utilisation simple se présente comme suit.

**C#**

{{< highlight "csharp" >}}

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

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Ajout de la propriété Style.QuotePrefix**
Aspose.Cells for .NET 8.8.0 a exposé la propriété Style.QuotePrefix afin de détecter si une valeur de cellule commence par un guillemet simple.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Détecter le guillemet unique au début de la valeur Cell](/cells/fr/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Le scénario d'utilisation simple se présente comme suit.

**C#**

{{< highlight "csharp" >}}

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
## **API obsolètes**
### **Propriété LoadOptions.ConvertNumericData obsolète**
Aspose.Cells 8.8.0 a marqué la propriété LoadOptions.ConvertNumericData comme obsolète. Veuillez utiliser la propriété correspondante des classes HTMLLoadOptions ou TxtLoadOptions.
