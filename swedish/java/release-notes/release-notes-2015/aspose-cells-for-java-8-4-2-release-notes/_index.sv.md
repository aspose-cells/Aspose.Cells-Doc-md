---
title: Aspose.Cells för Java 8.4.2 Release Notes
type: docs
weight: 60
url: /sv/java/aspose-cells-for-java-8-4-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 8.4.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.4.2/)

{{% /alert %}} 

 Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells



\1) Aspose.Cells 


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSJAVA-41289) - Enkelt sätt för sjökortsinställning


## **Buggar**


 (CELLSJAVA-41323) - Vattenstämplar visas inte korrekt

 (CELLSJAVA-41319) - Slicer tas bort i Excel 2010/2013 efter spara

 (CELLSJAVA-41317) - Versaler som skapats med funktionen "versaler" i Excel bevaras inte i PDF

 (CELLSJAVA-41315) - Återgivning av former på sidan 5 är inte korrekt

 (CELLSJAVA-41308) - Formplatsen är fel vid rendering av kalkylark till PDF-format

 (CELLSJAVA-41282) - Pilhuvuden förstoras när kalkylblad med ritningar konverteras till PDF

(CELLSJAVA-41249) - WordArt återges inte bra i utdata-PDF-filen

 (CELLSJAVA-41243) - Horisontell text i formerna renderas vertikalt medan kalkylblad konverteras till PDF

 (CELLSJAVA-41242) - Ritningen är förstörd när kalkylarket renderas till PDF

 (CELLSJAVA-41241) - Cirkelformer konverteras till ovaler samtidigt som kalkylbladet renderas till PDF

 (CELLSJAVA-41233) - Ritobjekt och former i Excel-mall renderas inte bra i utdata-PDF med Aspose.Cells

 (CELLSJAVA-41302) - Senaste Aspose-versionen misslyckas med att spara filen som sparats genom tidigare version

 (CELLSJAVA-41299) - Filen blir korrupt när xls sparas i xlsx-format

 (CELLSJAVA-41284) - Workbook.copy() korrumperar utdata excel-filen

 (CELLSJAVA-41283) - Beräkningsbugg med ELLER-funktion

 (CELLSJAVA-41281) - Automatisk anpassning av kolumner träder inte i kraft med ett fåtal celler med alternativet ShrinkToFit på

 (CELLSJAVA-41313) - Heldragna linjer visas som prickade linjer

(CELLSJAVA-41306) - Excel till PDF-konverteringsproblem - höger sida avskuren

 (CELLSJAVA-41316) - Vissa dataetiketter saknas i den renderade HTML-filen vid kopiering av arbetsbok

 (CELLSJAVA-41314) - DataLabels i diagrammet visas inte i den renderade EMF-bilden

 (CELLSJAVA-41311) - Saknar diagrams axeletiketter vid konvertering till EMF

 (CELLSJAVA-41301) - Hebreiska tecken i "smart art" som finns i excel speglas i PDF-återgivning

 (CELLSJAVA-41300) - Felaktiga cirkeldiagramdata när de återges via Aspose

 (CELLSJAVA-41285) - Höjd på diagrammets plotområde ökar efter att ha kombinerat arbetsböcker

 (CELLSJAVA-41277) - Att endast rendera cirkeldiagram resulterar i en tom PDF

 (CELLSJAVA-41276) - Chart.toImage genererar en tom bild för cirkeldiagram

 (CELLSJAVA-41275) - Två av axeletiketterna saknas i den resulterande EMF vid konvertering av diagram till bild

 (CELLSJAVA-40606) - Den renderade bilden av diagrammet stämmer inte (diagram till bild)

(CELLSJAVA-40368) - Chart.calculate() förlägger X- och Y-axeletiketter


## **Undantag**


 (CELLSJAVA-41310) - java.lang.IndexOutOfBoundsException: Index: 2, Storlek: 2, vid Workbook ctro

 (CELLSJAVA-41307) - java.lang.ArrayIndexOutOfBoundsException: -1 vid Workbook ctor när filen laddas som sparats med Aspose.Cells

 (CELLSJAVA-41280) - Undantag "java.lang.ArrayIndexOutOfBoundsException" inträffade för ett udda anpassat datumformat

 (CELLSJAVA-41274) - java.lang.NullPointerException vid Workbook.save efter upprepade laddnings- och sparaåtgärder


## **Public API och bakåtinkompatibla ändringar**


 Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.



 Lägger till VbaModuleCollection.Add metoder

 Lägger till VBA-modul.



 Lägger till åsidosättande Cells.CopyColumns() metoder.

 Kopierar några kolumner.



Lägger till PasteType.Default och PasteType.DefaultExceptBorders uppräkningar.

 Den används för att kopiera intervall som "Alla" och "Alla utom gränser" i MS Excel.





 Notera

 Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, är de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.4.2 också inkluderade i denna Aspose.Cells för Java v8.4.2.
