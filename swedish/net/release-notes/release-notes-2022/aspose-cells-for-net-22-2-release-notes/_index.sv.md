---
title: Aspose.Cells for .NET 22.2 Release Notes
type: docs
weight: 11
url: /sv/net/aspose-cells-for-net-22-2-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 22.2](https://www.nuget.org/packages/Aspose.Cells/22.2.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-50332| Extrahera alla namnsamlingar för ett visst kalkylblad|
|CELLSNET-50353|Lägg till StandardHeightInch-egenskapen i klassen Cells|
|CELLSNET-50152| Olika formaterings- och andra formrenderingsproblem i PDF och HTML i Excel-fil|
|CELLSNET-50300|Vissa former renderas inte korrekt i Excel till PDF-konvertering|
|CELLSNET-50301|Ogiltigt värde för extern referens i DataSource-fältet i pivottabellen|
|CELLSNET-50241|Regression: CSV till PDF konvertering fungerar inte|
|CELLSNET-50268|Tom CellsArea-array returneras för CSV/TSV filer|
|CELLSNET-50269|Finska språket - Numbers formaterad som Procent saknar mellanslag före procentsymbolen|
|CELLSNET-50333|Aspose.cell kunde inte samla in arbetsbokens revisionsloggar|
|CELLSNET-50239|Saknas sida efter konvertering av en Excel-fil till PDF|
|CELLSNET-50255|Typen Cell är fel efter export till html och omladdning av den exporterade html|
|CELLSNET-50266|Chart.ToImage() Trådsäkerhetsproblem|
|CELLSNET-50302|Regression: Konvertering till HTML nummer renderade inte korrekt|
|CELLSNET-50328|Cell bakgrunden blir svart efter konvertering till pdf|
|CELLSNET-50225| Diagramförklaring återställs när Excel sparas till PDF|
|CELLSNET-50247|Genom att infoga rader i arket tappar serien av diagram sina XValues|
|CELLSNET-50295|Chart.SetChartDataRange(area, false) känner inte igen sammanslagna celler|
|CELLSNET-50308|Intervall till PNG: utgången inte som förväntat|
|CELLSNET-50240| Oskyddade OLE-objekt på ett skyddat ark blir skyddade efter lagring|
|CELLSNET-50273|Upptäck filformatet för en speciell HTML-fil|
|CELLSNET-50294|ActiveX-kontrollknappar konverteras till former och filen är skadad för XLS till XLSM och sedan tillbaka till XLS|
|CELLSNET-50340|Tabellkolumnrader saknas vid konvertering av specifika filer till HTML|
|CELLSNET-50286|Cells.RemoveDuplicates kastar "System.IndexOutOfRangeException: Index var utanför gränserna för arrayen"|
|CELLSNET-50270|Inmatningssträngen var inte i korrekt format. undantag när filen XLS är öppen|
|CELLSNET-50271|Den här filens format stöds inte eller så anger du inte ett korrekt format. undantag när filen XLS är öppen|
|CELLSNET-50293|ExportXml med XML Map kastar "NullReferenceException" för en annan komplex fil|
|CELLSNET-50352|NullReferenceException vid konvertering av XLSM-fil till XLS|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Föråldrad Cells.AddAddInFunction()-metoden.**

Använd metoderna WorksheetCollection.RegisterAddInFunction() istället.

### **Lägger till metoden NameCollection.Filter() och NameScopeType enum.**

Hämtar de definierade namnen efter omfattning.

### **Lägger till MsoDrawingType.Timeline enum.**

Representerar typ av tidslinjeritningsobjekt.
