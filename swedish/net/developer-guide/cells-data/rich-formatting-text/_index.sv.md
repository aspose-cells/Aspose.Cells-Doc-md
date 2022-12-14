---
title: Få åtkomst till och uppdatera delarna av Rich Text på Cell
linktitle: Rik formateringstext
type: docs
weight: 40
url: /sv/net/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}}

 Aspose.Cells låter dig komma åt och uppdatera delarna av cellens RTF-text. För detta ändamål kan du använda[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) och[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metoder. Dessa metoder kommer att återvända och acceptera arrayen av[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)objekt som du kan använda för att komma åt och uppdatera olika egenskaper för teckensnitt som teckensnittsnamn, teckensnittsfärg, fetstil, etc.

{{% /alert %}}

## **Få åtkomst till och uppdatera delarna av Rich Text på Cell**

 Följande kod visar användningen av[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) och[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metod med hjälp av[source excel-fil](5112369.xlsx)som du kan ladda ner från den medföljande länken. Excel-källfilen har en rik text i cellen A1. Den har 3 delar och varje del har olika typsnitt. Följande kodsnutt kommer åt dessa delar och uppdaterar den första delen med ett nytt teckensnittsnamn. Slutligen sparar den arbetsboken som[output excel-fil](5112366.xlsx) . När du öppnar den kommer du att se att teckensnittet för den första delen av texten har ändrats till**"Arial"**.

### C#-kod för att komma åt och uppdatera delarna av Rich Text av Cell

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Konsolutdata genererad av exempelkoden

 Här är konsolutgången för ovanstående exempelkod med hjälp av[source excel-fil](5112369.xlsx).

{{< highlight "java" >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

