---
title: Documentos seguros PDF
type: docs
weight: 120
url: /es/python-net/secure-pdf-documents/
description: Aprenda cómo pasar las opciones de seguridad PDF al guardar hojas de cálculo en PDF con Aspose.Cells for Python via .NET API.
keywords: Python write security options to pdf, encrypt PDF document 
---
{{% alert color="primary" %}}

A veces, los desarrolladores necesitan trabajar con archivos cifrados PDF. Por ejemplo:

- Asegure los documentos con contraseñas de propietario y usuario para que no cualquiera pueda abrirlos.
- Establezca restricciones o permisos para el documento después de abrirlo. por ejemplo, restringir si el contenido del documento se puede imprimir o extraer.

Este artículo explica cómo pasar las opciones de seguridad PDF al guardar hojas de cálculo en PDF.

{{% /alert %}}

 Aspose.Cells for Python via .NET proporciona[**PdfSeguridadOpciones**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)para trabajar con seguridad. Puede configurar las contraseñas de propietario y usuario mientras guarda en PDF. Se requerirá la contraseña de propietario o de usuario para abrir el documento cifrado PDF para verlo.

- La contraseña del usuario puede ser nula o una cadena vacía, en este caso no se requerirá contraseña al usuario al abrir el documento PDF.
- Abrir el documento PDF con la contraseña de propietario correcta permite el acceso completo (sin ninguna restricción de acceso especificada) al documento.
- Abrir el documento PDF con la contraseña de usuario correcta (o abrir un documento que no tiene una contraseña de usuario) permite un acceso limitado según los permisos especificados.

El siguiente código de muestra describe cómo proteger archivos PDF con Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

 Si la hoja de cálculo contiene fórmulas, es mejor llamar[**Libro de trabajo.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de representarlo en PDF. Esto garantiza que los valores dependientes de la fórmula se recalculen y que los valores correctos se representen en PDF.

{{% /alert %}}
