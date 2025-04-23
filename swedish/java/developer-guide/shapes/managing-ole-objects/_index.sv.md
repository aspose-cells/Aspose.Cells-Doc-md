---
title: Hantera OLE objekt
type: docs
weight: 30
url: /sv/java/managing-ole-objects/
---

## **Introduktion**

OLE (Object Linking and Embedding) är Microsofts ramverk för en sammanfogande dokumentteknik. Kort sagt är en sammanfogande dokument något som en visnings- skrivbord som kan innehålla visuella och informationsobjekt av alla slag: text, kalendrar, animationer, ljud, rörlig video, 3D, löpande uppdaterade nyheter, kontroller och så vidare. Varje skrivbordsobjekt är en oberoende programenhet som kan interagera med en användare och också kommunicera med andra objekt på skrivbordet.

OLE (Object Linking and Embedding) stöds av många olika program och används för att göra innehåll skapat i ett program tillgängligt i ett annat. Till exempel kan du infoga ett Microsoft Word-dokument i Microsoft Excel. För att se vilka typer av innehåll du kan infoga, klicka på **Object** i **Infoga**-menyn. Endast program som är installerade på datorn och som stöder OLE-objekt visas i rutan **Objekttyp**.

## **Infoga OLE-objekt i en arbetsbok**

Aspose.Cells stöder att lägga till, extrahera och manipulera OLE-objekt i arbetsböcker. Av den anledningen har Aspose.Cells [**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection) klassen, som används för att lägga till ett nytt OLE-objekt i samlingens lista. En annan klass, [**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject), representerar ett OLE-objekt. Den har några viktiga medlemmar:

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData) anger bild (ikon) data av bytemassa typ. Bilden visas för att visa OLE-objektet i arbetsboken.
- [**ObjectData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData) anger objektdata i form av en bytemassa. Denna data visas i sitt relaterade program när du dubbelklickar på OLE-objektikonen.

Följande exempel visar hur man lägger till ett OLE-objekt i en arbetsbok.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **Extrahera OLE-objekt i arbetsboken**

Följande exempel visar hur man extraherar OLE-objekt i en arbetsbok. Exemplet hämtar olika OLE-objekt från en befintlig XLS-fil och sparar olika filer (DOC, XLS, PPT, PDF etc.) baserat på OLE-objektets filformatstyp.

Här är en skärmbild av mallen XLS-filen, den har olika OLE-objekt inbäddade i den första kalkylbladet.

**Mallfilen innehåller fyra OLE-objekt** 

![todo:image_alt_text](managing-ole-objects_1.png)

Efter att koden har körts kan vi spara olika filer baserat på deras respektive OLE-objekts format. Följande är skärmbilder för några av de skapade filerna.

**Den extraherade XLS-filen** 

![todo:image_alt_text](managing-ole-objects_2.png)

**Den extraherade PPT-filen** 

![todo:image_alt_text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **Extrahera inbäddad MOL-fil**

Aspose.Cells stödjer att extrahera objekt av ovanliga typer som MOL (molekylär datafil som innehåller information om atomer och bindningar). Följande kodsnutt demonstrerar extrahering av inbäddad MOL-fil och sparar den på disk genom att använda denna [exempel excelfil](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **Fortsatta ämnen**
- [Åtkomst och ändring av visningsmärket för det länkade OLE-objektet](/cells/sv/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Automatisk uppdatering av OLE-objekt via Microsoft Excel med Aspose.Cells](/cells/sv/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extrahera OLE-objekt från arbetsboken](/cells/sv/java/extract-ole-objects-from-workbook/)
- [Hämta eller ange klassidentifieraren för det inbäddade OLE-objektet](/cells/sv/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
{{< app/cells/assistant language="java" >}}
