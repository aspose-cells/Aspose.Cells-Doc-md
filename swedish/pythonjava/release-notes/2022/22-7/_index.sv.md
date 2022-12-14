---
title: Aspose.Cells för Python via Java 22.7 Release Notes
type: docs
weight: 6
url: /sv/python-java/aspose-cells-for-python-via-java-22-7-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för Python via Java 22.7](https://releases.aspose.com/cells/python-java/new-releases/aspose.cells-for-python-via-java-22.7/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44721|Stöd sortering av PivotField via beräknat fält|
|CELLSJAVA-44733|Undersök regler för ms excel för att visa cellens ram när intilliggande kolumn är dold: cellens ram har inte synkroniserats|
|CELLSJAVA-44695| Dålig konvertering till PDF från XLS med Line Callout till vänster på arket|
|CELLSJAVA-44700|Pivottabellberäknade fält uppdateras inte vid uppdatering av datakälla|
|CELLSJAVA-44705|Cell.getDependents() kastar undantag eller kan inte tillhandahålla alla anhöriga|
|CELLSJAVA-44717|Problem med kantstil (linje).|
|CELLSJAVA-44707| gränslinjen visas inte|
|CELLSJAVA-44670| Problem med formler i utdata HTML - Excel till HTML konvertering|
|CELLSJAVA-44202|Vid export till HTML är förklaringen i diagrammet inte densamma som MS Excel|
|CELLSJAVA-44591|Textrotation av etiketter stämmer inte överens med Excel i diagrammets utdatabild|
|CELLSJAVA-44655|Det går inte att visa trädkarta med negativt värde vilket gör att körningen fortsätter att köras|
|CELLSJAVA-44686|Titeltexten för diagram (2016) är felaktig när Title.IsAutoText är sant|
|CELLSJAVA-44689|Regression: Språkfråga för vattenfallsdiagramlegend|
|CELLSJAVA-44687|Diagramproblem vid kombination av filer|
|CELLSJAVA-44736|Bordsstilen förloras vid kopiering av ark|
|CELLSJAVA-44725| Undantag "java.util.zip.ZipException: ogiltig poststorlek (förväntade 0 men fick 1053 byte)" vid konvertering av XLSX till PDF|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Lägger till metoden Cells.GetDependentsInCalculation(int,int,bool)**

Hämtar alla celler vars beräknade resultat beror på cellen som anges av rad och kolumn enligt aktuell beräkningskedja. För cellen som är tom och inte har instansierats i nuvarande cellmodell, kan användaren använda denna metod istället för Cell.GetDependentsInCalculation(bool) eftersom den senare måste instansiera cellobjektet till den aktuella cellmodellen först.

### **Ändrar cellens vänster/höger kant för Cell.GetStyle() när den intilliggande kolumnen är dold**

gamla versioner, om den intilliggande kolumnen är dold för en cell, kommer denna cells Vänster/Höger-kant inte att kontrolleras med den intilliggande cellen, så den returnerade gränsen kan skilja sig från vad som visas i ms excels dialogruta när den här cellens kant ställs in. Från 22.7 gör vi att den returnerade gränsen alltid är det faktiska värdet (vilket bör överensstämma med gränsen för dess intilliggande cell) för cellen för Cell.GetStyle(). Om användaren behöver det som visas för cellen i ms excel (när den intilliggande kolumnen är dold, kan den visade gränsen vara den av nästa synliga kolumn), kan användaren prova Cell.GetDisplayStyle().

### **Lägg till egenskaperna Range.Top, Range.Left, Range.Height och Range.Width.**

Hämtar intervallets position och storlek i poängenhet.

### **Ta bort klassen PowerQueryFormulaCollction och lägg till klassen PowerQueryFormulaCollection.**

Det är ett stavfel i den gamla klassen.

### **Lägg till egenskaperna HtmlSaveOptions.ExportPageFooters och HtmlSaveOptions.ExportPageHeaders.**

Anger om sidhuvuden och sidfötter exporteras när du sparar som en enda html-fil.

### **Lägger till egenskapen HtmlSaveOptions.ShowAllSheets.**

Anger om alla ark visas när du sparar som en enda html-fil.

### **Föråldrar egenskapen HtmlSaveOptions.ExportHeadings och lägger till egenskapen HtmlSaveOptions.ExportRowColumnHeadings.**

Använd HtmlSaveOptions.ExportRowColumnHeadings istället.

### **Föråldrade Chart.ToImage(string, ImageFormat) och lägg till Chart.ToImage(string, ImageType)**

Använd Chart.ToImage(string, ImageType) istället.