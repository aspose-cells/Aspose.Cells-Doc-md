---
title: Create Dynamic Charts
type: docs
weight: 200
url: /java/create-dynamic-charts/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Dynamic (or interactive) charts have the ability to change when you change the scope of data. In other words, the dynamic charts can automatically reflect changes when the data source is changed. In order to trigger the change in data source, one can use the filtering option of Excel Tables or use a control such as ComboBox or drop‑down list.

This article demonstrates the usage of Aspose.Cells for Java APIs to create dynamic charts using both of the aforementioned approaches.

{{% /alert %}}

## **Using Excel Tables**

{{% alert color="primary" %}}

Excel tables are referred to as ListObjects in Aspose.Cells’ perspective, therefore we will use the term **ListObject** instead of **Table** for clarity. Please read in detail on how to [create ListObjects](/cells/java/creating-a-list-object/) with Aspose.Cells for Java API.

{{% /alert %}}

ListObjects provide the in‑built functionality to sort and filter the data upon user interaction. Both sorting and filtering options are provided through the drop‑down lists, which are automatically added to the header row of the ListObject. Due to these features (sorting and filtering), the ListObject seems to be the perfect candidate to serve as the data source for a dynamic chart because when sorting or filtering is changed, the representation of data in the chart will be changed to reflect the current state of the ListObject.

In order to keep the demonstration simple to understand, we will create the Workbook from scratch and move forward step by step as outlined below.

1. Create an empty Workbook.  
2. Access the Cells of the first Worksheet in the Workbook.  
3. Insert some data into the cells.  
4. Create a ListObject based on the inserted data.  
5. Create a Chart based on the data range of the ListObject.  
6. Save the result on disk.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Using Dynamic Formulas**

In case you do not wish to use the ListObjects as the data source for the dynamic chart, the other option is to use Excel functions (or formulas) to create a dynamic range of data, and a control (such as ComboBox) to trigger the change in data. In this scenario, we will use the VLOOKUP function to fetch the appropriate values based on the selection of the ComboBox. When the selection is changed, the VLOOKUP function will refresh the cell value. If a range of cells is using the VLOOKUP function, the whole range can be refreshed upon user interaction; therefore, it can be used as the source for the dynamic chart.

In order to keep the demonstration simple to understand, we will create the Workbook from scratch and move forward step by step as outlined below.

1. Create an empty Workbook.  
2. Access the Cells of the first Worksheet in the Workbook.  
3. Insert some data into the cells by creating a Named Range. This data will serve as the series for the dynamic chart.  
4. Create a ComboBox based on the Named Range created in the previous step.  
5. Insert some more data into the cells that will serve as the source for the VLOOKUP function.  
6. Insert the VLOOKUP function (with appropriate parameters) into a range of cells. This range will serve as the source for the dynamic chart.  
7. Create a Chart based on the range created in the previous step.  
8. Save the result on disk.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
{{< app/cells/assistant language="java" >}}
