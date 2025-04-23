---
title: Définir une source de données personnalisée pour WorkbookDesigner
type: docs
weight: 60
url: /fr/net/set-custom-datasource-for-workbookdesigner/
---

Aspose.Cells offre la possibilité de définir une source de données personnalisée pour WorkbookDesigner. L'API fournit une méthode surchargée [WorkbookDesigner.SetDataSource](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/setdatasource/methods/5) qui prend le nom de la source en premier paramètre et l'instance de la classe qui implémente [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) en second paramètre. 

Le code suivant démontre l'utilisation de la méthode [WorkbookDesigner.SetDataSource](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/setdatasource/methods/5) pour définir la source de données personnalisée.
## **Code d'exemple**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-1.cs" >}}

L'implémentation des classes *CustomerDataSource*, *Customer* et *CustomerList* est donnée ci-dessous

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}

Les fichiers Excel source et de sortie sont joints pour référence.

[Fichier Source](95584319.xlsx)

[Fichier de Sortie](95584320.xlsx)
{{< app/cells/assistant language="csharp" >}}
