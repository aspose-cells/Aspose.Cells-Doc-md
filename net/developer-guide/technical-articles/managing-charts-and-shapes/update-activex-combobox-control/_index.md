---
title: Update ActiveX ComboBox Control
type: docs
weight: 170
url: /net/update-activex-combobox-control/
---

## **Possible Usage Scenarios**
You can read or write the values of ActiveX ComboBox Control using Aspose.Cells. Please access the ActiveX Control via [Shape.ActiveXControl](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) property and check its type via [ActiveXControl.Type](https://apireference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/activexcontrolbase/properties/type) property, it should return [ControlType.ComboBox](https://apireference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) value and then typecast it into [ComboBoxActiveXControl](https://apireference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol) object and read or modify its various properties.

Please download the [sample excel file](5115124.xlsx) used in the following sample code.
## **Update ActiveX ComboBox Control**
The following screenshot shows the effect of the sample code on the [sample excel file](5115124.xlsx). As you can see, the ActiveX ComboBox value has been updated to "This is combo box control".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Sample Code**
The following sample code updates the value of ActiveX ComboBox Control present inside the [sample excel file](5115124.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.cs" >}}
