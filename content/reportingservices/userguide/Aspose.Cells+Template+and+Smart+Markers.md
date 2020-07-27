+++
title = "Aspose.Cells Template and Smart Markers" 
description = "" 
weight = 8051 
+++

Aspose.Cells for Reporting Services : Aspose.Cells Template and Smart Markers  

# Aspose.Cells for Reporting Services : Aspose.Cells Template and Smart Markers


An Aspose.Cells template is a Microsoft Excel workbook that contains Smart Markers. Smart Markers acts as data placeholder for report items and are replaced with the corresponding data at rendering time. There are five types of smart markers, listed as below. All the markers can be inserted into a template by Aspose.Cells.Report.Designer. The can also be edited manually.

### Smart Markers

#### Data Markers

The format of **data markers** is `&=DataSetName.FieldName`. For example: `&=SalesDetail.sales` where `SalesDetail` is the name of a data set or query and `sales` is the name of one of its fields. At rendering time, data markers are replaced with the values of dataset provided by Reporting Services.

#### Reporting Services Formulas Markers

The format of Reporting Services' **formulas markers** is `&=expression`. For example: `&=sum(SalesDetail.sales)/100`. The expression consists of function, dataset fields, operator and so on. At rendering time. Reporting Services formulas markers are replaced with computed values.

#### Reporting Services Global Variable Markers

The format of Reporting Services' **global variable markers** is `&=Globals! Variable Name`. For example: `&=Globals!ExecutionTime` where `ExecutionTime` is the name of a global variable. Global variable markers are replaced with global variable values at rendering time.

#### Reporting Services Parameters Markers

A report parameter has two attributes: value and label. Consequently, **parameters markers** have two formats: `&= Parameters! ParamName.Value` and `&=Parameters! ParamName.Label`. They indicate the name and the label of the parameter respectively. At rendering time, parameters markers are replaced with the parameter values entered by the user.

#### Dynamic Formulas

In order to make calculations on inserterd rows, use dynamic formulas. **Dynamic formulas** allow you to insert Microsoft Excel's formulas into cells even when a formula references rows that will be inserted during the export process. They can be repeated for each inserted row or used only with cells where data markers are placed for them.

The format of dynamic formulas is `&=&=RepeatDynamicFormula`.

Dynamic Formulas allow the following additional options:

*   {r} – Current row number.
*   {2}, {-1} – Offset to current row number.

**A repeating dynamic formula and the resulting Excel worksheet**  
![](https://docs2.aspose.com/cells/reportingservices/attachments/6094949/6193436.png)

## Attachments:

![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Aspose.Cells Template and Smart Markers-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094949/6193436.png) (image/png)  

