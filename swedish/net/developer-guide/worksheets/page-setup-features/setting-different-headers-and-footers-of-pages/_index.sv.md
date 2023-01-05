---
title: Ställa in olika sidhuvuden och sidfötter för olika sidor
type: docs
weight: 35
url: /sv/net/setting-different-headers-and-footers-for-pages-to-Excel/
---
{{% alert color="primary" %}}

MS Excel stöder inställning av olika sidhuvuden och sidfötter för första sidan, udda sidor och jämna sidor sedan Excel 2007.
Aspose.Cells stöder samma funktion.

{{% /alert %}}

## **Ställa in olika sidhuvuden och sidfötter i MS Excel**

**![Ställa in olika sidhuvuden och sidfötter](difpage.png)**

1.  Klick**sidlayout > Skriv ut titlar > Sidhuvud/sidfot**.
1.  Kolla upp**Olika udda och jämna sidor** eller**Annan gransida**.
1. Ange olika sidhuvuden och sidfötter.

## **Ställa in olika sidhuvuden och sidfötter med Aspose.Cells**

Aspose.Cells fungerar på samma sätt som Excel.
1.  Sätter flaggorna[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) och[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Ange olika sidhuvuden och sidfötter.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
