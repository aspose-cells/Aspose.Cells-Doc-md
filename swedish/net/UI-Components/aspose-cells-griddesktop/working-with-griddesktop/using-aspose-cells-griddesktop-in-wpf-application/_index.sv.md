---
title: Använda Aspose.Cells.GridDesktop i WPF applikation
type: docs
weight: 50
url: /sv/net/aspose-cells-griddesktop/use-aspose-cells-griddesktop-in-wpf-application/
keywords: GridDesktop,wpf
description: Denna artikel introducerar hur man använder GridDesktop i en WPF applikation.
---

{{% alert color="primary" %}} 

Denna artikel visar hur man använder Windows Presentation Foundation (WPF) Designer for Visual Studio för att vara värd för en Windows Forms-kontroll som Aspose.Cells.GridDesktop i en WPF-applikation. 
Vi kommer att använda Visual Studio 2015 för att demonstrera processen, men du kan använda vilken version som helst inklusive Visual Studio 2008 eller senare.

{{% /alert %}} 

Denna handledning kommer att visa dig processen för att lägga till Aspose.Cells.GridDesktop-kontroll i en WPF-applikation. Du behöver en version av Visual Studio IDE som stöder WPF-utveckling för att prova detta på din sida.
## **Skapa en WPF-applikation med Visual Studio**
Skapa först en WPF-applikation med Visual Studio IDE. Klicka på **Fil** >> **Ny** >> **Projekt** -menyn och välj **WPF-applikation** från mallarna, namnge projektet och klicka på **OK**. Du kan rikta din projekt till vilken .NET Framework som helst högre än 2.0, men du kan inte använda klientprofil .NET Frameworks.
## **Lägg till referenser till nödvändiga namnrymder**
Lägg till referenser till följande assemblys genom att högerklicka på Referenser från Lösningens Utforskare-fönstret och välj Lägg till referensmenyn.

- WindowsFormsIntegration assembly (WindowsFormsIntegration.dll).
- Windows Forms assembly (System.Windows.Forms.dll).
- Aspose.Cells.GridDesktop assembly (Aspose.Cells.GridDesktop.dll).

Denna åtgärd lägger till de nödvändiga assemblys i applikationen, dvs kopierar assemblys till Bin-mappen för applikationen.
## **Lägg till referenser till XAML**
Gå sedan till XAML-filen och lägg till följande namnrymder och assemblyreferenser inom Windows-taggen.

{{< highlight java >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**Den slutgiltiga Windows-taggen kommer att se ut som följer.**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Lägg till Aspose.Cells.GridDesktop-kontroll i XAML**
Lägg helt enkelt till koden nedan inuti Grid-taggen i XAML. **WindowsFormsHost**-taggen används för att vara värd för Windows Forms-kontrollen och **gridDesktop:GridDesktop**-taggen representerar Aspose.Cells.GridDesktop-kontrollen. Du kan också namnge kontrollen så att den kan refereras enkelt i koden.

{{< highlight java >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**Den slutgiltiga XAML kommer att se ut som följer.** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Använda Aspose.Cells.GridDesktop**
Nu kan vi komma åt och använda Aspose.Cells.GridDesktop-kontrollen i .cs-filen som vilken annan Windows Forms-applikation som helst. För att hålla demonstrationen enkel laddar vi bara en exempelkalkylblad i Aspose.Cells.GridDesktop-kontrollen och sparar tillbaka den. Dessutom har vi använt FrameworkElement_OnLoaded-händelsen för att utlösa följande uttalanden.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Bygg & Kör**
Bygg och kör nu applikationen med ** F5** eller ** Start** -knappen på Visual Studio UI.
