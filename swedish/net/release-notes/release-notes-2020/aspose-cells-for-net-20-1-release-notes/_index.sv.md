---
title: Aspose.Cells för .NET 20.1 Release Notes
type: docs
weight: 70
url: /sv/net/aspose-cells-for-net-20-1-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 20.1](https://www.nuget.org/packages/Aspose.Cells/20.1.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47026|Stöd för "Rank minsta till största" och "Rank störst till minsta" visningsformat alternativ|Ny funktion|
|CELLSNET-47030|Visa rubriker när du sparar i HTML|Ny funktion|
|CELLSNET-47089|Stöd alla datavisningsformat i DataField|Ny funktion|
|CELLSNET-47062|Stöd för STDEV.P och STDEV.S|Ny funktion|
|CELLSNET-47070|Stöd för Regex i Ersätt-funktion som liknar Find() med alternativ|Ny funktion|
|CELLSNET-46998|Stöd för XAdES-signaturer|Ny funktion|
|CELLSNET-40174|Infogar kryssruta i diagramtypblad|Ny funktion|
|CELLSNET-43089|Stöd för villkorlig formatering vid konvertering av ODS till XLSX|Ny funktion|
|CELLSNET-43090|Stöd för datavalidering vid konvertering av ODS till XLSX-format|Ny funktion|
|CELLSNET-47064|Stöd formerna i diagrammet för .xlsx-filen.|Förbättring|
|CELLSNET-47065|Hämta PowerQuery från DataConnections|Förbättring|
|CELLSNET-47066|Hämta formaterad PowerQuery MCode som liknar MS Excel|Förbättring|
|CELLSNET-47008|Problem när du renderar en bild av ett diagram i en specifik vinkel|Insekt|
|CELLSNET-47063|Återge Excel till skrivarproblem när teckensnitt inte är installerade|Insekt|
|CELLSNET-44237|Nedåtordning av pivottabellens datafält|Insekt|
|CELLSNET-47002|Det beräknade värdet visas som "#REF!" i resulterande PDF|Insekt|
|CELLSNET-47050|Vissa fält på första sidan visas inte i utdata-PDF-filen|Insekt|
|CELLSNET-40733|Öppna Office .ods-filen - den villkorliga formateringen stannar inte|Insekt|
|CELLSNET-47039|XY-spridningsdiagram i ODS-fil renderas inte bra|Insekt|
|CELLSNET-47040|Nätdiagram i ODS-filen renderas inte bra|Insekt|
|CELLSNET-47060|Stöd anpassad XY av titel i ods-fil|Insekt|
|CELLSNET-47072|Skillnaden i länksökvägen hämtad av Aspose.Cells jämfört med Excel|Insekt|
|CELLSNET-47087|Har ett problem när du skriver ut excel-filen som sparats av Aspose.Cells för .NET|Insekt|
|CELLSNET-47082|Beräkning av formel hänger|Insekt|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till egenskapen ReplaceOptions.RegexKey.**
 Indikerar om den sökta nyckeln är regex. Om**Sann** då kommer den sökta nyckeln (som ska ersättas del) att tas som ett användarspecificerat regex.
#### **Lägger till metoden CustomImplementationFactory.CreateCultureInfo.**
Vissa kulturer kanske inte stöds av användarens miljö. För att undvika undantag för sådana situationer kan användaren åsidosätta denna metod för att tillhandahålla en giltig CultureInfo-instans istället.
#### **Tar bort den föråldrade metoden ValidationCollection.Add(Aspose.Cells.Validation).**
Använd metoden ValidationCollection.Add(CellArea) istället.
#### **Lägger till egenskapen PowerQueryFormula.FormulaDefinition.**
Hämtar definitionen av power-frågeformeln.
#### **Lägger till egenskapen DBConnection.PowerQueryFormula.**
Hämtar definitionen av kraftfrågeformel.
#### **Lägger till egenskapen HtmlSaveOptions.ExportHeadings.**
 Anger om rubriker exporteras när filen sparas till HTML. Standardvärdet är**falsk**. Om du vill importera HTML-filen till Excel, behåll standardvärdet.
#### **Lägger till XAdESType-klass**
Typ av XML Advanced Electronic Signature (XAdES).
#### **Lägger till egenskapen DigitalSignature.XAdESType**
Hämtar och ställer in typen av XML Advanced Electronic Signature (XAdES). Standardvärdet är None (XAdES är avstängt).
