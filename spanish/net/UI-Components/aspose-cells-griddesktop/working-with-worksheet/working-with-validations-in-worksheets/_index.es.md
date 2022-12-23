---
title: Trabajar con validaciones en hojas de trabajo
type: docs
weight: 70
url: /es/net/working-with-validations-in-worksheets/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop también admite agregar validaciones (o reglas de validación) a las celdas de una hoja de cálculo. Al aplicar reglas de validación a las celdas, los desarrolladores pueden restringir a los usuarios para que ingresen datos en Grid en un formato específico. Aspose.Cells.GridDesktop admite diferentes modos de validación. En este tema, no solo discutiremos sobre esos modos de validación, sino que también explicaremos la manipulación de estas validaciones.

{{% /alert %}} 
## **Modos de validación**
Hay tres modos de validación admitidos por Aspose.Cells.GridDesktop de la siguiente manera:

- Se requiere modo de validación
- Modo de validación de expresiones regulares
- Modo de validación personalizado
### **Se requiere modo de validación**
 En este modo de validación, los usuarios están restringidos a ingresar valores en celdas específicas. Una vez**Se Requiere Validación** se aplica en una celda de la hoja de trabajo, se vuelve obligatorio para un usuario ingresar un valor en esa celda.
### **Modo de validación de expresiones regulares**
 En este modo, se aplican restricciones en las celdas de la hoja de trabajo para que los usuarios envíen datos a las celdas en un formato específico. El patrón de formato de datos se proporciona en forma de**Expresión regular**.
### **Modo de validación personalizado**
 Usar**Validación personalizada** Es imprescindible que los desarrolladores implementen la interfaz Aspose.Cells.GridDesktop.ICustomValidation. La interfaz proporciona una**Validar** método. Este método devuelve verdadero si los datos son válidos; de lo contrario, devuelve falso.
## **Trabajar con validaciones en Aspose.Cells.GridDesktop**
### **Agregar validación**
Para agregar cualquier tipo de validación a una celda de la hoja de trabajo, siga los pasos a continuación:

-  Agregue el control Aspose.Cells.GridDesktop a su**Formulario**
-  Accede a cualquier deseado**Hoja de cálculo**
-  Agregue una validación deseada a la**Validaciones** colección de la**Hoja de cálculo** para especificar qué validación se aplicaría en qué celda.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

 En la figura anterior, también mencionamos las reglas de validación delante de las celdas donde se aplican estas reglas de validación. Si se ingresa algún valor no válido (que no es válido de acuerdo con la regla de validación definida para esa celda), se**Buzon de mensaje** aparecería para notificar al usuario sobre la entrada no válida.

{{% /alert %}} 
### **Implementando ICustomValidation**
 En el fragmento de código anterior, hemos agregado una validación personalizada en**A8**cell pero aún no hemos implementado esa validación personalizada. Como hemos explicado al principio de este tema, para aplicar la validación personalizada, tenemos que implementar**IValidaciónPersonalizada** interfaz. Entonces, intentemos crear una clase para implementar**IValidaciónPersonalizada** interfaz.

En el fragmento de código que se proporciona a continuación, hemos implementado una validación personalizada para realizar las siguientes comprobaciones:

- Compruebe si la dirección de la celda es precisa en la que se agrega la validación
- Compruebe si el tipo de datos del valor de la celda es doble
- Comprobar si el valor de la celda es mayor que 100



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Accediendo a la Validación**
Una vez que se agrega una validación a una celda específica de la hoja de trabajo, los desarrolladores pueden solicitar que accedan y modifiquen los atributos de una validación específica en tiempo de ejecución. Entonces, Aspose.Cells.GridDesktop ha hecho que sea sencillo para los desarrolladores realizar esta tarea.

Para acceder a una validación específica, siga los pasos a continuación:

-  Accede a un deseado**Hoja de cálculo**
-  Accede a una determinada**Validación**en la hoja de trabajo especificando el nombre de la celda en la que se aplicó la validación
-  Editar**Validación** atributos, si se desea



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**Validaciones** La colección tiene dos indexadores. Un indexador (que se usa en el ejemplo a continuación) permite acceder a un**Validación** objeto tomando un nombre de celda como su índice mientras que el otro indexador toma dos parámetros (es decir, números de fila y columna) para realizar la misma tarea.

{{% /alert %}} 
### **Eliminación de la validación**
Para eliminar una validación específica de la hoja de trabajo, siga los pasos a continuación:

-  Accede a un deseado**Hoja de cálculo**
-  Eliminar un específico**Validación** desde el**Hoja de cálculo** especificando el nombre de la celda en la que se aplicó la validación



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
