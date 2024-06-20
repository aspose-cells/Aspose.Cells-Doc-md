---
title: Verwendung von Aspose.Cells.GridDesktop in WPF Anwendung
type: docs
weight: 50
url: /de/net/aspose-cells-griddesktop/use-aspose-cells-griddesktop-in-wpf-application/
keywords: GridDesktop,wpf
description: Dieser Artikel zeigt, wie GridDesktop in einer WPF Anwendung verwendet wird.
---

{{% alert color="primary" %}} 

Dieser Artikel zeigt, wie man den Windows Presentation Foundation (WPF) Designer für Visual Studio verwendet, um eine Windows Forms-Steuerung wie Aspose.Cells.GridDesktop in einer WPF-Anwendung zu hosten. 
Wir werden Visual Studio 2015 verwenden, um den Prozess zu demonstrieren, jedoch können Sie jede Version einschließlich Visual Studio 2008 oder später verwenden.

{{% /alert %}} 

Dieses Tutorial führt Sie durch den Prozess, die Aspose.Cells.GridDesktop-Steuerung zu einer WPF-Anwendung hinzuzufügen. Sie benötigen eine Version der Visual Studio-IDE, die die WPF-Entwicklung unterstützt, um dies auf Ihrer Seite auszuprobieren.
## **Erstellen Sie eine WPF-Anwendung mit Visual Studio**
Erstellen Sie zuerst eine WPF-Anwendung mit der Visual Studio-IDE. Klicken Sie auf **Datei** >> **Neu** >> **Projekt** und wählen Sie **WPF-Anwendung** aus den Vorlagen, benennen Sie das Projekt und klicken Sie auf **OK**. Sie können Ihr Projekt auf ein .NET Framework höher als 2.0 ausrichten, jedoch können Sie keine Clientprofil-.NET-Frameworks verwenden.
## **Fügen Sie Verweise auf erforderliche Namespaces hinzu**
Fügen Sie die Verweise auf die folgenden Assemblies hinzu, indem Sie mit der rechten Maustaste auf Verweise im Lösung-Explorerfenster klicken und im Menü Verweis hinzufügen auswählen.

- WindowsFormsIntegration Assembly (WindowsFormsIntegration.dll).
- Windows Forms-Assembly (System.Windows.Forms.dll).
- Aspose.Cells.GridDesktop-Assembly (Aspose.Cells.GridDesktop.dll).

Diese Aktion fügt die erforderlichen Assemblys der Anwendung hinzu; kopiert die Assemblys in den Bin-Ordner der Anwendung.
## **Fügen Sie Verweise auf XAML hinzu**
Gehen Sie als Nächstes zur XAML-Datei und fügen Sie die folgenden Namespaces und Assembly-Verweise innerhalb des Windows-Tags hinzu.

{{< highlight java >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**Der endgültige Windows-Tag wird ähnlich aussehen wie unten gezeigt.**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Fügen Sie Aspose.Cells.GridDesktop-Steuerung zu XAML hinzu**
Fügen Sie einfach den folgenden Code innerhalb des Grid-Tags in XAML hinzu. Der **WindowsFormsHost**-Tag wird verwendet, um Windows Forms-Steuerung zu hosten und der **gridDesktop:GridDesktop**-Tag repräsentiert die Aspose.Cells.GridDesktop-Steuerung. Sie können die Steuerung auch benennen, damit sie im Code leicht referenziert werden kann.

{{< highlight java >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**Das endgültige XAML wird wie folgt aussehen.** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Verwenden Sie Aspose.Cells.GridDesktop**
Wir können jetzt auf die Aspose.Cells.GridDesktop-Steuerung in der .cs-Datei wie in anderen Windows Forms-Anwendungen zugreifen und sie verwenden. Um die Demonstration einfach zu halten, laden wir lediglich eine Beispreadsheet in die Aspose.Cells.GridDesktop-Steuerung und speichern sie zurück. Darüber hinaus haben wir das FrameworkElement_OnLoaded-Ereignis verwendet, um die folgenden Anweisungen auszulösen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Build & Ausführen**
Jetzt bauen und starten Sie die Anwendung mit der Taste **F5** oder der **Start**-Schaltfläche in der Visual Studio UI.
