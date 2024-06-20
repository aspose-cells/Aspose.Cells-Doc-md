---
title: Documentos PDF seguros
type: docs
weight: 120
url: /es/python-net/secure-pdf-documents/
description: Aprende cómo pasar opciones de seguridad en PDF al guardar hojas de cálculo en PDF con Aspose.Cells para Python via .NET API.
keywords: Python escribe opciones de seguridad en PDF, encripta documento PDF 
---

{{% alert color="primary" %}}

A veces, los desarrolladores necesitan trabajar con archivos PDF encriptados. Por ejemplo:

- Asegurar los documentos con contraseñas de propietario y usuario para que no cualquier persona pueda abrirlo.
- Establecer restricciones o permisos al documento después de que se abra. Por ejemplo: restringir si el contenido del documento puede imprimirse o extraerse.

Este artículo explica cómo pasar opciones de seguridad en PDF al guardar hojas de cálculo en PDF.

{{% /alert %}}

Aspose.Cells para Python via .NET proporciona [**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) para trabajar con la seguridad. Puedes establecer contraseñas de propietario y usuario al guardar en PDF. La contraseña de propietario o de usuario será necesaria para abrir el documento PDF encriptado para verlo.

- La contraseña de usuario puede ser nula o una cadena vacía, en este caso no se requerirá ninguna contraseña del usuario al abrir el documento PDF.
- Abrir el documento PDF con la contraseña de propietario correcta permite acceso completo (sin restricciones de acceso especificadas) al documento.
- Abrir el documento PDF con la contraseña de usuario correcta (o abrir un documento que no tenga una contraseña de usuario) permite acceso limitado, según los permisos especificados.

El código de muestra a continuación describe cómo asegurar PDFs con Aspose.Cells para Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizarla en PDF. Esto asegura que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
