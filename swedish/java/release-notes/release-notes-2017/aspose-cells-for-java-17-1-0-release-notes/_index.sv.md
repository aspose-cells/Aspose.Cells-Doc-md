---
title: Aspose.Cells for Java 17.1.0 Release Notes
type: docs
weight: 120
url: /sv/java/aspose-cells-for-java-17-1-0-release-notes/
---
|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42132|Metoderna GetPaperWidth och GetPaperHeight har lagts till i klassen PageSetup|Ny funktion|
|CELLSJAVA-41950|Stöd Gradient Fill för WordArt när du konverterar kalkylblad till HTML|Ny funktion|
|CELLSJAVA-42129|Att spara till HTML är fel|Insekt|
|CELLSJAVA-42125|Rutnät bakom Shapes exporteras inte när de konverteras till HTML|Insekt|
|CELLSJAVA-42110|Vissa CSS-regler ignoreras vid import av HTML|Insekt|
|CELLSJAVA-42094|Innehållet är genomstruket i den konverterade HTML-koden|Insekt|
|CELLSJAVA-42091|Textstilen för vissa celler är fel när den sparas i HTML|Insekt|
|CELLSJAVA-42088|DataBar fel när cellen har en bakgrundsfärg inställd|Insekt|
|CELLSJAVA-42018|Sjökortsbilden sparas inte när EMF- eller SVG-format används|Insekt|
|CELLSJAVA-41980|HtrmlSaveOptions.ExportGridLines verkar inte fungera för ett visst kalkylblad|Insekt|
|CELLSJAVA-42131|Omräkning av ett antal formler med Aspose Cells API:er resulterar i "#NUM!" fel|Insekt|
|CELLSJAVA-42124|Datumformatproblem vid import av CSV med ICustomParser|Insekt|
|CELLSJAVA-42118|Name.getRanges() API ger oväntade resultat|Insekt|
|CELLSJAVA-42117|Det går inte att komma åt instansvariabeln m_LoadDataFilterOptions medan startSheet-metoden för klassen LoadFilter åsidosätts|Insekt|
|CELLSJAVA-41882|Cell strängvärde & avrundningsproblem baserat på olika JDK-versioner|Insekt|
|CELLSJAVA-42142|Höger till vänster och vänster till höger kontrolltecken renderas inte korrekt i PDF när konvertering görs på Linux|Insekt|
|CELLSJAVA-42136|Hebreiska - I tabellen är ordlindade rader justerade till höger i PDF medan de ska centreras som i Excel|Insekt|
|CELLSJAVA-42113|Fel konvertering av arabiskt kalkylblad till SVG|Insekt|
|CELLSJAVA-42135|Hebreiska - Radslagen text är inte högerjusterad i PDF som i Excel|Insekt|
|CELLSJAVA-42134|Hebreiska - Serieetiketter när det finns en radbrytning visas inte tecknen i rätt ordning|Insekt|
|CELLSJAVA-42127|Form till bild Fel vid rendering av 03.xls till PDF|Insekt|
|CELLSJAVA-42126|Form till bild Fel vid rendering av 02.xls till PDF|Insekt|
|CELLSJAVA-42087|Diagrambilden i HTML-koden är fel|Insekt|
|CELLSJAVA-42079|Ojämna linjers tjocklek vid korsningar samtidigt som kalkylblad med diagram renderas till PDF|Insekt|
|CELLSJAVA-42078|Diagrametiketter visas/renderas inte på samma sätt (som i den ursprungliga Excel-filen) i den utgående PDF-filen|Insekt|
|CELLSJAVA-42076|Vinkeln på x-axeletiketter är felaktig i diagrammets PDF|Insekt|
|CELLSJAVA-42065|Felaktig rendering av stapeldiagram vid rendering av kalkylblad till HTML|Insekt|
|CELLSJAVA-42152|Att ställa in formel som refererar till extern arbetsbok skapar en 3d-formel|Insekt|
|CELLSJAVA-42146|Oläsbart innehållsfel i Excel 2007 efter att ett kalkylblad har sparats om|Insekt|
|CELLSJAVA-42121|Villkorliga formatuttryck ändras vid radering av rader|Insekt|
|CELLSJAVA-42114|Cell.getFormula() returnerar bruten formel för en cell|Insekt|
|CELLSJAVA-42112|Utdatafilen blir korrupt efter att ha kört DataLabels.setPosition()-metoden|Insekt|
|CELLSJAVA-42108|Villkorliga formatprioritetsordningsändringar på metoden Cells.deleteRows()|Insekt|
|CELLSJAVA-42069|Vba-modulen går förlorad när en XLSM-fil sparas på nytt på Linux|Insekt|
|CELLSJAVA-42025|API lägger till extra apostrof till den modifierade formeln|Insekt|
|CELLSJAVA-41984|Dynamisk formel i designerkalkylblad med {-1} {-2} returnerar Ogiltigt formelfel|Insekt|
|CELLSJAVA-41739|Transparensen av formerna återställs till 0 medan XLS konverteras till XLSB|Insekt|
|CELLSJAVA-42122|NullPointerException när du öppnar en stor Excel-fil|Undantag|
|CELLSJAVA-42123|Form till bild-fel - vid rendering av en Excel-fil|Undantag|
|CELLSJAVA-42144|new Workbook() kan skapa ett undantag i Aspose.Cells for Java 16.12.6|Undantag|
|CELLSJAVA-42143|Undantag: java.lang.ArrayIndexOutOfBoundsException på metoden Workbook.save()|Undantag|
|CELLSJAVA-42137|Ogiltigt undantag för kolumnindex vid rendering av Excel|Undantag|
|CELLSJAVA-42111|Ogiltigt formelundantag för den sista cellen|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till setter för egenskapen LoadFilter.LoadDataFilterOptions för att ersätta variabeln m_LoadDataFilterOptions.**
Användaren kan ändra egenskapen LoadDataFilterOptions i sin implementering av LoadFilter för att ändra beteendet för att ladda arbetsboken.
### **Lägger till egenskapen CellsHelper.SignificantDigits.**
Hämtar och ställer in antalet signifikanta siffror.
### **Lägger till egenskapen GlowEffect.Color.**
Får färgen på glödeffekten.
### **Lägger till egenskapen PageSetup.PaperWidth.**
Representerar papprets bredd i tum, betraktad som sidorientering.
### **Lägger till egenskapen PageSetup.PaperHeight.**
Representerar höjden i tum på papperet, betraktad som sidorientering.
### **Lägger till egenskapen WorkbookSettings.CheckCustomNumberFormat.**
Anger om anpassat nummerformat kontrolleras när Style.Custom ställs in.
### **Lägger till några diagramtyper.**
Lägger till fler diagramtyper för MS Office 2016.
### **Lägger till DisplayUnitType.Percentage enum.**
Representerar värden på diagrammet ska delas med 0,01.
