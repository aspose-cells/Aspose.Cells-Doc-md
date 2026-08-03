---
title: Filtrera pivottabeller efter etikett eller värde
linktitle: Filtrera pivottabeller efter etikett eller värde
description: Aspose.Cells for Python via Java stöder omfattande filterfunktioner för pivottabeller. Den här artikeln förklarar hur man filtrerar pivottabellsdata med etikettfilter, datumfilter, värdefilter, topp 10-filter samt genom att dölja eller visa pivotobjekt.
keywords: Aspose.Cells, Python via Java-bibliotek, kalkylblad, pivottabell, filter, etikettfilter, värdefilter, datumfilter, topp 10-filter, pivotobjekt, dölj pivotobjekt
type: docs
weight: 10
url: /sv/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells erbjuder fem praktiska strategier för att filtrera de data som visas i en pivottabell. Du kan tillämpa etikettfilter på textbaserade rad- eller kolumnfält, använda datumfilter när fältet endast innehåller datum-/tidsceller eller tomma celler, tillämpa värdefilter mot aggregerade tal, använda topp 10-filter för att rangordna efter ett värdefält, eller manuellt dölja och visa enskilda pivotobjekt med egenskapen `is_hidden`. Varje strategi exponeras genom dedikerade API:er på klasserna `PivotField` och `PivotItem`.
{{% /alert %}}
## **Introduktion**
Pivottabeller är kraftfulla analysverktyg, men råa sammanfattningar innehåller ofta mycket mer information än du behöver presentera. Filtrering är den primära mekanismen för att begränsa en pivottabell till de rader, kolumner eller värden som är relevanta för en specifik rapport. Aspose.Cells for Python via Java speglar de filterfunktioner som finns i Microsoft Excel och exponerar dem programmatiskt så att rapportgenerering kan automatiseras fullständigt.
Följande filterstrategier behandlas i den här artikeln:
1. **Etikettfilter** — filtrerar rad- eller kolumnfälts objekt baserat på deras textetiketter.
2. **Datumfilter** — filtrerar rad- eller kolumnfält som endast innehåller datum-/tidsvärden (eller tomma värden).
3. **Värdefilter** — filtrerar objekt baserat på de aggregerade värdena för ett datafält.
4. **Topp 10-filter** — visar endast de N översta eller nedersta objekten rangordnade efter ett värdefält.
5. **Dölj / visa pivotobjekt** — manuellt styr synligheten för varje enskilt objekt i ett fält.
Varje tillvägagångssätt använder en specifik metod på klassen `PivotField` eller en egenskap på klassen `PivotItem`. Efter att du har tillämpat något filter måste du anropa `refresh_data()` och `calculate_data()` på pivottabellen så att cachade data och beräknade värden återspeglar det nya filterläget.
## **Etikettfilter**
Ett etikettfilter låter dig filtrera objekten i ett rad- eller kolumnfält genom att jämföra deras textetiketter mot ett mönster. Detta är användbart när du vill visa endast produkter vars namn börjar med en specifik bokstav, innehåller ett visst ord eller uppfyller något annat beskrivningsbaserat kriterium.
Aspose.Cells exponerar etikettfiltrering genom metoden `PivotField.filter_by_label(PivotFilterType, str)`. Uppräkningen `PivotFilterType` innehåller värden som `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` och så vidare. Det andra argumentet anger den etikettsträng som används för jämförelse.
Följande exempel läser in en arbetsbok som innehåller en befintlig pivottabell, tillämpar ett etikettfilter så att endast objekt vars beskrivningar börjar med ett angivet prefix förblir synliga, uppdaterar pivottabellen och sparar resultatet.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

fileName = "sample.xlsx"
prefix = "B"

# Ladda den befintliga arbetsboken som innehåller en pivottabell
workbook = Workbook(fileName)

# Hämta kalkylbladet via index (första kalkylbladet)
worksheet = workbook.getWorksheets().get(0)

# Hämta pivottabellen via index
pivotTable = worksheet.getPivotTables().get(0)

# Hämta det första radens PivotField
rowField = pivotTable.getRowFields().get(0)

# Tillämpa etikettfiltret — visa endast radobjekt vars etiketter börjar med det angivna prefixet
rowField.filterByLabel(PivotFilterType.CaptionBeginsWith, prefix, "")

# Uppdatera och beräkna om pivottabellens data så att filtret träder i kraft
pivotTable.getPivotCache().refresh()

# Spara arbetsboken tillbaka till disk
workbook.save(fileName)

jpype.shutdownJVM()
```
## **Datumfilter**
Datumfilter låter dig begränsa en pivottabell efter datumbaserade kriterier såsom idag, förra veckan, denna månad, nästa kvartal eller ett specifikt datumintervall. Det är specialiserade filter som endast fungerar mot fält som lagrar datum-/tidsinformation.
{{% alert color="primary" %}}
Datumfiltret fungerar endast när rad- eller kolumnområdet endast innehåller datum-/tidsceller eller tomma värden. Om det underliggande fältet innehåller andra datatyper såsom tal eller text kommer datumfiltret inte att ge det förväntade resultatet. Se till att fältet är formaterat som ett datum och att alla värden är giltiga `DateTime`-instanser eller tomma celler innan du tillämpar detta filter.
{{% /alert %}}
Aspose.Cells exponerar datumfiltrering genom metoden `PivotField.filter_by_date(PivotFilterType, values)`. Uppräkningen `PivotFilterType` innehåller dedikerade datumvärden såsom `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` och `Between`. Beroende på vald filtertyp skickar du ett eller två `DateTime`-värden (för `Between` skickar du start- och slutdatum).
Följande exempel läser in en arbetsbok med en pivottabell vars radområde innehåller ett datumfält, tillämpar ett datumfilter som begränsar de synliga objekten till ett visst datumintervall, uppdaterar pivottabellen och sparar arbetsboken.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"

if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")

# Ladda den befintliga arbetsboken som innehåller pivottabellen
workbook = Workbook(inputPath)

# Kom åt kalkylbladet som innehåller pivottabellen (via index)
worksheet = workbook.getWorksheets().get(0)

# Kom åt pivottabellen via index
pivotTable = worksheet.getPivotTables().get(0)

# Hämta datum-PivotField från radområdet
# (Datumfilter fungerar bara när rad-/kolumnområdet endast innehåller datum-tidsceller eller tomma celler)
dateField = pivotTable.getRowFields().get(0)

# Definiera datumkriteriet för Between-filtret
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)

# Tillämpa datumfiltret på pivotfältet
dateField.filterByDate(PivotFilterType.DateBetween, startDate, endDate)

# Uppdatera och beräkna om pivottabellen så att filtret träder i kraft
pivotTable.getPivotCache().refresh()

# Spara arbetsboken
workbook.save(outputPath)

jpype.shutdownJVM()
```
## **Värdefilter**
Värdefilter arbetar på de aggregerade värden som en pivottabell beräknar i sitt dataområde. Istället för att matcha textetiketter jämför de numeriska summor mot ett tröskelvärde. Typiska användningsfall är att endast visa produkter vars summa av försäljning överstiger ett målbelopp eller endast regioner vars antal transaktioner ligger inom ett intervall.
Aspose.Cells exponerar värdefiltrering genom metoden `PivotField.filter_by_value(value_field, filter_type, values)`. Parametern `filter_type` använder värden som `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` och `ValueLessThanOrEqual`. Parametern `value_field` anger vilket datafält som ska utvärderas, och det sista argumentet (eller de sista argumenten) anger tröskelvärdet (eller tröskelvärdena).
Följande exempel läser in en arbetsbok med en pivottabell, tillämpar ett värdefilter som endast behåller objekt vars aggregerade försäljning överstiger ett numeriskt tröskelvärde, uppdaterar pivottabellen och sparar arbetsboken.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)

rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)

# Hitta datafältets index manuellt eftersom PivotFieldCollection inte har IndexOf
dataFieldIndex = -1
for i in range(pivotTable.getDataFields().getCount()):
    if pivotTable.getDataFields().get(i) == dataField:
        dataFieldIndex = i
        break

if dataFieldIndex >= 0:
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivotTable.getPivotCache().refresh()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```
## **Topp 10-filter**
Topp 10-filtret är en specialiserad form av värdefilter som endast behåller de N översta eller nedersta objekten baserat på ett valt värdefält. Det används ofta för rankningsrapporter såsom "topp 10 produkter efter intäkt" eller "botten 5 regioner efter antal försäljningar".
{{% alert color="primary" %}}
Topp 10-filtret är endast effektivt när pivottabellen har ett eller flera värde-pivotfält i dataområdet. Utan minst ett värdefält finns det inget aggregerat mått att rangordna objekten mot, och filtret kan inte tillämpas.
{{% /alert %}}
Aspose.Cells exponerar topp 10-filtrering genom metoden `PivotField.filter_top10(item_count, is_top, value_field, filter_type)`. Parametern `item_count` definierar hur många objekt som ska behållas, `is_top` anger om de översta objekten (true) eller de nedersta objekten (false) ska behållas, `value_field` refererar till det datafält som används för rangordning, och `filter_type` styr hur värdet beräknas (vanligtvis `Sum`, men även `Count` och `Percent`).
Följande exempel läser in en arbetsbok med en pivottabell som innehåller ett värdefält, tillämpar ett topp 10-filter för att endast behålla de 10 översta objekten efter summa av försäljning, uppdaterar pivottabellen och sparar arbetsboken.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType

# Ladda den befintliga arbetsboken som innehåller pivottabellen
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)

# Öppna arbetsbladet som innehåller pivottabellen (index 0)
worksheet = workbook.getWorksheets().get(0)

# Öppna pivottabellen via index
pivotTable = worksheet.getPivotTables().get(0)

# Bekräfta att det finns minst ett värde PivotField i dataområdet
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)

# Hämta målets rad-PivotField (fältet vi vill tillämpa Topp 10 på)
rowField = pivotTable.getRowFields().get(0)

# Det första (och enda) datafältet finns på index 0; Topp 10 rangordnar efter det.
valueFieldIndex = 0

# Tillämpa Topp 10-filtret på radfältet:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (topp N; false skulle betyda botten N)
#   - valueFieldIndex = indexet för datafältet som används för att rangordna objekten
rowField.filterTop10(10, PivotFilterType.Sum, True, valueFieldIndex)

# Uppdatera pivottabellens data och beräkna om den så att filtret träder i kraft
pivotTable.getPivotCache().refresh()

# Spara arbetsboken
workbook.save(outputPath)

jpype.shutdownJVM()
```
## **Filtrera genom att dölja eller visa pivotobjekt**
Utöver de strukturerade filter-API:erna låter Aspose.Cells dig styra synligheten för varje enskilt pivotobjekt direkt. Genom att iterera genom samlingen `PivotItems` för en `PivotField` och växla egenskapen `is_hidden` kan du selektivt dölja specifika objekt utan att tillämpa ett formelbaserat filter. Om du ställer in `is_hidden = True` döljs objektet från pivottabellen; om du ställer in `is_hidden = False` visas det igen och blir synligt.
Detta tillvägagångssätt är användbart när filterregeln är oregelbunden eller objektspecifik, till exempel att dölja ett litet antal namngivna kategorier som inte bör visas i en viss rapport. Exemplet nedan läser in en pivottabell, döljer ett specifikt objekt efter namn, visar hur man visar det igen, uppdaterar pivottabellen och sparar arbetsboken.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem

# Ladda en befintlig arbetsbok som innehåller en pivottabell
workbook = Workbook("pivot_table_sample.xlsx")

# Få åtkomst till det första arbetsbladet som innehåller pivottabellen
sheet = workbook.getWorksheets().get(0)

# Få åtkomst till pivottabellen via index (den första pivottabellen på arket)
pivotTable = sheet.getPivotTables().get(0)

# Hämta mål-PivotField (det första radetikettfältet där vi kommer att dölja/visa objekt)
pivotField = pivotTable.getRowFields().get(0)

# Iterera genom PivotItems-samlingen för det valda PivotField
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)

    # Dölj pivotobjekt som matchar ett specifikt namn/kriterium
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setIsHidden(True)

    # Demonstrera att visa: visa ett tidigare dolt pivotobjekt igen
    if item.getName() == "Item3":
        item.setIsHidden(False)

# Uppdatera och beräkna om pivottabellen så att ändringarna träder i kraft
pivotTable.getPivotCache().refresh()

# Spara arbetsboken — dolda objekt finns kvar i underliggande data
# men är exkluderade från den visade pivottabellutdatan
workbook.save("output_pivot_filtered.xlsx")

jpype.shutdownJVM()
```
## **Sammanfattning**
Aspose.Cells for Python via Java tillhandahåller en komplett uppsättning filterfunktioner för pivottabeller som motsvarar de som finns i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analysscenarierna, medan topp 10-filtret hanterar rankningsrapporter. När filterregeln är oregelbunden erbjuder egenskapen `PivotItem.is_hidden` ett flexibelt reservalternativ på objektnivå. Genom att kombinera dessa strategier — till exempel att tillämpa ett etikettfilter och sedan dölja specifika objekt — kan du bygga precis riktade pivottabellrapporter helt från kod.
{{< app/cells/assistant language="python" >}}