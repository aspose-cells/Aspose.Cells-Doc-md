---
title: Erhalten Sie Warnungen für die Schriftartersetzung beim Rendern von Excel-Dateien
type: docs
weight: 230
url: /de/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}} 

Beim Rendern einer Microsoft-Excel-Datei in eine PDF-Datei ersetzt Aspose.Cells manchmal Schriftarten. Aspose.Cells bietet eine Funktion, die Entwickler durch das Auslösen einer Warnung darüber informiert, welche bestimmte Schriftart ersetzt wurde. Dies ist eine nützliche Funktion, mit der Sie feststellen können, warum eine gerenderte Aspose.Cells-PDF-Datei anders aussieht als die ursprüngliche Microsoft-Excel-Datei, damit Sie entsprechende Maßnahmen ergreifen können. Installieren Sie beispielsweise die fehlenden Schriftarten, damit die Rendering-Ergebnisse gleich aussehen.

{{% /alert %}} 

Um Warnungen für die Schriftartersetzung beim Rendern von Excel-Dateien in PDF zu erhalten, implementieren Sie die IWarningCallback-Schnittstelle und legen Sie die PdfSaveOptions.WarningCallback-Eigenschaft mit Ihrer implementierten Schnittstelle fest.

Der folgende Screenshot zeigt eine Excel-Quelldatei, die wir im folgenden Code verwenden werden. Es enthält Text in den Zellen A6 und A7 in Schriftarten, die von Microsoft Excel nicht gut wiedergegeben werden.

|**Nicht alle Schriftarten werden korrekt wiedergegeben**|
|:- |
|![todo: Bild_alt_Text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells ersetzt die Schriftarten in den Zellen A6 und A7 durch geeignete Schriftarten, wie unten gezeigt.

|**Ersetzte Schriftarten**|
|:- |
|![todo: Bild_alt_Text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **Quelldatei herunterladen und PDF ausgeben**
Sie können die Excel-Quelldatei und die PDF-Ausgabe über die folgenden Links herunterladen

- [source.xlsx](5112611.xlsx)
- [Ausgabe.pdf](5112616.pdf)
## **Code**
Der folgende Code implementiert IWarningCallback und legt die PdfSaveOptions.WarningCallback-Eigenschaft mit der implementierten Schnittstelle fest. Wenn jetzt eine beliebige Schriftart in einer beliebigen Zelle ersetzt wird, löst Aspose.Cells eine Warnung innerhalb der Methode WarningCallback.Warning() aus.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Ausgabe**
Nach der Konvertierung der Excel-Quelldatei in PDF werden die Warnungen wie folgt an die Debug-Konsole ausgegeben:

{{< highlight "java" >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Wenn Ihre Tabelle Formeln enthält, ist es am besten, die Methode Workbook.CalculateFormula direkt vor dem Rendern der Tabelle im PDF-Format aufzurufen. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet und die richtigen Werte im PDF wiedergegeben werden.

{{% /alert %}}
