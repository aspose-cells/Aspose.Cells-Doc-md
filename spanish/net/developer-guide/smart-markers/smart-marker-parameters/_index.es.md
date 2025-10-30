---
title: Parámetros de Smart Marker
type: docs
weight: 30
url: /es/net/smart-marker-parameters/
---

## **Hoja de cálculo de diseño y Marcadores inteligentes**
Las hojas de cálculo de diseño son archivos Excel estándar que contienen formato visual, fórmulas y marcadores inteligentes. Pueden contener marcadores inteligentes que hacen referencia a una o más fuentes de datos, como información de un proyecto e información de contactos relacionados. Los marcadores inteligentes se escriben en las celdas donde desea la información.

Todos los marcadores inteligentes comienzan con &=. Un ejemplo de marcador de datos es &=Party.FullName. Si el marcador de datos da como resultado más de un elemento, por ejemplo, una fila completa, entonces las filas siguientes se mueven automáticamente para dar cabida a la nueva información. De esta manera, los subtotales y totales pueden colocarse en la fila inmediatamente después del marcador de datos para realizar cálculos basados en la información insertada. Para realizar cálculos en las filas insertadas, utilice **formulas dinámicas**.

Los marcadores inteligentes consisten en las partes de **fuente de datos** y **nombre del campo** para la mayoría de la información. También se puede enviar información especial con variables y matrices de variables. Las variables siempre llenan solo una celda, mientras que las matrices de variables pueden llenar varias. Utilice solo un marcador de datos por celda. Los marcadores inteligentes no utilizados se eliminan.

El marcador inteligente también puede contener parámetros. Los parámetros le permiten modificar la disposición de la información. Se agregan al final del marcador inteligente entre paréntesis como una lista separada por comas.

## **Opciones de Marcador Inteligente**

```csharp
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==DynamicFormula 
&=&=RepeatDynamicFormula
```
## **Parámetros de Smart Marker**
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

## **Fórmulas dinámicas**
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

## **Cómo Usar Fórmulas Dinámicas y Variables en SmartMarkers**
A veces, necesitas usar fórmulas dinámicas y variables en SmartMarkers. Para fórmulas dinámicas, por favor, añade el carácter especial (~) como separador. Aspose.Cells permite usar fórmulas dinámicas y variables en SmartMarkers. Revisa [archivo de plantilla](template.xlsx), [archivo JSON](employees-data.json) y la captura de pantalla del archivo Excel generado con el siguiente código.

|**La primera hoja del archivo template.xlsx mostrando variables.**|
| :- |
|![todo:image_alt_text](template_variables.png)|

|**La segunda hoja del archivo template.xlsx mostrando smart markers.**|
| :- |
|![todo:image_alt_text](template_data.png)|

|**La captura de pantalla del archivo excel de salida.**|
| :- |
|![todo:image_alt_text](template_result.png)|

Datos json de la siguiente manera:
```json data
{
  "RootData": {
    "Directors": [
      {
        "FirstName": "director first 1",
        "id": "director id 1",
        "LastName": "director last 1",
        "MiddleName": "director middle 1",
        "Reportees": [
          {
            "City": "aaa city",
            "Department": "aaa department",
            "FirstName": "first aaa",
            "GST": "Yes",
            "id": "aaa",
            "ITR": "No",
            "LastName": "last aaa",
            "MiddleName": "middle aaa"
          },
          {
            "City": "bbb city",
            "Department": "bbb department",
            "FirstName": "first bbb",
            "GST": "Yes",
            "id": "bbb",
            "ITR": "Yes",
            "LastName": "last bbb",
            "MiddleName": "middle bbb"
          },
          {
            "City": "ccc city",
            "Department": "ccc department",
            "FirstName": "first ccc",
            "GST": "No",
            "id": "ccc",
            "ITR": "No",
            "LastName": "last ccc",
            "MiddleName": "middle ccc"
          },
          {
            "City": "ddd city",
            "Department": "ddd department",
            "FirstName": "first ddd",
            "GST": "No",
            "id": "ddd",
            "ITR": "No",
            "LastName": "last ddd",
            "MiddleName": "middle ddd"
          },
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "No",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          }
        ]
      },
      {
        "FirstName": "director first 2",
        "id": "director id 2",
        "LastName": "director last 2",
        "MiddleName": "director middle 2",
        "Reportees": [
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "Yes",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          },
          {
            "City": "fff city",
            "Department": "fff department",
            "FirstName": "first fff",
            "GST": "No",
            "id": "fff",
            "ITR": "No",
            "LastName": "last fff",
            "MiddleName": "middle fff"
          }
        ]
      }
    ],
    "DOB": "2025-02-28",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111",
	"CtcPerEmployee": 100000,
	"CountOfEmployees": 132
  }
}
```
El ejemplo que sigue muestra cómo funciona esto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-DynamicFormula-And-Variables.cs" >}}
