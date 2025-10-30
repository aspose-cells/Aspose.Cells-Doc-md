---
title: Validación de datos
type: docs
weight: 90
url: /es/python-net/data-validation/
description: Aprende cómo agregar validación de datos a través de la API de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Agregar Validación de Datos de Python, Obtener Valor de Validación de Python, Agregar Validación de Datos de Número Entero de Python, Agregar Validación de Datos de Lista de Python, Agregar Validación de Datos de Fecha de Python, Agregar Validación de Datos de Hora de Python, Agregar Validación de Longitud de Texto de Python, Agregar CellArea a la Validación existente de Python, Verificar si la validación en la celda es desplegable, Agregar Validación Personalizada  
---

{{% alert color="primary" %}}

Microsoft Excel proporciona algunas buenas funciones para filtrar automáticamente o validar los datos de la hoja de cálculo. Aspose.Cells for Python via .NET admite completamente la validación de datos y las funciones de AutoFilter de Microsoft Excel. Este artículo explica cómo utilizar las funciones en Microsoft Excel y cómo programarlas utilizando Aspose.Cells for for Python via .NET.

{{% /alert %}}

## **Tipos de Validación de Datos y Ejecución**

La validación de datos es la capacidad de establecer reglas relacionadas con los datos ingresados en una hoja de cálculo. Por ejemplo, use la validación para asegurarse de que una columna etiquetada como FECHA contenga solo fechas, o que otra columna contenga solo números. Incluso puede asegurarse de que una columna etiquetada como FECHA contenga solo fechas dentro de un cierto rango. Con la validación de datos, puede controlar lo que se ingresa en las celdas de la hoja de cálculo.

Microsoft Excel admite varios tipos diferentes de validación de datos. Cada tipo se usa para controlar qué tipo de datos se ingresa en una celda o rango de celdas. A continuación, se muestran fragmentos de código que ilustran cómo validar que:

- Los números son enteros, es decir, que no tienen parte decimal.
- Los números decimales siguen la estructura correcta. El ejemplo de código define que un rango de celdas debe tener dos espacios decimales.
- Los valores están restringidos a una lista de valores. La validación de lista define una lista separada de valores que se pueden aplicar a una celda o rango de celdas.
- Las fechas se encuentran dentro de un rango específico.
- Una hora está dentro de un rango específico.
- Un texto está dentro de una longitud de caracteres dada.

### **Validación de datos con Microsoft Excel**

Para crear validaciones usando Microsoft Excel:

1. En una hoja de cálculo, seleccione las celdas a las que desea aplicar la validación.
1. Desde el menú **Datos**, seleccione **Validación**. Se mostrará el diálogo de validación.
1. Haga clic en la pestaña **Configuración** e ingrese la configuración.

### **Validación de datos con la biblioteca Excel de Python de Aspose.Cells**

La validación de datos es una función poderosa para validar la información ingresada en las hojas de cálculo. Con la validación de datos, los desarrolladores pueden proporcionar a los usuarios una lista de opciones, restringir las entradas de datos a un tipo o tamaño específico, etc.
En Aspose.Cells para Python via .NET, cada clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tiene una propiedad [**validations**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/validations/) que representa una colección de objetos [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation). Para configurar la validación, establezca algunas de las propiedades de la clase [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) de la siguiente manera:

- type: representa el tipo de validación, que puede ser especificado utilizando uno de los valores predefinidos en la enumeración [**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype).
- Operator: representa el operador que se utilizará en la validación, que puede ser especificado utilizando uno de los valores predefinidos en la enumeración [**OperatorType**](https://reference.aspose.com/cells/python-net/aspose.cells/operatortype).
- formula1: representa el valor o la expresión asociada con la primera parte de la validación de datos.
- formula2: representa el valor o la expresión asociada con la segunda parte de la validación de datos.

Cuando las propiedades del objeto [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) hayan sido configuradas, los desarrolladores pueden utilizar la estructura [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) para almacenar información sobre el rango de celdas que se validarán utilizando la validación creada.

#### **Tipos de validación de datos**

La enumeración [**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) tiene los siguientes miembros:

|**Nombre del miembro**|**Descripción**|
| :- | :- |
|ANY_VALUE|Denota un valor de cualquier tipo.|
|WHOLE_NUMBER|Denota el tipo de validación para números enteros.|
|DECIMAL|Denota el tipo de validación para números decimales.|
|LISTA|Denota el tipo de validación para lista desplegable.|
|DATE|Denota el tipo de validación para fechas.|
|TIEMPO|Denota el tipo de validación para hora.|
|TEXT_LENGTH|Denota el tipo de validación para la longitud del texto.|
|PERSONALIZADO|Denota el tipo de validación personalizada.|

##### **Validación de datos de números enteros**

Con este tipo de validación, los usuarios solo pueden ingresar números enteros dentro de un rango especificado en las celdas validadas. Los ejemplos de código que siguen muestran cómo implementar el tipo de validación de números enteros. El ejemplo crea la misma validación de datos utilizando Aspose.Cells para Python via .NET que creamos utilizando Microsoft Excel anteriormente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-WholeNumberDataValidation-1.py" >}}

##### **Validación de datos de lista**

Este tipo de validación permite al usuario ingresar valores de una lista desplegable. Proporciona una lista: una serie de filas que contienen datos. En el ejemplo, se agrega una segunda hoja de cálculo para contener la fuente de la lista. Los usuarios solo pueden seleccionar valores de la lista. El área de validación es el rango de celdas A1:A5 en la primera hoja de cálculo.

Es importante aquí que establezca la propiedad [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) como **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-ListDataValidation-1.py" >}}

##### **Validación de datos de fechas**

Con este tipo de validación, los usuarios ingresan valores de fecha dentro de un rango especificado, o que cumplen criterios específicos, en las celdas validadas. En el ejemplo, el usuario está restringido a ingresar fechas entre 1970 y 1999. Aquí, el área de validación es la celda B1.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DateDataValidation-1.py" >}}

##### **Validación de datos de hora**

Con este tipo de validación, los usuarios pueden ingresar horas dentro de un rango especificado, o que cumplan con ciertos criterios, en las celdas validadas. En el ejemplo, al usuario se le restringe ingresar horas entre las 09:00 y las 11:30 AM. Aquí, el área de validación es la celda B1.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TimeDataValidation-1.py" >}}

##### **Validación de Datos de Longitud de Texto**

Con este tipo de validación, los usuarios pueden ingresar valores de texto de una longitud específica en las celdas validadas. En el ejemplo, al usuario se le restringe ingresar valores de cadena con no más de 5 caracteres. El área de validación es la celda B1.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TextLengthDataValidation-1.py" >}}

### **Reglas de Validación de Datos**

Cuando se implementan validaciones de datos, entonces la validación se puede verificar asignando diferentes valores en las celdas. [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) se puede utilizar para obtener el resultado de la validación. El siguiente ejemplo demuestra esta característica con valores diferentes. El archivo de ejemplo se puede descargar desde el siguiente enlace para pruebas:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

## **Verificar si la validación en la celda es de lista desplegable**

Como hemos visto, existen muchos tipos de validaciones que se pueden implementar dentro de una celda. Si quieres verificar si la validación es de lista desplegable o no, se puede utilizar la propiedad [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) para probarlo. El siguiente código de ejemplo muestra el uso de esta propiedad. Se puede descargar un archivo de ejemplo para pruebas desde el siguiente enlace:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-CheckIfValidationInCellDropDown-1.py" >}}

## **Agregar CellArea a la validación existente**

Puede haber casos en los que desees agregar [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) a la [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) existente. Cuando agregas [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) usando [**Validation.add_area(cell_area)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea), Aspose.Cells verifica todas las áreas existentes para ver si la nueva área ya está incluida. Si el archivo tiene un gran número de validaciones, esto afecta el rendimiento. Para superar esto, la API proporciona el método [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool). El parámetro *checkIntersection* indica si se debe verificar la intersección de una determinada área con áreas de validación existentes. Establecerlo en **falso** deshabilitará la verificación de otras áreas. El parámetro *checkEdge* indica si se deben verificar las áreas aplicadas. Si la nueva área se convierte en el área superior izquierda, se reconstruyen las configuraciones internas. Si estás seguro de que la nueva área no es el área superior izquierda, puedes establecer este parámetro en **falso**.

El siguiente fragmento de código muestra el uso del método [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool) para agregar nuevas [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) a las [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) existentes.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AddValidationArea-1.py" >}}

Se adjuntan los archivos de Excel de origen y salida para referencia.

[Archivo de origen](96928093.xlsx)

[Archivo de Salida](96928220.xlsx)


## **Temas avanzados**
- [Obtener validación de celda en archivos ODS](/cells/es/python-net/get-cell-validation-in-ods-files/)
- [Obtener Validación Aplicada en una Celda](/cells/es/python-net/get-validation-applied-on-a-cell/)
- [Verificar que el Valor de la Celda Satisface las Reglas de Validación de Datos](/cells/es/python-net/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="python-net" >}}
