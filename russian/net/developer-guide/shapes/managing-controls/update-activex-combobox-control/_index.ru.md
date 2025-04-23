---
title: Обновить элемент управления ActiveX ComboBox
type: docs
weight: 170
url: /ru/net/update-activex-combobox-control/
---

## **Возможные сценарии использования**
С помощью Aspose.Cells вы можете читать или записывать значения элементов управления ActiveX ComboBox. Пожалуйста, получите доступ к элементу ActiveX Control через свойство [Shape.ActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) и проверьте его тип через свойство [ActiveXControl.Type](https://reference.aspose.com/cells/net/aspose.cells.drawing/activexcontrols/activexcontrolbase/properties/type), оно должно возвращать значение [ControlType.ComboBox](https://reference.aspose.com/cells/net/aspose.cells.drawing/activexcontrols/controltype), а затем выполнить приведение типа к объекту [ComboBoxActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/activexcontrols/comboboxactivexcontrol) и прочитать или изменить его различные свойства.

Пожалуйста, загрузите [образец файла Excel](5115124.xlsx), используемый в следующем примере кода.
## **Обновление элемента управления ComboBox ActiveX**
На следующем скриншоте показан эффект примера кода на [образец файла Excel](5115124.xlsx). Как видно, значение элемента управления ActiveX ComboBox было обновлено на "This is combo box control".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Образец кода**
Следующий образец кода обновляет значение элемента управления ActiveX ComboBox, находящегося внутри [образца файла Excel](5115124.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.cs" >}}
{{< app/cells/assistant language="csharp" >}}
