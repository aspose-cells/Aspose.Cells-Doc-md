---
title: Configuración de diferentes encabezados y pies de página para diferentes páginas
type: docs
weight: 35
url: /es/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Este artículo proporciona un código de muestra que muestra cómo establecer programáticamente varios encabezados y pies de página de la configuración de Página de la Hoja de Excel utilizando la API de Aspose.Cells for Python. Puedes establecer los encabezados y pies de página para la primera página, páginas impares y páginas pares.
keywords: Biblioteca de Excel de Python, establecer encabezado y pie de página en Excel, establecer encabezado y pie de página de la primera página en Excel, establecer encabezado y pie de página de páginas impares en Excel, establecer encabezado y pie de página de páginas pares en Excel mediante Python.
---

{{% alert color="primary" %}}

MS Excel admite establecer diferentes encabezados y pies de página para la primera página, páginas impares y páginas pares desde Excel 2007.
Aspose.Cells para Python via .NET soporta la misma funcionalidad.

{{% /alert %}}

## **Cómo establecer encabezados y pies de página diferentes en MS Excel**

**![Configuración de diferentes encabezados y pies de página](difpage.png)**

1. Haz clic en **diseño de página > títulos de impresión > encabezado/pie de página**.
1. Marca **Páginas impares y pares diferentes** o **Diferente primera página**.
1. Ingrese encabezados y pies de página diferentes.

## **Cómo establecer encabezados y pies de página diferentes con la Biblioteca de Excel Aspose.Cells para Python**

Aspose.Cells para Python via .NET se comporta de la misma manera que Excel.
1. Establece los indicadores [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) y [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. Ingrese encabezados y pies de página diferentes.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
