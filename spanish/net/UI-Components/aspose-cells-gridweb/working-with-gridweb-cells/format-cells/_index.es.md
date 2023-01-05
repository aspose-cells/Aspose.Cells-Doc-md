---
title: Formato Cells
type: docs
weight: 40
url: /es/net/format-grid-cells/
---
{{% alert color="primary" %}} 

Este tema proporciona una discusión detallada sobre cómo dar formato a las celdas.

Cubre el formato de celdas en modo GUI utilizando el cuadro de diálogo Estilo del control Aspose.Cells.GridWeb. También muestra cómo formatear celdas mediante programación. Se analizan diferentes configuraciones de formato como fuente, borde y formato de número, ilustradas con ejemplos.

{{% /alert %}} 
## **Formateo Cells Uso del cuadro de diálogo Estilo**
 Cells se puede formatear[programáticamente](/cells/es/net/format-cells/)pero la forma más sencilla de formatear celdas en el control Aspose.Cells.GridWeb de forma WYSIWYG es mediante el cuadro de diálogo Estilo.

Para utilizar el cuadro de diálogo Estilo:
 Seleccione un rango de celdas, luego haga clic derecho y seleccione**Formato Cell**. 

**Selección del formato Cell** 

![todo:imagen_alternativa_texto](format-cells_1.png)



 Se muestra el cuadro de diálogo Estilo.

**El cuadro de diálogo Estilo se utiliza para dar formato a las celdas.** 

![todo:imagen_alternativa_texto](format-cells_2.png)

El cuadro de diálogo Estilo permite a los usuarios dar formato a las celdas personalizando la fuente y la configuración del borde.
### **Personalización de la configuración de fuentes**
Puede personalizar la siguiente configuración de fuente mediante el cuadro de diálogo Estilo:

- Nombre de fuente, seleccione una fuente deseada de la lista.
- Estilo de fuente, aplique un estilo de fuente como negrita, cursiva, etc.
- Tamaño de fuente, seleccione un tamaño de fuente en puntos.
- Subrayar, subrayar texto.
- Tachado, aplique un efecto de tachado al texto.
- Alineación horizontal, seleccione alineación horizontal.
- Alineación vertical, seleccione alineación vertical.
- Color de fuente, seleccione un color de fuente.
- Fondo, seleccione un color para el fondo.

Puede comprobar la configuración de la fuente seleccionada en una pequeña área de vista previa.

**Configuraciones de fuentes personalizadas** 

![todo:imagen_alternativa_texto](format-cells_3.png)
### **Personalización de la configuración del borde**
El control también permite a los usuarios dibujar un borde alrededor de las celdas al personalizar la configuración del borde en el cuadro de diálogo Estilo.

Para ver las opciones relacionadas con los bordes:
 Hacer clic**Fronteras** en el cuadro de diálogo Estilo.
 Se muestran las opciones relacionadas con los bordes.

**Opciones de borde en el cuadro de diálogo de estilo** 

![todo:imagen_alternativa_texto](format-cells_4.png)

Las siguientes opciones de borde se pueden seleccionar desde el cuadro de diálogo Estilo:

- Estilo de línea de borde, seleccione el estilo de borde como sólido, discontinuo, etc.
- Ancho de la línea del borde, seleccione el ancho del borde en píxeles.
- Color de línea de borde, seleccione el color de línea.
- Líneas de borde, seleccione la numeración y el posicionamiento de las líneas de borde.

**Configuraciones de borde personalizadas** 

![todo:imagen_alternativa_texto](format-cells_5.png)
### **Aplicar ajustes**
 Hacer clic**DE ACUERDO** en el cuadro de diálogo Estilo para aplicar los cambios.

**Configuraciones de fuentes y bordes aplicadas** 

![todo:imagen_alternativa_texto](format-cells_6.png)


## **Formateo Cells Usando API**
Cells también se puede formatear mediante programación con Aspose.Cells.GridWeb API. Cada celda tiene una propiedad Style, que representa un objeto GridTableItemStyle. Utilice la propiedad Estilo para personalizar la configuración de fuentes y bordes.
### **Configuración de fuente**
Para personalizar la configuración de fuente mediante programación:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web.
1. Accede a una hoja de trabajo.
1. Accede a la celda que estás formateando.
1. Accede al estilo de la celda.
1. Establezca el tamaño de fuente en puntos.
1. Establezca el estilo de fuente.
1. Establecer colores de primer plano y de fondo.
1. Establezca la alineación horizontal y vertical.
1. Establezca el estilo de nuevo en la celda.

**Salida: configuración de fuente personalizada que se muestra en A1** 

![todo:imagen_alternativa_texto](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **Establecer fronteras**
Los bordes se pueden aplicar a celdas individuales o a un rango.
#### **Soltero Cell**
Para establecer los bordes de una sola celda:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web.
1. Accede a una hoja de trabajo.
1. Accede a la celda que estás a punto de formatear.
1. Acceda al objeto Style de la celda.
1. Establece el estilo del borde.
1. Establezca el ancho del borde en píxeles.
1. Establezca el color del borde.
1. Establece el estilo de la celda.

**Configuraciones de borde personalizadas en una sola celda** 

![todo:imagen_alternativa_texto](format-cells_8.png)

{{% alert color="primary" %}} 

Es posible establecer diferentes estilos para cada línea de borde con las propiedades Style.TopBorderStyle, Style.BottomBorderStyle, Style.LeftBorderStyle, Style.RightBorderStyle de la celda.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **Rango de Cells**
Para establecer bordes en un rango de celdas:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web
1. Acceder a una hoja de trabajo deseada
1. Crear una instancia de un objeto de la clase WebBorderStyle
1. Establezca el Estilo del borde en Sólido o Discontinuo, etc.
1. Establecer el ancho del borde en píxeles
1. Establecer el color del borde
1. Aplique la configuración de borde almacenada en el objeto WebBorderStyle a un rango específico de celdas

**Un rango de celdas con configuraciones de borde personalizadas** 

![todo:imagen_alternativa_texto](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **Configuración de formatos de número**
 Aspose.Cells. GridWeb admite la configuración de formatos de números. Hay 59 formatos de números integrados. Para verlos, por favor refiérase a este[lista de formatos de número admitidos](/cells/es/net/list-of-supported-number-formats/).

Todos los formatos de números incorporados están en la enumeración NumberType. Para usar un formato de número integrado, establezca NumberType mediante el método SetNumberType del objeto de una celda en un formato de número de la enumeración NumberType.

Para establecer un formato de número personalizado, use el método SetCustom de la celda.

**Configuraciones de formato de número aplicadas en B1 y B2** 

![todo:imagen_alternativa_texto](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
