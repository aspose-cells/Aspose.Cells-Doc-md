---
title: Change the HTML Link Target Type
type: docs
weight: 450
url: /java/change-the-html-link-target-type/
---

{{% alert color="primary" %}} 

Aspose.Cells allows you to change the HTML link target type. HTML link looks like this

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

As you can see the target attribute in the above HTML link is **_self**. You can control this target attribute using the [HtmlSaveOptions.setLinkTargetType()](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlsaveoptions#LinkTargetType) property. This property takes the [HtmlLinkTargetType](https://apireference.aspose.com/java/cells/com.aspose.cells/HtmlLinkTargetType) enum which has the following values.

- [BLANK](https://apireference.aspose.com/java/cells/com.aspose.cells/htmllinktargettype#BLANK)
- [PARENT](https://apireference.aspose.com/java/cells/com.aspose.cells/htmllinktargettype#PARENT)
- [SELF](https://apireference.aspose.com/java/cells/com.aspose.cells/htmllinktargettype#SELF)
- [TOP](https://apireference.aspose.com/java/cells/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **Change the HTML Link Target Type**
The following code illustrates the usage of [HtmlSaveOptions.setLinkTargetType()](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlsaveoptions#LinkTargetType) property. It changes the link target type to **blank**. By default, it is the **parent**. You can get the [source excel file](5472932.xlsx) from this link however you can use any excel file which contains an HTML hyperlink inside it to run this code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
