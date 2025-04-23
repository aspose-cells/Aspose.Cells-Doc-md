---
title: Gestión de Propiedades del Documento
type: docs
weight: 10
url: /es/java/managing-document-properties/
---

## **Introducción**

Microsoft Excel proporciona la capacidad de agregar propiedades a los archivos de hojas de cálculo. Estas propiedades del documento proporcionan información útil y se dividen en 2 categorías como se detalla a continuación.

- Propiedades predeterminadas del sistema (integradas): Las propiedades integradas contienen información general sobre el documento, como el título del documento, el nombre del autor, estadísticas del documento, entre otros.
- Propiedades definidas por el usuario (personalizadas): Propiedades personalizadas definidas por el usuario final en forma de par nombre-valor.

{{% alert color="primary" %}}

El punto más importante a tener en cuenta sobre las propiedades incorporadas y personalizadas es que las propiedades incorporadas pueden ser accedidas y modificadas, pero no pueden ser creadas o eliminadas, sin embargo, las propiedades de documento personalizadas pueden ser creadas y gestionadas.

{{% /alert %}}

## **Gestión de Propiedades del Documento Utilizando Microsoft Excel**

Microsoft Excel permite gestionar las propiedades del documento de los archivos de Excel de manera WYSIWYG. Sigue los siguientes pasos para abrir el diálogo de **Propiedades** en Excel 2016.

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

## **Trabajando con las propiedades del documento usando Aspose.Cells**

Los desarrolladores pueden gestionar dinámicamente las propiedades del documento usando las APIs de Aspose.Cells. Esta característica ayuda a los desarrolladores a almacenar información útil junto con el archivo, como cuándo se recibió el archivo, se procesó, se marcó con la hora, y así sucesivamente.

{{% alert color="primary" %}}

Aspose.Cells for Java escribe directamente la información sobre la API y el número de versión en los documentos de salida. Por ejemplo, al representar un documento a PDF, Aspose.Cells for Java rellena el campo **Aplicación** con el valor 'Aspose.Cells' y el campo **Productor de PDF** con el valor, por ejemplo, 'Aspose.Cells for Java v17.9'.

Tenga en cuenta que no puede instruir a Aspose.Cells for Java para cambiar o eliminar esta información de los Documentos de salida.

{{% /alert %}}

### **Accediendo a las propiedades del documento**

Las APIs de Aspose.Cells admiten tanto tipos de propiedades de documentos integrados como personalizados. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) de Aspose.Cells representa un archivo de Excel y, al igual que un archivo de Excel, la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) puede contener múltiples hojas de cálculo, cada uno representado por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet), mientras que la colección de hojas de cálculo es representada por la clase [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection).

Utilice el [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) para acceder a las propiedades del documento del archivo como se describe a continuación.

- Para acceder a las propiedades de documento integradas, use [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
- Para acceder a propiedades de documento personalizadas, utiliza el [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

Tanto el [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) como el [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) devuelven una instancia de [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection). Esta colección contiene objetos [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty), cada uno de los cuales representa una única propiedad de documento incorporada o personalizada.

Depende de los requisitos de la aplicación cómo acceder a una propiedad, es decir; utilizando el índice o el nombre de la propiedad de [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) como se demuestra en el ejemplo a continuación.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

La clase [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) permite recuperar el nombre, valor y tipo de la propiedad del documento:

- Para obtener el nombre de la propiedad, use [**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
- Para obtener el valor de la propiedad, use [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value) devuelve el valor como un Objeto.
- Para obtener el tipo de propiedad, use [**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type). Esto devuelve uno de los valores de enumeración [**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Agregar o Quitar Propiedades de Documentos Personalizadas**

Como hemos descrito anteriormente al principio de este tema, los desarrolladores no pueden agregar o eliminar propiedades integradas porque estas propiedades están definidas por el sistema, pero es posible agregar o eliminar propiedades personalizadas porque estas son definidas por el usuario.

### **Agregar Propiedades Personalizadas**

Las APIs de Aspose.Cells han expuesto el método [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add-java.lang.String-boolean-) para la clase [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) con el fin de agregar propiedades personalizadas a la colección. El método [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add-java.lang.String-boolean-) agrega la propiedad al archivo de Excel y devuelve una referencia para la nueva propiedad del documento como un objeto [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Configurar la Propiedad Personalizada “Vincular al Contenido”**

Para crear una propiedad personalizada vinculada al contenido de un rango dado, llame al método [**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent-java.lang.String-java.lang.String-) y pase el nombre de la propiedad y la fuente. Puede verificar si una propiedad está configurada como vinculada con el contenido usando la propiedad [**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent). Además, también es posible obtener el rango de origen utilizando la propiedad [**Source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) de la clase [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)

Utilizamos un archivo de plantilla simple de Microsoft Excel en el ejemplo. El libro de trabajo tiene un rango con nombre definido etiquetado como **MiRango** que se refiere a un valor de celda.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Eliminar Propiedades Personalizadas**

Para eliminar propiedades personalizadas mediante Aspose.Cells, llame al método [**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove-java.lang.String-) y pase el nombre de la propiedad del documento que se va a eliminar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
{{< app/cells/assistant language="java" >}}
