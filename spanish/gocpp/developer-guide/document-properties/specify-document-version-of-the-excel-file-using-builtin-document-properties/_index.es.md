---
title: Especificar la versión del documento del archivo Excel usando propiedades incorporadas del documento con Golang a través de C++
linktitle: Especificar la versión del documento
type: docs
weight: 20
url: /es/go-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Aprende cómo especificar la versión del documento de un archivo Excel usando propiedades de documento integradas con Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Puedes cambiar el **Número de versión** de un archivo Excel haciendo clic derecho en el archivo y seleccionando Propiedades > Detalles y editando el campo **Número de versión**. Por favor, usa la propiedad [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getdocumentversion/) para cambiarlo programáticamente usando las APIs de Aspose.Cells.

## **Especificar la versión del documento del archivo de Excel mediante propiedades de documento integradas**

El siguiente ejemplo de código crea un libro de trabajo y cambia sus propiedades de documento integradas que incluyen Título, Autor y Número de versión. Por favor, mira el [archivo Excel de salida](64716811.xlsx) generado por el código y la captura que muestra el número de versión modificado mediante la propiedad [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getdocumentversion/).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyDocumentVersionOfTheExcelFileUsingBuiltinDocumentProperties.go" >}}
