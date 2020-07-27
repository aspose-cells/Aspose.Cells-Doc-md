+++
title = "Change the HTML Link Target Type" 
description = "" 
weight = 20387 
+++

Aspose.Cells for .NET : Change the HTML Link Target Type  

# Aspose.Cells for .NET : Change the HTML Link Target Type


Aspose.Cells allows you to change the HTML link target type. HTML link looks like this

{{< code lang="cs" >}}
<a href="http://www.aspose.com/" target="_self">
{{< /code >}}

As you can see the target attribute in above html link is **\_self**. You can control this target attribute using the `HtmlSaveOptions.LinkTargetType` property. This property takes the `HtmlLinkTargetType` enum which has the following values.

*   `HtmlLinkTargetType.Blank`
*   `HtmlLinkTargetType.Parent`
*   `HtmlLinkTargetType.Self`
*   `HtmlLinkTargetType.Top`

# Change the HTML Link Target Type

The following code illustrates the usage of `HtmlSaveOptions.LinkTargetType` property. It changes the link target type to **blank**. By default, it is **parent**. You can get the [source excel file](https://docs2.aspose.com/cells/net/attachments/5017278/5112364.xlsx) from this link however you can use any excel file which contains a html hyperlink inside it to run this code.

  
  

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [source.xlsx](https://docs2.aspose.com/cells/net/attachments/5017278/5112364.xlsx) (image/png)  

