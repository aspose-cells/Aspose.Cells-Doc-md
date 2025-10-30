---
title: Läs och hantera Excel 2016 diagram
type: docs
weight: 20
url: /sv/cpp/read-and-manipulate-excel-2016-charts/
---

## **Möjliga användningsscenario**
Aspose.Cells stöder läsning och hantering av Microsoft Excel 2016-diagram som inte finns i Microsoft Excel 2013 eller äldre versioner.
## **Läs och hantera Excel 2016-diagram**
Följande kodexempel laddar den [exempel Excel-filen](66519072.xlsx) som innehåller Excel 2016-diagram i det första arbetsbladet. Den läser alla diagram en efter en och ändrar dess titel enligt dess diagramtyp. Följande skärmbild visar exempel på Excel-filen innan körning av koden. Som du kan se är diagramtiteln densamma för alla diagram.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

Följande skärmbild visar den [utdata Excel-filen](66519073.xlsx) efter körningen av koden. Som du kan se har diagramtiteln ändrats enligt dess diagramtyp.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-ReadAndManipulateExcel2016Charts-new.cpp" >}}
## **Konsoloutput**
Här är konsolresultatet från det ovanstående kodexemplet när det körs med den medföljande exempel Excel-filen.

{{< highlight java >}}

 Waterfall

Treemap

Sunburst

Histogram

BoxWhisker

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
