# C++-Bibliothek für Excel-Dateiformate

![Version 23.11.0](https://img.shields.io/badge/nuget-v23.11.0-blue) ![NuGet](https://img.shields.io/nuget/dt/Aspose.Cells.Cpp)

[![banner](https://raw.githubusercontent.com/Aspose/aspose.github.io/master/img/banners/aspose_cells-for-cpp-banner.png)](https://releases.aspose.com/cells/cpp/)

[Produktseite](https://products.aspose.com/cells/cpp/) | [Dokumentation](https://docs.aspose.com/cells/cpp/) | [Demos](https://products.aspose.app/cells/family) | [API-Referenz](https://reference.aspose.com/cells/cpp) | [Beispiele](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blog](https://blog.aspose.com/category/cells/) | [Veröffentlichungen](https://releases.aspose.com/cells/cpp/) | [Kostenlose Unterstützung](https://forum.aspose.com/c/cells) | [Temporäre Lizenz](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for C++](https://products.aspose.com/cells/cpp/) ist eine native C++-Bibliothek für das Erstellen, Manipulieren, Verarbeiten und Konvertieren von Microsoft Excel? Dateien ohne Microsoft Office? oder Automation zu benötigen. Die Excel C++ API unterstützt Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML und andere Formate wie CSV, TSV und mehr.

Es ermöglicht Entwicklern, mit Tabellenzeilen, Spalten, Daten, Formeln, Pivot-Tabellen, Arbeitsblättern, Tabellen, Diagrammen und Zeichenobjekten aus ihren eigenen C++-Anwendungen zu arbeiten.

## Was ist Aspose.Cells for C++?

Aspose.Cells for C++ ist eine native C++-On-Premise-API zur Integration von Funktionen zur Erstellung, Manipulation und Konvertierung von Tabellenkalkulationen in Ihre C++-Apps. Es unterstützt die Arbeit mit vielen gängigen Tabellenkalkulationsdateiformaten von Microsoft Excel (XLS, XLSX, XLSB, CSV usw.) und OpenOffice/LibreOffice (ODS).

Sie können Aspose.Cells for C++ verwenden, um 64-Bit-Anwendungen in jeder Entwicklungsumgebung zu entwickeln, die C++ unterstützt, wie z.B. Microsoft Visual Studio. Aspose.Cells for C++ ist eine native Assembly, die einfach durch Kopieren bereitgestellt werden kann. Sie müssen sich keine Gedanken über andere Dienste oder Module machen.

Aspose.Cells for C++ ermöglicht es Ihnen, mit den integrierten sowie den benutzerdefinierten Dokumenteigenschaften in Microsoft Excel zu arbeiten. Es unterstützt die hochwertige Konvertierung von Excel-Arbeitsmappen in PDF/A-konforme Dateien. Arbeiten Sie mit Formeln, Pivot-Tabellen, Arbeitsblättern, Tabellen, Bereichen, Diagrammen, OLE-Objekten und vielem mehr.

## Funktionen zur Verarbeitung von Excel-Dateien

- Öffnen Sie eine Tabellenkalkulationsdatei ohne Microsoft Excel.
- [Öffnen Sie eine Excel-Datei](https://docs.aspose.com/cells/cpp/different-ways-to-open-files/) über einen Pfad auf dem lokalen Computer oder mit einem Stream.
- [Konvertieren Sie Arbeitsblätter](https://docs.aspose.com/cells/cpp/converting-worksheet-to-different-image-formats/) in verschiedene Bildformate.
- [Wenden Sie bedingte Formatierung an](https://docs.aspose.com/cells/cpp/apply-conditional-formatting-in-worksheet/) nach Ihrer Wahl an.
- [Manipulieren Sie Pivot-Tabellen](https://docs.aspose.com/cells/cpp/manipulate-pivot-table/) in Ihren Tabellenkalkulationen.
- [Konvertieren Sie Tabellen in Bereich](https://docs.aspose.com/cells/cpp/tables-and-ranges/) ohne Formatierung zu verlieren.
- Lesen Sie den Namen einer Zelle, indem Sie den Zeilen- und Spaltenindex angeben, ebenso [lesen Sie Zeilen- und Spaltenindex der Zelle](https://docs.aspose.com/cells/cpp/names-and-indices/) anhand ihres Namens ab.
- Erstellen Sie [Pyramiden-, Liniendiagramme, Bubble-Charts](https://docs.aspose.com/cells/cpp/creating-and-customizing-charts/) oder ein benutzerdefiniertes Diagramm.
- [Rendern](https://docs.aspose.com/cells/cpp/chart-rendering/) unterstützter Diagrammtypen zu Bildern oder PDF.
- Fügen Sie ein OLE-Objekt in das Arbeitsblatt ein](https://docs.aspose.com/cells/cpp/inserting-ole-objects-into-the-worksheet/).
- Greifen Sie auf alle im Arbeitsblatt enthaltenen OLE-Objekte zu und [extrahieren Sie sie](https://docs.aspose.com/cells/cpp/extracting-ole-objects-from-worksheet/).

## Unterstützte Lese- und Schreibformate

**Microsoft Excel:** XLS, XLSX, XLSB, SpreadsheetML\
**Text:** CSV, TSV, TabDelimited\
**OpenDocument:** ODS\
**Andere:** HTML, MHTML

## Speichern von Tabellendokumenten als

**Microsoft Excel:** XLSM, XLTX, XLTM, XLAM\
**Portable Document Format:** PDF, XPS\
**Text:** CSV, TSV, TabDelimited\
**Bilder:** SVG, JPEG, PNG, BMP, GIF\
**Web:** HTML, MHTML\
**Metafile:** EMF\
**Sonstige** DIF

## Erste Schritte

Sind Sie bereit, Aspose.Cells for C++ auszuprobieren? Führen Sie einfach `Install-Package Aspose.Cells.Cpp` von der Package Manager Console in Visual Studio aus, um das NuGet-Paket zu erhalten. Wenn Sie bereits Aspose.Cells for C++ haben und die Version aktualisieren möchten, führen Sie bitte `Update-Package Aspose.Cells.Cpp` aus, um die neueste Version zu erhalten.

### Konvertieren von XLS in XLSX, XLSB & CSV mit C++

Versuchen Sie, den folgenden Codeausschnitt auszuführen, um zu sehen, wie die API in Ihrer Umgebung funktioniert, oder prüfen Sie das [GitHub-Repository](https://github.com/aspose-cells/Aspose.Cells-for-C) für andere gängige Anwendungsszenarien.

```c++
U16String dir(u"your path");
// load the file to be converted
Workbook book(dir + u"template.xls");
// save in different formats
book.Save(dir + u"output.xlsx", SaveFormat::Xlsx);
book.Save(dir + u"output.xlsb", SaveFormat::Xlsb);
book.Save(dir + u"output.csv", SaveFormat::CSV);
book.Save(dir + u"output.json", SaveFormat::Json);
```

### Erstellen eines benutzerdefinierten Excel-Diagramms mit C++

```c++
// create a new workbook
Workbook workbook;

// get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// add sample data
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"A4").PutValue(110);
worksheet.GetCells().Get(u"B1").PutValue(260);
worksheet.GetCells().Get(u"B2").PutValue(12);
worksheet.GetCells().Get(u"B3").PutValue(50);
worksheet.GetCells().Get(u"B4").PutValue(100);

// add a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// access the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// add SeriesCollection (chart data source) to the chart ranging from A1 to B4
chart.GetNSeries().Add(u"A1:B4", true);

// set the chart type of 2nd NSeries to display as line chart
chart.GetNSeries().Get(1).SetType(
	Aspose::Cells::Charts::ChartType::Line);

// save the Excel file
workbook.Save(u"output.xlsx");
```

[Produktseite](https://products.aspose.com/cells/cpp/) | [Dokumentation](https://docs.aspose.com/cells/cpp/) | [Demos](https://products.aspose.app/cells/family) | [API-Referenz](https://reference.aspose.com/cells/cpp) | [Beispiele](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blog](https://blog.aspose.com/category/cells/) | [Veröffentlichungen](https://releases.aspose.com/cells/cpp/) | [Kostenlose Unterstützung](https://forum.aspose.com/c/cells) | [Temporäre Lizenz](https://purchase.aspose.com/temporary-license/)
