---
title: Aspose.Cells för Java 9.0.0 Release Notes
type: docs
weight: 40
url: /sv/java/aspose-cells-for-java-9-0-0-release-notes/
---
## **1) Aspose.Cells**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSJAVA-41947 | Möjlighet att upptäcka om en DataPoint är i Pie eller Bar| Ny funktion|
|CELLSJAVA-41827 | Kalkylark tar mer än 3 minuter att beräkna formler när du använder metoden Workbook.calculateFormula()| Förbättring|
|CELLSJAVA-41969 | Cell skuggning saknas vid konvertering av HTML till XLSX-filformat| Insekt|
|CELLSJAVA-41955 | Arbetsbok till HTML visar '#' i cellerna| Insekt|
|CELLSJAVA-41942 |Kanter saknas, cellskuggning och bilder - HTML till Excel-rendering| Insekt|
|CELLSJAVA-41967 | Cells saknas i PDF när flera utskriftsområden är definierade i ett enda ark| Insekt|
|CELLSJAVA-41958 | Förklaringen på höger sida är trunkerad i diagrammets bild| Insekt|
|CELLSJAVA-41953 | Text felplacerad i diagrammet efter konvertering till HTML-format| Insekt|
|CELLSJAVA-41948 | Diagrammet ändras vid konvertering av kalkylblad till HTML| Insekt|
|CELLSJAVA-41981 | Felaktig position av vertikal linje i diagrammets PDF| Insekt|
|CELLSJAVA-41964 | Autofit tar inte hänsyn till indragsnivå| Insekt|
|CELLSJAVA-40260 | Ändra texten i en befintlig WordArt i en Excel-fil| Insekt|
|CELLSJAVA-41971 | Cell.getValiationValue() kastar NullPointerException för anpassad valideringstyp| Undantag|
|CELLSJAVA-41963 | Undantag för olaglig nyckelstorlek inträffar när källan a5.xlsx öppnas| Undantag|
|CELLSJAVA-41962 | ArrayIndexOutOfBoundsException undantag inträffar när källan a4.xls öppnas| Undantag|
|CELLSJAVA-41961 | Ogiltig sträng i filen undantag inträffar när källan a3.xls öppnas| Undantag|
|CELLSJAVA-41960 | NegativeArraySizeException-undantaget inträffar när källan a2.xls öppnas| Undantag|
|CELLSJAVA-41959 | NullPointerException-undantag uppstår när källan a1.xlsx öppnas| Undantag|
## **2) Aspose.Cells Grid Suite**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSJAVA-41965 |Skaffa versionen som CELLSNET-44565 och CELLSNET-44676 som också behövs för GridWeb (Java)| Förbättring|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen Shape.TextOptions**
Representerar formens textalternativ.
### **Obsoletes Worksheet.SetBackground-metod**
Använd egenskapen Worksheet.BackgroundImage istället.
### **Föråldrade LineShape.BeginArrowheadStyle och ArcShape.BeginArrowheadStyle**
Använd egenskapen Shape.Line.BeginArrowheadStyle istället.
### **Föråldrade LineShape.BeginArrowheadWidth och ArcShape.BeginArrowheadWidth**
Använd egenskapen Shape.Line.BeginArrowheadWidth istället.
### **Föråldrade LineShape.BeginArrowheadLength och ArcShape.BeginArrowheadLength**
Använd egenskapen Shape.Line.BeginArrowheadLength istället.
### **Föråldrade LineShape.EndArrowheadStyle och ArcShape.EndArrowheadStyle**
Använd egenskapen Shape.Line.EndArrowheadStyle istället.
### **Föråldrade LineShape.EndArrowheadWidth och ArcShape.EndArrowheadWidth**
Använd egenskapen Shape.Line.EndArrowheadWidth istället.
### **Föråldrade LineShape.EndArrowheadLength och ArcShape.EndArrowheadLength**
Använd egenskapen Shape.Line.EndArrowheadLength istället.
### **Tar bort föråldrad Worksheet.CopyConditionalFormatting()-metod**
### **Tar bort föråldrad Workbook.CheckWriteProtectedPassword()-metod**
Använd metoden WorkbookSettings.WriteProtection.ValidatePassword istället.
### **Byter namn på Workbook.RemoveDigitalSign som Workbook.RemoveDigitalSignature-metod**
Metoden Workbook.RemoveDigitalSign har bytt namn till Workbook.RemoveDigitalSignature.
### **Lägger till egenskapen ChartSplitType.Auto**
Representerar att datapunkterna ska delas med standardmekanismen för denna diagramtyp.
### **Lägger till egenskapen ChartPoint.IsInSecondaryPlot**
Hämtar eller ställer in ett värde indikerar om dessa datapunkter finns i den andra cirkeln eller stapeln på en cirkel- eller stapeldiagram.
### **Lägger till egenskapen OleObject.ClassIdentifier**
Hämtar eller ställer in klassidentifieraren för det inbäddade objektet.
