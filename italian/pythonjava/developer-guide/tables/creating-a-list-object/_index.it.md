---
title: Creazione di un oggetto lista
type: docs
weight: 20
url: /it/python-java/creating-a-list-object/
---

L'uso dei fogli di lavoro rende facile lavorare con diversi tipi di elenchi, ad esempio elenchi telefonici, elenchi delle attività, ecc. Aspose.Cells supporta la creazione e la gestione degli elenchi.

## **Vantaggi di un oggetto elenco**

Ci sono diversi vantaggi quando si converte un elenco di dati in un vero oggetto lista:

- Nuove righe e colonne vengono automaticamente incluse.
- Una riga di totale in fondo al tuo elenco può essere facilmente aggiunta per visualizzare SOMMA, MEDIA, CONTEGGIO, ecc.
- Le colonne aggiunte a destra vengono automaticamente incorporate nell'oggetto Elenco.
- I grafici basati su righe e colonne verranno espansi automaticamente.
- I nomi definiti assegnati a righe e colonne verranno espansi automaticamente.
- L'elenco è protetto dalla cancellazione accidentale di righe e colonne.

## **Creazione di un oggetto elenco utilizzando Microsoft Excel**

**Selezione dell'intervallo di dati per la creazione di un oggetto lista** 

![todo:image_alt_text](picture1.png)

Questo visualizza il dialogo Crea elenco.

**Dialogo Crea elenco** 

![todo:image_alt_text](picture2.png)

Implementazione dell'oggetto Lista e specifica Riga totale (Seleziona **Dati**, quindi **Elenco**, seguito da **Riga totale**).

**Creazione di un oggetto Lista** 

![todo:image_alt_text](picture3.png)

## **Creazione di un oggetto Lista utilizzando l'API Aspose.Cells**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) che consente di accedere a ciascun foglio di calcolo in un file Excel.

Un foglio di calcolo è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione di un foglio di calcolo. Per creare un [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) in un foglio di calcolo, utilizzare la proprietà di raccolta di [**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects) della classe [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet). Ogni [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) è, infatti, un oggetto della classe [**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection), che fornisce ulteriormente il metodo [**add**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) per aggiungere un oggetto Lista e specificare un intervallo di celle per l'elenco.

In base all'intervallo specificato delle celle, l'oggetto Elenco viene creato nel foglio di calcolo da Aspose.Cells. Utilizzare gli attributi (ad esempio, Mostra totali, Colonnes dell'elenco, ecc.) della classe [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) per controllare l'elenco.

Nell'esempio riportato di seguito, abbiamo creato lo stesso [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) utilizzando Aspose.Cells per l'API Python via Java come abbiamo creato utilizzando Microsoft Excel nella sezione precedente.

## Codice Sorgente

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
