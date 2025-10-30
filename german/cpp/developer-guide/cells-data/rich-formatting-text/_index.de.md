---
title: Zugreifen und Aktualisieren der Abschnitte von Rich Text einer Zelle mit C++
linktitle: Rich Text Formatierung
type: docs
weight: 40
url: /de/cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Lernen Sie, wie Sie die Abschnitte von Rich Text einer Zelle über die API Aspose.Cells for C++ zugreifen und aktualisieren.
keywords: Zugriff und Aktualisierung des Rich Texts einer Zelle, Abrufen des Rich Texts einer Zelle, Rich Text einer Zelle bearbeiten, Rich Text einer Zelle abrufen, Rich Text einer Zelle aktualisieren, Rich Text einer Zelle ändern
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie auf die Teile des Rich-Texts einer Zelle zugreifen und diese aktualisieren. Hierfür können Sie die [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) und [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) Methoden verwenden. Diese Methoden geben ein Array von [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)-Objekten zurück und akzeptieren dieses, mit dem Sie verschiedene Eigenschaften der Schriftart wie Schriftartname, Schriftfarbe, Fettgedrucktheit usw. ändern können.

{{% /alert %}}

## **Teile des Rich-Texts der Zelle zugreifen und aktualisieren**

Der folgende Code demonstriert die Verwendung der [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/)- und [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/)-Methoden mit der [Quell-Excel-Datei](5112369.xlsx). Die Quell-Excel-Datei enthält einen Rich-Text in Zelle A1 mit 3 Abschnitten, die jeweils eine andere Schriftart haben. Der Code greift auf diese Abschnitte zu und aktualisiert die Schriftart des ersten Abschnitts auf **"Arial"**. Die modifizierte Arbeitsmappe wird als [Ausgabe-Excel-Datei](5112366.xlsx) gespeichert.

### C++-Code zum Zugriff und zur Aktualisierung von Rich-Text-Abschnitten

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"Sample.xlsx";
    U16String outputPath = outDir + u"Output.out.xlsx";

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(U16String(u"A1"));

    std::cout << "Before updating the font settings...." << std::endl;

    Vector<FontSetting> fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    if (fnts.GetLength() > 0)
    {
        FontSetting& fs = fnts[0];
        fs.GetFont().SetName(u"Arial");
        cell.SetCharacters(fnts);
    }

    std::cout << std::endl << "After updating the font settings...." << std::endl;

    fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Von der Beispiellösung generierte Konsolenausgabe

Hier ist die Konsolenausgabe beim Verwenden der [Quell-Excel-Datei](5112369.xlsx):

{{< highlight java >}}

Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
