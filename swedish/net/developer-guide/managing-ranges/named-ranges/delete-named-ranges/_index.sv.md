---
title: Ta bort namngivna områden
type: docs
weight: 90
url: /sv/net/Delete-named-ranges/
description: Du kan lära dig hur man tar bort definierade namn eller namngivna områden från Excel eller OpenOffice filer med Aspose.Cells for .Net .
---

## **Introduktion**
Om det finns för många definierade namn eller namngivna områden i Excel-filerna måste vi rensa några så att de inte längre refereras till.

## **Ta bort namngivet område i MS Excel**

För att ta bort ett namngivet område från Excel kan du följa dessa steg:
1. Öppna Microsoft Excel och öppna arbetsboken som innehåller det namngivna området.
2. Gå till fliken "Formler" i Excel-ribbonen.
3. Klicka på knappen "Namnhanterare" i gruppen "Definierade namn". Detta öppnar dialogrutan för Namnhanterare.
4. I dialogrutan för Namnhanterare väljer du det namngivna området du vill ta bort.
5. Klicka på knappen "Ta bort". Bekräfta borttagningen vid behov.
6. Klicka på knappen "Stäng" för att stänga dialogrutan för Namnhanterare.
7. Spara arbetsboken för att behålla ändringarna.


## **Tar bort namngivet område med Aspose.Cells for .Net**
Med Aspose.Cells for .Net kan du ta bort namngivna områden eller definierade namn genom [text](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove) eller [index](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat) i listan.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

Observera: Om det definierade namnet används av formler kan det inte tas bort. Vi kan bara ta bort formeln för det definierade namnet.

## **Tar bort vissa namngivna områden**
När vi tar bort ett definierat namn måste vi kontrollera om det används av alla formler i filen.
För att förbättra prestandan för att ta bort namngivna områden kan vi ta bort vissa tillsammans.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

## **Ta bort dubbla definierade namn**
Vissa Excel-filer korrumperas eftersom vissa definierade namn är dubletter. Så vi kan ta bort dessa dubbla namn för att reparera filen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



{{< app/cells/assistant language="csharp" >}}
