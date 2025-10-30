---
title: Ta bort namngivna områden med Golang via C++
linktitle: Ta bort namngivna områden
type: docs
weight: 90
url: /sv/go-cpp/delete-named-ranges/
description: Lär dig hur man tar bort definierade namn eller namngivna områden från Excel eller OpenOffice filer med Aspose.Cells for C++.
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

## **Tar bort Namngivet Område med Aspose.Cells for C++**
Med Aspose.Cells for C++ kan du ta bort namngivna områden eller definierade namn via [text](https://reference.aspose.com/cells/go-cpp/namecollection/remove_stringarray/) eller [index](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) i listan.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges.go" >}}
Obs: om det definierade namnet hänvisas av formler kan det inte tas bort. Vi kan endast ta bort formeln för det definierade namnet.

## **Tar bort vissa namngivna områden**
När vi tar bort ett definierat namn måste vi kontrollera om det används av alla formler i filen.
För att förbättra prestandan vid borttagning av namngivna områden kan vi ta bort några tillsammans.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-1.go" >}}
## **Ta bort dubbla definierade namn**
Vissa Excel-filer blir korrupta eftersom några definierade namn är duplicerade. Därför kan vi ta bort dessa duplicerade namn för att reparera filen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-2.go" >}}
