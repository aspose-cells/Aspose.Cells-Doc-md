---
title: Använder Aspose.Cells.GridDesktop i WPF Application
type: docs
weight: 50
url: /sv/net/using-aspose-cells-griddesktop-in-wpf-application/
---
{{% alert color="primary" %}} 

 Den här artikeln visar hur du använder WPF-designern (Windows Presentation Foundation) för Visual Studio för att vara värd för en Windows Forms-kontroll som Aspose.Cells.GridDesktop i en WPF-applikation.
Vi kommer att använda Visual Studio 2015 för att demonstrera processen, men du kan använda vilken version som helst inklusive Visual Studio 2008 eller senare.

{{% /alert %}} 

Denna handledning kommer att leda dig genom processen att lägga till Aspose.Cells.GridDesktop-kontroll till en WPF-applikation. Du behöver vilken version av Visual Studio IDE som helst som stöder WPF-utveckling för att prova detta på din sida.
## **Skapa en WPF-applikation med Visual Studio**
 Skapa först en WPF-applikation med Visual Studio IDE. Klicka på**Fil** >> **Ny** >> **Projekt** menyn och välj**WPF-applikation** från Mallar, namnge projektet och klicka**OK**. Du kan rikta ditt projekt till valfritt .NET Framework högre än 2.0, men du kan inte använda klientprofilen .NET Frameworks.
## **Lägg till referenser till obligatoriska namnutrymmen**
Lägg till referenserna till följande sammansättningar genom att högerklicka på fönstret References from Solution Explorer och välj Add Reference-menyn.

- WindowsFormsIntegration assembly (WindowsFormsIntegration.dll).
- Windows Forms assembly (System.Windows.Forms.dll).
- Aspose.Cells.GridDesktop assembly (Aspose.Cells.GridDesktop.dll).

Denna åtgärd lägger till de nödvändiga sammansättningarna till applikationen, det vill säga; kopierar sammansättningarna till mappen Bin i programmet.
## **Lägg till referenser till XAML**
Gå sedan till XAML-filen och lägg till följande namnområden och sammansättningsreferenser i Windows-taggen.

{{< highlight "java" >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**Den slutliga Windows-taggen kommer att se ut som visas nedan.**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Lägg till Aspose.Cells.GridDesktop-kontroll till XAML**
 Lägg bara till koden nedan i Grid-taggen i XAML. De**WindowsFormsHost** taggen används för att vara värd för Windows Forms-kontroll och**gridDesktop:GridDesktop** taggen representerar kontrollen Aspose.Cells.GridDesktop. Du kan också namnge kontrollen så att den lätt kan refereras i koden.

{{< highlight "java" >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**Den slutliga XAML kommer att se ut som följer.** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Använd Aspose.Cells.GridDesktop**
Vi kan nu komma åt och använda Aspose.Cells.GridDesktop-kontroll i .cs-filen som alla andra Windows Forms-program. För att hålla demonstrationen enkel laddar vi bara ett exempelark i kontrollen Aspose.Cells.GridDesktop och sparar tillbaka det. Dessutom har vi använt händelsen FrameworkElement_OnLoaded för att utlösa följande påståenden.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Bygg & Kör**
 Bygg och kör applikationen nu med hjälp av**F5** eller**Start** knappen i Visual Studio UI.
