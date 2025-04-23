---
title: Importar y colocar datos de manera inteligente con Marcadores Inteligentes
linktitle: Marcadores inteligentes
type: docs
weight: 190
url: /es/net/using-smart-markers/
description: Importar y colocar datos de manera inteligente según las plantillas de archivos de Excel con la biblioteca Aspose.Cells.
---


## **Introducción**
**Los marcadores inteligentes** se utilizan para informar a Aspose.Cells qué información colocar en una hoja de cálculo de Microsoft Excel diseñada. Los marcadores inteligentes le permiten crear plantillas que contienen solo información y formato específicos.
## **Hoja de cálculo de diseño y Marcadores inteligentes**
Las hojas de cálculo de diseño son archivos Excel estándar que contienen formato visual, fórmulas y marcadores inteligentes. Pueden contener marcadores inteligentes que hacen referencia a una o más fuentes de datos, como información de un proyecto e información de contactos relacionados. Los marcadores inteligentes se escriben en las celdas donde desea la información.

Todos los marcadores inteligentes comienzan con &=. Un ejemplo de marcador de datos es &=Party.FullName. Si el marcador de datos da como resultado más de un elemento, por ejemplo, una fila completa, entonces las filas siguientes se mueven automáticamente para dar cabida a la nueva información. De esta manera, los subtotales y totales pueden colocarse en la fila inmediatamente después del marcador de datos para realizar cálculos basados en la información insertada. Para realizar cálculos en las filas insertadas, utilice **formulas dinámicas**.

Los marcadores inteligentes consisten en las partes de **fuente de datos** y **nombre del campo** para la mayoría de la información. También se puede enviar información especial con variables y matrices de variables. Las variables siempre llenan solo una celda, mientras que las matrices de variables pueden llenar varias. Utilice solo un marcador de datos por celda. Los marcadores inteligentes no utilizados se eliminan.

El marcador inteligente también puede contener parámetros. Los parámetros le permiten modificar la disposición de la información. Se agregan al final del marcador inteligente entre paréntesis como una lista separada por comas.
### **Opciones de Marcador Inteligente**
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==DynamicFormula 
&=&=RepeatDynamicFormula
### **Parámetros**
Se permiten los siguientes parámetros:

- **noadd** - No agregar filas adicionales para ajustar los datos.
- **skip:n** - Omitir n filas por cada fila de datos.
- **ascending:n** o **descending:n** - Ordenar datos en marcadores inteligentes. Si n es 1, entonces la columna es la primera clave del ordenador. Los datos se ordenan después de procesar la fuente de datos. Por ejemplo: &=Tabla1.Campo3(ascending:1).
- **horizontal** - Escribir datos de izquierda a derecha, en lugar de arriba a abajo.
- **numérico** - Convertir texto a número si es posible.
- **shift** - Desplazar hacia abajo o a la derecha, creando filas o columnas adicionales para ajustar datos. El parámetro de desplazamiento funciona de la misma manera que en Microsoft Excel.
- **copiarEstilo** - Copiar el estilo de la celda base a todas las celdas de esa columna.

Los parámetros noadd y skip se pueden combinar para insertar datos en filas alternas. Debido a que la plantilla se procesa de abajo hacia arriba, debe agregar noadd en la primera fila para evitar que se inserten filas adicionales antes de la fila alternativa.

Si tiene múltiples parámetros, sepárelos con comas, pero sin espacio: parámetroA,parámetroB,parámetroC

Las siguientes capturas de pantalla muestran cómo insertar datos en cada otra fila.

|**Archivo de plantilla**|**Archivo de salida**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|
### **Fórmulas dinámicas**
Las fórmulas dinámicas te permiten insertar fórmulas de Excel en celdas incluso cuando la fórmula hace referencia a filas que se insertarán durante el proceso de exportación. Las fórmulas dinámicas pueden repetirse para cada fila insertada o usar solo la celda donde se coloca el marcador de datos.

Las fórmulas dinámicas permiten las siguientes opciones adicionales:

- r - Número de fila actual.
- 2, -1 - Desplazamiento al número de fila actual.

Por ejemplo:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

En el marcador de fórmula dinámica, "-1" denota el desplazamiento a la fila actual en las columnas B y C respectivamente que se establecerá para la operación de división, el parámetro de omisión es una fila. Además, deberíamos especificar el siguiente carácter:

{{< highlight java >}}

 "~"

{{< /highlight >}}

como un carácter separador para aplicar más parámetros en las fórmulas dinámicas.

Las siguientes capturas de pantalla ilustran una fórmula dinámica y repetitiva y la hoja de cálculo de Excel resultante.

|**Archivo de plantilla**|**Archivo de salida**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
La celda "C1" contiene la fórmula **= A1*B1**, la celda "C2" contiene **= A2*B2** y la celda "C3" contiene **= A3*B3**.

Es muy fácil procesar los marcadores inteligentes. El siguiente ejemplo de código muestra cómo usar fórmulas dinámicas en marcadores inteligentes. Cargamos el [archivo de plantilla](templateDynamicFormulas.xlsx) y creamos datos de prueba, procesamos los marcadores para llenar datos en las celdas del marcador. 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **Usar Arrays Variables**
El siguiente ejemplo de código muestra cómo usar arrays variables en marcadores inteligentes. Colocamos un marcador de array variable en la celda A1 de la primera hoja de cálculo del libro dinámicamente que contiene una cadena de valores que establecemos para el marcador, procesamos los marcadores para llenar datos en las celdas contra el marcador. Finalmente, guardamos el archivo de Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **Agrupación de datos**
En algunos informes de Excel es posible que necesite dividir los datos en grupos para que sea más fácil de leer y analizar. Uno de los propósitos principales para dividir los datos en grupos es ejecutar cálculos (realizar operaciones de resumen) en cada grupo de registros.

Los marcadores inteligentes de Aspose.Cells le permiten agrupar los datos por campos y colocar filas de resumen entre conjuntos de datos o grupos de datos. Por ejemplo, si está agrupando datos por Cliente.IDCliente, puede agregar un registro de resumen cada vez que cambie el grupo.
### **Parámetros**
A continuación se muestran algunos de los parámetros de marcadores inteligentes utilizados para agrupar datos.
#### **group:normal/merge/repeat**
Soportamos tres tipos de grupos entre los que puede elegir.

- **normal** - El valor del campo o campos de agrupación no se repite para los registros correspondientes en la columna; en su lugar se imprimen una vez por grupo de datos.
- **merge** - El mismo comportamiento que para el parámetro normal, excepto que fusiona las celdas en los campos de agrupación para cada conjunto de grupos.
- **repeat** - El valor del campo o campos de agrupación se repite para los registros correspondientes.

Por ejemplo: &=Clientes.IDCliente(grupo:merge)
#### **skip**
Salta un número especificado de filas después de cada grupo.

Por ejemplo, &=Empleados.IDEmpleado(grupo:normal,saltar:1)
#### **subtotalN**
Realiza una operación de resumen para un campo de datos especificado relacionado con un campo de agrupación. La N representa números del 1 al 11 que especifican la función utilizada al calcular los subtotales dentro de una lista de datos. (1=PROMEDIO, 2=CONTAR, 3=CONTARA, 4=MÁXIMO, 5=MÍNIMO,...9=SUMA, etc.) Consulta la referencia de subtotales en la ayuda de Microsoft Excel para más detalles.

El formato realmente se declara como:
subtotalN:Ref donde Ref se refiere a la columna de agrupación.

Por ejemplo,

- &=Productos.Unidades(subtotal9:Productos.IDProducto) especifica la función de resumen sobre el campo **Unidades** con respecto al campo **IDProducto** en la tabla **Productos**.
- &=Tabx.Col3(subtotal9:Tabx.Col1) especifica la función de resumen sobre el campo **Col3** agrupado por **Col1** en la tabla **Tabx**.
- &=Tabla1.ColumnaD(subtotal9:Tabla1.ColumnaA&Tabla1.ColumnaB) especifica la función de resumen sobre el campo **ColumnaD** agrupado por **ColumnaA** y **ColumnaB** en la tabla **Tabla1**.

Este ejemplo muestra algunos de los parámetros de agrupación en acción. Utiliza la base de datos de Microsoft Access Northwind.mdb y extrae datos de la tabla llamada "Detalles del Pedido". Creamos un archivo de diseño llamado SmartMarker_Designer.xls en Microsoft Excel y colocamos marcadores inteligentes en varias celdas de las hojas de cálculo. Los marcadores se procesan para llenar las hojas de cálculo. Los datos se colocan y organizan por un campo de grupo.

El archivo de diseño tiene dos hojas de cálculo. En la primera colocamos marcadores inteligentes con parámetros de agrupación como se muestra en la captura de pantalla a continuación. Se colocan tres marcadores inteligentes (con parámetros de agrupación):
&=[Order Details].OrderID(group:merge,skip:1),
&=[Detalles del pedido].Cantidad(subtotal9:Detalles del pedido.IDPedido), y
&=[Detalles del pedido].PrecioUnitario(subtotal9:Detalles del pedido.IDPedido) se van a A5, B5 y C5 respectivamente.

|**La primera hoja de trabajo en el archivo SmartMarker_Designer.xls, completa con marcadores inteligentes**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
En la segunda hoja de trabajo del archivo de diseñador, colocamos algunos marcadores inteligentes más como se muestra en la figura a continuación. Colocamos los siguientes marcadores inteligentes:
&=[Order Details].OrderID(group:normal),
&=[Order Details].Quantity,
&=[Order Details].UnitPrice,
&=&=B(r)*C(r), y
&=subtotal9:Detalles del pedido.IDPedido en A5, B5, C5, D5 y C6 respectivamente.

|**La segunda hoja de trabajo del archivo SmartMarker_Designer.xls, mostrando marcadores inteligentes mixtos.**|
| :- |
|![todo:image_alt_text](using-smart-markers_6.png)|
Aquí está el código fuente usado en el ejemplo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Si necesita agregar sus propias etiquetas personalizadas a las filas de resumen o si desea concatenar el nombre del campo con una etiqueta, por ejemplo, "Subtotal de pedidos", Aspose.Cells le proporciona atributos de Etiqueta y PosiciónEtiqueta, para que pueda colocar sus etiquetas personalizadas en los Marcadores Inteligentes mientras se concatenan con las filas de Subtotal en datos de agrupación. Consulte el documento sobre Cómo agregar etiquetas personalizadas para concatenar con las filas de subtotal en los Marcadores Inteligentes como referencia.

{{% /alert %}} 
## **Usar tipos anónimos u objetos personalizados**
Aspose.Cells también admite tipos anónimos u objetos personalizados en marcadores inteligentes. El ejemplo que sigue muestra cómo funciona esto. Para importar datos de objetos dinámicos utilizando Marcadores Inteligentes, visite el siguiente artículo:

[Importar desde objeto dinámico como origen de datos](/cells/es/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **Marcadores de imagen**
Aspose.Cells admite marcadores inteligentes de imágenes. Esta sección te muestra cómo insertar imágenes usando marcadores inteligentes.
### **Parámetros de la Imagen**
Parámetros de marcadores inteligentes para gestionar imágenes.

- **Imagen:AjustarACelda** - Ajusta automáticamente la imagen a la altura de la fila y al ancho de la columna de la celda.
- **Imagen:EscalarN** - Escala la altura y el ancho al N por ciento.
- **Imagen:Ancho:NyAltura:N** - Renderiza la imagen de N pulgadas de alto y N pulgadas de ancho. También se pueden especificar posiciones Izquierda y Arriba (en puntos).

Aquí está el código fuente usado en el ejemplo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **Usar objetos anidados**
Aspose.Cells soporta objetos anidados en marcadores inteligentes, los objetos anidados deben ser simples. Utilizamos un archivo de plantilla simple. Consulta la hoja de cálculo de diseño que contiene algunos marcadores inteligentes anidados.

|**La primera hoja de cálculo del archivo SM_NestedObjects.xlsx mostrando marcadores inteligentes anidados.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
El ejemplo que sigue muestra cómo funciona esto.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}

## **Uso de datos JSON**
Aspose.Cells soporta datos json en marcadores inteligentes, los datos json pueden estar anidados jerárquicamente. Por favor, revisa [archivo de plantilla](smartmarker.xlsx), [archivo json](smartmarker.json) y la captura de pantalla del archivo excel generado con el siguiente código.

|**La primera hoja de trabajo del archivo smartmarker.xlsx mostrando marcadores inteligentes.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**La captura de pantalla del archivo excel de salida.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

Datos json de la siguiente manera:
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
El ejemplo que sigue muestra cómo funciona esto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data.cs" >}}

## **Usando una Lista Genérica como Objeto Anidado**
Ahora Aspose.Cells también soporta usar una lista genérica como objeto anidado. Por favor, revisa la captura de pantalla del archivo excel de salida generado con el siguiente código. Como puedes ver en la captura de pantalla, un objeto de Profesor contiene varios objetos de Estudiante anidados.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Usar la propiedad HTML de Marcadores Inteligentes**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **No línea por línea**
El método de procesamiento predeterminado actual es procesar los marcadores inteligentes línea por línea. Pero a veces los marcadores inteligentes de la misma tabla de datos deben procesarse juntos, sin importar 
si están en la misma fila o no, entonces debes especificar un rango con nombre "_CellsSmartMarkers" y especificar WorkbookDesigner.LineByLine como falso antes de llamar al procesamiento.

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **Recibir notificaciones mientras se fusionan datos con Marcadores Inteligentes**
A veces, puede ser necesario recibir notificaciones sobre la referencia de la celda o el Marcador Inteligente particular que se está procesando antes de la finalización. Esto se puede lograr usando la propiedad WorkbookDesigner.CallBack e ISmartMarkerCallBack

## **Temas avanzados**
- [Agregar un Objeto Anónimo o Personalizado en los Marcadores Inteligentes](/cells/es/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Autocompletar Datos de Marcador Inteligente en Otras Hojas de Cálculo si los Datos son muy Grandes](/cells/es/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formateando Marcadores Inteligentes](/cells/es/net/formatting-smart-markers/)
- [Recibir notificaciones mientras se fusionan datos con Marcadores Inteligentes](/cells/es/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Establecer fuente de datos personalizada para WorkbookDesigner](/cells/es/net/set-custom-datasource-for-workbookdesigner/)
- [Mostrar apóstrofo inicial en celdas](/cells/es/net/show-leading-apostrophe-in-cells/)
- [Usar parámetro de fórmula en campo de Marcador Inteligente](/cells/es/net/using-formula-parameter-in-smart-marker-field/)
- [Usar Marcadores de Imagen mientras se agrupan datos en Marcadores Inteligentes](/cells/es/net/using-image-markers-while-grouping-data-in-smart-markers/)


{{< app/cells/assistant language="csharp" >}}
