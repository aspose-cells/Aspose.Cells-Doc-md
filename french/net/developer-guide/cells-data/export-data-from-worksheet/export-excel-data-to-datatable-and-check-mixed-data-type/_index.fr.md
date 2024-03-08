---
title: Exportez les données Excel vers DataTable et vérifiez le type de données mixte
type: docs
weight: 280
url: /fr/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Découvrez comment exporter des données Excel vers DataTable et vérifier le type de données mixtes via le Aspose.Cells for .NET API.
keywords: Export Excel Data to DataTable and Check Mixed Data Type, Export Workbook Data to DataTable and Check Mixed Data Type, Export Data to DataTable and Check Mixed Data Type, Export Worksheet Data to DataTable and Check Mixed Data Type.
---
##  **Scénarios d'utilisation possibles**
 Si une colonne contient des données de différents types, le programme lèvera une exception de type lors de l'exportation de données vers un DataTable. Pour exporter le tableau de données, par défaut, Aspose.Cells évalue le type de données pour les valeurs en fonction de la toute première valeur (cellule) de la colonne. Ainsi, si la valeur est numérique, cela signifie que le type de données de la colonne sera numérique, ce qui est raisonnable. Si la toute première valeur est un nombre mais qu'il y a des données ou des valeurs alphanumériques dans la colonne, un type de données chaîne doit être attribué. Pour y faire face, veuillez utiliser[Surcharge ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) qui implique[ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) et essayez de définir[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Attribut booléen à « true » si une colonne contient à la fois des valeurs numériques et des valeurs de chaîne pour échapper à l'erreur.

##  **Exportez les données Excel vers DataTable et vérifiez le type de données mixte**

 L'exemple suivant explique l'utilisation de[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) propriété pour exporter des données Excel vers une table de données. Veuillez consulter le[exemple de fichier Excel](sample.xlsx), sa capture d'écran et la sortie de la console pour référence.

###  **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

###  **Capture d'écran**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

###  **Sortie console**

Vous trouverez ci-dessous la sortie de débogage de la console de l'exemple de code ci-dessus

{{< highlight "java" >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
