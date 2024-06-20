---
title: Formattazione di un Intervallo di Celle
type: docs
weight: 60
url: /it/net/aspose-cells-griddesktop/formatting-a-range-of-cells/
keywords: GridDesktop, formattazione, stile, celle
description: Questo articolo introduce come applicare lo stile di formattazione alle celle in GridDesktop.
---

{{% alert color="primary" %}} 

Questo argomento fa parte della serie di argomenti relativi all'applicazione delle impostazioni del carattere e altri stili di formattazione alle celle. I nostri ultimi argomenti hanno trattato ampiamente su come gestire tali funzionalità. Ad esempio, puoi fare riferimento ai [Cambiamenti del Carattere e Colori di una Cella](/cells/it/net/changing-the-font-and-color-of-a-cell/) e [Applicare Stili alle Celle](/cells/it/net/applying-styles-on-cells/) per apprendere le stesse funzionalità. Qual è la novità di questo argomento se abbiamo già trattato questi concetti. Beh, l'unica differenza di questo argomento rispetto ai precedenti è che applicheremo le impostazioni di formattazione (relative a caratteri e altri stili) a un intervallo di celle anziché solo a una singola cella. Speriamo che troverai comunque utile questo argomento.

{{% /alert %}} 
## **Impostazione del Carattere e dello Stile di un Intervallo di Celle**
Prima di parlare delle impostazioni di formattazione (di cui abbiamo già parlato molto nei nostri argomenti precedenti), dovremmo sapere come creare un intervallo di celle. Bene, possiamo creare un intervallo di celle utilizzando la classe **CellRange** il cui costruttore richiede alcuni parametri per specificare l'intervallo di celle. Possiamo specificare l'intervallo di celle utilizzando i **Nomi** o gli **Indici di Riga e Colonna** delle celle di inizio e fine.

Una volta creato un oggetto **CellRange** possiamo utilizzare le versioni sovraccaricate dei metodi **SetStyle**, **SetFont** e **SetFontColor** di Worksheet che possono prendere un oggetto **CellRange** per applicare le impostazioni di formattazione all'intervallo specificato di celle.

Diamo un'occhiata a un esempio per capire questo concetto di base.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
