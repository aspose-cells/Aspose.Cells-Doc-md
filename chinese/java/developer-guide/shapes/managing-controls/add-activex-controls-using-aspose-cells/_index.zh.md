---
title: 使用Aspose.Cells添加ActiveX控件
type: docs
weight: 720
url: /zh/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

您可以使用[ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\))方法在Aspose.Cells中添加ActiveX控件。该方法接受一个参数[ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType)，告诉需要在工作表内添加什么类型的ActiveX控件。它有以下值。

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [SPIN_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [TEXT_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [TOGGLE_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

添加了ActiveX控件到形状集合后，您可以通过[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl)属性访问ActiveX控件对象，然后设置其各种属性。

{{% /alert %}} 
## **使用Aspose.Cells添加切换按钮ActiveX控件**
以下示例代码使用Aspose.Cells添加切换按钮ActiveX控件。请下载使用此代码生成的[输出Excel文件](5473427.xlsx)供参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
