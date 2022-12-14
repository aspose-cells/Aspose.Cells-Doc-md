---
title: Gestión de propiedades de documentos
type: docs
weight: 10
url: /es/java/managing-document-properties/
---
## **Introducción**

Microsoft Excel ofrece la posibilidad de agregar propiedades a los archivos de hojas de cálculo. Estas propiedades del documento brindan información útil y se dividen en 2 categorías, como se detalla a continuación.

- Propiedades definidas por el sistema (integradas): las propiedades integradas contienen información general sobre el documento, como el título del documento, el nombre del autor, las estadísticas del documento, etc.
- Propiedades definidas por el usuario (personalizadas): propiedades personalizadas definidas por el usuario final en forma de par nombre-valor.

{{% alert color="primary" %}}

El punto más importante que debe conocer acerca de las propiedades integradas y personalizadas es que se puede acceder a las propiedades integradas y modificarlas, pero no se pueden crear ni eliminar; sin embargo, se pueden crear y administrar las propiedades personalizadas de los documentos.

{{% /alert %}}

## **Administrar las propiedades del documento usando Microsoft Excel**

 Microsoft Excel permite administrar las propiedades de los documentos de los archivos de Excel de manera WYSIWYG. Siga los pasos a continuación para abrir el**Propiedades** cuadro de diálogo en Excel 2016.

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

 Aspose.Cells for Java escribe directamente la información sobre API y el número de versión en los documentos de salida. Por ejemplo, al renderizar Documento a PDF, Aspose.Cells for Java se completa**Solicitud** campo con valor 'Aspose.Cells' y**Productor de PDF** campo con el valor, por ejemplo, 'Aspose.Cells for Java v17.9'.

Tenga en cuenta que no puede indicar al Aspose.Cells for Java que cambie o elimine esta información de los documentos de salida.

{{% /alert %}}

### **Acceso a las propiedades del documento**

Aspose.Cells Las API admiten ambos tipos de propiedades de documentos, integradas y personalizadas. Aspose.Cells'[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase representa un archivo de Excel y, como un archivo de Excel, el[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) La clase puede contener varias hojas de trabajo, cada una representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) mientras que la colección de hojas de trabajo está representada por el[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)clase.

 Utilizar el[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)para acceder a las propiedades del documento del archivo como se describe a continuación.

-  Para acceder a las propiedades del documento incorporado, utilice[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
-  Para acceder a las propiedades del documento personalizado, use el[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

 Ambos[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) y[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) devolver una instancia de[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) . Esta colección contiene[**DocumentoPropiedad**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)objetos, cada uno de los cuales representa una única propiedad de documento integrada o personalizada.

 Queda a criterio de la solicitud cómo acceder a un inmueble, es decir; utilizando el índice o el nombre de la propiedad de la[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)como se demuestra en el siguiente ejemplo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

 los[**DocumentoPropiedad**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)class permite recuperar el nombre, valor y tipo de la propiedad del documento:

-  Para obtener el nombre de la propiedad, utilice[**DocumentoPropiedad.Nombre**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
-  Para obtener el valor de la propiedad, utilice[**DocumentoPropiedad.Valor**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentoPropiedad.Valor**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)devuelve el valor como un objeto.
-  Para obtener el tipo de propiedad, use[**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type) . Esto devuelve uno de los[**Tipo de propiedad**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType)valores de enumeración.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Adición o eliminación de propiedades de documentos personalizados**

Como describimos anteriormente al comienzo de este tema, los desarrolladores no pueden agregar o quitar propiedades integradas porque estas propiedades están definidas por el sistema, pero es posible agregar o quitar propiedades personalizadas porque están definidas por el usuario.

### **Adición de propiedades personalizadas**

 Aspose.Cells Las API han expuesto el[**agregar**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) método para el[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) class para agregar propiedades personalizadas a la colección. los[**agregar**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) agrega la propiedad al archivo de Excel y devuelve una referencia para la propiedad del nuevo documento como un[**DocumentoPropiedad**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)objeto.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Configuración de la propiedad personalizada "Enlace al contenido"**

 Para crear una propiedad personalizada vinculada al contenido de un rango determinado, llame al[**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String) ) método y pase el nombre de la propiedad y la fuente. Puede comprobar si una propiedad está configurada como vinculada a contenido utilizando el[**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent) propiedad. Además, también es posible obtener el rango de fuente usando el[**Fuente**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) propiedad de la[**DocumentoPropiedad**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)clase.

 Usamos una plantilla simple Microsoft archivo de Excel en el ejemplo. El libro de trabajo tiene un rango con nombre definido etiquetado**MiRango** que se refiere a un valor de celda.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Eliminación de propiedades personalizadas**

 Para eliminar propiedades personalizadas usando Aspose.Cells, llame al[**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) y pase el nombre de la propiedad del documento que se eliminará.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
