---
title: Elimina intervalli nominati con Golang tramite C++
linktitle: Eliminare i Nomi Definiti
type: docs
weight: 90
url: /it/go-cpp/delete-named-ranges/
description: Impara come rimuovere nomi definiti o intervalli nominati dai file Excel o OpenOffice usando Aspose.Cells for C++.
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

## **Elimina intervallo nominato usando Aspose.Cells for C++**
Con Aspose.Cells for C++, puoi rimuovere intervalli nominati o nomi definiti tramite [testo](https://reference.aspose.com/cells/go-cpp/namecollection/remove_stringarray/) o [indice](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) dalla lista.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges.go" >}}
Nota: se il nome definito è referenziato da formule, non può essere rimosso. Possiamo rimuovere solo la formula del nome definito.

## **Rimuove alcuni intervalli nominati**
Quando rimuoviamo un nome definito, dobbiamo verificare se è referenziato da tutte le formule nel file.
Per migliorare le performance nella rimozione degli intervalli nominati, possiamo rimuoverne alcuni insieme.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-1.go" >}}
## **Rimuovere Nomi Definiti Duplicati**
Alcuni file Excel si corrompono perché alcuni nomi definiti sono duplicati. Quindi possiamo rimuovere questi nomi duplicati per riparare il file.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-2.go" >}}
