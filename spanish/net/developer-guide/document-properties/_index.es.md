---
title: Administrar propiedades del documento
linktitle: Propiedades del documento
type: docs
weight: 80
url: /es/net/managing-document-properties/
description: Aprenda a administrar propiedades de documento a través de las API Aspose.Cells for NET.
keywords: Cómo administrar propiedades de documento en C#, Obtener o establecer propiedades de documento usando C#, Agregar o eliminar propiedades de documento vía C#, Insertar o quitar propiedades de documento con C#, Cómo acceder a propiedades de documento usando las API Aspose.Cells for NET.
---


## **Introducción**

Microsoft Excel proporciona la capacidad de agregar propiedades a los archivos de hojas de cálculo. Estas propiedades del documento proporcionan información útil y se dividen en 2 categorías como se detalla a continuación.

- Propiedades predeterminadas del sistema (integradas): Las propiedades integradas contienen información general sobre el documento, como el título del documento, el nombre del autor, estadísticas del documento, entre otros.
- Propiedades definidas por el usuario (personalizadas): Propiedades personalizadas definidas por el usuario final en forma de par nombre-valor.

{{% alert color="primary" %}}

El punto más importante a tener en cuenta sobre las propiedades integradas y personalizadas es que las propiedades integradas se pueden acceder y modificar, pero no crear ni eliminar. Sin embargo, las propiedades personalizadas se pueden crear y gestionar.

{{% /alert %}}

## **Cómo administrar propiedades de documento utilizando Microsoft Excel**

Microsoft Excel le permite administrar las propiedades de documento de los archivos de Excel de forma WYSIWYG. Siga los siguientes pasos para abrir el diálogo **Propiedades** en Excel 2016.

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

Aspose.Cells for .NET escribe directamente la información sobre API y el número de versión en los documentos de salida. Por ejemplo, al representar un documento a PDF, Aspose.Cells for .NET llena el campo **Aplicación** con el valor 'Aspose.Cells' y el campo **Productor de PDF** con el valor, por ejemplo 'Aspose.Cells v17.9'.

Tenga en cuenta que no puede indicar a Aspose.Cells for .NET que cambie o elimine esta información de los documentos de salida.

{{% /alert %}}

### **Cómo acceder a las propiedades del documento**

Las APIs de Aspose.Cells admiten tanto tipos de propiedades de documentos integrados como personalizados. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) de Aspose.Cells representa un archivo de Excel y, al igual que un archivo de Excel, la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) puede contener múltiples hojas de cálculo, cada uno representado por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet), mientras que la colección de hojas de cálculo es representada por la clase [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection).

Utilice el [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) para acceder a las propiedades del documento del archivo como se describe a continuación.

- Para acceder a las propiedades de documento integradas, use [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
- Para acceder a las propiedades de documento personalizadas, use [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

Tanto [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) como [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) devuelven la instancia de [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Esta colección contiene objetos de [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty), cada uno de los cuales representa una única propiedad de documento integrada o personalizada.

Depende de los requisitos de la aplicación cómo acceder a una propiedad, es decir; utilizando el índice o el nombre de la propiedad de [**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection) como se demuestra en el ejemplo a continuación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

La clase [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) permite recuperar el nombre, valor y tipo de la propiedad del documento:

- Para obtener el nombre de la propiedad, use [**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
- Para obtener el valor de la propiedad, use [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) devuelve el valor como un Objeto.
- Para obtener el tipo de propiedad, use [**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type). Esto devuelve uno de los valores de enumeración de [**PropertyType**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype). Después de obtener el tipo de propiedad, use uno de los métodos **DocumentProperty.ToXXX** para obtener el valor del tipo apropiado en lugar de usar [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). Los métodos **DocumentProperty.ToXXX** se describen en la tabla a continuación.

{{% alert color="primary" %}}

La clase [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) también proporciona un conjunto de métodos que devuelven los valores de otros tipos de datos.

{{% /alert %}}

|**Nombre de Miembro**|**Descripción**|**Método ToXXX**|
| :- | :- | :- |
|Boolean|El tipo de dato de propiedad es Booleano|ABoolean|
|Date|El tipo de datos de la propiedad es DateTime. Tenga en cuenta que Microsoft Excel solo almacena la parte de la fecha, no se puede almacenar la hora en una propiedad personalizada de este tipo|ToDateTime|
|Float|El tipo de datos de la propiedad es Double|ToDouble|
|Number|El tipo de datos de la propiedad es Int32|ToInt|
|String|El tipo de datos de la propiedad es String|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Cómo agregar o eliminar propiedades de documento personalizadas**

Como hemos descrito anteriormente al principio de este tema, los desarrolladores no pueden agregar o eliminar propiedades integradas porque estas propiedades están definidas por el sistema, pero es posible agregar o eliminar propiedades personalizadas porque estas son definidas por el usuario.

### **Cómo agregar propiedades personalizadas**

Las APIs de Aspose.Cells han expuesto el método [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) para la clase [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) con el fin de agregar propiedades personalizadas a la colección. El método [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) agrega la propiedad al archivo de Excel y devuelve una referencia para la nueva propiedad de documento como un objeto [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **Cómo configurar la propiedad personalizada de “Vínculo con contenido”**

Para crear una propiedad personalizada vinculada al contenido de un rango dado, llame al método [**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) y pase el nombre de la propiedad y la fuente. Puede verificar si una propiedad está configurada como vinculada con el contenido usando la propiedad [**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent). Además, también es posible obtener el rango de origen utilizando la propiedad [**Source**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) de la clase [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)

Utilizamos un archivo de plantilla simple de Microsoft Excel en el ejemplo. El libro de trabajo tiene un rango con nombre definido etiquetado como **MiRango** que se refiere a un valor de celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Cómo eliminar propiedades personalizadas**

Para eliminar propiedades personalizadas mediante Aspose.Cells, llame al método [**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove) y pase el nombre de la propiedad del documento que se va a eliminar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Temas avanzados**
- [Agregar propiedades personalizadas visibles dentro del Panel de información del documento](/cells/es/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Establecer las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento Integradas](/cells/es/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Especificar la versión del documento del archivo de Excel mediante propiedades de documento integradas](/cells/es/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Especificar el idioma del archivo de Excel mediante propiedades de documento integradas](/cells/es/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
