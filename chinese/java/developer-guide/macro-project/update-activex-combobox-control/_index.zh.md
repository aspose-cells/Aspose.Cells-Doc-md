---
title: 更新 ActiveX ComboBox 控件
type: docs
weight: 900
url: /zh/java/update-activex-combobox-control/
---

## **可能的使用场景**
您可以使用Aspose.Cells读取或写入ActiveX ComboBox控件的值。请通过[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) 属性访问ActiveX控件，并通过[ActiveXControl.Type](https://reference.aspose.com/cells/java/com.aspose.cells/activexcontrol#Type) 属性检查其类型，应返回[ControlType.ComboBox](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX) 值，然后将其强制转换为[ComboBoxActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/ComboBoxActiveXControl) 对象并读取或修改其各种属性。

请下载以下示例代码中使用的[示例Excel文件](5473374.xlsx)和由其生成的[输出Excel文件](5473375.xlsx)。
## **更新 ActiveX ComboBox 控件**
以下屏幕截图显示了示例代码对[样本Excel文件](5473374.xlsx)的影响。如您所见，ActiveX ComboBox的值已更新为"This is combo box control"。

![todo:image_alt_text](update-activex-combobox-control_1.png)
## **示例代码**
以下示例代码更新了[样本Excel文件](5473374.xlsx)中ActiveX ComboBox控件的值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.java" >}}
