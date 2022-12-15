---
title: Validación de datos
type: docs
weight: 70
url: /es/java/data-validation/
---
{{% alert color="primary" %}} 

Microsoft Excel proporciona algunas buenas funciones para filtrar automáticamente o validar datos de hojas de cálculo.

[Validación de datos](/cells/es/java/data-validation/) es la capacidad de establecer reglas relacionadas con los datos ingresados en una hoja de trabajo. Por ejemplo, utilice la validación para asegurarse de que una columna etiquetada como FECHA contenga solo fechas o que otra columna contenga solo números. Incluso podría asegurarse de que una columna etiquetada como FECHA contenga solo fechas dentro de un cierto rango. Con la validación de datos, puede controlar lo que se ingresa en las celdas de la hoja de trabajo. Aspose.Cells es totalmente compatible con las funciones de autofiltro y validación de datos de Microsoft de Excel. Este artículo explica cómo usar las funciones en Microsoft Excel y cómo codificarlas usando Aspose.Cells.

{{% /alert %}} 
## **Tipos de validación de datos y ejecución**
Microsoft Excel admite varios tipos diferentes de validación de datos. Cada tipo se usa para controlar qué tipo de datos se ingresan en una celda o rango de celdas. A continuación, los fragmentos de código ilustran cómo validar eso:

- [los numeros son enteros](/cells/es/java/data-validation/)es decir, que no tienen parte decimal.
- [Los números decimales siguen la estructura correcta](/cells/es/java/data-validation/). El ejemplo de código define que un rango de celdas debe tener dos espacios decimales.
- [Los valores están restringidos a una lista de valores.](/cells/es/java/data-validation/). La validación de lista define una lista separada de valores que se pueden aplicar a una celda o rango de celdas.
- [Las fechas caen dentro de un rango específico](/cells/es/java/data-validation/).
- [El tiempo está dentro de un rango específico](/cells/es/java/data-validation/).
- [Un texto está dentro de una longitud de carácter dada](/cells/es/java/data-validation/).
### **Validación de datos con Microsoft Excel**
Para crear validaciones usando Microsoft Excel:

1. En una hoja de trabajo, seleccione las celdas a las que desea aplicar la validación.
1. Desde el**Datos**menú, seleccione**Validación**.
 Se muestra el cuadro de diálogo de validación.
1. Haga clic en el**Ajustes**e ingrese la configuración como se muestra a continuación.

   **Configuración de validación de datos** 

![todo:imagen_alternativa_texto](data-validation_1.png)
### **Validación de datos con Aspose.Cells**
La validación de datos es una característica poderosa para validar la información ingresada en las hojas de trabajo. Con la validación de datos, los desarrolladores pueden proporcionar a los usuarios una lista de opciones, restringir las entradas de datos a un tipo o tamaño específico, etc.
 En Aspose.Cells, cada[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)la clase tiene un[Validaciones](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)objeto que representa una colección de[Validación](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)objetos. Para configurar la validación, configure algunos de los[Validación](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)propiedades de la clase:

- [Escribe](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): representa el tipo de validación, que se puede especificar utilizando uno de los valores predefinidos en el[Tipo de validación](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)enumeración.
- [Operador](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): representa el operador que se utilizará en la validación, que se puede especificar utilizando uno de los valores predefinidos en el[Tipo de operador](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)enumeración.
- [Fórmula 1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): representa el valor o expresión asociada a la primera parte de la validación de datos.
- [Fórmula2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): representa el valor o expresión asociada a la segunda parte de la validación de datos.

Cuando el[Validación](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)las propiedades del objeto han sido configuradas, los desarrolladores pueden usar el[área de celda](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)estructura para almacenar información sobre el rango de celdas que se validará utilizando la validación creada.
#### **Tipos de validación de datos**
La validación de datos le permite crear reglas comerciales en cada celda para que las entradas incorrectas generen mensajes de error. Las reglas comerciales son las políticas y los procedimientos que rigen el funcionamiento de una empresa. Aspose.Cells admite todos los tipos importantes de validación de datos.

los[Tipo de validación](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)enumeración tiene los siguientes miembros:

|**Nombre de miembro**|**Descripción**|
|:- |:- |
|[ALGÚN VALOR](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|Denota un valor de cualquier tipo.|
|[NÚMERO ENTERO](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|Indica el tipo de validación para números enteros.|
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Indica el tipo de validación para números decimales.|
|[LISTA](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Indica el tipo de validación para la lista desplegable.|
|[FECHA](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Indica el tipo de validación para las fechas.|
|[TIEMPO](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Indica el tipo de validación para Hora.|
|[TEXTO_LONGITUD](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|Indica el tipo de validación para la longitud del texto.|
|[DISFRAZ](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Indica un tipo de validación personalizado.|
#### **Ejemplo de programación: Validación de datos de números enteros**
Con este tipo de validación, los usuarios pueden ingresar solo números enteros dentro de un rango específico en las celdas validadas. Los ejemplos de código que siguen muestran cómo implementar el[NÚMERO ENTERO](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)tipo de validación. El ejemplo crea la misma validación de datos usando Aspose.Cells que creamos usando Microsoft Excel arriba.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Ejemplo de programación: validación de datos decimales**
Con este tipo de validación, el usuario puede ingresar números decimales en las celdas validadas. En el ejemplo, el usuario está restringido a ingresar solo el valor decimal y el área de validación es A1: A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Ejemplo de programación: Validación de datos de lista**
Este tipo de validación permite al usuario ingresar valores de una lista desplegable. Proporciona una lista: una serie de filas que contienen datos. Los usuarios solo pueden seleccionar valores de la lista. El área de validación es el rango de celdas A1:A5 en la primera hoja de cálculo.

Aquí es importante que establezca el[Validación.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) propiedad a**verdadero**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Ejemplo de programación: Validación de datos de fecha**
Con este tipo de validación, los usuarios ingresan valores de fecha dentro de un rango específico, o que cumplen criterios específicos, en las celdas validadas. En el ejemplo, el usuario está restringido a ingresar fechas entre 1970 y 1999. Aquí, el área de validación es la celda B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Ejemplos de programación: Validación de datos de tiempo**
Con este tipo de validación, los usuarios pueden ingresar tiempos dentro de un rango específico, o que cumplan con algunos criterios, en las celdas validadas. En el ejemplo, el usuario está restringido a ingresar horas entre las 09:00 y las 11:30 a. m. Aquí, el área de validación es la celda B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Ejemplos de programación: Validación de datos de longitud de texto**
Con este tipo de validación, los usuarios pueden ingresar valores de texto de una longitud específica en las celdas validadas. En el ejemplo, el usuario está restringido a ingresar valores de cadena con no más de 5 caracteres. El área de validación es la celda B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Reglas de validación de datos**
Cuando se implementan validaciones de datos, se puede verificar la validación asignando diferentes valores en las celdas.[Cell.ObtenerValidaciónValor()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) se puede utilizar para obtener el resultado de la validación. El siguiente ejemplo demuestra esta característica con diferentes valores. El archivo de muestra se puede descargar desde el siguiente enlace para realizar pruebas:

[Reglas de validación de datos de muestra.xlsx](77987849.xlsx)

**Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Comprobar si la validación en una celda es desplegable**
 Como hemos visto, hay muchos tipos de validaciones que se pueden implementar dentro de una celda. Si desea verificar si la validación es desplegable o no,[Validación.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) propiedad se puede utilizar para probar esto. El siguiente código de ejemplo demuestra el uso de esta propiedad. El archivo de muestra para la prueba se puede descargar desde el siguiente enlace:

[ejemploDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **Agregar CellArea a la validación existente**
Puede haber casos en los que desee agregar[área de celda](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)a existente[Validación](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). cuando agregas[área de celda](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)usando[Validación.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)), Aspose.Cells comprueba todas las áreas existentes para ver si la nueva área ya existe. Si el archivo tiene una gran cantidad de validaciones, esto afecta el rendimiento. Para superar esto, el API proporciona la[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) método. los*chequeIntersección*El parámetro indica si se debe verificar la intersección de un área dada con áreas de validación existentes. Configurándolo en**falso**deshabilitará la verificación de otras áreas. los*comprobarBorde*El parámetro indica si se deben verificar las áreas aplicadas. Si la nueva área se convierte en el área superior izquierda, se reconstruyen las configuraciones internas. Si está seguro de que la nueva área no es el área superior izquierda, puede configurar este parámetro como**falso**.

El siguiente fragmento de código demuestra el uso de la[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) método para agregar nuevos[área de celda](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)a existente[Validación](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

Los archivos de Excel de origen y salida se adjuntan como referencia.

[Archivo fuente](PivotTableHideAndSortSample.xlsx)

[Archivo de salida](ValidationsSample_out.xlsx)


## **Temas avanzados**
- [Obtenga la validación Cell en archivos ODS](/cells/es/java/get-cell-validation-in-ods-files/)
- [Obtenga la validación aplicada en un Cell](/cells/es/java/get-validation-applied-on-a-cell/)
- [Verifique que el valor Cell cumpla con las reglas de validación de datos](/cells/es/java/verify-that-cell-value-satisfies-data-validation-rules/)
