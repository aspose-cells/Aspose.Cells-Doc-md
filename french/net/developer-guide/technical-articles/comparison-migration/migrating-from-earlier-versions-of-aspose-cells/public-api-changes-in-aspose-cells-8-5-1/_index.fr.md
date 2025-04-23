---
title: Changements de l API publique dans Aspose.Cells 8.5.1
type: docs
weight: 170
url: /fr/net/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.5.0 à la version 8.5.1 qui pourraient intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, [classes ajoutées, etc.](/cells/fr/net/changements-de-l-api-publique-dans-aspose-cells-8-5-1/), mais également une description de tout changement dans le comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Méthode Workbook.Dispose ajoutée**
L'objet Workbook implémente maintenant l'interface System.IDisposable qui possède une seule méthode Dispose. Vous pouvez soit appeler directement la méthode Workbook.Dispose, soit créer un objet Workbook dans une structure Using pour appeler automatiquement cette méthode.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.5.1 a exposé la méthode Cell.GetHeightOfValue pour obtenir la hauteur de la valeur de la cellule. En utilisant cette méthode, vous pouvez calculer la hauteur de la valeur de la cellule, puis définir la hauteur de la ligne de cette cellule respectivement. Consultez l'article détaillé sur [comment calculer la hauteur et la largeur de la valeur de la cellule](/cells/fr/net/calculer-la-largeur-et-la-hauteur-de-la-valeur-de-la-cellule-en-unité-de-pixels/).
### **Énumération TableDataSourceType ajoutée**
Aspose.Cells for .NET 8.5.1 a exposé l'énumération Aspose.Cells.Tables.TableDataSourceType pour récupérer le type de source de données d'un ListObject. L'énumération TableDataSourceType comporte les champs suivants.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **Propriété ListObject.DataSourceType ajoutée**
Avec la sortie de la version 8.5.1, l'API Aspose.Cells a exposé la propriété en lecture seule ListObject.DataSourceType qui peut être utilisée pour détecter le type de source de données d'un ListObject.

Voici le scénario d'utilisation le plus simple.

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
