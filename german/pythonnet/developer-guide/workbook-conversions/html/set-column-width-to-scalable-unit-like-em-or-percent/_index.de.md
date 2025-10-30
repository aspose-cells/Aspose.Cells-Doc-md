---
title: Legen Sie die Spaltenbreite auf eine skalierbare Einheit wie em oder Prozent fest
type: docs
weight: 130
url: /de/python-net/set-column-width-to-scalable-unit-like-em-or-percent/
---

Das Generieren einer HTML-Datei aus einer Tabellenkalkulation ist sehr verbreitet. Die Größe der Spalten ist in "pt" definiert, was in vielen Fällen funktioniert. Es kann jedoch der Fall eintreten, dass diese feste Größe nicht erforderlich ist. Zum Beispiel, wenn die Breite eines Containerpanels 600px beträgt, in dem diese HTML-Seite angezeigt wird. In diesem Fall kann ein horizontaler Bildlaufbalken angezeigt werden, wenn die Breite der generierten Tabelle größer ist. Es war erforderlich, dass diese feste Größe in eine skalierbare Einheit wie em oder Prozent umgewandelt wird, um eine bessere Darstellung zu erhalten. Der folgende Beispielcode kann verwendet werden, wobei [**HtmlSaveOptions.width_scalable**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/width_scalable) auf **true** gesetzt ist, um eine skalierbare Breite zu erstellen.

Beispiel-Quelldatei und Ausgabedateien können von folgenden Links heruntergeladen werden:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetScalableColumnWidth-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
