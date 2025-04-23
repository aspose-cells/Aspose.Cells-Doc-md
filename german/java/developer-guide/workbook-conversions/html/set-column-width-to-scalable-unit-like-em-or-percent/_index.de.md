---
title: Legen Sie die Spaltenbreite auf eine skalierbare Einheit wie em oder Prozent fest
type: docs
weight: 130
url: /de/java/set-column-width-to-scalable-unit-like-em-or-percent/
---

Das Generieren einer HTML-Datei aus einer Tabellenkalkulation ist sehr verbreitet. Die Größe der Spalten ist in "pt" definiert, was in vielen Fällen funktioniert. Es kann jedoch Fälle geben, in denen diese feste Größe nicht erforderlich ist. Zum Beispiel, wenn die Breite des Container Panels 600px beträgt, in dem diese HTML-Seite angezeigt wird. In diesem Fall kann es sein, dass eine horizontale Bildlaufleiste angezeigt wird, wenn die Breite der generierten Tabelle größer ist. Es war erforderlich, dass diese feste Größe in eine skalierbare Einheit wie em oder Prozent geändert wird, um eine bessere Darstellung zu erhalten. Der folgende Beispielscode kann verwendet werden, wobei [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable) auf **true** festgelegt ist, um eine skalierbare Breite zu erstellen.

Beispiel-Quelldatei und Ausgabedateien können von folgenden Links heruntergeladen werden:

[sampleForScalableColumns.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
{{< app/cells/assistant language="java" >}}
