---
title: Обновить элемент управления ActiveX ComboBox
type: docs
weight: 900
url: /ru/java/update-activex-combobox-control/
---

## **Возможные сценарии использования**
Вы можете читать или записывать значения контроллера ActiveX ComboBox, используя Aspose.Cells. Обратитесь к активному управлению через свойство [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl), проверьте его тип через [ActiveXControl.Type](https://reference.aspose.com/cells/java/com.aspose.cells/activexcontrol#Type), он должен возвращать значение [ControlType.ComboBox](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO-BOX), затем приведите его к объекту [ComboBoxActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/ComboBoxActiveXControl) и читайте или изменяйте его свойства.

Пожалуйста, загрузите [образец файла Excel](5473374.xlsx), используемый в следующем образцовом коде, и [файл вывода Excel](5473375.xlsx), сгенерированный им.
## **Обновление элемента управления ComboBox ActiveX**
Следующий скриншот показывает эффект образца кода на [образцовый файл Excel](5473374.xlsx). Как видите, значение элемента управления ActiveX ComboBox было обновлено на "This is combo box control".

![todo:image_alt_text](update-activex-combobox-control_1.png)
## **Образец кода**
Следующий образец кода обновляет значение элемента управления ActiveX ComboBox, находящегося внутри [образца файла Excel](5473374.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.java" >}}
{{< app/cells/assistant language="java" >}}
