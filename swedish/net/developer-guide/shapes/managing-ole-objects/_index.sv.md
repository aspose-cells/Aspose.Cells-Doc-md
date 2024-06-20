---
title: Hantera OLE objekt
type: docs
weight: 50
url: /sv/net/managing-ole-objects/
---

## **Introduktion**

OLE (Object Linking and Embedding) är Microsofts ramverk för en sammanfogande dokumentteknik. Kort sagt är en sammanfogande dokument något som en visnings- skrivbord som kan innehålla visuella och informationsobjekt av alla slag: text, kalendrar, animationer, ljud, rörlig video, 3D, löpande uppdaterade nyheter, kontroller och så vidare. Varje skrivbordsobjekt är en oberoende programenhet som kan interagera med en användare och också kommunicera med andra objekt på skrivbordet.

OLE (Object Linking and Embedding) stöds av många olika program och används för att göra innehåll skapat i ett program tillgängligt i ett annat. Till exempel kan du infoga ett Microsoft Word-dokument i Microsoft Excel. För att se vilka typer av innehåll du kan infoga, klicka på **Object** i **Infoga**-menyn. Endast program som är installerade på datorn och som stöder OLE-objekt visas i rutan **Objekttyp**.

### **Infoga OLE-objekt i arbetsbladet**

Aspose.Cells stöder att lägga till, extrahera och manipulera OLE-objekt i arbetsblad. Av den anledningen har Aspose.Cells klassen [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection), som används för att lägga till ett nytt OLE-objekt i samlingens lista. En annan klass, [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), representerar ett OLE-objekt. Den har några viktiga medlemmar:

- Egenskapen [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata) anger bild (ikon) data av typen byte array. Bilden kommer att visas för att visa OLE-objektet i arbetsbladet.
- Egenskapen [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata) anger objektdata i form av en byte array. Denna data kommer att visas i sitt relaterade program när du dubbelklickar på OLE-objektikonen.

Följande exempel visar hur man lägger till en OLE-objekt/-objekt i ett arbetsblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **Extrahera OLE-objekt i arbetsboken**

Följande exempel visar hur man extraherar OLE-objekt i en arbetsbok. Exemplet hämtar olika OLE-objekt från en befintlig XLS-fil och sparar olika filer (DOC, XLS, PPT, PDF etc.) baserat på OLE-objektets filformatstyp.

Efter att ha kört koden kan vi spara olika filer baserat på deras respektive OLE-objektets format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **Extrahera inbäddad MOL-fil**

Aspose.Cells stöder att extrahera objekt av ovanliga typer som MOL (molekylär datafil som innehåller information om atomer och bindningar). Följande kodsnutt visar hur man extraherar inbäddad MOL-fil och sparar den på disk genom att använda denna [provexcelfil](94896196.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **Fortsatta ämnen**
- [Åtkomst och ändring av visningsmärket för det länkade OLE-objektet](/cells/sv/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Automatisk uppdatering av OLE-objekt via Microsoft Excel med Aspose.Cells](/cells/sv/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extrahera OLE-objekt från arbetsboken](/cells/sv/net/extract-ole-objects-from-workbook/)
- [Hämta eller ange klassidentifieraren för det inbäddade OLE-objektet](/cells/sv/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Infoga en WAV-fil som ett Ole-objekt](/cells/sv/net/inserting-a-wav-file-as-an-ole-object/)

