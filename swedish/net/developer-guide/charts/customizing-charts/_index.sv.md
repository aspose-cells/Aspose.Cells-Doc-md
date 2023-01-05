---
title: Anpassa diagram
type: docs
weight: 40
url: /sv/net/customizing-charts/
---
{{% alert color="primary" %}}

## **Skapa anpassade diagram**

Hittills, när vi har diskuterat diagram, har vi tittat på standarddiagram som har sina standardformateringsinställningar. Vi definierar bara datakällan, ställer in några få egenskaper och diagrammet skapas med dess standardformatinställningar. Men Aspose.Cells API:er stöder också att skapa anpassade diagram som gör det möjligt för utvecklare att skapa diagram med sina egna formatinställningar.

Utvecklare kan skapa anpassade diagram under körning med Aspose.Cells.

 Ett diagram är sammansatt av en dataserie. Varje dataserie i Aspose.Cells representeras av en[**Serier**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) objekt medan[**Seriekollektion**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) objekt fungerar som en samling av[**Serier**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)föremål. När du skapar ett anpassat diagram har utvecklare friheten att använda olika typer av diagram för olika dataserier (samlade i[**Seriekollektion**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)objekt).

Exempelkoden nedan visar hur man skapar anpassade diagram. I det här exemplet kommer vi att använda ett kolumndiagram för den första dataserien och ett linjediagram för den andra serien. Resultatet är att vi lägger till ett kolumndiagram, kombinerat med ett linjediagram, till kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

För närvarande stöder Aspose.Cells endast anpassade diagram som kombinerar cirkel-, linje-, kolumn- och kolumnstapeldiagram, men fler diagram kommer att stödjas i framtida versioner.

{{% /alert %}}
