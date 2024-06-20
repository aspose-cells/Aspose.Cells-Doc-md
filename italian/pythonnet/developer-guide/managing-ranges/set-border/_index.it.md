---
title: Imposta il bordo dell intervallo
type: docs
weight: 600
url: /it/python-net/set-range-border/
description: Questo articolo mostra come impostare il bordo dell intervallo tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, imposta bordo intervallo Python, aggiungi bordo intervallo Python.
---

## **Possibili Scenari di Utilizzo**
Quando si desidera impostare il bordo per un intervallo, non è necessario impostare ogni cella individualmente. Puoi impostare il bordo sull'intervallo. Aspose.Cells per Python via .NET offre questa funzionalità.
Questo articolo fornisce un codice di esempio che utilizza Aspose.Cells per Python via .NET per impostare il bordo dell'intervallo.

## **Come Impostare il Bordo dell'Intervallo in Excel**
Per impostare il bordo di un intervallo in Excel, puoi seguire questi passaggi:
1. Seleziona l'intervallo di celle a cui desideri applicare il bordo.
2. Nella scheda "Home" del menu, individua il gruppo "Carattere".
3. All'interno del gruppo "Carattere", fai clic sul pulsante a discesa "Bordi".
<br>
<img src="border.png" />
4. Scegli il tipo di bordo che desideri applicare dalle opzioni nel menu a discesa. Puoi scegliere tra stili di bordi predefiniti o personalizzare il tuo bordo.
5. Una volta selezionato lo stile di bordo desiderato, il bordo sarà applicato all'intervallo selezionato di celle.

## **Come impostare il bordo di intervallo utilizzando Aspose.Cells per la libreria Excel di Python**
Questo esempio mostra come:

1. Crea un libro di lavoro.
1. Aggiungi dati alle celle nel primo foglio di lavoro.
1. Crea un [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).
1. Imposta il bordo interno del Range.
1. Imposta il bordo esterno del Range.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-set-border.py" >}}
