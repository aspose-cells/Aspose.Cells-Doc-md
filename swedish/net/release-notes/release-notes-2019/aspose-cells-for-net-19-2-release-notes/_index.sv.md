---
title: Aspose.Cells för .NET 19.2 Release Notes
type: docs
weight: 110
url: /sv/net/aspose-cells-for-net-19-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 19.2](https://www.nuget.org/packages/Aspose.Cells/19.2.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46582|Stöd Range.Hyperlinks-egenskap|Ny funktion|
|CELLSNET-46534|Int32 kan vara liten för attributet Cells.count|Förbättring|
|CELLSNET-46552|Särskilj krypterad XLSX från krypterad PPTX och krypterad DOCX|Förbättring|
|CELLSNET-46568|Inställning Box Morrhår diagram stil|Förbättring|
|CELLSNET-46573|Ersätt ogiltiga tecken med lämpliga symboler som parenteser|Förbättring|
|CELLSNET-46581|Öppna/spara tar bort tabellalternativ text|Förbättring|
|CELLSNET-46584|Prestandaproblem med Aspose.Cells API:er|Prestanda|
|CELLSNET-46556|Texten i TextBox klipps ut|Insekt|
|CELLSNET-46565|Piktogram är inte synliga i PDF-utdata i Excel till PDF-rendering|Insekt|
|CELLSNET-46477|Villkorlig formatering i pivottabell fungerar inte i ett kopierat ark|Insekt|
|CELLSNET-46547|Innehåll saknas från HTML till Excel-konvertering|Insekt|
|CELLSNET-46566|XLSX-fil korrupt efter att ha sparats med Aspose.Cells API:er|Insekt|
|CELLSNET-46572|XLSB är skadad när man lägger till mer än 1 datafält medan XLSX fungerar bra|Insekt|
|CELLSNET-46548|NumberValue-problem vid konvertering av XLSX till PDF-filformat|Insekt|
|CELLSNET-46557|Fel cellvärde beräknat av Aspose.Cells formelberäkningsmotor|Insekt|
|CELLSNET-46578|Worksheet.AutoFitColumns() passar inte helt kolumner|Insekt|
|CELLSNET-46550|Märker text som är trasslig när du konverterar MS Excel-diagram till bilder|Insekt|
|CELLSNET-46558|Tecknen på diagrammet går förlorade när du läser och sparar en ODS-fil|Insekt|
|CELLSNET-46560|Serienamnet går förlorat när en ODS-fil sparas|Insekt|
|CELLSNET-46561|Standardgränsen för plotområdet i diagrammet ska inte vara synlig för ODS-fil|Insekt|
|CELLSNET-46562|X-axelns rutnätslinjer tas bort när du läser och sparar XLSX-fil|Insekt|
|CELLSNET-46569|Utskriftsinställningarna ändrades efter att MS Excel-filen laddades och sparades|Insekt|
|CELLSNET-46574|Problem med att spara och öppna XLSB-filer|Insekt|
|CELLSNET-46555|Ett undantag uppstår när vissa egenskaper redigeras|Undantag|
|CELLSNET-46571|Undantag vid öppning av utdatafilen (efter att mallfilen har sparats på nytt) i MS Excel|Undantag|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till Cells.CountLarge fastighet**
Funktionellt sett är den samma som Count-egenskapen, förutom att Count-egenskapen kan generera ett spillfel när det finns för många instansierade Cell-objekt.
#### **Lägger till metoden Hyperlink.Delete().**
Tar bort denna hyperlänk.
#### **Lägger till Range.Hyperlinks-egenskap**
Får alla hyperlänkar i sortimentet.
#### **Lägger till enum CopyFormatType**
Representerar typen av kopieringsformat när du infogar rader.
#### **Lägger till klassen InsertOptions och metoden Cells.InsertRows(int, int , InsertOptions)**
Infogar rader med vissa alternativ.
#### **Lägger till metoderna FileFormatUtil.DetectFileFormat(Stream,String) och FileFormatUtil.DetectFileFormat(String,String)**
Upptäcker filformatet för krypterad OOXML-fil.
#### **Lägger till egenskaperna ListObject.AlternativeDescription och ListObject.AlternativeText**
Hämtar och ställer in alternativ text och beskrivning av tabellen.
#### **Lägger till Line.ThemeColor-egenskapen**
Hämtar och ställer in linjens temafärg.
#### **Lägger till klassen Mode3d och MsoModel3dFormat**
Kapslar in objektet som representerar en enda 3D-modell i ett kalkylblad.
#### **Lägger till ImageType.Gltf enum**
Representera typen av 3D-modell.
