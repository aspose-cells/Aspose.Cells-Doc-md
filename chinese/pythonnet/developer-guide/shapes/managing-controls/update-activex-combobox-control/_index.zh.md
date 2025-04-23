---
title: 更新ActiveX组合框控件
type: docs
weight: 170
url: /zh/python-net/update-activex-combobox-control/
---

## **可能的使用场景**
你可以使用 Aspose.Cells for Python via .NET 读取或写入 ActiveX 组合框控件的值。请通过 [Shape.active_x_control](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) 属性访问 ActiveX 控件，并通过 [ActiveXControl.type](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/activexcontrolbase/type/) 属性检查它的类型，应返回 [ControlType.COMBO_BOX](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) 值，并将其强制类型转换为 [ComboBoxActiveXControl](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol) 对象，然后读取或修改其各种属性。

请下载以下示例代码中使用的 [示例 Excel 文件](5115124.xlsx)。
## **更新ActiveX ComboBox控件**
以下截图显示了样本代码对 [样本excel文件](5115124.xlsx) 的效果。正如你所看到的，活动X组合框的值已更新为"This is combo box control"。

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **示例代码**
以下样本代码更新了 [样本excel文件](5115124.xlsx) 中存在的活动X组合框控件的值。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-UpdateActiveXComboBoxControl.py" >}}
