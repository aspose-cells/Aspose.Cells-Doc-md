---
title: Numerische Textdaten in Zahlen umwandeln mit C++
linktitle: Ändern von Text Daten in Zahlen
type: docs
weight: 900
url: /de/cpp/convert-text-numeric-data-to-number/
description: Lernen Sie, wie Sie in Excel gespeicherte Zahlen, die als Text vorliegen, mit der Aspose.Cells for C++ API in Zahlen umwandeln.
keywords: Excel Text in Zahl umwandeln, Excel Text in Zahl umwandeln C++, Excel Numerische Textdaten in Zahl umwandeln, Excel Numerische Textdaten in Zahl umwandeln C++, Excel Numerischen Text in Zahl umwandeln, Excel Numerischen Text in Zahl umwandeln C++, Excel Numerischen Text mit C++ in Zahl umwandeln, Numerischen Text in Excel in Zahl umwandeln mit C++, Numerischen Text in Excel in Zahl umwandeln mit C++, Numerischen String in Zahl in Excel umwandeln mit C++, Excel Numerische Textdaten in Zahl umwandeln, Excel Numerischen String in Zahl C++
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie numerische Daten, die als Text eingegeben wurden, in Zahlen umwandeln. Sie können Zahlen als Text in Microsoft Excel eingeben, indem Sie eine Apostroph vor einer Zahl setzen, zum Beispiel **'12345**. Excel behandelt die Zahl dann als Zeichenfolge. Aspose.Cells ermöglicht es Ihnen, Zeichenfolgen in Zahlen umzuwandeln.

## Wie man in Excel Zahlen, die als Text gespeichert sind, in Zahlen umwandelt
Sie können Zahlen, die als Text gespeichert sind, in Zahlen umwandeln, indem Sie ein paar einfache Schritte befolgen.
1. Wählen Sie eine einzelne Zelle oder einen Zellenbereich aus, der oben links einen Fehlerindikator hat.
1. Klicken Sie neben der ausgewählten Zelle oder dem ausgewählten Zellenbereich auf die Schaltfläche für den Fehler, die erscheint. Klicken Sie im Menü auf In Zahl umwandeln. 
<br>
<img src="4.png" width=70% />
1. Wenn die Warnschaltfläche nicht verfügbar ist, wählen Sie eine Spalte mit diesem Problem aus. Wenn Sie nicht die ganze Spalte konvertieren möchten, können Sie stattdessen eine oder mehrere Zellen auswählen. Stellen Sie nur sicher, dass die von Ihnen ausgewählten Zellen sich in derselben Spalte befinden, andernfalls funktioniert dieser Vorgang nicht. Die Option Text in Spalten wird in der Regel zum Aufteilen einer Spalte verwendet, aber sie kann auch dazu verwendet werden, eine einzelne Spalte von Text in Zahlen umzuwandeln. Klicken Sie auf der Registerkarte Daten auf Text in Spalten.
<br>
<img src="1.png" width=70% />
1. Klicken Sie in dem Popup-Fenster auf die Schaltfläche Fertig stellen.
<br>
<img src="2.png" width=70% />
1. Die als Text gespeicherten Zahlen werden in Zahlen umgewandelt.
<br>
<img src="3.png" width=70% />

## Wie man numerische Daten, die als Text gespeichert sind, mit Aspose.Cells for C++ in Zahlen umwandelt
Aspose.Cells bietet die Methode [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/), die verwendet werden kann, um alle Zeichenfolgen oder textuellen numerischen Daten in Zahlen umzuwandeln.

Im folgenden Screenshot sind Zeichenfolgenzahlen in Zellen **A1:A17** zu sehen. Die Zeichenfolgenzahlen sind linksbündig ausgerichtet.
<br>
<img src="5.png" width=70% />

Diese Zeichenfolgenzahlen wurden in der folgenden Bildschirmaufnahme mithilfe von [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/) in Zahlen umgewandelt. Wie Sie sehen können, sind sie jetzt rechtsbündig.
<br>
<img src="6.png" width=70% />

## C++ Code zur Umwandlung von numerischen Strings in tatsächliche Zahlen

Der folgende Beispielcode veranschaulicht, wie man alle numerischen Zeichenfolgendaten in allen Arbeitsblättern in tatsächliche Zahlen umwandelt.

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

    // Instantiate workbook object with an Excel file
    U16String inputFilePath = srcDir + u"SampleBook.xlsx";
    Workbook workbook(inputFilePath);

    // Iterate through all worksheets and convert string values to numeric
    for (int32_t i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        workbook.GetWorksheets().Get(i).GetCells().ConvertStringToNumericValue();
    }

    // Save the Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
