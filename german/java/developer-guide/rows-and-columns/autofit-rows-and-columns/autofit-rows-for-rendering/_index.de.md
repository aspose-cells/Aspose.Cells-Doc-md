---
title: Zeilen für das Rendern automatisch anpassen
type: docs
weight: 130
url: /de/java/autofit-rows-for-rendering/
---
Wenn Sie den gesamten Text in einer Zelle anzeigen möchten, können Sie im Allgemeinen die Zeile in der Normalansicht mit 100 % Zoom in Microsoft Excel automatisch anpassen. Dadurch ist der Text in der Normalansicht vollständig sichtbar, und selbst wenn Sie die Datei drucken oder als PDF speichern, wird der Text korrekt angezeigt.

 In einigen Fällen funktioniert die automatische Zeilenanpassung jedoch in der Normalansicht einwandfrei. Wenn Sie jedoch zur Druckansicht wechseln oder die Datei als PDF speichern, wird der Text abgeschnitten. Bitte überprüfen Sie die Quelldatei[Buch1.xlsx](Book1.xlsx) und Screenshots.

![Text wird in der Druckansicht abgeschnitten](text_clipped_in_printview.png)

Wenn Sie verhindern möchten, dass Text in der gespeicherten Datei PDF abgeschnitten wird, können Sie die Zeile mit automatisch anpassen[AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-) Möglichkeit.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

Jetzt wird der Text in der Ausgabedatei PDF nicht abgeschnitten.

![Text wird im gespeicherten PDF nicht abgeschnitten](text_not_clipped_in_saved_pdf.png)