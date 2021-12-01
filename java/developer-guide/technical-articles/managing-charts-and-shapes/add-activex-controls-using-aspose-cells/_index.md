---
title: Add ActiveX Controls using Aspose.Cells
type: docs
weight: 720
url: /java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

You can add ActiveX controls with Aspose.Cells using the [ShapeCollection.addActiveXControl()](https://apireference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) method. This method takes a parameter [ControlType](https://apireference.aspose.com/cells/java/com.aspose.cells/ControlType) which tells what type of ActiveX control needs to be added inside a worksheet. It has the following values.

- [CHECK_BOX](https://apireference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [COMBO_BOX](https://apireference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [COMMAND_BUTTON](https://apireference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [IMAGE](https://apireference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://apireference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://apireference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [RADIO_BUTTON](https://apireference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [SCROLL_BAR](https://apireference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [SPIN_BUTTON](https://apireference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [TEXT_BOX](https://apireference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [TOGGLE_BUTTON](https://apireference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [UNKNOWN](https://apireference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

Once, you have added the ActiveX control inside the shape collection, you can then access the ActiveX control object via [Shape.ActiveXControl](https://apireference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) property and then set its various properties.

{{% /alert %}} 
## **Add Toggle Button ActiveX Control using Aspose.Cells**
The following sample code adds Toggle Button ActiveX Control using Aspose.Cells. Please download the [output excel file](5473427.xlsx) generated with this code for your reference.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
