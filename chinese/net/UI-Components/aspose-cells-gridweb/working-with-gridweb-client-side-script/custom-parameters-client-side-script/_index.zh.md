---
title: 自定义初始化参数
type: docs
weight: 10
url: /zh/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
description: 如何在 Aspose.Cells.GridWeb 客户端脚本中自定义初始化参数。
---
{{% alert color="primary" %}} 

开发人员可以为 acwmain.js 中的 Aspose.Cells.GridWeb 控件设置不同的初始化参数值以执行不同的行为。

{{% /alert %}} 
 
### **参数**
 
|**范围**|**描述**|
|:- |:- |
|需要InitAlignmentAdjust|是否在初始化时对单元格内容做垂直对齐，会导致对齐需要一定的时间，如果工作表的单元格很大，性能会很差，如果用户不关心垂直对齐，那么可以设置为为假，默认值为真|
|专注于内心|是否聚焦在cell span内，默认为true|
|复制_和_风格|是否带样式复制，默认为false，表示只复制单元格内容|
|使用ESCA离开|按esc时的默认行为相当于取消对单元格的编辑操作，如果我们将此值设置为true，我们将把它当作一个快捷键来离开单元格而不改变回以前的值，它也会改变内部编辑方式快速编辑方式，默认为false|
|需要验证所有|验证时是否验证活动工作表上的所有验证，（在aspx控制页面中设置ForceValidation="True"）。默认值为 false|
|滚动到无效|当 needValidateall 设置为 true 时是否滚动并将第一个无效单元格带入视图。默认值为 true。|
 
 
代码示例的输出如下所示，请检查[示例 excel 文件](valign.xlsx):

**needInitAlignmentAdjust=真** 

![待办事项：图片_替代_文本](align_true.png)

**needInitAlignmentAdjust=假** 

![待办事项：图片_替代_文本](align_false.png)

**focusinside=真** 
内部编辑方式——输入文本时，旧的单元格值仍然保留

![待办事项：图片_替代_文本](focus_inside_true.png)

**focusinside=假** 
快速编辑方式——输入文本时，旧的单元格值将被覆盖，如果你想根据旧的单元格值进行编辑，你可以点击单元格

![待办事项：图片_替代_文本](focus_inside_false.png)

 
 