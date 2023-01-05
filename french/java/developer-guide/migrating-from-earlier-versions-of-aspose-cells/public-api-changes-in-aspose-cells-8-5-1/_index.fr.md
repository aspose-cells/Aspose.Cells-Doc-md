---
title: Public API Changements dans Aspose.Cells 8.5.1
type: docs
weight: 180
url: /fr/java/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.5.0 à 8.5.1 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour,[classes ajoutées, etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-5-1/), mais aussi une description de tout changement de comportement dans les coulisses du Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Method Workbook.Dispose Ajouté**
Aspose.Cells for Java 8.5.1 a exposé la méthode Workbook.dispose pour libérer les ressources non gérées de l'objet Workbook. Le modèle de suppression est utilisé uniquement pour les objets qui accèdent aux ressources non managées, telles que les descripteurs de fichiers et de canaux, les descripteurs de registre, les descripteurs d'attente ou les pointeurs vers des blocs de mémoire non managée. En effet, le ramasse-miettes est très efficace pour récupérer les objets gérés inutilisés, mais il est incapable de récupérer les objets non gérés.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Méthode Cell.getHeightOfValue ajoutée**
 Aspose.Cells for Java 8.5.1 a exposé la méthode Cell.getHeightOfValue pour obtenir la hauteur de la valeur de la cellule. En utilisant cette méthode, vous pouvez calculer la hauteur de la valeur de la cellule, puis définir la hauteur de la ligne de cette cellule respectivement. Consultez l'article détaillé sur[comment calculer la hauteur et la largeur de la cellule](/cells/fr/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Énumération TableDataSourceType ajoutée**
Aspose.Cells for Java 8.5.1 a exposé l'énumération com.aspose.cells.TableDataSourceType pour récupérer le type de source de données d'un ListObject. L'énumération TableDataSourceType comme champs suivants.

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XMLTableDataSourceType.XML
### **Propriété ListObject.DataSourceType ajoutée**
Avec la version v8.5.1, le Aspose.Cells API a exposé la propriété ListObject.DataSourceType en lecture seule qui peut être utilisée pour détecter le type de source de données d'un ListObject.

Voici le scénario d'utilisation le plus simple.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.getWorksheets().get(0);

ListObject listObject = sheet.getListObjects().get(0);

if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.QUERY_TABLE)

{

	System.out.println("Data Source Type is Query Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.SHARE_POINT)

{

	System.out.println("Data Source Type is SharePoint Linked List");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.WORKSHEET)

{

	System.out.println("Data Source Type is Excel Worksheet Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.XML)

{

	System.out.println("Data Source Type is XML");

}

{{< /highlight >}}
