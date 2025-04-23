---
title: Filtern der Art der Daten beim Laden des Arbeitsbuches aus der Vorlagendatei
type: docs
weight: 680
url: /de/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}} 

Manchmal möchten Sie angeben, welche Art von Daten beim Erstellen der Arbeitsmappe aus einer Vorlagendatei geladen werden soll. Das Filtern der geladenen Daten kann die Leistung für Ihren speziellen Zweck verbessern, insbesondere bei Verwendung der [LightCells-APIs](/cells/de/java/using-lightcells-api/). Bitte verwenden Sie das Eigenschaft [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) zu diesem Zweck.

{{% /alert %}} 
## **Filtern der Art der Daten beim Laden der Arbeitsmappe aus einer Vorlagendatei**
Der folgende Beispielcode lädt nur Formobjekte beim Laden der Arbeitsmappe aus der [Vorlagendatei](5472556.xlsx), die Sie über den angegebenen Link herunterladen können.

Der folgende Screenshot zeigt die Inhalte der [Vorlagendatei](5472556.xlsx) und erklärt auch, dass die Daten in roter Farbe und mit gelbem Hintergrund nicht geladen werden, da das Eigenschaft [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) auf [LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE) gesetzt wurde.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Der folgende Screenshot zeigt das [Ausgabepdf](5472554.pdf), das Sie über den angegebenen Link herunterladen können. Hier sehen Sie, dass die Daten in roter Farbe und mit gelbem Hintergrund nicht vorhanden sind, aber alle Formen vorhanden sind.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
{{< app/cells/assistant language="java" >}}
