---
title: Documentos PDF seguros
type: docs
weight: 120
url: /es/net/secure-pdf-documents/
---

{{% alert color="primary" %}}

A veces, los desarrolladores necesitan trabajar con archivos PDF encriptados. Por ejemplo:

- Asegurar los documentos con contraseñas de propietario y usuario para que no cualquier persona pueda abrirlo.
- Establecer restricciones o permisos al documento después de que se abra. Por ejemplo: restringir si el contenido del documento puede imprimirse o extraerse.

Este artículo explica cómo pasar opciones de seguridad en PDF al guardar hojas de cálculo en PDF.

{{% /alert %}}

Aspose.Cells proporciona [**PdfSecurityOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) para trabajar con seguridad. Puede establecer contraseñas de propietario y usuario al guardar en PDF. Se requerirá la contraseña de propietario o usuario para abrir el documento PDF encriptado para verlo.

- La contraseña de usuario puede ser nula o una cadena vacía, en este caso no se requerirá ninguna contraseña del usuario al abrir el documento PDF.
- Abrir el documento PDF con la contraseña de propietario correcta permite acceso completo (sin restricciones de acceso especificadas) al documento.
- Abrir el documento PDF con la contraseña de usuario correcta (o abrir un documento que no tenga una contraseña de usuario) permite acceso limitado, según los permisos especificados.

El código de muestra a continuación describe cómo asegurar PDFs con Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de renderizarla en PDF. Esto asegura que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
