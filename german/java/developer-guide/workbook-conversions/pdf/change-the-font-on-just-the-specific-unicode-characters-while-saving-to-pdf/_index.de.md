---
title: Ändern Sie die Schriftart nur für bestimmte Unicode Zeichen beim Speichern in PDF
type: docs
weight: 150
url: /de/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}}

Einige Unicode-Zeichen können von der benutzerdefinierten Schriftart nicht angezeigt werden. Ein solches Unicode-Zeichen ist **Trennstrich** (U+2011) und seine Unicode-Nummer ist 8209. Dieses Zeichen kann nicht mit **Times New Roman** angezeigt werden, aber es kann mit anderen Schriften wie **Arial Unicode MS** angezeigt werden.

Wenn ein solches Zeichen in einem Wort oder Satz auftritt, das in einer bestimmten Schriftart wie Times New Roman steht, ändert Aspose.Cells die Schriftart des gesamten Wortes oder Satzes in eine Schriftart, die dieses Zeichen wie Arial Unicode MS anzeigen kann.

Dies ist jedoch ein unerwünschtes Verhalten für einige Benutzer, und sie wollen nur, dass die Schriftart des spezifischen Zeichens geändert wird, anstatt die Schriftart des gesamten Wortes oder Satzes zu ändern.

Um dieses Problem zu behandeln, bietet Aspose.Cells die [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)-Eigenschaft, die auf **true** gesetzt werden sollte, damit nur die Schriftart des spezifischen Zeichens, das nicht angezeigt werden kann, geändert wird und die Schriftart für den Rest des Wortes oder Satzes gleich bleibt.

{{% /alert %}}

## **Beispiel**

Der folgende Screenshot vergleicht die beiden Ausgabe-PDFs, die vom untenstehenden Beispielcode generiert wurden. Eines wurde ohne Einstellung der [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)-Eigenschaft generiert und das andere wurde nach Einstellung der [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)-Eigenschaft auf **true** generiert. Wie Sie im ersten PDF sehen können, wurde die Schriftart des gesamten Satzes von Times New Roman auf Arial Unicode MS geändert aufgrund des Trennstrichs. Im zweiten PDF wurde jedoch nur die Schriftart des Trennstrichs geändert.

![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
{{< app/cells/assistant language="java" >}}
