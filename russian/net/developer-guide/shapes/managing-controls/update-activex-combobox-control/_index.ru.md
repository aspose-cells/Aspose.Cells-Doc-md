---
title: Обновите элемент управления ActiveX ComboBox
type: docs
weight: 170
url: /ru/net/update-activex-combobox-control/
---
## **Возможные сценарии использования**
 Вы можете прочитать или записать значения элемента управления ActiveX ComboBox, используя Aspose.Cells. Получите доступ к элементу управления ActiveX через[Shape.ActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) свойство и проверьте его тип через[ActiveXControl.Type](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/activexcontrolbase/properties/type) свойство, оно должно возвращаться[ControlType.ComboBox](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) значение, а затем введите его в[ComboBoxActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol)объект и читать или изменять его различные свойства.

 Пожалуйста, загрузите[образец эксель файла](5115124.xlsx) используется в следующем примере кода.
## **Обновите элемент управления ActiveX ComboBox**
 На следующем снимке экрана показано влияние примера кода на[образец эксель файла](5115124.xlsx)Как видите, значение ActiveX ComboBox было обновлено до «Это элемент управления полем со списком».

|![дело:изображение_альтернативный_текст](update-activex-combobox-control_1.png)|
|:- |
## **Образец кода**
 Следующий пример кода обновляет значение элемента управления ActiveX ComboBox, присутствующего внутри[образец эксель файла](5115124.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.cs" >}}
