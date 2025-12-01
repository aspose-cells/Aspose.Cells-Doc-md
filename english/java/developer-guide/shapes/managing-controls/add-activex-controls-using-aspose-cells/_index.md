---
title: Add ActiveX Controls using Aspose.Cells
type: docs
weight: 720
url: /java/add-activex-controls-using-aspose-cells/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

You can add ActiveX controls with Aspose.Cells using the [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl-int-int-int-int-int-int-int-) method. This method takes a parameter [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType) which tells what type of ActiveX control needs to be added inside a worksheet. It has the following values.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK-BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO-BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND-BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST-BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO-BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL-BAR)
- [SPIN_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN-BUTTON)
- [TEXT_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT-BOX)
- [TOGGLE_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE-BUTTON)
- [UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

Once, you have added the ActiveX control inside the shape collection, you can then access the ActiveX control object via [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) property and then set its various properties.

{{% /alert %}} 
## **Add Toggle Button ActiveX Control using Aspose.Cells**
The following sample code adds Toggle Button ActiveX Control using Aspose.Cells. Please download the [output excel file](5473427.xlsx) generated with this code for your reference.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
{{< app/cells/assistant language="java" >}}
