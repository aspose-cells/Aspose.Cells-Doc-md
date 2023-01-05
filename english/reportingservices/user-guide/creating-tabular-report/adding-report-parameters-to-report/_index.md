---
title: Adding Report Parameters to Report
type: docs
weight: 60
url: /reportingservices/adding-report-parameters-to-report/
---

{{% alert color="primary" %}} 

Aspose.Cells' report template supports Reporting Services report parameters as a data source for cells that contains a Reporting Services parameter marker. Please refer to [Aspose.Cells Template and Smart Markers](/cells/reportingservices/aspose-cells-template-and-smart-markers/) to learn about Reporting Services parameter markers. Report parameters are normally placed in the text area of table header or footer.

{{% /alert %}} 
### **Adding a Report Parameter**
To add report parameters to reports:

1. Select a cell. 

   **Selecting a cell** 

![todo:image_alt_text](adding-report-parameters-to-report_1.png)




1. Click Insert formula on the Aspose.Cells.Report.Designer toolbar (

![todo:image_alt_text](adding-report-parameters-to-report_2.png)

).

1. Select **Parameters** from the Parameters panel to the left.
   All the parameters are listed in the right panel. 
1. Select a parameter, in the example, we've selected EmpID.
1. Double-click the parameter to make the expression appear in the editor at the top of the form.
   A parameter has two data attributes: label and value (the default attribute is value). 

   **Selecting a parameter** 

![todo:image_alt_text](adding-report-parameters-to-report_3.png)




1. In the sample, the parameter's label should be shown in the report, so modify the expression to Parameters!EmpID.Label. 

   **Modifying the parameter** 

![todo:image_alt_text](adding-report-parameters-to-report_4.png)




1. Click **OK**.
   The selected cell contains a report parameters marker. 

   **A report parameter inserted into the cell** 

![todo:image_alt_text](adding-report-parameters-to-report_5.png)
