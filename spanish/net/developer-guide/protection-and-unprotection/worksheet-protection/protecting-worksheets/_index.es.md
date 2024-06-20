---
title: Protección de hojas de cálculo
type: docs
weight: 10
url: /es/net/protecting-worksheets/
---

{{% alert color="primary" %}}

Cuando una hoja de cálculo está protegida, las acciones que un usuario puede realizar están restringidas. Por ejemplo, no pueden ingresar datos, insertar o eliminar filas o columnas, etc.

{{% /alert %}}

## **Proteger hojas de cálculo**

### **Introducción**

Las opciones generales de protección en Microsoft Excel son:

- Contenidos
- Objetos
- Escenarios

Las hojas de cálculo protegidas no ocultan ni protegen datos sensibles, por lo que es diferente del cifrado de archivos. Generalmente, la protección de la hoja de cálculo es adecuada para fines de presentación. Evita que el usuario final modifique los datos, el contenido y el formato en la hoja de cálculo.

### **Proteger una hoja de cálculo**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona el método [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) que se utiliza para aplicar protección en la hoja de cálculo. El método [**Protect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) acepta los siguientes parámetros:

- Tipo de protección, el tipo de protección a aplicar en la hoja de cálculo. El tipo de protección se aplica con la ayuda de la enumeración [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype).
- Nueva contraseña, la nueva contraseña utilizada para proteger la hoja de cálculo.
- Contraseña antigua, la contraseña antigua, si la hoja de cálculo ya está protegida con contraseña. Si la hoja de cálculo no está protegida, simplemente pase nula.

La enumeración [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype) contiene los siguientes tipos de protecciones predefinidos:

|**Tipos de protección**|**Descripción**|
| :- | :- |
|All|El usuario no puede modificar nada en esta hoja de cálculo|
|Contents|El usuario no puede introducir datos en esta hoja de cálculo|
|Objects|El usuario no puede modificar objetos de dibujo|
|Scenarios|El usuario no puede modificar escenarios guardados|
|Structure|El usuario no puede modificar la estructura|
|Windows|La protección se aplica a las ventanas|
|None|No se aplica protección|

El ejemplo a continuación muestra cómo proteger una hoja de cálculo con una contraseña.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

Después de que se use el código anterior para proteger la hoja de cálculo, puede verificar la protección en la hoja de cálculo abriéndola. Una vez que abra el archivo e intente agregar datos a la hoja de cálculo, verá el siguiente cuadro de diálogo:

|**Un aviso de diálogo de que el usuario no puede modificar la hoja de cálculo**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Para trabajar en la hoja de cálculo, desprotege la hoja de cálculo seleccionando **Protección**, luego **Desproteger hoja** del elemento de menú **Herramientas**.

Después de seleccionar la opción Desproteger hoja, se abrirá un cuadro de diálogo que te pedirá que ingreses la contraseña para que puedas trabajar en la hoja de cálculo como se muestra a continuación:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Proteger algunas celdas en la hoja de cálculo utilizando Microsoft Excel**

Puede haber ciertos escenarios en los que necesites bloquear solo algunas celdas en la hoja de cálculo. Si deseas bloquear celdas específicas en la hoja de cálculo, debes desbloquear todas las demás celdas de la hoja de cálculo. Todas las celdas de una hoja de cálculo ya están inicializadas para bloquearse, puedes verificar esto abriendo cualquier archivo de Excel en MS Excel y haciendo clic en **Formato | Celdas...** para mostrar el cuadro de diálogo **Formato de celdas** y luego hacer clic en la pestaña **Protección** y ver que hay una casilla de verificación etiquetada como "Bloqueada" marcada de manera predeterminada.

Los siguientes puntos describen cómo bloquear algunas celdas usando MS Excel. Este método se aplica a las versiones de Microsoft Office Excel 97, 2000, 2002, 2003 y posteriores.

1. Selecciona toda la hoja de cálculo haciendo clic en el botón **Seleccionar todo** (el rectángulo gris directamente arriba del número de fila para la fila 1 y a la izquierda de la letra de la columna A).
1. Haz clic en **Celdas** en el menú **Formato**, haz clic en la pestaña **Protección**, y luego desmarca la casilla de verificación **Bloqueada**.
   Esto desbloquea todas las celdas en la hoja de cálculo
   Si el comando **Celdas** no está disponible, es posible que partes de la hoja de cálculo ya estén bloqueadas. En el menú **Herramientas**, apunta a **Protección**, y luego haz clic en **Desproteger hoja**.
1. Selecciona solo las celdas que deseas bloquear y repite el paso 2, pero esta vez selecciona la casilla de verificación **Bloqueada**.
1. En el menú **Herramientas**, apunta a **Protección**, haz clic en **Proteger hoja** y luego haz clic en **Aceptar**.
1. En el cuadro de diálogo **Proteger hoja**, tienes la opción de especificar una contraseña y seleccionar los elementos que quieres que los usuarios puedan cambiar.

### **Proteger algunas celdas en la hoja de cálculo utilizando Aspose Cells**

En este método, solo utilizamos la API de Aspose.Cells para realizar la tarea.

Ejemplo: El siguiente ejemplo muestra cómo proteger algunas celdas en la hoja de cálculo. Desbloquea todas las celdas en la hoja de cálculo primero y luego bloquea 3 celdas (A1, B1, C1) en ella. Finalmente, protege la hoja de cálculo. El objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) contiene una propiedad booleana, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Puedes establecer la propiedad [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) en verdadero o falso y aplicar el método *Columna/Fila.AplicarEstilo()* para bloquear o desbloquear la fila/columna con los atributos deseados.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **Proteger una fila en la hoja de cálculo**

Aspose.Cells te permite bloquear fácilmente cualquier fila en la hoja de cálculo. Aquí, podemos utilizar el método [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) de la clase [**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) para aplicar [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) a una fila específica en la hoja de cálculo. Este método toma dos argumentos: un objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) y un objeto [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) que tiene todos los miembros relacionados con el formato aplicado.

El siguiente ejemplo muestra cómo proteger una fila en la hoja de cálculo. Desbloquea todas las celdas en la hoja de cálculo primero y luego bloquea la primera fila en ella. Finalmente, protege la hoja de cálculo. El objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) contiene una propiedad booleana, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Puedes establecer la propiedad [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) en verdadero o falso para bloquear o desbloquear la fila/columna utilizando el objeto [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **Proteger una columna en la hoja de cálculo**

Aspose.Cells te permite bloquear fácilmente cualquier columna en la hoja de cálculo. Aquí, podemos utilizar el método [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) de la clase [**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) para aplicar [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) a una columna específica en la hoja de cálculo. Este método toma dos argumentos: un objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) y un objeto [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) que tiene todos los miembros relacionados con el formato aplicado.

El siguiente ejemplo muestra cómo proteger una columna en la hoja de cálculo. Desbloquea todas las celdas en la hoja de cálculo primero y luego bloquea la primera columna en ella. Finalmente, protege la hoja de cálculo. El objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) contiene una propiedad booleana, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Puede establecer la propiedad [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) en true o false para bloquear o desbloquear la fila/columna utilizando el objeto [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **Permitir a los usuarios editar rangos**

El siguiente ejemplo muestra cómo permitir a los usuarios editar un rango en una hoja de cálculo protegida.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
