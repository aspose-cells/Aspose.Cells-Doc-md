---
title: Parameterized Report
type: docs
weight: 60
url: /reportingservices/parameterized-report/
---

{{% alert color="primary" %}} 

A *parameterized report* is a report that accepts input values that are used when the report is processed. 

With a parameterized report, you can vary the output of a report based on the values that are set at run-time. Reporting Services supports two kinds of parameters: query parameters and report parameters. 

- **Query parameters** are used to select or filter data during data processing. If a query parameter is specified, a value must be provided either by the user or by default properties to complete the SELECT statement or stored procedure that retrieves data for a report.
- **Report parameters** are used during report processing to show a different aspect of the data. A report parameter is usually used to filter a large set of records, but it can have other uses depending on the queries and expressions in the report.

Report parameters differ from query parameters in that they are defined in a report and processed by the report server, while query parameters are defined as a part of the dataset query and processed on the database server. In Aspose.Cells.Report.Designer, query parameters are specified at query creating time in Microsoft Query. 

You can create report parameters and map query parameters to the corresponding report parameter in Aspose.Cells.Report.Designer. This way, it is possible to select values for report parameters and have them passed in the query to limit the data retrieved from the data source.

{{% /alert %}} 
###### **This section includes the following topics:** 
- [Creating Report Parameters](/cells/reportingservices/creating-report-parameters-html/)
- [Modifying Report Parameters](/cells/reportingservices/modifying-report-parameters-html/)
- [Mapping Query Parameters to Report Parameters](/cells/reportingservices/mapping-query-parameters-to-report-parameters-html/)
