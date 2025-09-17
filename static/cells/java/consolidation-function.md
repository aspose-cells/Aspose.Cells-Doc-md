##Consolidation Function
Apply ConsolidationFunction to data fields of the pivot table.
## **Consolidation function**
Aspose.Cells can be used to apply ConsolidationFunction to data fields (or value fields) of the pivot table. In Microsoft Excel, you can right-click the value field and then select **Value Field Settings...** option and then select the tab **Summarize Values By**. From there, you can select any ConsolidationFunction of your choice like Sum, Count, Average, Max, Min, Product, Distinct Count, etc.
Aspose.Cells provides [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) enumeration to support the following consolidation functions.
- ConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP
- ConsolidationFunction.DISTINCT_COUNT
### **Applying ConsolidationFunction to Data Fields of Pivot Table**
The following code applies **AVERAGE** consolidation function to the first data field (or value field) and **STD_DEV** consolidation function to the second data field (or value field).
Sample source file and output files can be downloaded from here for testing the sample code:
[Source Excel File](source.xlsx)
[Output Excel File](output.xlsx)
DistinctCount consolidation function is supported by Microsoft Excel 2013 only.
