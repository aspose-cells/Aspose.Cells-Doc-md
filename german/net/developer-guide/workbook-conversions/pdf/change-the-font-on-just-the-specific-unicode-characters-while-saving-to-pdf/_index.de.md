---
title: Ändern Sie die Schriftart nur für die spezifischen Unicode-Zeichen, während Sie auf PDF speichern
type: docs
weight: 260
url: /de/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}} 

 Einige Unicode-Zeichen können von der benutzerdefinierten Schriftart nicht angezeigt werden. Ein solches Unicode-Zeichen ist**Nicht brechender Bindestrich** (U+2011) und seine Unicode-Nummer ist 8209. Dieses Zeichen kann nicht mit dargestellt werden**Times New Roman** , aber es kann mit anderen Schriftarten wie angezeigt werden**Arial Unicode-MS**.

Wenn ein solches Zeichen in einem Wort oder Satz in einer bestimmten Schriftart wie Times New Roman vorkommt, ändert Aspose.Cells die Schriftart des gesamten Worts oder Satzes in eine Schriftart, die dieses Zeichen wie Arial Unicode für MS anzeigen könnte.

Dies ist jedoch für einige Benutzer ein unerwünschtes Verhalten, und sie möchten, dass nur die Schriftart dieses bestimmten Zeichens geändert werden muss, anstatt die Schriftart des gesamten Worts oder Satzes zu ändern.

Um dieses Problem zu lösen, stellt Aspose.Cells die PdfSaveOptions.IsFontSubstitutionCharGranularity-Eigenschaft bereit, die auf „true“ gesetzt werden sollte, sodass nur die Schriftart eines bestimmten Zeichens, das nicht anzeigbar ist, in eine anzeigbare Schriftart geändert werden kann und der Rest des Wortes oder Satzes in der ursprünglichen Schriftart bleiben soll.

{{% /alert %}} 
## **Beispiel**
Der folgende Screenshot vergleicht die beiden Ausgabe-PDFs, die durch den unten stehenden Beispielcode generiert wurden.

Eine wird generiert, ohne die PdfSaveOptions.IsFontSubstitutionCharGranularity-Eigenschaft festzulegen, und die andere wurde generiert, nachdem die PdfSaveOptions.IsFontSubstitutionCharGranularity-Eigenschaft auf „true“ festgelegt wurde.

Wie Sie im ersten Pdf sehen können, hat sich die Schriftart des gesamten Satzes aufgrund von Non-Breaking Hyphen von Times New Roman zu Arial Unicode MS geändert. Während sich im zweiten Pdf nur die Schriftart von Non-Breaking Hyphen geändert hat.

|**Erste Pdf-Datei**|
|:- |
|![todo: Bild_alt_Text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Zweite PDF-Datei**|
|:- |
|![todo: Bild_alt_Text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Beispielcode**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



