---
title: Smartly Importing Variable Arrays into Excel With Smart Markers
type: docs
weight: 30
url: /net/how-to-import-variable-arrays-with-smart-markers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Why Use Variable Arrays for Smart Markers**
Variable arrays (e.g., <<products[0].name>> or <<foreach item in cart>>) enable dynamic handling of repeated data structures in templates. They solve limitations of flat/nested objects when dealing with lists, tables, or collections.

1. Dynamic Repetition Without Hardcoding: Static markers fail for variable‑length data (e.g., order items, user permissions). Arrays iterate dynamically.  
2. Simplified Aggregation: Calculate sums, averages, or filters directly. Avoid manual JavaScript/C# logic in templates.  
3. Tabular/List Data Representation: Natural fit: Tables, grids, and lists inherently map to arrays.  
4. Memory Efficiency: Arrays reduce template complexity and data‑binding overhead.  
5. Integration with APIs/Data Sources: Aligns with JSON/array‑centric data (e.g., REST APIs).

## **How to Import Variable Arrays with Smart Markers**
The following example code shows how to use variable arrays in Smart Markers. We place a variable‑array marker into cell **A1** of the first worksheet of the workbook dynamically, which contains a string of values that we set for the marker, process the markers to fill data into the cells corresponding to the marker, and finally save the Excel file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}

## **How to Import an HTML Property with Smart Markers**
The following sample code demonstrates the use of the HTML property of Smart Markers. When processed, it will display **"World"** in **"Hello World"** as bold because of the HTML `<b>` tag.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
