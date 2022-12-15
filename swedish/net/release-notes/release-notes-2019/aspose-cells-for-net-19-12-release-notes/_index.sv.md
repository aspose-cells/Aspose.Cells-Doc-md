---
title: Aspose.Cells for .NET 19.12 Release Notes
type: docs
weight: 10
url: /sv/net/aspose-cells-for-net-19-12-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 19.12](https://www.nuget.org/packages/Aspose.Cells/19.12.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-44451|Tillämpa datasortering för datafält med avseende på radfält i pivottabell - Efterlikna resultat enligt användarens förväntade fil|Ny funktion|
|CELLSNETCORE-45|Ladda data från Datasource med alternativet att hoppa över något tecken som Apostrophe|Ny funktion|
|CELLSNET-47018|Att beräkna vissa kombinationsdiagram kan orsaka ett undantag|Förbättring|
|CELLSNET-47016|Radbrytning är annorlunda i den senaste versionen av Aspose.Cells|Förbättring|
|CELLSNET-47023|Sjökortet gick förlorat när ODS-fil laddades och sparades|Förbättring|
|CELLSNET-47056|Diagram renderas inte när ODS-fil laddas och sparas|Förbättring|
|CELLSNET-46679|Felaktig rendering vid export av XLSX till PDF|Insekt|
|CELLSNET-46680|Wingding-symbol saknas vid konvertering av XLSX till PDF|Insekt|
|CELLSNET-46740|Fel i bilder vid konvertering av Excel-fil till PDF|Insekt|
|CELLSNET-46901|3D-modellens position skiftar|Insekt|
|CELLSNET-46936|Teckensnittet återges inte bra i HTML|Insekt|
|CELLSNET-47013|Siffror på trattdiagram försvinner när Excel-fil konverteras till PDF|Insekt|
|CELLSNET-43846|Pivottabellen förlorar de anpassade fältnamnen och inställningen "Visa värde som...".|Insekt|
|CELLSNET-46444|Pivottabellens värde ändrades efter anrop av PivotTable.CalculateData|Insekt|
|CELLSNET-46484|RefreshData sorterar inte data innan filen öppnas i Excel|Insekt|
|CELLSNET-47010|Ett problem med formateringen av pivottabellgrupprubriker|Insekt|
|CELLSNET-47024|Felaktig sorteringsordning för rader i pivottabeller med värderad|Insekt|
|CELLSNET-47034|Kolumnbredder och radhöjder pressas under HTML till Excel-konvertering|Insekt|
|CELLSNET-47007|Värdefel visas när formeln utvärderas|Insekt|
|CELLSNET-47029|Felaktigt värde TRUE hämtat från Cell istället för värdet FALSE|Insekt|
|CELLSNET-47052|Korrupt DateTimeFormat vid konvertering av Excel till PDF|Insekt|
|CELLSNET-46757|Problem vid konvertering av XLSX till PDF|Insekt|
|CELLSNET-46976|Vissa kantlinjer försvinner i Excel till PDF-rendering|Insekt|
|CELLSNET-47000|Olämplig resultatbild av SheetRender från lösenordsskyddad .ods-fil|Insekt|
|CELLSNET-47025|Makron för XLSM upptäcktes inte|Insekt|
|CELLSNET-47038|Linjediagram i ODS-filen renderas inte bra när de öppnas eller sparas via Aspose.Cells|Insekt|
|CELLSNET-47045|Ändring av VBA-modulnamn kraschar|Insekt|
|CELLSNET-47051|Diagrammet är fortfarande bundet till det första kalkylbladet efter kopian|Insekt|
|CELLSNET-47053|Felaktigt filformatsavkänning och process har fastnat under filöppningen|Insekt|
|CELLSNET-46922|Undantag vid laddning av XLS-filen|Undantag|
|CELLSNET-46999|Ett undantag skapas när .ods-filen "Parametern är inte giltig."|Undantag|
|CELLSNET-47017|OpenXML SDK skapar ett undantag när den konverterade filen öppnas|Undantag|
|CELLSNET-47022|Undantag vid laddning av ett XLSX-filformat|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Tar bort föråldrad DataLabels.BaseField-egenskap**
Använd PivotField.BaseFieldIndex istället.
#### **Tar bort föråldrad DataLabels.BaseItem-egenskap**
Använd PivotField.BaseItemIndex istället.
#### **Tar bort föråldrad DataLabels.IsValueShown-egenskap**
Använd egenskapen DataLabels.ShowValue istället.
#### **Tar bort föråldrad DataLabels.IsPercentageShown-egenskap**
Använd egenskapen DataLabels.ShowPercentage istället.
#### **Tar bort föråldrad DataLabels.IsBubbleSizeShown-egenskap**
Använd egenskapen DataLabels.ShowBubbleSize istället.
#### **Tar bort föråldrad DataLabels.IsCategoryNameShown-egenskap**
Använd egenskapen DataLabels.ShowCategoryName istället.
#### **Tar bort föråldrad DataLabels.IsSeriesNameShown-egenskap**
Använd egenskapen DataLabels.ShowSeriesName istället.
#### **Tar bort föråldrad DataLabels.IsLegendKeyShown-egenskap**
Använd egenskapen DataLabels.ShowLegendKey istället.
#### **Lägger till alternativet LoadOptions.KeepUnparsedData**
Alternativet anger om den oparsade datan ska behållas i minnet för arbetsboken när den laddas från mallfilen. Om användare inte behöver spara tillbaka arbetsboken helt och hållet, särskilt när de bara behöver läsa något speciellt innehåll i arbetsboken (t.ex. med någon form av LoadFilter), behövs inte dessa oparsade data längre och de kan ställa in den här egenskapen som falsk för att få bättre prestanda. För gamla versioner, när arbetsbok laddades från en mallfil med användarspecificerat LoadFilter, behölls inte dessa oparsade data av prestanda. Nu tillhandahåller vi det här alternativet och gör dess standardvärde sant, det kan påverka prestandan för användarnas fall av att använda LoadFilter. Om så är fallet bör användarna uttryckligen ange den här egenskapen som falsk i sin applikation.
#### **Lägger till alternativet LoadDataFilterOptions.Picture**
Alternativet som anger om bilden ska laddas.
#### **Lägger till alternativet LoadDataFilterOptions.OleObject**
Alternativet som anger om OleObject ska laddas.
#### **Lägger till alternativet LoadDataFilterOptions.Drawing**
Alternativet som anger om ritobjekt (inklusive diagram, bild, OleObject och alla andra ritobjekt) ska laddas.
#### **Föråldrade LoadDataFilterOptions.Shape-alternativet**
Använd (LoadDataFilterOptions.Drawing & ~LoadDataFilterOptions.Chart) istället för LoadDataFilterOptions.Shape.
#### **Lägger till klassen FormulaParseOptions**
Det ger användaralternativ för att ställa in formler.
#### **Lägger till metoder: Cell.SetFormula(strängformel,FormulaParseOptions optioner,objektvärde),SetArrayFormula(string arrayFormula,int rowNumber,int columnNumber,FormulaParseOptions options),SetSharedFormula(string sharedFormula,int rowNumber,FormulaParseNumberOption)**
Ställer in formler med alternativ.
#### **Föråldrade metoder: Cell.SetFormula(strängformel,bool ärR1C1,bool ärLokal,objektvärde),SetArrayFormula(sträng arrayFormula,int radNumber,int kolumnNumber,bool ärR1C1,bool ärLokal),SetSharedFormula,(intkolonnNumberFormula,,introwdNumber isR1C1,bool isLocal)**
Använd motsvarande metoder med FormulaParseOptions istället.
#### **Lägger till FileFormatType.OTP enum**
Stöder detektering av .OTP-filformatet.
#### **Lägger till AutoFitterOptions.AutoFitWrappedTextType-egenskapen och AutoFitWrappedTextType-enum.**
Hämtar och ställer in typen av automatisk anpassning av inslagen text.
#### **Lägger till klassen EmfRenderSetting**
Uppsättningar för att rendera Emf-metafil.
#### **Lägger till egenskapen PdfSaveOptions.EmfRenderSetting**
Uppsättningar för att rendera EMF-metafil under rendering till PDF-fil.
#### **Lägger till metoden ShapeCollection.AddSvg().**
Lägger till SVG-bild.
#### **Lägger till WorkbookSettings.QuotePrefixToStyle-egenskapen**
Anger om Style.QuotePrefix-egenskapen ställs in när strängvärdet (som börjar med ett citattecken ) anges i cellen
#### **Lägger till egenskapen HtmlSaveOptions.AddTooltipText**
Anger om man lägger till verktygstipstext när data inte kan visas helt. Standardvärdet är falskt.
