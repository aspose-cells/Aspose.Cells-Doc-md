---
title: Hantera OLE-objekt
type: docs
weight: 50
url: /sv/net/managing-ole-objects/
---
## **Introduktion**

OLE (Object Linking and Embedding) är Microsoft:s ramverk för en sammansatt dokumentteknologi. Kortfattat är ett sammansatt dokument något som ett skärmskrivbord som kan innehålla visuella objekt och informationsobjekt av alla slag: text, kalendrar, animationer, ljud, rörlig video, 3D, ständigt uppdaterade nyheter, kontroller och så vidare. Varje skrivbordsobjekt är en oberoende programenhet som kan interagera med en användare och även kommunicera med andra objekt på skrivbordet.

 OLE (Object Linking and Embedding) stöds av många olika program och används för att göra innehåll skapat i ett program tillgängligt i ett annat. Till exempel kan du infoga ett Microsoft Word-dokument i Microsoft Excel. Klicka på för att se vilka typer av innehåll du kan infoga**Objekt** på**Föra in** meny. Endast program som är installerade på datorn och som stöder OLE-objekt visas i**Objekttyp** låda.

### **Infoga OLE-objekt i arbetsbladet**

Aspose.Cells stöder att lägga till, extrahera och manipulera OLE-objekt i kalkylblad. Av denna anledning har Aspose.Cells[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) klass, används för att lägga till ett nytt OLE-objekt till samlingslistan. En annan klass,[**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), representerar ett OLE-objekt. Den har några viktiga medlemmar:

-  De[**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)egenskapen specificerar bilddata (ikon) av byte-arraytyp. Bilden kommer att visas för att visa OLE-objektet i kalkylbladet.
-  De[**Objektdata**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)egenskapen specificerar objektdata i form av en byte-array. Dessa data kommer att visas i dess relaterade program när du dubbelklickar på OLE-objektikonen.

Följande exempel visar hur man lägger till ett eller flera OLE-objekt i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **Extrahera OLE-objekt i arbetsboken**

Följande exempel visar hur man extraherar OLE-objekt i en arbetsbok. Exemplet hämtar olika OLE-objekt från en befintlig XLS-fil och sparar olika filer (DOC, XLS, PPT, PDF, etc.) baserat på OLE-objektets filformattyp.

Efter att ha kört koden kan vi spara olika filer baserat på deras respektive OLE Objects-formattyper.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **Extraherar inbäddad MOL-fil**

Aspose.Cells stöder extrahering av objekt av ovanliga typer som MOL (molekylär datafil som innehåller information om atomer och bindningar). Följande kodavsnitt visar att man extraherar en inbäddad MOL-fil och sparar den på disken genom att använda detta[exempel på excel-fil](94896196.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **Förhandsämnen**
- [Få åtkomst till och ändra visningsetiketten för det länkade Ole-objektet](/cells/sv/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Uppdatera OLE-objekt automatiskt via Microsoft Excel med Aspose.Cells](/cells/sv/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extrahera OLE-objekt från arbetsbok](/cells/sv/net/extract-ole-objects-from-workbook/)
- [Hämta eller ställ in klassidentifieraren för det inbäddade OLE-objektet](/cells/sv/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Infoga en WAV-fil som ett Ole-objekt](/cells/sv/net/inserting-a-wav-file-as-an-ole-object/)

