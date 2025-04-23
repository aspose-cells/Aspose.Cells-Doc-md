---
title: Installare Aspose Cells tramite NuGet
type: docs
weight: 30
url: /it/net/installation/
---


## **Installare Aspose.Cells for .NET tramite NuGet**
NuGet è il modo più semplice per scaricare e installare le API di Aspose per .NET. Aprire Microsoft Visual Studio e il gestore dei pacchetti NuGet. Cercare "aspose" per trovare la API desiderata. Fare clic su "Installa", la API selezionata verrà scaricata e referenziata nel proprio progetto.

Nota: È possibile visitare la pagina web di nuget per aspose.cells per ulteriori informazioni: 
[Pacchetto NuGet Aspose.Cells for .NET](https://www.nuget.org/packages/Aspose.Cells/)

### **Installare Aspose.Cells utilizzando la GUI del Gestore pacchetti**
Seguire questi passaggi per referenziare il componente Aspose.Cells utilizzando la GUI del gestore dei pacchetti:

- Aprire la soluzione/progetto in Visual Studio.
- Fare clic su **Strumenti** -> **Gestione pacchetti libreria** -> **Gestione pacchetti NuGet** dalla soluzione. È anche possibile accedere facilmente alla stessa opzione tramite Esplora soluzioni. Fare clic con il pulsante destro del mouse sulla soluzione o sul progetto e selezionare **Gestione pacchetti NuGet** dal menu di contesto.
- Selezionare **Online** nel menu a sinistra e digitare "Aspose.Cells" nella casella di ricerca per trovare il pacchetto .NET di Aspose.Cells.
- Fare clic sul pulsante **Installa** accanto all'entrata Aspose.Cells for .NET per installare la versione più recente nel proprio progetto.
### **Installare Aspose.Cells utilizzando la Console del gestore pacchetti**
È possibile seguire i passaggi seguenti per referenziare il componente Aspose.Cells utilizzando la console del gestore pacchetti:

- Aprire la soluzione/progetto in Visual Studio.
- Selezionare **Strumenti** -> **Gestore pacchetti libreria** -> **Console del gestore pacchetti** dal menu per aprire la console del gestore pacchetti.
  - Digitare il comando "Install-Pacchetto Aspose.Cells" e premere invio per installare l'ultima versione completa nella propria applicazione. In alternativa è possibile aggiungere il suffisso "-prerelease" al comando per specificare che la versione più recente inclusi hotfix sia installata.
- Si vedrà che appare la dicitura "Download di Aspose.Cells..." in basso a sinistra della finestra, indicando che il download è in corso.
- Una volta scaricato, si vedranno i seguenti messaggi di conferma. Se non si conosce l'EULA di Aspose, è una buona idea leggere la licenza referenziata nell'URL.
- Ora si dovrebbe trovare che Aspose.Cells è stato aggiunto e referenziato con successo nell'applicazione.
## **Referenziare Aspose.Cells da un progetto .NET**
Per utilizzare Aspose.Cells in un'applicazione, aggiungere un riferimento ad esso. Per aggiungere un riferimento utilizzando Visual Studio:

1. Nel **Esplora soluzioni**, espandi il nodo del progetto a cui desideri aggiungere un riferimento.
1. Fai clic con il pulsante destro del mouse sul nodo **Riferimenti** del progetto e seleziona **Aggiungi riferimento** dal menu.
1. Nella finestra di dialogo **Aggiungi riferimento**, seleziona la scheda .NET (selezionata per impostazione predefinita). Se hai installato utilizzando l'installatore MSI, Aspose.Cells apparirà nel riquadro superiore.
1. Selezionalo e fai clic su **Seleziona**.

Se hai scaricato o decompresso solo il file DLL:

1. Trova il file Aspose.Cells.dll utilizzando il pulsante **Sfoglia**. Aspose.Cells dovrebbe apparire nel riquadro **Componenti selezionati** della finestra di dialogo.
1. Fai clic su **OK**. Il riferimento Aspose.Cells appare sotto il nodo **Riferimenti** del progetto.
### **Riferimento al componente da un progetto Client Profile VS.NET 2010**
Se il framework di destinazione del tuo progetto è .NET Framework 3.5/4 Client Profile, utilizza il file del componente Aspose.Cells.dll situato nella cartella net_ClientProfile della directory di installazione. Ad esempio:

- Nell'**Esplora soluzioni** di VS.NET 2010 per il tuo progetto, fai clic con il pulsante destro del mouse su **Riferimenti** e seleziona **Aggiungi riferimento**.
- Seleziona la scheda **Sfoglia** nella finestra di dialogo e fai clic su Cerca nel menu a discesa.
- Trova e seleziona il file del componente Aspose.Cells.dll nella directory di installazione, ad esempio: .../Program Files/Aspose/Aspose.Cells for .NET/Bin/net_ClientProfile/ **(Assicurati di aver installato il prodotto utilizzando l'installatore MSI sul tuo computer.)**
- Fai clic su **OK** per chiudere la finestra di dialogo

{{% alert color="primary" %}} 

Se il framework di destinazione del tuo progetto VS.NET 2010 è ".NET Framework 4" o altro, utilizza semplicemente il file del componente Aspose.Cells.dll situato nella cartella net4.0/net2.0.

{{% /alert %}} 
## **Riferimento ai controlli della griglia Aspose.Cells da un progetto .NET**
Per utilizzare un controllo della griglia nella tua applicazione, aggiungi un riferimento ad esso. Per referenziare un controllo della griglia in Visual Studio, procedi come segue:

- Nell'**Esplora soluzioni**, espandi il nodo del progetto a cui desideri aggiungere un riferimento.
- Fai clic con il pulsante destro del mouse sul nodo **Riferimenti** del progetto e seleziona **Aggiungi riferimento** dal menu.
- Nella finestra di dialogo **Aggiungi riferimento**, seleziona la scheda **.NET** (selezionata per impostazione predefinita). Se hai utilizzato l'installatore MSI per installare Aspose.Cells for .NET, Aspose.Cells.GridDesktop e Aspose.Cells.GridWeb appariranno nel riquadro superiore.
- Selezionali e fai clic su **Seleziona**.
- I riferimenti Aspose.Cells.GridDesktop e Aspose.Cells.GridWeb appaiono sotto il nodo Riferimenti del progetto.

Se hai scaricato e scompattato solo il file DLL:

- Trova i file Aspose.Cells.GridDesktop.dll e Aspose.Cells.GridWeb.dll utilizzando il pulsante Sfoglia. Aspose.Cells Grid Suite è stato referenziato e dovrebbe apparire nel riquadro **Componenti selezionati** della finestra di dialogo.
- Fare clic su **OK.**
## **Disinstallazione Aspose.Cells for .NET**
Se hai utilizzato l'installer MSI per distribuire Aspose.Cells for .NET, segui questi passaggi per rimuovere completamente il componente e i controlli, le demo associate e la documentazione:

- Dal menu **Start**, seleziona **Impostazioni**, seguito da **Pannello di controllo**.
- Fare clic su **Aggiungi/Rimuovi programmi**.
- Seleziona Aspose.Cells for .NET (versione).
- Fare clic su **Modifica/Rimuovi** per rimuovere Aspose.Cells.
{{< app/cells/assistant language="csharp" >}}
