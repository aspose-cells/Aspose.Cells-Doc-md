---
title: Ändern Sie die Schriftart nur für bestimmte Unicode Zeichen beim Speichern als PDF mit Golang über C++
linktitle: Schriftart für Unicode Zeichen ändern
type: docs
weight: 260
url: /de/go-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Lernen Sie, wie Sie die Schriftart bestimmter Unicode Zeichen beim Speichern als PDF mit Aspose.Cells unter Golang über C++ ändern.
---

{{% alert color="primary" %}}

Einige Unicode-Zeichen können von der benutzerdefinierten Schriftart nicht angezeigt werden. Ein solches Unicode-Zeichen ist **Trennstrich** (U+2011) und seine Unicode-Nummer ist 8209. Dieses Zeichen kann nicht mit **Times New Roman** angezeigt werden, aber es kann mit anderen Schriften wie **Arial Unicode MS** angezeigt werden.

Wenn ein solches Zeichen innerhalb eines Wortes oder Satzes auftritt, das in einer bestimmten Schriftart wie Times New Roman vorliegt, ändert Aspose.Cells die Schriftart des gesamten Wortes oder Satzes in eine Schriftart, die dieses Zeichen darstellen kann, wie z. B. Arial Unicode MS.

Dies ist jedoch für einige Benutzer unerwünscht, da sie möchten, dass nur die Schriftart dieses spezifischen Zeichens geändert wird, anstatt die Schriftart des gesamten Wortes oder Satzes zu ändern.

Um dieses Problem zu beheben, bietet Aspose.Cells die Eigenschaft `PdfSaveOptions.IsFontSubstitutionCharGranularity`, die auf `true` gesetzt werden sollte, damit nur die Schriftart des spezifischen Zeichens, das nicht darstellbar ist, in eine darstellbare Schriftart geändert wird und der Rest des Wortes oder Satzes in der Originalschriftart bleibt.

{{% /alert %}}

## **Beispiel**

Der folgende Screenshot vergleicht die beiden Ausgabepdf-Dateien, die vom unten stehenden Beispielcode erstellt wurden.

Ein PDF wird ohne die Eigenschaft `PdfSaveOptions.IsFontSubstitutionCharGranularity` gesetzt, und das andere wurde nach dem Setzen dieser Eigenschaft auf `true` erstellt.

Wie im ersten PDF zu sehen ist, hat sich die Schriftart des gesamten Satzes aufgrund des Nichtbrech-Hyphens von Times New Roman auf Arial Unicode MS geändert. Im zweiten PDF hat sich nur die Schriftart des Nichtbrech-Hyphens geändert.

|**Erste PDF-Datei**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**Zweite PDF-Datei**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheFontOnJustTheSpecificUnicodeCharactersWhileSavingToPdf.go" >}}
