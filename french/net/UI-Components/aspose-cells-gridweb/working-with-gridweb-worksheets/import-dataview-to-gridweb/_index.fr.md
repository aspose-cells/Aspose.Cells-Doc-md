---
title: Importer DataView dans GridWeb
type: docs
weight: 60
url: /fr/net/import-dataview-to-gridweb/
---
{{% alert color="primary" %}} 

Avec la sortie du framework Microsoft .NET, une nouvelle façon de stocker les données a été introduite. Maintenant les objets DataSet, DataTable et DataView qui stockent les données en mode hors ligne. Ces objets sont très pratiques en tant que référentiels de données. À l'aide de Aspose.Cells.GridWeb, il est possible d'importer des données à partir d'objets DataTable ou DataView dans des feuilles de calcul. Aspose.Cells.GridWeb ne prend en charge que l'importation de données à partir d'un DataView. mais un objet DataTable peut également être utilisé indirectement. Discutons de cette fonctionnalité en détail.

{{% /alert %}} 
## **Importation de données depuis DataView**
Importez des données à partir d'un objet DataView à l'aide de la méthode ImportDataView de GridWorsheetCollection dans le contrôle GridWeb. Transmettez l'objet DataView à partir duquel vous souhaitez importer des données à la méthode ImportDataView. Il est possible de spécifier l'en-tête de colonne et les styles de données lors de l'importation.

{{% alert color="primary" %}} 

Lorsque des données sont importées à partir d'un objet DataView, une nouvelle feuille de calcul est créée pour contenir les données importées. La feuille de calcul porte le même nom que DataTable.

{{% /alert %}} 

**Sortie : données importées d'un DataView dans une nouvelle feuille de calcul** 

![tâche : image_autre_texte](import-dataview-to-gridweb_1.png)

 La largeur des colonnes est ajustée pour afficher toutes les données qu'elles contiennent. Lorsque les données sont importées à partir de DataView, les largeurs de colonne ne sont pas ajustées automatiquement. Les utilisateurs doivent les régler eux-mêmes. Pour ajuster les largeurs de colonne par programmation, reportez-vous à[Redimensionner les lignes et les colonnes](/cells/fr/net/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

Une version surchargée de la méthode ImportDataView permet aux développeurs de spécifier le nom de la feuille qui contient les données importées et un nombre spécifique de lignes et de colonnes à importer à partir de l'objet DataView.

{{% /alert %}}
