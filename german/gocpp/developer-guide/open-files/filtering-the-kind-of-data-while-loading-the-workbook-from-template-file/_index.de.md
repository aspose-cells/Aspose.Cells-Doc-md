---
title: Filtern bestimmter Datentypen beim Laden der Arbeitsmappe aus einer Vorlage mit Golang via C++
linktitle: Daten filtern beim Laden der Arbeitsmappe
type: docs
weight: 400
url: /de/go-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Lernen Sie, wie man beim Laden einer Arbeitsmappe aus einer Vorlage mit Aspose.Cells in Golang via C++ bestimmte Datentypen filtern kann.
---

{{% alert color="primary" %}}

Manchmal möchten Sie angeben, welche Art von Daten beim Erstellen der Arbeitsmappe aus der Vorlage geladen werden soll. Das Filtern der geladenen Daten kann die Leistung für Ihren speziellen Zweck verbessern, insbesondere bei der Verwendung [LightCells-APIs](/cells/de/cpp/using-lightcells-api/). Bitte verwenden Sie hierfür die Eigenschaft [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/).

{{% /alert %}}

Der folgende Beispielcode lädt nur Formobjekte beim Laden des Arbeitsbuches aus der [Vorlagendatei](5115552.xlsx), die Sie aus dem angegebenen Link herunterladen können. Der folgende Screenshot zeigt den Inhalt der [Vorlagendatei](5115552.xlsx) und erklärt auch, dass die Daten in roter Farbe und gelbem Hintergrund nicht geladen werden, da das [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/)-Eigenschaft auf [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) gesetzt wurde.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Der folgende Screenshot zeigt das [Ausgabe-PDF](5115555.pdf), das Sie aus dem angegebenen Link herunterladen können. Hier sehen Sie, dass die Daten in roter Farbe und gelbem Hintergrund nicht vorhanden sind, aber alle Formen sind vorhanden.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilteringTheKindOfDataWhileLoadingTheWorkbookFromTemplateFile.go" >}}
