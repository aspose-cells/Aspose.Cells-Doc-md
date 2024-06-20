---
title: Skapa dynamiska diagram
description: Lär dig hur du skapar dynamiska diagram i Aspose.Cells for .NET. Vår guide visar hur du dynamiskt uppdaterar diagrammets data, serier och formatering baserat på dina behov, vilket gör det möjligt för dig att visuellt presentera föränderliga data i dina kalkylblad.
keywords: Aspose.Cells for .NET, diagram, dynamiska diagram, data, serier, formatering, kalkylblad, uppdatering.
type: docs
weight: 240
url: /sv/net/create-dynamic-charts/
---

{{% alert color="primary" %}}

Dynamiska (eller interaktiva) diagram har förmågan att ändra sig när du ändrar omfånget för data. Med andra ord kan de dynamiska diagrammen automatiskt återspegla förändringar när datakällan ändras. För att trigga ändringen i datakällan kan man använda filteralternativet för Excel-tabeller eller använda en kontroll såsom ComboBox eller rullgardinslista.

Den här artikeln demonstrerar användningen av Aspose.Cells for .NET API för att skapa dynamiska diagram med hjälp av båda de tidigare nämnda metoderna.

{{% /alert %}}

## **Använda Excel-tabeller**

{{% alert color="primary" %}}

Excel-tabeller hänvisas till som ListObjects i Aspose.Cells-perspektiv, därför kommer vi att använda termen "ListObject" istället för "Tabell" för att öka tydligheten. Läs detaljerat om hur du [skapar ListObjects](/cells/sv/net/create-and-format-table/) med Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects tillhandahåller inbyggd funktionalitet för att sortera och filtrera data efter användarinteraktion. Både sorterings- och filteralternativ tillhandahålls via rullgardinslistor som automatiskt läggs till i rubrikraden för [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject). På grund av dessa funktioner (sortering och filtrering) verkar [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) vara det perfekta alternativet för att fungera som datakälla till ett dynamiskt diagram eftersom när sortering eller filtrering ändras kommer representationen av data i diagrammet att ändras för att återspegla det aktuella tillståndet för [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

För att hålla demonstrationen enkel att förstå kommer vi att skapa [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) från början och gå framåt steg för steg enligt följande anvisningar.

1. Skapa en tom [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Få tillgång till [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) på den första [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) i [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Infoga några data i cellerna.
1. Skapa [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) baserat på de infogade datan.
1. Skapa [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) baserat på dataområdet för [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Spara resultatet på disken.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **Använda dynamiska formler**

Om du inte vill använda [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) som datakälla till det dynamiska diagrammet är det andra alternativet att använda Excel-funktioner (eller formler) för att skapa en dynamisk datarange och en kontroll (såsom ComboBox) för att utlösa ändringen i datan. I detta scenario kommer vi att använda VLOOKUP-funktionen för att hämta lämpliga värden baserat på valet av ComboBox. När valet ändras kommer VLOOKUP-funktionen att uppdatera cellvärdet. Om en datarange använder VLOOKUP-funktionen kan hela området uppdateras efter användarinteraktion, därför kan det användas som källa till det dynamiska diagrammet.

För att hålla demonstrationen enkel att förstå kommer vi att skapa arbetsboken från början och gå framåt steg för steg enligt följande anvisningar.

1. Skapa en tom [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Få tillgång till [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) på den första [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) i [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Infoga några data i cellerna genom att skapa en namngiven range. Dessa data kommer att tjäna som en serie till det dynamiska diagrammet.
1. Skapa [**ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) baserat på den namngivna range som skapats i det föregående steget.
1. Infoga mer data i cellerna som kommer att fungera som källa till VLOOKUP-funktionen.
1. Infoga VLOOKUP-funktionen (med lämpliga parametrar) till ett område av celler. Detta område kommer att fungera som källa till den dynamiska diagrammet.
1. Skapa [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) baserat på det område som skapats i det föregående steget.
1. Spara resultatet på disken.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
