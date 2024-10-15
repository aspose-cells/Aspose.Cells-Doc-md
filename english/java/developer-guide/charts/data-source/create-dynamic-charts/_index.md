---
title: Create Dynamic Charts
type: docs
weight: 200
url: /java/create-dynamic-charts/
---

{{% alert color="primary" %}}

Dynamic (or interactive) charts have the ability to change when you change the scope of data. In other words, the dynamic charts can automatically reflect changes when the data source is changed. In order to trigger the change in data source, one can use the filtering option of Excel Tables or use a control such as ComboBox or Dropdown list.

This article demonstrates the usage of Aspose.Cells for Java APIs to create dynamic charts using both of the aforementioned approaches.

{{% /alert %}}

## **Using Excel Tables**

{{% alert color="primary" %}}

Excel tables are referred to as ListObjects in Aspose.Cells' perspective therefore we will use the term "ListObject" instead of "Table" for clarity. Please read in detail on how to [create ListObjects](/cells/java/creating-a-list-object/) with Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects provides the in-built functionality to sort & filter the data upon user interaction. Both sorting & filtering options are provided through the drop-down lists which are automatically added to the header row of the ListObject. Due to these features (sorting & filtering) , the ListObject seems to be the perfect candidate to serve as the data source to a dynamic chart because when sorting or filtering is changed, the representation of data in the chart will be changed to reflect the current state of the ListObject.

In order to keep the demonstration simple to understand, we will create the Workbook from scratch and move forward step by step as outlined below.

1. Create an empty Workbook.
1. Access the Cells of first Worksheet in the Workbook.
1. Insert some data to the cells.
1. Create ListObject based on the inserted data.
1. Create Chart based on the data range of ListObject.
1. Save result on disc.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Using Dynamic Formulas**

In case you do not wish to use the ListObjects as data source to the dynamic chart, the other option is to use Excel functions (or formulas) to create a dynamic range of data, and a control (such as ComboBox) to trigger the change in data. In this scenario, we will use the VLOOKUP function to fetch the appropriate values based on the selection of ComboBox. When selection is changed, the VLOOKUP function will refresh the cell value. If a range of cells is using the the VLOOKUP function, whole range can be refreshed upon user interaction, therefore can be used as source to the dynamic chart.

In order to keep the demonstration simple to understand, we will create the Workbook from scratch and move forward step by step as outlined below.

1. Create an empty Workbook.
1. Access the Cells of first Worksheet in the Workbook.
1. Insert some data to the cells by creating a Named Range. This data will serve as series to the dynamic chart.
1. Create ComboBox based on the Named Range created in previous step.
1. Insert some more data to the cells that will serve as source to the VLOOKUP function.
1. Insert VLOOKUP function (with appropriate parameters) to a range of cells. This will range will serve as source to the dynamic chart.
1. Create Chart based on the range created in previous step.
1. Save result on disc.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
{{< app/cells/assistant language="java" >}}