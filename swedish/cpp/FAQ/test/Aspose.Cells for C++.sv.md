# C++ Bibliotek för Excel-filformat

![Version 23.11.0](https://img.shields.io/badge/nuget-v23.11.0-blue) ![NuGet](https://img.shields.io/nuget/dt/Aspose.Cells.Cpp)

[![banner](https://raw.githubusercontent.com/Aspose/aspose.github.io/master/img/banners/aspose_cells-for-cpp-banner.png)](https://releases.aspose.com/cells/cpp/)

[Produktsida](https://products.aspose.com/cells/cpp/) | [Dokumentation](https://docs.aspose.com/cells/cpp/) | [Demo](https://products.aspose.app/cells/family) | [API-referens](https://reference.aspose.com/cells/cpp) | [Exempel](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blogg](https://blog.aspose.com/category/cells/) | [Utgåvor](https://releases.aspose.com/cells/cpp/) | [Gratis support](https://forum.aspose.com/c/cells) | [Tillfällig licens](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for C++](https://products.aspose.com/cells/cpp/) är ett nativt C++-bibliotek för att skapa, manipulera, bearbeta och konvertera Microsoft Excel-filer utan att behöva Microsoft Office eller Automation. Excel C++ API:et stödjer Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML och andra format som CSV, TSV med mera.

Det tillåter utvecklare att arbeta med kalkylbladsrader, kolumner, data, formler, pivot-tabeller, arbetsblad, tabeller, diagram och ritobjekt från sina egna C++-applikationer.

## Vad är Aspose.Cells for C++?

Aspose.Cells for C++ är ett inbyggt C++-API för att integrera funktioner för skapande, bearbetande och konvertering av kalkylblad i dina C++-appar. Det stödjer arbete med många populära kalkylbladsfilformat från Microsoft Excel (XLS, XLSX, XLSB, CSV med mera) och OpenOffice/LibreOffice (ODS).

Du kan använda Aspose.Cells for C++ för att utveckla 64-bitarsapplikationer i vilken utvecklingsmiljö som helst som stöder C++, till exempel Microsoft Visual Studio. Aspose.Cells for C++ är en nativ samling som kan distribueras genom enkel kopia. Du behöver inte oroa dig för andra tjänster eller moduler.

Aspose.Cells for C++ låter dig arbeta med inbyggda såväl som anpassade dokumentegenskaper i Microsoft Excel. Stödjer högkvalitativ konvertering av Excel-arbetsböcker till PDF/A-kompatibla filer. Arbeta med formler, pivot-tabeller, arbetsblad, tabeller, områden, diagram, OLE-objekt och mycket mer.

## Funktioner för bearbetning av Excel-filer

- Öppna en kalkylbladsfil utan Microsoft Excel.
- [Öppna en Excelfil](https://docs.aspose.com/cells/cpp/different-ways-to-open-files/) via en sökväg på den lokala datorn eller med hjälp av en ström.
- [Konvertera arbetsblad](https://docs.aspose.com/cells/cpp/converting-worksheet-to-different-image-formats/) till olika bildformat.
- [Tillämpa villkorlig formatering](https://docs.aspose.com/cells/cpp/apply-conditional-formatting-in-worksheet/) enligt ditt val.
- [Manipulera pivot-tabeller](https://docs.aspose.com/cells/cpp/manipulate-pivot-table/) i dina kalkylblad.
- [Konvertera tabell till område](https://docs.aspose.com/cells/cpp/tables-and-ranges/) utan att förlora formatering.
- Hämta en cells namn genom att ange rad- och kolumnindex, på liknande sätt, [hämta rad- och kolumnindex för cellen](https://docs.aspose.com/cells/cpp/names-and-indices/) från dess namn.
- Skapa [Pyramid-diagram, Linjediagram, Bubbel-diagram](https://docs.aspose.com/cells/cpp/creating-and-customizing-charts/), eller ett anpassat diagram.
- [Rendera](https://docs.aspose.com/cells/cpp/chart-rendering/) stödda diagramtyper till bilder eller PDF.
- [Lägg till ett OLE-objekt i kalkylarket](https://docs.aspose.com/cells/cpp/inserting-ole-objects-into-the-worksheet/).
- Få åtkomst till alla OLE-objekt som finns i kalkylarket för [utvinning](https://docs.aspose.com/cells/cpp/extracting-ole-objects-from-worksheet/).

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

Är du redo att prova Aspose.Cells for C++? Kör helt enkelt `Install-Package Aspose.Cells.Cpp` från Package Manager Console i Visual Studio för att hämta NuGet-paketet. Om du redan har Aspose.Cells for C++ och vill uppgradera versionen, kör `Update-Package Aspose.Cells.Cpp` för att få den senaste versionen.

### Konvertera XLS till XLSX, XLSB & CSV med C++

Försök att köra koden nedan för att se hur API fungerar i din miljö eller kolla in [GitHub Repository](https://github.com/aspose-cells/Aspose.Cells-for-C) för andra vanliga användningsfall.

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

### Skapa en anpassad Excel-diagram med C++

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

[Produktsida](https://products.aspose.com/cells/cpp/) | [Dokumentation](https://docs.aspose.com/cells/cpp/) | [Demo](https://products.aspose.app/cells/family) | [API-referens](https://reference.aspose.com/cells/cpp) | [Exempel](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blogg](https://blog.aspose.com/category/cells/) | [Utgåvor](https://releases.aspose.com/cells/cpp/) | [Gratis support](https://forum.aspose.com/c/cells) | [Tillfällig licens](https://purchase.aspose.com/temporary-license/)
{{< app/cells/assistant language="cpp" >}}
