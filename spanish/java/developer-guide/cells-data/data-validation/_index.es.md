---
title: Validación de datos
type: docs
weight: 70
url: /es/java/data-validation/
---

{{% alert color="primary" %}} 

Microsoft Excel proporciona algunas buenas características para autofiltrar o validar datos en la hoja de cálculo.

La [validación de datos](/cells/es/java/data-validation/) es la capacidad de establecer reglas relacionadas con los datos introducidos en una hoja de cálculo. Por ejemplo, usar validación para asegurarse de que una columna etiquetada como FECHA contiene solo fechas, o que otra columna contiene solo números. Incluso podría asegurar que una columna etiquetada como FECHA contiene solo fechas dentro de un rango específico. Con la validación de datos, puedes controlar lo que se introduce en las celdas de la hoja de cálculo. Aspose.Cells soporta completamente la validación de datos y las funciones de autofiltrado de Microsoft Excel. Este artículo explica cómo usar las funciones en Microsoft Excel y cómo codificarlas usando Aspose.Cells.

{{% /alert %}} 
## **Tipos de Validación de Datos y Ejecución**
Microsoft Excel admite varios tipos diferentes de validación de datos. Cada tipo se usa para controlar qué tipo de datos se ingresa en una celda o rango de celdas. A continuación, se muestran fragmentos de código que ilustran cómo validar que:

- [Los números son enteros](/cells/es/java/data-validation/), es decir, que no tienen una parte decimal.
- [Los números decimales siguen la estructura correcta](/cells/es/java/data-validation/). El ejemplo de código define que un rango de celdas debe tener dos espacios decimales.
- [Los valores están restringidos a una lista de valores](/cells/es/java/data-validation/). La validación de lista define una lista separada de valores que se pueden aplicar a una celda o rango de celdas.
- [Las fechas están dentro de un rango específico](/cells/es/java/data-validation/).
- [El tiempo está dentro de un rango específico](/cells/es/java/data-validation/).
- [Un texto está dentro de una longitud de caracteres dada](/cells/es/java/data-validation/).
### **Validación de datos con Microsoft Excel**
Para crear validaciones usando Microsoft Excel:

1. En una hoja de cálculo, seleccione las celdas a las que desea aplicar la validación.
1. En el menú **Datos**, selecciona **Validación**.
   Se mostrará el cuadro de diálogo de validación.
1. Haz clic en la pestaña **Configuración** e introduce las configuraciones como se muestra a continuación. 

   **Configuración de validación de datos** 

![todo:image_alt_text](data-validation_1.png)
### **Validación de datos con Aspose.Cells**
La validación de datos es una función poderosa para validar la información ingresada en las hojas de cálculo. Con la validación de datos, los desarrolladores pueden proporcionar a los usuarios una lista de opciones, restringir las entradas de datos a un tipo o tamaño específico, etc.
En Aspose.Cells, cada clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) tiene un objeto [Validations](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations) que representa una colección de objetos [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). Para configurar la validación, establezca algunas de las propiedades de la clase [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation):

- [Type](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): representa el tipo de validación, que puede especificarse utilizando uno de los valores predefinidos en la enumeración [ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType).
- [Operator](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): representa el operador que se utilizará en la validación, que puede especificarse utilizando uno de los valores predefinidos en la enumeración [OperatorType](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType).
- [Formula1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): representa el valor o expresión asociada con la primera parte de la validación de datos.
- [Formula2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): representa el valor o expresión asociada con la segunda parte de la validación de datos.

Cuando se han configurado las propiedades del objeto [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation), los desarrolladores pueden utilizar la estructura [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) para almacenar información sobre el rango de celdas que se validarán utilizando la validación creada.
#### **Tipos de validación de datos**
La validación de datos le permite establecer reglas de negocio en cada celda para que las entradas incorrectas resulten en mensajes de error. Las reglas de negocio son las políticas y procedimientos que rigen cómo opera un negocio. Aspose.Cells admite todos los tipos importantes de validación de datos.

La enumeración [ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType) tiene los siguientes miembros:

|**Nombre del miembro**|**Descripción**|
| :- | :- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|Denota un valor de cualquier tipo.
|[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|Denota el tipo de validación para números enteros.
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Denota el tipo de validación para números decimales.
|[LIST](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Denota el tipo de validación para lista desplegable.
|[DATE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Denota el tipo de validación para fechas.
|[TIME](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Denota el tipo de validación para hora.
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|Denota el tipo de validación para la longitud del texto.
|[CUSTOM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Denota tipo de validación personalizada.|
#### **Ejemplo de programación: Validación de datos de números enteros**
Con este tipo de validación, los usuarios solo pueden ingresar números enteros dentro de un rango especificado en las celdas validadas. Los ejemplos de código que siguen muestran cómo implementar el tipo de validación [NÚMERO_ENTERO](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER). El ejemplo crea la misma validación de datos usando Aspose.Cells que creamos usando Microsoft Excel anteriormente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Ejemplo de programación: Validación de datos decimales**
Con este tipo de validación, el usuario puede ingresar números decimales en las celdas validadas. En el ejemplo, el usuario está restringido a ingresar solo valores decimales y el área de validación es A1:A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Ejemplo de programación: Validación de datos de lista**
Este tipo de validación permite al usuario ingresar valores de una lista desplegable. Proporciona una lista: una serie de filas que contienen datos. Los usuarios solo pueden seleccionar valores de la lista. El área de validación es el rango de celdas A1:A5 en la primera hoja de cálculo.

Es importante aquí que establezca la propiedad [Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) en **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Ejemplo de programación: Validación de datos de fecha**
Con este tipo de validación, los usuarios ingresan valores de fecha dentro de un rango especificado, o que cumplen criterios específicos, en las celdas validadas. En el ejemplo, el usuario está restringido a ingresar fechas entre 1970 y 1999. Aquí, el área de validación es la celda B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Ejemplos de programación: Validación de datos de tiempo**
Con este tipo de validación, los usuarios pueden ingresar horas dentro de un rango especificado, o que cumplan con ciertos criterios, en las celdas validadas. En el ejemplo, al usuario se le restringe ingresar horas entre las 09:00 y las 11:30 AM. Aquí, el área de validación es la celda B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Ejemplos de programación: Validación de datos de longitud de texto**
Con este tipo de validación, los usuarios pueden ingresar valores de texto de una longitud específica en las celdas validadas. En el ejemplo, al usuario se le restringe ingresar valores de cadena con no más de 5 caracteres. El área de validación es la celda B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Reglas de Validación de Datos**
Cuando se implementan validaciones de datos, la validación se puede verificar asignando diferentes valores a las celdas. [Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) se puede utilizar para obtener el resultado de la validación. El siguiente ejemplo demuestra esta función con diferentes valores. El archivo de ejemplo se puede descargar desde el siguiente enlace para probarlo:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Código de Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Verifique si la validación en una celda es desplegable**
Como hemos visto, hay muchos tipos de validaciones que se pueden implementar dentro de una celda. Si desea verificar si la validación es desplegable o no, se puede utilizar la propiedad [Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) para probar esto. El siguiente código de muestra demuestra el uso de esta propiedad. El archivo de ejemplo para probar se puede descargar desde el siguiente enlace:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **Agregar CellArea a la validación existente**
Puede haber casos en los que desee agregar [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) a la Validación existente. Cuando se agrega [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) usando [Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)), Aspose.Cells verifica todas las áreas existentes para ver si la nueva área ya existe. Si el archivo tiene un gran número de validaciones, esto afecta el rendimiento. Para solucionar esto, la API proporciona el método [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)). El parámetro *checkIntersection* indica si se debe verificar la intersección de un área dada con las áreas de validación existentes. Establecerlo en **false** deshabilitará la verificación de otras áreas. El parámetro *checkEdge* indica si se deben comprobar las áreas aplicadas. Si la nueva área se convierte en la parte superior izquierda, se reconstruyen las configuraciones internas. Si está seguro de que la nueva área no es la parte superior izquierda, puede establecer este parámetro en **false**.

El siguiente fragmento de código demuestra el uso del método [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) para agregar una nueva [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) a la Validación existente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

Se adjuntan los archivos de Excel de origen y salida para referencia.

[Archivo de origen](PivotTableHideAndSortSample.xlsx)

[Archivo de Salida](ValidationsSample_out.xlsx)


## **Temas avanzados**
- [Obtener validación de celda en archivos ODS](/cells/es/java/get-cell-validation-in-ods-files/)
- [Obtener Validación Aplicada en una Celda](/cells/es/java/get-validation-applied-on-a-cell/)
- [Verificar que el Valor de la Celda Satisface las Reglas de Validación de Datos](/cells/es/java/verify-that-cell-value-satisfies-data-validation-rules/)
