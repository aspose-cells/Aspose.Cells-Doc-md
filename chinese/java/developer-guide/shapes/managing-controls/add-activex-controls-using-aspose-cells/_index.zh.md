---
title: 使用 Aspose.Cells 添加 ActiveX 控件
type: docs
weight: 720
url: /zh/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

 可以使用 [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl-int-int-int-int-int-int-int-) 方法向工作表添加 ActiveX 控件。该方法的参数 [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType) 指示需要添加的 ActiveX 控件类型。其取值如下：

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK-BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO-BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND-BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST-BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO-BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL-BAR)
- [旋钮](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN-BUTTON)
- [文本框](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT-BOX)
- [切换按钮](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE-BUTTON)
- [未知](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

一旦将ActiveX控件添加到形状集合中，您可以通过[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl)属性访问ActiveX控件对象，然后设置其各种属性。

{{% /alert %}} 
## **使用Aspose.Cells添加切换按钮ActiveX控件**
以下示例代码使用Aspose.Cells添加切换按钮ActiveX控件。请下载使用此代码生成的[输出excel文件](5473427.xlsx)供您参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
{{< app/cells/assistant language="java" >}}
