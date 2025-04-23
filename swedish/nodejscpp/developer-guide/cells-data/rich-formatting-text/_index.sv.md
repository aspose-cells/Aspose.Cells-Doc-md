---
title: Åtkomst och uppdatering av delar av riktad text från cellen
linktitle: Riktad formateringstext
type: docs
weight: 40
url: /sv/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Lär dig hur man får åtkomst till och uppdaterar delar av rik text i cellen genom Aspose.Cells for Node.js via C++ API.
keywords: Kom åt och uppdatera rik text i cell, Få rik text i cell, Redigera rik text i cell, Kom åt rik text i cell, Uppdatera rik text i cell, Ändra rik text i cell
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ tillåter dig att få åtkomst till och uppdatera delar av den rika texten i cellen. För detta kan du använda [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) och [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-)-metoderna. Dessa metoder returnerar och accepterar en array av [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)-objekt som du kan använda för att få åtkomst till och uppdatera olika egenskaper hos teckensnittet som teckensnittnamn, teckensnittfärg, fetstil, etc.

{{% /alert %}}

## **Åtkomst och uppdatering av delar av riktad text från cellen**

Följande kod demonstrerar användningen av [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) och [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) metoder med [källa Excel-fil](5112369.xlsx) som du kan ladda ner från länken. Källfilen har rik text i cellen A1. Den har 3 delar, och varje del har ett annat teckensnitt. Följande kodsnutt når dessa delar och uppdaterar den första delen med ett nytt teckensnittsnamn. Slutligen sparar den arbetsboken som [utgångs Excel-fil](5112366.xlsx). När du öppnar den, kommer du att se att teckensnittet för den första delen av texten har ändrats till **"Arial"**.

### Nodejs kod för att få åtkomst till och uppdatera delar av rik text i cellen

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "UpdateRichTextCells-1.js" >}}

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

