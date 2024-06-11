---
title: 在GridWeb中应用样式
type: docs
weight: 20
url: /zh/net/aspose-cells-gridweb/apply-styles-to-gridweb/
keywords: GridWeb,样式,样式
description: 本文介绍了如何在GridWeb中应用或设置样式。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb有自己的默认外观，但可以更改其外观。Aspose.Cells.GridWeb提供了多个属性，让开发人员完全控制其外观。本主题讨论了其中一些属性。

{{% /alert %}} 
## **将预设或自定义样式应用于Aspose.Cells.GridWeb**
### **预设样式**
为了节省开发人员的工作，Aspose.Cells.GridWeb提供了一些预设样式。只需从列表中选择样式以应用该样式。

|**样式**|**颜色方案**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
选择特定样式后，会改变GridWeb控件的整体外观。开发人员可以在设计时选择要应用于Grid的预设样式，但也可以使用Aspose.Cells.GridWeb的灵活API在运行时完成此任务。

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb控件由GridWeb类表示。

{{% /alert %}} 

要选择预设样式：

1. 将Aspose.Cells.GridWeb控件添加到Web表单。
1. 选择要应用于控件的预设样式。

GridWeb控件提供了PresetStyle属性，开发人员可以将任何所需的预设样式分配给它。

下面代码片段的输出显示如下。 

**GridWeb控件应用了Colorful1样式** 

![todo:image_alt_text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **标题栏样式**
如果您查看GridWeb控件，您会注意到两个标题栏。一个用于列（即A、B、C、D等），另一个用于行（即1、2、3、4等）。Aspose.Cells.GridWeb允许开发人员控制这些标题栏的外观。开发人员可以在设计时或运行时设置标题栏的样式。

{{% alert color="primary" %}} 

GridWeb控件提供了HeaderBarStyle属性，该属性应用于控件的两个标题栏。

{{% /alert %}} 

下面显示了示例代码的输出。 

**修改了标题栏的样式** 

![todo:image_alt_text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **选项卡栏样式**
可以设置选项卡栏的样式。 

**修改了活动和非活动选项卡栏的样式** 

![todo:image_alt_text](apply-styles-to-gridweb_3.png)

在上图中，Sheet4 是活动选项卡，因此它的外观与其他选项卡不同，如下面的示例代码所定义。





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **可重复使用的自定义样式文件**
Aspose.Cells.GridWeb 还支持将其外观或样式设置持久保存到文件中。当您设置了 GridWeb 控件的所有外观属性后，可以将这些属性或设置保存到磁盘文件。这种方法对开发人员非常有用，他们可以通过从样式文件中重新使用他们以前的样式配置而不是逐个设置控件的所有样式（或外观）属性来节省时间和精力。
### **保存样式文件**
一旦完成设置样式属性，您可以通过调用 GridWeb 控件的 SaveCustomStyleFile 方法将样式配置设置保存为 XML 文件格式（因为样式文件存储为 XML 文件）。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

保存的样式文件为 XML 格式，因此开发人员也可以使用任何文本编辑器编辑此文件（如果需要）。

{{% /alert %}} 
### **加载样式文件**
要将现有样式文件中的样式设置应用于 GridWeb 控件，开发人员可以将样式文件的路径设置为控件的 CustomStyleFileName 属性。但在这样做之前，必须将控件的 PresetStyle 属性设置为自定义。这是因为样式文件包含开发人员已经定义的自定义样式信息。

{{% alert color="primary" %}} 

还可以使用 Aspose.Cells.GridWeb Designer 加载或保存样式文件。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

重要提示：将样式文件加载到GridWeb控件中不会影响控件的单元格格式设置。

{{% /alert %}} 
### **XML 样式模板的标准格式**
{{< highlight java >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
