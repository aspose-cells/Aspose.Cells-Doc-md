---
title: Agregar controles ActiveX usando Aspose.Cells
type: docs
weight: 720
url: /es/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

Puede agregar controles ActiveX con Aspose.Cells usando el método [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl-int-int-int-int-int-int-int-). Este método requiere un parámetro [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType) que indica qué tipo de control ActiveX necesita agregarse dentro de una hoja de trabajo. Tiene los siguientes valores.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK-BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO-BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND-BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST-BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO-BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL-BAR)
- [SPIN_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN-BUTTON)
- [TEXT_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT-BOX)
- [TOGGLE_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE-BUTTON)
- [DESCONOCIDO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

Una vez que haya agregado el control ActiveX dentro de la colección de formas, puede acceder al objeto de control ActiveX a través de la propiedad [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) y luego establecer sus diversas propiedades.

{{% /alert %}} 
## **Agregar control ActiveX de botón de alternancia con Aspose.Cells**
El siguiente código de muestra agrega un control ActiveX de botón de alternancia utilizando Aspose.Cells. Descargue el [archivo de Excel de salida](5473427.xlsx) generado con este código para su referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
{{< app/cells/assistant language="java" >}}
