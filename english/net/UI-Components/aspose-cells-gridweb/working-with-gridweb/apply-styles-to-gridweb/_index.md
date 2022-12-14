---
title: Apply Styles to GridWeb
type: docs
weight: 20
url: /net/apply-styles-to-gridweb/
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb has its own default look & feel but it is possible to change its appearance. Aspose.Cells.GridWeb provides several properties to let developers fully control its appearance. This topic discusses some of those properties.

{{% /alert %}} 
## **Applying Preset or Custom Styles to Aspose.Cells.GridWeb**
### **Preset Styles**
To save the efforts of developers, Aspose.Cells.GridWeb offers some preset styles. Simply select a style from the list to apply the style.

|**Styles**|**Color Scheme**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
When a particular style is selected, it changes the whole appearance of the GridWeb control. Developers can select a Preset Style to be applied on Grid during design time but this task can also be accomplished at runtime using the flexible API of Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb control is represented by GridWeb class.

{{% /alert %}} 

To select a preset style:

1. Add Aspose.Cells.GridWeb control to a web form.
1. Select a preset style to be applied on the control.

The GridWeb control provides the PresetStyle property to which developers can assign any desired preset style.

The output of the below code snippet is shown below. 

**GridWeb control with Colorful1 style applied on it** 

![todo:image_alt_text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Header Bar Style**
If you take a look at the GridWeb control, you'll notice two header bars. One for columns (that is A, B, C, D etc.) and other for rows (that is 1, 2, 3, 4 etc.). Aspose.Cells.GridWeb allows developers to control the appearance of these header bars. Developers may set the style of header bars either at design time or runtime.

{{% alert color="primary" %}} 

The GridWeb control provides the HeaderBarStyle property that applies a style on both header bars of the control.

{{% /alert %}} 

The output the example code below is shown here. 

**Modified style of Header Bar** 

![todo:image_alt_text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Tab Bar Style**
It's possible to set the style of the tab bar. 

**Modified styles of active & non-active tab bars** 

![todo:image_alt_text](apply-styles-to-gridweb_3.png)

In the above figure, Sheet4 is the active tab so its appearance is different from the other tabs, as defined by the example code below.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **Reusable Customized Style File**
Aspose.Cells.GridWeb also supports to persist its appearance or style settings to a file. When you have set all the appearance properties of the GridWeb control, you may save these properties or settings to a disk file. This approach is very useful for developers to save their time and efforts by re-using their old style configurations from a style file instead of setting all style (or appearance) properties of the control one by one.
### **Saving Style File**
Once you have finished setting style properties, you can save your style configuration settings in the form of an XML file (it is because that Style file is stored as an XML file) by calling SaveCustomStyleFile method of the GridWeb control.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

The saved style file is in XML format so, developers may also edit this file with any text editor, if desired.

{{% /alert %}} 
### **Loading Style File**
To apply style settings from an existing style file to GridWeb control, developers can set the path of style file to CustomStyleFileName property of the control. But, before doing that it is must to set the PresetStyle property of control to Custom. It is because that style file contains custom style information that is already defined by a developer.

{{% alert color="primary" %}} 

It is also possible to load or save style file using Aspose.Cells.GridWeb Designer .

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

IMPORTANT: Loading style file into GridWeb control doesn't affect the formatting settings of the cells of the control.

{{% /alert %}} 
### **Standard Format of XML Style Template**
{{< highlight java >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
