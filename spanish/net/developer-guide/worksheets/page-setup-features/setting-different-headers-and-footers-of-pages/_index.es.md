---
title: Configuración de diferentes encabezados y pies de página para diferentes páginas
type: docs
weight: 35
url: /es/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Este artículo proporciona un código de ejemplo que muestra cómo configurar programáticamente varios encabezados y pies de página de la configuración de la página de la hoja de cálculo de Excel utilizando la Biblioteca de C# y la API .NET. Puedes configurar los encabezados y pies de página para la primera página, páginas impares y páginas pares.
keywords: establecer encabezado pie de página excel primera página c#, establecer encabezado pie de página excel páginas impares c#, establecer encabezado pie de página excel páginas pares c#
---

{{% alert color="primary" %}}

MS Excel admite establecer diferentes encabezados y pies de página para la primera página, páginas impares y páginas pares desde Excel 2007.
Aspose.Cells admite la misma función.

{{% /alert %}}

## **Configuración de diferentes encabezados y pies de página en MS Excel**

**![Configuración de diferentes encabezados y pies de página](difpage.png)**

1. Haz clic en **diseño de página > títulos de impresión > encabezado/pie de página**.
1. Marca **Páginas impares y pares diferentes** o **Diferente primera página**.
1. Ingrese encabezados y pies de página diferentes.

## **Configuración de diferentes encabezados y pies de página con Aspose.Cells**

Aspose.Cells se comporta igual que Excel.
1. Establece las banderas [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) y [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Ingrese encabezados y pies de página diferentes.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
