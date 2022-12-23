---
title: Aspose.Cells for Java 19.2 Release Notes
type: docs
weight: 110
url: /sv/java/aspose-cells-for-java-19-2-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 19.2.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42827|Infoga rad med InsertOptions liknande MS Excel|Ny funktion|
|CELLSJAVA-42712|Förbättra JavaDocs för Aspose.Cells for Java|Förbättring|
|CELLSJAVA-42823|Användning av FontUnderlineType.WORDS skapar undantag|Förbättring|
|CELLSJAVA-42826|Data med villkorlig formatering utelämnad vid konvertering från XLSX till HTML|Insekt|
|CELLSJAVA-42815|Att lägga till komplexa referenser till definierade namn resulterar i korrupt MS Excel-arbetsbok|Insekt|
|CELLSJAVA-42822|Cell.getValidationValue returnerar fel värde för det angivna värdet|Insekt|
|CELLSJAVA-42829|Anpassat funktionsnamn inom de delade formlerna ersatt av ett annat namn|Insekt|
|CELLSJAVA-42824|Axeltitlar saknas och annan formatering är fel av diagram i Excel till PDF/A-konvertering|Insekt|
|CELLSJAVA-42814|Pilarna i PNG-utgången matchar inte pilarna i Excel-diagrammet|Insekt|
|CELLSJAVA-42777|Fel radhöjd har ändrats när du använder automatisk anpassning av rader|Insekt|
|CELLSJAVA-42813|Arbetsboksinställningen "ReCalculateOnOpen" kvarstod inte|Insekt|
|CELLSJAVA-42816|Ofullständig visning för AutoFitterOptions.setAutoFitMergedCells(true)|Insekt|
|CELLSJAVA-42817|Textboxens bakgrundsfärg ändrades oväntat|Insekt|
|CELLSJAVA-42821|När den första raden i ett intervall tas bort uppdateras intervallet felaktigt|Insekt|
|CELLSJAVA-42828|När du använder Cell.setHtmlString läggs en ny rad till i slutet av texten|Insekt|
|CELLSJAVA-42820|Undantag "Invalid IMEModeType string val" vid inläsning av ett XLSX filformat|Undantag|
Offentlig API och bakåtinkompatibla ändringar

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
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
Representerar typen av 3D-modell.
