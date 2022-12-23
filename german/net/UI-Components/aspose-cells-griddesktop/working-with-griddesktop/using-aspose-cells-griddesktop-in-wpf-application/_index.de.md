---
title: Verwenden von Aspose.Cells.GridDesktop in der WPF-Anwendung
type: docs
weight: 50
url: /de/net/using-aspose-cells-griddesktop-in-wpf-application/
---
{{% alert color="primary" %}} 

 In diesem Artikel wird veranschaulicht, wie Sie den Windows Presentation Foundation (WPF) Designer für Visual Studio verwenden, um ein Windows Forms-Steuerelement wie Aspose.Cells.GridDesktop in einer WPF-Anwendung zu hosten.
Wir werden Visual Studio 2015 verwenden, um den Prozess zu demonstrieren, Sie können jedoch jede Version verwenden, einschließlich Visual Studio 2008 oder höher.

{{% /alert %}} 

Dieses Tutorial führt Sie durch den Prozess des Hinzufügens des Aspose.Cells.GridDesktop-Steuerelements zu einer WPF-Anwendung. Sie benötigen eine beliebige Version der Visual Studio-IDE, die die WPF-Entwicklung unterstützt, um dies auf Ihrer Seite auszuprobieren.
## **Erstellen Sie eine WPF-Anwendung mit Visual Studio**
 Erstellen Sie zunächst eine WPF-Anwendung mit der Visual Studio-IDE. Klicke auf**Datei** >> **Neu** >> **Projekt** Menü und auswählen**WPF-Anwendung** aus Vorlagen, benennen Sie das Projekt und klicken Sie auf**OK**. Sie können Ihr Projekt auf jedes .NET-Framework höher als 2.0 ausrichten, Sie können jedoch keine Clientprofil-.NET-Frameworks verwenden.
## **Fügen Sie Referenzen zu erforderlichen Namespaces hinzu**
Fügen Sie die Verweise zu den folgenden Assemblys hinzu, indem Sie mit der rechten Maustaste auf das Fenster Verweise aus dem Projektmappen-Explorer klicken und das Menü Verweis hinzufügen auswählen.

- WindowsFormsIntegration-Assembly (WindowsFormsIntegration.dll).
- Windows Forms-Assembly (System.Windows.Forms.dll).
- Aspose.Cells.GridDesktop-Assembly (Aspose.Cells.GridDesktop.dll).

Diese Aktion fügt der Anwendung die erforderlichen Assemblys hinzu, d. kopiert die Assemblys in den Bin-Ordner der Anwendung.
## **Verweise auf XAML hinzufügen**
Wechseln Sie als Nächstes zur XAML-Datei und fügen Sie die folgenden Namespaces und Assemblyverweise innerhalb des Windows-Tags hinzu.

{{< highlight "java" >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**Das letzte Windows-Tag sieht ähnlich aus wie unten gezeigt.**

![todo: Bild_alt_Text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu XAML hinzu**
 Fügen Sie einfach den folgenden Code in das Grid-Tag in XAML ein. Das**WindowsFormsHost** -Tag wird zum Hosten von Windows Forms Control und verwendet**gridDesktop:GridDesktop** -Tag stellt das Aspose.Cells.GridDesktop-Steuerelement dar. Sie können das Steuerelement auch benennen, damit es im Code leicht referenziert werden kann.

{{< highlight "java" >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**Das endgültige XAML sieht wie folgt aus.** 

![todo: Bild_alt_Text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Verwenden Sie Aspose.Cells.GridDesktop**
Wir können jetzt auf das Aspose.Cells.GridDesktop-Steuerelement in der .cs-Datei wie auf alle anderen Windows Forms-Anwendungen zugreifen und es verwenden. Um die Demonstration einfach zu halten, laden wir einfach eine Beispieltabelle in das Aspose.Cells.GridDesktop-Steuerelement und speichern sie zurück. Darüber hinaus haben wir das FrameworkElement_OnLoaded-Ereignis verwendet, um die folgenden Anweisungen auszulösen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Bauen und ausführen**
 Erstellen Sie nun die Anwendung und führen Sie sie aus**F5** oder**Start** Schaltfläche auf der Benutzeroberfläche von Visual Studio.
