---
title: Añadir Cell Validaciones
type: docs
weight: 70
url: /es/net/add-cell-validations/
---
{{% alert color="primary" %}} 

Una de las funciones avanzadas de Aspose.Cells.GridWeb es agregar reglas de validación de entrada para las celdas. Los desarrolladores pueden crear diferentes tipos de reglas de validación para que las celdas controlen y validen los valores de entrada. Este tema analiza los tipos de validación admitidos y cómo crearlos.

{{% /alert %}} 
## **Tipos de Validaciones**
Se pueden aplicar tres tipos de validaciones usando Aspose.Cells.GridWeb:

- Lista de validación.
- Validación de lista desplegable.
- Validación de expresiones personalizadas.

Cada uno se discute en detalle a continuación.
### **Lista de Validación**
La validación de listas permite a los usuarios proporcionar entradas de celda escribiendo o seleccionando un valor de un menú. Para crear una validación de lista para una celda:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web.
1. Accede a una hoja de trabajo.
1. Acceda a la celda para agregar validación.
1. Cree la validación para la celda y especifique el tipo de validación como Lista.
1. Agregue valores para la validación de la lista.

El código de ejemplo agrega una validación de lista a C1. Cuando un usuario hace clic en la celda, aparece una lista.

**Salida: seleccionando un valor de la lista** 

![todo:imagen_alternativa_texto](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **Validación de lista desplegable**
La validación de la lista desplegable permite a los usuarios proporcionar entradas para las celdas seleccionando un valor de una lista predefinida. Para crear una validación de lista desplegable:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web.
1. Accede a una hoja de trabajo.
1. Acceda a la celda para crear la validación.
1. Cree una validación para la celda y especifique el tipo como DropDownList.
1. Agregue valores para la validación.

El código de ejemplo agrega una validación de lista desplegable a C1. Cuando un usuario hace clic en la celda, aparece un menú desplegable y los usuarios pueden seleccionar un valor de él.

**Selección de un valor de un menú desplegable** 

![todo:imagen_alternativa_texto](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **Validación de expresiones personalizadas**
La validación de expresiones personalizadas permite a los desarrolladores escribir sus propias expresiones regulares personalizadas para validar los valores de entrada. Para crear una validación de expresión personalizada:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web.
1. Accede a una hoja de trabajo.
1. Acceda a la celda para crear una validación.
1. Cree una validación para la celda y especifique el tipo como CustomExpression.
1. Establece la expresión regular de la validación.

El código de muestra agrega una validación de expresión personalizada a C1. Los usuarios solo pueden agregar una fecha en la celda según el formato especificado por la expresión regular.

**Agregar un valor de fecha a C1 de acuerdo con una expresión regular** 

![todo:imagen_alternativa_texto](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **Forzar validación**
Utilizando Aspose.Cells.GridWeb, los usuarios pueden publicar datos de entrada en un servidor. Incluso si hay reglas de validación para diferentes celdas pero la propiedad ForceValidation del control GridWeb no está configurada como verdadera, los datos de entrada incorrectos también se enviarán al servidor y no se fuerza la validación. La propiedad ForceValidation de GridWeb siempre se establece en verdadero de forma predeterminada.

 Cuando la propiedad ForceValidation es verdadera, el control no envía datos al servidor web hasta que los valores de entrada de todas las celdas sean válidos. Por ejemplo, si alguien ingresa un valor de entrada no válido en una celda, o no ingresa un valor, la validación del lado del cliente se activa y los usuarios no pueden publicar datos incluso si hacen clic en**Enviar**.

**Valor de entrada incorrecto resaltado por GridWeb** 

![todo:imagen_alternativa_texto](add-cell-validations_4.png)
