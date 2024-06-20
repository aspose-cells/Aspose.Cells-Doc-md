---
title: Proteger y Desproteger Hoja de Cálculo
type: docs
weight: 50
url: /es/java/protect-and-unprotect-worksheet/
---

## **Proteger hojas de cálculo**

Cuando una hoja de cálculo está protegida, las acciones que un usuario puede realizar están restringidas. Por ejemplo, no pueden introducir datos, insertar o eliminar filas o columnas, etc. Las opciones generales de protección en Microsoft Excel son:

- Contenidos
- Objetos
- Escenarios

Las hojas de cálculo protegidas no ocultan ni protegen datos sensibles, por lo que es diferente del cifrado de archivos. En general, la protección de hojas de cálculo es adecuada para propósitos de presentación. Evita que el usuario final modifique datos, contenido y formato en la hoja de cálculo.

### **Agregar o Eliminar Protección**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase Workbook contiene una WorksheetCollection que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La clase Worksheet proporciona el método [**Protect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)) que se utiliza para aplicar protección a una hoja de cálculo. El método Protect acepta los siguientes parámetros:

- Tipo de Protección, el tipo de protección a aplicar en la hoja de cálculo. El tipo de protección se aplica con la ayuda de la enumeración [**ProtectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType).
- Nueva contraseña, la nueva contraseña utilizada para proteger la hoja de cálculo.
- Contraseña anterior, la contraseña anterior, si la hoja de cálculo ya está protegida con contraseña. Si la hoja de cálculo no está protegida, simplemente pase un nulo.

La enumeración ProtectionType contiene los siguientes tipos de protecciones predefinidos:

|**Tipos de protección**|**Descripción**|
| :- | :- |
|[**ALL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|El usuario no puede modificar nada en esta hoja de cálculo|
|[**CONTENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|El usuario no puede ingresar datos en esta hoja de cálculo|
|[**OBJECTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|El usuario no puede modificar objetos de dibujo|
|[**SCENARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|El usuario no puede modificar escenarios guardados|
|[**STRUCTURE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|El usuario no puede modificar la estructura guardada|
|[**WINDOWS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|El usuario no puede modificar ventanas guardadas|
|[**NONE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Sin protección|

El ejemplo a continuación muestra cómo proteger una hoja de cálculo con una contraseña.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

Después de que el código anterior se utiliza para proteger la hoja de cálculo, verifique la protección en la hoja de cálculo abriéndola. Una vez que abra el archivo e intente agregar algunos datos a la hoja de cálculo, se muestra el siguiente cuadro de diálogo:

**Un cuadro de diálogo advirtiendo que un usuario no puede modificar la hoja de cálculo** 

![todo:image_alt_text](protect-and-unprotect-worksheet_1.png)

Para trabajar en la hoja de cálculo, desproteja la hoja de cálculo seleccionando **Proteger** y luego **Desproteger hoja** del elemento de menú **Herramientas**, como se muestra a continuación.

**Seleccionar el elemento de menú Desproteger hoja** 

![todo:image_alt_text](protect-and-unprotect-worksheet_2.png)

Se abre un cuadro de diálogo solicitando una contraseña.

**Ingresar contraseña para desproteger la hoja de trabajo** 

![todo:image_alt_text](protect-and-unprotect-worksheet_3.png)

### **Protegiendo algunas celdas**

Puede haber ciertos escenarios en los que necesite bloquear solo algunas celdas en la hoja de cálculo. Si desea bloquear celdas específicas en la hoja de cálculo, debe desbloquear todas las demás celdas en la hoja de cálculo. Todas las celdas en una hoja de cálculo ya están inicializadas para bloquear, puede verificar esto abriendo cualquier archivo de Excel en MS Excel y haciendo clic en **Formato | Celdas...** para mostrar el cuadro de diálogo **Formato de celdas** y luego hacer clic en la pestaña Protección y ver que una casilla de verificación etiquetada como "Bloqueada" está marcada de forma predeterminada.

A continuación se presentan los dos enfoques para implementar la tarea.

**Método1:**

Los siguientes puntos describen cómo bloquear algunas celdas usando MS Excel. Este método se aplica a las versiones de Microsoft Office Excel 97, 2000, 2002, 2003 y posteriores.

1. Seleccione toda la hoja de cálculo haciendo clic en el botón Seleccionar todo (el rectángulo gris directamente encima del número de fila para la fila 1 y a la izquierda de la letra de columna A).
1. Haga clic en Celdas en el menú Formato, haga clic en la pestaña Protección y luego desactive la casilla de verificación Bloqueada.

   Esto desbloquea todas las celdas en la hoja de cálculo

{{% alert color="primary" %}}

Si el comando de celdas no está disponible, es posible que partes de la hoja de cálculo ya estén bloqueadas. En el menú Herramientas, apunte a Protección y luego haga clic en Desproteger hoja.

{{% /alert %}}

1. Seleccione solo las celdas que desea bloquear y repita el paso 2, pero esta vez seleccione la casilla Bloqueada.
1. En el menú **Herramientas**, seleccione **Protección**, haga clic en **Proteger hoja** y luego haga clic en **Aceptar**.

{{% alert color="primary" %}}

En el cuadro de diálogo Proteger hoja, tiene la opción de especificar una contraseña y seleccionar los elementos que desea que los usuarios puedan cambiar.

{{% /alert %}}

**Método2:**

En este método, solo utilizamos la API de Aspose.Cells para realizar la tarea.

El siguiente ejemplo muestra cómo proteger algunas celdas en la hoja de cálculo. Primero desbloquea todas las celdas de la hoja de cálculo y luego bloquea 3 celdas (A1, B1, C1) en ella. Finalmente, protege la hoja de cálculo. Una fila/columna tiene una API de estilo que contiene un método set Locked. Puede usar este método para bloquear o desbloquear la fila/columna.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Proteger una fila en la hoja de cálculo**

Aspose.Cells le permite bloquear fácilmente cualquier fila en la hoja de cálculo. Aquí, podemos utilizar el método [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) de la clase [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) para aplicar estilo a una fila específica en la hoja de cálculo. Este método toma dos argumentos: un objeto [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) y una estructura [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) que tiene todos los miembros relacionados con el formato aplicado.

El siguiente ejemplo muestra cómo proteger una fila en la hoja de cálculo. Primero desbloquea todas las celdas de la hoja de cálculo y luego bloquea la primera fila en ella. Finalmente, protege la hoja de cálculo. Una fila/columna tiene una API de estilo que contiene un método setCellLocked. Puede bloquear o desbloquear la fila/columna utilizando la estructura StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Proteger una columna en la hoja de cálculo**

Aspose.Cells le permite bloquear fácilmente cualquier columna en la hoja de cálculo. Aquí, podemos hacer uso del método [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) de la clase [**Column**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) para aplicar estilo a una columna específica en la hoja de cálculo. Este método toma dos argumentos: un objeto [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) y una estructura [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) que tiene todos los miembros relacionados con el formato aplicado.

El siguiente ejemplo muestra cómo proteger una columna en la hoja de cálculo. Primero desbloquea todas las celdas de la hoja de cálculo y luego bloquea la primera columna en ella. Finalmente, protege la hoja de cálculo. Una fila/columna tiene una API de estilo que contiene un método set Locked. Puede bloquear o desbloquear la fila/columna utilizando la estructura StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Desproteger una Hoja de Cálculo**

[Proteger hojas de cálculo](/cells/es/java/protect-and-unprotect-worksheet/#protect-worksheets) y [Configuraciones Avanzadas de Protección desde Excel XP](/cells/es/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) discuten diferentes enfoques para proteger hojas de cálculo. ¿Qué pasa si un desarrollador necesita quitar la protección de una hoja de cálculo protegida en tiempo de ejecución para que se puedan realizar algunos cambios en el archivo? Esto se puede hacer fácilmente con Aspose.Cells.

### **Usar Microsoft Excel**

Para quitar la protección de una hoja de cálculo:

Desde el menú **Herramientas**, selecciona **Protección** seguido por **Desproteger hoja**.

**Seleccionar Desproteger hoja** 

![todo:image_alt_text](protect-and-unprotect-worksheet_4.png)

La protección se quita, a menos que la hoja de trabajo esté protegida con contraseña. En este caso, se solicita un cuadro de diálogo para la contraseña.

**Ingresar contraseña para desproteger la hoja de trabajo** 

![todo:image_alt_text](protect-and-unprotect-worksheet_5.png)

### **Usar Aspose.Cells**

Una hoja de trabajo puede desprotegerse llamando al método [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). El método [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--) puede utilizarse de dos formas, descritas a continuación.

### **Desproteger una hoja de trabajo simplemente protegida**

Una hoja de trabajo simplemente protegida no está protegida con una contraseña. Estas hojas de trabajo pueden desprotegerse llamando al método desproteger sin pasar un parámetro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Desproteger una hoja de trabajo protegida con contraseña**

Una hoja de trabajo protegida con contraseña está protegida con una contraseña. Estas hojas de trabajo pueden desprotegerse llamando a una versión sobrecargada del método Desproteger que toma la contraseña como parámetro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Configuración de Protección Avanzada desde Excel XP**

[Protección de hojas de trabajo](/cells/es/java/protect-and-unprotect-worksheet/#protect-worksheets) discute la protección de una hoja de trabajo en Microsoft Excel 97 y 2000. Pero, desde la versión de Excel 2002 o XP, Microsoft ha añadido muchas configuraciones avanzadas de protección. Estas configuraciones de protección restringen o permiten a los usuarios:

- Eliminar filas o columnas.
- Editar contenido, objetos o escenarios.
- Formatear celdas, filas o columnas.
- Insertar filas, columnas o hiperenlaces.
- Seleccionar celdas bloqueadas o desbloqueadas.
- Utilizar tablas dinámicas y mucho más.

Aspose.Cells admite todas las configuraciones avanzadas de protección ofrecidas por Excel XP y versiones posteriores.

### **Configuraciones de protección avanzada utilizando Excel XP y versiones posteriores**

Para ver las configuraciones de protección disponibles en Excel XP:

1. Desde el menú **Herramientas**, seleccione **Proteger** seguido de **Proteger hoja**.
   Se muestra un cuadro de diálogo.

   **Cuadro de diálogo para mostrar opciones de protección en Excel XP**

![todo:image_alt_text](protect-and-unprotect-worksheet_6.png)

1. Permitir o restringir funciones de las hojas de cálculo o aplicar una contraseña.

### **Configuraciones de protección avanzada utilizando Aspose.Cells**

Aspose.Cells soporta todas las configuraciones de protección avanzada.

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase Workbook contiene una colección WorksheetCollection que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La clase Worksheet proporciona la propiedad Protection que se utiliza para aplicar estas configuraciones avanzadas de protección. La propiedad Protection es en realidad un objeto de la clase [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) que encapsula varias propiedades booleanas para deshabilitar o habilitar restricciones.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

A continuación se muestra un pequeño ejemplo de aplicación. Abre un archivo de Excel y utiliza la mayoría de los ajustes de protección avanzados admitidos por Excel XP y versiones posteriores.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Guarde el archivo en formato EXCEL97TO2003 o XLSX porque estas configuraciones avanzadas de protección solo son compatibles con MS Excel XP y versiones posteriores.

{{% /alert %}}

### **Problema de bloqueo de celdas**

Si desea restringir a los usuarios de editar celdas, las celdas deben estar bloqueadas antes de aplicar cualquier configuración de protección. De lo contrario, las celdas pueden editarse incluso si la hoja de cálculo está protegida. En Microsoft Excel XP, las celdas se pueden bloquear a través del siguiente cuadro de diálogo:

**Cuadro de diálogo para bloquear celdas en Excel XP** 

![todo:image_alt_text](protect-and-unprotect-worksheet_7.png)

Es posible bloquear celdas usando la API de Aspose.Cells también. Cada celda tiene una API de estilo que contiene un método setLocked. Úselo para bloquear o desbloquear celdas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
