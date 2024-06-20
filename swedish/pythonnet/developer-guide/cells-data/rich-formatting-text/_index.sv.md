---
title: Åtkomst och uppdatering av delar av riktad text från cellen
linktitle: Riktad formateringstext
type: docs
weight: 40
url: /sv/python-net/access-and-update-the-portions-of-rich-text-of-cell/
description: Lär dig hur man får åtkomst till och uppdaterar delarna av riktad text i cellen genom Aspose.Cells for Python via .NET API.
keywords: Python Excel bibliotek, Python Åtkomst och uppdatera riktext av cell, Python Hämta riktext av cell, Python Redigera riktext av cell, Python Åtkomst riktext av cell, Python Uppdatera riktext av cell, Python Ändra riktext av cell.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET gör att du kan nå och uppdatera delarna av riktexten i cellen. För detta ändamål kan du använda [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) och [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list) metoder. Dessa metoder kommer att returnera och acceptera en array av [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) objekt som du kan använda för att nå och uppdatera olika egenskaper hos teckensnittet, som teckensnittsnamn, teckenfärg, fetstil, etc.

{{% /alert %}}

## **Åtkomst och uppdatering av delar av riktad text från cellen**

Följande kod visar hur man använder [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) och [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list) metoder med den [källa excelfilen](5112369.xlsx) som du kan ladda ner från den angivna länken. Källa excelfilen har riktext i cellen A1. Den har 3 delar och varje del har ett annat teckensnitt. Följande kodsnutt når dessa delar och uppdaterar den första delen med ett nytt teckensnittsnamn. Slutligen sparar den kalkylarket som [utdatorkelfil](5112366.xlsx). När du öppnar den hittar du att teckensnittet för den första delen av texten har ändrats till **"Arial"**.

### C#-kod för att nå och uppdatera delarna av riktext av cellen

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-UpdateRichTextCells-1.py" >}}

### Konsoloutput som genereras av provkoden

Här är konsolresultatet av den ovanstående kodprov med den [källa excelfilen](5112369.xlsx).

{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

