---
title: Protección de hojas de trabajo
type: docs
weight: 10
url: /es/net/protecting-worksheets/
---
{{% alert color="primary" %}}

Cuando una hoja de trabajo está protegida, las acciones que un usuario puede realizar están restringidas. Por ejemplo, no pueden ingresar datos, insertar o eliminar filas o columnas, etc.

{{% /alert %}}

## **Proteger hojas de trabajo**

### **Introducción**

Las opciones generales de protección en Microsoft Excel son:

- Contenido
- Objetos
- Escenarios

Las hojas de trabajo protegidas no ocultan ni protegen datos confidenciales, por lo que es diferente del cifrado de archivos. En general, la protección de la hoja de trabajo es adecuada para fines de presentación. Evita que el usuario final modifique los datos, el contenido y el formato de la hoja de trabajo.

### **Proteger una hoja de trabajo**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)clase.

 los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)la clase proporciona la[**Proteger**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) método que se utiliza para aplicar protección en la hoja de trabajo.[**Proteger**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) método acepta los siguientes parámetros:

-  Tipo de protección, el tipo de protección que se aplicará en la hoja de trabajo. El tipo de protección se aplica con la ayuda del[**Tipo de protección**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)enumeración.
- Nueva contraseña, la nueva contraseña utilizada para proteger la hoja de trabajo.
- Old Password, la contraseña anterior, si la hoja de trabajo ya está protegida con contraseña. Si la hoja de trabajo aún no está protegida, simplemente pase nulo.

 los[**Tipo de protección**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)La enumeración contiene los siguientes tipos de protección predefinidos:

|**Tipos de protección**|**Descripción**|
|:- |:- |
|Todos|El usuario no puede modificar nada en esta hoja de trabajo|
|Contenido|El usuario no puede ingresar datos en esta hoja de trabajo|
|Objetos|El usuario no puede modificar los objetos de dibujo.|
|Escenarios|El usuario no puede modificar los escenarios guardados|
|Estructura|El usuario no puede modificar la estructura.|
|Windows|La protección se aplica a las ventanas.|
|Ninguna|No se aplica protección|

El siguiente ejemplo muestra cómo proteger una hoja de trabajo con una contraseña.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

Después de usar el código anterior para proteger la hoja de trabajo, puede verificar la protección en la hoja de trabajo abriéndola. Una vez que abra el archivo e intente agregar algunos datos a la hoja de trabajo, verá el siguiente cuadro de diálogo:

|**Un cuadro de diálogo que advierte que un usuario no puede modificar la hoja de cálculo**|
|:- |
|![todo:imagen_alternativa_texto](protecting-worksheets_1.png)|

Para trabajar en la hoja de trabajo, desproteja la hoja de trabajo seleccionando el**Proteccion** , después**Desproteger hoja** desde el**Instrumentos** opción del menú.

Después de seleccionar el elemento de menú Desproteger hoja, se abrirá un cuadro de diálogo que le pedirá que ingrese la contraseña para que pueda trabajar en la hoja de trabajo como se muestra a continuación:

|![todo:imagen_alternativa_texto](protecting-worksheets_2.png)|

### **Proteja algunos Cells en la hoja de trabajo usando Microsoft Excel**

 Puede haber ciertos escenarios en los que necesite bloquear algunas celdas solo en la hoja de trabajo. Si desea bloquear algunas celdas específicas en la hoja de cálculo, debe desbloquear todas las demás celdas de la hoja de cálculo. Todas las celdas en una hoja de trabajo ya están inicializadas para el bloqueo, puede verificar esto abriendo cualquier archivo de Excel en MS Excel y hacer clic en el botón**Formato | Cells...** mostrar**Formato Cells**cuadro de diálogo y luego haga clic en el**Proteccion** pestaña y ver una casilla de verificación con la etiqueta "Bloqueado" está marcada de forma predeterminada.

Los siguientes puntos describen cómo bloquear algunas celdas usando MS Excel. Este método se aplica a Microsoft Office Excel 97, 2000, 2002, 2003 y versiones posteriores.

1.  Seleccione toda la hoja de trabajo haciendo clic en el**Seleccionar todo** (el rectángulo gris directamente encima del número de fila para la fila 1 y a la izquierda de la letra A de la columna).
1.  Hacer clic**Cells** sobre el**Formato** menú, haga clic en el**Proteccion** ficha y, a continuación, borre la**bloqueado** caja.
 Esto desbloquea todas las celdas en la hoja de cálculo.
 Si el**Cells** El comando no está disponible, es posible que partes de la hoja de trabajo ya estén bloqueadas. Sobre el**Instrumentos** menú, señale**Proteccion** y luego haga clic en**Desproteger hoja**.
1.  Seleccione solo las celdas que desea bloquear y repita el paso 2, pero esta vez seleccione la**bloqueado** caja.
1.  Sobre el**Instrumentos** menú, señale**Proteccion** , haga clic**hoja de protección** y luego haga clic**OK**.
1.  En el**hoja de protección** cuadro de diálogo, tiene la opción de especificar una contraseña y seleccionar los elementos que desea que los usuarios puedan cambiar.

### **Proteja algunos Cells en la hoja de trabajo usando Aspose Cells**

En este método, usamos Aspose.Cells API solo para realizar la tarea.

 Ejemplo: El siguiente ejemplo muestra cómo proteger algunas celdas en la hoja de cálculo. Primero desbloquea todas las celdas en la hoja de trabajo y luego bloquea 3 celdas (A1, B1, C1) en ella. Finalmente, protege la hoja de trabajo. los[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto contiene una propiedad booleana,[**Está bloqueado**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Puedes configurar[**Está bloqueado**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) propiedad a verdadero o falso y aplicar*Columna/Fila.ApplyStyle()* para bloquear o desbloquear la fila/columna con los atributos deseados.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **Proteger una fila en la hoja de trabajo**

 Aspose.Cells le permite bloquear fácilmente cualquier fila en la hoja de trabajo. Aquí, podemos hacer uso de[**AplicarEstilo()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) método de[**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) clase para aplicar[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) a una fila en particular en la hoja de trabajo. Este método toma dos argumentos: un[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto y[**Bandera de estilo**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) objeto que tiene todos los miembros relacionados con el formato aplicado.

 El siguiente ejemplo muestra cómo proteger una fila en la hoja de trabajo. Primero desbloquea todas las celdas de la hoja de trabajo y luego bloquea la primera fila. Finalmente, protege la hoja de trabajo. los[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto contiene una propiedad booleana,[**Está bloqueado**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Puedes configurar[**Está bloqueado**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) propiedad a verdadero o falso para bloquear o desbloquear la fila/columna usando el[**Bandera de estilo**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objeto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **Proteger una columna en la hoja de trabajo**

 Aspose.Cells le permite bloquear fácilmente cualquier columna en la hoja de trabajo. Aquí, podemos hacer uso de[**AplicarEstilo()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) método de[**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) clase para aplicar[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) a una columna en particular en la hoja de trabajo. Este método toma dos argumentos: un[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto y[**Bandera de estilo**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objeto que tiene todos los miembros relacionados con el formato aplicado.

El siguiente ejemplo muestra cómo proteger una columna en la hoja de trabajo. Primero desbloquea todas las celdas en la hoja de trabajo y luego bloquea la primera columna en ella. Finalmente, protege la hoja de trabajo. los[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto contiene una propiedad booleana,[**Está bloqueado**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Puedes configurar[**Está bloqueado**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) propiedad a verdadero o falso para bloquear o desbloquear la fila/columna usando el[**Bandera de estilo**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objeto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **Permitir a los usuarios editar rangos**

El siguiente ejemplo muestra cómo permitir que los usuarios editen un rango en una hoja de cálculo protegida.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
