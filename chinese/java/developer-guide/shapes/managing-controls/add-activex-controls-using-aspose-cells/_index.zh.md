---
title: 使用 Aspose.Cells 添加 ActiveX 控件
type: docs
weight: 720
url: /zh/java/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}} 

您可以使用 Aspose.Cells 添加 ActiveX 控件[ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\) ） 方法。这个方法接受一个参数[控件类型](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType)它告诉需要在工作表中添加什么类型的 ActiveX 控件。它具有以下值。

- [复选框](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [组合框](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [命令按钮](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [图片](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [标签](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [列表框](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [单选按钮](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [滚动条](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [旋转按钮](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [文本框](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [切换按钮](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [未知](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

一旦您在形状集合中添加了 ActiveX 控件，您就可以通过以下方式访问 ActiveX 控件对象[形状.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl)属性，然后设置其各种属性。

{{% /alert %}} 
## **使用 Aspose.Cells 添加切换按钮 ActiveX 控件**
以下示例代码使用 Aspose.Cells 添加 Toggle Button ActiveX 控件。请下载[输出excel文件](5473427.xlsx)使用此代码生成供您参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
