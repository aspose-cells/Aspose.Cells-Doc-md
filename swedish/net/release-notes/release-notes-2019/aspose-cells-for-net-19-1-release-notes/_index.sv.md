---
title: Aspose.Cells for .NET 19.1 Release Notes
type: docs
weight: 120
url: /sv/net/aspose-cells-for-net-19-1-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 19.1](https://www.nuget.org/packages/Aspose.Cells/19.1.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46429|Lägg till pivottabell med alternativet Visa rapportfiltersidor|Ny funktion|
|CELLSNET-46014|Stöd för att hantera överflödande cellinnehåll samtidigt som du sparar som PDF och bild|Ny funktion|
|CELLSNET-46490|Stöd för Excel95/5.0 XLS-filer|Ny funktion|
|CELLSNET-46500|Sortera efter cellbakgrundsfärg|Ny funktion|
|CELLSNET-46544|Upptäck om genererad MHT-fil är ett kalkylblad eller inte|Ny funktion|
|CELLSNET-46538|När XLSX sparas som PDF eller TIFF saknas botten av texten|Insekt|
|CELLSNET-46509|R1C1-formler läses felaktigt för vissa celler|Insekt|
|CELLSNET-46513|Aspose.Cells formelberäkningsmotorn beräknar en formel för cellen som "0" istället för "#REF!" fel|Insekt|
|CELLSNET-46535|"#NAMN?" för formler sparade i XLSB-format|Insekt|
|CELLSNET-46539|Formel skiftlägeskänslig fråga|Insekt|
|CELLSNET-46531|Att byta namn på ListColumns förstör arbetsboken (när det finns en pivottabell)|Insekt|
|CELLSNET-46511|TIFF skapad med extra tomma sidor|Insekt|
|CELLSNET-46522|Tillämpa regionala inställningar för utskriftsinställningar|Insekt|
|CELLSNET-46529|Bild saknas efter XLSX till PDF-konvertering|Insekt|
|CELLSNET-46451|Problem vid återgivning av mallfilen till PDF-filformat|Insekt|
|CELLSNET-46518|Layoutproblem (vissa axeletiketter är på två rader) när mallfilen renderas till PDF-filformat|Insekt|
|CELLSNET-46113|Filformat stöds inte undantag för XLS-dokument|Insekt|
|CELLSNET-46504|Problem med länkar|Insekt|
|CELLSNET-46506|Skillnad med metoden ImportObjectArray|Insekt|
|CELLSNET-46541|Kombinationsdiagram fungerar inte med v18.12.x men fungerar med v18.4 och tidigare versioner|Insekt|
|CELLSNET-46543|Undantag när du ringer Cells.DeleteBlankRows|Undantag|
|CELLSNET-46459|Ett undantag uppstår vid konvertering till Open Strict XML-formatet|Undantag|
|CELLSNET-46485|Undantag vid laddning av ett XLSB-filformat|Undantag|
|CELLSNET-46508|Undantag vid laddning av ett XLSM-filformat|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
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
