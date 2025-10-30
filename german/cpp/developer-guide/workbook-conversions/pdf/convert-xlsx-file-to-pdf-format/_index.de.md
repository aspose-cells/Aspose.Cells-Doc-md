---
title: XLSX Datei in PDF Format mit C++ konvertieren
linktitle: XLSX Datei in PDF Format konvertieren
type: docs
weight: 30
url: /de/cpp/convert-xlsx-file-to-pdf-format/
description: Erfahren Sie, wie Sie Excel Dateien mit Aspose.Cells for C++ in hoher Präzision und Genauigkeit in PDF Format konvertieren.
---

{{% alert color="primary" %}}

PDF (Portable Document Format) repräsentiert Dokumente unabhängig von der verwendeten Software, Hardware und dem Betriebssystem, um diese Dokumente zu erstellen. Eine PDF-Datei kann beliebige Kombinationen aus Text, Grafiken und Bildern in einer geräte- und auflösungsunabhängigen Weise enthalten. PDF-Dateien werden häufig komprimiert, sodass sie weniger Platz als die Originaldatei benötigen.

Manchmal müssen Sie eine Microsoft Excel-Datei in PDF konvertieren. Dafür benötigen Sie eine schnelle, sichere, genaue und zuverlässige Lösung, mit der Sie PDF-Dokumente weltweit verteilen können. Es gibt zahlreiche Konvertierungstools, die diese Aufgabe ausführen können. Aber Sie müssen sicherstellen, dass das Layout des ursprünglichen Excel-Dokuments im Ausgabepdf beibehalten wird. Bilder, Diagramme, Formen, Datenformatierung, Schriftarten, Attribute, Farben, Seiteneinrichtungsoptionen, Textausrichtung, Rahmen, Diagramme usw. sollten präzise und genau wiedergegeben werden. [Aspose.Cells](https://products.aspose.com/cells/cpp/) sorgt für eine hochwertige Konvertierung.

Dieses Dokument soll ein umfassendes Verständnis darüber vermitteln, wie ein Microsoft Excel-Dokument (mit Bildern, Diagrammen, Formatierungen usw.) in PDF umgewandelt werden kann. Dazu wird gezeigt, wie man eine einfache Konsolenanwendung in C++ erstellt, die eine Excel-Datei mit Aspose.Cells API in PDF umwandelt. Die Konvertierung erfolgt mit hohem Präzisions- und Genauigkeitsgrad.

{{% /alert %}}

## **Konvertierung von Excel nach PDF**

Dieses Beispiel verwendet eine Excel-Datei (SampleInput.xlsx) als Vorlage. Die Arbeitsmappe enthält Arbeitsblätter mit Diagrammen und Bildern. Jedes Arbeitsblatt enthält verschiedene Typen von Formaten unter Verwendung von Schriftarten, Attributen, Farben, Schattierungseffekten und Rahmen. Auf dem ersten Arbeitsblatt befindet sich ein Säulendiagramm und auf dem letzten ein Bild.

### **Die Vorlagen Excel-Datei**

Die Vorlage-Datei verfügt über drei Arbeitsblätter, darunter Diagramme und Bilder als Medien. Das erste Arbeitsblatt enthält Diagramme, und das letzte Arbeitsblatt ein Bild, wie in den Bildschirmaufnahmen gezeigt.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Das erste Arbeitsblatt **(Umsatzprognose)**|Das zweite Arbeitsblatt **(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Das dritte Arbeitsblatt **(Dateneingabe)**|Das letzte Arbeitsblatt **(Bild)**|

### **Konvertierungsprozess**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    try
    {
        // Get the template excel file path
        U16String designerFile = srcDir + u"SampleInput.xlsx";

        // Specify the pdf file path
        U16String pdfFile = outDir + u"Output.out.pdf";

        // Open the template excel file
        Workbook wb(designerFile);

        // Save the pdf file
        wb.Save(pdfFile, SaveFormat::Pdf);

        std::cout << "PDF file saved successfully!" << std::endl;
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Wenn die Tabelle Formeln enthält, ist es am besten, die Methode [Workbook.CalculateFormula](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) direkt vor der Umwandlung der Tabelle in PDF aufzurufen. Dadurch werden Formelabhängige Werte neu berechnet, und die korrekten Werte werden im PDF angezeigt.

{{% /alert %}}

### **Ergebnis**

Wenn der obige Code ausgeführt wurde, wird eine PDF-Datei im Ordner Files im Anwendungsverzeichnis erstellt.
Die folgenden Screenshots zeigen die PDF-Seiten. Beachten Sie, dass Kopf- und Fußzeilen auch in der Ausgabe-PDF-Datei beibehalten werden.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Das erste Arbeitsblatt **(Umsatzprognose)**|Das zweite Arbeitsblatt **(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Das dritte Arbeitsblatt **(Dateneingabe)**|Das letzte Arbeitsblatt **(Bild)**|
{{< app/cells/assistant language="cpp" >}}
