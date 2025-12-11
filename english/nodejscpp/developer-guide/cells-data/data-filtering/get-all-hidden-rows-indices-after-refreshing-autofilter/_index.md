---  
title: Get All Hidden Rows Indices after Refreshing AutoFilter 
type: docs  
weight: 320  
url: /nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Learn how to get all hidden rows indices after refreshing AutoFilter by using the Aspose.Cells for Node.js via C++ API.  
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter Node.js via C++, Obtain All Hidden Rows Indices after Refreshing AutoFilter Node.js via C++, Retrieve All Hidden Rows Indices after Refreshing AutoFilter Node.js via C++  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

When you apply the AutoFilter on worksheet cells, some of the rows get hidden automatically. However, it might be the case that some rows are already hidden manually by Excel end‑users and are not hidden by an AutoFilter. This makes it difficult to know which rows are hidden by the AutoFilter and which are hidden manually by Excel end‑users. Aspose.Cells for Node.js via C++ addresses this problem using the `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-). This method returns the row indices of all rows that are hidden by the AutoFilter and not manually by the Excel end‑user.  

## **Get All Hidden Rows Indices after Refreshing AutoFilter**  

Please see the following sample code that loads the [sample Excel file](64716909.xlsx) which contains some rows hidden manually by Excel end‑users. The code applies the AutoFilter and refreshes it using the `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-) method that returns the row indices of all rows hidden by the AutoFilter. It then prints the indices of the hidden rows on the console along with cell names and values.  

## **Sample Code**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.js" >}}

## **Console Output**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
