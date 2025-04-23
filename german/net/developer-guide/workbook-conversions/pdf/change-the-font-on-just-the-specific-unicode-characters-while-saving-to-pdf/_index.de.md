---
title: Ändern Sie die Schriftart nur für bestimmte Unicode Zeichen beim Speichern in PDF
type: docs
weight: 260
url: /de/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}} 

Einige Unicode-Zeichen sind nicht vom Benutzer angegebener Schriftart darstellbar. Ein solches Unicode-Zeichen ist **Bindestrich ohne Umbruch** (U+2011) und seine Unicode-Nummer lautet 8209. Dieses Zeichen kann nicht mit **Times New Roman** dargestellt werden, aber es kann mit anderen Schriftarten wie **Arial Unicode MS** dargestellt werden.

Wenn ein solches Zeichen innerhalb eines Wortes oder Satzes auftritt, der in einer bestimmten Schriftart wie Times New Roman ist, ändert Aspose.Cells die Schriftart des gesamten Wortes oder Satzes in eine Schriftart, die dieses Zeichen anzeigen kann, wie Arial Unicode MS.

Dies ist jedoch ein unerwünschtes Verhalten für einige Benutzer, und sie möchten nur, dass die Schriftart dieses spezifischen Zeichens geändert wird, anstatt die Schriftart des gesamten Wortes oder Satzes zu ändern.

Um dieses Problem zu lösen, bietet Aspose.Cells die Eigenschaft PdfSaveOptions.IsFontSubstitutionCharGranularity, die auf wahr gesetzt werden sollte, damit nur die Schriftart des spezifischen Zeichens, das nicht angezeigt werden kann, in eine angezeigte Schriftart geändert wird und der Rest des Wortes oder Satzes in der Originalschriftart bleiben sollte.

{{% /alert %}} 
## **Beispiel**
Der folgende Screenshot vergleicht die beiden Ausgabepdf-Dateien, die vom unten stehenden Beispielcode erstellt wurden.

Eine wurde ohne Einstellung der Eigenschaft PdfSaveOptions.IsFontSubstitutionCharGranularity erstellt, und die andere wurde nach Einstellung der Eigenschaft PdfSaveOptions.IsFontSubstitutionCharGranularity auf wahr erstellt.

Wie Sie im ersten PDF sehen können, wurde die Schriftart des gesamten Satzes von Times New Roman in Arial Unicode MS geändert, da der Bindestrich ohne Umbruch vorkam. Während im zweiten PDF nur die Schriftart des Bindestrichs ohne Umbruch geändert wurde.

|**Erste PDF-Datei**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Zweite PDF-Datei**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Beispielcode**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



{{< app/cells/assistant language="csharp" >}}
