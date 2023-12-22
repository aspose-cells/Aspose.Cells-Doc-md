---
title: Elimina intervalli denominati
type: docs
weight: 90
url: /it/net/Delete-named-ranges/
description: Puoi imparare come rimuovere nomi definiti o intervalli denominati da file Excel o OpenOffice con Aspose.Cells per .Net .
---
##  **introduzione**
Se ci sono troppi nomi definiti o intervalli denominati nei file Excel, dobbiamo cancellarne alcuni perché non verranno più referenziati.

##  **Rimuovi l'intervallo denominato in MS Excel**

Per rimuovere un intervallo denominato da Excel, puoi seguire questi passaggi:
1. Apri Microsoft Excel e apri la cartella di lavoro che contiene l'intervallo denominato.
2. Vai alla scheda "Formule" nella barra multifunzione di Excel.
3. Fare clic nel gruppo "Nomi definiti" sul pulsante "Gestione nomi". Questo aprirà la finestra di dialogo Gestione nomi.
4. Nella finestra di dialogo Gestione nomi, selezionare l'intervallo denominato che si desidera rimuovere.
5. Fare clic sul pulsante "Elimina". Conferma l'eliminazione quando richiesto.
6. Fare clic sul pulsante "Chiudi" per chiudere la finestra di dialogo Gestione nomi.
7. Salvare la cartella di lavoro per mantenere le modifiche.


##  ** Elimina l'intervallo denominato utilizzando Aspose.Cells per .Net**
 Con Aspose.Cells per .Net, puoi rimuovere intervalli denominati o nomi definiti da[testo](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove) O[indice](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat) nella lista.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

Nota: se il nome definito è riferito da formule, non potrà essere rimosso. Possiamo solo rimuovere la formula del nome definito.

##  **Rimuove alcuni intervalli denominati**
Quando rimuoviamo un nome definito, dobbiamo verificare se è riferito a tutte le formule nel file.
Per migliorare le prestazioni di rimozione degli intervalli denominati, possiamo rimuoverne alcuni insieme.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

##  **Rimuovi nomi definiti duplicati**
Alcuni campi Excel sono corrotti perché alcuni nomi definiti sono duplicati. Quindi possiamo rimuovere questi nomi duplicati per riparare il file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



