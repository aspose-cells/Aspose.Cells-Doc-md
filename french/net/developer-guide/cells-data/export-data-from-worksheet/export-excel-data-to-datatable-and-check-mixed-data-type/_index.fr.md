---
title: Exporter des données Excel vers un DataTable et vérifier le type de données mixte
type: docs
weight: 280
url: /fr/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Apprenez comment exporter des données Excel vers un DataTable et vérifier le type de données mixte à travers l API Aspose.Cells for .NET.
keywords: Exporter les données Excel vers un DataTable et vérifier le type de données mixte, exporter les données du classeur vers un DataTable et vérifier le type de données mixte, exporter les données vers un DataTable et vérifier le type de données mixte, exporter les données de la feuille de calcul vers un DataTable et vérifier le type de données mixte.
---

## **Scénarios d'utilisation possibles**
Si une colonne contient des données de différents types, le programme lancera une exception de type lors de l'exportation des données vers un DataTable. Pour l'exportation d'un tableau de données, par défaut, Aspose.Cells évalue le type de données des valeurs en se basant sur la toute première valeur (cellule) dans la colonne. Donc, si la valeur est un nombre, cela signifie que le type de données de la colonne serait numérique, ce qui est raisonnable. Si la toute première valeur est un nombre mais qu'il y a des données ou des valeurs alphanumériques dans la colonne, un type de données de chaîne devrait être attribué. Pour y faire face, veuillez utiliser la [surcharge ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) qui implique [ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) et essayez de définir l'attribut booléen [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) sur "true" si une colonne contient à la fois des valeurs numériques et de chaîne pour éviter les erreurs.

## **Exporter des données Excel vers un DataTable et vérifier le type de données mixte**

L'exemple suivant explique l'utilisation de la propriété [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) pour exporter des données Excel vers un DataTable. Veuillez consulter le [fichier Excel d'exemple](sample.xlsx), sa capture d'écran et la sortie de la console pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

### **Capture d'écran**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

### **Sortie console**

Ci-dessous se trouve la sortie de débogage de la console du code d'exemple ci-dessus

{{< highlight java >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
