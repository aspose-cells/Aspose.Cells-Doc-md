---
title: AutoFit für das Rendern von Zeilen
type: docs
weight: 130
url: /de/python-net/autofit-rows-for-rendering/
description: Erfahren Sie, wie Sie durch die Aspose.Cells für Python via .NET API Zeilen für das Rendering automatisch anpassen.
keywords: Python Excel Bibliothek, Python Autofit Rows für das Rendering, Python passt die Zeilenhöhe automatisch an, wenn die Excel Datei geöffnet wird. 
---

Im Allgemeinen, wenn Sie den gesamten Text in einer Zelle anzeigen möchten, können Sie die Zeile in der Normalansicht mit 100% Zoom in Microsoft Excel automatisch anpassen. Dies ermöglicht es, den Text in der Normalansicht vollständig sichtbar zu machen, und auch beim Drucken oder Speichern der Datei als PDF wird der Text richtig angezeigt.

Jedoch funktioniert in einigen Fällen das automatische Anpassen der Zeile in der Normalansicht gut, aber wenn Sie zur Druckansicht wechseln oder die Datei als PDF speichern, wird der Text beschnitten. Bitte überprüfen Sie die Quelldatei [Book1.xlsx](Book1.xlsx) und die Screenshots.

![Text wird in der Druckansicht beschnitten](text_clipped_in_printview.png)

Wenn Sie verhindern möchten, dass Text in der gespeicherten PDF-Datei abgeschnitten wird, können Sie die Zeile mit der Option [AutoFitterOptions.for_rendering](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/for_rendering/) autofitten.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsForRendering.py" >}}

Nun wird der Text nicht in der Ausgabe-PDF-Datei beschnitten.

![Text wird in der gespeicherten PDF-Datei nicht beschnitten](text_not_clipped_in_saved_pdf.png)
