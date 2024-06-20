---
title: Åtkomst och uppdatering av delar av riktad text från cellen
linktitle: Riktad formateringstext
type: docs
weight: 40
url: /sv/net/access-and-update-the-portions-of-rich-text-of-cell/
description: Lär dig hur du kan komma åt och uppdatera delar av rik text i en cell genom Aspose.Cells for .NET API.
keywords: Kom åt och uppdatera rik text i cell, Få rik text i cell, Redigera rik text i cell, Kom åt rik text i cell, Uppdatera rik text i cell, Ändra rik text i cell
---

{{% alert color="primary" %}}

Aspose.Cells låter dig komma åt och uppdatera delar av rik text i cellen. För detta ändamål kan du använda [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) och [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metoder. Dessa metoder returnerar och accepterar en matris av [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) objekt som du kan använda för att komma åt och uppdatera olika egenskaper hos teckensnittet, som teckensnittsnamn, teckensnittsfärg, fetstil, osv.

{{% /alert %}}

## **Åtkomst och uppdatering av delar av riktad text från cellen**

Följande kod visar användningen av [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) och [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metod med [källa excel filen](5112369.xlsx) som du kan ladda ner från den angivna länken. Källa excel filen har en rik text i cell A1. Den har 3 delar och varje del har ett olika teckensnitt. Följande kodsnutt kommer åt dessa delar och uppdaterar den första delen med ett nytt teckensnittsnamn. Slutligen sparar den arbetsboken som [utdata excel fil](5112366.xlsx). När du öppnar den kommer du att märka att teckensnittet för den första delen av texten har ändrats till **"Arial"**.

### C#-kod för att nå och uppdatera delarna av riktext av cellen

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

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

