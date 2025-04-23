---
title: Hantera kommentarer och noteringar
linktitle: Kommentarer och noteringar
type: docs
weight: 128
url: /sv/net/comments-and-notes/
description: Infoga och hantera kommentarer eller anteckningar med Aspose.Cells för .Net.
keywords: Infoga kommentarer, infoga noteringar
---

## **Introduktion**

Kommentarer används för att lägga till ytterligare information i celler. Aspose.Cells tillhandahåller två metoder för att lägga till kommentarer i celler. Den första är att skapa kommentarer i en designerfil manuellt. Dessa kommentarer importeras sedan med hjälp av Aspose.Cells. Den andra är att lägga till kommentarer med hjälp av Aspose.Cells API vid körning. Detta ämne diskuterar att lägga till kommentarer i celler med hjälp av Aspose.Cells API. Formatering av kommentarer kommer också att förklaras.

## **Lägga till en kommentar**

Lägg till en kommentar i en cell genom att anropa [**Comments**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) samlingen [**Add**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/add/index) metod (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objektet). Det nya [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment) objektet kan nås från [**Comments**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) samlingen genom att skicka kommentarindexet. Efter att ha fått tillgång till [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment) objektet, anpassa kommentarnoteringen genom att använda [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment) objektets [**Note**](https://reference.aspose.com/cells/net/aspose.cells/comment/properties/note) egenskap.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **Kommentarformatering**

Det är också möjligt att formatera kommentarers utseende genom att konfigurera deras höjd, bredd och teckensnittsinställningar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **Fortsatta ämnen**
- [Ändra textriktning för kommentaren](/cells/sv/net/change-text-direction-of-the-comment/)
- [Hur man ändrar färgen på kommentarsfönstret](/cells/sv/net/how-to-change-the-comment-font-color/)
- [Hur man ställer in kommentarens bakgrund](/cells/sv/net/how-to-set-comment-background/)
- [Trådade Kommentarer](/cells/sv/net/threaded-comments/)

{{< app/cells/assistant language="csharp" >}}
