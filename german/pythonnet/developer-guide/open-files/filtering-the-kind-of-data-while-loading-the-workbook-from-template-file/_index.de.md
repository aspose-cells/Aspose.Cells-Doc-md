---
title: Filtern der Art der Daten beim Laden des Arbeitsbuches aus der Vorlagendatei
type: docs
weight: 400
url: /de/python-net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

Manchmal möchten Sie angeben, welche Art von Daten beim Erstellen des Arbeitsbuchs aus der Vorlage geladen werden soll. Das Filtern geladener Daten kann die Leistung für Ihren speziellen Zweck verbessern. Verwenden Sie dafür die [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter)-Eigenschaft.

{{% /alert %}}

Der folgende Beispielcode lädt nur Formobjekte beim Laden des Arbeitsbuches aus der [Vorlagendatei](5115552.xlsx), die Sie aus dem angegebenen Link herunterladen können. Der folgende Screenshot zeigt den Inhalt der [Vorlagendatei](5115552.xlsx) und erklärt auch, dass die Daten in roter Farbe und gelbem Hintergrund nicht geladen werden, da das [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter)-Eigenschaft auf [**LoadDataFilterOptions.SHAPE**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) gesetzt wurde.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Der folgende Screenshot zeigt das [Ausgabe-PDF](5115555.pdf), das Sie aus dem angegebenen Link herunterladen können. Hier sehen Sie, dass die Daten in roter Farbe und gelbem Hintergrund nicht vorhanden sind, aber alle Formen sind vorhanden.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDataWhileLoadingWorkbook-1.py" >}}

