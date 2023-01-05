---
title: Public API Changements dans Aspose.Cells 8.5.1
type: docs
weight: 170
url: /fr/net/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.5.0 à 8.5.1 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour,[classes ajoutées, etc.](/cells/fr/net/public-api-changes-in-aspose-cells-8-5-1/), mais aussi une description de tout changement de comportement dans les coulisses du Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Method Workbook.Dispose Ajouté**
L'objet Workbook implémente désormais l'interface System.IDisposable qui a une seule méthode Dispose. Vous pouvez appeler directement la méthode Workbook.Dispose ou créer un objet Workbook dans une structure Using pour appeler cette méthode automatiquement.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call Dispose method

book.Dispose();

//Call Dispose method via Using statement

using (Workbook book = new Workbook())

{

    //do processing

}

{{< /highlight >}}


### **Méthode Cell.GetHeightOfValue ajoutée**
 Aspose.Cells for .NET 8.5.1 a exposé la méthode Cell.GetHeightOfValue pour obtenir la hauteur de la valeur de la cellule. En utilisant cette méthode, vous pouvez calculer la hauteur de la valeur de la cellule, puis définir la hauteur de la ligne de cette cellule respectivement. Consultez l'article détaillé sur[comment calculer la hauteur et la largeur de la cellule](/cells/fr/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Énumération TableDataSourceType ajoutée**
Aspose.Cells for .NET 8.5.1 a exposé l'énumération Aspose.Cells.Tables.TableDataSourceType pour récupérer le type de source de données d'un ListObject. L'énumération TableDataSourceType comme champs suivants.

1. TableDataSourceType.QueryTableTableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.WorksheetTableDataSourceType.Worksheet
1. TableDataSourceType.XMLTableDataSourceType.XML
### **Propriété ListObject.DataSourceType ajoutée**
Avec la version v8.5.1, le Aspose.Cells API a exposé la propriété ListObject.DataSourceType en lecture seule qui peut être utilisée pour détecter le type de source de données d'un ListObject.

Voici le scénario d'utilisation le plus simple.

**C#**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.Worksheets[0];

ListObject listObject = sheet.ListObjects[0];

if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.QueryTable)

{

    Console.WriteLine("Data Source Type is Query Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.SharePoint)

{

    Console.WriteLine("Data Source Type is SharePoint Linked List");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.Worksheet)

{

    Console.WriteLine("Data Source Type is Excel Worksheet Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.XML)

{

    Console.WriteLine("Data Source Type is XML");

}

{{< /highlight >}}
