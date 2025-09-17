##How to Filter Blanks or Non-Blanks
Learn how to filter Blanks and non-blanks by using the Aspose.Cells for Node.js via C++ API.
## **Possible Usage Scenarios**
Filtering data in Excel is a valuable tool that enhances data analysis, exploration, and presentation by enabling users to focus on specific subsets of data based on their criteria, making the overall data manipulation and interpretation process more efficient and effective.
## **How to Filter Blanks or Non-Blanks in Excel**
In Excel, you can easily filter blanks or non-blanks using the filtering options. Here's how you can do it:
### **How to Filter Blanks in Excel**
1. Select the Range: Click on the letter of the column header to select the entire column or select the range where you want to filter blanks.
1. Open the Filter Menu: Go to the "Data" tab in the ribbon.
1. Filter Options: Click on the "Filter" button. This will add filter arrows to the selected range.
1. Filter Blanks: Click on the filter arrow in the column you want to filter blanks. Unselect all options except "Blanks" and click OK. This will display only the blank cells in that column.
1. The result as follows:
### **How to Filter Non-Blanks in Excel**
1. Select the Range: Click on the letter of the column header to select the entire column or select the range where you want to filter non-blanks.
1. Open the Filter Menu: Go to the "Data" tab in the ribbon.
1. Filter Options: Click on the "Filter" button. This will add filter arrows to the selected range.
1. Filter Non-Blanks: Click on the filter arrow in the column you want to filter non-blanks. Unselect all options except "Non-blanks" or "Custom" and set the conditions accordingly. Click OK. This will display only the cells that are not blank in that column.
1. The result as follows:
## **How to Filter Blanks using Aspose.Cells for Node.js via C++**
If a column contains text such that few cells are blank, and filter is required to select those rows only where blank cells are present, [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchBlanks-number-) and [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#addFilter-number-string-) functions can be used as demonstrated below.
Please see the following sample code that loads the [sample Excel file](sample.xlsx) which contains some dummy data. The sample code uses three methods to filter blanks. It then saves the workbook as [output Excel file](FilteredBlanks.xlsx).
## **How to Filter Non-Blanks using Aspose.Cells for Node.js via C++**
Please see the following sample code that loads the [sample Excel file](sample.xlsx) which contains some dummy data. After loading the file, call the [AutoFilter.matchNonBlanks(number)](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchNonBlanks-number-) function to filter non-blank data, and finally save the workbook as [output Excel file](FilteredNonBlanks.xlsx).
