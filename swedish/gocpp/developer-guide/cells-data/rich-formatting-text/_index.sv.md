---
title: Åtkomst och uppdatering av delar av riktext för celler med Golang via C++
linktitle: Riktad formateringstext
type: docs
weight: 40
url: /sv/go-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Lär dig hur du får åtkomst till och uppdaterar delar av rik text i cell via API et Aspose.Cells for C++.
keywords: Kom åt och uppdatera rik text i cell, Få rik text i cell, Redigera rik text i cell, Kom åt rik text i cell, Uppdatera rik text i cell, Ändra rik text i cell
---

{{% alert color="primary" %}}

Aspose.Cells låter dig komma åt och uppdatera delar av rik text i cellen. För detta ändamål kan du använda [**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/) och [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) metoder. Dessa metoder returnerar och accepterar en matris av [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) objekt som du kan använda för att komma åt och uppdatera olika egenskaper hos teckensnittet, som teckensnittsnamn, teckensnittsfärg, fetstil, osv.

{{% /alert %}}

## **Åtkomst och uppdatering av delar av riktad text från cellen**

Följande kod demonstrerar användningen av [**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/) och [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) metoden med hjälp av [källexcelfilen](5112369.xlsx). Källexcelfilen har rik text i cell A1 med 3 delar, var och en med ett annat typsnitt. Koden hämtar dessa delar och uppdaterar det första delens typsnitt till **"Arial"**. Den modifierade arbetsboken sparas som [utgångs excel fil](5112366.xlsx).

### C++-kod för att komma åt och uppdatera rik textdelar

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RichFormattingText.go" >}}
### Konsoloutput som genereras av provkoden

Här är utskriften i konsolen när du använder [källexcelfilen](5112369.xlsx):

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
