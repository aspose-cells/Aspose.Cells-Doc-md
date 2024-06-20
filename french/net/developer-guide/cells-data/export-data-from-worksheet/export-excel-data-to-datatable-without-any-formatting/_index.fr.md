---
title: Exporter des données Excel vers un DataTable sans aucun formatage
type: docs
weight: 280
url: /fr/net/export-excel-data-to-datatable-without-any-formatting/
description: Apprenez comment exporter des données Excel vers un DataTable sans aucun formatage à travers l API Aspose.Cells for .NET.
keywords: Exporter des données Excel vers un DataTable sans aucun formatage, spécifier la stratégie de formatage des valeurs de cellule, ajouter une stratégie de formatage lors de l exportation des données vers un DataTable. 
---

{{% alert color="primary" %}}

Parfois, les utilisateurs veulent exporter les données Excel dans un tableau de données sans aucun formatage. Par exemple, si une cellule a une valeur de 0,012345 et est formatée pour afficher deux décimales, alors lorsque l'utilisateur exportera les données Excel dans un tableau de données, elles seront exportées en tant que 0,01 et non pas en tant que 0,012345. Pour résoudre ce problème, Aspose.Cells a fourni la propriété [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) qui peut prendre une de ces trois valeurs

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

Si vous le définissez sur [**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), alors il exportera les données sans aucun formatage.

{{% /alert %}}

## Code d'exemple

L'exemple suivant explique l'utilisation de la propriété [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) pour exporter des données Excel avec ou sans mise en forme.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **Sortie console**

Ci-dessous se trouve la sortie de débogage de la console du code d'exemple ci-dessus

{{< highlight java >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
