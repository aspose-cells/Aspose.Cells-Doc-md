---
title: Hantera kommentarer och anteckningar
linktitle: Kommentarer och anteckningar
type: docs
weight: 128
url: /sv/java/comments-and-notes/
description: Infoga och hantera kommentarer eller anteckningar med Aspose.Cells för java.
keywords: insert comments, insert notes
---
## **Introduktion**

Kommentarer används för att lägga till ytterligare information till celler. Aspose.Cells tillhandahåller två metoder för att lägga till kommentarer till celler. Det första är att skapa kommentarer i en designerfil manuellt. Dessa kommentarer importeras sedan med Aspose.Cells. Den andra är att lägga till kommentarer med Aspose.Cells API vid körning. Det här ämnet diskuterar att lägga till kommentarer till celler med Aspose.Cells API. Formateringskommentarer kommer också att förklaras.

## **Lägger till en kommentar**

 Lägg till en kommentar till en cell genom att anropa[**Kommentarer**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) samlingens**Lägg till** metod (inkapslad i[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objekt). Den nya[**Kommentar**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) objekt kan nås från[**Kommentarer**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) insamling genom att passera kommentarsindex. Efter att ha kommit åt[**Kommentar**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) objekt, anpassa kommentaren genom att använda[**Kommentar**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) objekt[**Notera**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note)fast egendom.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **Kommentarsformatering**

Det är också möjligt att formatera kommentarers utseende genom att konfigurera deras höjd, bredd och teckensnitt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **Förhandsämnen**
- [Ändra textriktning för kommentaren](/cells/sv/java/change-text-direction-of-the-comment/)
- [Hur man ändrar teckensnittsfärg för kommentar](/cells/sv/java/how-to-change-the-comment-font-color/)
- [Hur man ställer in kommentarsbakgrund](/cells/sv/java/how-to-set-comment-background/)
- [Trådade kommentarer](/cells/sv/java/threaded-comments/)

