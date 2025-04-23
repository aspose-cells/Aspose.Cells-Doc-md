---
title: 更新ActiveX组合框控件
type: docs
weight: 900
url: /zh/java/update-activex-combobox-control/
---

## **可能的使用场景**
你可以使用 Aspose.Cells 读取或写入 ActiveX 组合框控件的值。请通过 [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) 属性访问 ActiveX 控件，并通过 [ActiveXControl.Type](https://reference.aspose.com/cells/java/com.aspose.cells/activexcontrol#Type) 属性检查其类型，应返回 [ControlType.ComboBox](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO-BOX) 值，然后将其强制类型转换为 [ComboBoxActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/ComboBoxActiveXControl) 对象，读取或修改其各种属性。

请下载以下示例代码中使用的[示例Excel文件](5473374.xlsx)和由其生成的[输出Excel文件](5473375.xlsx)。
## **更新ActiveX ComboBox控件**
下面的屏幕截图显示了示例代码对[示例Excel文件](5473374.xlsx)的影响。您可以看到，ActiveX组合框的值已更新为"这是组合框控件"。

![todo:image_alt_text](update-activex-combobox-control_1.png)
## **示例代码**
以下示例代码更新了[示例Excel文件](5473374.xlsx)中的ActiveX组合框控件的值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.java" >}}
{{< app/cells/assistant language="java" >}}
