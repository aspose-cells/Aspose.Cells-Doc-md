---
title: Filtern der Datenart beim Laden der Arbeitsmappe aus der Vorlagendatei
type: docs
weight: 680
url: /de/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}} 

 Manchmal möchten Sie angeben, welche Art von Daten geladen werden soll, wenn Sie die Arbeitsmappe aus einer Vorlagendatei erstellen. Das Filtern geladener Daten kann die Leistung für Ihren speziellen Zweck verbessern, insbesondere bei der Verwendung[LightCells-APIs](/cells/de/java/using-lightcells-api/) . Bitte verwenden Sie die[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) Eigentum für diesen Zweck.

{{% /alert %}} 
## **Filtern der Datenart beim Laden der Arbeitsmappe aus einer Vorlagendatei**
Der folgende Beispielcode lädt nur Shape-Objekte, während die Arbeitsmappe aus der geladen wird[Vorlagendatei](5472556.xlsx)die Sie unter dem angegebenen Link herunterladen können.

 Der folgende Screenshot zeigt die[Vorlagendatei](5472556.xlsx) Inhalt und erklärt auch, dass die Daten in roter Farbe und gelbem Hintergrund nicht geladen werden, weil die[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)Eigenschaft eingestellt wurde[LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![todo: Bild_alt_Text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

 Der folgende Screenshot zeigt die[PDF ausgeben](5472554.pdf) die Sie unter dem angegebenen Link herunterladen können. Hier können Sie sehen, dass die Daten in roter Farbe und gelbem Hintergrund nicht vorhanden sind, aber alle Formen vorhanden sind.

![todo: Bild_alt_Text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
