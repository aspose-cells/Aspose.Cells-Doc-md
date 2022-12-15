---
title: Administrar propiedades de documentos
linktitle: Propiedades del documento
type: docs
weight: 80
url: /es/net/managing-document-properties/
description: Administre las propiedades de los documentos de los archivos de hojas de cálculo.
---
## **Introducción**

Microsoft Excel ofrece la posibilidad de agregar propiedades a los archivos de hojas de cálculo. Estas propiedades del documento brindan información útil y se dividen en 2 categorías, como se detalla a continuación.

- Propiedades definidas por el sistema (integradas): las propiedades integradas contienen información general sobre el documento, como el título del documento, el nombre del autor, las estadísticas del documento, etc.
- Propiedades definidas por el usuario (personalizadas): propiedades personalizadas definidas por el usuario final en forma de par nombre-valor.

{{% alert color="primary" %}}

El punto más importante que debe saber acerca de las propiedades integradas y personalizadas es que se puede acceder a las propiedades integradas y modificarlas, pero no crearlas ni eliminarlas. Sin embargo, las propiedades personalizadas se pueden crear y administrar.

{{% /alert %}}

## **Administrar las propiedades del documento usando Microsoft Excel**

 Microsoft Excel le permite administrar las propiedades del documento de los archivos de Excel de manera WYSIWYG. Siga los pasos a continuación para abrir el**Propiedades** cuadro de diálogo en Excel 2016.

1.  Desde el**Expediente** menú, seleccione**Información**.

|**Selección del menú de información**|
|:- |
|![todo:imagen_alternativa_texto](managing-document-properties_1.png)|
1.  Haga clic en**Propiedades** encabezado y seleccione "Propiedades avanzadas".

|**Hacer clic en Selección de propiedades avanzadas**|
|:- |
|![todo:imagen_alternativa_texto](managing-document-properties_2.png)|
1. Administre las propiedades del documento del archivo.

|**Diálogo de propiedades**|
|:- |
|![todo:imagen_alternativa_texto](managing-document-properties_3.png)|
En el cuadro de diálogo Propiedades, hay diferentes pestañas, como General, Resumen, Estadísticas, Contenido y Aduanas. Cada pestaña ayuda a configurar diferentes tipos de información relacionada con el archivo. La pestaña Personalizado se utiliza para administrar las propiedades personalizadas.

## **Trabajar con propiedades de documentos usando Aspose.Cells**

Los desarrolladores pueden administrar dinámicamente las propiedades del documento utilizando las API Aspose.Cells. Esta función ayuda a los desarrolladores a almacenar información útil junto con el archivo, como cuándo se recibió, procesó, marcó la hora, etc.

{{% alert color="primary" %}}

 Aspose.Cells for .NET escribe directamente la información sobre API y el número de versión en los documentos de salida. Por ejemplo, al renderizar Documento a PDF, Aspose.Cells for .NET se completa**Solicitud** campo con valor 'Aspose.Cells' y**Productor de PDF** campo con el valor, por ejemplo, 'Aspose.Cells v17.9'.

Tenga en cuenta que no puede indicar al Aspose.Cells for .NET que cambie o elimine esta información de los documentos de salida.

{{% /alert %}}

### **Acceso a las propiedades del documento**

 Aspose.Cells Las API admiten ambos tipos de propiedades de documentos, integradas y personalizadas. Aspose.Cells'[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase representa un archivo de Excel y, como un archivo de Excel, el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)La clase puede contener varias hojas de trabajo, cada una representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) mientras que la colección de hojas de trabajo está representada por el[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)clase.

 Utilizar el[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)para acceder a las propiedades del documento del archivo como se describe a continuación.

-  Para acceder a las propiedades del documento incorporado, use[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  Para acceder a las propiedades del documento personalizado, use[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 Ambos[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) y[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) devolver la instancia de[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Esta colección contiene[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)objetos, cada uno de los cuales representa una única propiedad de documento integrada o personalizada.

 Queda a criterio de la solicitud cómo acceder a un inmueble, es decir; utilizando el índice o el nombre de la propiedad de la[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)como se demuestra en el siguiente ejemplo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

 los[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)class permite recuperar el nombre, valor y tipo de la propiedad del documento:

-  Para obtener el nombre de la propiedad, utilice[**DocumentoPropiedad.Nombre**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  Para obtener el valor de la propiedad, utilice[**DocumentoPropiedad.Valor**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentoPropiedad.Valor**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)devuelve el valor como un objeto.
-  Para obtener el tipo de propiedad, use[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Esto devuelve uno de los[**Tipo de propiedad**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype) valores de enumeración. Después de obtener el tipo de propiedad, utilice uno de los**PropiedadDocumento.ToXXX** métodos para obtener el valor del tipo apropiado en lugar de utilizar[**DocumentoPropiedad.Valor**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) . los**PropiedadDocumento.ToXXX**Los métodos se describen en la siguiente tabla.

{{% alert color="primary" %}}

 los[**DocumentoPropiedad**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)class también proporciona un conjunto de métodos que devuelven los valores de otros tipos de datos.

{{% /alert %}}

|**Nombre de miembro**|**Descripción**|**Método ToXXX**|
|:- |:- |:- |
|booleano|El tipo de datos de la propiedad es booleano.|ToBool|
|Fecha|El tipo de datos de la propiedad es DateTime. Tenga en cuenta que Microsoft Excel solo almacena<br>la parte de la fecha, no se puede almacenar la hora en una propiedad personalizada de este tipo|HastaFechaHora|
|Flotar|El tipo de datos de la propiedad es Doble|Para duplicar|
|Número|El tipo de datos de propiedad es Int32|ToInt|
|Cuerda|El tipo de datos de la propiedad es String|Encadenar|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Adición o eliminación de propiedades de documentos personalizados**

Como describimos anteriormente al comienzo de este tema, los desarrolladores no pueden agregar o quitar propiedades integradas porque estas propiedades están definidas por el sistema, pero es posible agregar o quitar propiedades personalizadas porque están definidas por el usuario.

### **Adición de propiedades personalizadas**

 Aspose.Cells Las API han expuesto el[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) método para el[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) class para agregar propiedades personalizadas a la colección. los[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) El método agrega la propiedad al archivo de Excel y devuelve una referencia para la propiedad del nuevo documento como un[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)objeto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **Configuración de la propiedad personalizada "Enlace al contenido"**

 Para crear una propiedad personalizada vinculada al contenido de un rango determinado, llame al[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) método y pase el nombre de la propiedad y la fuente. Puede comprobar si una propiedad está configurada como vinculada a contenido utilizando el[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) propiedad. Además, también es posible obtener el rango de fuente usando el[**Fuente**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) propiedad de la[**DocumentoPropiedad**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)clase.

 Usamos una plantilla simple Microsoft archivo de Excel en el ejemplo. El libro de trabajo tiene un rango con nombre definido etiquetado**MiRango** que se refiere a un valor de celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Eliminación de propiedades personalizadas**

 Para eliminar propiedades personalizadas usando Aspose.Cells, llame al[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)y pase el nombre de la propiedad del documento que se eliminará.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Temas avanzados**
- [Adición de propiedades personalizadas visibles dentro del panel de información del documento](/cells/es/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Configuración de las propiedades ScaleCrop y LinksUpToDate de las propiedades del documento integrado](/cells/es/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Especifique la versión del documento del archivo de Excel usando las propiedades del documento incorporado](/cells/es/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Especifique el idioma del archivo de Excel usando las propiedades del documento incorporado](/cells/es/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
