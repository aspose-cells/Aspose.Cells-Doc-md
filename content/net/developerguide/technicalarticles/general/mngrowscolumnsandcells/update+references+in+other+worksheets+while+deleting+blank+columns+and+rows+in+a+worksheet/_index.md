---
title : "Update references in other worksheets while deleting blank columns and rows in a worksheet" 
description : "" 
weight : 20495 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngrowscolumnsandcells/update+references+in+other+worksheets+while+deleting+blank+columns+and+rows+in+a+worksheet/
---

# Aspose.Cells for .NET : Update references in other worksheets while deleting blank columns and rows in a worksheet


When you delete blank columns and rows in a worksheet, then its references in other worksheets become invalid. If you want to avoid this behavior and want those references of the current worksheet in other worksheets are also updated, then please use the [DeleteOptions.UpdateReference](https://apireference.aspose.com/net/cells/aspose.cells/deleteoptions/properties/updatereference) property and set it to **true**.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Update references in other worksheets while deleting blank columns and rows in a worksheet](#update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet)
    *   1.1 [Programming Sample](#programming-sample)
    *   1.2 [Console Output](#console-output)
{{< /panel >}}
 

 

## Update references in other worksheets while deleting blank columns and rows in a worksheet

Please see the following sample code and its console output. The cell E3 in the second worksheet has a formula `=Sheet1!C3` which is referring to cell C3 in the first worksheet. If you will set [DeleteOptions.UpdateReference](https://apireference.aspose.com/net/cells/aspose.cells/deleteoptions/properties/updatereference) property as **true**, this formula will be updated and become `=Sheet1!A1` on deleting blank columns and rows in the first worksheet. However, if you will set [DeleteOptions.UpdateReference](https://apireference.aspose.com/net/cells/aspose.cells/deleteoptions/properties/updatereference) property as **false**, the formula in cell E3 of the second worksheet will remain `=Sheet1!C3` and become invalid.

### Programming Sample

### Console Output

This is the console output of the above sample code when [DeleteOptions.UpdateReference](https://apireference.aspose.com/net/cells/aspose.cells/deleteoptions/properties/updatereference) property has been set as **true**.

{{< code lang="cs" >}}
Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!A1
Cell Value: 4
{{< /code >}}

This is the console output of the above sample code when [DeleteOptions.UpdateReference](https://apireference.aspose.com/net/cells/aspose.cells/deleteoptions/properties/updatereference) property has been set as **false**. As you can see, the formula in cell E3 of the second worksheet is not updated and its cell value is now 0 instead of 4 which is invalid.

{{< code lang="cs" >}}
Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 0
{{< /code >}}

