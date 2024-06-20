---
title: Actualizar el control de cuadro combinado ActiveX
type: docs
weight: 170
url: /es/net/update-activex-combobox-control/
---

## **Escenarios de uso posibles**
Puede leer o escribir los valores del Control Combo Box ActiveX utilizando Aspose.Cells. Acceda al control ActiveX a través de la propiedad [Shape.ActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) y verifique su tipo a través de la propiedad [ActiveXControl.Type](https://reference.aspose.com/cells/net/aspose.cells.drawing/activexcontrols/activexcontrolbase/properties/type), debería devolver el valor [ControlType.ComboBox](https://reference.aspose.com/cells/net/aspose.cells.drawing/activexcontrols/controltype) y luego hágale un moldeado al objeto [ComboBoxActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/activexcontrols/comboboxactivexcontrol) y lea o modifique sus diversas propiedades.

Descargue el [archivo de Excel de ejemplo](5115124.xlsx) utilizado en el siguiente código de ejemplo.
## **Actualizar control ActiveX ComboBox**
La siguiente captura de pantalla muestra el efecto del código de ejemplo en el [archivo de Excel de ejemplo](5115124.xlsx). Como puede ver, el valor del Control Combo Box ActiveX se ha actualizado a "Este es un control de combo box".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Código de muestra**
El siguiente código de ejemplo actualiza el valor del Control Combo Box ActiveX presente dentro del [archivo de Excel de ejemplo](5115124.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.cs" >}}
