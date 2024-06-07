---
title: 自定义初始化参数
type: docs
weight: 10
url: /zh/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
keywords: GridWeb，自定义，自定义参数
description: 如何在Aspose.Cells.GridWeb客户端脚本中自定义初始化参数。
---

{{% alert color="primary" %}} 

开发人员可以设置不同的初始化参数值，以执行Aspose.Cells.GridWeb控件的不同行为。（acwmain.js）  

{{% /alert %}} 

### **参数**

|参数|描述|
| :- | :- |
|needInitAlignmentAdjust|是否在初始化时为单元格内容进行垂直对齐，这会导致执行对齐操作需要一些时间，如果工作表具有大单元格，则性能会较差，如果用户不关心垂直对齐，则可以将其设置为 false， 默认值为 true。|
|focusinside|是否在单元格范围内聚焦，默认值为 true。|
|copy_with_style|是否复制样式，默认值为 false，表示仅复制单元格内容。|
|useESCAsLeave|按下 Esc 键时的默认行为是取消编辑操作，如果将此值设置为 true，则将其视为离开单元格的快捷键，并且快速编辑方式也会改变，默认值为 false。|
|needValidateall|是否验证活动工作表上的所有验证项，进行验证时（在 aspx 控件页上设置 ForceValidation="True"）默认值为 false。|
|scrollToInvalidate|是否滚动并将第一个无效单元格带入视图，需要将 needValidateall 设置为 true 时。默认值为 true。|


代码示例的输出如下，请查看[示例Excel文件](valign.xlsx):

**needInitAlignmentAdjust=true** 

![todo:image_alt_text](align_true.png)

**needInitAlignmentAdjust=false** 

![todo:image_alt_text](align_false.png)

**focusinside=true** 
内部编辑方式--输入文本时，旧单元格值将保持不变   

![todo:image_alt_text](focus_inside_true.png)

**focusinside=false** 
快速编辑方式--输入文本时，旧单元格值将被覆盖，如果想基于旧单元格值进行编辑，可以单击单元格

![todo:image_alt_text](focus_inside_false.png)



