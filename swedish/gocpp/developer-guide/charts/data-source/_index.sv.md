---
title: Ställ in datakälla för diagrammet med Golang via C++
linktitle: Datakälla
type: docs
weight: 10
url: /sv/go-cpp/data-formatting-in-charts/
description: Lär dig om de olika datakällorna som stöds av Aspose.Cells for C++. Vår guide visar de olika typer av datakällor som finns och hur du ansluter och hämtar data från dem för att fylla dina kalkylblad.
keywords: Aspose.Cells for C++, diagram, dataformat, etiketter, färger, typsnitt, utseende, användbarhet.
---

I våra tidigare ämnen har vi redan gett många exempel för att visa hur du kan ställa in en datakälla för ditt diagram. I det här ämnet kommer vi att ge mer information om de typer av data som kan anges för ett diagram.

## **Ställa in Diagramdata**

Det finns två typer av data att hantera när man arbetar med diagram med hjälp av Aspose.Cells som följer:

- Diagramdata.
- Kategoridata.

### **Diagramdata**

Diagramdata är den data som vi använder som datakälla för att bygga våra diagram. Vi kan lägga till ett intervall av celler (innehållande diagramdata) genom att ringa [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) objektets [**Add**](https://reference.aspose.com/cells/go-cpp/seriescollection/add/) metod.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource.go" >}}
### **Kategoridata**

Kategoridata används för märkning av diagramdata och kan läggas till i [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) genom att använda dess [**GetCategoryData()**](https://reference.aspose.com/cells/go-cpp/seriescollection/getcategorydata/) egenskap. Ett komplett exempel ges nedan för att demonstrera användningen av diagram- och kategoridata. Efter att ha utfört ovanstående exempelkod läggs ett kolumn diagram till i arbetsbladet enligt nedan.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource-1.go" >}}
## **Avancerade ämnen**
- [Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område](/cells/sv/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Skapa Dynamiska Diagram](/cells/sv/cpp/create-dynamic-charts/)
- [Enkel metod för diagraminställning med hjälp av Chart.SetChartDataRange-metoden](/cells/sv/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Hitta typ av X- och Y-värden för punkter i diagramserier](/cells/sv/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
