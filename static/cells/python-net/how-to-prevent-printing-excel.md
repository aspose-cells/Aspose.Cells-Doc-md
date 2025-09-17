##How to Prevent Users from Printing Excel File
Learn how to How to prevent users from printing excel through the Aspose.Cells for Python via .NET API.
## **Possible Usage Scenarios**
In our daily work, there may be some important information in the excel file, in order to protect the internal data outspread, the company will not allow us to print them. This document will tell you how to prevent others from printing Excel files.
## **How to Prevent Users from Printing File in MS-Excel**
You can apply the following VBA code to protect your specific file to be printed.
1. Open your workbook which you don’t allow others to print.
1. Select "Developer" tab tab in the Excel ribbon and Click on the "View Code" button in the "Controls" section. Alternatively, you can hold down the ALT + F11 keys to open the Microsoft Visual Basic for Applications window.
1. And then in the left Project Explorer, double click ThisWorkbook to open the module, and add some vba codes.
1. Then save and close this code, and go to back the workbook, and now when you print the sample file, they will not allowed to be printed and you will get the following warning box:
## **How to Prevent Users from Printing Excel File using Aspose.Cells for Python via .NET**
The following sample code illustrates how to prevent users from printing excel file:
1. Load the [sample file](sample.xlsx).
1. Get the VbaModuleCollection object from VbaProject property of Workbook.
1. Get VbaModule object via "ThisWorkbook" name.
1. Set the codes property of VbaModule.
1. Save the sample file to [xlsm format](out.xlsm).
