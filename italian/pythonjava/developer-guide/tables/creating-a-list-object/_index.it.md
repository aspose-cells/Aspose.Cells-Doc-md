---
title: Creazione di un oggetto elenco
type: docs
weight: 20
url: /it/python-java/creating-a-list-object/
---
L'uso dei fogli di lavoro rende facile lavorare con diversi tipi di elenchi, ad esempio. elenchi telefonici, elenchi di attività. ecc. Aspose.Cells supporta la creazione e la gestione di elenchi.

## **Vantaggi di un oggetto elenco**

Ci sono alcuni vantaggi quando si converte un elenco di dati in un vero oggetto elenco:

- Nuove righe e colonne vengono incluse automaticamente.
- È possibile aggiungere facilmente una riga totale in fondo all'elenco per visualizzare SUM, AVERAGE, COUNT, ecc.
- Le colonne aggiunte a destra vengono incorporate automaticamente nell'oggetto List.
- I grafici basati su righe e colonne verranno espansi automaticamente.
- Gli intervalli denominati assegnati a righe e colonne verranno espansi automaticamente.
- L'elenco è protetto dall'eliminazione accidentale di righe e colonne.

## **Creazione di un oggetto elenco utilizzando Microsoft Excel**

**Selezione dell'intervallo di dati per la creazione di un oggetto elenco** 

![cose da fare:immagine_alt_testo](picture1.png)

Viene visualizzata la finestra di dialogo Crea elenco.

**Finestra di dialogo Crea elenco** 

![cose da fare:immagine_alt_testo](picture2.png)

Implementando l'oggetto List e specificando Total Row (Select**Dati**, poi**Elenco**, seguito da**Riga totale**).

**Creazione di un oggetto Elenco** 

![cose da fare:immagine_alt_testo](picture3.png)

## **Creazione di un oggetto elenco utilizzando Aspose.Cells API**

Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)fornisce un'ampia gamma di proprietà e metodi per la gestione di un foglio di lavoro. Per creare un[**ElencoOggetto**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)in un foglio di lavoro, usa[**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)proprietà della collezione del[**Foglio di lavoro**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)classe. A testa[**ElencoOggetto**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)è, infatti, un oggetto del[**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)classe, che fornisce inoltre il[**Inserisci**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) per aggiungere un oggetto List e specificare un intervallo di celle per l'elenco.

In base all'intervallo di celle specificato, l'oggetto List viene creato nel foglio di lavoro da Aspose.Cells. Utilizzare gli attributi (ad esempio, ShowTotals, ListColumns e così via) del[**ElencoOggetto**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)class per controllare l'elenco.

Nell'esempio fornito di seguito, abbiamo creato lo stesso[**ElencoOggetto**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)utilizzando Aspose.Cells per Python tramite Java API come abbiamo creato utilizzando Microsoft Excel nella sezione precedente.

## Codice sorgente

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
