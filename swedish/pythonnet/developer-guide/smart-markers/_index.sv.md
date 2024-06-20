---
title: Smart import och placering av data med Smarta markörer i Python via .Net
linktitle: Smarta markörer
type: docs
weight: 190
url: /sv/python-net/using-smart-markers/
description: Smart import och placering av data enligt mall Excel filen med Aspose.Cells for Python via .Net bibliotek.
---

## **Introduktion**
**Smart markers** används för att låta Aspose.Cells veta vilken information som ska placeras i en Microsoft Excel-designmall. Smarta markörer gör det möjligt att skapa mallar som endast innehåller specifik information och formatering.
## **Designer Spreadsheet & Smart Markers**
Designer kalkylblad är standard Excel-filer som innehåller visuell formatering, formler och smarta markörer. De kan innehålla smarta markörer som refererar till en eller flera datakällor, såsom information från ett projekt och information för relaterade kontakter. Smarta markörer skrivs in i cellerna där du vill ha informationen.

Alla smarta markörer börjar med &=. Ett exempel på en datamarkör är &=Party.FullName. Om datamarkören resulterar i mer än en post, till exempel en komplett rad, flyttas följande rader ned automatiskt för att ge plats för den nya informationen. På så sätt kan delsummor och totaler placeras på raden omedelbart efter datamarkören för att göra beräkningar baserade på den infogade datan. Använd **dynamiska formler** för att göra beräkningar på de infogade raderna.

Smart markers består av **datakälla** och **fältnamn** för de flesta uppgifter. Speciell information kan också skickas med variabler och variabelmatriser. Variabler fyller alltid bara en cell medan variabelmatriser kan fylla flera. Använd endast en datamarkör per cell. Oanvända smart markers tas bort.

Smarta markörer kan också innehålla parametrar. Parametrar gör det möjligt att modifiera hur informationen layoutas. De läggs till i slutet av den smarta markören inom parentes som en kommateckenavgränsad lista.
### **Smart Marker-alternativ**
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==Dynamisk formula 
&=&=UpprepaDynamiskFormula
### **Parametrar**
Följande parametrar är tillåtna:

- **noadd** - Lägg inte till extra rader för att passa data.
- **skip:n** - Hoppa över n antal rader för varje datarad.
- **ascending:n** eller **descending:n** - Sortera data i smarta markörer. Om n är 1, då är kolumnen den första nyckeln för sorteraren. Datan sorteras efter bearbetningen av datakällan. Till exempel: &=Table1.Field3(ascending:1).
- **horisontell** - Skriv data från vänster till höger i stället för uppifrån och ner.
- **numerisk** - Konvertera text till nummer om möjligt.
- **shift** - Skifta nedåt eller åt höger, skapa extra rader eller kolumner för att passa datan. Skiftparametern fungerar på samma sätt som i Microsoft Excel. Till exempel i Microsoft Excel, när du väljer en rad av celler, högerklickar och väljer **Infoga** och specificerar **skifta celler nedåt**, **skifta celler åt höger** och andra alternativ. Kort sagt, fyller **shift**-parametern samma funktion för vertikala/normala (uppifrån och ner) eller horisontella (från vänster till höger) smarta markörer.
- **kopierastil** - Kopiera bascellens stil till alla celler i den kolumnen.

Parametrarna noadd och skip kan kombineras för att infoga data på växelvis rader. Eftersom mallen behandlas uppifrån och ner, bör du lägga till noadd på den första raden för att undvika att extra rader infogas före den växelvisa raden.

Om du har flera parametrar, separera dem med kommatecken, men inget mellanrum: parameterA, parameterB, parameterC

Följande skärmbilder visar hur du infogar data på varannan rad.

|**Mallfil**|**Resultatfil**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|
### **Dynamiska formler**
Dynamiska formler gör det möjligt att infoga Excel-formler i celler även när formeln refererar till rader som kommer att infogas under exportprocessen. Dynamiska formler kan upprepas för varje infogad rad eller använda endast den cell där datamarkören placeras.

Dynamiska formler möjliggör följande ytterligare alternativ:

- r - Nuvarande radnummer.
- 2, -1 - Förskjutning till aktuellt radnummer.

Exempelvis:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

I den dynamiska formelmarkören betecknar "-1" förskjutningen till den nuvarande raden i kolumn B och C respektive som kommer att ställas in för divisionsoperationen, hoppa parametern är en rad. Dessutom bör vi ange följande tecken:

{{< highlight java >}}

 "~"

{{< /highlight >}}

som ett avskiljande tecken för att tillämpa ytterligare parametrar i dynamiska formler.

De följande skärmbilderna illustrerar en upprepande dynamisk formel och den resulterande Excel-arket.

|**Mallfil**|**Utdatafil**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
Cellen "C1" innehåller formeln **= A1*B1**, cellen "C2" innehåller **= A2*B2** och cellen "C3" innehåller **= A3*B3**.

Det är mycket enkelt att bearbeta smarta markörer. Nedan följer en kodsnutt i Python via .Net, som visar hur det görs.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "SmartMarker-SimpleProcess.py" >}}


