---
title: Utilizzo di Aspose.Cells.GridDesktop in un applicazione WPF
type: docs
weight: 50
url: /it/net/aspose-cells-griddesktop/use-aspose-cells-griddesktop-in-wpf-application/
keywords: GridDesktop,wpf
description: Questo articolo illustra come utilizzare GridDesktop in un applicazione WPF.
---

{{% alert color="primary" %}} 

Questo articolo dimostra come utilizzare il Windows Presentation Foundation (WPF) Designer per Visual Studio per ospitare un controllo di Windows Forms come Aspose.Cells.GridDesktop in un'applicazione WPF. 
Utilizzeremo Visual Studio 2015 per mostrare il processo, tuttavia, è possibile utilizzare qualsiasi versione, inclusa Visual Studio 2008 o successiva.

{{% /alert %}} 

Questo tutorial ti guiderà attraverso il processo di aggiunta del controllo Aspose.Cells.GridDesktop a un'applicazione WPF. È necessaria una qualsiasi versione dell'IDE Visual Studio che supporti lo sviluppo WPF per provare questa procedura sul tuo sistema.
## **Crea un'applicazione WPF utilizzando Visual Studio**
Prima crea un'applicazione WPF utilizzando l'IDE Visual Studio. Fai clic su **File** >> **Nuovo** >> **Progetto** e seleziona **Applicazione WPF** da Modelli, quindi nomina il progetto e fai clic su **OK**. Puoi indirizzare il tuo progetto a qualsiasi Framework .NET superiore a 2.0, tuttavia non puoi utilizzare i profili dei client di Framework .NET.
## **Aggiungi riferimenti ai namespace richiesti**
Aggiungi i riferimenti alle seguenti assembly facendo clic con il pulsante destro del mouse su Riferimenti dalla finestra Esplora soluzioni e seleziona Aggiungi riferimento.

- Assembly WindowsFormsIntegration (WindowsFormsIntegration.dll).
- Assembly Windows Forms (System.Windows.Forms.dll).
- Assembly Aspose.Cells.GridDesktop (Aspose.Cells.GridDesktop.dll).

Questa azione aggiunge le assembly richieste all'applicazione, ovvero; copia le assembly nella cartella Bin dell'applicazione.
## **Aggiungi riferimenti a XAML**
Successivamente, vai al file XAML e aggiungi i seguenti namespace e riferimenti alle assembly all'interno del tag Windows.

{{< highlight java >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**Il tag finale di Windows avrà un'aspetto simile a quanto mostrato di seguito.**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Aggiungi il controllo Aspose.Cells.GridDesktop a XAML**
Semplicemente aggiungi il codice sottostante all'interno del tag Grid in XAML. Il tag **WindowsFormsHost** viene utilizzato per ospitare il controllo Windows Forms e il tag **gridDesktop: GridDesktop** rappresenta il controllo Aspose.Cells.GridDesktop. Puoi anche dare un nome al controllo in modo che possa essere facilmente referenziato nel codice.

{{< highlight java >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**Il XAML finale avrà questo aspetto.** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Usa Aspose.Cells.GridDesktop**
Ora possiamo accedere e usare il controllo Aspose.Cells.GridDesktop nel file .cs come qualsiasi altra applicazione Windows Forms. Per mantenere la demo semplice, stiamo solo caricando un foglio di calcolo di esempio nel controllo Aspose.Cells.GridDesktop e salvandolo nuovamente. Inoltre, abbiamo utilizzato l'evento FrameworkElement_OnLoaded per attivare le seguenti istruzioni.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Compila ed Esegui**
Ora, crea ed esegui l'applicazione utilizzando il pulsante **F5** o **Start** nell'interfaccia utente di Visual Studio.
