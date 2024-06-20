---
title: Actualizar el control de cuadro combinado ActiveX
type: docs
weight: 900
url: /es/java/update-activex-combobox-control/
---

## **Escenarios de uso posibles**
Puedes leer o escribir los valores del control de cuadro combinado ActiveX utilizando Aspose.Cells. Accede al Control ActiveX a través de la propiedad [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) y verifica su tipo a través de la propiedad [ActiveXControl.Type](https://reference.aspose.com/cells/java/com.aspose.cells/activexcontrol#Type), debería devolver el valor [ControlType.ComboBox](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX) y luego realiza un typecast en el objeto [ComboBoxActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/ComboBoxActiveXControl) y lee o modifica sus diversas propiedades.

Por favor, descarga el [archivo de Excel de ejemplo](5473374.xlsx) utilizado en el siguiente código de muestra y el [archivo de Excel de salida](5473375.xlsx) generado por él.
## **Actualizar control ActiveX ComboBox**
La siguiente captura de pantalla muestra el efecto del código de muestra en el [archivo de Excel de ejemplo](5473374.xlsx). Como puedes ver, el valor del cuadro combinado ActiveX se ha actualizado a "Este es un control de cuadro combinado".

![todo:image_alt_text](update-activex-combobox-control_1.png)
## **Código de muestra**
El siguiente código de muestra actualiza el valor del Control ComboBox de ActiveX presente dentro del [archivo de Excel de muestra](5473374.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.java" >}}
