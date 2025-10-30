---
title: Komma igång
type: docs
weight: 10
url: /sv/net/getting-started/
---

{{% alert color="primary" %}} 

Denna sida kommer att visa dig hur du installerar Aspose Cells och skapar en Hello World-applikation.

{{% /alert %}}

## **Installation**

### **Installera Aspose.Cells genom NuGet**

NuGet är det enklaste sättet att ladda ner och installera Aspose.Cells for .NET. 

1. Öppna Microsoft Visual Studio och NuGet-paket hanterare. 
1. Sök efter "aspose.cells" för att hitta önskad Aspose.Cells for .NET. 
1. Klicka på "Installera", Aspose.Cells for .NET kommer att laddas ner och refereras i ditt projekt.
**![Installera Aspose Cells genom NuGet](install-through-nuget.png)**

Du kan också ladda ner den från nuget-webbsidan för aspose.cells: 
[Aspose.Cells for .NET NuGet-paket](https://www.nuget.org/packages/Aspose.Cells/)

[Fler steg för detaljer](/cells/sv/net/installation/)

### **Installera Aspose.Cells på Windows**

1. Ladda ner Aspose.Cells.msi från följande sida:
[Ladda ner Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. Dubbelklicka på Aspose Cells msi och följ anvisningarna för att installera den:

**![Installera Aspose Cells på windows](install-on-windows.png)**

[Fler steg för detaljer](/cells/sv/net/installing-aspose-cells-on-windows/)

### **Installera Aspose.Cells på linux**

I det här exemplet använder jag Ubuntu för att visa hur du börjar använda Aspose.Cells på linux.

1. Skapa en .netcore-applikation med namnet "AsposeCellsTest".
2. Öppna filen "AsposeCellsTest.csproj", lägg till följande rader i den för Aspose.Cells-paketreferenser:
{{< highlight plain >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="25.10" />
  </ItemGroup>
{{< /highlight >}}
3. Öppna projektet med VSCode på Ubuntu:
**![Installera Aspose Cells på linux](install-on-linux.png)**
4. kör testet med följande kod:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Obs! Aspose.Cells för .NetStandard kan stödja dina krav på linux.

Gäller för: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 och avancerad version.

### **Installera Aspose.Cells på MAC OS**

I det här exemplet använder jag macOS High Sierra för att visa hur du börjar använda Aspose.Cells på MAC OS.

1. Skapa en .netcore-applikation med namnet "AsposeCellsTest".
2. Öppna applikationen med Visual Studio för Mac, sedan installera Aspose Cells via NuGet:
**![Installera Aspose Cells på macOS](install-on-mac-os.png)**
3. kör testet med följande kod:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Om du behöver använda ritrelaterade funktioner, installera libgdiplus i macOS, se:
[Hur man installerar libgdiplus i macOS](/cells/sv/net/how-to-install-libgdiplus-in-macos/)

Obs! Aspose.Cells för .NetStandard kan stödja dina krav på MAC OS.

Gäller för: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 och avancerad version.

### [**Run Aspose Cells in Docker**](/cells/sv/net/how-to-run-aspose-cells-in-docker/)

### **Hur man använder grafikbibliotek på icke-Windows-plattformar med Net6**

Aspose.Cells för Net6 använder nu SkiaSharp som grafikbibliotek, som rekommenderas i [Microsofts officiella uttalande](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md). För mer information om att använda Aspose.Cells med NET6, se [Hur man kör Aspose.Cells för .Net6](/cells/sv/net/how-to-run-aspose-cells-for-net6/).

## **Skapa Hello World-applikationen**

Följande steg skapar Hello World-applikationen med Aspose.Cells API:

1. Om du har en licens, [ansök om den](/cells/sv/net/licensing/).
   Om du använder utvärderingsversionen, hoppa över licensrelaterade kodrader.
1. Skapa en instans av klassen [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) för att skapa en ny Excel-fil eller öppna en befintlig Excel-fil.
1. Åtkomst till valfri cell i ett kalkylblad i Excel-filen.
1. Infoga orden **Hello World!** i en åtkomstcell.
1. Generera den modifierade Microsoft Excel-filen.

Implementeringen av ovanstående steg visas i exemplen nedan.

### **Kodexempel: Skapa en ny arbetsbok**

Det följande exemplet skapar en ny arbetsbok från grunden, infogar "Hello World!" i cell A1 i den första kalkylbladet och sparar den som Excel-fil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Kodexempel: Öppna en befintlig fil**

Följande exempel öppnar en befintlig Microsoft Excel-mal fil "Prov.xlsx", sätter in "Hej världen!" i cell A1 i det första kalkylarket och sparar som Excel fil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
