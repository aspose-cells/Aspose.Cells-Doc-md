---
title: Smart import och placering av data med smarta markörer i Python via java
linktitle: Smarta markörer
type: docs
weight: 190
url: /sv/python-java/using-smart-markers/
description: Smart import och placering av data som följer mallen Excel-filer med Aspose.Cells för Python via java-biblioteket.
---
## **Introduktion**
**Smarta markörer**används för att låta Aspose.Cells veta vilken information som ska placeras i ett Microsoft Excel-designark. Smarta markörer låter dig skapa mallar som bara innehåller specifik information och formatering.
## **Designerkalkylblad och smarta markörer**
Designer-kalkylblad är vanliga Excel-filer som innehåller visuell formatering, formler och smarta markörer. De kan innehålla smarta markörer som refererar till en eller flera datakällor, till exempel information från ett projekt och information för relaterade kontakter. Smarta markörer skrivs in i cellerna där du vill ha informationen.

 Alla smarta markörer börjar med &=. Ett exempel på en datamarkör är &=Party.FullName. Om datamarkören resulterar i mer än ett objekt, till exempel en hel rad, flyttas följande rader ned automatiskt för att ge plats åt den nya informationen. Således kan delsummor och summor placeras på raden omedelbart efter datamarkören för att göra beräkningar baserat på infogade data. För att göra beräkningar på de infogade raderna, använd**dynamiska formler**.

 Smarta markörer består av**datakälla** och**fält namn**delar för mest information. Särskild information kan också skickas med variabler och variabla arrayer. Variabler fyller alltid bara en cell medan variabla arrayer kan fylla flera. Använd endast en datamarkör per cell. Oanvända smarta markörer tas bort.

Smart markör kan också innehålla parametrar. Parametrar låter dig ändra hur informationen är upplagd. De läggs till i slutet av den smarta markören inom parentes som en kommaseparerad lista.
### **Alternativ för smarta markörer**
 &=Datakälla.Fältnamn
 &=[Datakälla].[Fältnamn]&=$VariableName
 &=$VariableArray
 &==DynamicFormula
&=&=RepeatDynamicFormula
### **Parametrar**
Följande parametrar är tillåtna:

- **noadd** - Lägg inte till extra rader för att passa data.
- **hoppa över:n** - Hoppa över n antal rader för varje rad med data.
- **stigande:n** eller**fallande:n** - Sortera data i smarta markörer. Om n är 1, är kolumnen den första nyckeln i sorteraren. Data sorteras efter bearbetning av datakällan. Till exempel: &=Tabell1.Fält3(stigande:1).
- **horisontell** - Skriv data från vänster till höger, istället för från topp till botten.
- **numerisk** - Konvertera text till nummer om möjligt.
- **flytta** - Växla nedåt eller höger, skapa extra rader eller kolumner för att passa data. Skiftparametern fungerar på samma sätt som i Microsoft Excel. Till exempel i Microsoft Excel, när du markerar ett cellintervall högerklickar du och väljer**Föra in** och specificera?**flytta ner cellerna**, **flytta celler åt höger** och andra alternativ. Kort sagt**flytta** parametern fyller samma funktion för vertikala/normala (uppifrån och ned) eller horisontella (vänster till höger) smarta markörer.
- **copystyle** - Kopiera bascellens stil till alla celler i den kolumnen.

Parametrarna noadd och skip kan kombineras för att infoga data på alternerande rader. Eftersom mallen bearbetas från botten till toppen bör du lägga till noadd på första raden för att undvika att extra rader infogas före den alternativa raden.

Om du har flera parametrar, separera dem med ett kommatecken, men inget mellanslag: parameterA,parameterB,parameterC

Följande skärmdumpar visar hur man infogar data på varannan rad.

|**Mallfil**|**Utdatafil**|
|:- |:- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|
### **Dynamiska formler**
Dynamiska formler låter dig infoga Excel-formler i celler även när formeln refererar till rader som kommer att infogas under exportprocessen. Dynamiska formler kan upprepas för varje infogat rad eller bara använda cellen där datamarkören är placerad.

Dynamiska formler tillåter följande ytterligare alternativ:

- r - Aktuellt radnummer.
- 2, -1 - Offset till aktuellt radnummer.

Till exempel:

{{< highlight "java" >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

I den dynamiska formelmarkören betecknar "-1" förskjutningen till den aktuella raden i B- respektive C-kolumner som kommer att ställas in för divisionsoperation, överhoppningsparametern är en rad. Dessutom bör vi ange följande char:

{{< highlight "java" >}}

 "~"

{{< /highlight >}}

som ett separatortecken för att tillämpa ytterligare parametrar i dynamiska formler.

Följande skärmdumpar illustrerar en återkommande dynamisk formel och det resulterande Excel-kalkylbladet.

|**Mallfil**|**OutPut-fil**|
|:- |:- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
 Cell "C1" innehåller formeln**= A1*B1** , cell "C2" innehåller**= A2*B2** och cell "C3" innehåller**= A3*B3**.

Det är väldigt enkelt att bearbeta de smarta markörerna. Vad som följer är ett kodavsnitt i Python via Java, som visar hur det går till.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "SmartMarker-SimpleProcess.py" >}}


