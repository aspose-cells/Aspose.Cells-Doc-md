---
title: Komma igång
type: docs
weight: 10
url: /sv/net/getting-started/
---
{{% alert color="primary" %}} 

Den här sidan visar hur du installerar Aspose Cells och skapar en Hello World-applikation.

{{% /alert %}}

##  **Installation**

###  **Installera Aspose.Cells till NuGet**

 NuGet är det enklaste sättet att ladda ner och installera Aspose.Cells for .NET.

1.  Öppna Microsoft Visual Studio och NuGet pakethanterare.
1.  Sök "aspose.cells" för att hitta önskad Aspose.Cells for .NET.
1. Klicka på "Installera", Aspose.Cells for .NET kommer att laddas ner och refereras till i ditt projekt.
**![Installera Aspose Cells till NuGet](install-through-nuget.png)**

 Du kan också ladda ner den från webbsidan nuget för aspose.cells:
[Aspose.Cells for .NET NuGet Paket](https://www.nuget.org/packages/Aspose.Cells/)

[Fler steg för detaljer](/cells/sv/net/installation/)

###  **Installera Aspose.Cells på Windows**

1. Ladda ner Aspose.Cells.msi från följande sida:
[Ladda ner Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. Dubbelklicka på Aspose Cells msi och följ instruktionerna för att installera den:

**![Installera Aspose Cells på Windows](install-on-windows.png)**

[Fler steg för detaljer](/cells/sv/net/installing-aspose-cells-on-windows/)

###  **Installera Aspose.Cells på linux**

I det här exemplet använder jag Ubuntu för att visa hur man börjar använda Aspose.Cells på linux.

1. Skapa en .netcore-applikation med namnet "AsposeCellsTest".
2. Öppna filen "AsposeCellsTest.csproj", lägg till följande rader i den för Aspose.Cells paketreferenser:
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="23.5" />
  </ItemGroup>
{{< /highlight >}}
3. Öppna projektet med VSCode på Ubuntu:
**![Installera Aspose Cells på linux](install-on-linux.png)**
4. kör testet med följande kod:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Obs: Aspose.Cells För .NetStandard kan stödja dina krav på linux.

Gäller: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 och avancerad version.

###  **Installera Aspose.Cells på MAC OS**

I det här exemplet använder jag macOS High Sierra för att visa hur man börjar använda Aspose.Cells på MAC OS.

1. Skapa en .netcore-applikation med namnet "AsposeCellsTest".
2. Öppna programmet med Visual Studio för Mac och installera sedan Aspose Cells till NuGet:
**![Installera Aspose Cells på macOS](install-på-mac-os.png)**
3. kör testet med följande kod:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Om du behöver använda ritningsrelaterade funktioner, installera libgdiplus i macOS, se:
[Hur man installerar libgdiplus i macOS](/cells/sv/net/how-to-install-libgdiplus-in-macos/)

Obs: Aspose.Cells För .NetStandard kan stödja dina krav på MAC OS.

Gäller: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 och avancerad version.

###  **[Kör Aspose Cells i Docker](/cells/net/how-to-run-aspose-cells-in-docker/)**

###  **Hur man använder grafikbibliotek på icke-Windows-plattformar med Net6**

 Aspose.Cells för Net6 använder nu SkiaSharp som grafikbibliotek, som rekommenderas i[officiellt uttalande på Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) . För mer information om hur du använder Aspose.Cells med NET6, se[Hur man kör Aspose.Cells för .Net6](/cells/sv/net/how-to-run-aspose-cells-for-net6/).

##  **Skapar Hello World-applikationen**

Stegen nedan skapar Hello World-applikationen med hjälp av Aspose.Cells API:

1.  Om du har en licens, då[tillämpa den](/cells/sv/net/licensing/).
Om du använder utvärderingsversionen, hoppa över de licensrelaterade kodraderna.
1.  Skapa en instans av[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass för att skapa en ny Excel-fil, eller öppna en befintlig Excel-fil.
1. Få åtkomst till valfri cell i ett kalkylblad i Excel-filen.
1.  Sätt in orden**Hello World!** in i en cell som nås.
1. Generera den modifierade Microsoft Excel-filen.

Implementeringen av stegen ovan visas i exemplen nedan.

###  **Kodexempel: Skapa en ny arbetsbok**

Följande exempel skapar en ny arbetsbok från början, infogar "Hello World!" i cell A1 i det första kalkylbladet och sparas som Excel-fil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **Kodexempel: Öppna en befintlig fil**

Följande exempel öppnar en befintlig Microsoft Excel-mallfil "Sample.xlsx", infogar "Hello World!" i cell A1 i det första kalkylbladet och sparas som Excel-fil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
