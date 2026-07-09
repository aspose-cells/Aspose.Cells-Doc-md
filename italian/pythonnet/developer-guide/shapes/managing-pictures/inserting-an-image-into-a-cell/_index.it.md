---
title: Inserimento di un'immagine in una cella
description: Aspose.Cells è una libreria Python per lavorare con file di fogli di calcolo. Questo articolo spiega come adattare un'immagine esattamente alle dimensioni di una singola cella utilizzando due approcci diversi, posizionare un'immagine mobile sopra la cella, oppure incorporare l'immagine direttamente nella cella.
keywords: Aspose.Cells, libreria Python, foglio di calcolo, inserire immagine, incorporare immagine, immagine nella cella, adattare immagine alla cella, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /it/python-net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells offre due modi distinti per associare un'immagine a una singola cella. Un'immagine mobile è una forma sul livello di disegno del foglio di lavoro che si sovrappone visivamente a un intervallo di celle, mentre un'immagine incorporata è memorizzata all'interno della cella stessa e si ridimensiona automaticamente all'area di visualizzazione della cella. Scegli l'approccio che meglio soddisfa le tue esigenze di layout.

{{% /alert %}}

## **Introduzione**

Adattare un'immagine esattamente a una singola cella è un requisito comune quando si progettano fogli di calcolo che fungono da report visivi, cataloghi di prodotti, rubriche dei dipendenti, dashboard o elenchi di inventario. Piuttosto che estendere un'immagine su molte celle o posizionarla liberamente su un foglio di lavoro, potresti volere un'immagine pulita e legata alla cella che rimanga allineata con la cella che la possiede.

Aspose.Cells supporta questo scenario in due modi complementari:

- **Approccio 1 — Posizionare un'immagine mobile sopra una cella.** Aggiungi una `Picture` al foglio di lavoro, imposta il suo `placement` su `MOVE_AND_SIZE` e regola le sue celle di ancoraggio (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) in modo che l'immagine copra esattamente una cella.
- **Approccio 2 — Incorporare un'immagine direttamente in una cella.** Assegna i byte dell'immagine alla proprietà `embedded_image` della cella. L'immagine si ridimensiona automaticamente per adattarsi all'area di visualizzazione della cella e si sposta con la cella.

Il resto di questo articolo illustra entrambi gli approcci, spiega le API pertinenti e mostra come utilizzarle nel codice.

## **Approccio 1: Posizionare un'immagine sopra una cella**

Un'immagine mobile è un oggetto `Picture` che risiede sul livello di disegno del foglio di lavoro. Sebbene non faccia parte di alcuna singola cella, è ancorata a un intervallo di celle. Le celle di ancoraggio dell'immagine — i suoi angoli in alto a sinistra e in basso a destra — determinano la sua estensione visiva sul foglio di lavoro. Per impostazione predefinita, un'immagine appena aggiunta si estende su più celle.

Per fare in modo che un'immagine mobile copra **esattamente una cella**, è necessario:

1. Aggiungere l'immagine utilizzando `Worksheet.pictures.add(row, column, stream)`, che ancora la nuova immagine alla cella specificata.
2. Impostare le quattro proprietà di ancoraggio in modo che il rettangolo di delimitazione dell'immagine coincida con la cella di destinazione.
3. Impostare `Picture.placement` su `PlacementType.MOVE_AND_SIZE` in modo che l'immagine si sposti e si ridimensioni con la cella sottostante quando l'utente modifica la larghezza della colonna o l'altezza della riga.

### **Ancoraggio dell'immagine a una singola cella**

L'ancoraggio dell'immagine è definito da quattro proprietà con indice a base zero:

- `Picture.upper_left_row` — l'indice di riga del bordo superiore dell'immagine.
- `Picture.upper_left_column` — l'indice di colonna del bordo sinistro dell'immagine.
- `Picture.lower_right_row` — l'indice di riga del bordo inferiore dell'immagine. Per fare in modo che il bordo inferiore dell'immagine si trovi alla fine della riga `r`, imposta questo valore su `r + 1`.
- `Picture.lower_right_column` — l'indice di colonna del bordo destro dell'immagine. Per fare in modo che il bordo destro dell'immagine si trovi alla destra della colonna `c`, imposta questo valore su `c + 1`.

Ad esempio, per adattare l'immagine esattamente alla cella **C6** (indice di riga `5`, indice di colonna `2`), imposta `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6` e `lower_right_column = 3`.

{{% alert color="primary" %}}

Gli indici di riga e colonna in Aspose.Cells sono **a base zero**. La cella C6 ha indice di riga 5 e indice di colonna 2. Gli errori di offset di uno sull'ancoraggio in basso a destra sono la causa più comune di immagini che sembrano sovrapporsi a una cella adiacente.

{{% /alert %}}

### **Controllo del comportamento di posizionamento**

`Picture.placement` è un'enumerazione di tipo `PlacementType` che controlla come si comporta l'immagine quando l'utente ridimensiona la riga o la colonna sottostante. Il valore consigliato per un'immagine a cella singola è `PlacementType.MOVE_AND_SIZE`, che fa sì che l'immagine si sposti e si ridimensioni insieme alla cella sottostante, preservando l'adattamento esatto.

### **Istruzioni passo per passo**

1. Crea un nuovo `Workbook` (o aprine uno esistente).
2. Accedi al `Worksheet` di destinazione da `workbook.worksheets[0]`.
3. Apri il file immagine dal disco in un flusso di file (o in un oggetto `BytesIO`) utilizzando un blocco `with` in modo che il flusso venga chiuso correttamente.
4. Chiama `worksheet.pictures.add(5, 2, stream)` per aggiungere un'immagine ancorata alla cella C6. Acquisisci il riferimento `Picture` restituito.
5. Imposta le quattro coordinate di ancoraggio in modo che l'immagine copra solo la cella C6: `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Imposta `picture.placement = PlacementType.MOVE_AND_SIZE` per mantenere l'immagine allineata con C6 quando la colonna o la riga viene ridimensionata.
7. Facoltativamente, aggiungi testo di esempio alle celle circostanti per dimostrare che solo la cella C6 contiene l'immagine.
8. Salva la cartella di lavoro su disco come file `.xlsx`.

Il codice seguente dimostra l'approccio completo.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

with open("logo.png", "rb") as fs:
    pic_index = worksheet.pictures.add(5, 2, fs)
    picture = worksheet.pictures[pic_index]
    picture.upper_left_row = 5
    picture.upper_left_column = 2
    picture.lower_right_row = 6
    picture.lower_right_column = 3
    picture.placement = ac.PlacementType.MOVE_AND_SIZE

workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Approccio 2: Incorporare un'immagine direttamente in una cella**

Aspose.Cells espone anche un meccanismo più semplice per le immagini legate alla cella: la proprietà `Cell.embedded_image`. Assegnare i byte dell'immagine a questa proprietà collega l'immagine alla cella stessa, come se fosse contenuto in linea.

### **Come funzionano le immagini incorporate**

- L'immagine viene memorizzata come parte del contenuto della cella anziché come forma sul livello di disegno.
- L'immagine si ridimensiona automaticamente per adattarsi ai confini resi della cella. Non sono richieste coordinate di ancoraggio o impostazioni di posizionamento.
- La cella rimane una vera cella con un vero indirizzo che può essere referenziato da formule, ordinato come parte di una riga o utilizzato in altre operazioni a livello di cella.

Questo rende `Cell.embedded_image` l'opzione più concisa quando il tuo obiettivo è semplicemente "un'immagine che vive all'interno di questa cella".

### **Istruzioni passo per passo**

1. Crea un nuovo `Workbook` (o aprine uno esistente).
2. Accedi al `Worksheet` di destinazione da `workbook.worksheets[0]`.
3. Leggi il file immagine dal disco in un oggetto `bytes` (ad esempio, aprendo il file in modalità binaria e chiamando `.read()`).
4. Ottieni un riferimento alla cella di destinazione — tramite `worksheet.cells["C6"]` o `worksheet.cells[5, 2]`.
5. Assegna l'oggetto bytes alla proprietà `embedded_image` della cella.
6. Facoltativamente, regola l'altezza della riga e la larghezza della colonna della riga e della colonna di destinazione per dare all'immagine incorporata un aspetto più prominente.
7. Salva la cartella di lavoro su disco come file `.xlsx`.

Il codice seguente dimostra l'approccio completo.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Ottieni la cella di destinazione C6
cell = worksheet.cells["C6"]

# Leggi il file immagine in un array di byte
with open("logo.png", "rb") as f:
    imageData = f.read()

# Incorpora l'immagine direttamente nella cella
cell.embedded_image = imageData

# Facoltativamente, regola l'altezza della riga e la larghezza della colonna per rendere più visibile l'immagine incorporata
worksheet.cells.set_column_width(2, 30)   # Colonna C (indice 2)
worksheet.cells.set_row_height(5, 100)     # Riga 6 (indice 5)

# Salva la cartella di lavoro risultante come file .xlsx
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Scegliere l'approccio giusto**

Entrambi gli approcci producono un'immagine che si adatta all'interno di una singola cella, ma differiscono nel modo in cui l'immagine viene memorizzata e nel suo comportamento:

- **Usa un'immagine mobile (Approccio 1) quando:**
  - Hai bisogno di un controllo più fine sul posizionamento, sulla stratificazione o sull'allineamento con altri oggetti di disegno.
  - Vuoi che l'immagine si comporti come una forma che può essere selezionata, riordinata o raggruppata con altre forme.
  - Richiedi compatibilità legacy con codice che già funziona con le raccolte `pictures`.
  - Hai bisogno di calcolare le coordinate di ancoraggio dinamicamente in base al layout del foglio di lavoro.

- **Usa un'immagine incorporata (Approccio 2) quando:**
  - Vuoi il modo più semplice possibile di inserire un'immagine in una cella.
  - L'immagine deve viaggiare con la cella come qualsiasi altro contenuto della cella.
  - Non hai bisogno di manipolare l'immagine come una forma.

{{% alert color="primary" %}}

Entrambi gli approcci possono coesistere nella stessa cartella di lavoro. Puoi posizionare immagini mobili sopra un insieme di celle e incorporare immagini direttamente in altre celle, poiché i due meccanismi utilizzano diversi livelli di archiviazione nel file.

{{% /alert %}}

## **Articoli correlati**

- [Come inserire un'immagine in una cella](/cells/it/python-net/how-to-place-image-to-cell/)
- [Aggiungere collegamenti ipertestuali alle immagini](/cells/it/python-net/add-image-hyperlinks/)
- [Caricare un'immagine Web da un URL in un foglio di lavoro Excel](/cells/it/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipolare posizione, dimensione e grafico della finestra di progettazione](/cells/it/python-net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="python" >}}