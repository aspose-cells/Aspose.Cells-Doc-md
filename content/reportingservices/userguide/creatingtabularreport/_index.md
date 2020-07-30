---
title : "Creating Tabular Report" 
description : "" 
weight : 8062 
toc : false
type: docs
url: /reportingservices/userguide/creatingtabularreport/
---

# Aspose.Cells for Reporting Services : Creating Tabular Report


A table in an Aspose.Cells Report template consists of a header, table data rows, row groups and footers. A sample table is shown below.

**An example table**  
![](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193293.png)

#### Table Header

Table header normally contains the title for each table column and other text items such as static text, report parameters, global report variables and so on. The table header is optional. If using a header, the header tag should be placed to the left of the first column of table data to indicate that the row is a header.

#### Table Data Row

A table data row is a row of cells that contain smart markers. A table can only contain a single data row.

#### Row Group

The row group follows closely after the table data row and comprises two parts: group tag and group data row.

The group tag should be placed to the left of the first table data column to indicate that the row is the row group's data row. The format of the group tag is `##group{GroupColumn`}, for example `##group{SalesOrderNumber`} where `SalesOrderNumber` is one of the data set' column names. A table can only contain one row group, but a row group can contain more than one group data row. The group tag may be placed only in the first data row, as shown in the sample above.

The group tag is removed from the output Microsoft Excel file at rendering time. Row groups are optional.

#### Footers

Footers come after the row group and includes three parts: footer tag, footer data row and footer text area.

The footer tag should be placed on the left of the first column of the table data column that indicates the row is the table footer. A table can contain more than one footer data rows and each footer row has to be marked by a footer tag.

The footer text area can contain static text, report parameters and global report variables, as shown in the sample above.

The footer tag is removed from output Microsoft Excel file at rendering time. Footers are optional.

The output of the sample template is shown below.

**Sample template**  
![](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193290.png)

###### This section includes the following topics:  

*   [Preparing for Creating Table Report](https://docs2.aspose.com/cells/reportingservices/userguide/creatingtabularreport/preparing+for+creating+table+report)
*   [Adding base information for Table](https://docs2.aspose.com/cells/reportingservices/userguide/creatingtabularreport/adding+base+information+for+table)
*   [Adding Reporting Services Formulas](https://docs2.aspose.com/cells/reportingservices/userguide/creatingtabularreport/adding+reporting+services+formulas)
*   [Adding Table Group](https://docs2.aspose.com/cells/reportingservices/userguide/creatingtabularreport/adding+table+group)
*   [Adding Table Footers](https://docs2.aspose.com/cells/reportingservices/userguide/creatingtabularreport/adding+table+footers)
*   [Adding Report Parameters to Report](https://docs2.aspose.com/cells/reportingservices/userguide/creatingtabularreport/adding+report+parameters+to+report)
*   [Adding Reporting Services Global Variables to Report](https://docs2.aspose.com/cells/reportingservices/userguide/creatingtabularreport/adding+reporting+services+global+variables+to+report)
*   [Setting Report Attributes](https://docs2.aspose.com/cells/reportingservices/userguide/creatingtabularreport/setting+report+attributes)
*   [Modifying Report Attributes](https://docs2.aspose.com/cells/reportingservices/userguide/creatingtabularreport/modifying+report+attributes)

## Attachments:

![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating Tabular Report-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193293.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating Tabular Report-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193290.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Preparing for Creating Table Report-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193295.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Preparing for Creating Table Report-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193300.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Preparing for Creating Table Report-003.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193301.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Preparing for Creating Table Report-004.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193298.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating a new Table-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193309.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating a new Table-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193308.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating a new Table-003.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193311.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating a new Table-004.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193310.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating a new Table-005.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193313.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating a new Table-006.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193312.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating a new Table-007.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193315.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Reporting Services Formulas-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193321.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Reporting Services Formulas-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193320.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Reporting Services Formulas-003.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193322.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Reporting Services Formulas-004.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193323.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Reporting Services Formulas-005.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193324.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Table Group-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193330.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Table Group-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193331.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Table Group-003.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193332.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Table Group-004.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193333.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Table Group-005.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193334.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Table Footers-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193342.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Table Footers-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193341.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Table Footers-003.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193340.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Table Footers-004.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193339.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Table Footers-005.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193338.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Table Footers-006.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193353.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Report Parameters to Report-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193347.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Report Parameters to Report-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193346.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Report Parameters to Report-003.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193360.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Report Parameters to Report-004.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193361.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Report Parameters to Report-005.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193358.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Reporting Services Global Variables to Report-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193355.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Reporting Services Global Variables to Report-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193368.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Reporting Services Global Variables to Report-003.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193369.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Adding Reporting Services Global Variables to Report-004.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193366.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Setting Report Attributes-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193374.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Setting Report Attributes-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193377.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Setting Report Attributes-003.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193376.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Setting Report Attributes-004.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193371.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Setting Report Attributes-005.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193370.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Setting Report Attributes-006.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193373.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Modifying Report Attributes-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193385.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Modifying Report Attributes-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193384.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Modifying Report Attributes-003.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094957/6193379.png) (image/png)  

