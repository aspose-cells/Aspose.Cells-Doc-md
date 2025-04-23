---
title: Agregar marcadores de posición en PDF
type: docs
weight: 10
url: /es/net/add-pdf-bookmarks/
---

{{% alert color="primary" %}}

Este artículo proporciona información sobre cómo insertar marcadores de posición en PDF al convertir una hoja de cálculo a PDF.

Aspose.Cells te permite agregar marcadores sobre la marcha. Los marcadores PDF pueden mejorar notablemente la navegabilidad de documentos extensos. Al añadir enlaces de marcadores al documento PDF, tienes un control preciso sobre la vista exacta que deseas, no estás limitado a enlazar a una página. Puedes configurar la vista precisa posicionando la página objetivo y luego crear el marcador.

{{% /alert %}}

Por favor, consulta el siguiente código de ejemplo para saber cómo agregar marcadores PDF. El código genera un libro de trabajo sencillo, especifica marcadores PDF con ubicaciones de destino y genera el archivo PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddPDFBookmarks-1.cs" >}}

{{% alert color="primary" %}}

Si tu hoja de cálculo tiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) justo antes de renderizar la hoja de cálculo en formato PDF. Haciendo esto garantizarás que los valores dependientes de las fórmulas se actualicen y se representen correctamente en PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
