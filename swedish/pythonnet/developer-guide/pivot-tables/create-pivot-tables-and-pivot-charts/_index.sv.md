---
title: Skapa pivottabeller och pivotdiagram
type: docs
weight: 20
url: /sv/python-net/create-pivot-tables-and-pivot-charts/
description: Hur man lägger till pivottabeller och pivotdiagram med Aspose.Cells for Python via .NET.
keywords: Add Pivot Tables and Pivot Charts.
---
{{% alert color="primary" %}}

En pivottabell är en interaktiv sammanfattning av poster. Till exempel kan du ha hundratals fakturaposter i en lista i ett kalkylblad. En pivottabell kan summera fakturorna per kund, produkt eller datum. Med Microsoft Excel är det möjligt att snabbt ordna om informationen i pivottabellen genom att dra knappar till en ny position.

Ett pivotdiagram är en interaktiv grafisk representation av data i en pivottabell. Pivotdiagram introducerades i Excel 2000. Att använda ett pivotdiagram gör det ännu lättare att förstå data eftersom pivottabellen skapar delsummor och summor automatiskt.

 Aspose.Cells for Python via .NET stöder[pivottabeller](/cells/sv/python-net/create-pivot-tables-and-pivot-charts/) och[pivotdiagram](/cells/sv/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

##  **Lägga till pivottabeller och diagram**

Aspose.Cells for Python via .NET tillhandahåller en speciell uppsättning klasser som används för att skapa pivottabeller. Dessa klasser används för att skapa och ställa in PivotTable-objekt, som fungerar som ett PivotTable-objekts grundläggande byggstenar:

- PivotField, ett fält i en pivottabellsrapport.
- PivotFields, en samling av alla PivotField-objekt i en pivottabell.
- Pivottabell, en pivottabellrapport på ett kalkylblad.
- Pivottabeller, en samling av alla pivottabellobjekt på kalkylbladet.

###  **Förbereder att använda Aspose.Cells for Python via .NET**
1.  Installera Aspose.Cells for Python via .NET från[pypi](https://pypi.org/project/aspose-cells-python/)använd kommandot som: $ pip installera aspose-cells-python.
1. Du kan också följa steg-för-steg-instruktionerna om hur du installerar "Aspose.Cells for Python via .NET" i din utvecklarmiljö.


###  **Lägga till en pivottabell**

Så här skapar du en pivottabell med Aspose.Cells for Python via .NET:

1. Lägg till några data i ett kalkylbladsceller med hjälp av ett Cell-objekts put_value-metod. Du använder också en mallfil som redan är fylld med data. Data kommer att användas som pivottabellens datakälla.
1. Lägg till en pivottabell till kalkylbladet genom att anropa PivotTables-samlingens add-metod (inkapslad i Worksheet-objektet).
1. Få tillgång till det nya PivotTable-objektet från PivotTables-samlingen genom att skicka dess index. # Använd något av pivottabellobjekten som är inkapslade i PivotTable-objektet för att hantera tabellen.

Kodexempel ges nedan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

###  **Lägga till ett pivotdiagram**

Så här skapar du ett pivotdiagram med Aspose.Cells for Python via .NET:

1. Lägg till ett diagram.
1. Ställ in pivotkällan för diagrammet så att den refererar till en befintlig pivottabell i kalkylarket.
1. Ställ in andra attribut.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

