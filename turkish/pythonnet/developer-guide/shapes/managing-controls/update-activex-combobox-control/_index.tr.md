---
title: ActiveX ComboBox Kontrolünü Güncelle
type: docs
weight: 170
url: /tr/python-net/update-activex-combobox-control/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells for Python via .NET kullanarak ActiveX ComboBox Kontrolünün değerlerini okuyabilir veya yazabilirsiniz. Lütfen ActiveX Kontrolüne [Shape.active_x_control](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) özelliği üzerinden erişin ve türünü [ActiveXControl.type](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/activexcontrolbase/type/) özelliğiyle kontrol edin, bu [ControlType.COMBO_BOX](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) değerini döndürmelidir ve ardından [ComboBoxActiveXControl](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol) nesnesine tip dönüştürün ve çeşitli özelliklerini okuyun veya değiştirin.

Lütfen aşağıdaki örnek kodda kullanılan [örnek excel dosyasını](5115124.xlsx) indirin.
## **ActiveX ComboBox Kontrolünü Güncelleme**
Aşağıdaki ekran görüntüsü, [örnek excel dosyası](5115124.xlsx) üzerinde örnek kodun etkisini göstermektedir. Görebileceğiniz gibi, AktifX ComboBox değeri "Bu bir combo box kontrolüdür" olarak güncellenmiştir.

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Örnek Kod**
[örnek excel dosyası](5115124.xlsx) içinde bulunan AktifX ComboBox Kontrolünün değerini güncelleyen aşağıdaki örnek kodu takip edin.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-UpdateActiveXComboBoxControl.py" >}}
{{< app/cells/assistant language="python-net" >}}
