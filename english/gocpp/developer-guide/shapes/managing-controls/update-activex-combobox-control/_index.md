---
title: Update ActiveX ComboBox Control with Golang via C++
linktitle: Update ActiveX ComboBox Control
type: docs
weight: 170
url: /go-cpp/update-activex-combobox-control/
description: Learn how to read or write values of ActiveX ComboBox Control using Aspose.Cells with Golang via C++.
---

## **Possible Usage Scenarios**
You can read or write the values of ActiveX ComboBox Control using Aspose.Cells. Please access the ActiveX Control via [Shape.ActiveXControl](https://reference.aspose.com/cells/go-cpp/activexcontrol/) property and check its type via [ActiveXControl.GetType()](https://reference.aspose.com/cells/go-cpp/activexcontrolbase/gettype/) property. It should return [ControlType.ComboBox](https://reference.aspose.com/cells/go-cpp/controltype/) value, and then typecast it into [ComboBoxActiveXControl](https://reference.aspose.com/cells/go-cpp/comboboxactivexcontrol/) object to read or modify its various properties.

Please download the [sample excel file](5115124.xlsx) used in the following sample code.

## **Update ActiveX ComboBox Control**
The following screenshot shows the effect of the sample code on the [sample excel file](5115124.xlsx). As you can see, the ActiveX ComboBox value has been updated to "This is combo box control".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |

## **Sample Code**
The following sample code updates the value of ActiveX ComboBox Control present inside the [sample excel file](5115124.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdateActivexComboboxControl.go" >}}
{{< app/cells/assistant language="go" >}}
