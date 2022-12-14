---
title: Ändern Sie die Schriftart nur für die spezifischen Unicode-Zeichen, während Sie sie als PDF speichern
type: docs
weight: 150
url: /de/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}}

 Einige Unicode-Zeichen können von der benutzerdefinierten Schriftart nicht angezeigt werden. Ein solches Unicode-Zeichen ist**Nicht brechender Bindestrich** (U+2011) und seine Unicode-Nummer ist 8209. Dieses Zeichen kann nicht mit dargestellt werden**Times New Roman** , aber es kann mit anderen Schriftarten wie angezeigt werden**Arial Unicode-MS**.

Wenn ein solches Zeichen in einem Wort oder Satz in einer bestimmten Schriftart wie Times New Roman vorkommt, ändert Aspose.Cells die Schriftart des gesamten Worts oder Satzes in eine Schriftart, die dieses Zeichen wie Arial Unicode für MS anzeigen könnte.

Dies ist jedoch für einige Benutzer ein unerwünschtes Verhalten, und sie möchten nur, dass die Schriftart des spezifischen Zeichens geändert werden muss, anstatt die Schriftart des gesamten Worts oder Satzes zu ändern.

 Um dieses Problem zu lösen, bietet Aspose.Cells[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) Eigenschaft, die gesetzt werden soll**Stimmt**so dass nur die Schriftart des bestimmten nicht darstellbaren Zeichens geändert wird und die Schriftart für den Rest des Wortes oder Satzes gleich bleibt.

{{% /alert %}}

## **Beispiel**

 Der folgende Screenshot vergleicht die beiden Ausgabe-PDFs, die durch den unten stehenden Beispielcode generiert wurden. Einer wurde ohne Einstellung generiert[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) Eigenschaft und die andere wurde nach dem Festlegen der generiert[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) Eigentum zu**Stimmt**. Wie Sie im ersten PDF sehen können, hat sich die Schriftart des gesamten Satzes aufgrund von Non-Breaking Hyphen von Times New Roman zu Arial Unicode MS geändert. Während sich im zweiten PDF nur die Schriftart von Non-Breaking Hyphen geändert hat.

![todo: Bild_alt_Text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
