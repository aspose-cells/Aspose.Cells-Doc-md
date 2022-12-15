---
title: Aspose.Cells for .NET 22.6 Release Notes
type: docs
weight: 7
url: /sv/net/aspose-cells-for-net-22-6-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 22.6](https://www.nuget.org/packages/Aspose.Cells/22.6.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-50880|Nytt api för att konvertera data till ICellsDataTable för användarens bekvämlighet|
|CELLSNET-51140|Stöd datalagring 5.0 av .numbers|
|CELLSNET-51144|Stöd för att läsa bilder av Numbers13|
|CELLSNET-51230|Stöd för att ställa in stil för CellRange|
|CELLSNET-50996|Lägg till ChartCollection.Add (ChartType, String, Boolean, Int32, Int32, Int32, Int32) överbelastad metod|
|CELLSNET-51184| Stöd import av matrisvärde om intervallet är en enkel cell|
|CELLSNET-51215|Stöd för att spara tabellformler till xlsb|
|CELLSNET-50226|bilden är suddig|
|CELLSNET-50954|Fel UpperLeftRow i CheckBox efter att arbetsboken lästs in|
|CELLSNET-51153| Dubbletter av kryssrutor|
|CELLSNET-51158|Tecken skrivna på objekt som former och textrutor är förvrängda i Linux|
|CELLSNET-51180|XLS-fil med pivottabell konverterad till XLSM är skadad och dataanslutningsdetaljer har raderats|
|CELLSNET-50598|Dynamisk formel med FILTER-funktion kan inte uppdateras och beräknas korrekt|
|CELLSNET-51069|Cell.Calculate() uppdaterar inte formelberoenden när beräkningskedjan är aktiverad för arbetsboken|
|CELLSNET-51186| Problem med CEILING-funktionen i Aspose.Cells' formelberäkningsmotor|
|CELLSNET-51192|DATE-funktionen beräknades som #NUM! för 1/0/1900|
|CELLSNET-51195|Konvertering av en XLSB-fil med Data Tables till XLSM-format resulterade i radering av Data Table|
|CELLSNET-51235|Vissa celler med mycket långa formler beräknas inte av Aspose.Cells|
|CELLSNET-51268|Problem med att COUNTIFS-formeln behandlar 0 felaktigt|
|CELLSNET-51041|Kinesiska tecken är skadade när html laddas|
|CELLSNET-51072|ImportXml-problem med datumfältet|
|CELLSNET-51081|Anpassat format ändras efter att sparad html har laddats in i arbetsboken|
|CELLSNET-51092|Överstruket teckensnitt fungerar inte i den renderade SVG/bilden på linux|
|CELLSNET-51120|Undantag vid export av xml-data kopplade till XML Map|
|CELLSNET-51197|ImportXml-problem med booleskt fält|
|CELLSNET-50854|XLSX till PDF: Stapeldiagram renderas inte korrekt|
|CELLSNET-50983|X-axeletiketter är fel|
|CELLSNET-50998| Sista x-axelparametern visas inte|
|CELLSNET-50999|Kartetiketter passar inte i lådan - lådan är överdimensionerad|
|CELLSNET-51000|Diagrametikett justerad vertikalt istället för horisontellt|
|CELLSNET-51043| Felaktig utmatning av serienamn när arbetsbok sparas till PDF|
|CELLSNET-51159| Buggar med Chart.Title.IsVisible=false när du sparar pdf|
|CELLSNET-51211| Saknade siffror när du skapar bild från Excel-diagram|
|CELLSNET-49105|Sparad .ods-fil är skadad när filen innehåller listvalidering|
|CELLSNET-50691|Förlora intervall för ErrorCheckOption|
|CELLSNET-50995| Chart.SetChartDataRange hoppar över tomma celler i dataintervallet|
|CELLSNET-51056|Chart.SetChartDataRange kände inte igen sammanslagna celler|
|CELLSNET-51062|Typen av tomt diagram ska vara ChartType.Line om den innehåller Marker-nod|
|CELLSNET-51116| Har revisionsattribut returnerar true men spåra ändringar är inaktiverat|
|CELLSNET-51199| workbook.save(filePath) Avbryter frysa rutor|
|CELLSNET-51228|Workbook.CalculateFormula orsakar undantaget "Objektreferens inte satt till en instans av ett objekt".|
|CELLSNET-51045|Undantag "Cell har tagits bort: D7" vid inställning av stil till ett intervall i Aspose.Cells.GridDesktop|
|CELLSNET-47707|Undantag "Denna Excel-fil innehåller (Excel2.1 eller tidigare filformat) poster" när en XLS-fil laddas|
|CELLSNET-47960|ny arbetsbok misslyckas höjning undantag: Denna Excel-fil innehåller (Excel4.0 eller tidigare filformat) poster.|
|CELLSNET-51227| System.FormatException. Strängen kändes inte igen som en giltig DateTime när Suomi Excel-fil laddades|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till klassen CellsDataTableFactory**

Den här klassen tillhandahåller api för att skapa instanser av ICellsDataTable från anpassade objekt för användarens bekvämlighet.

### **Lägger till egenskapen Workbook.CellsDataTableFactory**

Ge användaren CellsDataTableFactory för att skapa en instans av ICellsDataTable från anpassade objekt.

### **Lägger till metoden Cell.GetDependentsInCalculation(bool)**

Enligt nuvarande beräkningskedja, få alla celler vars beräknade resultat beror på denna cell.

### **Lägger till metoden Cell.GetPrecedentsInCalculation()**

Enligt nuvarande beräkningskedja, hämta alla prejudikat (referens till celler i aktuell arbetsbok) som används av denna cells formel när du beräknar den.

### **Föråldrade metoderna Cell.GetLeafs() och Cell.GetLeafs(bool)**

Använd metoden Cell.GetDependentsInCalculation(bool) istället.

### **Lägger till metoden PivotTable.FormatRow(int row, Style style).**

Formatera raddata i det vridbara området.

### **Lägger till egenskapen Shapes.CreateId**

Får skapande id för formen.

### **Lägger till WarningType.InvalidData enum**

Representerar den ogiltiga datatypen.

### **Lägger till överbelastningsmetoden ChartCollection.Add().**

Lägger till ett diagram med datakälla.

### **Lägger till metoden Chart.GetActualSize().**

Hämtar den faktiska storleken på diagrammet i pixelenhet.

### **Föråldrade egenskapen Chart.ActualChartSize**

Använd metoden Chart.GetActualSize() istället.

### **Föråldrade egenskapen PdfSaveOptions.ImageType**

Diagram och Shape renderas alltid som vektorelement (t.ex. punkt, linje) för renderingskvalitet.

### **Föråldrade egenskapen ImageOrPrintOptions.ChartImageType**

Diagram och Shape renderas alltid som vektorelement (t.ex. punkt, linje) för renderingskvalitet.

### **Tar bort föråldrad egenskap ImageOrPrintOptions.ImageFormat-egenskap**

Använd egenskapen ImageOrPrintOptions.ImageType istället.

### **Tar bort föråldrad egenskap ImageOrPrintOptions.IsImageFitToPage-egenskapen**

Fastigheten är värdelös.
