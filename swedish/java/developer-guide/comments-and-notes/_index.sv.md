---
title: Hantera kommentarer och noteringar
linktitle: Kommentarer och noteringar
type: docs
weight: 128
url: /sv/java/comments-and-notes/
description: Infoga och hantera kommentarer eller noteringar med Aspose.Cells for java.
keywords: Infoga kommentarer, infoga noteringar
---

## **Introduktion**

Kommentarer används för att lägga till ytterligare information i celler. Aspose.Cells tillhandahåller två metoder för att lägga till kommentarer i celler. Den första är att skapa kommentarer i en designerfil manuellt. Dessa kommentarer importeras sedan med hjälp av Aspose.Cells. Den andra är att lägga till kommentarer med hjälp av Aspose.Cells API vid körning. Detta ämne diskuterar att lägga till kommentarer i celler med hjälp av Aspose.Cells API. Formatering av kommentarer kommer också att förklaras.

## **Lägga till en kommentar**

Lägg till en kommentar till en cell genom att anropa [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) samlingens **Lägg till** metod (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objektet). Det nya [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) objektet kan nås från [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) samlingen genom att skicka kommentarens index. Efter att ha nått [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) objektet, anpassa kommentarnoteringen genom att använda [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) objektets [**Note**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note) egenskap.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **Kommentarformatering**

Det är också möjligt att formatera kommentarers utseende genom att konfigurera deras höjd, bredd och teckensnittsinställningar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

## **Lägg till en bild till en kommentar**

Med Microsoft Excel 2007 är det också möjligt att ha en bild som bakgrund till en cellkommentar. I Excel 2007 uppnås detta genom följande steg. (De förutsätter att du redan har lagt till en cellkommentar.)

1. Högerklicka på cellen som innehåller kommentaren.
1. Välj ** Visa/dölj kommentarer ** och ta bort all text från kommentaren.
1. Klicka på kommentarens kant för att markera den.
1. Välj ** Formatera **, sedan ** Kommentar **.
1. På fliken ** Färg och linjer **, expandera **Färg** listan.
1. Klicka på **Fyllnings effekter**.
1. På fliken **Bild**, klicka på **Välj bild**.
1. Hitta och välj bilden.
1. Klicka **OK** tills alla dialogrutor har stängts.

Aspose.Cells tillhandahåller också den här funktionen. Nedan finns ett kodexempel som skapar en XLSX-fil från grunden och lägger till en kommentar i cellen "A1" med en bild som bakgrund.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **Fortsatta ämnen**
- [Ändra textriktning för kommentaren](/cells/sv/java/change-text-direction-of-the-comment/)
- [Hur man ändrar färgen på kommentarsfönstret](/cells/sv/java/how-to-change-the-comment-font-color/)
- [Hur man ställer in kommentarens bakgrund](/cells/sv/java/how-to-set-comment-background/)
- [Trådade Kommentarer](/cells/sv/java/threaded-comments/)

{{< app/cells/assistant language="java" >}}
