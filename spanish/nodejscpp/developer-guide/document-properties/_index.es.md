---
title: Gestionar propiedades del documento con Node.js a través de C++
linktitle: Propiedades del documento
type: docs
weight: 80
url: /es/nodejs-cpp/managing-document-properties/
description: Aprende cómo gestionar las propiedades del documento a través de las APIs Aspose.Cells for Node.js via C++.
keywords: Cómo gestionar las propiedades del documento en Node.js a través de C++, Obtener o establecer propiedades del documento usando Node.js a través de C++, Agregar o eliminar propiedades del documento mediante Node.js a través de C++, Insertar o remover propiedades del documento con Node.js a través de C++, Cómo acceder a las propiedades del documento usando las APIs Aspose.Cells for Node.js via C++.
---


## **Introducción**

Microsoft Excel proporciona la capacidad de agregar propiedades a los archivos de hojas de cálculo. Estas propiedades del documento proporcionan información útil y se dividen en 2 categorías como se detalla a continuación.

- Propiedades predeterminadas del sistema (integradas): Las propiedades integradas contienen información general sobre el documento, como el título del documento, el nombre del autor, estadísticas del documento, entre otros.
- Propiedades definidas por el usuario (personalizadas): Propiedades personalizadas definidas por el usuario final en forma de par nombre-valor.

{{% alert color="primary" %}}

El punto más importante a tener en cuenta sobre las propiedades integradas y personalizadas es que las propiedades integradas se pueden acceder y modificar, pero no crear ni eliminar. Sin embargo, las propiedades personalizadas se pueden crear y gestionar.

{{% /alert %}}

## **Cómo administrar propiedades de documento utilizando Microsoft Excel**

Microsoft Excel te permite gestionar las propiedades del documento de los archivos de Excel de forma WYSIWYG. Por favor, sigue los pasos a continuación para abrir el diálogo de **Propiedades** en Excel 2016.

1. Desde el menú **Archivo**, seleccione **Información**.

|**Seleccionar menú Información**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Haga clic en el encabezado **Propiedades** y seleccione "Propiedades avanzadas".

|**Haciendo clic en la selección de Propiedades avanzadas**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Administre las propiedades del documento del archivo.

|**Cuadro de propiedades**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
En el cuadro de propiedades, hay pestañas diferentes, como General, Resumen, Estadísticas, Contenidos y Aduanas. Cada pestaña ayuda a configurar diferentes tipos de información relacionada con el archivo. La pestaña Aduanas se usa para gestionar propiedades personalizadas.

## **Cómo trabajar con las propiedades del documento usando Aspose.Cells**

Los desarrolladores pueden gestionar dinámicamente las propiedades del documento usando las APIs de Aspose.Cells. Esta característica ayuda a los desarrolladores a almacenar información útil junto con el archivo, como cuándo se recibió el archivo, se procesó, se marcó con la hora, y así sucesivamente.

{{% alert color="primary" %}}

Las APIs Aspose.Cells for Node.js via C++ escriben directamente la información sobre la API y el número de versión en los documentos de salida. Por ejemplo, al convertir un Documento a PDF, Aspose.Cells for Node.js via C++ llena el campo **Aplicación** con el valor 'Aspose.Cells' y el campo **Productor PDF** con el valor, por ejemplo, 'Aspose.Cells v17.9'.

Ten en cuenta que no puedes instruir a Aspose.Cells for Node.js via C++ para cambiar o eliminar esta información de los Documentos de salida.

{{% /alert %}}

### **Cómo acceder a las propiedades del documento**

Las APIs de Aspose.Cells soportan ambos tipos de propiedades del documento, integradas y personalizadas. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) de Aspose.Cells representa un archivo de Excel y, como un archivo de Excel, la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) puede contener múltiples hojas de cálculo, cada una representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) mientras que la colección de hojas de cálculo está representada por la clase [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection).

Utiliza [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) para acceder a las propiedades del documento del archivo como se describe a continuación.

- Para acceder a las propiedades de documento integradas, use [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--).
- Para acceder a las propiedades de documento personalizadas, use [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--).

Tanto [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--) como [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--) devuelven la instancia de [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/). Esta colección contiene [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) objetos, cada uno de los cuales representa una sola propiedad del documento, ya sea integrada o personalizada.

Depende del requisito de la aplicación cómo acceder a una propiedad; es decir, usando el índice o el nombre de la propiedad desde [**DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/) como se demuestra en el ejemplo a continuación.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property by using the property name
const customProperty1 = customProperties.get("ContentTypeId");
console.log(`${customProperty1.getName()} ${customProperty1.getValue()}`);

// Accessing the same custom document property by using the property index
const customProperty2 = customProperties.get(0);
console.log(`${customProperty2.getName()} ${customProperty2.getValue()}`);
```

La clase [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) permite recuperar el nombre, valor y tipo de la propiedad del documento:

- Para obtener el nombre de la propiedad, use [**DocumentProperty.getName()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getName--).
- Para obtener el valor de la propiedad, usa [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--) devuelve el valor como un Objeto.
- Para obtener el tipo de propiedad, usa [**DocumentProperty.getType()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getType--). Esto devuelve uno de los valores de la enumeración [**PropertyType**](https://reference.aspose.com/cells/nodejs-cpp/propertytype/). Después de obtener el tipo de propiedad, usa uno de los métodos **DocumentProperty.ToXXX** para obtener el valor del tipo apropiado en lugar de usar [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). Los métodos **DocumentProperty.ToXXX** se describen en la tabla a continuación.

{{% alert color="primary" %}}

La clase [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) también proporciona un conjunto de métodos que devuelven los valores de otros tipos de datos.

{{% /alert %}}

|**Nombre de Miembro**|**Descripción**|**Método ToXXX**|
| :- | :- | :- |
|Boolean|El tipo de dato de propiedad es Booleano|ABoolean|
|Date|El tipo de datos de la propiedad es DateTime. Tenga en cuenta que Microsoft Excel solo almacena la parte de la fecha, no se puede almacenar la hora en una propiedad personalizada de este tipo|ToDateTime|
|Float|El tipo de datos de la propiedad es Double|ToDouble|
|Number|El tipo de datos de la propiedad es Int32|ToInt|
|String|El tipo de dato de la propiedad es string|ToString|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property
const customProperty1 = customProperties.get(0);

// Storing the value of the document property as an object
const objectValue = customProperty1.getValue();

// Accessing a custom document property
const customProperty2 = customProperties.get(1);

// Checking the type of the document property and then storing the value of the
// document property according to that type
if (customProperty2.getType() === AsposeCells.PropertyType.String) {
const value = customProperty2.getValue().toString();
console.log(`${customProperty2.getName()} : ${value}`);
}
```

### **Cómo agregar o eliminar propiedades de documento personalizadas**

Como hemos descrito anteriormente al principio de este tema, los desarrolladores no pueden agregar o eliminar propiedades integradas porque estas propiedades están definidas por el sistema, pero es posible agregar o eliminar propiedades personalizadas porque estas son definidas por el usuario.

### **Cómo agregar propiedades personalizadas**

Las APIs de Aspose.Cells han expuesto el método [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) para la clase [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/) con el fin de agregar propiedades personalizadas a la colección. El método [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) añade la propiedad al archivo de Excel y devuelve una referencia para la nueva propiedad del documento como un objeto [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Adding a custom document property to the Excel file
customProperties.add("Publisher", "Aspose");

// Saving resultant spreadsheet
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Cómo configurar la propiedad personalizada de “Vínculo con contenido”**

Para crear una propiedad personalizada vinculada al contenido de un rango dado, llama al método [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) y pasa el nombre de la propiedad y la fuente. Puedes verificar si una propiedad está configurada como vinculada al contenido usando la propiedad [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#isLinkedToContent--). Además, también es posible obtener el rango fuente usando la propiedad [**getSource()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getSource--) de la clase [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/).

Utilizamos un archivo de plantilla simple de Microsoft Excel en el ejemplo. El libro de trabajo tiene un rango con nombre definido etiquetado como **MiRango** que se refiere a un valor de celda.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate an object of Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getWorksheets().getCustomDocumentProperties();

// Add link to content.
customProperties.addLinkToContent("Owner", "MyRange");

// Accessing the custom document property by using the property name
const customProperty1 = customProperties.get("Owner");

// Check whether the property is linked to content
const isLinkedToContent = customProperty1.isLinkedToContent();

// Get the source for the property
const source = customProperty1.getSource();

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Cómo eliminar propiedades personalizadas**

Para eliminar propiedades personalizadas usando Aspose.Cells, llama al método [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/#remove-string-) y pasa el nombre de la propiedad del documento a eliminar.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Removing a custom document property
customProperties.remove("Publisher");

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

## **Temas avanzados**
- [Agregar propiedades personalizadas visibles dentro del Panel de información del documento](/cells/es/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Establecer las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento Integradas](/cells/es/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Especificar la versión del documento del archivo de Excel mediante propiedades de documento integradas](/cells/es/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Especificar el idioma del archivo de Excel mediante propiedades de documento integradas](/cells/es/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
