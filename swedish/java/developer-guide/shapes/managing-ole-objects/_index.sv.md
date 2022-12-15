---
title: Hantera OLE-objekt
type: docs
weight: 30
url: /sv/java/managing-ole-objects/
---
## **Introduktion**

OLE (Object Linking and Embedding) är Microsoft:s ramverk för en sammansatt dokumentteknologi. Kortfattat är ett sammansatt dokument något som ett skärmskrivbord som kan innehålla visuella objekt och informationsobjekt av alla slag: text, kalendrar, animationer, ljud, rörlig video, 3D, ständigt uppdaterade nyheter, kontroller och så vidare. Varje skrivbordsobjekt är en oberoende programenhet som kan interagera med en användare och även kommunicera med andra objekt på skrivbordet.

 OLE (Object Linking and Embedding) stöds av många olika program och används för att göra innehåll skapat i ett program tillgängligt i ett annat. Till exempel kan du infoga ett Microsoft Word-dokument i Microsoft Excel. Klicka på för att se vilka typer av innehåll du kan infoga**Objekt** på**Föra in** meny. Endast program som är installerade på datorn och som stöder OLE-objekt visas i**Objekttyp** låda.

## **Infoga OLE-objekt i ett kalkylblad**

Aspose.Cells stöder att lägga till, extrahera och manipulera OLE-objekt i kalkylblad. Av denna anledning har Aspose.Cells[**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection)klass, används för att lägga till ett nytt OLE-objekt till samlingslistan. En annan klass,[**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject), representerar ett OLE-objekt. Den har några viktiga medlemmar:

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData)anger bilddata (ikon) av byte-arraytyp. Bilden kommer att visas för att visa OLE-objektet i kalkylbladet.
- [**Objektdata**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData)specificerar objektdata i form av en byte-array. Dessa data kommer att visas i dess relaterade program när du dubbelklickar på OLE-objektikonen.

Följande exempel visar hur man lägger till ett OLE-objekt i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **Extrahera OLE-objekt i arbetsboken**

Följande exempel visar hur man extraherar OLE-objekt i en arbetsbok. Exemplet hämtar olika OLE-objekt från en befintlig XLS-fil och sparar olika filer (DOC, XLS, PPT, PDF, etc.) baserat på OLE-objektets filformattyp.

Här är skärmdumpen av mallen XLS-fil, den har olika OLE-objekt inbäddade i det första kalkylbladet.

**Mallfilen innehåller fyra OLE-objekt** 

![todo:image_alt_text](managing-ole-objects_1.png)

Efter att ha kört koden kan vi spara olika filer baserat på deras respektive OLE Objects-formattyper. Följande är skärmdumpar för några av de skapade filerna.

**Den extraherade XLS-filen** 

![todo:image_alt_text](managing-ole-objects_2.png)

**Den extraherade PPT-filen** 

![todo:image_alt_text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **Extraherar inbäddad MOL-fil**

Aspose.Cells stöder extrahering av objekt av ovanliga typer som MOL (molekylär datafil som innehåller information om atomer och bindningar). Följande kodavsnitt visar att man extraherar en inbäddad MOL-fil och sparar den på disken genom att använda detta[exempel på excel-fil](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **Förhandsämnen**
- [Få åtkomst till och ändra visningsetiketten för det länkade Ole-objektet](/cells/sv/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Uppdatera OLE-objekt automatiskt via Microsoft Excel med Aspose.Cells](/cells/sv/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extrahera OLE-objekt från arbetsbok](/cells/sv/java/extract-ole-objects-from-workbook/)
- [Hämta eller ställ in klassidentifieraren för det inbäddade OLE-objektet](/cells/sv/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
