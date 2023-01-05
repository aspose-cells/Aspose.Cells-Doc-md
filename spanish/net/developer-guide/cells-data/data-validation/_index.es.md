---
title: Validación de datos
type: docs
weight: 90
url: /es/net/data-validation/
---
{{% alert color="primary" %}}

Microsoft Excel proporciona algunas buenas características para filtrar automáticamente o validar datos de la hoja de cálculo. Este artículo explica cómo usar las funciones en Microsoft Excel y cómo codificarlas usando Aspose.Cells.

{{% /alert %}}

## **Tipos de validación de datos y ejecución**

La validación de datos es la capacidad de establecer reglas relacionadas con los datos ingresados en una hoja de trabajo. Por ejemplo, utilice la validación para asegurarse de que una columna etiquetada como FECHA contenga solo fechas o que otra columna contenga solo números. Incluso podría asegurarse de que una columna etiquetada como FECHA contenga solo fechas dentro de un cierto rango. Con la validación de datos, puede controlar lo que se ingresa en las celdas de la hoja de trabajo.

Microsoft Excel admite varios tipos diferentes de validación de datos. Cada tipo se usa para controlar qué tipo de datos se ingresan en una celda o rango de celdas. A continuación, los fragmentos de código ilustran cómo validar eso:

- Numbers son enteros, es decir, que no tienen parte decimal.
- Los números decimales siguen la estructura correcta. El ejemplo de código define que un rango de celdas debe tener dos espacios decimales.
- Los valores están restringidos a una lista de valores. La validación de lista define una lista separada de valores que se pueden aplicar a una celda o rango de celdas.
- Las fechas caen dentro de un rango específico.
- Un tiempo está dentro de un rango específico.
- Un texto está dentro de una longitud de caracteres determinada.

### **Validación de datos con Microsoft Excel**

Para crear validaciones usando Microsoft Excel:

1. En una hoja de trabajo, seleccione las celdas a las que desea aplicar la validación.
1.  Desde el**Datos** menú, seleccione**Validación**. Se mostrará el cuadro de diálogo de validación.
1.  Haga clic en el**Ajustes** pestaña e ingrese a la configuración.

### **Validación de datos con Aspose.Cells**

La validación de datos es una característica poderosa para validar la información ingresada en las hojas de trabajo. Con la validación de datos, los desarrolladores pueden proporcionar a los usuarios una lista de opciones, restringir las entradas de datos a un tipo o tamaño específico, etc.
 En Aspose.Cells, cada[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase tiene un[**Validaciones**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations)propiedad que representa una colección de[**Validación**](https://reference.aspose.com/cells/net/aspose.cells/validation) objetos. Para configurar la validación, configure algunos de los[**Validación**](https://reference.aspose.com/cells/net/aspose.cells/validation)propiedades de la clase de la siguiente manera:

- Tipo: representa el tipo de validación, que se puede especificar utilizando uno de los valores predefinidos en el[**Tipo de validación**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)enumeración.
-  Operador: representa el operador que se utilizará en la validación, que se puede especificar utilizando uno de los valores predefinidos en el[**Tipo de operador**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)enumeración.
- Formula1: representa el valor o la expresión asociada con la primera parte de la validación de datos.
- Formula2: representa el valor o la expresión asociada con la segunda parte de la validación de datos.

 Cuando el[**Validación**](https://reference.aspose.com/cells/net/aspose.cells/validation) las propiedades del objeto han sido configuradas, los desarrolladores pueden usar el[**área de celda**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)estructura para almacenar información sobre el rango de celdas que se validará utilizando la validación creada.

#### **Tipos de validación de datos**

 Él[**Tipo de validación**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)enumeración tiene los siguientes miembros:

|**Nombre de miembro**|**Descripción**|
|:- |:- |
|Algún valor|Denota un valor de cualquier tipo.|
|Número entero|Indica el tipo de validación para números enteros.|
|Decimal|Indica el tipo de validación para números decimales.|
|Lista|Indica el tipo de validación para la lista desplegable.|
|Fecha|Indica el tipo de validación para las fechas.|
|Hora|Indica el tipo de validación por tiempo.|
|Longitud del texto|Indica el tipo de validación para la longitud del texto.|
|Disfraz|Indica un tipo de validación personalizado.|

##### **Validación de datos de números enteros**

Con este tipo de validación, los usuarios pueden ingresar solo números enteros dentro de un rango específico en las celdas validadas. Los ejemplos de código que siguen muestran cómo implementar el tipo de validación WholeNumber. El ejemplo crea la misma validación de datos usando Aspose.Cells que creamos usando Microsoft Excel arriba.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **Validación de datos de lista**

Este tipo de validación permite al usuario ingresar valores de una lista desplegable. Proporciona una lista: una serie de filas que contienen datos. En el ejemplo, se agrega una segunda hoja de trabajo para contener la fuente de la lista. Los usuarios solo pueden seleccionar valores de la lista. El área de validación es el rango de celdas A1:A5 en la primera hoja de cálculo.

 Aquí es importante que establezca el[**Validación.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) propiedad a**verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **Validación de datos de fecha**

Con este tipo de validación, los usuarios ingresan valores de fecha dentro de un rango específico, o que cumplen criterios específicos, en las celdas validadas. En el ejemplo, el usuario está restringido a ingresar fechas entre 1970 y 1999. Aquí, el área de validación es la celda B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **Validación de datos de tiempo**

Con este tipo de validación, los usuarios pueden ingresar tiempos dentro de un rango específico, o que cumplan con algunos criterios, en las celdas validadas. En el ejemplo, el usuario está restringido a ingresar horas entre las 09:00 y las 11:30 a. m. Aquí, el área de validación es la celda B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **Validación de datos de longitud de texto**

Con este tipo de validación, los usuarios pueden ingresar valores de texto de una longitud específica en las celdas validadas. En el ejemplo, el usuario está restringido a ingresar valores de cadena con no más de 5 caracteres. El área de validación es la celda B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **Reglas de validación de datos**

Cuando se implementan validaciones de datos, se puede verificar la validación asignando diferentes valores en las celdas.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) se puede utilizar para obtener el resultado de la validación. El siguiente ejemplo demuestra esta característica con diferentes valores. El archivo de muestra se puede descargar desde el siguiente enlace para realizar pruebas:

[ejemploDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **Compruebe si la validación en la celda es desplegable**

 Como hemos visto, hay muchos tipos de validaciones que se pueden implementar dentro de una celda. Si desea verificar si la validación es desplegable o no,[**Validación.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) propiedad se puede utilizar para probar esto. El siguiente código de ejemplo muestra el uso de esta propiedad. Un archivo de muestra para la prueba se puede descargar desde el siguiente enlace:

[muestraValidación.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **Agregar CellArea a la validación existente**

 Puede haber casos en los que desee agregar[**área de celda**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)a existente[**Validación**](https://reference.aspose.com/cells/net/aspose.cells/validation). cuando agregas[**área de celda**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) usando[**Validación.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea), Aspose.Cells comprueba todas las áreas existentes para ver si la nueva área ya existe. Si el archivo tiene una gran cantidad de validaciones, esto afecta el rendimiento. Para superar esto, el API proporciona la[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) método. Él*chequeIntersección* El parámetro indica si se debe verificar la intersección de un área dada con áreas de validación existentes. Configurándolo en**falso** deshabilitará la verificación de otras áreas. Él*comprobarBorde* El parámetro indica si se deben verificar las áreas aplicadas. Si la nueva área se convierte en el área superior izquierda, se reconstruyen las configuraciones internas. Si está seguro de que la nueva área no es el área superior izquierda, puede configurar este parámetro como**falso**.

El siguiente fragmento de código demuestra el uso de la[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) método para agregar nuevos[**área de celda**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)a existente[**Validación**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

Los archivos de Excel de origen y salida se adjuntan como referencia.

[Archivo fuente](96928093.xlsx)

[Archivo de salida](96928220.xlsx)


## **Temas avanzados**
- [Obtenga la validación Cell en los archivos ODS](/cells/es/net/get-cell-validation-in-ods-files/)
- [Obtenga la validación aplicada en un Cell](/cells/es/net/get-validation-applied-on-a-cell/)
- [Verifique que el valor Cell cumpla con las reglas de validación de datos](/cells/es/net/verify-that-cell-value-satisfies-data-validation-rules/)
