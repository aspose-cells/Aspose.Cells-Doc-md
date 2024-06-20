---
title: Skapa, manipulera eller ta bort scenarier från arbetsblad
linktitle: Hantera scenarier
type: docs
weight: 120
url: /sv/java/create-manipulate-or-remove-scenarios-from-worksheets/
---

{{% alert color="primary" %}}

Ibland behöver du skapa, manipulera eller ta bort scenarier i kalkylblad. Ett scenario är en namngiven vad-händer-om-modell som inkluderar variabla insatsceller som är länkade tillsammans genom en eller flera formler. Innan du skapar ett scenario, utforma ett kalkylblad så att det innehåller åtminstone en formel som är beroende av celler där olika värden kan sättas in. Följande exempel visar hur du skapar och tar bort scener från ett kalkylblad med hjälp av Aspose.Cells API:erna.

{{% /alert %}}

Aspose.Cells tillhandahåller några användbara klasser, till exempel [**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) och [**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell). Det tillhandahåller också [**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios) egenskapen. Följande provkod öppnar en XLSX Excel-fil (som innehåller några scenarier) och tar bort ett befintligt scenario från kalkylbladet. Det lägger också till ett nytt scenario innan Excel-filen sparas. Den använder en mycket enkel mallfil som innehåller ett scenario.

Efter att koden har utförts, tas ett befintligt scenario bort och ett nytt scenario läggs till i kalkylbladet.

**Utgångsfilen**

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
