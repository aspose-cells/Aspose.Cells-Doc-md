---
title: Skapa dynamiska diagram
type: docs
weight: 240
url: /sv/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

Dynamiska (eller interaktiva) diagram har möjlighet att ändras när du ändrar dataomfånget. Med andra ord kan de dynamiska diagrammen automatiskt återspegla ändringar när datakällan ändras. För att utlösa förändringen i datakällan kan man använda filtreringsalternativet i Excel-tabeller eller använda en kontroll som ComboBox eller Dropdown-lista.

Den här artikeln visar användningen av Aspose.Cells for .NET API:er för att skapa dynamiska diagram med båda de ovannämnda metoderna.

{{% /alert %}}

## **Använda Excel-tabeller**

{{% alert color="primary" %}}

 Excel-tabeller hänvisas till som ListObjects i Aspose.Cells' perspektiv, därför kommer vi att använda termen "ListObject" istället för "Tabell" för tydlighetens skull. Läs i detalj hur du gör[skapa ListObjects](/cells/sv/net/create-and-format-table/) med Aspose.Cells for .NET API.

{{% /alert %}}

 ListObjects tillhandahåller den inbyggda funktionen för att sortera och filtrera data vid användarinteraktion. Både sorterings- och filtreringsalternativ tillhandahålls via rullgardinslistorna som automatiskt läggs till i rubrikraden i[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . På grund av dessa funktioner (sortering och filtrering),[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)verkar vara den perfekta kandidaten för att fungera som datakälla för ett dynamiskt diagram eftersom när sortering eller filtrering ändras kommer representationen av data i diagrammet att ändras för att återspegla det aktuella tillståndet för[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 För att hålla demonstrationen enkel att förstå kommer vi att skapa[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)från början och gå framåt steg för steg enligt beskrivningen nedan.

1.  Skapa en tom[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Få tillgång till[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) av den första[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) i[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Infoga lite data i cellerna.
1.  Skapa[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)baserat på de infogade uppgifterna.
1.  Skapa[**Diagram**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) baserat på dataintervallet för[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Spara resultatet på skivan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **Använda dynamiska formler**

 Om du inte vill använda[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)som en datakälla till det dynamiska diagrammet är det andra alternativet att använda Excel-funktioner (eller formler) för att skapa ett dynamiskt dataområde, och en kontroll (som ComboBox) för att utlösa dataändringen. I det här scenariot kommer vi att använda VLOOKUP-funktionen för att hämta lämpliga värden baserat på valet av ComboBox. När valet ändras, uppdaterar funktionen VLOOKUP cellens värde. Om ett cellintervall använder funktionen VLOOKUP, kan hela intervallet uppdateras vid användarinteraktion, därför kan det användas som en källa till det dynamiska diagrammet.

För att hålla demonstrationen enkel att förstå kommer vi att skapa arbetsboken från början och gå vidare steg för steg enligt beskrivningen nedan.

1.  Skapa en tom[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Få tillgång till[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) av den första[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) i[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Infoga några data i cellerna genom att skapa ett namngivet intervall. Dessa data kommer att fungera som en serie till det dynamiska diagrammet.
1.  Skapa[**Kombinationsrutan**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)baserat på det namngivna intervallet som skapades i föregående steg.
1. Infoga lite mer data till cellerna som kommer att fungera som en källa till UPPSÖKNINGSfunktionen.
1. Infoga VLOOKUP-funktionen (med lämpliga parametrar) i ett cellområde. Detta kommer att fungera som en källa till det dynamiska diagrammet.
1.  Skapa[**Diagram**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)baserat på intervallet som skapades i föregående steg.
1. Spara resultatet på skivan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
