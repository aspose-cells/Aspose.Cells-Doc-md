---
title: Skapa dynamiska diagram
type: docs
weight: 200
url: /sv/java/create-dynamic-charts/
---
{{% alert color="primary" %}}

Dynamiska (eller interaktiva) diagram har möjlighet att ändras när du ändrar dataomfånget. Med andra ord kan de dynamiska diagrammen automatiskt återspegla ändringar när datakällan ändras. För att utlösa förändringen av datakällan kan man använda filtreringsalternativet i Excel-tabeller eller använda en kontroll som ComboBox eller Dropdown-lista.

Den här artikeln visar användningen av Aspose.Cells for Java API:er för att skapa dynamiska diagram med båda de ovannämnda metoderna.

{{% /alert %}}

## **Använda Excel-tabeller**

{{% alert color="primary" %}}

 Excel-tabeller hänvisas till som ListObjects i Aspose.Cells' perspektiv, därför kommer vi att använda termen "ListObject" istället för "Tabell" för tydlighetens skull. Läs i detalj hur du gör[skapa ListObjects](/cells/sv/java/creating-a-list-object/) med Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects tillhandahåller den inbyggda funktionen för att sortera och filtrera data vid användarinteraktion. Både sorterings- och filtreringsalternativ tillhandahålls via rullgardinslistorna som automatiskt läggs till i rubrikraden i ListObject. På grund av dessa funktioner (sortering och filtrering) verkar ListObject vara den perfekta kandidaten för att fungera som datakälla till ett dynamiskt diagram, eftersom när sortering eller filtrering ändras kommer representationen av data i diagrammet att ändras för att återspegla den aktuella status för ListObject.

För att hålla demonstrationen enkel att förstå kommer vi att skapa arbetsboken från början och gå vidare steg för steg enligt beskrivningen nedan.

1. Skapa en tom arbetsbok.
1. Gå till Cells för det första arbetsbladet i arbetsboken.
1. Infoga lite data i cellerna.
1. Skapa ListObject baserat på infogade data.
1. Skapa diagram baserat på dataintervallet för ListObject.
1. Spara resultatet på skivan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Använda dynamiska formler**

Om du inte vill använda ListObjects som datakälla till det dynamiska diagrammet, är det andra alternativet att använda Excel-funktioner (eller formler) för att skapa ett dynamiskt dataområde, och en kontroll (som ComboBox) för att utlösa ändringen i data. I det här scenariot kommer vi att använda VLOOKUP-funktionen för att hämta lämpliga värden baserat på valet av ComboBox. När valet ändras, uppdaterar funktionen VLOOKUP cellens värde. Om ett cellområde använder funktionen VLOOKUP, kan hela området uppdateras vid användarinteraktion och kan därför användas som källa till det dynamiska diagrammet.

För att hålla demonstrationen enkel att förstå kommer vi att skapa arbetsboken från början och gå vidare steg för steg enligt beskrivningen nedan.

1. Skapa en tom arbetsbok.
1. Gå till Cells för det första arbetsbladet i arbetsboken.
1. Infoga några data i cellerna genom att skapa ett namngivet intervall. Dessa data kommer att fungera som serier till det dynamiska diagrammet.
1. Skapa ComboBox baserat på det namngivna intervallet som skapades i föregående steg.
1. Infoga lite mer data i cellerna som kommer att fungera som källa till UPPSÖKNING-funktionen.
1. Infoga VLOOKUP-funktionen (med lämpliga parametrar) i ett cellområde. Detta kommer att fungera som källa till det dynamiska diagrammet.
1. Skapa diagram baserat på intervallet som skapades i föregående steg.
1. Spara resultatet på skivan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
