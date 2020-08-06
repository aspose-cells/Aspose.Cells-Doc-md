---
title: Create a Pivot Table
type: docs
weight: 10
url: /pythonjava/create-a-pivot-table/
---

## **Create a Pivot Table**
Aspose.Cells for Python via Java provides the feature to create pivot tables. To create a pivot table using Aspose.Cells, please follow the steps below:

1. Add some data to worksheet cells by using the [Cell](https://apireference.aspose.com/cells/python/asposecells.api/Cell) object's [setValue](https://apireference.aspose.com/cells/python/asposecells.api/cell#Value) property. This data will be used as a data source for the pivot table.
1. Add a pivot table to the worksheet by calling the [PivotTableCollection](https://apireference.aspose.com/cells/python/asposecells.api/PivotTableCollection)[add](https://apireference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)) method, encapsulated in the [Worksheet](https://apireference.aspose.com/cells/python/asposecells.api/Worksheet) object.
1. Access the [PivotTable](https://apireference.aspose.com/cells/python/asposecells.api/PivotTable) object from the [PivotTableCollection](https://apireference.aspose.com/cells/python/asposecells.api/PivotTableCollection)by passing the [PivotTable](https://apireference.aspose.com/cells/python/asposecells.api/PivotTable) index.
1. Use any of the pivot table objects (explained above) encapsulated in the [PivotTableCollection](https://apireference.aspose.com/cells/python/asposecells.api/PivotTableCollection)object to manage the pivot table.

The following code snippet demonstrates creating a pivot table with the Aspose.Cells API.

{{< gist "aspose-com-gists" "f3cac13617c487b51b47cc9ae1d7c008" "PivotTables-CreatePivotTable.py" >}}
