---
title: Formatear celda
type: docs
weight: 40
url: /es/net/aspose-cells-gridweb/format-grid-cell/
keywords: GridWeb, formato, estilo
description: Este artículo introduce cómo establecer o aplicar formato de estilo para una celda (GridCell) en GridWeb.
---

{{% alert color="primary" %}} 

Este tema proporciona una discusión detallada sobre cómo dar formato a las celdas.

Cubre el formato de celdas en el modo de IU mediante el control Aspose.Cells.GridWeb Style dialog. También muestra cómo dar formato a las celdas programáticamente. Se discuten diferentes configuraciones de formato como fuente, borde y formato de número, ilustrado con ejemplos.

{{% /alert %}} 
## **Dar formato a las celdas mediante el cuadro de diálogo de estilo**
Las celdas pueden ser formateadas [programáticamente](/cells/es/net/aspose-cells-gridweb/format-cells/) pero la forma más fácil de dar formato a las celdas en el control Aspose.Cells.GridWeb de forma WYSIWYG, es utilizando el cuadro de diálogo de estilo.

Para usar el cuadro de diálogo de estilo:
Selecciona un rango de celdas, luego haz clic derecho y selecciona **Formato de celda**. 

**Seleccionar formato de celda** 

![todo:image_alt_text](format-cells_1.png)



Se muestra el cuadro de diálogo de estilo. 

**Se utiliza el cuadro de diálogo de estilo para dar formato a las celdas** 

![todo:image_alt_text](format-cells_2.png)

El cuadro de diálogo de estilo permite a los usuarios dar formato a las celdas personalizando la configuración de fuente y borde.
### **Personalizar la configuración de la fuente**
Puedes personalizar las siguientes configuraciones de fuente utilizando el cuadro de diálogo de estilo:

- Nombre de fuente, selecciona una fuente deseada de la lista.
- Estilo de fuente, aplica un estilo de fuente como negrita, cursiva, etc.
- Tamaño de fuente, selecciona un tamaño de fuente en puntos.
- Subrayado, subraya el texto.
- Tachado, aplica un efecto de tachado al texto.
- Alineación horizontal, seleccione alineación horizontal.
- Alineación vertical, seleccione alineación vertical.
- Color de fuente, seleccione un color de fuente.
- Fondo, seleccione un color para el fondo.

Puede verificar la configuración de fuente seleccionada en un área de vista previa pequeña.

**Configuración de fuente personalizada** 

![todo:image_alt_text](format-cells_3.png)
### **Personalizar la configuración de bordes**
El control también permite a los usuarios dibujar un borde alrededor de las celdas personalizando la configuración de bordes en el cuadro de diálogo de estilo.

Para ver las opciones relacionadas con el borde:
Haga clic en **Bordes** en el cuadro de diálogo de estilo.
Las opciones relacionadas con el borde se muestran. 

**Opciones de borde en el cuadro de diálogo de estilo** 

![todo:image_alt_text](format-cells_4.png)

Las siguientes opciones de borde se pueden seleccionar en el cuadro de diálogo de estilo:

- Estilo de línea de borde, seleccione el estilo de borde como sólido, segmentado, etc.
- Ancho de línea de borde, seleccione el ancho de borde en píxeles.
- Color de línea de borde, seleccione el color de la línea.
- Líneas de borde, seleccione la numeración y la posición de las líneas de borde.

**Configuración de borde personalizada** 

![todo:image_alt_text](format-cells_5.png)
### **Aplicar ajustes**
Haga clic en **Aceptar** en el cuadro de diálogo de estilo para aplicar los cambios.

**Ajustes de fuente y borde aplicados** 

![todo:image_alt_text](format-cells_6.png)


## **Formato de celdas usando API**
Las celdas también se pueden formatear programáticamente con la API Aspose.Cells.GridWeb. Cada celda tiene una propiedad de estilo, que representa un objeto GridTableItemStyle. Utilice la propiedad de estilo para personalizar la configuración de fuente y borde.
### **Configuración de fuente**
Para personalizar la configuración de fuente programáticamente:

1. Agregue el control Aspose.Cells.GridWeb a un Formulario Web.
1. Acceder a una hoja de cálculo.
1. Acceda a la celda que está formateando.
1. Acceda al estilo de la celda.
1. Establezca el tamaño de fuente en puntos.
1. Establezca el estilo de fuente.
1. Establezca los colores de primer plano y fondo.
1. Establecer alineación horizontal y vertical.
1. Restablecer el estilo de la celda.

**Salida: configuración personalizada de la fuente mostrada en A1** 

![todo:image_alt_text](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **Establecer bordes**
Los bordes se pueden aplicar a celdas individuales o a un rango.
#### **Celda individual**
Para establecer los bordes de una celda individual:

1. Agregue el control Aspose.Cells.GridWeb a un Formulario Web.
1. Acceder a una hoja de cálculo.
1. Acceda a la celda que va a formatear.
1. Acceda al objeto de estilo de la celda.
1. Establezca el estilo del borde.
1. Establezca el ancho del borde en píxeles.
1. Establezca el color del borde.
1. Establezca el estilo de la celda.

**Configuración de bordes personalizados en una celda individual** 

![todo:image_alt_text](format-cells_8.png)

{{% alert color="primary" %}} 

Es posible establecer diferentes estilos para cada línea de borde con las propiedades Style.TopBorderStyle, Style.BottomBorderStyle, Style.LeftBorderStyle, Style.RightBorderStyle de la celda.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **Rango de celdas**
Para establecer bordes en un rango de celdas:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web
1. Acceda a una hoja de cálculo deseada
1. Instantíe un objeto de la clase WebBorderStyle
1. Establecer el estilo del borde como Sólido o Discontinuo, etc.
1. Establecer Anchura del Borde en píxeles
1. Establecer el color del borde
1. Aplicar la configuración del borde almacenada en el objeto WebBorderStyle a un rango especificado de celdas

**Un rango de celdas con configuración de bordes personalizados** 

![todo:image_alt_text](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **Establecer formatos de números**
Aspose.Cells.GridWeb admite el establecimiento de formatos de número. Hay 59 formatos de número integrados. Para verlos, consulte esta [lista de formatos de número admitidos](/cells/es/net/aspose-cells-gridweb/list-of-supported-number-formats/).

Todos los formatos de número integrados están en la enumeración NumberType. Para usar un formato de número integrado, establezca el NumberType usando el método SetNumberType de un objeto celda a un formato de número de la enumeración NumberType.

Para establecer un formato de número personalizado, use el método SetCustom de la celda.

**Configuración de formato de número aplicada en B1 y B2** 

![todo:image_alt_text](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
