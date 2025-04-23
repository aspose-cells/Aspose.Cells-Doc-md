# Go-bibliotek för Excel filformat

![Version 24.11.0](https://img.shields.io/badge/go-v24.11.0-blue)

[Produkt sida](https://products.aspose.com/cells/go-cpp/) | [Dokumentation](https://docs.aspose.com/cells/go-cpp/) | [Demos](https://products.aspose.app/cells/family) | [API-Referens](https://reference.aspose.com/cells/go-cpp) | [Exempel](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blogg](https://blog.aspose.com/category/cells/) | [Uppdateringar](https://releases.aspose.com/cells/go-cpp/) | [Gratis support](https://forum.aspose.com/c/cells) | [Tillfällig licens](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for Go via C++](https://products.aspose.com/cells/go-cpp/) är ett inbyggt Go-bibliotek för att skapa, manipulera, bearbeta och konvertera Microsoft Excel?-filer utan behov av Microsoft Office?- eller Automation. Excel Go API stöder Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML och andra format som CSV, TSV och fler.

Det tillåter utvecklarna att arbeta med kalkylbladrader, kolumner, data, formler, pivottabeller, kalkylblad, tabeller, diagram och ritobjekt från deras egna Go-applikationer.

## Vad är Aspose.Cells for Go via C++?

Aspose.Cells for Go via C++ är ett inbyggt Go-primärt API för att integrera funktioner för skapande, manipulation och konvertering av kalkylblad i dina Go-appar. Det stöder att arbeta med många populära filformat för kalkylblad från Microsoft Excel (XLS, XLSX, XLSB, CSV, etc.) och OpenOffice/LibreOffice (ODS).

Du kan använda Aspose.Cells for Go via C++ för att utveckla 64-bitars applikationer i alla utvecklingsmiljöer som stöder Go, till exempel Microsoft Visual Studio. Aspose.Cells for Go via C++ är en inbyggd sammansättningskod som kan distribueras genom att helt enkelt kopiera den. Du behöver inte oroa dig för andra tjänster eller moduler.

Aspose.Cells for Go via C++ tillåter dig att arbeta med de inbyggda samt de anpassade dokumentegenskaperna i Microsoft Excel. Stöder högkvalitativ konvertering av Excel-arbetsböcker till PDF/A-kompatibla filer. Arbeta med formler, pivottabeller, kalkylblad, tabeller, område, diagram, OLE-objekt och mycket mer.

## Funktioner för bearbetning av Excel-filer

- Öppna en kalkylbladsfil utan Microsoft Excel.
- [Öppna en Excel-fil](https://docs.aspose.com/cells/go/different-ways-to-open-files/) via en sökväg på den lokala datorn eller med hjälp av en ström.
- [Konvertera kalkylblad](https://docs.aspose.com/cells/go/converting-worksheet-to-different-image-formats/) till olika bildformat.
- [Använd villkorsstyrd formatering](https://docs.aspose.com/cells/go/apply-conditional-formatting-in-worksheet/) efter eget val.
- [Manipulera pivottabeller](https://docs.aspose.com/cells/go/manipulate-pivot-table/) i dina kalkylblad.
- [Konvertera tabell till område](https://docs.aspose.com/cells/go/tables-and-ranges/) utan att förlora formatering.
- Hämta ett cellnamn genom att ange rad- och kolumnindex, likaså, [hämta rad- och kolumnindex för cellen](https://docs.aspose.com/cells/go/names-and-indices/) utifrån dess namn.
- Skapa [pyramiddiagram, linjediagram, bubbladiagram](https://docs.aspose.com/cells/go/creating-and-customizing-charts/), eller ett anpassat diagram.
- [Rendera](https://docs.aspose.com/cells/go/chart-rendering/) stödda diagramtyper till bilder eller PDF.
- [Infoga ett OLE-objekt i kalkylbladet](https://docs.aspose.com/cells/go/inserting-ole-objects-into-the-worksheet/).
- Åtkomst till alla OLE-objekt i kalkylbladet för [utdrag](https://docs.aspose.com/cells/go/extracting-ole-objects-from-worksheet/).

## Stödda läs- och skrivformat

**Microsoft Excel:** XLS, XLSX, XLSB, SpreadsheetML\
**Text:** CSV, TSV, TabDelimited\
**OpenDocument:** ODS\
**Övriga:** HTML, MHTML

## Spara kalkylblad som dokument

**Microsoft Excel:** XLSM, XLTX, XLTM, XLAM\
**Portable Document Format:** PDF, XPS\
**Text:** CSV, TSV, TabDelimited\
**Bilder:** SVG, JPEG, PNG, BMP, GIF\
**Web:** HTML, MHTML\
**Metafil:** EMF\
**Övrigt** DIF

## Komma igång

Är du redo att prova Aspose.Cells for Go via C++? Kör helt enkelt `go get -u github.com/aspose-cells/aspose-cells-go-cpp` och importera `github.com/aspose-cells/aspose-cells-go-cpp` från go-filen. Om du redan har Aspose.Cells for Go via C++ och vill uppgradera versionen, kör `go get github.com/aspose-cells/aspose-cells-go-cpp@v24.12.0` för att få den senaste versionen.

### Konvertera XLS till XLSX, XLSB & CSV med Go

Prova att köra kodsnutten nedan för att se hur API:t fungerar i din miljö eller kolla in [GitHub-repositoryt](https://github.com/aspose-cells/aspose-cells-go-cpp) för andra vanliga användningsscenarier.

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

### Skapa ett anpassat Excel-diagram med Go

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

[Produkt sida](https://products.aspose.com/cells/go-cpp/) | [Dokumentation](https://docs.aspose.com/cells/go-cpp/) | [Demos](https://products.aspose.app/cells/family) | [API-Referens](https://reference.aspose.com/cells/go-cpp) | [Exempel](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blogg](https://blog.aspose.com/category/cells/) | [Uppdateringar](https://releases.aspose.com/cells/go-cpp/) | [Gratis support](https://forum.aspose.com/c/cells) | [Tillfällig licens](https://purchase.aspose.com/temporary-license/)
