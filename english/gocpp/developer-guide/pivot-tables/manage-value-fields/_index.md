---
title: Manage Pivot Table Value Fields in Aspose.Cells for Go via C++
description: Learn how to add base fields to the data region of a pivot table, change the summary function with PivotField.Function, and plot the value field onto the Row or Column axis in Aspose.Cells for Go via C++.
linktitle: Value Fields
keywords: Aspose.Cells, Go, pivot table, value field, PivotField, PivotField.Function, data field, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /go-cpp/manage-value-fields/
---

## Adding a Field to the Data Region
Adding a base field to the data (value) region is the first step in shaping how a pivot table aggregates your source data. Aspose.Cells exposes `PivotTable.AddFieldToArea(PivotFieldType, string)`, an overload that accepts the constant `PivotFieldType.Data` and the source-column name. Once a field is added to the data region, the API exposes it through the `PivotTable.DataFields` collection, in the order in which the fields were added. By default, a numeric source column is summarised with `ConsolidationFunction.Sum`, while a non-numeric column defaults to `Count`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManageValueFields.go" >}}

## Changing the Summary Function
Once a field lives in the data region, Aspose.Cells exposes it through the `PivotField` object on `PivotTable.DataFields`. Each `PivotField` has a writable `Function` property of type `ConsolidationFunction`, which controls the aggregate applied to that field's underlying values. `ConsolidationFunction` is an enum with members `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var`, and `Varp` — the first six cover the vast majority of real-world use cases, while the last four are statistical aggregates useful for variance analysis.

{{% alert color="primary" %}}
Changing `Function` only affects the aggregate; the source column and the pivot's row/column structure are not modified. To switch the aggregate for an existing data field, set `pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` and then call `pivotTable.CalculateData()` to re-render the pivot.
{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManageValueFields-1.go" >}}

## Plotting Value Fields to Row or Column Axis
When a pivot table contains two or more data fields, Aspose.Cells exposes an additional virtual field called `PivotTable.ValuesField`. This virtual field represents the aggregate of every data field that lives in the data region. You can drag it into the Row or Column region as a base pivot field, which is useful for laying out multiple measures side by side.

{{% alert color="primary" %}}
`PivotTable.ValuesField` does not work if there is no or only one value field.
{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManageValueFields-2.go" >}}

{{< app/cells/assistant language="go" >}}