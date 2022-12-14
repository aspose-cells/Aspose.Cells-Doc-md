---
title: Aspose.Cells för .NET 8.1.2 Release Notes
type: docs
weight: 50
url: /sv/net/aspose-cells-for-net-8-1-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 8.1.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.1.2/)

{{% /alert %}} 

Aspose.Cells för .NET har uppdaterats till version 8.1.2 och vi är glada att kunna meddela att denna utgåva innehåller över 20 nya användbara förbättringar.
Med Aspose.Cells för .NET kan du arbeta med XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS och andra format i dina applikationer. Du kan också visa, generera, ändra, konvertera, rendera och skriva ut arbetsböcker utan att använda Microsoft Excel.
Besök dokumentationen för att lära dig hur du kommer igång med Aspose.Cells för .NET.
Observera att den här nedladdningen innehåller en fullt fungerande version av produkten, men utan en licensuppsättning kommer den att köras i utvärderingsläge med vissa begränsningar. För att testa Aspose.Cells utan dessa utvärderingsbegränsningar kan du begära en gratis 30-dagars tillfällig licens.
 Följande är en lista över ändringar i denna version av Aspose.Cells.

\1) Aspose.Cells 
## **Andra förbättringar och förändringar**

## **Prestanda**


 (CELLSNET-42820) - FileFormatUtil.DetectFileFormat använder allt systemets tillgängliga minne samtidigt som det upptäcker ett skadat kalkylblad


## **Buggar**


 (CELLSNET-42801) - Data saknas när pivottabell konverteras till PDF

 (CELLSNET-42800) - Total titel saknas när pivottabell konverteras till PDF

 (CELLSNET-42799) - Cell Sammanfogningsproblem när pivottabell konverteras till PDF

 (CELLSNET-42775) - Pivottabell-bugg angående delsummor

 (CELLSNET-42749) - Pillinjerna är för tjocka än i Excel

 (CELLSNET-42438) - Sammanfogat cellinnehåll försvinner när rader filtreras och kalkylark konverteras till HTML

 (CELLSNET-42353) - Aspose.Cells producera pil dubbel i tjocklek samtidigt som XLS konverteras till PDF

 (CELLSNET-42747) - Utskrivet resultat centreras inte korrekt och sista raden går vilse

(CELLSNET-42744) - Texten i sammanslagna celler visas inte vid konvertering till PDF

 (CELLSNET-42781) - Form till bild Fel vid konvertering av ExcelShapeToImageRedactedEx.xls till Tiff

 (CELLSNET-42780) - Form till bild Fel vid konvertering av ExcelShapeToImageError.xls till Tiff

 (CELLSNET-42760) - Linjen är mycket tjock när den sparas som pdf med Aspose-celler

 (CELLSNET-42622) - Excel-diagrametiketter överlappar efter att ha öppnat och sparat xlsm-filen

 (CELLSNET-42836) - Matchningsformeln har inte beräknats korrekt med Workbook.CalculateFormula

 (CELLSNET-42818) - #NUM! fel vid läsning av vissa celler

 (CELLSNET-42811) - Smarta markörer - Cells Formatering bibehålls inte på Grupp:Sammanfoga, Hoppa över:1


## **Undantag**


 (CELLSNET-42635) - MonoDevelop orsakar SIGSEGV-fel

 (CELLSNET-42812) - CellsException vid konvertering av kalkylblad till PDF

 (CELLSNET-42788) - System.NullReferenceException för att spara ods-filen


## **Public API och bakåtinkompatibla ändringar**


Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.



Public WarningInfo, WarningType-klasser, IWarningCallback-gränssnitt och SaveOptions.WarningCallback, ImageOrPrintOptions.WarningCallback-egenskapen.

 Stöder varningar när teckensnitt har ersatts.



Ta bort föråldrad PdfSaveOptions.ChartImageType-egenskap.


