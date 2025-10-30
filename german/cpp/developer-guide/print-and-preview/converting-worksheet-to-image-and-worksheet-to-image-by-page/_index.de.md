---
title: Arbeitsblatt in Bild umwandeln und Arbeitsblatt Seitenweise in Bilder umwandeln mit C++
linktitle: Arbeitsblatt in Bild und Arbeitsblatt in Bild pro Seite konvertieren
type: docs
weight: 80
url: /de/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
description: Lernen Sie, wie Sie ein Arbeitsblatt in eine Bilddatei umwandeln und ein mehrseitiges Arbeitsblatt seitenweise in Bilddateien umwandeln mit Aspose.Cells und C++.
---

{{% alert color="primary" %}}

Dieses Dokument ist dafür vorgesehen, Entwicklern ein detailliertes Verständnis darüber zu vermitteln, wie ein Arbeitsblatt in eine Bilddatei umgewandelt wird und wie ein mehrseitiges Arbeitsblatt seitenweise in Bilddateien umgewandelt wird.

Manchmal müssen Arbeitsblätter als Bilder präsentiert werden, zum Beispiel um sie in Anwendungen oder Webseiten zu verwenden. Sie müssen die Bilder möglicherweise in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Im Grunde genommen möchten Sie das Arbeitsblatt als Bild rendern. Aspose.Cells unterstützt die Umwandlung von Arbeitsblättern in Microsoft Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells die Umwandlung eines Arbeitsmappen in mehrere Bilddateien, eine pro Seite.

Sie könnten Office-Automatisierung verwenden, um dies zu erreichen, aber Office-Automatisierung hat ihre eigenen Nachteile. Es gibt verschiedene Gründe und Probleme: z.B. Sicherheit, Stabilität, Skalierbarkeit/Schnelligkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, aber der Hauptgrund ist, dass Microsoft selbst dringend von Office-Automatisierung abrät.

{{% /alert %}}

## **Verwendung von Aspose.Cells zum Konvertieren eines Arbeitsblatts in eine Bilddatei**

In diesem Artikel wird gezeigt, wie man eine Konsolenanwendung in Visual Studio erstellt, ein Arbeitsblatt in ein Bild konvertiert und ein Arbeitsblatt mit wenigen und einfachsten Codezeilen in ein Bild pro Arbeitsblatt umwandelt, indem man die Aspose.Cells API verwendet.

Sie müssen den [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)-Namespace in Ihr Programm/Ihr Projekt einbinden. Er enthält mehrere wertvolle Klassen, wie [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) und so weiter. Die [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)-Klasse repräsentiert ein Arbeitsblatt zum Rendern von Bildern für das Arbeitsblatt und hat eine überladene [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)-Methode, die ein Arbeitsblatt direkt mit beliebigen Attributen oder Optionen in Bilddateien umwandeln kann. Sie kann ein `System.Drawing.Bitmap`-Objekt zurückgeben, und Sie können eine Bilddatei auf die Festplatte/den Stream speichern. Verschiedene Bildformate werden unterstützt, z.B. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF und andere.

Dieser Artikel erklärt, wie:

- Ein Arbeitsblatt in ein Bild konvertiert wird
- Jede Seite in einem Arbeitsblatt in ein Bild konvertiert wird

Diese Aufgabe zeigt, wie man Aspose.Cells verwendet, um ein Arbeitsblatt aus einer Vorlagenarbeitsmappe in eine Bilddatei zu konvertieren.

### **Setup-Projekt**

1. Zuerst [laden Sie Aspose.Cells for C++ herunter](https://downloads.aspose.com/cells/cpp).
1. Installieren Sie es auf Ihrem Entwicklungssystem. Alle [Aspose](http://www.aspose.com/)-Komponenten funktionieren im Evaluierungsmodus. Der Evaluierungsmodus hat keine Zeitbegrenzung und fügt nur Wasserzeichen in die erzeugten Dokumente ein. Öffnen Sie jetzt Visual Studio und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel verwendet eine C++-Konsolenanwendung. Fügen Sie eine Referenz zu Aspose.Cells im erstellten Projekt hinzu.

### **Arbeitsblatt in Bilddatei konvertieren**

Ich habe eine neue Arbeitsmappe in Microsoft Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt: **Testbook.xlsx** (1 Arbeitsblatt). Konvertieren Sie als Nächstes das Arbeitsblatt Sheet1 der Vorlagendatei in eine Bilddatei namens SheetImage.jpg.

Nachfolgend ist der von der Komponente verwendete Code, um die Aufgabe zu erledigen. Es konvertiert Sheet1 in **Testbook.xlsx** in eine Bilddatei, um zu erklären, wie einfach diese Konvertierung ist.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

std::string convert_u16_to_string(const U16String& u16str);

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheettoImageFile.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetImageType(ImageType::Jpeg);

    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputConvertWorksheettoImageFile.jpg");

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Verwendung von Aspose.Cells zur Konvertierung eines Arbeitsblatts in eine Bilddatei nach Seite**

Dieses Beispiel zeigt, wie man Aspose.Cells verwendet, um ein Arbeitsblatt aus einer Vorlagenarbeitsmappe, die mehrere Seiten hat, in eine Bilddatei pro Seite zu konvertieren.

### **Arbeitsblatt seitenweise in Bild umwandeln**

Ich habe eine neue Arbeitsmappe in Microsoft Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt: **Testbook2.xlsx** (1 Arbeitsblatt).

Konvertieren Sie jetzt das Arbeitsblatt Sheet1 der Vorlagendatei in Bilddateien (eine Datei pro Seite). Da ich die Konsolenanwendung bereits erstellt habe, um die Kopieraufgabe auszuführen, werde ich diese Schritte zur Erstellung der Konsolenanwendung überspringen und direkt zu den Arbeitsblattkonvertierungsschritten übergehen.

Der folgende Code wird vom Component zum Erreichen der Aufgabe verwendet. Er wandelt Sheet1 in Testbook2.xlsx in Bilder nach Seitenzahl um.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

std::u16string intToU16String(int value) {
    std::u16string result;
    if (value == 0) {
        result.push_back(u'0');
        return result;
    }
    while (value > 0) {
        result.insert(result.begin(), static_cast<char16_t>(u'0' + (value % 10)));
        value /= 10;
    }
    return result;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::u16string pageNum = intToU16String(j + 1);
        U16String fileName = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + U16String(pageNum.c_str()) + U16String(u".tif");
        sr.ToImage(j, fileName);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
