---
title : "Public API Changes in Aspose.Cells 8.7.2" 
description : "" 
weight : 12311 
toc : false
type: docs
url: /java/developerguide/migratingfromearliervs/public+api+changes+in+aspose.cells+8.7.2/
---

# Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.7.2


This document describes the changes to the Aspose.Cells API from version 8.7.1 to 8.7.2 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Extended the Default Calculation Engine

Aspose.Cells APIs have powerful calculation engine that can calculate almost all of the Microsoft Excel functions. Moreover, the Aspose.Cells APIs now allow to extend the default calculation engine to meet custom calculation requirements of any application.

Following APIs have been added with the release of Aspose.Cells for Java 8.7.2.

1.  `AbstractCalculationEngine` Class
2.  `CalculationData` Class
3.  `CalculationOptions.CustomEngine` Property

Above mentioned APIs allow to implement custom calculation engine for all functions (including Excel's native functions) with more flexibility.

For more details on this feature, please review the detailed article on [Implementing Custom Calculation Engine](http://www.aspose.com/docs/display/cellsjava/Implement+Custom+Calculation+Engine+to+extend+the+Default+Calculation+Engine+of+Aspose.Cells)

Following is the simple usage scenario.

**Java**

{{< code lang="java" >}}
public class CustomEngine extends AbstractCalculationEngine
{
	public void calculate(CalculationData data)
        {
		if(data.getFunctionName().toUpperCase().equals("SUM")==true)
                {
                    double val = (double)data.getCalculatedValue();
                    val = val + 30;

                    data.setCalculatedValue(val);
                }
        }
}
{{< /code >}}

### Added Overloaded Indexer for TextBoxCollection

Aspose.Cells for Java 8.7.2 has exposed the overloaded indexer for the `TextBoxCollection` class in order to access the instance of `TextBox` using its name as `String`.

For more details on this feature, please review the detailed article on [Accessing the TextBox via its Name](http://www.aspose.com/docs/display/cellsjava/Access+the+Text+Box+by+the+Name)

Simple usage scenario looks as follow.

**Java**

{{< code lang="java" >}}
//Create an instance of Workbook
Workbook workbook = new Workbook();

//Access the first Worksheet from the collection
Worksheet sheet = workbook.getWorksheets().get(0);

//Add a TextBox to the collection
int idx = sheet.getTextBoxes().add(10, 10, 10, 10);

//Access the TextBox using its index
TextBox box = sheet.getTextBoxes().get(idx);

//Set the name for the TextBox
box.setName("MyTextBox");

//Access the same TextBox via its name
box = sheet.getTextBoxes().get("MyTextBox");
{{< /code >}}

