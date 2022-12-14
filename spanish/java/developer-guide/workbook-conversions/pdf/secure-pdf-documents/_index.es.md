---
title: Documentos PDF seguros
type: docs
weight: 260
url: /es/java/secure-pdf-documents/
description: Proteja los archivos PDF mientras los convierte desde archivos de Excel. Este artículo demuestra cómo generar un archivo PDF seguro desde Excel con Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

A veces, los desarrolladores necesitan trabajar con archivos PDF encriptados. Por ejemplo, necesitan proteger los documentos con contraseñas de usuario y propietario para que no cualquiera pueda abrirlos, o desean restringir si el contenido del documento se puede imprimir o extraer.

Este artículo explica cómo pasar las opciones de seguridad de PDF al guardar hojas de cálculo en PDF.

{{% /alert %}} 

 Aspose.Cells Las API proporcionan la[**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSecurityOptions)clase para trabajar con la seguridad del formato de archivo PDF. El siguiente código de ejemplo describe cómo crear archivos PDF protegidos con Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Si la hoja de cálculo contiene fórmulas, es mejor llamar[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) justo antes de convertirlo en PDF. Esto garantiza que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en el PDF.

{{% /alert %}}
