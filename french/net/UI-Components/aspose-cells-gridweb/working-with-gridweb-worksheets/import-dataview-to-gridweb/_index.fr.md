---
title: Importer DataView dans GridWeb
type: docs
weight: 60
url: /fr/net/aspose-cells-gridweb/import-dataview-to-gridweb/
keywords: GridWeb, importation
description: Cet article présente comment importer des données dans GridWeb.
---

{{% alert color="primary" %}} 

Avec la sortie du Microsoft .NET Framework, un nouveau moyen de stocker les données a été introduit. Maintenant, les objets DataSet, DataTable et DataView stockent les données en mode hors ligne. Ces objets sont très utiles en tant que référentiels de données. En utilisant Aspose.Cells.GridWeb, il est possible d'importer des données à partir d'objets DataTable ou DataView dans des feuilles de calcul. Aspose.Cells.GridWeb prend en charge uniquement l'importation de données à partir d'un objet DataView, mais un objet DataTable peut également être utilisé de manière indirecte. Discutons en détail de cette fonctionnalité.

{{% /alert %}} 
## **Importation de données depuis DataView**
Importer les données à partir d'un objet DataView en utilisant la méthode ImportDataView de la collection GridWorsheet dans le contrôle GridWeb. Passez l'objet DataView dont vous souhaitez importer les données à la méthode ImportDataView. Il est possible de spécifier l'en-tête de colonne et les styles de données lors de l'importation.

{{% alert color="primary" %}} 

Lorsque les données sont importées à partir d'un objet DataView, une nouvelle feuille de calcul est créée pour contenir les données importées. La feuille de calcul porte le même nom que le DataTable.

{{% /alert %}} 

**Sortie : Données importées depuis un DataView dans une nouvelle feuille de calcul** 

![todo:image_alt_text](import-dataview-to-gridweb_1.png)

Les largeurs des colonnes sont ajustées pour montrer toutes les données qu'elles contiennent. Lorsque les données sont importées depuis DataView, les largeurs des colonnes ne sont pas ajustées automatiquement. Les utilisateurs doivent les ajuster eux-mêmes. Pour ajuster les largeurs des colonnes de manière programmatique, reportez-vous à [Redimensionner les lignes et les colonnes](/cells/fr/net/aspose-cells-gridweb/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

Une version surchargée de la méthode ImportDataView permet aux développeurs de spécifier le nom de la feuille qui contient les données importées et un nombre spécifique de lignes et de colonnes à importer à partir de l'objet DataView.

{{% /alert %}}
