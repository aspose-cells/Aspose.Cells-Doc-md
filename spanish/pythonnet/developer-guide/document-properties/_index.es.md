---
title: Administrar propiedades del documento
linktitle: Propiedades del documento
type: docs
weight: 80
url: /es/python-net/managing-document-properties/
description: Aprende cómo gestionar las propiedades del documento a través de las APIs Aspose.Cells para Python via .NET.
keywords: Cómo gestionar propiedades de documentos en C#, Obtener o establecer propiedades de documentos usando C#, Añadir o eliminar propiedades de documentos vía C#, Insertar o remover propiedades de documentos con C#, Cómo acceder a propiedades del documento usando las APIs Aspose.Cells para Python via .NET.
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

Los desarrolladores pueden gestionar dinámicamente las propiedades del documento usando las APIs Aspose.Cells para Python via .NET. Esta característica ayuda a los desarrolladores a almacenar información útil junto con el archivo, como cuándo se recibió, procesó, se le puso marca de tiempo, etc.

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET escribe directamente la información sobre la API y el número de versión en los documentos de salida. Por ejemplo, al renderizar un documento a PDF, Aspose.Cells para Python via .NET llena el campo **Application** con el valor 'Aspose.Cells' y el campo **PDF Producer** con el valor, por ejemplo, 'Aspose.Cells para Python via .NET v17.9'.

Ten en cuenta que no puedes instruir a Aspose.Cells para Python via .NET para cambiar o eliminar esta información de los documentos de salida.

{{% /alert %}}


### **Cómo agregar o eliminar propiedades de documento personalizadas**

Como hemos descrito anteriormente al principio de este tema, los desarrolladores no pueden agregar o eliminar propiedades integradas porque estas propiedades están definidas por el sistema, pero es posible agregar o eliminar propiedades personalizadas porque estas son definidas por el usuario.

### **Cómo agregar propiedades personalizadas**

Las APIs Aspose.Cells para Python via .NET han expuesto el método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) para la clase [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection) para añadir propiedades personalizadas a la colección. El método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) añade la propiedad al archivo de Excel y devuelve una referencia a la nueva propiedad del documento como un objeto [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/documentproperty).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingDocumentProperties.py" >}}


## **Temas avanzados**
- [Agregar propiedades personalizadas visibles dentro del Panel de información del documento](/cells/es/python-net/adding-custom-properties-visible-inside-document-information-panel/)
- [Establecer las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento Integradas](/cells/es/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Especificar la versión del documento del archivo de Excel mediante propiedades de documento integradas](/cells/es/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Especificar el idioma del archivo de Excel mediante propiedades de documento integradas](/cells/es/python-net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

