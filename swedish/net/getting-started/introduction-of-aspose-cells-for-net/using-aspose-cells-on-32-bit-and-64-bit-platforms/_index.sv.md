---
title: Användning av Aspose.Cells på 32 bitars och 64 bitars plattformar
type: docs
weight: 10
url: /sv/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---

{{% alert color="primary" %}} 

Aspose.Cells är en ren .NET-komponent som kan förenkla din distributionsprocess genom att använda XCOPY-distribution. För att installera Aspose.Cells kan du helt enkelt kopiera komponentförsamlingen (Aspose.Cells.dll) till en katalog för din applikation: applikationen kan börja använda den direkt. Detta är möjligt på grund av den självbeskrivande naturen hos .NET-komponenter. Denna typ av distribution har också nollpåverkan på installationsprocessen.

{{% /alert %}} 
## **Distribution**
Aspose.Cells stöder både 32-bitars och 64-bitars miljöer. När du installerar Aspose.Cells for .NET komponenten med Aspose.Cells MSI-installationsprogrammet, läggs olika DLL:er till olika mappar i Aspose.Cells ${installation_Path} mapp(ar). Se beskrivningen i tabellen vilken mapp som innehåller de assemblys du behöver använda med en specifik version av .NET Framework.

|**Mapp**|**Beskrivning**|
| :- | :- |
|net2.0|Innehåller församlingar att använda med .NET Framework 2.0, 3.0, 3.5, 4.0 och Mono. Detta är församlingar som du normalt sett bör använda för både 32-bitars och 64-bitars miljöer.|
|net2.0_AuthenticodeSigned|Samma som ovan, men församlingarna är digitalt signerade med Authenticode. Signerade församlingar kan ladda långsammare än utan Authenticode|
|net3.5_ClientProfile|Innehåller församlingar att använda med .NET Framework 3.5 eller 4.0 Client Profile.|
|net3.5_ClientProfile_AuthenticodeSigned|Samma som ovan, men församlingarna är digitalt signerade med Authenticode. Signerade församlingar kan ladda långsammare än utan Authenticode.|
|net3.5|Innehåller församlingar att använda med .NET Framework 3.5 eller 4.0.|
|net3.5_AuthenticodeSigned|Samma som ovan, men församlingarna är digitalt signerade med Authenticode. Signerade församlingar kan ladda långsammare än utan Authenticode.|
|net4.0|Innehåller församlingar att använda med .NET Framework 4.0 och 4.5.|
|netStandard|Innehåller församlingar att använda med .Net Standard 2.0|
|netcoreapp2.1|Innehåller församlingar att använda med .Net core 2.1|
|Xamarin.iOS|Innehåller församlingar att använda med Xamarin.iOS|
|Xamarin.Android|Innehåller assemblyn för att använda med Xamarin.Android|
|net5.0|Innehåller assemblyn för att använda med .net5.0.|
|net6.0|Innehåller assemblyn för att använda med .net6.0.|
|net8.0|Innehåller samlingar att använda med .net8.0.|
|net9.0|Innehåller samlingar att använda med .net9.0.|

{{% alert color="primary" %}} 

I VS.NET (till exempel 2005, 2008, 2010, 2012 etc.) projekt, när du lägger till en referens till Aspose.Cells, hänvisar Lägg till referensdialog till Aspose.Cells.dll-filerna i mappen net2.0 eller net3.5. (För ytterligare referens, läs Referencing Aspose.Cells from a .NET project.) Du kan ändra referensen till biblioteket enligt din miljö. Observera om projektets målramverk är .NET Framework 3.5/4 -klientprofil, använd Aspose.Cells.dll-komponentfilen som finns i net_ClientProfile-mappen.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
