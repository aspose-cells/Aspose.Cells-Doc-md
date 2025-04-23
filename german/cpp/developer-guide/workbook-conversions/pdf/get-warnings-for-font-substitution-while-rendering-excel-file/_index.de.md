---
title: Warnungen für Schriftart Ersetzung beim Rendern der Excel Datei mit C++ erhalten
linktitle: Warnungen für Schriftart Ersetzung erhalten
type: docs
weight: 230
url: /de/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Erfahren Sie, wie Sie Warnungen für Schriftart Ersetzung beim Rendern von Excel Dateien in PDF mit Aspose.Cells in C++ erhalten.
---

{{% alert color="primary" %}}

Manchmal ersetzt Aspose.Cells beim Rendern einer Microsoft Excel-Datei in PDF Schriftarten. Aspose.Cells bietet eine Funktion, die Entwickler darüber informiert, welche bestimmte Schriftart durch eine Warnung ersetzt wurde. Dies ist eine nützliche Funktion, die Ihnen helfen kann zu erkennen, warum ein von Aspose.Cells gerendertes PDF anders aussieht als die ursprüngliche Microsoft Excel-Datei, damit Sie geeignete Maßnahmen ergreifen können. Zum Beispiel, das Installieren der fehlenden Schriftarten, damit die Rendierungsergebnisse gleich aussehen.

{{% /alert %}}

Um Warnungen für Schriftart-Ersetzung beim Rendern von Excel-Dateien in PDF zu erhalten, implementieren Sie die Schnittstelle `IWarningCallback` und setzen Sie die Eigenschaft `PdfSaveOptions.WarningCallback` mit Ihrer implementierten Schnittstelle.

Der folgende Screenshot zeigt eine Quell-Excel-Datei, die wir im folgenden Code verwenden werden. Sie enthält einige Texte in den Zellen A6 und A7 in Schriftarten, die von Microsoft Excel nicht korrekt gerendert werden.

|**Nicht alle Schriftarten werden korrekt gerendert**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|

Aspose.Cells wird die Schriftarten in den Zellen A6 und A7 durch geeignete Schriftarten ersetzen, wie unten gezeigt.

|**Ersetzte Schriftarten**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **Quelldatei herunterladen und PDF ausgeben**
Sie können die Quell-Excel-Datei und das Ausgabepdf von den folgenden Links herunterladen:

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)

## **Code**
Der folgende Code implementiert das `IWarningCallback` und setzt die Eigenschaft `PdfSaveOptions.WarningCallback` mit der implementierten Schnittstelle. Sobald eine Schrift in einer Zelle ersetzt wird, löst Aspose.Cells eine Warnung in der `WarningCallback.Warning()`-Methode aus.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GetWarningsForFontSubstitution : public IWarningCallback
{
public:
    void Warning(WarningInfo& info) override
    {
        if (info.GetType() == ExceptionType::FontSubstitution)
        {
            std::cout << "WARNING INFO: " << info.GetDescription().ToUtf8() << std::endl;
        }
    }

    static void Run()
    {
        U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
        U16String outDir(u"..\\Data\\02_OutputDirectory\\");
        Workbook workbook(srcDir + u"source.xlsx");
        PdfSaveOptions options;
        auto callback = std::make_shared<GetWarningsForFontSubstitution>();
        options.SetWarningCallback(callback.get());
        workbook.Save(outDir + u"output_out.pdf", options);
        std::cout << "PDF saved successfully with font substitution warnings!" << std::endl;
    }
};

int main()
{
    Aspose::Cells::Startup();
    GetWarningsForFontSubstitution::Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Ergebnis**
Nachdem die Quell-Excel-Datei in PDF konvertiert wurde, werden die Warnungen wie folgt in die Debug-Konsole ausgegeben:

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, die Methode `Workbook.CalculateFormula` direkt vor dem Rendern der Tabelle in das PDF-Format aufzurufen. Dadurch wird sichergestellt, dass die formulaabhängigen Werte neu berechnet werden und die korrekten Werte im PDF dargestellt werden.

{{% /alert %}}
