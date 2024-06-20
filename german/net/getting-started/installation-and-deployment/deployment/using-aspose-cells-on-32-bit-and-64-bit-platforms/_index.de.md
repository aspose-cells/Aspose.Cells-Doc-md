---
title: Verwendung von Aspose.Cells auf 32 Bit und 64 Bit Plattformen
type: docs
weight: 10
url: /de/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---

{{% alert color="primary" %}} 

Aspose.Cells ist eine reine .NET-Komponente, die Ihren Bereitstellungsprozess vereinfachen kann, indem Sie eine XCOPY-Bereitstellung verwenden. Um Aspose.Cells zu installieren, können Sie einfach die Komponentenassembly (Aspose.Cells.dll) in ein Verzeichnis für Ihre Anwendung kopieren: Die Anwendung kann sofort damit beginnen, diese zu verwenden. Dies ist aufgrund der selbstbeschreibenden Natur von .NET-Komponenten möglich. Diese Art der Bereitstellung hat auch keinerlei Auswirkungen auf den Installationsprozess.

{{% /alert %}} 
## **Bereitstellung**
Aspose.Cells unterstützt sowohl 32-Bit- als auch 64-Bit-Umgebungen. Wenn Sie das Aspose.Cells for .NET-Komponente mit dem Aspose.Cells MSI-Installer installieren, werden verschiedene DLLs in verschiedenen Ordnern im Aspose.Cells ${installation_Path}-Ordner hinzugefügt. Beachten Sie die Beschreibung in der Tabelle, welcher Ordner die Assemblys enthält, die Sie mit einer bestimmten Version des .NET-Frameworks verwenden müssen.

|**Ordner**|**Beschreibung**|
| :- | :- |
|net2.0|Enthält Assemblys zur Verwendung mit .NET Framework 2.0, 3.0, 3.5, 4.0 und Mono. Dies sind die Assemblys, die Sie normalerweise für 32-Bit- und 64-Bit-Umgebungen verwenden sollten.|
|net2.0_AuthenticodeSigned|Gleich wie oben, aber die Assemblys sind digital mit Authenticode signiert. Signierte Assemblys laden möglicherweise langsamer als ohne Authenticode.|
|net3.5_ClientProfile|Enthält Assemblys zur Verwendung mit .NET Framework 3.5 oder 4.0 Client Profile.|
|net3.5_ClientProfile_AuthenticodeSigned|Gleich wie oben, aber die Assemblys sind digital mit Authenticode signiert. Signierte Assemblys laden möglicherweise langsamer als ohne Authenticode.|
|net3.5|Enthält Assemblys zur Verwendung mit .NET Framework 3.5 oder 4.0.|
|net3.5_AuthenticodeSigned|Gleich wie oben, aber die Assemblys sind digital mit Authenticode signiert. Signierte Assemblys laden möglicherweise langsamer als ohne Authenticode.|
|net4.0|Enthält Assemblys zur Verwendung mit .NET Framework 4.0 und 4.5.|
|netStandard|Enthält Assemblys zur Verwendung mit .Net Standard 2.0|
|netcoreapp2.1|Enthält Assemblys zur Verwendung mit .Net core 2.1|
|Xamarin.iOS|Enthält Assemblys zur Verwendung mit Xamarin.iOS|
|Xamarin.Android|Enthält Assemblys zur Verwendung mit Xamarin.Android|
|net5.0|Enthält Assemblys zur Verwendung mit .net5.0.|
|net6.0|Enthält Assemblys zur Verwendung mit .net6.0.|
{{% alert color="primary" %}} 

In VS.NET (zum Beispiel 2005, 2008, 2010, 2012 usw.)-Projekten, wenn Sie einen Verweis auf Aspose.Cells hinzufügen, verweist der Verweisdialog auf die Aspose.Cells.dll-Dateien im Ordner net2.0 oder net3.5. (Lesen Sie für weitere Informationen Verweisen von Aspose.Cells aus einem .NET-Projekt.) Sie können den Verweis auf die Bibliothek entsprechend Ihrer Umgebung ändern. Bitte beachten Sie, dass, wenn das Ziel-Framework des Projekts .NET Framework 3.5/4 Client Profile ist, verwenden Sie die Aspose.Cells.dll-Komponentendatei im Ordner net_ClientProfile.

{{% /alert %}}
