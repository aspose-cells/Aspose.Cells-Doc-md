---
title: Seguro PDF Documentos
type: docs
weight: 120
url: /es/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

A veces, los desarrolladores necesitan trabajar con archivos cifrados PDF. Por ejemplo, necesitan proteger los documentos con contraseñas de usuario y propietario para que no cualquiera pueda abrirlos, o desean restringir si el contenido del documento se puede imprimir o extraer.

Este artículo explica cómo pasar las opciones de seguridad PDF al guardar hojas de cálculo en PDF.

{{% /alert %}}

 Aspose.Cells proporciona el[**Aspose.Cells.Rendering.PdfSecurity**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity) espacio de nombres para trabajar con seguridad. El código de muestra a continuación describe cómo proteger archivos PDF con Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

 Si la hoja de cálculo contiene fórmulas, es mejor llamar[**Libro de trabajo. Calcular fórmula ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)justo antes de representarlo en PDF. Esto garantiza que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en PDF.

{{% /alert %}}
