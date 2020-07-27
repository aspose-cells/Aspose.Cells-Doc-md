+++
title = "Check Password to modify using Aspose.Cells" 
description = "" 
weight = 16433 
+++

Aspose.Cells for Java : Check Password to modify using Aspose.Cells  

# Aspose.Cells for Java : Check Password to modify using Aspose.Cells


You can assign a **Password to open** and a **Password to modify** while creating your workbooks in Microsoft Excel. Please see this screenshot which shows the interface Microsoft Excel provides to specify these passwords.

![](https://docs2.aspose.com/cells/java/attachments/5276699/5473056.png)

Sometimes, you need to check if the given password matches with the **Password to modify** programmatically. Aspose.Cells provides [workbook.getSettings().getWriteProtection().validatePassword()](https://apireference.aspose.com/java/cells/com.aspose.cells/writeprotection#validatePassword(java.lang.String)) method which you can use to check if the given Password to modify is correct or not.

#### Check Password to modify using Aspose.Cells

The following sample codes load the [source Excel](https://docs2.aspose.com/cells/java/attachments/5276699/5473057.xlsx) file. It has a Password to open as 1234 and Password to modify as 5678. The code first checks if 567 is correct Password to modify and it returns false and then it checks if 5678 is Password to modify and it returns true.


#### Console Output

Here is the Console Output of the above sample code after loading the [source Excel](https://docs2.aspose.com/cells/java/attachments/5276699/5473057.xlsx) file.

{{< code lang="cs" >}}
Is 567 correct Password to modify: false
Is 5678 correct Password to modify: true
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Book1.xlsx](https://docs2.aspose.com/cells/java/attachments/5276699/5473057.xlsx) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Specify passwords while saving workbook.png](https://docs2.aspose.com/cells/java/attachments/5276699/5473056.png) (image/png)  

