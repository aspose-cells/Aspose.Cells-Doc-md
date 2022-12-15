---
title: 将样式应用于 GridWeb
type: docs
weight: 20
url: /zh/net/apply-styles-to-gridweb/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 有自己的默认外观，但可以更改其外观。 Aspose.Cells.GridWeb 提供了几个属性让开发者完全控制它的外观。本主题讨论其中一些属性。

{{% /alert %}} 
## **将预设或自定义样式应用于 Aspose.Cells.GridWeb**
### **预设样式**
为了节省开发者的精力，Aspose.Cells.GridWeb 提供了一些预设样式。只需从列表中选择一种样式即可应用该样式。

|**样式**|**配色方案**|
|:- |:- |
|标准|银|
|炫彩1|玫瑰|
|炫彩2|蓝色的|
|专业1|青色|
|专业2|又是青色|
|传统1|黑暗的|
|传统2|灰色的|
|风俗|定制|
选择特定样式时，它会更改 GridWeb 控件的整体外观。开发人员可以在设计时选择要应用于 Grid 的预设样式，但此任务也可以在运行时使用 Aspose.Cells.GridWeb 的灵活 API 完成。

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb控件由GridWeb类表示。

{{% /alert %}} 

选择预设样式：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 选择要应用于控件的预设样式。

GridWeb 控件提供 PresetStyle 属性，开发人员可以将任何所需的预设样式分配给该属性。

以下代码片段的输出如下所示。

**应用了 Colorful1 样式的 GridWeb 控件** 

![待办事项：图像_替代_文本](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **标题栏样式**
如果您查看 GridWeb 控件，您会注意到两个标题栏。一个用于列（即 A、B、C、D 等），另一个用于行（即 1、2、3、4 等）。 Aspose.Cells.GridWeb 允许开发人员控制这些标题栏的外观。开发人员可以在设计时或运行时设置标题栏的样式。

{{% alert color="primary" %}} 

GridWeb 控件提供了 HeaderBarStyle 属性，该属性在控件的两个标题栏上应用样式。

{{% /alert %}} 

以下示例代码的输出显示在此处。

**Header Bar 修改样式** 

![待办事项：图像_替代_文本](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **标签栏样式**
可以设置标签栏的样式。

**活动和非活动标签栏的修改样式** 

![待办事项：图像_替代_文本](apply-styles-to-gridweb_3.png)

在上图中，Sheet4 是活动选项卡，因此它的外观与其他选项卡不同，如下面的示例代码所定义。





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **可重复使用的自定义样式文件**
Aspose.Cells.GridWeb 还支持将其外观或样式设置保存到文件中。当您设置了 GridWeb 控件的所有外观属性后，您可以将这些属性或设置保存到磁盘文件中。这种方法对于开发人员非常有用，可以通过重新使用样式文件中的旧样式配置而不是一个一个地设置控件的所有样式（或外观）属性来节省时间和精力。
### **保存伴奏文件**
完成样式属性设置后，您可以通过调用 GridWeb 控件的 SaveCustomStyleFile 方法以 XML 文件的形式保存样式配置设置（这是因为该样式文件存储为 XML 文件）。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

保存的样式文件为 XML 格式，因此开发人员也可以根据需要使用任何文本编辑器编辑此文件。

{{% /alert %}} 
### **加载样式文件**
要将现有样式文件中的样式设置应用于 GridWeb 控件，开发人员可以将样式文件的路径设置为控件的 CustomStyleFileName 属性。但是，在这样做之前必须将控件的 PresetStyle 属性设置为 Custom。这是因为该样式文件包含开发人员已经定义的自定义样式信息。

{{% alert color="primary" %}} 

也可以使用 Aspose.Cells.GridWeb Designer 加载或保存样式文件。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

重要提示：将样式文件加载到 GridWeb 控件中不会影响控件单元格的格式设置。

{{% /alert %}} 
### **XML样式模板标准格式**
{{< highlight "java" >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
