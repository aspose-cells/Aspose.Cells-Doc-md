---
title: Obtenga el número de versión de la aplicación que creó el documento de Excel
type: docs
weight: 150
url: /es/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---
{{% alert color="primary" %}}

 A menudo, necesita saber el número de versión de la aplicación que creó un documento de Excel Microsoft. Aspose.Cells proporciona el[**Libro de trabajo.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) propiedad para este fin.

{{% /alert %}}

 El siguiente código de ejemplo demuestra el uso de la[**Libro de trabajo.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)propiedad. Carga archivos de Excel creados con Microsoft Excel 2003, 2007, 2010 y 2013 e imprime el número de versión de la aplicación que creó estos documentos de Excel.

Para su referencia, a continuación se muestra la salida de la consola que crea el código de muestra.

{{< highlight "java" >}}

Excel 2003 XLS Version: 726502

Excel 2007 XLS Version: 786432

Excel 2010 XLS Version: 917504

Excel 2013 XLS Version: 983040

Excel 2007 XLSX Version: 12.0000

Excel 2010 XLSX Version: 14.0300

Excel 2013 XLSX Version: 15.0300

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetVersionNumberofApplication-GetVersionNumberofApplication.java" >}}
