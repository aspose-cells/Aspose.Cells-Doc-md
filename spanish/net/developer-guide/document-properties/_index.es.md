---
title: Administrar propiedades del documento
linktitle: Propiedades del documento
type: docs
weight: 80
url: /es/net/managing-document-properties/
description: Aprenda a administrar las propiedades del documento a través de Aspose.Cells para las API NET.
keywords: How to Manage Document Properties in C#, Get or Set Document Properties using C#, Add or Delete Document Properties via C#, Insert or Remove Document Properties with C#, How to Access Document Properties using Aspose.Cells for NET APIs.
---
##  **Introducción**

Microsoft Excel ofrece la posibilidad de agregar propiedades a archivos de hojas de cálculo. Estas propiedades del documento proporcionan información útil y se dividen en 2 categorías como se detalla a continuación.

- Propiedades definidas por el sistema (integradas): las propiedades integradas contienen información general sobre el documento, como el título del documento, el nombre del autor, las estadísticas del documento, etc.
- Propiedades definidas por el usuario (personalizadas): propiedades personalizadas definidas por el usuario final en forma de par nombre-valor.

{{% alert color="primary" %}}

El punto más importante que debe saber sobre las propiedades integradas y personalizadas es que se puede acceder a las propiedades integradas y modificarlas, pero no crearlas ni eliminarlas. Sin embargo, se pueden crear y administrar propiedades personalizadas.

{{% /alert %}}

##  **Cómo administrar las propiedades del documento usando Microsoft Excel**

 Microsoft Excel le permite administrar las propiedades del documento de los archivos de Excel de manera WYSIWYG. Siga los pasos a continuación para abrir el**Propiedades** cuadro de diálogo en Excel 2016.

1.  Desde el**Archivo** menú, seleccione *Información**.

|**Selección del menú Información**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1.  Haga clic en**Propiedades** encabezado y seleccione "Propiedades avanzadas".

|**Al hacer clic en Selección de propiedades avanzadas**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Administre las propiedades del documento del archivo.

|**Diálogo de propiedades**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
En el cuadro de diálogo Propiedades, hay diferentes pestañas, como General, Resumen, Estadísticas, Contenido y Aduanas. Cada pestaña ayuda a configurar diferentes tipos de información relacionada con el archivo. La pestaña Personalizado se utiliza para administrar propiedades personalizadas.

##  **Cómo trabajar con propiedades de documentos usando Aspose.Cells**

Los desarrolladores pueden administrar dinámicamente las propiedades del documento utilizando las API Aspose.Cells. Esta característica ayuda a los desarrolladores a almacenar información útil junto con el archivo, como cuándo se recibió, procesó, con marca de tiempo, etc.

{{% alert color="primary" %}}

 Aspose.Cells for .NET escribe directamente la información sobre API y el número de versión en los documentos de salida. Por ejemplo, al representar el documento en PDF, Aspose.Cells for .NET completa**Solicitud** campo con valor 'Aspose.Cells' y**PDF Productor** campo con el valor, por ejemplo, 'Aspose.Cells v17.9'.

Tenga en cuenta que no puede indicarle a Aspose.Cells for .NET que cambie o elimine esta información de los documentos de salida.

{{% /alert %}}

###  **Cómo acceder a las propiedades del documento**

 Aspose.Cells Las API admiten ambos tipos de propiedades de documento, integradas y personalizadas. Aspose.Cells'[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) La clase representa un archivo de Excel y, como un archivo de Excel, el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) La clase puede contener varias hojas de trabajo, cada una representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase, mientras que la colección de hojas de trabajo está representada por[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)clase.

 Utilizar el[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)para acceder a las propiedades del documento del archivo como se describe a continuación.

- Para acceder a las propiedades integradas del documento, utilice[**Colección de hojas de trabajo.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  Para acceder a las propiedades personalizadas del documento, utilice[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 Ambos[**Colección de hojas de trabajo.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) y[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) devolver la instancia de[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Esta colección contiene[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)objetos, cada uno de los cuales representa una única propiedad de documento integrada o personalizada.

 Depende del requisito de la solicitud cómo acceder a una propiedad, es decir; utilizando el índice o nombre de la propiedad del[**Colección de propiedades del documento**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)como se demuestra en el siguiente ejemplo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

 El[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)La clase permite recuperar el nombre, valor y tipo de la propiedad del documento:

-  Para obtener el nombre de la propiedad, utilice[**PropiedadDocumento.Nombre**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  Para obtener el valor de la propiedad, use[**Propiedad del documento.Valor**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**Propiedad del documento.Valor**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)devuelve el valor como un Objeto.
-  Para obtener el tipo de propiedad, utilice[**PropiedadDeDocumento.Tipo**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Esto devuelve uno de los[**Tipo de propiedad**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)valores de enumeración. Después de obtener el tipo de propiedad, utilice uno de los**PropiedadDeDocumento.ToXXX** métodos para obtener el valor del tipo apropiado en lugar de utilizar[**Propiedad del documento.Valor**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) . El**PropiedadDeDocumento.ToXXX**Los métodos se describen en la siguiente tabla.

{{% alert color="primary" %}}

 El[**Propiedad del documento**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)La clase también proporciona un conjunto de métodos que devuelven los valores de otros tipos de datos.

{{% /alert %}}

|**Nombre de miembro**|**Descripción**|**Método ToXXX**|
| :- | :- | :- |
|Booleano|El tipo de datos de la propiedad es booleano.|ParaBool|
|Fecha| El tipo de datos de la propiedad es DateTime. Tenga en cuenta que Microsoft Excel sólo almacena<br>la parte de la fecha, no se puede almacenar ninguna hora en una propiedad personalizada de este tipo|Hasta fecha y hora|
|Flotar|El tipo de datos de la propiedad es Doble|Para duplicar|
|Número|El tipo de datos de la propiedad es Int32.|ToInt|
|String|El tipo de datos de la propiedad es String|Encadenar|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

###  **Cómo agregar o eliminar propiedades de documentos personalizados**

Como describimos anteriormente al comienzo de este tema, los desarrolladores no pueden agregar ni eliminar propiedades integradas porque están definidas por el sistema, pero es posible agregar o eliminar propiedades personalizadas porque están definidas por el usuario.

###  **Cómo agregar propiedades personalizadas**

 Aspose.Cells Las API han expuesto el[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) método para el[**Colección de propiedades de documentos personalizados**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) clase para agregar propiedades personalizadas a la colección. El[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) El método agrega la propiedad al archivo de Excel y devuelve una referencia para la nueva propiedad del documento como un[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)objeto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

###  **Cómo configurar la propiedad personalizada "Enlace al contenido"**

 Para crear una propiedad personalizada vinculada al contenido de un rango determinado, llame al[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) método y pase el nombre de la propiedad y la fuente. Puede verificar si una propiedad está configurada como vinculada al contenido usando el[**PropiedadDeDocumento.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) propiedad. Además, también es posible obtener el rango de fuente utilizando el[**Fuente**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) propiedad de la[**Propiedad del documento**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)clase.

Usamos una plantilla simple Microsoft archivo Excel en el ejemplo. El libro tiene un rango con nombre definido etiquetado**Mi gama** que se refiere a un valor de celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

###  **Cómo eliminar propiedades personalizadas**

 Para eliminar propiedades personalizadas usando Aspose.Cells, llame al[**DocumentPropertyCollection.Eliminar**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)método y pase el nombre de la propiedad del documento que se eliminará.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

##  **Temas avanzados**
- [Agregar propiedades personalizadas visibles dentro del Panel de información del documento](/cells/es/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Configuración de las propiedades ScaleCrop y LinksUpToDate de las propiedades del documento integrado](/cells/es/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Especifique la versión del documento del archivo de Excel utilizando las propiedades del documento integradas](/cells/es/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Especifique el idioma del archivo de Excel utilizando las propiedades del documento integradas](/cells/es/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
