---
title: Exporter des données Excel vers DataTable sans aucun formatage
type: docs
weight: 280
url: /fr/net/export-excel-data-to-datatable-without-any-formatting/
description: Découvrez comment exporter des données Excel vers DataTable sans aucun formatage via le Aspose.Cells for .NET API.
keywords: Export Excel Data to DataTable without any Formatting, Specify Cell Value Format Strategy, Add Format Strategy When Exporting Data to DataTable. 
---
{{% alert color="primary" %}}

Parfois, les utilisateurs souhaitent exporter des données Excel dans un tableau de données sans aucun formatage. Par exemple, si une cellule a une valeur 0,012345 et qu'elle est formatée pour afficher deux décimales, alors lorsque l'utilisateur exportera des données Excel vers une table de données, elles seront exportées sous la forme 0,01 et non sous la forme 0,012345. Pour faire face à ce problème, le Aspose.Cells a mis à disposition[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) propriété qui peut prendre une de ces trois valeurs

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.Aucun

 Si vous le réglez sur[**CellValueFormatStrategy.Aucun**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), il exportera alors les données sans aucun formatage.

{{% /alert %}}

##  Exemple de code

 L'exemple suivant explique l'utilisation de[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)propriété pour exporter des données Excel avec et sans aucun formatage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

##  **Sortie console**

Vous trouverez ci-dessous la sortie de débogage de la console de l'exemple de code ci-dessus

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
