---
title: Trabajando con Validaciones en Hojas de Cálculo
type: docs
weight: 70
url: /es/net/aspose-cells-griddesktop/work-with-validations-in-worksheets/
keywords: GridDesktop, validaciones, validación
description: Este artículo presenta cómo trabajar con validaciones en GridDesktop.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop también admite agregar validaciones (o reglas de validación) a las celdas de una hoja de cálculo. Aplicando reglas de validación a las celdas, los desarrolladores pueden restringir a los usuarios a introducir datos en Grid en un formato específico. Aspose.Cells.GridDesktop admite diferentes modos de validación. En este tema, no solo discutiremos sobre esos modos de validación, sino que también explicaremos la manipulación de estas validaciones.

{{% /alert %}} 
## **Modos de Validación**
Hay tres modos de validación admitidos por Aspose.Cells.GridDesktop de la siguiente manera:

- Modo de Validación Obligatorio
- Modo de Validación de Expresiones Regulares
- Modo de Validación Personalizado
### **Modo de Validación Obligatorio**
En este modo de validación, se restringe a los usuarios ingresar valores en las celdas especificadas. Una vez que se aplica **Validación Obligatoria** en una celda de la hoja de cálculo, es obligatorio que un usuario ingrese un valor en esa celda.
### **Modo de Validación de Expresiones Regulares**
En este modo, se aplican restricciones en las celdas de la hoja de cálculo para que los usuarios envíen datos a las celdas en un formato específico. El patrón del formato de datos se proporciona en forma de una **Expresión Regular**.
### **Modo de Validación Personalizado**
Para usar **Validación Personalizada**, es necesario que los desarrolladores implementen la interfaz Aspose.Cells.GridDesktop.ICustomValidation. La interfaz proporciona un método **Validar**. Este método devuelve true si los datos son válidos; de lo contrario, devuelve false.
## **Trabajando con Validaciones en Aspose.Cells.GridDesktop**
### **Agregar Validación**
Para agregar cualquier tipo de validación a una celda de hoja de cálculo, siga los siguientes pasos:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceda a cualquier **Hoja de Cálculo** deseada
- Agregue una validación deseada a la colección de **Validaciones** de la **Hoja de Cálculo** para especificar qué validación se aplicaría en qué celda.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

En la figura anterior, también hemos mencionado las reglas de validación frente a las celdas donde se aplican estas reglas. Si se introduce un valor inválido (que no es válido según la regla de validación definida para esa celda), aparecerá un **MessageBox** para notificar al usuario sobre la entrada inválida.

{{% /alert %}} 
### **Implementando ICustomValidation**
En el fragmento de código anterior, hemos agregado una validación personalizada en la celda **A8** pero aún no hemos implementado esa validación personalizada. Como hemos explicado al principio de este tema que para aplicar una validación personalizada, debemos implementar la interfaz **ICustomValidation**. Entonces, intentemos crear una clase para implementar la interfaz **ICustomValidation**.

En el fragmento de código que se muestra a continuación, hemos implementado una validación personalizada para realizar las siguientes verificaciones:

- Comprobar si la dirección de la celda es precisa en la cual se agregó la validación
- Comprobar si el tipo de datos del valor de la celda es doble
- Verificar si el valor de la celda es mayor que 100



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Accediendo a la Validación**
Una vez que se agrega una validación a una celda de hoja de cálculo específica, puede ser necesario para los desarrolladores acceder y modificar los atributos de una validación específica en tiempo de ejecución. Por lo tanto, Aspose.Cells.GridDesktop ha facilitado a los desarrolladores lograr esta tarea.

Para acceder a una validación específica, por favor siga los siguientes pasos:

- Acceda a una **Hoja de cálculo** deseada
- Acceda a una **Validación** específica en la hoja de cálculo especificando el nombre de la celda en la que se aplicó la validación
- Edite los atributos de la **Validación**, si es necesario



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

La colección **Validations** tiene dos indexadores. Un indexador (que se utiliza en el ejemplo a continuación) permite acceder a un objeto de **Validación** tomando un nombre de celda como su índice, mientras que el otro indexador toma dos parámetros (es decir, números de fila y columna) para realizar la misma tarea.

{{% /alert %}} 
### **Eliminando Validación**
Para eliminar una validación específica de la hoja de cálculo, por favor siga los siguientes pasos:

- Acceda a una **Hoja de cálculo** deseada
- Elimine una **Validación** específica de la **Hoja de cálculo** especificando el nombre de la celda en la que se aplicó la validación



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
