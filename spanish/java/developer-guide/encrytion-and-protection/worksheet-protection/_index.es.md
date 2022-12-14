---
title: Hoja de trabajo de protección y desprotección
type: docs
weight: 50
url: /es/java/protect-and-unprotect-worksheet/
---
## **Proteger hojas de trabajo**

Cuando una hoja de trabajo está protegida, las acciones que un usuario puede realizar están restringidas. Por ejemplo, no pueden ingresar datos, insertar o eliminar filas o columnas, etc. Las opciones generales de protección en Microsoft Excel son:

- Contenido
- Objetos
- Escenarios

Las hojas de trabajo protegidas no ocultan ni protegen datos confidenciales, por lo que es diferente del cifrado de archivos. En general, la protección de la hoja de trabajo es adecuada para fines de presentación. Evita que el usuario final modifique datos, contenido y formato en la hoja de trabajo.

### **Agregar o quitar protección**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. La clase Workbook contiene una WorksheetCollection que permite acceder a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase.

 La clase Worksheet proporciona la[**Proteger**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)) método que se utiliza para aplicar protección a una hoja de trabajo. El método Protect acepta los siguientes parámetros:

-  Tipo de protección, el tipo de protección que se aplicará en la hoja de trabajo. El tipo de protección se aplica con la ayuda del[**Tipo de protección**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType) enumeración.
- Nueva contraseña, la nueva contraseña utilizada para proteger la hoja de trabajo.
- Old Password, la contraseña anterior, si la hoja de trabajo ya está protegida con contraseña. Si la hoja de trabajo aún no está protegida, simplemente pase un valor nulo.

La enumeración ProtectionType contiene los siguientes tipos de protección predefinidos:

|**Tipos de protección**|**Descripción**|
|:- |:- |
|[**TODOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|El usuario no puede modificar nada en esta hoja de trabajo|
|[**CONTENIDO**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|El usuario no puede ingresar datos en esta hoja de cálculo|
|[**OBJETOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|El usuario no puede modificar los objetos de dibujo|
|[**ESCENARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|El usuario no puede modificar los escenarios guardados|
|[**ESTRUCTURA**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|El usuario no puede modificar la estructura guardada|
|[**VENTANAS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|El usuario no puede modificar las ventanas guardadas|
|[**NINGUNA**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Sin protección|

El siguiente ejemplo muestra cómo proteger una hoja de trabajo con una contraseña.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

Después de usar el código anterior para proteger la hoja de trabajo, verifique la protección en la hoja de trabajo abriéndola. Una vez que abre el archivo e intenta agregar algunos datos a la hoja de trabajo, se muestra el siguiente cuadro de diálogo:

**Un cuadro de diálogo que advierte que un usuario no puede modificar la hoja de cálculo** 

![todo:imagen_alternativa_texto](protect-and-unprotect-worksheet_1.png)

Para trabajar en la hoja de trabajo, desproteja la hoja de trabajo seleccionando el**Proteccion** , después**Desproteger hoja** desde el**Instrumentos** elemento de menú como se muestra a continuación.

**Selección del elemento de menú Desproteger hoja** 

![todo:imagen_alternativa_texto](protect-and-unprotect-worksheet_2.png)

Se abre un cuadro de diálogo que solicita una contraseña.

**Ingresar contraseña para desproteger la hoja de trabajo** 

![todo:imagen_alternativa_texto](protect-and-unprotect-worksheet_3.png)

### **Protegiendo a unos pocos Cells**

 Puede haber ciertos escenarios en los que necesite bloquear algunas celdas solo en la hoja de trabajo. Si desea bloquear algunas celdas específicas en la hoja de cálculo, debe desbloquear todas las demás celdas de la hoja de cálculo. Todas las celdas en una hoja de trabajo ya están inicializadas para el bloqueo, puede verificar esto abriendo cualquier archivo de Excel en MS Excel y hacer clic en el botón**Formato | Cells...** mostrar**Formato Cells** cuadro de diálogo y luego haga clic en la pestaña Protección y vea una casilla de verificación etiquetada como "Bloqueada" que está marcada de forma predeterminada.

Los siguientes son los dos enfoques para implementar la tarea.

**Método 1:**

Los siguientes puntos describen cómo bloquear algunas celdas usando MS Excel. Este método se aplica a Microsoft Office Excel 97, 2000, 2002, 2003 y versiones posteriores.

1. Seleccione toda la hoja de trabajo haciendo clic en el botón Seleccionar todo (el rectángulo gris directamente arriba del número de fila para la fila 1 y a la izquierda de la letra A de la columna).
1. Haga clic en Cells en el menú Formato, haga clic en la pestaña Protección y luego desactive la casilla de verificación Bloqueado.

 Esto desbloquea todas las celdas en la hoja de cálculo.

{{% alert color="primary" %}}

Si el comando de celdas no está disponible, es posible que partes de la hoja de trabajo ya estén bloqueadas. En el menú Herramientas, seleccione Protección y luego haga clic en Desproteger hoja.

{{% /alert %}}

1. Seleccione solo las celdas que desea bloquear y repita el paso 2, pero esta vez seleccione la casilla de verificación Bloqueado.
1.  Sobre el**Instrumentos** menú, seleccione**Proteccion** , haga clic**hoja de protección** y luego haga clic en**OK**.

{{% alert color="primary" %}}

En el cuadro de diálogo Proteger hoja, tiene la opción de especificar una contraseña y seleccionar los elementos que desea que los usuarios puedan cambiar.

{{% /alert %}}

**Método2:**

En este método, usamos Aspose.Cells API solo para realizar la tarea.

El siguiente ejemplo muestra cómo proteger algunas celdas en la hoja de trabajo. Primero desbloquea todas las celdas en la hoja de trabajo y luego bloquea 3 celdas (A1, B1, C1) en ella. Finalmente, protege la hoja de trabajo. Una fila/columna tiene un estilo API que además contiene un método bloqueado establecido. Puede utilizar este método para bloquear o desbloquear la fila/columna.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Proteger una fila en la hoja de trabajo**

 Aspose.Cells le permite bloquear fácilmente cualquier fila en la hoja de trabajo. Aquí, podemos hacer uso de[**aplicarEstilo()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) método de[**Fila**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) class para aplicar Style a una fila en particular en la hoja de cálculo. Este método toma dos argumentos: un[**Estilo**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objeto y[**Bandera de estilo**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) estructura que tiene todos los miembros relacionados con el formato aplicado.

El siguiente ejemplo muestra cómo proteger una fila en la hoja de trabajo. Primero desbloquea todas las celdas de la hoja de trabajo y luego bloquea la primera fila. Finalmente, protege la hoja de trabajo. Una fila/columna tiene un estilo API que además contiene un método setCellLocked. Puede bloquear o desbloquear la fila/columna usando la estructura StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Proteger una columna en la hoja de trabajo**

 Aspose.Cells le permite bloquear fácilmente cualquier columna en la hoja de trabajo. Aquí, podemos hacer uso de[**aplicarEstilo()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) método de[**Columna**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) class para aplicar Estilo a una columna en particular en la hoja de trabajo. Este método toma dos argumentos: un[**Estilo**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objeto y[**Bandera de estilo**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) estructura que tiene todos los miembros relacionados con el formato aplicado.

El siguiente ejemplo muestra cómo proteger una columna en la hoja de trabajo. Primero desbloquea todas las celdas en la hoja de trabajo y luego bloquea la primera columna en ella. Finalmente, protege la hoja de trabajo. Una fila/columna tiene un estilo API que además contiene un método bloqueado establecido. Puede bloquear o desbloquear la fila/columna usando la estructura StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Desproteger una hoja de trabajo**

[Protección de hojas de trabajo](/cells/es/java/protect-and-unprotect-worksheet/#protect-worksheets) y[Configuración de protección avanzada desde Excel XP](/cells/es/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) discutieron diferentes enfoques para proteger las hojas de trabajo. ¿Qué sucede si un desarrollador necesita eliminar la protección de una hoja de trabajo protegida en tiempo de ejecución para que se puedan realizar algunos cambios en el archivo? Esto se puede hacer fácilmente con Aspose.Cells.

### **Usando Microsoft Excel**

Para eliminar la protección de una hoja de trabajo:

 Desde el**Instrumentos** menú, seleccione**Proteccion** seguido por**Desproteger hoja**.

**Seleccionar hoja desprotegida** 

![todo:imagen_alternativa_texto](protect-and-unprotect-worksheet_4.png)

Se elimina la protección, a menos que la hoja de trabajo esté protegida con contraseña. En este caso, un cuadro de diálogo solicita la contraseña.

**Ingresar contraseña para desproteger la hoja de trabajo** 

![todo:imagen_alternativa_texto](protect-and-unprotect-worksheet_5.png)

### **Usando Aspose.Cells**

 Una hoja de trabajo se puede desproteger llamando al[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[**Desproteger**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect() ) método. los[**Desproteger**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect()) El método se puede utilizar de dos maneras, que se describen a continuación.

### **Desproteger una hoja de trabajo simplemente protegida**

Una hoja de trabajo simplemente protegida es aquella que no está protegida con una contraseña. Estas hojas de trabajo se pueden desproteger llamando al método unprotect sin pasar un parámetro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Desproteger una hoja de trabajo protegida con contraseña**

Una hoja de trabajo protegida con contraseña es aquella que está protegida con una contraseña. Estas hojas de trabajo se pueden desproteger llamando a una versión sobrecargada del método Unprotect que toma la contraseña como parámetro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Configuración de protección avanzada desde Excel XP**

[Protección de hojas de trabajo](/cells/es/java/protect-and-unprotect-worksheet/#protect-worksheets) discutió la protección de una hoja de trabajo en Microsoft Excel 97 y 2000. Pero desde el lanzamiento de Excel 2002 o XP, Microsoft ha agregado muchas configuraciones de protección avanzadas. Estas configuraciones de protección restringen o permiten a los usuarios:

- Eliminar filas o columnas.
- Edita contenidos, objetos o escenarios.
- Formato de celdas, filas o columnas.
- Inserta filas, columnas o hipervínculos.
- Seleccione celdas bloqueadas o desbloqueadas.
- Utilice tablas dinámicas y mucho más.

Aspose.Cells admite todas las configuraciones de protección avanzadas que ofrece Excel XP y versiones posteriores.

### **Configuración de protección avanzada con Excel XP y versiones posteriores**

Para ver la configuración de protección disponible en Excel XP:

1.  Desde el**Instrumentos** menú, seleccione**Proteccion** seguido por**hoja de protección**.
 Se muestra un cuadro de diálogo.

   **Diálogo para mostrar opciones de protección en Excel XP**

![todo:imagen_alternativa_texto](protect-and-unprotect-worksheet_6.png)

1. Permita o restrinja las funciones de las hojas de trabajo o aplique una contraseña.

### **Configuración de protección avanzada usando Aspose.Cells**

Aspose.Cells admite todas las configuraciones de protección avanzada.

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. La clase Workbook contiene una colección WorksheetCollection que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase.

 La clase Worksheet proporciona la propiedad Protection que se utiliza para aplicar esta configuración de protección avanzada. La propiedad de Protección es de hecho un objeto de la[**Proteccion**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) clase que encapsula varias propiedades booleanas para deshabilitar o habilitar restricciones.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

A continuación se muestra una pequeña aplicación de ejemplo. Abre un archivo de Excel y utiliza la mayoría de las configuraciones de protección avanzadas compatibles con Excel XP y versiones posteriores.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Guarde el archivo en formato EXCEL97TO2003 o XLSX porque esta configuración de protección avanzada solo es compatible con MS Excel XP y versiones posteriores.

{{% /alert %}}

### **Cell Problema de bloqueo**

Si desea restringir que los usuarios editen celdas, las celdas deben bloquearse antes de que se aplique cualquier configuración de protección. De lo contrario, las celdas se pueden editar incluso si la hoja de trabajo está protegida. En Microsoft Excel XP, las celdas se pueden bloquear a través del siguiente cuadro de diálogo:

**Diálogo para bloquear celdas en Excel XP** 

![todo:imagen_alternativa_texto](protect-and-unprotect-worksheet_7.png)

También es posible bloquear celdas usando el Aspose.Cells API. Cada celda tiene un estilo API que además contiene un método setLocked. Úselo para bloquear o desbloquear celdas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
