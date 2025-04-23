---  
title: Validación de datos
type: docs  
weight: 90  
url: /es/nodejs-cpp/data-validation/  
description: Aprende cómo agregar validación de datos a través de la API Aspose.Cells for Node.js via C++.  
keywords: Agregar Validación de Datos Node.js vía C++, Obtener Valor de Validación Node.js vía C++, Agregar Validación de Número Entero Node.js vía C++, Agregar Validación de Lista Node.js vía C++, Agregar Validación de Fecha Node.js vía C++, Agregar Validación de Hora Node.js vía C++, Agregar Validación de Longitud de Texto Node.js vía C++, Agregar Área de Celdas a Validación existente Node.js vía C++, Verificar si la validación en la celda es un menú desplegable Node.js vía C++, Agregar Validación Personalizada Node.js vía C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel ofrece buenas funciones para autofiltrar o validar datos en hojas de cálculo. Aspose.Cells soporta completamente las funciones de validación de datos y autofiltrado de Microsoft Excel. Este artículo explica cómo usar estas funciones en Microsoft Excel y cómo programarlas usando Aspose.Cells for Node.js via C++.  
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

### **Validación de Datos con Aspose.Cells for Node.js via C++**  

La validación de datos es una función poderosa para validar la información ingresada en las hojas de cálculo. Con la validación de datos, los desarrolladores pueden proporcionar a los usuarios una lista de opciones, restringir las entradas de datos a un tipo o tamaño específico, etc.  
En Aspose.Cells for Node.js via C++, cada clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) tiene un método [**getValidations()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getValidations--) que representa una colección de objetos [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation). Para configurar la validación, establece algunas propiedades de la clase [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) como sigue:  

- Tipo – representa el tipo de validación, que puede especificarse usando uno de los valores predefinidos en la enumeración [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype).  
- Operador – representa el operador que se usará en la validación, que puede especificarse usando uno de los valores predefinidos en la enumeración [**OperatorType**](https://reference.aspose.com/cells/nodejs-cpp/operatortype).  
- Fórmula1 – representa el valor o expresión asociado con la primera parte de la validación de datos.  
- Fórmula2 – representa el valor o expresión asociado con la segunda parte de la validación de datos.  

Cuando las propiedades del objeto [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) hayan sido configuradas, los desarrolladores pueden usar la estructura [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) para almacenar información sobre el rango de celdas que será validado usando la validación creada.  

#### **Tipos de validación de datos**  

La enumeración [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) tiene los siguientes miembros:  

|**Nombre del miembro**|**Descripción**|  
| :- | :- |  
|AnyValue|Denota un valor de cualquier tipo.|  
|WholeNumber|Denota tipo de validación para números enteros.|  
|Decimal|Denota tipo de validación para números decimales.|  
|List|Denota tipo de validación para lista desplegable.|  
|Date|Denota tipo de validación para fechas.|  
|Time|Denota tipo de validación para tiempo.|  
|TextLength|Denota tipo de validación para longitud del texto.|  
|Custom|Denota tipo de validación personalizado.|  

##### **Validación de datos de números enteros**  

Con este tipo de validación, los usuarios solo pueden ingresar números enteros dentro de un rango específico en las celdas validadas. Los ejemplos de código que siguen muestran cómo implementar el tipo de validación WholeNumber y crea la misma validación de datos usando Aspose.Cells for Node.js via C++ que creamos con Microsoft Excel arriba.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-WholeNumber.js" >}}


##### **Validación de datos de lista**  

Este tipo de validación permite al usuario ingresar valores de una lista desplegable. Proporciona una lista: una serie de filas que contienen datos. En el ejemplo, se agrega una segunda hoja de cálculo para contener la fuente de la lista. Los usuarios solo pueden seleccionar valores de la lista. El área de validación es el rango de celdas A1:A5 en la primera hoja de cálculo.  

Es importante aquí que configures la propiedad [**Validation.setInCellDropDown(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#setInCellDropDown-boolean-) a **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ListData.js" >}}


##### **Validación de datos de fechas**  

Con este tipo de validación, los usuarios ingresan valores de fecha dentro de un rango especificado, o que cumplen criterios específicos, en las celdas validadas. En el ejemplo, el usuario está restringido a ingresar fechas entre 1970 y 1999. Aquí, el área de validación es la celda B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DateData.js" >}}

##### **Validación de datos de hora**  

Con este tipo de validación, los usuarios pueden ingresar horas dentro de un rango especificado, o que cumplan con ciertos criterios, en las celdas validadas. En el ejemplo, al usuario se le restringe ingresar horas entre las 09:00 y las 11:30 AM. Aquí, el área de validación es la celda B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TimeData.js" >}}


##### **Validación de Datos de Longitud de Texto**  

Con este tipo de validación, los usuarios pueden ingresar valores de texto de una longitud específica en las celdas validadas. En el ejemplo, al usuario se le restringe ingresar valores de cadena con no más de 5 caracteres. El área de validación es la celda B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TextLengthData.js" >}}


### **Reglas de Validación de Datos**  

Cuando se implementan validaciones de datos, se puede verificar la validación asignando diferentes valores en las celdas. [**Cell.getValidationValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) se puede usar para obtener el resultado de la validación. El siguiente ejemplo demuestra esta función con diferentes valores. El archivo de muestra se puede descargar desde el siguiente enlace para pruebas:  

[sampleDataValidationRules.xlsx](77496339.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DataValidationRules.js" >}}


## **Verificar si la validación en la celda es de lista desplegable**  

Como hemos visto, hay muchos tipos de validaciones que se pueden implementar dentro de una celda. Si quieres verificar si la validación es un menú desplegable o no, se puede usar el método [**Validation.getInCellDropDown()**](https://reference.aspose.com/cells/nodejs-cpp/validation/#getInCellDropDown--) para probar esto. El siguiente código de ejemplo demuestra el uso de esta propiedad. Un archivo de muestra para pruebas puede descargarse desde el siguiente enlace:  

[sampleValidation.xlsx](79527947.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-CheckValidationIsDropDown.js" >}}


## **Agregar CellArea a la validación existente**  

Podría haber casos en los que quieras añadir [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) a [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) existente. Cuando agregas [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) usando [**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-), Aspose.Cells revisa todas las áreas existentes para ver si la nueva área ya existe. Si el archivo tiene una gran cantidad de validaciones, esto afecta el rendimiento. Para superar esto, la API proporciona el método [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-). El parámetro *checkIntersection* indica si se debe verificar la intersección de un área dada con las áreas de validación existentes. Configurarlo a **false** deshabilitará la comprobación de otras áreas. El parámetro *checkEdge* indica si se deben verificar las áreas aplicadas. Si el área nueva se vuelve el área superior izquierda, se reconstruyen las configuraciones internas. Si estás seguro de que el área nueva no es la esquina superior izquierda, puedes establecer este parámetro a **false**.  

El siguiente fragmento de código demuestra el uso del método [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-) para agregar un nuevo [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) a los [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) existentes.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-AddCellAreaToExistingValidation.js" >}}

Se adjuntan los archivos de Excel de origen y salida para referencia.  

[Archivo de origen](96928093.xlsx)  

[Archivo de Salida](96928220.xlsx)  

## **Temas avanzados**  
- [Obtener validación de celda en archivos ODS](/cells/es/nodejs-cpp/get-cell-validation-in-ods-files/)  
- [Obtener Validación Aplicada en una Celda](/cells/es/nodejs-cpp/get-validation-applied-on-a-cell/)  
- [Verificar que el Valor de la Celda Satisface las Reglas de Validación de Datos](/cells/es/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/)  

