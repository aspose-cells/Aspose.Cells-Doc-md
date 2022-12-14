---
title: Aspose.Cells för .NET 18.5 Release Notes
type: docs
weight: 80
url: /sv/net/aspose-cells-for-net-18-5-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 18.5](https://www.nuget.org/packages/Aspose.Cells/18.5.1).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46095|Implementera funktionen TAK.PRECIS|Ny funktion|
|CELLSNET-46023|Stöd Strikt Open XML-kalkylbladsformat|Ny funktion|
|CELLSNET-46080|Färgen på bilden ska vara svart vid konvertering till PDF|Förbättring|
|CELLSNET-46087|Page Setup PrintErrorType fungerar inte i Excel till PDF-rendering|Förbättring|
|CELLSNET-46084|PageSetup.PrintDraft träder inte i kraft när du sparar till PDF|Förbättring|
|CELLSNET-46100|System.OutOfMemoryException vid konvertering av Excel-fil till PDF|Prestanda|
|CELLSNET-46033|Sidfält med namnet "Frånvarande objekt Ja" försvinner vid uppdatering|Insekt|
|CELLSNET-46096|Beräkningsfel vid användning av beräkningskedja och definierat namn|Insekt|
|CELLSNET-46047|Några kolumner försvinner när en Excel-fil importeras till GridWeb|Insekt|
|CELLSNET-46110|Textbrytning är inte korrekt när "Issue2 wrapping-nr_beställnings-_page_size.xlsx" konverteras till PDF|Insekt|
|CELLSNET-46109|Textbrytning är inte korrekt när "Issue2 wrapping.xlsx" konverteras till PDF|Insekt|
|CELLSNET-46108|Textbrytning är inte korrekt när "Issue3 wrapping.xlsx" konverteras till PDF|Insekt|
|CELLSNET-46088|Zoomfaktor för sidinställningar skapar felaktigt antal sidor i PDF|Insekt|
|CELLSNET-46076|Undantag när du sparar en arbetsbok i MemoryStream|Insekt|
|CELLSNET-46052|Vissa av rutnätslinjerna runt vissa celler är inte ritade korrekt|Insekt|
|CELLSNET-46036|Diagramtiteln är squished där alla tecken körs tillsammans i Excel till PDF-rendering|Insekt|
|CELLSNET-46082|Färgerna på cirkeldiagramförklaringar ändras efter att de har sparats till PDF och stämmer inte överens med cirkeldiagramsegment|Insekt|
|CELLSNET-46104|Att spara XLSB till XLSM skapar en korrupt MS Excel-fil|Insekt|
|CELLSNET-46098|Namngivna intervall förlorade vid kopiering till befintlig arbetsbok|Insekt|
|CELLSNET-46077|Inbäddade ritobjekt är för smala i utdatafilen när du sparar om en XLSX-fil|Insekt|
|CELLSNET-46068|Aspose.Cells returnerar tom PDF när en SpreadsheetML-fil sparas som PDF|Insekt|
|CELLSNET-46060|Dataförlust uppstår när ODS-filformatet konverteras till XLSX|Insekt|
|CELLSNET-46057|Namngivna intervall utökas inte med Smart Markers "shift"-parameter|Insekt|
|CELLSNET-46055|Genom att använda parametern "shift" i Smart Markers, renderas de genererade raderna inte med samma stil/formatering|Insekt|
|CELLSNET-46048|Villkorlig formatering fungerar inte i Smart Markers med shift-parameter|Insekt|
|CELLSNET-42764|Text beskuren i MS Excel-celler om dokumentraderna har automatisk storlek|Insekt|
|CELLSNET-41678|Ändra storlek på ett ListObject/Table uppdaterar inte dess villkorliga formatering|Insekt|
|CELLSNET-46059|Det går inte att öppna XLS-filen eftersom den ger undantag under laddning|Undantag|
|CELLSNET-46097|Undantag "Ogiltig formel:"'Nytt' namn'!G11:G15"." när du uppdaterar pivotdiagramdata|Undantag|
|CELLSNET-46075|Undantag vid rendering av en Excel-fil till PDF|Undantag|
|CELLSNET-46101|NullReferenceExceptions för att öppna MS Excel-filer på Mono Ubuntu Linux|Undantag|
|CELLSNET-46085|Undantag vid användning av metoden ListObject.ConvertToRange|Undantag|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till nya egenskaper Cell.IsTableFormula/IsArrayFormula för att ersätta Cell.IsInTable/IsInArray**
Anger om en cell är en del av tabellformeln eller matrisformeln. Gamla namn gör otydlighet, så vi gjorde dem föråldrade och tillhandahåller nya.
#### **Lägger till klass IndividualFontConfigs**
Representerar teckensnittskonfigurationer för varje arbetsboksobjekt.
#### **Lägger till egenskapen LoadOptions.FontConfigs**
Hämtar och ställer in individuella teckensnittskonfigurationer.
#### **Tar bort föråldrad FontSetting.ShapeFont-egenskap**
Använd egenskapen FontSetting.TextOptions istället.
#### **Lägger till OoxmlCompliance enum och WorkbookSettings.Compliance-egenskapen**
Stöder Strict Open XML-kalkylblad.
#### **Lägger till metoden GroupShape.Ungroup().**
Delar upp former.
#### **Lägger till MsoFormatPicture.Gamma-egenskapen**
Får och ställer in bildens gamma.
#### **Lägger till egenskaperna TextOptions.FarEastName och TextOptions.LatinName**
Hämta och ställer in Fjärran Östern och det latinska namnet på teckensnittet.
