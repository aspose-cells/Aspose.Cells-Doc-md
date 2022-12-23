---
title: Erhalten Sie Warnungen für die Schriftartersetzung beim Rendern von Excel-Dateien
type: docs
weight: 120
url: /de/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}}

Manchmal werden beim Rendern von Microsoft-Excel-Dateien in PDF Schriftarten durch Aspose.Cells ersetzt. Aspose.Cells bietet eine Funktion, die Entwickler durch das Auslösen einer Warnung darüber informiert, dass eine bestimmte Schriftart ersetzt wurde. Dies ist eine nützliche Funktion, mit der Sie feststellen können, warum Aspose.Cells als PDF gerendert wird und sich von der eigentlichen Excel-Datei unterscheidet, und Sie können dann entsprechende Maßnahmen ergreifen. Beispielsweise können Sie die fehlenden Schriftarten installieren, damit die Rendering-Ergebnisse gleich aussehen.

Wenn Sie beim Rendern einer Excel-Datei in PDF die Warnungen für die Schriftartersetzung erhalten möchten, implementieren Sie die Schnittstelle IWarningCallback und legen Sie die Methode PdfSaveOptions.setWarningCallback() mit Ihrer implementierten Schnittstelle fest.

{{% /alert %}}

Der folgende Screenshot zeigt die Excel-Quelldatei, die im folgenden Code verwendet wird. Es enthält Text in den Zellen A6 und A7 in Schriftarten, die von Microsoft Excel nicht gut wiedergegeben werden.

![todo: Bild_alt_Text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells ersetzt die Schriftarten in den Zellen A6 und A7 durch geeignete Schriftarten, wie unten gezeigt.

![todo: Bild_alt_Text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Quelldatei herunterladen und PDF ausgeben**

Sie können die Excel-Quelldatei und die Ausgabe PDF über die folgenden Links herunterladen

- [source.xlsx](5472700.xlsx)
- [Ausgabe.pdf](5472699.pdf)

 Der folgende Code implementiert die[**IWarnungRückruf**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) und setze die[**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) Methode mit der implementierten Schnittstelle. Wenn jetzt eine Schriftart in einer Zelle ersetzt wird, löst Aspose.Cells eine Warnung innerhalb der Methode WarningCallback.warning() aus.

{{< highlight "java" >}}

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

## **Ausgabe von Warnungen**

Nach der Konvertierung der Quelldatei werden folgende Warnungen an der Debug-Konsole ausgegeben:

{{< highlight "java" >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

 Wenn Ihre Tabelle Formeln enthält, ist es am besten, die Methode Workbook.calculateFormula direkt vor dem Rendern der Tabelle in das Format PDF aufzurufen. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet und die richtigen Werte in PDF wiedergegeben werden.

{{% /alert %}}
