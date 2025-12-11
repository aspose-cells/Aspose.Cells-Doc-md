---
title: Customize initialization parameters
type: docs
weight: 10
url: /net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
keywords: GridWeb,customize,customize parameters
description: how to customize initialization parameters in Aspose.Cells.GridWeb client side script.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Developers can set different initialization parameter values to achieve different behavior for the Aspose.Cells.GridWeb control in acwmain.js.  

{{% /alert %}} 

### **Parameters**

| **Parameter**           | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| needInitAlignmentAdjust | Whether to do vertical alignment for cell content at initialization. It will take some time to perform the alignment work; if the worksheet has large cells, the performance will be poor. If the user does not care about the vertical alignment, then he can set it to false. The default value is true.                                                                                                                                                                                                                                                                     |
| focusinside             | Whether to focus inside the cell span. The default value is true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| copy_with_style         | Whether to copy with style. The default value is false, which means only the cell content is copied.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| useESCAsLeave           | The default behavior when pressing Esc works as canceling the edit operation on a cell. If we set this value to true, we will treat it as a shortcut to leave the cell without reverting to the previous value, and it will also change the internal edit mode to fast edit mode. The default value is false.                                                                                                                                                                                                                                                    |
| needValidateall         | Whether to validate all the validations on the active sheet when performing validation (in ASPX control page set `ForceValidation="True"`). The default value is false.                                                                                                                                                                                                                                                                                                                                                                                                |
| scrollToInvalidate      | Whether to scroll and bring the first invalid cell into view when `needValidateall` is set to true. The default value is true.                                                                                                                                                                                                                                                                                                                                                                                                                                          |

The output of the code example is shown below, please check the [sample Excel file](valign.xlsx):

**needInitAlignmentAdjust=true**

![todo:image_alt_text](align_true.png)

**needInitAlignmentAdjust=false**

![todo:image_alt_text](align_false.png)

**focusinside=true**  
inside edit mode — when entering text, the old cell value will remain  

![todo:image_alt_text](focus_inside_true.png)

**focusinside=false**  
fast edit mode — when entering text, the old cell value will be overwritten. If you want to edit based on the old cell value, you can click on the cell  

![todo:image_alt_text](focus_inside_false.png)
