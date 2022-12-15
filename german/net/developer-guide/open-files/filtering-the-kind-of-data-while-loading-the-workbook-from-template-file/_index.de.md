---
title: Filtern der Datenart beim Laden der Arbeitsmappe aus der Vorlagendatei
type: docs
weight: 400
url: /de/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}}

 Manchmal möchten Sie angeben, welche Art von Daten geladen werden sollen, wenn Sie die Arbeitsmappe aus der Vorlagendatei erstellen. Das Filtern geladener Daten kann die Leistung für Ihren speziellen Zweck verbessern, insbesondere bei der Verwendung[LightCells-APIs](/cells/de/net/using-lightcells-api/) . Bitte verwenden Sie die[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) Eigentum für diesen Zweck.

{{% /alert %}}

Der folgende Beispielcode lädt nur Shape-Objekte, während die Arbeitsmappe aus der geladen wird[Vorlagendatei](5115552.xlsx) die Sie unter dem angegebenen Link herunterladen können. Der folgende Screenshot zeigt die[Vorlagendatei](5115552.xlsx) Inhalt und erklärt auch, dass die Daten in roter Farbe und gelbem Hintergrund nicht geladen werden, weil[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)Eigenschaft eingestellt wurde[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![todo: Bild_alt_Text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Der folgende Screenshot zeigt die[PDF ausgeben](5115555.pdf) die Sie unter dem angegebenen Link herunterladen können. Hier können Sie sehen, dass die Daten in roter Farbe und gelbem Hintergrund nicht vorhanden sind, aber alle Formen vorhanden sind.

![todo: Bild_alt_Text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
