---
title: Hantera kommentarer och anteckningar
linktitle: Kommentarer och anteckningar
type: docs
weight: 128
url: /sv/net/comments-and-notes/
description: Infoga och hantera kommentarer eller anteckningar med Aspose.Cells för .Net.
keywords: insert comments, insert notes
---
## **Introduktion**

Kommentarer används för att lägga till ytterligare information till celler. Aspose.Cells tillhandahåller två metoder för att lägga till kommentarer till celler. Det första är att skapa kommentarer i en designerfil manuellt. Dessa kommentarer importeras sedan med Aspose.Cells. Den andra är att lägga till kommentarer med Aspose.Cells API under körning. Det här ämnet diskuterar att lägga till kommentarer till celler med hjälp av Aspose.Cells API. Formatering av kommentarer kommer också att förklaras.

## **Lägger till en kommentar**

 Lägg till en kommentar till en cell genom att anropa[**Kommentarer**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) samlingens[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/add/index) metod (inkapslad i[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objekt). Den nya[**Kommentar**](https://reference.aspose.com/cells/net/aspose.cells/comment) objekt kan nås från[**Kommentarer**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) insamling genom att passera kommentarsindex. Efter att ha kommit åt[**Kommentar**](https://reference.aspose.com/cells/net/aspose.cells/comment) objekt, anpassa kommentarsanteckningen med hjälp av[**Kommentar**](https://reference.aspose.com/cells/net/aspose.cells/comment) objekt[**Notera**](https://reference.aspose.com/cells/net/aspose.cells/comment/properties/note)fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **Kommentarsformatering**

Det är också möjligt att formatera kommentarers utseende genom att konfigurera deras höjd, bredd och teckensnitt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

## **Lägg till en bild för att kommentera**

Med Microsoft Excel 2007 är det också möjligt att ha en bild som bakgrund till en cellkommentar. I Excel 2007 uppnås detta genom att utföra följande steg. (De antar att du redan har lagt till en cellkommentar.)

1. Högerklicka på cellen som innehåller kommentaren.
1.  Välj**Visa/dölj kommentarer**, och ta bort all text från kommentaren.
1. Klicka på kommentarens kant för att välja den.
1.  Välj**Formatera** , då**Kommentar**.
1.  På**Färger och linjer** flik, expandera**Färg** lista.
1.  Klick**Fyllningseffekter**.
1.  På**Bild** fliken, klicka**Välj Bild**.
1. Leta upp och välj bilden.
1.  Klick**OK** tills alla dialogrutor har stängts.

Aspose.Cells tillhandahåller också denna funktion. Nedan är ett kodexempel som skapar en XLSX-fil från grunden och lägger till en kommentar till cell "A1" med en bild som bakgrund.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **Förhandsämnen**
- [Ändra textriktning för kommentaren](/cells/sv/net/change-text-direction-of-the-comment/)
- [Hur man ändrar teckensnittsfärg för kommentar](/cells/sv/net/how-to-change-the-comment-font-color/)
- [Hur man ställer in kommentarsbakgrund](/cells/sv/net/how-to-set-comment-background/)
- [Trådade kommentarer](/cells/sv/net/threaded-comments/)

