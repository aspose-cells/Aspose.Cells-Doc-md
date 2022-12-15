---
title: Aspose.Cells for .NET 22.8 Release Notes
type: docs
weight: 5
url: /sv/net/aspose-cells-for-net-22-8-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 22.8](https://www.nuget.org/packages/Aspose.Cells/22.8.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-51589|Stöd expandera/komprimera knappstil för pivottabell|
|CELLSNET-51473|Konvertera trådade kommentarer till html|
|CELLSNET-51570|Kopiera radhöjd när du bearbetar smarta markörer för en tabell|
|CELLSNET-51590|Ta bort grupperade former från gruppen|
|CELLSNET-51595|Fel vertikal justering av celltext vid konvertering till PDF från Excel-fil med pivottabell|
|CELLSNET-51621|Delade formler kopierades felaktigt för olika filformat|
|CELLSNET-51524|Fel radbrytning vid konvertering till PDF från Excel-fil med pivottabell|
|CELLSNET-51675|Form går förlorad vid konvertering till pdf|
|CELLSNET-51435|Nya kalkylbladsrelationer läggs till när en XLSB-arbetsbok konverteras till XLSM|
|CELLSNET-51545|Arbetsbok med MS Excel 5.0-dialogblad kunde inte laddas av Aspose.Cells|
|CELLSNET-51546|Diagram dupliceras efter att ha öppnats och sparats med Aspose-celler och sedan visas i Excel|
|CELLSNET-51550|Länkar i namngivna intervall tas bort i XLS till XLSM-konvertering|
|CELLSNET-51551|Filer blev skadade och extern länk ändrades till DDE-länk när XLS-filer konverterades till XLSM|
|CELLSNET-51558|Konvertering av XLS-filer med länk av typen xlAlternateStartup till XLSM matar ut skadade filer|
|CELLSNET-51564|Duplicera data av smart markör|
|CELLSNET-51574|En textruta med två kolumner i den återges med en kolumn endast när en XLSX-fil sparas på nytt|
|CELLSNET-51580|En extern länk av typen xlPathMissing ändras till normal externLinkPath-typ i XLS till XLSM-konvertering|
|CELLSNET-51599|Mycket långa namn för bildtypsresurser samtidigt som de sparas som HTML|
|CELLSNET-51627|Specifik XLSM-fil kan inte laddas|
|CELLSNET-51632|RibbonXml fungerar inte|
|CELLSNET-51696|Att konvertera XLS till XLSM ändrar egenskapen "Spara lösenord" som dataanslutningsdefinition|
|CELLSNET-51559|Konvertera en XLSB-fil till XLSM med undantag "startIndex kan inte vara större än längden på strängen"|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägg till metoden FontSettingCollection.Replace().**

Byt ut formens text.

### **Lägg till egenskapen ShapeTextAlignment.NumberOfColumns.**

Hämtar och ställer in antalet kolumner i formens text.

### **Lägg till egenskapen HtmlSaveOptions.ExportCommentsType.**

Hämtar och ställer in typen av exportkommentarer till html.

### **Lägg till basklassen PagineradeSaveOptions för PdfSaveOptions och XpsSaveOptions.**

Representerar alternativen för paginering.

### **Lägg till klass SheetSet.**

Beskriver en uppsättning ark.

### **Lägg till egendomen PaginatedSaveOptions.SheetSet.**

Hämtar eller ställer in arken att rendera.

### **Lägg till egenskapen ImageOrPrintOptions.SheetSet.**

Hämtar eller ställer in arken att rendera.

### **Lägg till egenskapen GridWeb.IgnoreStyleWithNoData.**

Hämtar eller ställer in om GridWeb ignorerar att visa rader eller kolumner som inte innehåller cellvärden men som fortfarande är formaterade

### **Föråldrad ImageOrPrintOptions.SaveFormat-egenskap.**

För Tiff/Svg, använd ImageType; För Xps, använd Workbook.Save(sträng, SaveOptions) med XpsSaveOptions.

### **Föråldrad konstruktor XpsSaveOptions(Aspose.Cells.SaveFormat saveFormat).**

Använd konstruktorn XpsSaveOptions() istället.

### **Föråldrad konstruktor SvgSaveOptions(Aspose.Cells.SaveFormat saveFormat).**

Använd konstruktorn SvgSaveOptions() istället.

### **Ta bort konstruktorn PdfSaveOptions(Aspose.Cells.SaveFormat saveFormat).**

Använd konstruktorn PdfSaveOptions() istället.
