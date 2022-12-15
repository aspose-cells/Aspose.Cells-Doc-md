---
title: Aspose.Cells for .NET 8.6.1 Release Notes
type: docs
weight: 30
url: /sv/net/aspose-cells-for-net-8-6-1-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 8.6.1](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.6.1/)

{{% /alert %}} 

 Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells



\1) Aspose.Cells 


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSNET-43905) - Stöd för att ändra HTML-hyperlänkens målattribut till "_blank"

 (CELLSNET-43885) - Möjlighet att hämta ConnectionString för ExternalConnection av typen WebQuery

 (CELLSNET-43935) - Ignorerar dold kolumn med ExportTableOptions.PlotVisibleColumns inställd på sant

 (CELLSNET-43925) - Lägga till en referens till VBA-makron i arbetsboken


## **Förbättringar**


 (CELLSNET-43933) - Cell.Formel kan acceptera en ogiltig formel och API försöker korrigera den

 (CELLSNET-43476) - API behövs för att kontrollera om licensen är laddad eller inte

 (CELLSNET-43310) - Byta namn på dubbla kalkylbladsnamn vid kombination av arbetsböcker

 (CELLSNET-42518) - Möjlighet att komma åt delobjekt via smarta markörer


## **Buggar**


 (CELLSNET-43946) - Cell.HtmlString returnerar en sträng som återger den normala strängen som nedsänkt

(CELLSNET-43941) - Diagram genereras inte korrekt

 (CELLSNET-43936) - Visar förklaringsnycklar även om Chart.ChartDataTable.ShowLegendKey är inställt på false

 (CELLSNET-43991) - Att ta bort kalkylbladen förstör den resulterande XLSX

 (CELLSNET-43988) - Lösenord att ändra försvinner när XLSX åter sparas med Aspose.Cells

 (CELLSNET-43984) - Lösenord att ändra konverterar till lösenord för att öppna när XLSM sparas på nytt

 (CELLSNET-43983) - Lösenord att ändra konverterar till lösenord för att öppna när XLSX sparas på nytt

 (CELLSNET-43982) - Lösenord att ändra konverterar till lösenord för att öppna när XLTM sparas på nytt

 (CELLSNET-43981) - Lösenord att ändra försvinner när XLTM sparas på nytt

 (CELLSNET-43980) - Lösenord att ändra konverterar till lösenord för att öppna när XLTX sparas på nytt

 (CELLSNET-43979) - SetStyle-teckensnitt tillämpas inte för vissa typsnitt

 (CELLSNET-43977) - Lösenord att ändra försvinner när XLTX sparas på nytt med Aspose.Cells

 (CELLSNET-43976) - Flera försök att öppna lösenordsskyddad XLSX

(CELLSNET-43973) - Lösenordet att ändra försvinner efter att XLSM har sparats på nytt

 (CELLSNET-43968) - Excel-applikationen rekommenderar att den resulterande XLSB öppnas i skrivskyddad

 (CELLSNET-43967) - Lösenordsskyddad XLT blir skadad efter återlagring

 (CELLSNET-43966) - ISNONTEXT-formeln returnerar fel värde efter CalculateFormula

 (CELLSNET-43965) - DetectFileFormat(FileStream) förbrukar mycket minne för zip-fil

 (CELLSNET-43951) - Lösenord som ska ändras har förlorats i OOXML-filer

 (CELLSNET-43950) - Skyddsidentifieringsproblem i Aspose.Cells

 (CELLSNET-43944) - Bildstorleken är inte korrekt och ändras efter återställning

 (CELLSNET-43943) - Kan inte läsa upphöjd från celltecken

 (CELLSNET-43940) - Fel cell vald i rapporten öppen

 (CELLSNET-43931) - Att radera rader från namngivna intervall förstör den resulterande XLSX

 (CELLSNET-43928) - DocumentProperty Author-värdet har lästs ofullständigt

(CELLSNET-43927) - #REF i formel som refererar till listobjekt på annat kalkylblad

 (CELLSNET-43891) - Problem med Workbook.VBAProject.Modules operationer

 (CELLSNET-43737) - FileFormatInfo.IsEncrypted har fel värde för äldre format

 (CELLSNET-42120) - DisplayStringValue-värdet är felaktigt i vissa scenarier

 (CELLSNET-42110) - Gränsuppsättning för intervall i XLSX visas inte i PDF


## **Undantag**


 (CELLSNET-43932) - Form till bild Fel! medan du renderar ett kalkylblad till PDF

 (CELLSNET-43964) - Att få visningsstil för alla celler kastar IndexOutOfRangeException

 (CELLSNET-43926) - CellsException at Workbook.CalculateFormula

 (CELLSNET-43911) - CellsException vid Workbook.Save

 (CELLSNET-43930) - GetNamedRanges()-metoden kastar Domain First Chance Exception

 (CELLSNET-43918) - Undantag för att öppna mallen XLSX-fil



\2) Aspose.Cells Grid Suite


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSNET-44004) - Stöd för att ladda och spara SpreasheetML(XML)-fil - GridDesktop


## **Förbättringar**


(CELLSNET-43873) - Gammal kod i - Formatera ett intervall på Cells - artikeln fungerar inte


## **Buggar**


 (CELLSNET-43997) - Aktiv cell i arket är inte på rätt plats när du laddar/sparar en XLSX-fil - GridWeb

 (CELLSNET-43993) - C2686-fel vid kompilering av VS2008 C++ med griddesktop.dll

 (CELLSNET-43986) - WebWorksheet eller GridWorkSheet har inte metoden SetReadonlyRange

 (CELLSNET-43970) - Regressionsproblem vid uppgradering från 8.4.2.0 till 8.6.0

 (CELLSNET-43952) - LoadValueList API saknas i klassen Aspose.Cells.GridWeb.Validation

 (CELLSNET-43859) - Cell fylld med gul färg exporteras inte till XLSX-fil


## **Offentlig API och bakåtinkompatibla ändringar**


 Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.



 Lägger till enum HtmlLinkTargetType och HtmlSaveOptions.LinkTargetType.

 Det används för att ställa in typen av målattribut i HTML
