---
title: Eliminare i Nomi Definiti
type: docs
weight: 90
url: /it/python-net/delete-named-ranges/
description: Puoi imparare come rimuovere nomi definiti o nomi definiti da file Excel o OpenOffice con Aspose.Cells per Python tramite .Net.
keywords: Python Excel Library, Python Rimuovere Nomi Definiti Duplicati, Python Eliminare Nomi Definiti Duplicati.
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
Con Aspose.Cells per .Net, puoi rimuovere intervalli denominati o nomi definiti tramite [testo](https://reference.aspose.com/cells/python-net/aspose.cells/namecollection/remove_a_name/#str) dalla lista.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# The path to the documents directory
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a new Workbook
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete a named range by text
worksheets.names.remove_a_name("NamedRange")


# Save the workbook to retain the changes
workbook.save(os.path.join(data_dir, "Book2.xlsx"))
```

Nota: se il nome definito è referenziato da formule, non può essere rimosso. Possiamo solo rimuovere la formula del nome definito.

## **Rimuove alcuni intervalli nominati**
Quando rimuoviamo un nome definito, dobbiamo verificare se è referenziato da tutte le formule nel file.
Per migliorare le prestazioni della rimozione di intervalli nominati, possiamo rimuoverne alcuni insieme.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete some defined names
worksheets.names.remove_names_by_array(["NamedRange1", "NamedRange2"])

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```


## **Rimuovere Nomi Definiti Duplicati**
Alcuni file di Excel si corrompono perché alcuni nomi definiti sono duplicati. Possiamo rimuovere questi nomi duplicati per riparare il file.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete duplicate defined names
worksheets.names.remove_duplicate_names()

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```
