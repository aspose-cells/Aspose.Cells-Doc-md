---
title: Filtrera pivottabeller efter etikett eller värde
linktitle: Filtrera pivottabeller efter etikett eller värde
description: Aspose.Cells for Python via .NET stöder omfattande filtreringsfunktioner för pivottabeller. Den här artikeln förklarar hur man filtrerar pivottabellsdata med etikettfilter, datumfilter, värdefilter, topp 10-filter och genom att dölja eller visa pivotobjekt.
keywords: Aspose.Cells, Python via .NET-bibliotek, kalkylblad, pivottabell, filter, etikettfilter, värdefilter, datumfilter, topp 10-filter, pivotobjekt, dölj pivotobjekt
type: docs
weight: 10
url: /sv/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells erbjuder fem praktiska strategier för att filtrera data som visas i en pivottabell. Du kan tillämpa etikettfilter på textbaserade rad- eller kolumnfält, använda datumfilter när fältet endast innehåller datum-tid-celler eller tomma celler, tillämpa värdefilter mot aggregerade tal, använda topp 10-filter för att rangordna efter ett värdefält, eller manuellt dölja och visa enskilda pivotobjekt med hjälp av egenskapen `is_hidden`. Varje strategi exponeras genom dedikerade API:er på klasserna `PivotField` och `PivotItem`.
{{% /alert %}}
## **Introduktion**
Pivottabeller är kraftfulla analysverktyg, men råa sammanfattningar innehåller ofta betydligt mer information än vad du behöver presentera. Filtrering är den primära mekanismen för att begränsa en pivottabell till de rader, kolumner eller värden som är relevanta för en specifik rapport. Aspose.Cells for Python via .NET speglar de filtreringsfunktioner som är tillgängliga i Microsoft Excel och exponerar dem programmatiskt så att rapportgenerering kan automatiseras fullständigt.
Följande filtreringsstrategier behandlas i denna artikel:
1. **Etikettfilter** — filtrerar rad- eller kolumnfältsobjekt baserat på deras textetiketter.
2. **Datumfilter** — filtrerar rad- eller kolumnfält som endast innehåller datum-tid-värden (eller tomma värden).
3. **Värdefilter** — filtrerar objekt baserat på de aggregerade värdena i ett datafält.
4. **Topp 10-filter** — visar endast de N översta eller understa objekten rangordnade efter ett värdefält.
5. **Dölj / visa pivotobjekt** — styr manuellt synligheten för varje enskilt objekt i ett fält.
Varje tillvägagångssätt använder en annan metod på klassen `PivotField` eller en egenskap på klassen `PivotItem`. Efter att du har tillämpat ett filter måste du anropa `refresh_data()` och `calculate_data()` på pivottabellen så att den cachade datan och de beräknade värdena återspeglar det nya filterläget.
## **Etikettfilter**
Ett etikettfilter låter dig filtrera objekten i ett rad- eller kolumnfält genom att jämföra deras textetiketter mot ett mönster. Detta är användbart när du vill visa endast produkter vars namn börjar med en specifik bokstav, innehåller ett visst ord eller uppfyller något annat textbaserat kriterium.
Aspose.Cells exponerar etikettfiltrering genom metoden `PivotField.filter_by_label(PivotFilterType, label_string)`. Uppräkningen `PivotFilterType` innehåller värden som `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` och så vidare. Det andra argumentet anger den etikettsträng som används för jämförelse.
Följande exempel läser in en arbetsbok som innehåller en befintlig pivottabell, tillämpar ett etikettfilter så att endast objekt vars etiketter börjar med ett angivet prefix förblir synliga, uppdaterar pivottabellen och sparar resultatet.
```python
import aspose.cells as ac

fileName = "sample.xlsx"
prefix = "B"

# Ladda den befintliga arbetsboken som innehåller en pivottabell
workbook = ac.Workbook(fileName)

# Kom åt kalkylbladet via index (första kalkylbladet)
worksheet = workbook.worksheets[0]

# Kom åt pivottabellen via index
pivot_table = worksheet.pivot_tables[0]

# Hämta den första radens PivotField
row_field = pivot_table.row_fields[0]

# Använd etikettfiltret — visa endast radobjekt vars etiketter börjar med det angivna prefixet
row_field.filter_by_label(ac.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")

# Uppdatera och beräkna om pivottabelldatan så att filtret träder i kraft
pivot_table.pivot_cache.refresh()

# Spara arbetsboken tillbaka till disk
workbook.save(fileName)
```
## **Datumfilter**
Datumfilter låter dig begränsa en pivottabell efter datumbaserade kriterier som idag, förra veckan, denna månad, nästa kvartal eller ett specifikt datumintervall. De är specialiserade filter som endast fungerar mot fält som lagrar datum-tid-information.
{{% alert color="primary" %}}
Datumfiltret fungerar endast när rad- eller kolumnområdet endast innehåller datum-tid-celler eller tomma värden. Om det underliggande fältet innehåller andra datatyper som tal eller text kommer datumfiltret inte att ge det förväntade resultatet. Se till att fältet är formaterat som ett datum och att alla värden är giltiga `DateTime`-instanser eller tomma celler innan du tillämpar detta filter.
{{% /alert %}}
Aspose.Cells exponerar datumfiltrering genom metoden `PivotField.filter_by_date(PivotFilterType, *date_times)`. Uppräkningen `PivotFilterType` innehåller dedikerade datumvärden som `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` och `Between`. Beroende på vald filtertyp skickar du ett eller två `DateTime`-värden (för `Between` skickar du start- och slutdatum).
Följande exempel läser in en arbetsbok med en pivottabell vars radområde innehåller ett datumfält, tillämpar ett datumfilter som begränsar de synliga objekten till ett visst datumintervall, uppdaterar pivottabellen och sparar arbetsboken.
```python
from datetime import datetime

input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"

if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)

# Ladda den befintliga arbetsboken som innehåller pivottabellen
workbook = ac.Workbook(input_path)

# Åtkomst till kalkylbladet som innehåller pivottabellen (via index)
worksheet = workbook.worksheets[0]

# Åtkomst till pivottabellen via index
pivot_table = worksheet.pivot_tables[0]

# Hämta datum-PivotField från radområdet
# (Datumfilter fungerar bara när rad-/kolumnområdet endast innehåller datum-tid-celler eller tomma celler)
date_field = pivot_table.row_fields[0]

# Definiera datumpvillkoret för Between-filtret
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

# Tillämpa datumfiltret på pivotfältet
date_field.filter_by_date(ac.PivotFilterType.DATE_BETWEEN, start_date, end_date)

# Uppdatera och beräkna om pivottabellen så att filtret träder i kraft
pivot_table.pivot_cache.refresh()

# Spara arbetsboken
workbook.save(output_path)
```
## **Värdefilter**
Värdefilter opererar på de aggregerade värden som en pivottabell beräknar i sitt dataområde. Istället för att matcha textetiketter jämför de numeriska totalsummor mot ett tröskelvärde. Typiska användningsfall inkluderar att visa endast produkter vars summa av försäljning överstiger ett målbelopp eller endast regioner vars antal transaktioner ligger inom ett intervall.
Aspose.Cells exponerar värdefiltrering genom metoden `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)`. Parametern `PivotFilterType` använder värden som `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` och `ValueLessThanOrEqual`. Parametern `value_field` anger vilket datafält som ska utvärderas, och det sista argumentet (eller de sista argumenten) anger tröskelvärdet (eller tröskelvärdena).
Följande exempel läser in en arbetsbok med en pivottabell, tillämpar ett värdefilter som endast behåller objekt vars aggregerade försäljning överstiger ett numeriskt tröskelvärde, uppdaterar pivottabellen och sparar arbetsboken.
```python
import aspose.cells as ac

workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]

row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]

# Hitta datafältindex manuellt eftersom PivotFieldCollection inte har IndexOf
data_field_index = -1
for i in range(pivot_table.data_fields.count):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break

if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, ac.PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivot_table.pivot_cache.refresh()

workbook.save("output.xlsx")
```
## **Topp 10-filter**
Topp 10-filtret är en specialiserad form av värdefilter som endast behåller de N översta eller understa objekten baserat på ett valt värdefält. Det används vanligtvis för rankningsrapporter som "topp 10 produkter efter intäkt" eller "botten 5 regioner efter försäljningsantal".
{{% alert color="primary" %}}
Topp 10-filtret är endast effektivt när pivottabellen har ett eller flera värdepivotfält i dataområdet. Utan minst ett värdefält finns det inget aggregerat mått att rangordna objekten mot, och filtret kan inte tillämpas.
{{% /alert %}}
Aspose.Cells exponerar topp 10-filtrering genom metoden `PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)`. Parametern `item_count` anger hur många objekt som ska behållas, `is_top` anger om de översta objekten (True) eller de understa objekten (False) ska behållas, `value_field` refererar till det datafält som används för rankning, och `PivotFilterType` styr hur värdet beräknas (vanligtvis `Sum`, men även `Count` och `Percent`).
Följande exempel läser in en arbetsbok med en pivottabell som innehåller ett värdefält, tillämpar ett topp 10-filter för att endast behålla de 10 översta objekten efter summa av försäljning, uppdaterar pivottabellen och sparar arbetsboken.
```python
import aspose.cells as ac
import aspose.cells.pivot as acp

# Ladda den befintliga arbetsboken som innehåller pivottabellen
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)

# Kom åt kalkylbladet som innehåller pivottabellen (index 0)
worksheet = workbook.worksheets[0]

# Kom åt pivottabellen via index
pivotTable = worksheet.pivot_tables[0]

# Bekräfta att det finns minst ett värde-PivotField i dataområdet
if pivotTable.data_fields.count == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]

# Hämta målradens PivotField (fältet vi vill tillämpa Topp 10 på)
rowField = pivotTable.row_fields[0]

# Det första (och enda) datafältet är på index 0; Topp 10 rangordnar efter det.
valueFieldIndex = 0

# Tillämpa Topp 10-filtret på radfältet:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (topp N; false skulle betyda botten N)
#   - valueFieldIndex = index för datafältet som används för att rangordna poster
rowField.filter_top10(10, acp.PivotFilterType.Sum, True, valueFieldIndex)

# Uppdatera pivottabellens data och beräkna om den så att filtret träder i kraft
pivotTable.pivot_cache.refresh()

# Spara arbetsboken
workbook.save(outputPath)
```
## **Filtrera genom att dölja eller visa pivotobjekt**
Utöver de strukturerade filter-API:erna låter Aspose.Cells dig styra synligheten för varje enskilt pivotobjekt direkt. Genom att iterera genom `PivotItems`-samlingen för en `PivotField` och växla egenskapen `is_hidden` kan du selektivt undertrycka specifika objekt utan att tillämpa ett formelbaserat filter. Att sätta `is_hidden = True` döljer objektet från pivottabellen; att sätta `is_hidden = False` visar det igen och gör det synligt.
Detta tillvägagångssätt är användbart när filtreringsregeln är oregelbunden eller objektspecifik, till exempel att dölja ett litet antal namngivna kategorier som inte ska visas i en viss rapport. Exemplet nedan läser in en pivottabell, döljer ett specifikt objekt efter namn, visar hur man visar det igen, uppdaterar pivottabellen och sparar arbetsboken.
```python
import aspose.cells as ac

# Ladda en befintlig arbetsbok som innehåller en pivottabell
workbook = ac.Workbook("pivot_table_sample.xlsx")

# Öppna det första kalkylbladet som innehåller pivottabellen
sheet = workbook.worksheets[0]

# Öppna pivottabellen via index (den första pivottabellen på bladet)
pivot_table = sheet.pivot_tables[0]

# Hämta mål-PivotField (det första radetikettfältet där vi kommer att dölja/visa objekt)
pivot_field = pivot_table.row_fields[0]

# Iterera genom PivotItems-samlingen för den valda PivotField
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]

    # Dölj pivotobjekt som matchar ett specifikt namn/kriterium
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True

    # Demonstrera att visa igen: visa ett tidigare dolt pivotobjekt
    if item.name == "Item3":
        item.is_hidden = False

# Uppdatera och beräkna om pivottabellen så att ändringarna träder i kraft
pivot_table.pivot_cache.refresh()

# Spara arbetsboken — dolda objekt finns kvar i underliggande data
# men är exkluderade från den visade pivottabellens utdata
workbook.save("output_pivot_filtered.xlsx")
```
## **Sammanfattning**
Aspose.Cells for Python via .NET tillhandahåller en komplett uppsättning filtreringsfunktioner för pivottabeller som matchar de som finns i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analysscenarierna, medan topp 10-filtret hanterar rankningsrapporter. När filtreringsregeln är oregelbunden erbjuder egenskapen `PivotItem.is_hidden` ett flexibelt reservalternativ på objektnivå. Genom att kombinera dessa strategier — till exempel att tillämpa ett etikettfilter och sedan dölja specifika objekt — kan du bygga exakt riktade pivottabellrapporter helt från kod.
{{< app/cells/assistant language="python-net" >}}