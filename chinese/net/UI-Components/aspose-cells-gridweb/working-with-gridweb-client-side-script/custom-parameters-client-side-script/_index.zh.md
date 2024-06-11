---
title: 自定义初始化参数
type: docs
weight: 10
url: /zh/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
keywords: GridWeb，自定义，自定义参数
description: 如何在Aspose.Cells.GridWeb客户端脚本中自定义初始化参数。
---

{{% alert color="primary" %}} 

开发人员可以在acwmain.js中设置不同的初始化参数值，以执行Aspose.Cells.GridWeb控件的不同行为。  

{{% /alert %}} 

### **参数**

|**参数**|**描述**|
| :- | :- |
|needInitAlignmentAdjust| 是否在初始化时对单元格内容进行垂直对齐，这会导致在工作表存在大单元格时需要花费一些时间进行对齐工作，如果用户不关心垂直对齐，则可以将其设置为false，默认值为true。
|focusinside| 是否聚焦在单元格跨度内，默认值为true。
|copy_with_style| 是否复制样式，默认值为false，这意味着仅复制单元格内容。
|useESCAsLeave| 按下esc键时的默认行为是取消对单元格的编辑操作，如果将此值设为true，则仅将其视为离开单元格的快捷键，不会改变回到先前值的编辑方式，并且还将改变内部编辑方式为快速编辑方式，默认值为false。
|needValidateall| 在进行验证时是否验证活动工作表上的所有验证（在aspx控件页设置ForceValidation="True"）。默认值为false。
|scrollToInvalidate| 是否在needValidateall设置为true时滚动并将第一个无效单元格带入视图。默认值为true。


下面是代码示例的输出，请查看[示例Excel文件](valign.xlsx)：

**needInitAlignmentAdjust=true** 

![todo:image_alt_text](align_true.png)

**needInitAlignmentAdjust=false** 

![todo:image_alt_text](align_false.png)

**focusinside=true** 
内部编辑方式——输入文本时，旧的单元格值仍保留。   

![todo:image_alt_text](focus_inside_true.png)

**focusinside=false** 
快速编辑方式——输入文本时，旧的单元格值将被覆盖，如果要基于旧的单元格值进行编辑，可以单击单元格。

![todo:image_alt_text](focus_inside_false.png)



