---
title: Komma igång
type: docs
weight: 10
url: /sv/cpp/getting-started/
description: Så här installerar du Aspose Cells for C++ och skapar en Hello World-applikation.
---
{{% alert color="primary" %}} 

Den här sidan visar hur du installerar Aspose Cells for C++ och skapar en Hello World-applikation.

{{% /alert %}}

## **Installation**

### **Installera Aspose Cells till NuGet**

 NuGet är det enklaste sättet att ladda ner och installera Aspose.Cells for C++.
1. Skapa ett Microsoft Visual Studio-projekt for C++.
2. Inkludera rubrikfilen "Aspose.Cells.h".
3. Öppna Microsoft Visual Studio och NuGet pakethanterare.
4. Sök "aspose.cells.cpp" för att hitta önskad Aspose.Cells for C++.
5. Klicka på "Installera", Aspose.Cells for C++ kommer att laddas ner och refereras till i ditt projekt.

**![Installera Aspose Cells till NuGet](InstallThroughNuget.png)**

 Du kan också ladda ner den från webbsidan nuget för aspose.cells:
[Aspose.Cells for C++ NuGet Paket](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Fler steg för detaljer](/cells/sv/cpp/installation/)

### **En demo för att använda Aspose.Cells for C++ på Windows**

1. Ladda ner Aspose.Cells for C++ från följande sida:
[Ladda ner Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Packa upp paketet så hittar du en demo som handlar om hur du använder Aspose.Cells for C++.
3. Öppna Demo.sln med Visual Studio 2017 eller högre version
4. main.cpp: den här filen visar hur man kodar för att testa Aspose.Cells for C++
 5. sourceFile/resultFile: dessa två mappar är lagringskataloger som används i main.cpp

### **Hur man använder Aspose.Cells for C++ på Linux OS**

1. Ladda ner Aspose.Cells for C++ från följande sida:
[Ladda ner Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. Packa upp paketet så hittar du en demo som handlar om hur du använder Aspose.Cells for C++ för Linux.
3. Kör "cd Demo" i din Linux-kommandorad
4. Kör "rm -rf build;mkdir build;cd build"
5. Kör "cmake .." kommer att skapa en Makefile av CMakeLists.txt i Demo-mappen
6. Kör "make" för att kompilera
 7. Kör "./demo" så ser du resultatet

## **Skapar Hello World-applikationen**

Stegen nedan skapar Hello World-applikationen med hjälp av Aspose.Cells API:

1.  Skapa en instans av[Arbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass.
1.  Om du har en licens, då[tillämpa den](/cells/sv/cpp/licensing/).
 Om du använder utvärderingsversionen, hoppa över de licensrelaterade kodraderna.
1. Få åtkomst till valfri cell i ett kalkylblad i Excel-filen.
1. Infoga orden "**Hello World!**" in i en cell som nås.
1. Generera den modifierade Microsoft Excel-filen.

Implementeringen av stegen ovan visas i exemplen nedan.

### **Kodexempel: Skapa en ny arbetsbok**

Följande exempel skapar en ny arbetsbok från början, infogar "**Hello World!**" i cell A1 på det första kalkylbladet och sparar Excel-filen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1.cpp" >}}

### **Kodexempel: Öppna en befintlig fil**

Följande exempel öppnar en befintlig Microsoft Excel-mallfil, hämtar en cell och kontrollerar värdet i cellen A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1.cpp" >}}
