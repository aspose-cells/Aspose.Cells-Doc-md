---
title: Обновите элемент управления ActiveX ComboBox
type: docs
weight: 900
url: /ru/java/update-activex-combobox-control/
---
## **Возможные сценарии использования**
 Вы можете прочитать или записать значения элемента управления ActiveX ComboBox, используя Aspose.Cells. Получите доступ к элементу управления ActiveX через[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) свойство и проверьте его тип через[ActiveXControl.Type](https://reference.aspose.com/cells/java/com.aspose.cells/activexcontrol#Type) свойство, оно должно возвращаться[ControlType.ComboBox](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX) значение, а затем введите его в[ComboBoxActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/ComboBoxActiveXControl)объект и читать или изменять его различные свойства.

 Пожалуйста, загрузите[образец эксель файла](5473374.xlsx) используется в следующем примере кода и[выходной файл excel](5473375.xlsx) порожденный им.
## **Обновите элемент управления ActiveX ComboBox**
 На следующем снимке экрана показано влияние примера кода на[образец эксель файла](5473374.xlsx)Как видите, значение ActiveX ComboBox было обновлено до «Это элемент управления полем со списком».

![дело:изображение_альтернативный_текст](update-activex-combobox-control_1.png)
## **Образец кода**
 Следующий пример кода обновляет значение элемента управления ActiveX ComboBox, присутствующего внутри[образец эксель файла](5473374.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.java" >}}
