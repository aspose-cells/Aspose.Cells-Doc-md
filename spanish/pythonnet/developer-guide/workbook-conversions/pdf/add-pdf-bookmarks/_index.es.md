---
title: Agregar marcadores de posición en PDF
type: docs
weight: 10
url: /es/python-net/add-pdf-bookmarks/
description: Aprenda cómo agregar marcadores de PDF con la API de Aspose.Cells para Python via .NET.
keywords: Agregar marcadores de PDF con Python, añadir marcas de libro PDF Python via NET, insertar marcadores de PDF
---

{{% alert color="primary" %}}

Este artículo proporciona información sobre cómo insertar marcadores de posición en PDF al convertir una hoja de cálculo a PDF.

Aspose.Cells para Python via .NET te permite agregar marcadores sobre la marcha. Los marcadores de PDF pueden mejorar drásticamente la navegabilidad de documentos largos. Al agregar enlaces de marcadores al documento PDF, puedes tener un control preciso sobre la vista exacta que deseas, no estás limitado a enlazar a una página. Puedes configurar la vista precisa posicionando la página de destino y luego crear el marcador.

{{% /alert %}}

Por favor, consulta el siguiente código de ejemplo para saber cómo agregar marcadores PDF. El código genera un libro de trabajo sencillo, especifica marcadores PDF con ubicaciones de destino y genera el archivo PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AddPDFBookmarks-1.py" >}}

{{% alert color="primary" %}}

Si tu hoja de cálculo tiene fórmulas, es mejor llamar a [**Workbook.calculate_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizar la hoja de cálculo en formato PDF. Haciendo esto garantizarás que los valores dependientes de las fórmulas se actualicen y se representen correctamente en PDF.

{{% /alert %}}
