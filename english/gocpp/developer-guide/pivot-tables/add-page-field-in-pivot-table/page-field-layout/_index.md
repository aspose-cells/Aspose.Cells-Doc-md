---
title: Modify Page Field Layout in Pivot Table
description: Learn how to control the page field area layout in a pivot table using Aspose.Cells for Go via C++, including setting the display order, wrap count, and field order of the page fields at the top of the pivot table.
linktitle: Modify Page Field Layout in Pivot Table
keywords: Aspose.Cells, Go library, spreadsheet, pivot table, page field, page field order, page field wrap count, move page field
type: docs
weight: 191
url: /go-cpp/change-page-field-layout/
---

{{% alert color="primary" %}}
This article is a continuation of the **Add Page Field in Pivot Table** topic. It demonstrates how to control the layout of the page field area — the strip of filter controls at the top of a pivot table — including display order, wrap count, and field reordering.
{{% /alert %}}

## **Introduction**
A pivot table in Microsoft Excel exposes a dedicated **page field area** that sits above the row/column/data body of the table. This area is rendered as a strip of dropdown filter controls (one per page field) and is what end-users click to slice the pivot by criteria such as year or region. Aspose.Cells for Go via C++ models this area through the `PivotTable.PageFields` collection and exposes three properties that control how the strip is visually laid out:
- `PivotTable.PageFieldOrder` (an `Aspose.Cells.PrintOrderType` value) decides whether additional page fields are placed *next to* the existing ones or *below* them.
- `PivotTable.PageFieldWrapCount` sets how many page fields are placed per row or column before wrapping.
- `PivotTable.PageFields.Move(currIndex, destIndex)` reorders the page fields without changing the order mode.
This article walks through three code examples that demonstrate each of these operations on a shared dataset, so that you can compare the resulting layouts side-by-side.

## **Source Data**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
All eight rows are populated in every code example, in identical order, so the source data never differs between scenarios — only the page-field layout properties do.

## **Example 1: Over Then Down**
In the first scenario we configure the two page fields (`Year`, `Region`) to appear **side-by-side in a single row** at the top of the pivot table. We assign `Fruit` to the row axis, place `Year` first and `Region` second on the page axis (the order of `AddFieldToArea` calls determines the starting index), add `Amount` (Sum) as the data field, and then set `PageFieldOrder` to `PrintOrderType.OverThenDown` with `PageFieldWrapCount = 2`. With `OverThenDown` and a wrap count of 2, the two page fields are laid out horizontally side-by-side in a single row at the top of the pivot table, so the strip occupies one row of width two.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PageFieldLayout.go" >}}

## **Example 2: Down Then Over**
In this example we place `Fruit` on the row axis, `Year` and `Region` on the page axis (with `Year` first), and `Amount` (Sum) as the data field — exactly as in Example 1. We then set `PageFieldOrder` to `PrintOrderType.DownThenOver` and `PageFieldWrapCount` to `2`. With `DownThenOver` and a wrap count of 2, the two page fields are stacked vertically — `Year` on top, `Region` directly below — forming a single column at the top of the pivot table. The strip therefore occupies two rows of width one, in contrast to Example 1.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PageFieldLayout-1.go" >}}

## **Example 3: Move a Page Field**
In the third scenario we keep this dataset and field allocation, set a neutral layout (`OverThenDown` with wrap count `2`), and then demonstrate the `PageFields.Move` operation. The `Move(0, 1)` call moves the page field at index 0 (`Year`) to position 1, and the page field that was at position 1 (`Region`) shifts to position 0. After this call, `Region` is the first page field and `Year` is the second. The wrap and order mode are unchanged, so the strip is still rendered horizontally side-by-side — only the order of the two dropdowns has been swapped.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PageFieldLayout-2.go" >}}

## **Related Articles**
- [Add Page Field in Pivot Table](/cells/go-cpp/add-page-field-in-pivot-table/) — the parent page that introduces how page fields are added to a pivot table.
- [Row and Column Fields in Pivot Table](/cells/go-cpp/row-and-column-fields/) — covers allocating fields to the row and column axes, complementing the page-axis work shown here.
- [Manage Value Fields in Pivot Table](/cells/go-cpp/manage-value-fields/) — describes how to configure the data (value) area, including the `Sum` aggregation used in this article.
- [Refresh Pivot Table](/cells/go-cpp/refresh-pivot-table/) — explains `RefreshData` and `CalculateData`, which are required after reordering page fields.
- [Apply Style to Pivot Table](/cells/go-cpp/apply-style-to-pivot-table/) — shows how to format the rendered pivot table after the page-field strip has been laid out.

{{< app/cells/assistant language="" >}}