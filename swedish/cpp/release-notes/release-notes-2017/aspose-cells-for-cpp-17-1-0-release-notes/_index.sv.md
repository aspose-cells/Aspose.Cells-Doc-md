---
title: Aspose.Cells för CPP 17.1.0 Release Notes
type: docs
weight: 40
url: /sv/cpp/aspose-cells-for-cpp-17-1-0-release-notes/
---
|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSCPP-35|Läs/skriv XLSM-filformat|Ny funktion|
|CELLSCPP-36|Läs/skriv CSV-filformat|Ny funktion|
|CELLSCPP-37|Läs/skriv XLSB-filformat|Ny funktion|
|CELLSCPP-38|Skapa och manipulera namngivna intervall|Ny funktion|
|CELLSCPP-39|Läs/skriv tabbavgränsat filformat|Ny funktion|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, omdöpta, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells för C++. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Tar bort metoden IPageSetup::GetDraft()/SetDraft().**
Använd metoden IPageSetup::GetPrintDraft()/SetPrintDraft() istället.
#### **Tar bort ICell::GetConditionalIStyle()-metoden**
Använd ICell::GetIConditionalFormattingResult() istället.
#### **Tar bort ICells::MaxDataRowInColumn()-metoden**
Använd ICells::GetLastDataRow() istället.
#### **Tar bort metoden IPaneCollection::GetAcitvePaneType()/SetAcitvePaneType()**
Onödigt, raderat.
#### **Tar bort IRange::ToString()-metoden**
Onödigt, raderat.
#### **Tar bort metoden IRow::Equals().**
Onödigt, raderat.
#### **Tar bort metoden IWorkbook::SetISettings().**
Onödigt, raderat.
#### **Tar bort ICell::ToString()-metoden**
Onödigt, raderat.
#### **Tar bort ICell::Equals(ObjectPtr)-metoden**
Onödigt, raderat.
#### **Tar bort ICell::GetHashCode()-metoden**
Onödigt, raderat.
#### **Tar bort IWorksheet::ToString()-metoden**
Onödigt, raderat.
#### **Lägger till metoden IBuiltInDocumentPropertyCollection::GetScaleCrop()/SetScaleCrop()**
Indikerar visningsläget för dokumentminiatyren.
#### **Lägger till metoden IBuiltInDocumentPropertyCollection::GetLinksUpToDate()/SetLinksUpToDate()**
Anger om hyperlänkar i ett dokument är uppdaterade.
#### **Lägger till metoden IExternalLink::IsVisible().**
Anger om denna externa länk är synlig i MS Excel.
#### **Lägger till metoden IListColumn::GetFormula()/SetFormula().**
Hämtar och ställer in formeln för listkolumnen.
#### **Lägger till metoden IWorkbook::GetAbsolutePath()/SetAbsolutePath()**
Hämtar och ställer in den absoluta sökvägen för filen, används endast för externa länkar.
#### **Lägger till metoden IWorkbookSettings::GetCheckCompatibility()/SetCheckCompatibility()**
Indikerar om kontrollera kompatibilitet när du sparar arbetsbok, standardvärdet är sant.
#### **Lägger till metoden IWorksheetCollection::CreateIRange().**
Skapar ett IRange-objekt från en adress i intervallet.
#### **Lägger till metoden IWorkbookSettings::ClearPivottables().**
Rensar pivottabeller från kalkylarket.
#### **Lägger till metoden ILoadOptions::GetCultureInfo/SetCultureInfo().**
Hämtar systemkulturinformationen vid den tidpunkt då filen laddades.
#### **Lägger till metoden ILoadOptions::GetILightCellsDataHandler()/SetILightCellsDataHandler()**
Betecknar datahanteraren för bearbetning av celldata vid läsning av mallfil.
#### **Lägger till metoden IWorksheet::GetIProtectedRangeCollection().**
Hämtar samlingen tillåt redigeringsintervall i kalkylbladet.
#### **Lägger till metoden IWorksheet::Dispose().**
Kastar arbetsbladet.
#### **Lägger till metoden ICells::ImportTwoDimensionArray().**
Importerar en tvådimensionell datamatris till ett kalkylblad
#### **Lägger till metoden ICells::ImportCSV().**
Importerar en CSV-fil till cellerna.
#### **Lägger till metoden ICells::LinkToXmlMap().**
Länkar till en xml-karta.
