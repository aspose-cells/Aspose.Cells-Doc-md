---
title: Smart Markers funktionen i Aspose.Cells
type: docs
weight: 30
url: /sv/net/smart-markers-feature-in-aspose-cells/
---

**Smart markers** används för att låta Aspose.Cells veta vilken information som ska placeras i en Microsoft Excel designer kalkylblad. Smarta markörer gör att du kan skapa mallar som endast innehåller specifik information och formatering.
## **Designer Spreadsheet & Smart Markers**
Designer kalkylblad är standard Excel-filer som innehåller visuell formatering, formler och smarta markörer. De kan innehålla smarta markörer som refererar till en eller flera datakällor, såsom information från ett projekt och information för relaterade kontakter. Smarta markörer skrivs in i cellerna där du vill ha informationen.

Alla smarta markörer börjar med &=. Ett exempel på en datamarkör är &=Party.FullName. Om datamarkören resulterar i mer än en post, till exempel en komplett rad, flyttas följande rader automatiskt ned för att ge plats för all ny information. Därför kan delsummeringar och totaler placeras på raden omedelbart efter datamarkören för att göra beräkningar baserade på den infogade informationen. För att göra beräkningar på de infogade raderna, använd dynamiska formler.

Smart markers består av **datakälla** och **fältnamn** för de flesta uppgifter. Speciell information kan också skickas med variabler och variabelmatriser. Variabler fyller alltid bara en cell medan variabelmatriser kan fylla flera. Använd endast en datamarkör per cell. Oanvända smart markers tas bort.

Smart markör kan också innehålla parametrar. Parametrar låter dig modifiera hur informationen ska läggas ut. De läggs till i slutet av smart markör i parentes som en kommaseparerad lista.
### **Smart Marker-alternativ**
- &=DataSource.FieldName
- &=Data Source.Field Name
- &=$VariableName
- &=$VariableArray
- &==DynamicFormula
- &=&=RepeatDynamicFormula
### **Parametrar**
Följande parametrar är tillåtna:

- noadd - Lägg inte till extra rader för att passa data.
- skip:n - Hoppa över n antal rader för varje rad med data.
- ascending:n eller descending:n - Sortera data i smarta markörer. Om n är 1, är kolumnen den första sorteringen. Data sorteras efter att datakällan har bearbetats. T.ex. &=Table1.Field3(stigande:1).
- horisontell - Skriv data från vänster till höger istället för uppifrån och ner.
- numerisk - Omvandla text till nummer om möjligt. Endast stöds i .NET-versionen.
- skift - Skifta nedåt eller åt höger, skapa extra rader eller kolumner för att passa data. Skiftparametern fungerar på samma sätt som i Microsoft Excel. Till exempel i MS Excel, när du markerar en cellintervall, högerklickar och väljer Infoga och specificerar skifta celler nedåt, skifta celler åt höger och andra alternativ. Kort sagt fyller skiftparametern samma funktion för vertikala/normala (uppifrån och ner) eller horisontella (från vänster till höger) smarta markörer.
- kopystil - Kopiera bascellens stil till alla celler i den kolumnen.

Parametrarna **noadd** och skip kan kombineras för att infoga data på växelvis rader. Eftersom mallen bearbetas underifrån och upp bör du lägga till noadd på den första raden för att undvika att extra rader infogas före den växlande raden.

Denna avsnitt inkluderar följande ämnen

- [Gruppering av data i Aspose.Cells](/cells/sv/net/grouping-data-in-aspose-cells/)
- [Bildmarkörer i Aspose.Cells](/cells/sv/net/image-markers-in-aspose-cells/)
- [Användning av anonyma typer eller anpassade objekt i Aspose.Cells](/cells/sv/net/using-anonymous-types-or-custom-objects-in-aspose-cells/)
- [Användning av inbäddade objekt i Aspose.Cells](/cells/sv/net/using-nested-objects-in-aspose-cells/)
