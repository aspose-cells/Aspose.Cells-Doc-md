---
title: How to Filter Blanks or Non-Blanks
type: docs
weight: 85
url: /nodejs-cpp/how-to-filter-blanks-and-non-blanks/
description: Learn how to filter blanks and non-blanks by using the Aspose.Cells for Node.js via C++ API.
keywords: Filter Blanks, Filter Non-Blanks, Filter Blanks in worksheet, Filter Non-Blanks in worksheet, Filter Blanks in excel, Filter Non-Blanks in excel, Filter Blanks and Non-Blanks in excel
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Filtering data in Excel is a valuable tool that enhances data analysis, exploration, and presentation by enabling users to focus on specific subsets of data based on their criteria, making the overall data manipulation and interpretation process more efficient and effective.

## **How to Filter Blanks or Non-Blanks in Excel**
In Excel, you can easily filter blanks or non-blanks using the filtering options. Here's how you can do it:

### **How to Filter Blanks in Excel**
1. **Select the Range:** Click on the letter of the column header to select the entire column or select the range where you want to filter blanks.  
2. **Open the Filter Menu:** Go to the **Data** tab in the ribbon.  
   <br>
   <image src="1.png" width="70%" />
3. **Filter Options:** Click on the **Filter** button. This will add filter arrows to the selected range.  
4. **Filter Blanks:** Click on the filter arrow in the column you want to filter blanks. Unselect all options except **Blanks** and click **OK**. This will display only the blank cells in that column.  
   <br>
   <image src="2.png" width="70%" />
5. **The result is as follows:**  
   <br>
   <image src="3.png" width="70%" />

### **How to Filter Non-Blanks in Excel**
1. **Select the Range:** Click on the letter of the column header to select the entire column or select the range where you want to filter non-blanks.  
2. **Open the Filter Menu:** Go to the **Data** tab in the ribbon.  
   <br>
   <image src="1.png" width="70%" />
3. **Filter Options:** Click on the **Filter** button. This will add filter arrows to the selected range.  
4. **Filter Non-Blanks:** Click on the filter arrow in the column you want to filter non-blanks. Unselect all options except **Non-Blanks** or **Custom** and set the conditions accordingly. Click **OK**. This will display only the cells that are not blank in that column.  
   <br>
   <image src="4.png" width="70%" />
5. **The result is as follows:**  
   <br>
   <image src="5.png" width="70%" />

## **How to Filter Blanks using Aspose.Cells for Node.js via C++**
If a column contains text and only a few cells are blank, and you need to filter rows where the cells are blank, you can use the [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchBlanks-number-) and [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#addFilter-number-string-) functions as demonstrated below.

Please see the following sample code that loads the [sample Excel file](sample.xlsx) containing some dummy data. The sample code uses three methods to filter blanks and then saves the workbook as the [output Excel file](FilteredBlanks.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterBlanks.js" >}}

## **How to Filter Non-Blanks using Aspose.Cells for Node.js via C++**

Please see the following sample code that loads the [sample Excel file](sample.xlsx) containing some dummy data. After loading the file, call the [**AutoFilter.matchNonBlanks(number)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchNonBlanks-number-) function to filter non‑blank data, and finally save the workbook as the [output Excel file](FilteredNonBlanks.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterNonBlanks.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
