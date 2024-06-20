---
title: Abilita Diverse Modalità GridWeb
type: docs
weight: 60
url: /it/net/aspose-cells-gridweb/enable-different-gridweb-modes/
keywords: GridWeb,EditMode,SessionMode
description: Questo articolo introduce come lavorare con EditMode e SessionMode in GridWeb.
---

{{% alert color="primary" %}} 

Questo articolo descrive le diverse modalità di Aspose.Cells.GridWeb. Queste modalità sono differenziate logicamente a causa delle loro diverse funzionalità e comportamenti. Abbiamo identificato diversi tipi di modalità:

- Modalità di modifica
- Modalità di visualizzazione
- Modalità Sessione
- Modalità Senza Sessione

Tutte queste modalità hanno le proprie caratteristiche. Gli sviluppatori possono lavorare con Aspose.Cells.GridWeb in qualsiasi modalità in base alle loro esigenze. Vedremo ciascuna modalità di seguito.

{{% /alert %}} 
## **Modalità di modifica**
Per impostazione predefinita, il controllo Aspose.Cells.GridWeb è in modalità di modifica. In modalità di modifica, è possibile modificare completamente il contenuto della griglia utilizzando tutte le funzionalità offerte dal controllo Aspose.Cells.GridWeb. Queste funzionalità includono:

- Salvataggio del contenuto della griglia nei file di Microsoft Excel.
- Invio dei dati a un server.
- Calcolo delle formule.
- Annullamento o eliminazione delle azioni precedenti.
- Gestione delle righe e delle colonne.
- Taglio, copia o incolla dei dati.
- Formattazione delle celle, ecc.

**Controllo GridWeb in modalità di modifica** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Gli sviluppatori possono anche passare alla modalità di modifica tramite programmazione impostando la proprietà EditMode del controllo GridWeb su true.

Nell'esempio sottostante viene mostrato come abilitare la modalità di modifica programmata.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

Ogni volta che un utente fa clic sul pulsante **Annulla**, riporta il GridWeb al suo stato precedente (lo stato prima dell'ultimo postback al server). Non cancella le azioni precedenti una per una.

{{% /alert %}} 
## **Modalità di visualizzazione**
Quando il controllo GridWeb è in modalità Visualizzazione, gli utenti non possono modificare o modificare i contenuti della griglia, il che significa che possono solo visualizzare i contenuti della griglia. Ecco perché questa modalità è chiamata modalità Visualizzazione. In modalità Visualizzazione, alcuni pulsanti (**Invia**, **Salva** e **Annulla**) sono nascosti e il menu che appare con il clic destro contiene solo l'opzione **Copia**.

**Controllo GridWeb in modalità di visualizzazione** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Se gli sviluppatori vogliono che i loro utenti visualizzino solo i dati, possono passare alla modalità Visualizzazione programmaticamente impostando la proprietà EditMode del controllo GridWeb su false.

Nell'esempio seguente viene mostrato come abilitare la modalità visualizzazione in modo programmato



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

Anche in modalità di visualizzazione, gli utenti possono modificare l'altezza e la larghezza delle righe e delle colonne.

{{% /alert %}} 
## **Modalità Sessione**
Il controllo Aspose.Cells.GridWeb mantiene i dati del foglio nella Sessione Utente del server web tra ogni richiesta di un utente web. Significa che il controllo GridWeb funziona sempre in modalità Sessione per impostazione predefinita. Tuttavia, se non stai lavorando in modalità Sessione, attivala impostando la proprietà SessionMode del controllo GridWeb su SessionMode.Session.

Nell'esempio seguente viene mostrato come abilitare la modalità sessione in modo programmato



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **Modalità Senza Sessione**
Abbiamo già discusso che l'approccio della modalità Sessione fornisce le migliori prestazioni utilizzando una sessione utente per caricare e memorizzare i dati del foglio. Tuttavia, consuma memoria del server. Quindi, se ci sono un gran numero di utenti contemporanei, potrebbero sorgere problemi di memoria. Per risparmiare memoria del server e supportare un gran numero di utenti contemporanei, considera la modalità Senza Sessione.

La modalità Senza Sessione può essere attivata impostando la proprietà SessionMode del controllo GridWeb su SessionMode.ViewState.

Nell'esempio seguente viene mostrato come abilitare la modalità Senza Sessione in modo programmato



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Quando la proprietà SessionMode del GridWeb è impostata su SessionMode.ViewState, la griglia memorizza i dati nello ViewState della pagina. Ciò significa che la pagina renderizzata è più grande e consuma più traffico di rete.

{{% /alert %}} {{% alert color="primary" %}} 

Se desideri utilizzare SQL Server o StateServer per memorizzare le sessioni, utilizza la modalità Sessione. Il controllo GridWeb supporta la serializzazione dei dati su SQL Server o StateServer.

Si prega di controllare l'articolo seguente per ulteriore aiuto.

- [Funzionamento di GridWeb quando la modalità di stato di sessione ASP.NET è SQL Server](/cells/it/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
