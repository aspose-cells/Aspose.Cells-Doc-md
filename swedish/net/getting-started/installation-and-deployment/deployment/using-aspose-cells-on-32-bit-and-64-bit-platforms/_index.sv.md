---
title: Använder Aspose.Cells på 32-bitars och 64-bitars plattformar
type: docs
weight: 10
url: /sv/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---
{{% alert color="primary" %}} 

Aspose.Cells är en ren .NET-komponent som kan förenkla din distributionsprocess genom att använda XCOPY-distribution. För att installera Aspose.Cells kan du helt enkelt kopiera komponentsammansättningen (Aspose.Cells.dll) till en katalog för din applikation: applikationen kan börja använda den direkt. Detta är möjligt på grund av .NET-komponenternas självbeskrivande karaktär. Denna typ av distribution har också ingen inverkan på installationsprocessen.

{{% /alert %}} 
## **Spridning**
Aspose.Cells stöder både 32-bitars och 64-bitars miljöer. När du installerar Aspose.Cells för .NET-komponenten med Aspose.Cells MSI-installationsprogram, läggs olika DLL-filer till i olika mappar i mapparna Aspose.Cells ${installation_Path}. Se beskrivningen i tabellen vilken mapp som innehåller assemblyerna du behöver använda med en viss version av .NET Framework.

|**Mapp**|**Beskrivning**|
|:- |:- |
|net2.0|Innehåller sammansättningar att använda med .NET Framework 2.0, 3.0, 3.5, 4.0 och Mono. Det här är de sammansättningar som du normalt ska använda för både 32-bitars och 64-bitars miljöer.|
|net2.0_AuthenticodeSigned|Samma som ovan, men sammansättningarna är digitalt signerade med Authenticode. Signerade sammansättningar kan laddas långsammare än utan autentikod|
|net3.5_ClientProfile|Innehåller sammansättningar att använda med .NET Framework 3.5 eller 4.0 Client Profile.|
|netto3.5_Klientprofil_Autentisk kod Signerad|Samma som ovan, men sammansättningarna är digitalt signerade med Authenticode. Signerade sammansättningar kan laddas långsammare än utan autentikod.|
|netto3.5|Innehåller sammansättningar för användning med .NET Framework 3.5 eller 4.0.|
|net3.5_AuthenticodeSigned|Samma som ovan, men sammansättningarna är digitalt signerade med Authenticode. Signerade sammansättningar kan laddas långsammare än utan autentikod.|
|net4.0|Innehåller sammansättningar att använda med .NET Framework 4.0 och 4.5.|
|netStandard|Innehåller sammansättningar för användning med .Net Standard 2.0|
|netcoreapp2.1|Innehåller sammansättningar för användning med .Net core 2.1|
|Xamarin.iOS|Innehåller sammansättningar att använda med Xamarin.iOS|
|Xamarin.Android|Innehåller sammansättningar att använda med Xamarin.Android|
|net5.0|Innehåller sammansättningar att använda med .net5.0.|
|net6.0|Innehåller sammansättningar att använda med .net6.0.|
{{% alert color="primary" %}} 

VS.NET (till exempel 2005, 2008, 2010, 2012 etc.)-projekt, när du lägger till en referens till Aspose.Cells, hänvisar dialogrutan Lägg till referens till Aspose.Cells.dll-filer i net2.0- respektive net3.5-mapp(ar) . (För ytterligare referens, läs Referens Aspose.Cells från ett .NET-projekt.) Du kan ändra referensen till biblioteket efter din miljö. Observera att om projektets målramverk är .NET Framework 3.5/4 Client Profile, använd komponentfilen Aspose.Cells.dll som finns i mappen net_ClientProfile.

{{% /alert %}}
