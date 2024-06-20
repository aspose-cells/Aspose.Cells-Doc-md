---
title: Especificar la versión de documento del archivo de Excel usando las propiedades de documento integradas
type: docs
weight: 20
url: /es/java/specify-document-version-of-the-excel-file-using-builtin-document-properties/
---

## **Escenarios de uso posibles**

Puede cambiar el *número de versión* del archivo de Excel haciendo clic derecho en el archivo y luego seleccionando *Propiedades > Detalles* y luego editando el campo *número de versión*. Por favor, use la propiedad [**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#DocumentVersion) para cambiarla programáticamente utilizando las APIs de Aspose.Cells.

## **Especificar la versión del documento del archivo de Excel mediante propiedades de documento integradas**

El siguiente código de ejemplo crea un libro de trabajo y cambia sus propiedades de documento integradas que incluyen *Título*, *Autores* y *Número de versión*. Por favor, consulte el archivo de Excel de salida (64716836.xlsx) generado por el código y la captura de pantalla que muestra el *Número de versión* modificado por la propiedad [**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#DocumentVersion).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SpecifyDocumentVersionOfExcelFile.java" >}}
