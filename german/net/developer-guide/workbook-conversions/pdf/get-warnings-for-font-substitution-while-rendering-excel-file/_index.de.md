---
title: Warnungen für Schriftarten ersetzen beim Rendern von Excel Dateien erhalten
type: docs
weight: 230
url: /de/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}} 

Manchmal ersetzt Aspose.Cells beim Rendern einer Microsoft Excel-Datei in PDF Schriftarten. Aspose.Cells bietet eine Funktion, die Entwickler darüber informiert, welche bestimmte Schriftart durch eine Warnung ersetzt wurde. Dies ist eine nützliche Funktion, die Ihnen helfen kann zu erkennen, warum ein von Aspose.Cells gerendertes PDF anders aussieht als die ursprüngliche Microsoft Excel-Datei, damit Sie geeignete Maßnahmen ergreifen können. Zum Beispiel, das Installieren der fehlenden Schriftarten, damit die Rendierungsergebnisse gleich aussehen.

{{% /alert %}} 

Um Warnungen für Schriftarten-Substitution beim Rendern von Excel-Dateien in PDF zu erhalten, implementieren Sie das IWarningCallback-Interface und setzen Sie die PdfSaveOptions.WarningCallback-Eigenschaft mit Ihrem implementierten Interface.

Der folgende Screenshot zeigt eine Quell-Excel-Datei, die wir im folgenden Code verwenden werden. Sie enthält einige Texte in den Zellen A6 und A7 in Schriftarten, die von Microsoft Excel nicht korrekt gerendert werden.

|**Nicht alle Schriftarten werden korrekt gerendert**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells wird die Schriftarten in den Zellen A6 und A7 durch geeignete Schriftarten ersetzen, wie unten gezeigt.

|**Ersetzte Schriftarten**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **Quelldatei herunterladen und PDF ausgeben**
Sie können die Quelldatei und das PDF-Output von den folgenden Links herunterladen

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)
## **Code**
Der folgende Code implementiert das IWarningCallback und setzt die PdfSaveOptions.WarningCallback-Eigenschaft mit dem implementierten Interface. Jetzt, wann immer eine Schriftart in einer Zelle ersetzt wird, wird Aspose.Cells eine Warnung in der WarningCallback.Warning() Methode auslösen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Ergebnis**
Nachdem die Quell-Excel-Datei in PDF konvertiert wurde, werden die Warnungen wie folgt in die Debug-Konsole ausgegeben:

{{< highlight java >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Wenn Ihre Tabelle Formeln enthält, ist es am besten, die Workbook.CalculateFormula Methode unmittelbar vor der Umsetzung der Tabelle in das PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die korrekten Werte im PDF dargestellt werden.

{{% /alert %}}
