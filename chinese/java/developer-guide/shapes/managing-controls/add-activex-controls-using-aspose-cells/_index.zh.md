---
title: 使用 Aspose.Cells 添加 ActiveX 控件
type: docs
weight: 720
url: /zh/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

您可以使用 [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) 方法在 Aspose.Cells 中添加 ActiveX 控件。该方法接受 [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType) 参数，用于指示需要在工作表中添加何种类型的 ActiveX 控件。它有以下值。

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [旋钮](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [文本框](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [切换按钮](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [未知](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

一旦将ActiveX控件添加到形状集合中，您可以通过[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl)属性访问ActiveX控件对象，然后设置其各种属性。

{{% /alert %}} 
## **使用Aspose.Cells添加切换按钮ActiveX控件**
以下示例代码使用Aspose.Cells添加切换按钮ActiveX控件。请下载使用此代码生成的[输出excel文件](5473427.xlsx)供您参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
