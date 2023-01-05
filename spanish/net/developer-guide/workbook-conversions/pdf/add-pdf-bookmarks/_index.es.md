---
title: Añadir PDF Favoritos
type: docs
weight: 10
url: /es/net/add-pdf-bookmarks/
---
{{% alert color="primary" %}}

Este artículo proporciona información sobre cómo insertar marcadores PDF al convertir una hoja de cálculo a PDF.

Aspose.Cells le permite agregar marcadores sobre la marcha. Los marcadores PDF pueden mejorar drásticamente la navegabilidad de documentos largos. Al agregar enlaces de marcadores al documento PDF, puede tener un control preciso sobre la vista exacta que desea, no está limitado a vincular a una página. Puede configurar la vista precisa colocando la página de destino y luego crear el marcador.

{{% /alert %}}

Consulte el siguiente código de ejemplo para averiguar cómo agregar marcadores PDF. El código genera un libro de trabajo simple, especifica PDF marcadores con ubicaciones de destino y genera el archivo PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddPDFBookmarks-1.cs" >}}

{{% alert color="primary" %}}

Si su hoja de cálculo tiene fórmulas, es mejor llamar[**Workbook.CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) justo antes de renderizar la hoja de cálculo al formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se actualicen y representen correctamente en PDF.

{{% /alert %}}
