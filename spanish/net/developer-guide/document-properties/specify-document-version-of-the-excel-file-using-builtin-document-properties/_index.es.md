---
title: Especificar la versión de documento del archivo de Excel usando las propiedades de documento integradas
type: docs
weight: 20
url: /es/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/
---

## **Escenarios de uso posibles**

Puede cambiar el **número de versión** del archivo de Excel haciendo clic con el botón derecho en el archivo y luego seleccionando Propiedades > Detalles y luego editando el campo **Número de versión**. Utilice la propiedad [**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/documentversion) para cambiarlo programáticamente usando las APIs de Aspose.Cells.

## **Especificar la versión del documento del archivo de Excel mediante propiedades de documento integradas**

El siguiente código de muestra crea un libro de trabajo y cambia sus propiedades de documento integradas que incluyen Título, Autores y Número de versión. Consulte el [archivo de Excel de salida](64716811.xlsx) generado por el código y la captura de pantalla que muestra el **Número de versión** modificado por la propiedad [**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/documentversion).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SpecifyDocumentVersionOfExcelFile.cs" >}}
