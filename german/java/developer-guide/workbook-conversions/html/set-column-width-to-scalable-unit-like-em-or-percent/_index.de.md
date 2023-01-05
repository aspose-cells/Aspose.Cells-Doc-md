---
title: Stellen Sie die Spaltenbreite auf eine skalierbare Einheit wie em oder Prozent ein
type: docs
weight: 130
url: /de/java/set-column-width-to-scalable-unit-like-em-or-percent/
---
Das Generieren einer HTML-Datei aus einer Tabellenkalkulation ist weit verbreitet. Die Größe der Spalten wird in "pt" definiert, was in vielen Fällen funktioniert. Es kann jedoch einen Fall geben, in dem diese feste Größe nicht erforderlich ist. Beispiel: Wenn die Breite des Containerbereichs 600 Pixel beträgt, wird diese HTML-Seite angezeigt. In diesem Fall erhalten Sie möglicherweise eine horizontale Bildlaufleiste, wenn die generierte Tabellenbreite größer ist. Es war erforderlich, dass diese feste Größe in eine skalierbare Einheit wie em oder Prozent umgewandelt wird, um eine bessere Darstellung zu erhalten. Der folgende Beispielcode kann verwendet werden, wo[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable) ist eingestellt auf**wahr** zum Erstellen einer skalierbaren Breite.

Beispielquelldatei und Ausgabedateien können über die folgenden Links heruntergeladen werden:

[sampleForScalableColumns.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
