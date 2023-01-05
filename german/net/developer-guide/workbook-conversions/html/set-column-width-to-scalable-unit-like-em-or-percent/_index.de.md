---
title: Stellen Sie die Spaltenbreite auf eine skalierbare Einheit wie em oder Prozent ein
type: docs
weight: 130
url: /de/net/set-column-width-to-scalable-unit-like-em-or-percent/
---
Das Generieren einer HTML-Datei aus einer Tabellenkalkulation ist weit verbreitet. Die Größe der Spalten wird in "pt" definiert, was in vielen Fällen funktioniert. Es kann jedoch einen Fall geben, in dem diese feste Größe nicht erforderlich ist. Wenn beispielsweise ein Container-Panel 600 Pixel breit ist und diese HTML-Seite angezeigt wird. In diesem Fall erhalten Sie möglicherweise eine horizontale Bildlaufleiste, wenn die generierte Tabellenbreite größer ist. Es war erforderlich, dass diese feste Größe in eine skalierbare Einheit wie em oder Prozent umgewandelt wird, um eine bessere Darstellung zu erhalten. Der folgende Beispielcode kann verwendet werden, wo[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable) ist eingestellt auf**wahr** zum Erstellen einer skalierbaren Breite.

Beispielquelldatei und Ausgabedateien können über die folgenden Links heruntergeladen werden:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
