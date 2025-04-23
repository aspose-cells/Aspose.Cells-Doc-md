---
title: Filtern der Art der Daten beim Laden des Arbeitsbuches aus der Vorlagendatei
type: docs
weight: 400
url: /de/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

Manchmal möchten Sie angeben, welche Art von Daten geladen werden soll beim Erstellen des Arbeitsbuches aus der Vorlagendatei. Das Filtern geladener Daten kann die Leistung für Ihren speziellen Zweck verbessern, insbesondere bei Verwendung der [LightCells-APIs](/cells/de/net/using-lightcells-api/). Bitte verwenden Sie das [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)-Eigenschaft zu diesem Zweck.

{{% /alert %}}

Der folgende Beispielcode lädt nur Formobjekte beim Laden des Arbeitsbuches aus der [Vorlagendatei](5115552.xlsx), die Sie aus dem angegebenen Link herunterladen können. Der folgende Screenshot zeigt den Inhalt der [Vorlagendatei](5115552.xlsx) und erklärt auch, dass die Daten in roter Farbe und gelbem Hintergrund nicht geladen werden, da das [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)-Eigenschaft auf [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) gesetzt wurde.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Der folgende Screenshot zeigt das [Ausgabe-PDF](5115555.pdf), das Sie aus dem angegebenen Link herunterladen können. Hier sehen Sie, dass die Daten in roter Farbe und gelbem Hintergrund nicht vorhanden sind, aber alle Formen sind vorhanden.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
