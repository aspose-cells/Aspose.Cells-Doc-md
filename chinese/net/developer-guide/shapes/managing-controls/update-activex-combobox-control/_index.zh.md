---
title: 更新ActiveX组合框控件
type: docs
weight: 170
url: /zh/net/update-activex-combobox-control/
---

## **可能的使用场景**
您可以使用 Aspose.Cells 读取或写入 ActiveX ComboBox 控件的值。请通过 [Shape.ActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) 属性访问 ActiveX 控件，并通过 [ActiveXControl.Type](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/activexcontrolbase/properties/type) 属性检查其类型，它应该返回 [ControlType.ComboBox](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) 值，然后将其转换为 [ComboBoxActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol) 对象并读取或修改其各种属性。

请下载以下示例代码中使用的 [示例 Excel 文件](5115124.xlsx)。
## **更新ActiveX ComboBox控件**
以下截图显示了样本代码对 [样本excel文件](5115124.xlsx) 的效果。正如你所看到的，活动X组合框的值已更新为"This is combo box control"。

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **示例代码**
以下样本代码更新了 [样本excel文件](5115124.xlsx) 中存在的活动X组合框控件的值。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.cs" >}}
