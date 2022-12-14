---
title: Aspose.Cells för PHP via Java 19.1 Release Notes
type: docs
weight: 20
url: /sv/php-java/aspose-cells-for-php-via-java-19-1-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells för PHP via Java 19.1.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-41026|Stöd för Excel 95/5.0 (XLS-filer)|Ny funktion|
|CELLSJAVA-42778|Undantag "stil textRotation måste vara mellan 0 och 180" när XLSM laddas|Förbättring|
|CELLSJAVA-42290|Mdash och ndash infogade i textrutor i diagram renderas inte korrekt i diagrammets PDF|Insekt|
|CELLSJAVA-42750|Det gick inte att hämta sidfältens objekt i pivottabellsrapporten|Insekt|
|CELLSJAVA-42783|Problem med genomstruken text i genererat HTML-filformat|Insekt|
|CELLSJAVA-42784|Data i vissa celler (t.ex. G7, H7, etc.) renderas inte på samma sätt som i originalfilen i Excel till HTML/bildkonvertering|Insekt|
|CELLSJAVA-42797|Vissa stilar återges inte i HTML-inmatning|Insekt|
|CELLSJAVA-42807|Formel/funktion "ISOWEEKNUM"-beräkning är inte detsamma som MS Excel|Insekt|
|CELLSJAVA-42794|ODS till XLSX - Textfärg ändrad|Insekt|
|CELLSJAVA-42795|ODS till XLSX - Teckensnittet genomstrukits inte korrekt bevarat|Insekt|
|CELLSJAVA-42796|ODS till XLSX - Textrutans dimensioner ändrade|Insekt|
|CELLSJAVA-42798|ODS -> XLSX - Hyperlänk är funktionell men visas som vanlig text|Insekt|
|CELLSJAVA-42802|ODS till XLSX, procentandelar går förlorade i stapeldiagrammet|Insekt|
|CELLSJAVA-42803|Outline "SummaryRowBelow" påverkas inte när du sparar som XLSB-filformat|Insekt|
|CELLSJAVA-42757|CellsException vid konvertering av filer|Undantag|
|CELLSJAVA-42799|Undantag "java.lang.ArrayIndexOutOfBoundsException: -32768" när ett XLSX-filformat laddas|Undantag|
|CELLSJAVA-42800|ArrayIndexOutOfBoundsException när en arbetsbok laddas|Undantag|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells för PHP via Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till metoden PivotTable.ShowReportFilterPageByName(strängfältnamn).**
Visar alla rapportfiltersidor enligt PivotFields namn, PivotField måste finnas i PageFields.
#### **Lägger till metoden PivotTable.ShowReportFilterPageByIndex(int posIndex)**
Visar alla rapportfiltersidor enligt positionsindex i sidfälten.
#### **Lägger till metoden PivotTable.ShowReportFilterPage(PivotField pageField)**
Visar alla rapportfiltersidor enligt PivotField, PivotField måste finnas i PageFields.
#### **Lägger till klasserna DataSorterKey och DataSorterKeyCollection**
Representerar nyckeln för datasorteraren.
#### **Lägger till metoden DataSorter.AddKey(Int32,SortOnType,SortOrder,Object)**
Lägger till sorteringsnyckeln som cellens bakgrundsfärg, teckensnittsfärg.
#### **Lägger till egenskapen Aspose.Cells.DataSorter.Keys**
Får alla nycklar till datasorteraren.
#### **Lägger till SortOnType enum**
Representerar typen av sorterad data.
#### **Lägger till klass ODSLoadOptions**
Representerar alternativen för att ladda ODS-fil.
#### **Lägger till egenskapen HTMLLoadOptions.ProgId**
Hämtar program-id för att skapa filen. används endast för MHT-filer.
#### **Lägger till egenskapen PdfSaveOptions.TextCrossType**
Hämtar eller ställer in visning av texttyp när textbredden är större än cellbredden.
#### **Lägger till TextCrossType enum-klass**
Räknar upp visning av texttyp när textbredden är större än cellbredden.
#### **Lägger till WorksheetCollection.RegisterAddInFunction() metoder**
Ersättning av Cell.SetAddInFormula(), ett mer bekvämt och effektivt sätt för användare att lägga till och använda tilläggsfunktioner.
#### **Föråldrad metod Cell.SetAddInFormula().**
Registrera tilläggsfunktionerna först med WorksheetCollection.RegisterAddInFunction() och ställ sedan in formeln för Cell med Cell.Formula/Cell.SetFormula() istället.

