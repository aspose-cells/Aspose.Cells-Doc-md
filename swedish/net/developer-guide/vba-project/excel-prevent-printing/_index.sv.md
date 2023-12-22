---
title: Hur man förhindrar användare från att skriva ut Excel-fil
type: docs
weight: 600
url: /sv/net/how-to-prevent-printing-excel/
description: Lär dig hur du förhindrar användare från att skriva ut Excel genom Aspose.Cells for .NET API.
keywords: excel printing, prevent printing excel, how to prevent users from printing excel, excel prevent printing, prevent printing workbook, Prevent users from printing the whole workbook with VBA. 
---
##  **Möjliga användningsscenarier**
I vårt dagliga arbete kan det finnas en del viktig information i excel-filen, för att skydda den interna informationsspridningen kommer företaget inte att tillåta oss att skriva ut dem. Det här dokumentet kommer att berätta hur du förhindrar andra från att skriva ut Excel-filer.

##  **Hur man förhindrar användare från att skriva ut filer i MS-Excel**
Du kan använda följande VBA-kod för att skydda din specifika fil som ska skrivas ut.
1. Öppna din arbetsbok som du inte tillåter andra att skriva ut.
1. Välj fliken "Utvecklare" i Excel-bandet och klicka på knappen "Visa kod" i avsnittet "Kontroller". Alternativt kan du hålla ned ALT + F11-tangenterna för att öppna fönstret Microsoft Visual Basic for Applications.
<br>
<img src="1.png" width=70% />
1. Och sedan i den vänstra Project Explorer, dubbelklicka på ThisWorkbook för att öppna modulen och lägg till några vba-koder.
<br>
<img src="2.png" width=70% />
1. Spara och stäng sedan den här koden och gå tillbaka till arbetsboken, och nu när du skriver ut exempelfilen kommer de inte att tillåtas att skrivas ut och du kommer att få följande varningsruta:
<br>
<img src="3.png" width=70% />

##  **Hur man förhindrar användare från att skriva ut Excel-fil med Aspose.Cells for .NET**

Följande exempelkod illustrerar hur man förhindrar användare från att skriva ut Excel-fil:

1.  Ladda[exempelfil](sample.xlsx).
1. Hämta VbaModuleCollection-objektet från VbaProject-egenskapen i Workbook.
1. Hämta VbaModule-objekt via "ThisWorkbook"-namnet.
1. Ställ in kodegenskapen för VbaModule.
1.  Spara exempelfilen till[xlsm-format](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}