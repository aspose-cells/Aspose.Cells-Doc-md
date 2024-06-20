---
title: Warnungen für Schriftarten ersetzen beim Rendern von Excel Dateien erhalten
type: docs
weight: 120
url: /de/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}}

Manchmal ersetzt Aspose.Cells beim Rendern von Microsoft Excel-Dateien in PDF-Schriftarten. Aspose.Cells bietet eine Funktion, die Entwickler darüber informiert, dass eine bestimmte Schriftart durch Auslösen einer Warnung ersetzt wurde. Dies ist eine nützliche Funktion, die Ihnen dabei helfen kann zu erkennen, warum das von Aspose.Cells gerenderte PDF anders ist als die tatsächliche Excel-Datei, und Sie können dann entsprechende Maßnahmen ergreifen. Zum Beispiel können Sie die fehlenden Schriften installieren, damit das Rendernergebnis gleich aussieht.

Wenn Sie die Warnungen für Schriftarten ersetzen möchten, während Sie eine Excel-Datei in PDF rendert, implementieren Sie das Interface IWarningCallback und setzen Sie die Methode PdfSaveOptions.setWarningCallback() mit Ihrem implementierten Interface.

{{% /alert %}}

Der untenstehende Screenshot zeigt die verwendete Excel-Quelldatei im folgenden Code. Sie enthält einige Texte in den Zellen A6 und A7 in Schriftarten, die von Microsoft Excel nicht gut wiedergegeben werden.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells wird die Schriftarten in den Zellen A6 und A7 durch geeignete Schriftarten ersetzen, wie unten gezeigt.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Quelldatei herunterladen und PDF ausgeben**

Sie können die Quelldatei und das PDF-Output von den folgenden Links herunterladen

- [source.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

Der folgende Code implementiert das [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) und setzt die [**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback)-Methode mit dem implementierten Interface. Nun, wann immer eine Schriftart in einer Zelle ersetzt wird, gibt Aspose.Cells eine Warnung in der WarningCallback.warning() Methode aus.

{{< highlight java >}}

 public class WarningCallback implements IWarningCallback {

    @Override

    public void warning(WarningInfo info) {

        if(info.getWarningType() == WarningType.FONT_SUBSTITUTION)

        {

            System.out.println("WARNING INFO: " + info.getDescription());

        }

    }

}

//........

//........

static void Run() throws Exception

{

    Workbook workbook = new Workbook("source.xlsx");

    PdfSaveOptions options = new PdfSaveOptions();

    options.setWarningCallback(new WarningCallback());

    workbook.save("output.pdf", options);

}

{{< /highlight >}}

## **Warnausgabe**

Nach der Konvertierung der Quelldatei werden die folgenden Warnungen in der Debug-Konsole ausgegeben:

{{< highlight java >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, die Methode Workbook.calculateFormula kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden. 

{{% /alert %}}
