---
title: Documentos seguros PDF
type: docs
weight: 260
url: /es/java/secure-pdf-documents/
description: Proteja archivos PDF mientras convierte desde archivos de Excel. Este artículo demuestra cómo generar un archivo PDF seguro desde Excel con Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

A veces, los desarrolladores necesitan trabajar con archivos cifrados PDF. Por ejemplo:

- Asegure los documentos con contraseñas de propietario y usuario para que no cualquiera pueda abrirlos.
- Establezca restricciones o permisos para el documento después de abrirlo. por ejemplo, restringir si el contenido del documento se puede imprimir o extraer.

Este artículo explica cómo pasar las opciones de seguridad PDF al guardar hojas de cálculo en PDF.

{{% /alert %}}

 Aspose.Cells proporciona[**PdfSeguridadOpciones**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/)para trabajar con seguridad. Puede configurar las contraseñas de propietario y usuario mientras guarda en PDF. Se requerirá la contraseña de propietario o de usuario para abrir el documento cifrado PDF para verlo.

- La contraseña del usuario puede ser nula o una cadena vacía, en este caso no se requerirá contraseña al usuario al abrir el documento PDF.
- Abrir el documento PDF con la contraseña de propietario correcta permite el acceso completo (sin ninguna restricción de acceso especificada) al documento.
- Abrir el documento PDF con la contraseña de usuario correcta (o abrir un documento que no tiene una contraseña de usuario) permite un acceso limitado según los permisos especificados.

El siguiente código de muestra describe cómo crear archivos PDF seguros con Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Si la hoja de cálculo contiene fórmulas, es mejor llamar[**Libro de trabajo.calcularFórmula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()justo antes de representarlo en PDF. Esto garantiza que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en PDF.

{{% /alert %}}
