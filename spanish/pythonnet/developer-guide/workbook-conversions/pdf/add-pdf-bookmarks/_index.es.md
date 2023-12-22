---
title: Agregar PDF Marcadores
type: docs
weight: 10
url: /es/python-net/add-pdf-bookmarks/
description: Aprenda a agregar marcas de libros en PDF con Aspose.Cells for Python via .NET API.
keywords: Python add pdf bookmarks, add pdf book marks Pyton via NET, insert pdf bookmarks
---
{{% alert color="primary" %}}

Este artículo proporciona información sobre cómo insertar marcadores PDF al convertir una hoja de cálculo a PDF.

Aspose.Cells for Python via .NET le permite agregar marcadores sobre la marcha. Los marcadores PDF pueden mejorar drásticamente la navegabilidad de documentos largos. Al agregar enlaces de marcadores al documento PDF, puede tener un control preciso sobre la vista exacta que desea, no está limitado a vincular a una página. Puede configurar la vista precisa colocando la página de destino y luego creando el marcador.

{{% /alert %}}

Consulte el siguiente código de muestra para saber cómo agregar marcadores PDF. El código genera un libro de trabajo simple, especifica PDF marcadores con ubicaciones de destino y genera el archivo PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AddPDFBookmarks-1.py" >}}

{{% alert color="primary" %}}

 Si su hoja de cálculo tiene fórmulas, lo mejor es llamar[**Libro de trabajo.calcular_fórmula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizar la hoja de cálculo al formato PDF. Al hacerlo, se garantizará que los valores dependientes de la fórmula se actualicen y se representen correctamente en PDF.

{{% /alert %}}
