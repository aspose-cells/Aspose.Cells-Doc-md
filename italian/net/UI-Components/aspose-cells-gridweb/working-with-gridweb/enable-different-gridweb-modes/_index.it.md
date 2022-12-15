---
title: Abilita diverse modalità GridWeb
type: docs
weight: 60
url: /it/net/enable-different-gridweb-modes/
---
{{% alert color="primary" %}} 

Questo articolo descrive le diverse modalità di Aspose.Cells.GridWeb. Queste modalità sono logicamente differenziate a causa delle loro diverse caratteristiche e comportamenti. Abbiamo identificato diversi tipi di modalità:

- Modalità Modifica
- Modalità di visualizzazione
- Modalità Sessione
- Modalità senza sessione

Tutte queste modalità hanno le loro caratteristiche. Gli sviluppatori possono lavorare con Aspose.Cells.GridWeb in qualsiasi modalità in base alle loro esigenze. Vedremo ciascuna modalità di seguito.

{{% /alert %}} 
## **Modalità Modifica**
Per impostazione predefinita, il controllo Aspose.Cells.GridWeb è in modalità di modifica. In modalità Modifica è possibile modificare completamente o modificare il contenuto della griglia utilizzando tutte le funzionalità offerte dal controllo Aspose.Cells.GridWeb. Queste funzionalità includono:

- Salvataggio del contenuto della griglia in file di Microsoft Excel.
- Invio di dati a un server.
- Formule di calcolo.
- Annullamento o eliminazione di azioni precedenti.
- Gestione di righe e colonne.
- Tagliare, copiare o incollare dati.
- Formattazione delle celle ecc.

**Controllo GridWeb in modalità di modifica** 

![cose da fare:immagine_alt_testo](enable-different-gridweb-modes_1.png)

Gli sviluppatori possono anche passare alla modalità di modifica a livello di codice impostando la proprietà EditMode del controllo GridWeb su true.

L'esempio seguente mostra come abilitare la modalità di modifica a livello di codice.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

 Ogni volta che un utente fa clic sul**Annullare** pulsante, porta GridWeb al suo stato precedente (lo stato prima dell'ultimo postback al server). Non annulla le azioni precedenti una per una.

{{% /alert %}} 
## **Modalità di visualizzazione**
Quando il controllo GridWeb è in modalità di visualizzazione, gli utenti non possono modificare o modificare il contenuto della griglia, il che significa che gli utenti possono solo visualizzare il contenuto della griglia. Ecco perché questa modalità è chiamata modalità di visualizzazione. In modalità di visualizzazione, alcuni pulsanti (**Invia**, **Salva** e**Annullare** ) sono nascosti e il menu che appare facendo clic con il pulsante destro del mouse contiene solo i file**copia** opzione.

**Controllo GridWeb in modalità di visualizzazione** 

![cose da fare:immagine_alt_testo](enable-different-gridweb-modes_1.png)

Se gli sviluppatori desiderano che i propri utenti visualizzino solo i dati, possono passare alla modalità di visualizzazione a livello di codice impostando la proprietà EditMode del controllo GridWeb su false.

L'esempio seguente mostra come abilitare la modalità di visualizzazione a livello di codice



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

Anche in modalità di visualizzazione, gli utenti possono modificare l'altezza e la larghezza di righe e colonne.

{{% /alert %}} 
## **Modalità Sessione**
Il controllo Aspose.Cells.GridWeb conserva i dati del foglio nella sessione utente del server web tra ogni richiesta di un utente web. Significa che il controllo GridWeb funziona sempre in modalità Session per impostazione predefinita. Tuttavia, se non stai lavorando in modalità Session, attivala impostando la proprietà SessionMode del controllo GridWEb su SessionMode.Session.

L'esempio seguente mostra come abilitare la modalità sessione a livello di codice



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **Modalità senza sessione**
Abbiamo già discusso del fatto che l'approccio in modalità sessione fornisce le migliori prestazioni utilizzando una sessione utente per caricare e archiviare i dati del foglio. Tuttavia, consuma la memoria del server. Quindi, se c'è un gran numero di utenti simultanei, potrebbero sorgere problemi di memoria. Per risparmiare memoria del server e supportare un numero elevato di utenti simultanei, prendere in considerazione la modalità senza sessione.

La modalità senza sessione può essere attivata impostando la proprietà SessionMode del controllo GridWeb su SessionMode.ViewState.

L'esempio seguente mostra come abilitare la modalità senza sessione a livello di codice



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: quando la proprietà SessionMode di GridWeb è impostata su SessionMode.ViewState, la griglia memorizza i dati nel ViewState della pagina. Ciò significa che la pagina visualizzata è più grande e consuma più traffico di rete.

{{% /alert %}} {{% alert color="primary" %}} 

Se desideri utilizzare SQL Server o StateServer per tenere le sessioni, utilizza la modalità Session. Il controllo GridWeb supporta la serializzazione dei dati in SQL Server o StateServer.

Si prega di controllare il seguente articolo per ulteriore assistenza.

- [Funzionamento di GridWeb quando la modalità dello stato della sessione ASP.NET è SQL Server](/cells/it/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
