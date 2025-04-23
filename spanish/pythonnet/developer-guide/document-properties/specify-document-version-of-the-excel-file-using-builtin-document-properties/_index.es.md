---
title: Especificar la versión de documento del archivo de Excel usando las propiedades de documento integradas
type: docs
weight: 20
url: /es/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/
---

## **Escenarios de uso posibles**

Puedes cambiar el **Número de versión** del archivo de Excel haciendo clic derecho en el archivo y seleccionando Propiedades > Detalles y luego editando el campo **Número de versión**. Utiliza la propiedad [**BuiltInDocumentPropertyCollection.document_version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/document_version) para cambiarlo de forma programática usando las API de Aspose.Cells para Python via .NET.

## **Especificar la versión del documento del archivo de Excel mediante propiedades de documento integradas**

El siguiente código de muestra crea un libro de trabajo y cambia sus propiedades de documento integradas que incluyen Título, Autores y Número de versión. Consulte el [archivo de Excel de salida](64716811.xlsx) generado por el código y la captura de pantalla que muestra el **Número de versión** modificado por la propiedad [**BuiltInDocumentPropertyCollection.document_version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/document_version).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SpecifyDocumentVersionOfExcelFile.py" >}}

