---
title: Preface
type: docs
weight: 20
url: /reportingservices/preface/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services mainly contains two components : Aspose.Cells.Report.Designer and Aspose.Cells.Renderer for Reporting Services. The former is used to design reports directly in Microsoft Excel and the latter is responsible for rendering a RDL report to Microsoft Excel. 

{{% /alert %}} 
### **Designing a Report with the Report Designer**
The main steps to design a report using Aspose.Cells.Report.Designer are:

1. **Create data sources and queries**.
   Microsoft Query is integrated with Aspose.Cells.Report.Designer and used as a graphic tool to create data sources and queries. Users can also make use of an existing RDL file in which data sources and queries are available for operations.
1. **Map parameters**.
   If the SQL statements of a query include parameters, users have to create report parameters and map SQL parameters to report parameters. You can designate valid values for a report parameter in Aspose.Cells.Report.Designer.
1. **Design Microsoft Excel report template contents, styles and formats**.
   An Aspose.Cells report template may contain any number of the following types of report items: 
   1. Table
   1. Pivot table
   1. Chart
   1. Textbox
   1. Matrix
      Normally a query (that is, DataSet) is used as a data source for report item. You can also use Reporting Services parameters, formulas and global variables as a data source for some types of report items. The styles and formats of report items are specified simply by setting the styles and formats of the cells that compose the report items.
1. **Publish report**.
   After the above steps, the report is ready to publish. Users can designate which folder the report is published to. If needed, you can assign a shared data source on the Report Server as the data source for the report.
1. **Preview report**.
   When selecting a report for preview on the Report Server, you are prompted to specify which file format to export it to (for example Microsoft Excel 97-2003 binary XLS format, SpreadsheetML or Microsoft Excel 2007 XLSX format), and any input report parameters created during the report design. After this, the report is populated with data supplied by Reporting Services.
