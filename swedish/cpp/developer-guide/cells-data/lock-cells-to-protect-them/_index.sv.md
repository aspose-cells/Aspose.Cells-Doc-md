---
title: Hur man låser celler för att skydda dem med C++
linktitle: Hur man låser celler för att skydda dem
type: docs
weight: 130
url: /sv/cpp/how-to-lock-cells-to-protect-them/
description: Denna artikel visar kod som förklarar hur man låser celler för att skydda dem med Aspose.Cells biblioteket i C++.
keywords: C++ Lås celler för att skydda dem, Hur man låser celler för att skydda dem med C++, Lås celler för att skydda dem i C++.
---

## **Möjliga användningsscenario**
Att låsa celler för att skydda dem är en vanlig praxis i kalkylbladsapplikationer, som Microsoft Excel eller Google Sheets, av flera viktiga skäl:

1. Förebygga oavsiktliga ändringar: Att låsa celler kan förhindra att användare oavsiktligt modifierar viktig data eller formler. Detta är särskilt användbart i komplexa kalkylblad där oavsiktliga ändringar kan leda till betydande fel.

1. Upprätthållande av dataintegritet: Genom att låsa celler kan du säkerställa att kritiska data förblir konsekventa och korrekta. Detta är avgörande för finansiella dokument, rapporter och andra dokument där dataintegritet är väsentlig.

1. Kontrollad åtkomst: I samarbetsmiljöer låter låsning av celler dig kontrollera vem som kan redigera vissa delar av ett kalkylblad. Till exempel kan du vilja tillåta endast vissa teammedlemmar att redigera specifika celler samtidigt som resten av bladet är skyddat.

1. Skydda formler: Formler är ofta avgörande för beräkningar och dataanalys. Att låsa celler som innehåller formler säkerställer att dessa formler inte oavsiktligt förändras eller tas bort, vilket kan störa funktionaliteten i hela bladet.

1. Tillämpa affärsregler: I vissa fall kan specifika affärsregler eller regler kräva att viss data skyddas mot förändringar. Att låsa celler hjälper till att följa dessa krav.

1. Vägledning för användare: Genom att låsa celler och ge tydliga instruktioner om vilka celler som kan redigeras kan du vägleda användare om hur de ska interagera med kalkylbladet, vilket minskar förvirring och fel.

## **Hur låser du celler för att skydda dem i Excel**
Så här låser du celler i Microsoft Excel:

1. Välj cellerna att låsa: Välj de celler du vill låsa. Om du vill låsa hela bladet kan du hoppa över detta steg.
1. Öppna dialogrutan för formatering av celler: Högerklicka på de valda cellerna och välj "Formatera celler," eller tryck på Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Lås cellerna: I dialogrutan Formatera celler, gå till fliken "Skydd". Markera kryssrutan "Låst". Klicka på "OK."
1. Skydda arket: Gå till "Granska"-fliken på menyfliksområdet. Klicka på "Skydda blad." Ange ett lösenord (valfritt) och välj de behörigheter du vill tillåta (t.ex. välja låsta celler, formatera celler etc.). Klicka på "OK."
<br>
<img src="2.png" width=60% />

## **Hur man låser celler för att skydda dem med C++**

Aspose.Cells är ett kraftfullt bibliotek för att arbeta med Excel-filer programmässigt. För att låsa celler med Aspose.Cells måste du följa dessa steg: ladda [exempel fil](sample.xlsx), lås upp alla celler först (eftersom alla celler som standard är låsta men inte tvingade förrän arket skyddas), lås sedan de specifika cellerna du vill skydda, och slutligen skydda arket för att genomdriva låsningen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Unlock all cells first
    Style unlockStyle = workbook.CreateStyle();
    unlockStyle.SetIsLocked(false);

    StyleFlag styleFlag;
    styleFlag.SetLocked(true);
    sheet.GetCells().ApplyStyle(unlockStyle, styleFlag);

    // Lock specific cells (e.g., A1 and B2)
    Style lockStyle = workbook.CreateStyle();
    lockStyle.SetIsLocked(true);

    sheet.GetCells().Get(u"A1").SetStyle(lockStyle);
    sheet.GetCells().Get(u"B2").SetStyle(lockStyle);

    // Protect the worksheet to enforce the locking
    sheet.Protect(ProtectionType::All);

    // Save the modified workbook
    workbook.Save(u"output_locked.xlsx");

    std::cout << "Worksheet protection applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Utdataresultat**
Denna kod säkerställer att endast de angivna cellerna (A1 och B2 i detta exempel) är låsta, och att arket är skyddat för att genomdriva dessa inställningar. Alla andra celler i arket förblir upplåsta och redigerbara.

<br>
<img src="3.png" width=60% />

{{< app/cells/assistant language="cpp" >}}
