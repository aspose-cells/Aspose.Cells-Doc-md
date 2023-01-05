---
title: Agregue controles ActiveX usando Aspose.Cells
type: docs
weight: 720
url: /es/java/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}} 

 Puede agregar controles ActiveX con Aspose.Cells usando el[ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\) ) método. Este método toma un parámetro[Tipo de control](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType)que indica qué tipo de control ActiveX debe agregarse dentro de una hoja de trabajo. Tiene los siguientes valores.

- [CAJA](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [CAJA COMBO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [BOTÓN DE COMANDO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [IMAGEN](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [ETIQUETA](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [CUADRO DE LISTA](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [BOTON DE RADIO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [BARRA DE DESPLAZAMIENTO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [GIRAR_BOTÓN](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [CAJA DE TEXTO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [BOTÓN DE ACTIVACIÓN](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [DESCONOCIDO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

 Una vez que haya agregado el control ActiveX dentro de la colección de formas, puede acceder al objeto de control ActiveX a través de[Forma.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) propiedad y luego establecer sus diversas propiedades.

{{% /alert %}} 
## **Agregue el control ActiveX del botón de alternar usando Aspose.Cells**
 El siguiente código de ejemplo agrega el control ActiveX del botón de alternar usando Aspose.Cells. Descargue el[archivo de salida de Excel](5473427.xlsx) generado con este código para su referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
