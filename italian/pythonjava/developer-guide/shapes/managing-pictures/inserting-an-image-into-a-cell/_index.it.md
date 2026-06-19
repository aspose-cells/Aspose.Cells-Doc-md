---
title: Inserimento di un'immagine in una cella
description: Aspose.Cells for Python via Java è una libreria per lavorare con file di fogli di calcolo. Questo articolo spiega come adattare esattamente un'immagine alle dimensioni di una singola cella utilizzando due approcci diversi: posizionare un'immagine mobile sopra la cella o incorporare l'immagine direttamente nella cella.
keywords: Aspose.Cells, libreria Python via Java, foglio di calcolo, inserire immagine, incorporare immagine, immagine nella cella, adattare immagine alla cella, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /it/python-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells offre due modi distinti per associare un'immagine a una singola cella. Un'immagine mobile è una forma sul livello di disegno del foglio di lavoro che si sovrappone visivamente a un intervallo di celle, mentre un'immagine incorporata è memorizzata all'interno della cella stessa e si ridimensiona automaticamente in base all'area di visualizzazione della cella. Scegliete l'approccio che meglio soddisfa i requisiti di layout.

{{% /alert %}}

## **Introduzione**

Adattare esattamente un'immagine a una singola cella è un requisito comune quando si progettano fogli di calcolo che fungono da report visivi, cataloghi di prodotti, elenchi di dipendenti, dashboard o elenchi di inventario. Invece di estendere un'immagine su molte celle o di posizionarla in modo approssimativo su un foglio di lavoro, potreste desiderare un'immagine pulita e legata alla cella che rimane allineata con la cella che la contiene.

Aspose.Cells supporta questo scenario in due modi complementari:

- **Approccio 1 — Posizionare un'immagine mobile sopra una cella.** Aggiungere una `Picture` al foglio di lavoro, impostare il suo `setPlacement` su `MOVE_AND_SIZE` e regolare le sue celle di ancoraggio (`setUpperLeftRow`, `setUpperLeftColumn`, `setLowerRightRow`, `setLowerRightColumn`) in modo che l'immagine copra esattamente una cella.
- **Approccio 2 — Incorporare un'immagine direttamente in una cella.** Assegnare i byte dell'immagine alla proprietà `setEmbeddedImage` della cella. L'immagine si ridimensiona automaticamente per adattarsi all'area di visualizzazione della cella e si sposta con la cella.

Il resto di questo articolo illustra entrambi gli approcci, spiega le API pertinenti e mostra come utilizzarle nel codice.

## **Approccio 1: Posizionare un'immagine sopra una cella**

Un'immagine mobile è un oggetto `Picture` che risiede sul livello di disegno del foglio di lavoro. Sebbene non faccia parte di nessuna singola cella, è ancorata a un intervallo di celle. Le celle di ancoraggio dell'immagine — i suoi angoli in alto a sinistra e in basso a destra — ne determinano l'estensione visiva sul foglio di lavoro. Per impostazione predefinita, un'immagine appena aggiunta si estende su più celle.

Per fare in modo che un'immagine mobile copra **esattamente una cella**, è necessario:

1. Aggiungere l'immagine utilizzando `Worksheet.getPictures().add(int row, int column, InputStream stream)`, che ancora la nuova immagine alla cella specificata.
2. Impostare le quattro proprietà di ancoraggio in modo che il rettangolo di delimitazione dell'immagine coincida con la cella di destinazione.
3. Impostare `Picture.setPlacement` su `PlacementType.MOVE_AND_SIZE` in modo che l'immagine si sposti e si ridimensioni con la cella sottostante quando l'utente modifica la larghezza della colonna o l'altezza della riga.

### **Ancoraggio dell'immagine a una singola cella**

L'ancoraggio dell'immagine è definito da quattro proprietà di indice a base zero:

- `setUpperLeftRow` — l'indice di riga del bordo superiore dell'immagine.
- `setUpperLeftColumn` — l'indice di colonna del bordo sinistro dell'immagine.
- `setLowerRightRow` — l'indice di riga del bordo inferiore dell'immagine. Per fare in modo che il bordo inferiore dell'immagine si trovi in fondo alla riga `r`, impostare questo valore su `r + 1`.
- `setLowerRightColumn` — l'indice di colonna del bordo destro dell'immagine. Per fare in modo che il bordo destro dell'immagine si trovi a destra della colonna `c`, impostare questo valore su `c + 1`.

Ad esempio, per adattare esattamente l'immagine nella cella **C6** (indice di riga `5`, indice di colonna `2`), impostare `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)` e `setLowerRightColumn(3)`.

{{% alert color="primary" %}}

Gli indici di riga e colonna in Aspose.Cells sono **a base zero**. La cella C6 ha indice di riga 5 e indice di colonna 2. Gli errori di una unità sull'ancoraggio in basso a destra sono la fonte più comune di immagini che sembrano sovrapporsi a una cella adiacente.

{{% /alert %}}

### **Controllo del comportamento di posizionamento**

`getPlacement` è un'enumerazione di tipo `PlacementType` che controlla come si comporta l'immagine quando l'utente ridimensiona la riga o la colonna sottostante. Il valore consigliato per un'immagine a cella singola è `PlacementType.MOVE_AND_SIZE`, che fa sì che l'immagine si sposti e si ridimensioni insieme alla cella sottostante, preservando l'adattamento esatto.

### **Istruzioni passo-passo**

1. Creare un nuovo `Workbook` (o aprirne uno esistente).
2. Accedere al `Worksheet` di destinazione da `workbook.getWorksheets().get(0)`.
3. Aprire il file immagine dal disco in un `InputStream` (tipicamente un `FileInputStream`) in modo che lo stream venga chiuso correttamente.
4. Chiamare `worksheet.getPictures().add(5, 2, stream)` per aggiungere un'immagine ancorata alla cella C6. Acquisire il riferimento `Picture` restituito.
5. Impostare le quattro coordinate di ancoraggio in modo che l'immagine copra solo la cella C6: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Impostare `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` per mantenere l'immagine allineata con C6 quando la colonna o la riga viene ridimensionata.
7. Facoltativamente, aggiungere testo di esempio alle celle circostanti per dimostrare che solo la cella C6 contiene l'immagine.
8. Salvare la cartella di lavoro su disco come file `.xlsx`.

Il seguente codice dimostra l'approccio completo.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat, PlacementType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

FileInputStream = jpype.JClass("java.io.FileInputStream")
fs = FileInputStream("logo.png")
try:
    picIndex = worksheet.getPictures().add(5, 2, fs)
    picture = worksheet.getPictures().get(picIndex)
    picture.setUpperLeftRow(5)
    picture.setUpperLeftColumn(2)
    picture.setLowerRightRow(6)
    picture.setLowerRightColumn(3)
    picture.setPlacement(PlacementType.MoveAndSize)
finally:
    fs.close()

workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **Approccio 2: Incorporare un'immagine direttamente in una cella**

Aspose.Cells espone anche un meccanismo più semplice per le immagini legate alle celle: la proprietà `Cell.setEmbeddedImage`. Assegnando i byte dell'immagine a questa proprietà, l'immagine viene collegata alla cella stessa, come se fosse contenuto in linea.

### **Come funzionano le immagini incorporate**

- L'immagine viene memorizzata come parte del contenuto della cella anziché come forma sul livello di disegno.
- L'immagine si ridimensiona automaticamente per adattarsi ai confini resi della cella. Non sono richieste coordinate di ancoraggio o impostazioni di posizionamento.
- La cella rimane una vera cella con un vero indirizzo che può essere referenziato da formule, ordinato come parte di una riga o utilizzato in altre operazioni a livello di cella.

Questo rende `Cell.setEmbeddedImage` l'opzione più concisa quando il vostro obiettivo è semplicemente "un'immagine che vive all'interno di questa cella".

### **Istruzioni passo-passo**

1. Creare un nuovo `Workbook` (o aprirne uno esistente).
2. Accedere al `Worksheet` di destinazione da `workbook.getWorksheets().get(0)`.
3. Leggere il file immagine dal disco in un array `byte[]` (ad esempio, utilizzando una chiamata `Files.readAllBytes` da `java.nio.file.Files`).
4. Ottenere un riferimento alla cella di destinazione — tramite `worksheet.getCells().get("C6")` oppure `worksheet.getCells().get(5, 2)`.
5. Assegnare l'array di byte alla proprietà `setEmbeddedImage` della cella.
6. Facoltativamente, regolare l'altezza della riga e la larghezza della colonna della riga e colonna di destinazione per dare all'immagine incorporata un aspetto più prominente.
7. Salvare la cartella di lavoro su disco come file `.xlsx`.

Il seguente codice dimostra l'approccio completo.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# codice portato qui
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Ottieni la cella di destinazione C6
cell = worksheet.getCells().get("C6")

# Leggi il file immagine in un array di byte
imageData = open("logo.png", "rb").read()

# Incorpora l'immagine direttamente nella cella
cell.setEmbeddedImage(imageData)

# Facoltativamente regola l'altezza della riga e la larghezza della colonna per rendere l'immagine incorporata più visibile
worksheet.getCells().setColumnWidth(2, 30)   # Colonna C (indice 2)
worksheet.getCells().setRowHeight(5, 100)    # Riga 6 (indice 5)

# Salva la cartella di lavoro risultante come file .xlsx
workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **Scegliere l'approccio giusto**

Entrambi gli approcci producono un'immagine che si adatta a una singola cella, ma differiscono nel modo in cui l'immagine viene memorizzata e nel suo comportamento:

- **Utilizzare un'immagine mobile (Approccio 1) quando:**
  - È necessario un controllo più preciso sul posizionamento, sulla disposizione a strati o sull'allineamento con altri oggetti di disegno.
  - Si desidera che l'immagine si comporti come una forma che può essere selezionata, riordinata o raggruppata con altre forme.
  - È richiesta la compatibilità legacy con codice che già funziona con `PictureCollection`.
  - È necessario calcolare dinamicamente le coordinate di ancoraggio in base al layout del foglio di lavoro.

- **Utilizzare un'immagine incorporata (Approccio 2) quando:**
  - Si desidera l'inserimento più semplice possibile di un'immagine in una cella.
  - L'immagine deve viaggiare con la cella come qualsiasi altro contenuto della cella.
  - Non è necessario manipolare l'immagine come una forma.

{{% alert color="primary" %}}

Entrambi gli approcci possono coesistere nella stessa cartella di lavoro. È possibile posizionare immagini mobili sopra un insieme di celle e incorporare immagini direttamente in altre celle, poiché i due meccanismi utilizzano diversi livelli di archiviazione nel file.

{{% /alert %}}



{{< app/cells/assistant language="python" >}}