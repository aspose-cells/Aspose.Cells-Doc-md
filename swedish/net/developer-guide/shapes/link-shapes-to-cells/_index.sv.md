---
title: Hur man länkar Excel former till kalkylbladsceller
linktitle: Länka Excel former till celler
type: docs
description: "Hur man länkar Excel former till kalkylbladsceller"
weight: 3300
url: /sv/net/link-shapes-to-cells/
---

{{% alert color="primary" %}}

Ibland behöver du visa innehållet i en kalkylbladcells i en form, textruta eller diagramdel. Ibland, när data i en cell eller ett cellområde ändras, måste du synkronisera cellinnehållet med innehållet i en form, textruta eller diagramdel. För att göra detta kan du länka en form, textruta eller diagramdel till cellerna som innehåller de data du vill visa.

{{% /alert %}}

## Hur man länkar former till celler i Ms Excel

Följande figur visar hur man ställer in en länkad cell för en form.

![todo:image_alt_text](link-shapes-to-cells-1.png)

1. Markera en form. Formelfältet är vanligtvis tomt.

2. Ange formeln för formen, till exempel "=A1"

## Hur man länkar former till celler i Aspose.Cells

Följande kod demonstrerar hur man använder Aspose.Cells-biblioteket för att ställa in en länk för en form eller textruta för att dynamiskt visa cellinnehåll.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-1.cs"  >}}

## Avancerad användning

Om du vill att formens text ska bestå av två eller fler celler, eller om du vill välja det önskade innehållet baserat på ett formel, kanske ovanstående exempel inte passar dina behov. I så fall behöver du göra något mer avancerat. Du måste först placera formeln som producerar det önskade resultatet i en cell, och sedan länka formen till cellen som innehåller formeln.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-2.cs"  >}}

{{< app/cells/assistant language="csharp" >}}
