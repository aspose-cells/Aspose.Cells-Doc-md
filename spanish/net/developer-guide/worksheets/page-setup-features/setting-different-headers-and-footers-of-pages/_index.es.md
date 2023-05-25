---
title: Establecer diferentes encabezados y pies de página para diferentes páginas
type: docs
weight: 35
url: /es/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Este artículo proporciona un código de muestra que muestra cómo establecer mediante programación varios encabezados y pies de página de la configuración de configuración de página de la hoja de cálculo de Excel usando la biblioteca C# y .NET API. Puede establecer los encabezados y pies de página para la primera página, las páginas impares y las páginas pares.
keywords: set excel header footer first page c#, set excel header footer odd pages c#, set excel header footer even pages c#
---
{{% alert color="primary" %}}

MS Excel admite la configuración de diferentes encabezados y pies de página para la primera página, las páginas impares y las páginas pares desde Excel 2007.
Aspose.Cells admite la misma función.

{{% /alert %}}

##  **Configuración de diferentes encabezados y pies de página en MS Excel**

**![Configuración de diferentes encabezados y pies de página](difpage.png)**

1. Haga clic en *diseño de página > Imprimir títulos > Encabezado/Pie de página**.
1.  Controlar**Diferentes páginas pares e impares** o *Diferente página de abeto**.
1. Introduzca diferentes encabezados y pies de página.

##  **Configuración de diferentes encabezados y pies de página con Aspose.Cells**

Aspose.Cells se comporta igual que Excel.
1.  Establece las banderas[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) y[PageSetup.IsHFDiffPrimero](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Introduzca diferentes encabezados y pies de página.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
