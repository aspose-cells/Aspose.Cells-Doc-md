---
title: Komma igång
type: docs
weight: 10
url: /sv/cpp/getting-started/
description: Hur man installerar Aspose Cells för C++ och skapar en Hello World applikation.
---

{{% alert color="primary" %}} 

Den här sidan visar hur du installerar Aspose Cells för C++ och skapar en Hello World-applikation.

{{% /alert %}}

## **Installation**

### **Installera Aspose Cells via NuGet**

NuGet är det enklaste sättet att ladda ner och installera Aspose.Cells for C++. 
1. Skapa ett Microsoft Visual Studio-projekt för C++.
2. Inkludera headerfilen "Aspose.Cells.h".
3. Öppna Microsoft Visual Studio och pakethanteraren NuGet.
4. Sök efter "aspose.cells.cpp" för att hitta den önskade Aspose.Cells for C++. 
5. Klicka på "Installera", Aspose.Cells for C++ kommer att laddas ner och refereras i ditt projekt.

**![Installera Aspose Cells via NuGet](InstallThroughNuget.png)**

Du kan också ladda ner den från nuget-webbsidan för aspose.cells: 
[Aspose.Cells for C++ NuGet-paket](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Fler steg för detaljer](/cells/sv/cpp/installation/)

### **En demo för att använda Aspose.Cells for C++ på Windows**

1. Ladda ner Aspose.Cells for C++ från följande sida:
[Ladda ner Aspose.Cells for C++ (Windows)](https://downloads.aspose.com/cells/cpp/)
2. Packa upp paketet och du hittar ett exempel som visar hur man använder Aspose.Cells for C++.
3. Öppna example.sln med Visual Studio 2017 eller en högre version
4. main.cpp: denna fil visar hur man kodar för att testa Aspose.Cells for C++

### **En demo för att använda Aspose.Cells for C++ på Linux**

1. Ladda ner Aspose.Cells for C++ från följande sida:
[Ladda ner Aspose.Cells for C++ (Linux)](https://downloads.aspose.com/cells/cpp/)
2. Packa upp paketet och du hittar ett exempel som visar hur man använder Aspose.Cells for C++ för Linux.
3. Säkerställ att du är i sökvägen där exemplet finns.
4. Kör "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Kör "cmake --build example/build"

### **En demo för att använda Aspose.Cells for C++ på Mac OS**

1. Ladda ner Aspose.Cells for C++ från följande sida:
[Ladda ner Aspose.Cells for C++ (MacOS)](https://downloads.aspose.com/cells/cpp/)
2. Packa upp paketet och du hittar ett exempel som visar hur man använder Aspose.Cells for C++ för MacOS.
3. Säkerställ att du är i sökvägen där exemplet finns.
4. Kör "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Kör "cmake --build example/build"

## **Skapa Hello World-applikationen**

Följande steg skapar Hello World-applikationen med Aspose.Cells API:

1. Skapa en instans av klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. Om du har en licens, [tillämpa den](/cells/sv/cpp/licensing/).
   Om du använder utvärderingsversionen, hoppa över licensrelaterade kodrader.
1. Åtkomst till valfri cell i ett kalkylblad i Excel-filen.
1. Infoga orden "**Hej Världen!**" i en åtkomstcell.
1. Generera den modifierade Microsoft Excel-filen.

Implementeringen av ovanstående steg visas i exemplen nedan.

### **Kodexempel: Skapa en ny arbetsbok**

Följande exempel skapar en ny arbetsbok från grunden, infogar "**Hej Världen!**" i cell A1 på första kalkylbladet och sparar Excel-filen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

### **Kodexempel: Öppna en befintlig fil**

Följande exempel öppnar en befintlig Microsoft Excel-mallfil, hämtar en cell och kontrollerar värdet i cell A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
