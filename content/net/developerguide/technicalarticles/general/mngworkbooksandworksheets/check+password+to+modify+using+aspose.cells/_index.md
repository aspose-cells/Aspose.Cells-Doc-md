---
title : "Check Password to modify using Aspose.Cells" 
description : "" 
weight : 20445 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngworkbooksandworksheets/check+password+to+modify+using+aspose.cells/
---

# Aspose.Cells for .NET : Check Password to modify using Aspose.Cells


Sometimes, you need to check if the given password matches with the **Password to modify** programmatically. Aspose.Cells provides `Workbook``Settings.WriteProtection.ValidatePassword()` method which you can use to check if the given Password to modify is correct or not.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Check Password to modify in Microsoft Excel](#check-password-to-modify-in-microsoft-excel)
*   2 [Check Password to modify using Aspose.Cells](#check-password-to-modify-using-aspose.cells)
    *   2.1 [Console Output](#console-output)
{{< /panel >}}
 

 

## Check Password to modify in Microsoft Excel

You can assign **Password to open** and **Password to modify** while creating your workbooks in Microsoft Excel. Please see this screenshot which shows the interface Microsoft Excel provides to specify these passwords.

![](https://docs2.aspose.com/cells/net/attachments/5017659/5112231.png)

## Check Password to modify using Aspose.Cells

The following sample codes load the [source Excel](https://docs2.aspose.com/cells/net/attachments/5017659/5112232.xlsx) file. It has a Password to open as 1234 and Password to modify as 5678. The code first checks if 567 is correct Password to modify and it returns false and then it checks if 5678 is Password to modify and it returns true.

### Console Output

Here is the Console Output of the above sample code after loading the [source Excel](https://docs2.aspose.com/cells/net/attachments/5017659/5112232.xlsx) file.

{{< code lang="cs" >}}
Is 567 correct Password to modify: False
Is 5678 correct Password to modify: True
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Specify passwords while saving workbook.png](https://docs2.aspose.com/cells/net/attachments/5017659/5112231.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Book1.xlsx](https://docs2.aspose.com/cells/net/attachments/5017659/5112232.xlsx) (image/png)  

