---
title: Skapa dynamiska diagram
type: docs
weight: 200
url: /sv/java/create-dynamic-charts/
---

{{% alert color="primary" %}}

Dynamiska (eller interaktiva) diagram har förmågan att ändra när du ändrar omfånget av data. Med andra ord kan de dynamiska diagrammen automatiskt återspegla förändringar när datakällan ändras. För att utlösa förändringen i datakällan kan man använda filteralternativet för Excel-tabeller eller använda en kontroll såsom ComboBox eller Dropdown-lista.

Den här artikeln demonstrerar användningen av Aspose.Cells for Java API:er för att skapa dynamiska diagram med båda ovan nämnda tillvägagångssätt.

{{% /alert %}}

## **Använda Excel-tabeller**

{{% alert color="primary" %}}

Excel-tabeller hänvisas till som ListObjects i Aspose.Cells-perspektivet därför kommer vi att använda termen "ListObject" istället för "Tabell" för tydlighet. Vänligen läs detaljerat om hur man [skapar ListObjects](/cells/sv/java/creating-a-list-object/) med Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects ger inbyggd funktionalitet för att sortera & filtera data vid användarinteraktion. Både sorterings- och filteralternativ tillhandahålls genom nedrullningslistor som automatiskt läggs till i rubrikraden för ListObject. På grund av dessa funktioner (sortering & filtrering) verkar ListObject vara det perfekta valet för att fungera som datakälla för ett dynamiskt diagram eftersom när sortering eller filtrering ändras kommer representationen av data i diagrammet att ändras för att återspegla det nuvarande tillståndet för ListObject.

För att hålla demonstrationen enkel att förstå kommer vi att skapa arbetsboken från början och gå framåt steg för steg enligt följande anvisningar.

1. Skapa en tom arbetsbok.
1. Kom åt cellerna i första kalkylbladet i arbetsboken.
1. Infoga några data i cellerna.
1. Skapa ListObject baserat på de infogade data.
1. Skapa diagram baserat på dataraden för ListObject.
1. Spara resultatet på disk.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Använda dynamiska formler**

Om du inte vill använda ListObjects som datakälla till det dynamiska diagrammet, är det andra alternativet att använda Excel-funktioner (eller formler) för att skapa en dynamisk dataserie, och en kontroll (som ComboBox) för att utlösa förändringen i data. I det här scenariot kommer vi att använda VLOOKUP-funktionen för att hämta lämpliga värden baserat på valet av ComboBox. När valet ändras kommer VLOOKUP-funktionen uppdatera cellvärdet. Om ett cellområde använder VLOOKUP-funktionen kan hela området uppdateras vid användarinteraktion, och därför kan användas som källa till det dynamiska diagrammet.

För att hålla demonstrationen enkel att förstå kommer vi att skapa arbetsboken från början och gå framåt steg för steg enligt följande anvisningar.

1. Skapa en tom arbetsbok.
1. Kom åt cellerna i första kalkylbladet i arbetsboken.
1. Infoga några data i cellerna genom att skapa en namngiven område. Dessa data kommer att fungera som serier till det dynamiska diagrammet.
1. Skapa en ComboBox baserad på det namngivna område skapat i föregående steg.
1. Infoga mer data i cellerna som kommer att användas som källa till VLOOKUP-funktionen.
1. Infoga VLOOKUP-funktionen (med lämpliga parametrar) i en rad celler. Denna rad kommer att fungera som källa till den dynamiska diagrammet.
1. Skapa diagram baserat på det intervall som skapats i föregående steg.
1. Spara resultatet på disk.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
{{< app/cells/assistant language="java" >}}
