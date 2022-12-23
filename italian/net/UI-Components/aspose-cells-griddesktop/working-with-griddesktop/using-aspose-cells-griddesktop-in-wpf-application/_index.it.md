---
title: Utilizzo di Aspose.Cells.GridDesktop nell'applicazione WPF
type: docs
weight: 50
url: /it/net/using-aspose-cells-griddesktop-in-wpf-application/
---
{{% alert color="primary" %}} 

 Questo articolo illustra come usare la finestra di progettazione WPF (Windows Presentation Foundation) per Visual Studio per ospitare un controllo Forms Windows come Aspose.Cells.GridDesktop in un'applicazione WPF.
Useremo Visual Studio 2015 per dimostrare il processo, tuttavia, puoi utilizzare qualsiasi versione, incluso Visual Studio 2008 o successivo.

{{% /alert %}} 

Questa esercitazione ti guiderà attraverso il processo di aggiunta del controllo Aspose.Cells.GridDesktop a un'applicazione WPF. Hai bisogno di qualsiasi versione dell'IDE di Visual Studio che supporti lo sviluppo WPF per provare questo dalla tua parte.
## **Creare un'applicazione WPF usando Visual Studio**
 Creare innanzitutto un'applicazione WPF utilizzando l'IDE di Visual Studio. Clicca su**File** >> **Nuovo** >> **Progetto** menu e selezionare**Applicazione WPF** da Modelli, assegna un nome al progetto e fai clic**OK**. È possibile indirizzare il progetto a qualsiasi framework .NET superiore a 2.0, tuttavia non è possibile utilizzare i framework .NET del profilo client.
## **Aggiungi riferimenti agli spazi dei nomi richiesti**
Aggiungere i riferimenti ai seguenti assembly facendo clic con il pulsante destro del mouse sulla finestra Riferimenti da Esplora soluzioni e selezionare il menu Aggiungi riferimento.

- Assembly WindowsFormsIntegration (WindowsFormsIntegration.dll).
- Windows Assemblaggio moduli (System.Windows.Forms.dll).
- Aspose.Cells.GridDesktop assembly (Aspose.Cells.GridDesktop.dll).

Questa azione aggiunge gli assembly richiesti all'applicazione, ovvero; copia gli assembly nella cartella Bin dell'applicazione.
## **Aggiungi riferimenti a XAML**
Successivamente, vai al file XAML e aggiungi gli spazi dei nomi e i riferimenti all'assembly seguenti all'interno del tag Windows.

{{< highlight "java" >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**Il tag finale Windows avrà un aspetto simile a quello mostrato di seguito.**

![cose da fare:immagine_alt_testo](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Aggiungere il controllo Aspose.Cells.GridDesktop a XAML**
 Aggiungi semplicemente il codice seguente all'interno del tag Grid in XAML. Il**WindowsFormsHost** tag viene utilizzato per ospitare Windows Forms control e**gridDesktop:GridDesktop** tag rappresenta il controllo Aspose.Cells.GridDesktop. Puoi anche nominare il controllo in modo che possa essere facilmente referenziato nel codice.

{{< highlight "java" >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**Il codice XAML finale avrà il seguente aspetto.** 

![cose da fare:immagine_alt_testo](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Utilizzare Aspose.Cells.GridDesktop**
Ora possiamo accedere e utilizzare il controllo Aspose.Cells.GridDesktop nel file .cs come qualsiasi altra applicazione Forms Windows. Per semplificare la dimostrazione, stiamo solo caricando un foglio di calcolo di esempio nel controllo Aspose.Cells.GridDesktop e salvandolo nuovamente. Inoltre, abbiamo utilizzato l'evento FrameworkElement_OnLoaded per attivare le seguenti istruzioni.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Costruisci ed esegui**
 Ora, crea ed esegui l'applicazione utilizzando**F5** o**Inizio** pulsante nell'interfaccia utente di Visual Studio.
