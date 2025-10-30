---
title: Actualizar el control de cuadro combinado ActiveX
type: docs
weight: 170
url: /es/python-net/update-activex-combobox-control/
---

## **Escenarios de uso posibles**
Puedes leer o escribir los valores del control ActiveX ComboBox usando Aspose.Cells para Python via .NET. Accede al Control ActiveX mediante la propiedad [Shape.active_x_control](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) y verifica su tipo mediante la propiedad [ActiveXControl.type](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/activexcontrolbase/type/); debe devolver el valor [ControlType.COMBO_BOX](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) y luego convertirlo al objeto [ComboBoxActiveXControl](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol) para leer o modificar sus diversas propiedades.

Descargue el [archivo de Excel de ejemplo](5115124.xlsx) utilizado en el siguiente código de ejemplo.
## **Actualizar control ActiveX ComboBox**
La siguiente captura de pantalla muestra el efecto del código de ejemplo en el [archivo de Excel de ejemplo](5115124.xlsx). Como puede ver, el valor del Control Combo Box ActiveX se ha actualizado a "Este es un control de combo box".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Código de muestra**
El siguiente código de ejemplo actualiza el valor del Control Combo Box ActiveX presente dentro del [archivo de Excel de ejemplo](5115124.xlsx).



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-UpdateActiveXComboBoxControl.py" >}}
{{< app/cells/assistant language="python-net" >}}
