---
title: Legen Sie die Spaltenbreite auf eine skalierbare Einheit wie em oder Prozent fest
type: docs
weight: 130
url: /de/net/set-column-width-to-scalable-unit-like-em-or-percent/
---

Das Generieren einer HTML-Datei aus einer Tabellenkalkulation ist sehr verbreitet. Die Größe der Spalten ist in "pt" definiert, was in vielen Fällen funktioniert. Es kann jedoch der Fall eintreten, dass diese feste Größe nicht erforderlich ist. Zum Beispiel, wenn die Breite eines Containerpanels 600px beträgt, in dem diese HTML-Seite angezeigt wird. In diesem Fall kann ein horizontaler Bildlaufbalken angezeigt werden, wenn die Breite der generierten Tabelle größer ist. Es war erforderlich, dass diese feste Größe in eine skalierbare Einheit wie em oder Prozent umgewandelt wird, um eine bessere Darstellung zu erhalten. Der folgende Beispielcode kann verwendet werden, wobei [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable) auf **true** gesetzt ist, um eine skalierbare Breite zu erstellen.

Beispiel-Quelldatei und Ausgabedateien können von folgenden Links heruntergeladen werden:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
