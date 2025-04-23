---
title: Documentos PDF seguros
type: docs
weight: 260
url: /es/java/secure-pdf-documents/
description: Asegure archivos PDF al convertir desde archivos de Excel. Este artículo demuestra cómo generar un archivo PDF seguro desde Excel con la API Aspose.Cells for Java.
keywords: documentos pdf seguros en java, documentos pdf seguros, excel a pdf seguro, excel a pdf seguro en java, convertir excel a pdf seguro, convertir excel a pdf seguro en java, convertir excel a pdf protegido con contraseña, convertir excel a pdf protegido con contraseña en java, excel a pdf protegido con contraseña en java, excel a pdf protegido con contraseña
---

{{% alert color="primary" %}}

A veces, los desarrolladores necesitan trabajar con archivos PDF encriptados. Por ejemplo:

- Asegurar los documentos con contraseñas de propietario y usuario para que no cualquier persona pueda abrirlo.
- Establecer restricciones o permisos al documento después de que se abra. Por ejemplo: restringir si el contenido del documento puede imprimirse o extraerse.

Este artículo explica cómo pasar opciones de seguridad en PDF al guardar hojas de cálculo en PDF.

{{% /alert %}}

Aspose.Cells proporciona [**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/) para trabajar con seguridad. Puede establecer contraseñas de propietario y usuario al guardar en PDF. Se requerirá la contraseña de propietario o usuario para abrir el documento PDF encriptado para verlo.

- La contraseña de usuario puede ser nula o una cadena vacía, en este caso no se requerirá ninguna contraseña del usuario al abrir el documento PDF.
- Abrir el documento PDF con la contraseña de propietario correcta permite acceso completo (sin restricciones de acceso especificadas) al documento.
- Abrir el documento PDF con la contraseña de usuario correcta (o abrir un documento que no tenga una contraseña de usuario) permite acceso limitado, según los permisos especificados.

El código de muestra a continuación describe cómo crear archivos PDF seguros con la API Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) justo antes de convertirla a PDF. Esto asegura que se recalculen los valores dependientes de las fórmulas y que los valores correctos se representen en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
