---
title:  Inställ olika sidhuvuden och sidfötter för olika sidor 
type: docs
weight: 35
url: /sv/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Denna artikel ger exempel på kod som visar hur man programmässigt ställer in olika rubriker och sidfötter för Excel kalkylbladets sidsetup inställningar med Aspose.Cells för Python API et. Du kan ställa in rubriker och sidfötter för första sidan, udda sidor och jämna sidor.
keywords: Python Excel Library, Python ställ in excel rubrik och sidfot för första sidan, ställ in excel rubrik och sidfot för udda sidor i Python, ställ in excel rubrik och sidfot för jämna sidor med Python.
---

{{% alert color="primary" %}}

MS Excel stödjer inställning av olika sidhuvuden och sidfötter för första sidan, udda sidor och jämna sidor sedan Excel 2007.
Aspose.Cells för Python via .NET stöder samma funktion.

{{% /alert %}}

## **Hur man ställer in olika rubriker och sidfötter i MS Excel**

**![Inställning av olika sidhuvuden och sidfötter](difpage.png)**

1. Klicka på **Sidlayout > Sidhuvud/fot > Sidhuvud/sidfot**.
1. Markera **Olika udda och jämna sidor** eller **Olika första sidan**.
1. Ange olika sidhuvuden och sidfötter.

## **Hur man ställer in olika rubriker och sidfötter med Aspose.Cells för Python Excel Library**

Aspose.Cells för Python via .NET fungerar som Excel.
1. Sätter flaggorna [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) och [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. Ange olika sidhuvuden och sidfötter.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
{{< app/cells/assistant language="python-net" >}}
