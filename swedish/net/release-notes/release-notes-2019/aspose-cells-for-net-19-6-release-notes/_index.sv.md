---
title: Aspose.Cells for .NET 19.6 Release Notes
type: docs
weight: 70
url: /sv/net/aspose-cells-for-net-19-6-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 19.6](https://www.nuget.org/packages/Aspose.Cells/19.6.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-41277|Kommentarer i HTML-export av XLS/XLSX-filer|Ny funktion|
|CELLSNET-45194|Stöd ritning av Slicer medan du renderar till PDF|Ny funktion|
|CELLSNET-46742|Lägg till stöd för filformat för OpenDocument Flat XML Spreadsheet (.fods).|Ny funktion|
|CELLSNET-46744|Lägg till stöd för filformat för StarOffice Calc Spreadsheet (.sxc).|Ny funktion|
|CELLSNET-46714|Inbäddad OOXML-fil som ett paket för XLSX.|Förbättring|
|CELLSNET-46722|Säkerhetsvarning efter att ha sparat ett XLS-filformat igen|Förbättring|
|CELLSNET-46737|Problem med medium linjer/tjocka linjer när XLSX sparat som ODS|Förbättring|
|CELLSNET-46755|Detekterar om objektfilen är diagram eller oleobject för ODS.|Förbättring|
|CELLSNET-46731|Worksheet.Copy() hänger programmet|Prestanda|
|CELLSNET-46770|Slut på minne när du uppdaterar pivottabellen med en stor datakälla|Prestanda|
|CELLSNET-46730|Chart.ToImage() hänger programmet|Prestanda|
|CELLSNET-46670|Excel-filinnehåll överlappas efter att anpassade egenskaper lagts till|Insekt|
|CELLSNET-46747|Rutnätslinjer skrivs ut över det inbäddade objektet medan det renderas till PDF|Insekt|
|CELLSNET-41479|Slicerinställningar i genererad PDF|Insekt|
|CELLSNET-41783|Filer som genereras från en mallfil som innehåller en slicer behöver fixas|Insekt|
|CELLSNET-46733|Stil/format förlorade när pivottabellen sparades som HTML|Insekt|
|CELLSNET-46736|Teckensnittsproblem när HTML konverteras till PDF|Insekt|
|CELLSNET-46751|XLSX kan inte konverteras till HTML|Insekt|
|CELLSNET-46766|XIRR-funktionen fungerar inte om den sista raden är större än -62 i intervallet|Insekt|
|CELLSNET-46769|Cell värde extraherat annorlunda än Excel i tysk kultur|Insekt|
|CELLSNET-46761|Problem med Aspose.Cells.GridDesktop-skärm när du ställer in upplösningar och zoomar in en 4k-skärm|Insekt|
|CELLSNET-46592|Textåtergivningsproblem vid konvertering av XLSX till PDF|Insekt|
|CELLSNET-46735|Sidnummer startar inte om till 1 på varje ark i utdata-PDF-filen|Insekt|
|CELLSNET-46739|Tiff-komprimeringstypen ignorerar bakgrundsskuggning för diagram och former|Insekt|
|CELLSNET-46749|SheetRender.ToImage skapar felaktig EMF-bild|Insekt|
|CELLSNET-46093|Diagram respekterar inte Page Setup Black and White|Insekt|
|CELLSNET-46738|Aspose.Cells 19.4 Det går inte att öppna vissa .ots- och .ods-filer|Insekt|
|CELLSNET-46741|Felaktigt resultat vid arbete med kapslade listor|Insekt|
|CELLSNET-46748|Utdatafilen är alltid korrupt när du använder mätlicenser|Insekt|
|CELLSNET-46752|Utdata XLSX-fil blir skadad efter anrop av InsertCutCells()|Insekt|
|CELLSNET-46754|Namngivna intervall ändras när funktionen InsertCutCells() anropas|Insekt|
|CELLSNET-46759|Inget undantag togs upp när fel ström laddades in i arbetsboken|Insekt|
|CELLSNET-46043|System.InvalidCastException|Undantag|
|CELLSNET-46510|Form till bild-fel! när du konverterar XLSX till PDF|Undantag|
|CELLSNET-46765|Undantag "System.StackOverflowException" vid rendering av en Excel-fil till PDF-filformat|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till enum FileFormatType.FODS,FileFormatType.SXC,LoadFormat.FODS,LoadFormat.SXC,SaveFormat.FODS och SaveFormat.SXC**
Representerar filformatstyperna .FODS och .SXC.
#### **Lägger till enum WarningType.UnsupportedFileFormat**
Representerar filformat som inte stöds för varningstyper.
#### **Lägger till enum ODSGeneratorType**
Representerar generatortypen för ODS.
#### **OoxmlSaveOptions.EmbedOoxmlAsOleObject**
Anger om ooxml-fil bäddas in som OleObject.
#### **Lägger till Row.CopySettings(Aspose.Cells.Row,System.Boolean)**
Kopiera inställningar för rad, som stil, höjd, synlighet, ... etc.
