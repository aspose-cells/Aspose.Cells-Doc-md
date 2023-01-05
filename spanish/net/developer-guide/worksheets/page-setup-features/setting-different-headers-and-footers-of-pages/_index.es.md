---
title: Establecer diferentes encabezados y pies de página para diferentes páginas
type: docs
weight: 35
url: /es/net/setting-different-headers-and-footers-for-pages-to-Excel/
---
{{% alert color="primary" %}}

MS Excel admite la configuración de diferentes encabezados y pies de página para la primera página, las páginas impares y las páginas pares desde Excel 2007.
Aspose.Cells admite la misma función.

{{% /alert %}}

## **Configuración de diferentes encabezados y pies de página en MS Excel**

**![Configuración de diferentes encabezados y pies de página](difpage.png)**

1.  Hacer clic**Diseño de página > Imprimir títulos > Encabezado/Pie de página**.
1.  Controlar**Diferentes páginas pares e impares** o**Página de abeto diferente**.
1. Introduzca diferentes encabezados y pies de página.

## **Configuración de diferentes encabezados y pies de página con Aspose.Cells**

Aspose.Cells se comporta igual que Excel.
1.  Establece las banderas[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) y[PageSetup.IsHFDiffPrimero](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Introduzca diferentes encabezados y pies de página.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
