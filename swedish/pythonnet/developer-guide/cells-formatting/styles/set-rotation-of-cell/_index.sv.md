---
title: Hur man roterar text i en cell
type: docs
weight: 80
url: /sv/python-net/how-to-rotate-text-of-cell/
description: C# kod för att rotera text i Cell med Aspose.Cells för Python via .NET API
keywords: Python rotera text i Cell, Python programmera rotering av cell i arbetsbok, programmera inställning av cellrotation, Python hur man roterar text i Cell i Excel
---

## **Rotera Text i Cell i Aspose.Cells för Python via .NET**

Aspose.Cells för Python via .NET är en kraftfull .NET- och Java-komponent som gör det möjligt för utvecklare att arbeta med Excel-arket programmässigt. En av funktionerna som tillhandahålls av Aspose.Cells för Python via .NET är möjligheten att rotera celler, vilket gör att du kan anpassa orienteringen av text och förbättra den visuella presentationen av din data. I detta dokument utforskar vi hur man roterar celler med Aspose.Cells för Python via .NET.

## **Hur man roterar text i cell i Excel**
För att rotera en cell i Excel kan du använda följande steg:
1. Öppna Excel och välj den cell eller det cellområde som du vill rotera.
1. Högerklicka på den markerade cellen/cellerna och välj "Formatera celler" i snabbmenyn. Alternativt kan du gå till fliken "Hem" i Excels menyflik, klicka på rullgardinsmenyn "Formatera" i gruppen "Celler" och välj "Formatera celler".
1. I dialogrutan "Formatera celler" navigerar du till fliken "Justering".
1. Under avsnittet "Orientering" ser du alternativen för att rotera texten. Du kan direkt ange önskad rotationsvinkel i grader i rutan "Grader". Positiva värden roterar texten moturs, och negativa värden roterar den medurs.
<br>
![todo:image_alt_text](alignment.png)
1. När du har valt önskad rotation klickar du på "OK" för att tillämpa ändringarna. Den valda cellen/cellerna kommer nu att vara roterade enligt din valda rotationsvinkel eller orientering.

## **Hur man roterar text i cell med Aspose.Cells för Python via .NET API**

[**Style.rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) egenskapen gör det bekvämt att rotera celler. För att rotera celler i Aspose.Cells för Python via .NET behöver du följa dessa steg:
1. Läs in Excel-arbetsboken
<br>
Först måste du ladda Excel-arbetsboken med Aspose.Cells för Python via .NET. Du kan använda Workbook-klassen för att öppna en befintlig Excel-fil eller skapa en ny. 

1. Kom åt arbetsbladet
<br>
När arbetsboken har lästs in måste du komma åt det arbetsblad där du vill rotera cellerna. Du kan antingen komma åt arbetsbladet genom dess index eller namn. 

1. Rotera texten i cellen
<br>
Nu när du har åtkomst till arbetsbladet kan du rotera cellerna genom att ändra Style-objektet för de önskade cellerna. Style-objektet låter dig ställa in olika formateringsalternativ, inklusive rotation. 

1. Spara arbetsboken
<br>
Efter att ha roterat cellerna kan du spara den modifierade arbetsboken till en fil eller ström med hjälp av Save -metoden.

## **Python Exempelkod**

Var god se följande kod, den skapar ett arbetsboksobjekt och ställer in olika rotationsvinklar för flera celler. Skärmbilden visar resultatet efter körningen av det här provkoden.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Cells-rotate-text.py" >}}

