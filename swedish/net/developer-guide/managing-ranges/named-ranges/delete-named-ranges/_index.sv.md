---
title: Ta bort namngivna intervall
type: docs
weight: 90
url: /sv/net/Delete-named-ranges/
description: Du kan lära dig hur du tar bort definierade namn eller namngivna intervall från Excel- eller OpenOffice-filer med Aspose.Cells för .Net .
---
##  **Introduktion**
Om det finns för många definierade namn eller namngivna intervall i Excel-filerna måste vi rensa några för de hänvisas inte igen.

##  **Ta bort Namn Range i MS Excel**

För att ta bort ett namngivet intervall från Excel, kan du följa dessa steg:
1. Öppna Microsoft Excel och öppna arbetsboken som innehåller det namngivna intervallet.
2. Gå till fliken "Formler" i Excel-bandet.
3. Klicka på knappen "Name Manager" i gruppen "Defined Names". Detta öppnar dialogrutan Namnhanterare.
4. I dialogrutan Namnhanterare väljer du det namngivna intervallet som du vill ta bort.
5. Klicka på knappen "Ta bort". Bekräfta raderingen när du uppmanas.
6. Klicka på knappen "Stäng" för att stänga dialogrutan Namnhanterare.
7. Spara arbetsboken för att behålla ändringarna.


##  ** Tar bort Named Range med Aspose.Cells för .Net**
 Med Aspose.Cells för .Net kan du ta bort namngivna intervall eller definierade namn genom att[text](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove) eller[index](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat) i listan.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

Obs: om det definierade namnet refereras av formler, kunde det inte tas bort . Vi kan bara ta bort formeln för det definierade namnet.

##  **Tar bort några namngivna intervall**
När vi tar bort ett definierat namn måste vi kontrollera om det refereras av alla formler i filen.
För att förbättra prestanda för att ta bort namngivna intervall kan vi ta bort några tillsammans.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

##  **Ta bort dubbletter av definierade namn**
Vissa Excel-filer är korrupta eftersom vissa definierade namn är dubbletter. Så vi kan ta bort dessa dubblettnamn för att reparera filen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



