---
title: Agregar Validaciones de Celda
type: docs
weight: 70
url: /es/net/aspose-cells-gridweb/add-cell-validations/
keywords: GridWeb, GridValidation, validación de lista, validación de expresión personalizada
description: Este artículo presenta cómo agregar validación de lista, validación de lista desplegable y validación de expresión personalizada en GridWeb.
---

{{% alert color="primary" %}} 

Una de las características avanzadas de Aspose.Cells.GridWeb es agregar reglas de validación de entradas para las celdas. Los desarrolladores pueden crear diferentes tipos de reglas de validación para las celdas para controlar y validar los valores de entrada. Este tema discute los tipos de validaciones admitidos y cómo crearlos.

{{% /alert %}} 
## **Tipos de Validaciones**
Se pueden aplicar tres tipos de validaciones utilizando Aspose.Cells.GridWeb:

- Validación de lista.
- Validación de lista desplegable.
- Validación de expresión personalizada.

Cada uno se analiza en detalle a continuación.
### **Validación de lista**
La validación de lista permite a los usuarios proporcionar una entrada de celda ya sea escribiendo o seleccionando un valor de un menú. Para crear una validación de lista para una celda:

1. Agregue el control Aspose.Cells.GridWeb a un Formulario Web.
1. Acceder a una hoja de cálculo.
1. Acceda a la celda para agregar validación.
1. Cree la validación para la celda y especifique el tipo de validación como Lista.
1. Agregue valores para la validación de la lista.

El código de ejemplo agrega una validación de lista a C1. Cuando un usuario hace clic en la celda, aparece una lista.

**Salida: seleccionar un valor de la lista** 

![todo:image_alt_text](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **Validación de Lista Desplegable**
La validación de lista desplegable permite a los usuarios proporcionar entradas para las celdas seleccionando un valor de una lista predefinida. Para crear una validación de lista desplegable:

1. Agregue el control Aspose.Cells.GridWeb a un Formulario Web.
1. Acceder a una hoja de cálculo.
1. Acceda a la celda para crear la validación.
1. Cree una validación para la celda y especifique el tipo como DropDownList.
1. Agregue valores para la validación.

El código de ejemplo agrega una validación de lista desplegable a C1. Cuando un usuario hace clic en la celda, aparece un menú desplegable y los usuarios pueden seleccionar un valor de él.

**Seleccionar un valor de un menú desplegable** 

![todo:image_alt_text](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **Validación de Expresión Personalizada**
La validación de expresión personalizada permite a los desarrolladores escribir sus propias expresiones regulares personalizadas para validar valores de entrada. Para crear una validación de expresión personalizada:

1. Agregue el control Aspose.Cells.GridWeb a un Formulario Web.
1. Acceder a una hoja de cálculo.
1. Acceda a la celda para crear la validación.
1. Cree una validación para la celda y especifique el tipo como CustomExpression.
1. Establezca la expresión regular de la validación.

El código de ejemplo agrega una validación de expresión personalizada a C1. Los usuarios solo pueden agregar una fecha en la celda según el formato especificado por la expresión regular.

**Agregar un valor de fecha a C1 según una expresión regular** 

![todo:image_alt_text](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **Forzar Validación**
Usando Aspose.Cells.GridWeb, los usuarios pueden enviar datos de entrada a un servidor. Incluso si hay reglas de validación para diferentes celdas pero la propiedad ForceValidation del control GridWeb no está establecida en true, los datos de entrada incorrectos también se enviarán al servidor y no se forzará ninguna validación. La propiedad ForceValidation de GridWeb siempre está establecida en true de forma predeterminada.

Cuando la propiedad ForceValidation es verdadera, el control no enviará datos al servidor web hasta que los valores de entrada de todas las celdas sean válidos. Por ejemplo, si alguien ingresa un valor de entrada incorrecto en una celda, o no ingresa un valor, se activa la validación del lado del cliente y los usuarios no pueden enviar datos incluso si hacen clic en **Enviar**.

**Valor de entrada incorrecto resaltado por GridWeb** 

![todo:image_alt_text](add-cell-validations_4.png)
