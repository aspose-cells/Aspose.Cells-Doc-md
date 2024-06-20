---
title: Pivot Table problem
type: docs
weight: 50
url: /sv/net/pivot-table-issue/
---

## **Symptom**
"Jag försökte öppna den genererade Excel-filen från "Öppna"-knappen i IE. Excel-filen har genererats genom att läsa en Excel-mall. När jag klickar på Öppna-knappen öppnas den och samtidigt dyker det upp ett felmeddelande som säger "Kan inte öppna Pivot Table-källfil.....".

Men när jag sparar den genererade Excel-filen med hjälp av "Spara"-knappen och öppnar den från filen från den sparade sökvägen öppnas den korrekt utan några fel."
### **Lösning**
Aspose.Cells ställer in pivottabellformatet och tvingar MS Excel att skapa pivottabellrapporten och andra beräkningsuppgifter baserat på datakällan när arbetsboken öppnas i MS Excel. Så man bör använda **SaveType.OpenInBrowser** istället för att använda **SaveType.OpenInExcel**. En av de många anledningarna är när man använder OpenInExcel-alternativet vid sparande av den genererade filen i MS Excel vid körning med "Öppna"-knappen i dialogrutan för nedladdning kan inte MS Excel tolka arboksdata för att generera pivottabellrapport. Detta orsakas av filnamnsproblemet, detta är rutinen för IE eftersom den lägger till något som "[1]" för att göra det som "filNamn"+ "[1]"+ ".xls" till det ursprungliga namnet och därför har det ingenting att göra med Aspose.Cells. (dvs.... den lägger alltid till "[1]" för att göra "filNamn"+ "[1]"+ ".xls" och inte som filNamn.xls). Kort sagt, om en fil innehåller pivottabell kan den inte öppnas med alternativet SaveType.OpenInExcel och detta gäller för båda alternativen, dvs. om du skapar filen från grunden eller använder någon mallfil för källdata för att skapa pivottabellsrapport. Så du bör använda SaveType.OpenInBrowser om filen innehåller pivottabelldata för att skapa pivottabellsrapport.

Du bör ändra din kod och uppdatera till SaveType.OpenInBrowser om du använder Workbook.Save()-metoden.

Eller redigera din kod för att använda "inline" om du använder alternativet "attachment" i din kod. dvs.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
