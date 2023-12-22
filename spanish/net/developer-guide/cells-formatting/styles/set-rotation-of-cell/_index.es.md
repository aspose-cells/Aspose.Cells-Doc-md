---
title: Cómo rotar el texto de Cell
type: docs
weight: 80
url: /es/net/how-to-rotate-text-of-cell/
description: Código C# para rotar texto de Cell con Aspose.Cells for .NET API
keywords: c# rotate text of Cell, c# programmatically rotate text of Cell in workbook, programmatically set cell rotation angle in workbook, c# how to rotate text of Cell in excel
---
##  **Rotar texto de Cell en Aspose.Cells**

Aspose.Cells es un potente componente .NET y Java que permite a los desarrolladores trabajar con hojas de cálculo de Excel mediante programación. Una de las características que ofrece Aspose.Cells es la capacidad de rotar celdas, lo que le permite personalizar la orientación del texto y mejorar la presentación visual de sus datos. En este documento, exploraremos cómo rotar celdas usando Aspose.Cells.

##  **Cómo rotar el texto de Cell en Excel**
Para rotar una celda en Excel, puede utilizar los siguientes pasos:
1. Abra Excel y seleccione la celda o rango de celdas que desea rotar.
1. Haga clic derecho en las celdas seleccionadas y elija "Formato Cells" en el menú contextual. Alternativamente, puede ir a la pestaña "Inicio" en la cinta de Excel, hacer clic en el menú desplegable "Formato" en el grupo "Cells" y seleccionar "Formato Cells".
1. En el cuadro de diálogo "Formato Cells", navegue hasta la pestaña "Alineación".
1. En la sección "Orientación", verás las opciones para rotar el texto. Puede ingresar directamente el ángulo de rotación deseado en grados en el cuadro "Grados". Los valores positivos rotan el texto en el sentido contrario a las agujas del reloj y los valores negativos lo rotan en el sentido de las agujas del reloj.
<br>
![todo:image_alt_text](alignment.png)
1. Una vez que haya seleccionado la rotación deseada, haga clic en "Aceptar" para aplicar los cambios. Las celdas seleccionadas ahora se rotarán según el ángulo de rotación u orientación elegidos.

##  **Cómo rotar el texto de Cell usando Aspose.Cells API**

[**Estilo.Ángulo de rotación**](https://reference.aspose.com/cells/net/aspose.cells/style/rotationangle/) La propiedad hace que sea conveniente rotar las celdas. Para rotar celdas en Aspose.Cells, debes seguir estos pasos:
1. Cargue el libro de Excel
<br>
 Primero, debe cargar el libro de Excel usando Aspose.Cells. Puede usar la clase Libro de trabajo para abrir un archivo de Excel existente o crear uno nuevo.

1. Acceder a la hoja de trabajo
<br>
Una vez cargado el libro, debe acceder a la hoja de trabajo donde desea rotar las celdas. Puede acceder a la hoja de trabajo por su índice o nombre.

1. Rotar el texto de Cell
<br>
 Ahora que tiene acceso a la hoja de trabajo, puede rotar las celdas modificando el objeto Estilo de las celdas deseadas. El objeto Estilo le permite configurar varias opciones de formato, incluida la rotación.

1. Guarde el libro de trabajo
<br>
Después de rotar las celdas, puede guardar el libro modificado nuevamente en un archivo o secuencia utilizando el método Guardar.

##  **C# Código de muestra**

Consulte el siguiente código, crea un objeto de libro de trabajo y establece diferentes ángulos de rotación para varias celdas. La captura de pantalla muestra el resultado después de la ejecución del código de muestra.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-rotate-text.cs" >}}
