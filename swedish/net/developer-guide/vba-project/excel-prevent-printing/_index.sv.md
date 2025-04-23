---
title: Hur man förhindrar användare från att skriva ut Excel fil
type: docs
weight: 600
url: /sv/net/how-to-prevent-printing-excel/
description: Lär dig hur man förhindrar användare från att skriva ut Excel genom Aspose.Cells for .NET API.
keywords: excel utskrift, förhindra utskrift av Excel, hur man förhindrar användare från att skriva ut Excel, Excel förhindra utskrift, förhindra utskrift av arbetsbok, Förhindra användare från att skriva ut hela arbetsboken med VBA. 
---

## **Möjliga användningsscenario**
I vårt dagliga arbete kan det finnas viktig information i Excel-filen, för att skydda interna data sprids företaget kommer inte att tillåta oss att skriva ut dem. Detta dokument kommer att berätta för dig hur man förhindrar andra från att skriva ut Excel-filer.

## **Hur man förhindrar användare från att skriva ut fil i MS-Excel**
Du kan tillämpa följande VBA-kod för att skydda din specifika fil från att skrivas ut.
1. Öppna arbetsboken som du inte tillåter andra att skriva ut.
1. Välj "Utvecklare"-fliken i Excel-menyn och klicka på "Visa kod"-knappen i "Kontroller"-avsnittet. Alternativt kan du trycka ner ALT + F11-tangenterna för att öppna fönstret för Microsoft Visual Basic for Applications.
<br>
<img src="1.png" width=70% />
1. Och sedan i den vänstra projektfönstret dubbelklickar du på ThisWorkbook för att öppna modulen och lägg till lite vba-kod.
<br>
<img src="2.png" width=70% />
1. Spara sedan och stäng den här koden och gå tillbaka till arbetsboken, och nu när du skriver ut provfilen kommer de inte att tillåtas att skrivas ut och du kommer att få följande varningsruta:
<br>
<img src="3.png" width=70% />

## **Hur man förhindrar användare från att skriva ut Excel-fil med hjälp av Aspose.Cells for .NET**

Följande exempelkod illustrerar hur man förhindrar användare från att skriva ut Excel-fil:

1. Ladda in [provfilen](sample.xlsx).
1. Hämta VbaModuleCollection-objektet från VbaProject-egenskapen i arbetsboken.
1. Hämta VbaModule-objekt via namnet "ThisWorkbook".
1. Ange egenskapen codes på VbaModule.
1. Spara provfilen till [xlsm-format](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}
{{< app/cells/assistant language="csharp" >}}
