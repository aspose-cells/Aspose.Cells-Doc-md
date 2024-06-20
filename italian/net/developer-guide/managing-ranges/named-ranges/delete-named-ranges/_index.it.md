---
title: Eliminare i Nomi Definiti
type: docs
weight: 90
url: /it/net/Delete-named-ranges/
description: Puoi imparare come rimuovere nomi definiti o intervalli nominati da file Excel o OpenOffice con Aspose.Cells for .Net.
---

## **Introduzione**
Se ci sono troppi nomi definiti o intervalli nominati nei file Excel, dobbiamo eliminarne alcuni perché non vengono più referenziati.

## **Rimuovere Intervallo Nominato in MS Excel**

Per rimuovere un intervallo nominato da Excel, segui questi passaggi:
1. Apri Microsoft Excel e apri il libro di lavoro che contiene l'intervallo nominato.
2. Vai alla scheda "Formule" nella barra multifunzione di Excel.
3. Fai clic sul pulsante "Gestione nomi" nel gruppo "Nomi definiti". Si aprirà la finestra di dialogo Gestione nomi.
4. Nella finestra di dialogo Gestione nomi, seleziona l'intervallo nominato che desideri rimuovere.
5. Fai clic sul pulsante "Elimina". Conferma l'eliminazione quando richiesto.
6. Fai clic sul pulsante "Chiudi" per chiudere la finestra di dialogo Gestione nomi.
7. Salva il libro di lavoro per mantenere le modifiche.


## **Elimina l'intervallo nominato utilizzando Aspose.Cells for .Net**
Con Aspose.Cells for .Net, puoi rimuovere intervalli nominati o nomi definiti tramite [testo](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove) o [indice](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat) nella lista.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

Nota: se il nome definito è referenziato da formule, non può essere rimosso. Possiamo solo rimuovere la formula del nome definito.

## **Rimuove alcuni intervalli nominati**
Quando rimuoviamo un nome definito, dobbiamo verificare se è referenziato da tutte le formule nel file.
Per migliorare le prestazioni della rimozione di intervalli nominati, possiamo rimuoverne alcuni insieme.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

## **Rimuovere Nomi Definiti Duplicati**
Alcuni file di Excel si corrompono perché alcuni nomi definiti sono duplicati. Possiamo rimuovere questi nomi duplicati per riparare il file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



