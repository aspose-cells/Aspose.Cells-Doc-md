---
title: Pivottabellproblem
type: docs
weight: 50
url: /sv/net/pivot-table-issue/
---
## **Symptom**
"Jag försökte öppna den genererade excel-filen från "Öppna"-knappen i IE. Excel har skapats genom att läsa en excel-mall. Medan jag klickar på knappen Öppna öppnas den och samtidigt dyker den upp en felmeddelande som säger "Kan inte öppna pivottabellens källfil.....".

Men när jag sparar den genererade Excel-filen med "Spara"-knappen och öppnar den från filen från den sparade sökvägen öppnas den korrekt utan några fel. "
### **Lösning**
Aspose.Cells ställer in pivotdataformatet och tvingar MS Excel att skapa pivottabellsrapporter och andra beräkningsuppgifter baserat på datakällan när arbetsboken öppnas i MS Excel. Så man bör använda**SaveType.OpenInBrowser** snarare än att använda**SaveType.OpenInExcel**En av många anledningar är att när du använder OpenInExcel-alternativet medan du sparar den utdatagenererade filen i MS Excel vid körning med "Öppna"-knappen i nedladdningsdialogrutan, kunde MS Excel inte analysera arbetsboksdata för att generera pivottabellsrapport. Detta orsakas av filnamnsproblemet. Det är rutin för IE eftersom det lägger till något i stil med "[1]" för att göra det till "filnamn"+ "[1]"+ ".xls" till det ursprungliga namnet och alltså inget till gör med Aspose.Cells. (dvs... den lägger alltid till "[1]" för att göra "filnamn"+ "[1]"+ ".xls" och inte som filnamn.xls). Kort sagt, om en fil innehåller pivottabell kan den inte öppnas med OpenInExcel SaveType-alternativet och detta kommer att gälla för båda, dvs om du skapar filen från början eller använder valfri mallfil för källdata för att skapa pivottabellsrapporter. Så du bör använda alternativet OpenInBrowser SaveType om filen har pivottabelldata för att skapa en pivottabellsrapport.

Du bör ändra din kod och uppdatera till SaveType.OpenInBrowser om du använder metoden Workbook.Save()

Eller redigera din kod för att använda "inline" om du använder alternativet "attachment" i din kod. dvs



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
