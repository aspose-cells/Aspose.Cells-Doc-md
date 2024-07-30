---
title:  Inställ olika sidhuvuden och sidfötter för olika sidor 
type: docs
weight: 35
url: /sv/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Den här artikeln ger exempelkod som visar hur man programmatiskt ställer in olika header och footers av Excel arkets Siduppställningsinställningar med hjälp av Aspose.Cells för Python API. Du kan ställa in headers och footers för första sidan, udda sidor och jämna sidor.
keywords: Python Excel bibliotek, Python ställ in excel header footer första sidan, ställ in excel header footer udda sidor i Python, ställ in excel header footer jämna sidor med Python.
---

{{% alert color="primary" %}}

MS Excel stödjer inställning av olika sidhuvuden och sidfötter för första sidan, udda sidor och jämna sidor sedan Excel 2007.
Aspose.Cells för Python via .NET stöder samma funktion.

{{% /alert %}}

## **Hur man ställer in olika sidhuvuden och sidfotter i MS Excel**

**![Inställning av olika sidhuvuden och sidfötter](difpage.png)**

1. Klicka på **Sidlayout > Sidhuvud/fot > Sidhuvud/sidfot**.
1. Markera **Olika udda och jämna sidor** eller **Olika första sidan**.
1. Ange olika sidhuvuden och sidfötter.

## **Hur man ställer in olika sidhuvuden och sidfotter med Aspose.Cells för Python Excel Library**

Aspose.Cells för Python via .NET beter sig på samma sätt som Excel.
1. Ställer in flaggorna [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) och [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. Ange olika sidhuvuden och sidfötter.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
