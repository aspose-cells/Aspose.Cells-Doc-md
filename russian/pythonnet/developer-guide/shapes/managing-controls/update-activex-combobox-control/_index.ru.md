---
title: Обновить элемент управления ActiveX ComboBox
type: docs
weight: 170
url: /ru/python-net/update-activex-combobox-control/
---

## **Возможные сценарии использования**
Вы можете читать или записывать значения элемента управления ActiveX ComboBox с помощью Aspose.Cells для Python via .NET. Доступ к элементу управления осуществляется через свойство [Shape.active_x_control](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control), а его тип проверяется через свойство [ActiveXControl.type](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/activexcontrolbase/type/). Оно должно возвращать значение [ControlType.COMBO_BOX](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype), затем его приводят к типу [ComboBoxActiveXControl](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol) и читают или изменяют его свойства.

Пожалуйста, загрузите [образец файла Excel](5115124.xlsx), используемый в следующем примере кода.
## **Обновление элемента управления ComboBox ActiveX**
На следующем скриншоте показан эффект примера кода на [образец файла Excel](5115124.xlsx). Как видно, значение элемента управления ActiveX ComboBox было обновлено на "This is combo box control".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Образец кода**
Следующий образец кода обновляет значение элемента управления ActiveX ComboBox, находящегося внутри [образца файла Excel](5115124.xlsx).



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-UpdateActiveXComboBoxControl.py" >}}
