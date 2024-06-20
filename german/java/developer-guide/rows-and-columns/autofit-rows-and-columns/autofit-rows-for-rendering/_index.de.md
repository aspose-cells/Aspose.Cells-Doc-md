---
title: AutoFit für das Rendern von Zeilen
type: docs
weight: 130
url: /de/java/autofit-rows-for-rendering/
---

Im Allgemeinen, wenn Sie den gesamten Text in einer Zelle anzeigen möchten, können Sie die Zeile in der Normalansicht mit 100% Zoom in Microsoft Excel automatisch anpassen. Dies ermöglicht es, den Text in der Normalansicht vollständig sichtbar zu machen, und auch beim Drucken oder Speichern der Datei als PDF wird der Text richtig angezeigt.

Jedoch funktioniert in einigen Fällen das automatische Anpassen der Zeile in der Normalansicht gut, aber wenn Sie zur Druckansicht wechseln oder die Datei als PDF speichern, wird der Text beschnitten. Bitte überprüfen Sie die Quelldatei [Book1.xlsx](Book1.xlsx) und die Screenshots.

![Text wird in der Druckansicht beschnitten](text_clipped_in_printview.png)

Wenn Sie verhindern möchten, dass Text in der gespeicherten PDF-Datei abgeschnitten wird, können Sie die Zeile mit der Option [AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-) automatisch anpassen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

Nun wird der Text nicht in der Ausgabe-PDF-Datei beschnitten.

![Text wird in der gespeicherten PDF-Datei nicht beschnitten](text_not_clipped_in_saved_pdf.png)
