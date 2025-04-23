# Go-Bibliothek für Excel-Dateiformate

![Version 24.11.0](https://img.shields.io/badge/go-v24.11.0-blue)

[Produktseite](https://products.aspose.com/cells/go-cpp/) | [Dokumentation](https://docs.aspose.com/cells/go-cpp/) | [Demos](https://products.aspose.app/cells/family) | [API-Referenz](https://reference.aspose.com/cells/go-cpp) | [Beispiele](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blog](https://blog.aspose.com/category/cells/) | [Veröffentlichungen](https://releases.aspose.com/cells/go-cpp/) | [Kostenloser Support](https://forum.aspose.com/c/cells) | [Temporäre Lizenz](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for Go via C++](https://products.aspose.com/cells/go-cpp/) ist eine native Go-Bibliothek zum Erstellen, Manipulieren, Verarbeiten und Konvertieren von Microsoft Excel-Dateien, ohne Microsoft Office oder Automation zu benötigen. Die Excel Go API unterstützt Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML und andere Formate wie CSV, TSV und mehr.

Ermöglicht es Entwicklern, mit Zeilen, Spalten, Daten, Formeln, Pivot-Tabellen, Arbeitsblättern, Tabellen, Diagrammen und Zeichenobjekten in Tabellenkalkulationen aus eigenen Go-Anwendungen zu arbeiten.

## Was ist Aspose.Cells for Go via C++?

Aspose.Cells for Go via C++ ist eine native Go-On-Premise-API, um Funktionen zur Erstellung, Manipulation und Konvertierung von Tabellenkalkulationen in Ihre Go-Apps zu integrieren. Es unterstützt die Arbeit mit vielen gängigen Tabellenkalkulationsdateiformaten von Microsoft Excel (XLS, XLSX, XLSB, CSV usw.) und OpenOffice/LibreOffice (ODS).

Sie können Aspose.Cells for Go via C++ verwenden, um 64-Bit-Anwendungen in jeder Entwicklungsumgebung zu entwickeln, die Go unterstützt, wie z.B. Microsoft Visual Studio. Aspose.Cells for Go via C++ ist eine native Assembly, die einfach durch Kopieren bereitgestellt werden kann. Sie müssen sich keine Sorgen um andere Dienste oder Module machen.

Aspose.Cells for Go via C++ ermöglicht die Arbeit mit den integrierten sowie benutzerdefinierten Dokumenteigenschaften in Microsoft Excel. Unterstützt hochwertige Konvertierung von Excel-Arbeitsmappen in PDF/A-konforme Dateien. Arbeiten Sie mit Formeln, Pivot-Tabellen, Arbeitsblättern, Tabellen, Bereichen, Diagrammen, OLE-Objekten und vielem mehr.

## Funktionen zur Verarbeitung von Excel-Dateien

- Öffnen Sie eine Tabellenkalkulationsdatei ohne Microsoft Excel.
- [Öffnen Sie eine Excel-Datei](https://docs.aspose.com/cells/go/different-ways-to-open-files/) über einen Pfad auf dem lokalen Computer oder mit einem Stream.
- [Konvertieren Sie ein Arbeitsblatt](https://docs.aspose.com/cells/go/converting-worksheet-to-different-image-formats/) in verschiedene Bildformate.
- [Wenden Sie bedingte Formatierungen an](https://docs.aspose.com/cells/go/apply-conditional-formatting-in-worksheet/) nach Ihren Vorgaben.
- [Manipulieren Sie Pivot-Tabellen](https://docs.aspose.com/cells/go/manipulate-pivot-table/) in Ihren Tabellen.
- [Konvertieren Sie Tabellen in Bereiche](https://docs.aspose.com/cells/go/tables-and-ranges/) ohne Formatierungsverlust.
- Holen Sie sich den Namen einer Zelle, indem Sie die Zeilen- und Spaltenindizes angeben, oder similarly, [holen Sie Zeilen- und Spaltenindizes der Zelle](https://docs.aspose.com/cells/go/names-and-indices/) anhand ihres Namens.
- Erstellen Sie [Pyramiden-, Linien- oder Blasendiagramme](https://docs.aspose.com/cells/go/creating-and-customizing-charts/), oder ein benutzerdefiniertes Diagramm.
- [Rendern](https://docs.aspose.com/cells/go/chart-rendering/) unterstützter Diagrammtypen in Bilder oder PDF.
- [Fügen Sie ein OLE-Objekt in das Arbeitsblatt ein](https://docs.aspose.com/cells/go/inserting-ole-objects-into-the-worksheet/).
- Greifen Sie auf alle im Arbeitsblatt enthaltenen OLE-Objekte zu, um sie zu [extrahieren](https://docs.aspose.com/cells/go/extracting-ole-objects-from-worksheet/).

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

Sind Sie bereit, Aspose.Cells for Go via C++ auszuprobieren? Führen Sie einfach `go get -u github.com/aspose-cells/aspose-cells-go-cpp` aus und importieren Sie `github.com/aspose-cells/aspose-cells-go-cpp` in Ihre Go-Datei. Wenn Sie bereits Aspose.Cells for Go via C++ haben und die Version aktualisieren möchten, führen Sie `go get github.com/aspose-cells/aspose-cells-go-cpp@v24.12.0` aus, um die neueste Version zu erhalten.

### Konvertieren Sie XLS zu XLSX, XLSB & CSV mit Go

Versuchen Sie, das folgende Snippet auszuführen, um zu sehen, wie die API in Ihrer Umgebung funktioniert, oder prüfen Sie das [GitHub-Repository](https://github.com/aspose-cells/aspose-cells-go-cpp) für weitere häufige Verwendungsszenarien.

```Go
lic, _ := NewLicense()
lic.SetLicense_String(os.Getenv("LicensePath"))
workbook, err1 := NewWorkbook_String("Book1.xlsx")
if err1 != nil {
    println(err1)
}
workbook.Save_String("Book1.pdf")
workbook.Save_String("Book1.png")
workbook.Save_String("Book1.txt")
workbook.Save_String("Book1.ods")
workbook.Save_String("Book1.md")
workbook.Save_String("Book1.json")
workbook.Save_String("Book1.html")
```

### Erstellen Sie ein benutzerdefiniertes Excel-Diagramm mit Go

```Go
package main

import (
 . "asposecells"
 "os"
)

func main() {
 lic, _ := NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

 workbook, _ := NewWorkbook()
 worksheets, _ := workbook.GetWorksheets()
 worksheet, _ := worksheets.Get_Int(0)
 cells, _ := worksheet.GetCells()
 cell, _ := cells.Get_String("A1")
 cell.PutValue_Int(50)
 cell, _ = cells.Get_String("A2")
 cell.PutValue_Int(100)
 cell, _ = cells.Get_String("A3")
 cell.PutValue_Int(150)
 cell, _ = cells.Get_String("B1")
 cell.PutValue_Int(4)
 cell, _ = cells.Get_String("B2")
 cell.PutValue_Int(20)
 cell, _ = cells.Get_String("B3")
 cell.PutValue_Int(50)
 charts, _ := worksheet.GetCharts()
 chartIndex, _ := charts.Add_ChartType_Int_Int_Int_Int(ChartType_Pyramid, 5, 0, 20, 8)
 chart, _ := charts.Get_Int(chartIndex)
 series, _ := chart.GetNSeries()
 series.Add_String_Bool("A1:B3", true)
 workbook.Save_String("CreateChart.xlsx")
}

```

[Produktseite](https://products.aspose.com/cells/go-cpp/) | [Dokumentation](https://docs.aspose.com/cells/go-cpp/) | [Demos](https://products.aspose.app/cells/family) | [API-Referenz](https://reference.aspose.com/cells/go-cpp) | [Beispiele](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blog](https://blog.aspose.com/category/cells/) | [Veröffentlichungen](https://releases.aspose.com/cells/go-cpp/) | [Kostenloser Support](https://forum.aspose.com/c/cells) | [Temporäre Lizenz](https://purchase.aspose.com/temporary-license/)
