---
title: Public API Changes in Aspose.Cells 8.7.2
type: docs
weight: 260
url: /java/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.7.1 to 8.7.2 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Extended the Default Calculation Engine**
Aspose.Cells APIs have powerful calculation engine that can calculate almost all of the Microsoft Excel functions. Moreover, the Aspose.Cells APIs now allow to extend the default calculation engine to meet custom calculation requirements of any application.

Following APIs have been added with the release of Aspose.Cells for Java 8.7.2.

1. AbstractCalculationEngine Class
1. CalculationData Class
1. CalculationOptions.CustomEngine Property

{{% alert color="primary" %}} 

Above mentioned APIs allow to implement custom calculation engine for all functions (including Excel's native functions) with more flexibility.

{{% /alert %}} {{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Implementing Custom Calculation Engine](/cells/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

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

{{< /highlight >}}
### **Added Overloaded Indexer for TextBoxCollection**
Aspose.Cells for Java 8.7.2 has exposed the overloaded indexer for the TextBoxCollection class in order to access the instance of TextBox using its name as String.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Accessing the TextBox via its Name](/cells/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

Simple usage scenario looks as follow. 

**Java**

{{< highlight csharp >}}

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

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}