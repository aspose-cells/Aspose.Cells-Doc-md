---
title: Verwendung von Aspose.Cells auf 32-Bit- und 64-Bit-Plattformen
type: docs
weight: 10
url: /de/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---
{{% alert color="primary" %}} 

Aspose.Cells ist eine reine .NET-Komponente, die Ihren Bereitstellungsprozess mithilfe von XCOPY-Bereitstellung vereinfachen kann. Um Aspose.Cells zu installieren, können Sie einfach die Komponenten-Assembly (Aspose.Cells.dll) in ein Verzeichnis für Ihre Anwendung kopieren: Die Anwendung kann sie sofort verwenden. Dies ist aufgrund der selbstbeschreibenden Natur der .NET-Komponenten möglich. Diese Art der Bereitstellung hat auch keine Auswirkungen auf den Installationsprozess.

{{% /alert %}} 
## **Einsatz**
Aspose.Cells unterstützt sowohl 32-Bit- als auch 64-Bit-Umgebungen. Wenn Sie die Komponente Aspose.Cells for .NET mit dem Aspose.Cells MSI-Installationsprogramm installieren, werden verschiedene DLLs zu verschiedenen Ordnern im Ordner Aspose.Cells ${installation_Path} hinzugefügt. Siehe die Beschreibung in der Tabelle, welcher Ordner die Assemblys enthält, die Sie mit einer bestimmten Version des Frameworks .NET verwenden müssen.

|**Mappe**|**Beschreibung**|
|:- |:- |
|net2.0|Enthält Assemblys zur Verwendung mit .NET Framework 2.0, 3.0, 3.5, 4.0 und Mono. Dies sind die Assemblys, die Sie normalerweise sowohl für 32-Bit- als auch für 64-Bit-Umgebungen verwenden sollten.|
|net2.0_Authenticode Signiert|Wie oben, aber die Assemblies sind mit Authenticode digital signiert. Signierte Assemblys werden möglicherweise langsamer geladen als ohne Authenticode|
|net3.5_ClientProfile|Enthält Assemblys zur Verwendung mit .NET Framework 3.5 oder 4.0 Client Profile.|
|Netz3.5_Kundenprofil_AuthenticodeSigniert|Wie oben, aber die Assemblies sind mit Authenticode digital signiert. Signierte Assemblys werden möglicherweise langsamer geladen als ohne Authenticode.|
|Netz3.5|Enthält Baugruppen zur Verwendung mit .NET Framework 3.5 oder 4.0.|
|net3.5_Authenticode Signiert|Wie oben, aber die Assemblies sind mit Authenticode digital signiert. Signierte Assemblys werden möglicherweise langsamer geladen als ohne Authenticode.|
|net4.0|Enthält Baugruppen zur Verwendung mit .NET Framework 4.0 und 4.5.|
|netStandard|Enthält Assemblys zur Verwendung mit .Net Standard 2.0|
|netcoreapp2.1|Enthält Assemblys zur Verwendung mit .Net Core 2.1|
|Xamarin.iOS|Enthält Assemblys zur Verwendung mit Xamarin.iOS|
|Xamarin.Android|Enthält Assemblys zur Verwendung mit Xamarin.Android|
|net5.0|Enthält Assemblys zur Verwendung mit .net5.0.|
|net6.0|Enthält Assemblys zur Verwendung mit .net6.0.|
{{% alert color="primary" %}} 

In VS.NET-Projekten (z. B. 2005, 2008, 2010, 2012 usw.) verweist das Dialogfeld „Referenz hinzufügen“ beim Hinzufügen einer Referenz auf Aspose.Cells auf Aspose.Cells.dll-Dateien in den Ordnern net2.0 bzw. net3.5. (Weitere Informationen finden Sie unter Referenzieren von Aspose.Cells aus einem .NET-Projekt.) Sie können den Verweis auf die Bibliothek entsprechend Ihrer Umgebung ändern. Bitte beachten Sie, wenn das Ziel-Framework des Projekts .NET Framework 3.5/4 Client Profile ist, verwenden Sie die Komponentendatei Aspose.Cells.dll, die sich im Ordner net_ClientProfile befindet.

{{% /alert %}}
