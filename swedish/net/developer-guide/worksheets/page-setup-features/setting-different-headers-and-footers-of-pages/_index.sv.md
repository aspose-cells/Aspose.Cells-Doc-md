---
title:  Inställ olika sidhuvuden och sidfötter för olika sidor 
type: docs
weight: 35
url: /sv/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Den här artikeln tillhandahåller exempelkod som visar hur man programmatiskt ställer in olika sidhuvuden och sidfötter för Excel kalkylbladets Page Setup inställningar med hjälp av C# biblioteket och .NET API. Du kan ställa in sidhuvuden och sidfötter för första sidan, udda sidor och jämna sidor.
keywords: ställ in sidhuvud och sidfot i excel första sida c#, ställ in sidhuvud och sidfot i excel udda sidor c#, ställ in sidhuvud och sidfot i excel jämna sidor c#
---

{{% alert color="primary" %}}

MS Excel stödjer inställning av olika sidhuvuden och sidfötter för första sidan, udda sidor och jämna sidor sedan Excel 2007.
Aspose.Cells stöder samma funktion.

{{% /alert %}}

## **Inställning av olika sidhuvuden och sidfötter i MS Excel**

**![Inställning av olika sidhuvuden och sidfötter](difpage.png)**

1. Klicka på **Sidlayout > Sidhuvud/fot > Sidhuvud/sidfot**.
1. Markera **Olika udda och jämna sidor** eller **Olika första sidan**.
1. Ange olika sidhuvuden och sidfötter.

## **Inställning av olika sidhuvuden och sidfötter med Aspose.Cells**

Aspose.Cells beter sig på samma sätt som Excel.
1. Ange flaggorna [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) och [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Ange olika sidhuvuden och sidfötter.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
{{< app/cells/assistant language="csharp" >}}
