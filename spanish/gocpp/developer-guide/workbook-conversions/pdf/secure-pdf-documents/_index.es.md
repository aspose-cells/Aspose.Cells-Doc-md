---
title: Proteger documentos PDF con Golang mediante C++
linktitle: Documentos PDF seguros
type: docs
weight: 120
url: /es/go-cpp/secure-pdf-documents/
description: Aprende cómo proteger documentos PDF con contraseñas de propietario y usuario usando Aspose.Cells con Golang mediante C++.
---

{{% alert color="primary" %}}

A veces, los desarrolladores necesitan trabajar con archivos PDF encriptados. Por ejemplo:

- Asegurar los documentos con contraseñas de propietario y usuario para que no cualquier persona pueda abrirlo.
- Establecer restricciones o permisos al documento después de que se abra. Por ejemplo: restringir si el contenido del documento puede imprimirse o extraerse.

Este artículo explica cómo pasar opciones de seguridad en PDF al guardar hojas de cálculo en PDF.

{{% /alert %}}

Aspose.Cells proporciona [**PdfSecurityOptions**](https://reference.aspose.com/cells/go-cpp/pdfsecurityoptions/) para trabajar con seguridad. Puede establecer contraseñas de propietario y de usuario al guardar en PDF. La contraseña de propietario o de usuario será necesaria para abrir el documento PDF encriptado para su visualización.

- La contraseña de usuario puede ser nula o una cadena vacía, en este caso no se requerirá ninguna contraseña del usuario al abrir el documento PDF.
- Abrir el documento PDF con la contraseña de propietario correcta permite acceso completo (sin restricciones de acceso especificadas) al documento.
- Abrir el documento PDF con la contraseña de usuario correcta (o abrir un documento que no tenga una contraseña de usuario) permite acceso limitado, según los permisos especificados.

El código de muestra a continuación describe cómo asegurar PDFs con Aspose.Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SecurePdfDocuments.go" >}}
{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) justo antes de renderizarla a PDF. Esto asegura que los valores dependientes de fórmulas se recalculen y se rendericen los valores correctos en el PDF.

{{% /alert %}}
