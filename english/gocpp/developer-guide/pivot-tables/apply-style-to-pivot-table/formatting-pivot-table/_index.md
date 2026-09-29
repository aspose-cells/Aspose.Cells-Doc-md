---
title: Formatting Pivot Table with Golang via C++
linktitle: Formatting Pivot Table
type: docs
weight: 10
url: /go-cpp/formatting-pivot-table/
description: Learn how to customize the appearance of pivot tables using Aspose.Cells for C++.
---

## **Pivot Table Appearance**

How to Create a Pivot Table explains how to create a simple pivot table. This article describes how to customize a pivot table's appearance by setting various properties:

- Pivot table format options
- Pivot fields format options
- Data field format options

### **Setting Pivot Table Format Options**

The [**PivotTable**](https://reference.aspose.com/cells/go-cpp/pivottable/) class controls the overall pivot table and can be formatted in a number of ways.

#### **Setting the AutoFormat Type**

Microsoft Excel offers a number of different pre‑set report formats. Aspose.Cells supports these formatting options too. To access them:

1. Set [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/go-cpp/pivottable/isautoformat/) to **true**.  
2. Assign a formatting option from the [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/go-cpp/pivottableautoformattype/) enumeration.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable.go" >}}

#### **Setting Format Options**

The code sample below shows how to format the pivot table to show grand totals for rows and columns, how to set the report's field order, and how to set a custom string for null values.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-1.go" >}}

#### **Formatting Look and Feel Manually**

To format how the pivot table report looks manually, instead of using pre‑set report formats, use the [**PivotTable.Format()**](https://reference.aspose.com/cells/go-cpp/pivottable/format_pivotarea_style/) and [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) methods. Create a style object for your desired formatting, for example:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-2.go" >}}

### **Setting Pivot Field Format Options**

The [**PivotField**](https://reference.aspose.com/cells/go-cpp/pivotfield/) class represents a field in a pivot table and can be formatted in a number of ways. The code sample below shows how to:

- Access row fields.  
- Set subtotals.  
- Set autosort.  
- Set autoshow.

#### **Setting Row/Column/Page Fields Format**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-3.go" >}}

### **Setting Data Fields Format**

The code sample below shows how to set display formats and number format for data fields.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-4.go" >}}

### **Clearing Pivot Fields**

The [**PivotFieldCollection**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/) has a method named [**Clear()**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/clear/) that allows you to clear pivot fields. Use it when you want to clear all the pivot fields in the areas, for example, page, column, row, or data.  
The code sample below shows how to clear all the pivot fields in a data area.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-5.go" >}}