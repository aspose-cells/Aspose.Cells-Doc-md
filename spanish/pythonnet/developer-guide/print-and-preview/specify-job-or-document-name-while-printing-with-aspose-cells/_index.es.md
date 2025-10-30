---
title: Especificar nombre de trabajo o documento al imprimir con Aspose.Cells
type: docs
weight: 270
url: /es/python-net/specify-job-or-document-name-while-printing-with-aspose-cells/
---

{{% alert color="primary" %}}

Puedes especificar el nombre del trabajo o del documento al imprimir tu libro de trabajo o hoja de trabajo usando los objetos WorkbookRender o SheetRender. Aspose.Cells para Python via .NET proporciona los métodos WorkbookRender.ToPrinter(printerName, jobName) y SheetRender.ToPrinter(printerName, jobName) que puedes usar para especificar el nombre del trabajo al imprimir tu libro o hoja de trabajo.

{{% /alert %}}

## **Especificar el nombre del trabajo o del documento al imprimir con Aspose.Cells para Python via .NET**

El código de muestra carga el archivo de Excel de origen y luego lo envía a la impresora especificando el nombre de trabajo o documento utilizando los métodos WorkbookRender.ToPrinter(nombreImpresora, nombreTrabajo) y SheetRender.ToPrinter(nombreImpresora, nombreTrabajo).

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SpecifyJobNameWhilePrinting.py" >}}
{{< app/cells/assistant language="python-net" >}}
