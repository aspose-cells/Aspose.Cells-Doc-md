---
title: Inserimento di un'immagine in una cella
description: Aspose.Cells è una libreria Java per lavorare con file di fogli di calcolo. Questo articolo spiega come adattare un'immagine esattamente alle dimensioni di una singola cella utilizzando due approcci diversi, posizionare un'immagine mobile sopra la cella o incorporare l'immagine direttamente nella cella.
keywords: Aspose.Cells, libreria Java, foglio di calcolo, inserisci immagine, incorpora immagine, immagine nella cella, adatta immagine alla cella, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /it/java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce due modi distinti per associare un'immagine a una singola cella. Un'immagine mobile è una forma sul livello di disegno del foglio di lavoro che si sovrappone visivamente a un intervallo di celle, mentre un'immagine incorporata è memorizzata all'interno della cella stessa e si ridimensiona automaticamente all'area di visualizzazione della cella. Scegli l'approccio che meglio soddisfa le tue esigenze di layout.

{{% /alert %}}

## **Introduzione**

Adattare un'immagine esattamente a una singola cella è un requisito comune quando si progettano fogli di calcolo che fungono da report visivi, cataloghi di prodotti, elenchi di dipendenti, dashboard o inventari. Invece di estendere un'immagine su molte celle o di posizionarla in modo approssimativo su un foglio di lavoro, potresti volere un'immagine pulita, legata alla cella, che rimanga allineata con la cella che la possiede.

Aspose.Cells supporta questo scenario in due modi complementari:

- **Approccio 1 — Posizionare un'immagine mobile sopra una cella.** Aggiungi un `Picture` al foglio di lavoro, imposta il suo `Placement` su `MOVE_AND_SIZE` e regola le sue celle di ancoraggio (`getUpperLeftRow`, `getUpperLeftColumn`, `getLowerRightRow`, `getLowerRightColumn`) in modo che l'immagine copra esattamente una cella.
- **Approccio 2 — Incorporare un'immagine direttamente in una cella.** Assegna i byte dell'immagine al setter `getEmbeddedImage()` della cella. L'immagine si ridimensiona automaticamente per adattarsi all'area di visualizzazione della cella e si sposta con essa.

Il resto di questo articolo illustra entrambi gli approcci, spiega le API rilevanti e mostra come utilizzarle nel codice.

## **Approccio 1: Posizionare un'immagine sopra una cella**

Un'immagine mobile è un oggetto `Picture` che risiede sul livello di disegno del foglio di lavoro. Sebbene non faccia parte di alcuna singola cella, è ancorata a un intervallo di celle. Le celle di ancoraggio dell'immagine — i suoi angoli superiore sinistro e inferiore destro — ne determinano l'estensione visiva sul foglio di lavoro. Per impostazione predefinita, un'immagine appena aggiunta si estende su più celle.

Per fare in modo che un'immagine mobile copra **esattamente una cella**, devi:

1. Aggiungere l'immagine usando `Worksheet.getPictures().add(int row, int column, InputStream stream)`, che ancora la nuova immagine alla cella specificata.
2. Impostare le quattro proprietà di ancoraggio in modo che il rettangolo di delimitazione dell'immagine coincida con la cella di destinazione.
3. Impostare `Picture.setPlacement()` su `PlacementType.MOVE_AND_SIZE` in modo che l'immagine si sposti e si ridimensioni con la cella sottostante quando l'utente modifica la larghezza della colonna o l'altezza della riga.

### **Ancoraggio dell'immagine a una singola cella**

L'ancoraggio dell'immagine è definito da quattro proprietà con indice a base zero:

- `Picture.getUpperLeftRow()` — l'indice di riga del bordo superiore dell'immagine.
- `Picture.getUpperLeftColumn()` — l'indice di colonna del bordo sinistro dell'immagine.
- `Picture.getLowerRightRow()` — l'indice di riga del bordo inferiore dell'immagine. Per fare in modo che il bordo inferiore dell'immagine si trovi alla fine della riga `r`, imposta questo valore su `r + 1`.
- `Picture.getLowerRightColumn()` — l'indice di colonna del bordo destro dell'immagine. Per fare in modo che il bordo destro dell'immagine si trovi alla fine della colonna `c`, imposta questo valore su `c + 1`.

Ad esempio, per adattare l'immagine esattamente alla cella **C6** (indice di riga `5`, indice di colonna `2`), imposta `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)` e `setLowerRightColumn(3)`.

{{% alert color="primary" %}}

Gli indici di riga e colonna in Aspose.Cells sono **a base zero**. La cella C6 ha indice di riga 5 e indice di colonna 2. Gli errori off-by-one sull'ancoraggio inferiore destro sono la causa più comune di immagini che sembrano sovrapporsi a una cella adiacente.

{{% /alert %}}

### **Controllo del comportamento di posizionamento**

`Picture.getPlacement()` restituisce un'enumerazione di tipo `PlacementType` che controlla come si comporta l'immagine quando l'utente ridimensiona la riga o la colonna sottostante. Il valore consigliato per un'immagine a cella singola è `PlacementType.MOVE_AND_SIZE`, che fa sì che l'immagine si sposti e si ridimensioni insieme alla cella sottostante, preservando l'adattamento esatto.

### **Istruzioni passo passo**

1. Crea un nuovo `Workbook` (o aprine uno esistente).
2. Accedi al `Worksheet` di destinazione da `workbook.getWorksheets().get(0)`.
3. Apri il file immagine dal disco in un `InputStream` (ad esempio un `FileInputStream`) usando un blocco try-with-resources in modo che lo stream venga chiuso correttamente.
4. Chiama `worksheet.getPictures().add(5, 2, stream)` per aggiungere un'immagine ancorata alla cella C6. Cattura il riferimento `Picture` restituito.
5. Imposta le quattro coordinate di ancoraggio in modo che l'immagine copra solo la cella C6: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Imposta `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` per mantenere l'immagine allineata con C6 quando la colonna o la riga viene ridimensionata.
7. Facoltativamente, aggiungi del testo di esempio alle celle circostanti per dimostrare che solo la cella C6 contiene l'immagine.
8. Salva la cartella di lavoro su disco come file `.xlsx`.

Il codice seguente dimostra l'approccio completo.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

try (FileInputStream fs = new FileInputStream("logo.png"))
{
    int picIndex = worksheet.getPictures().add(5, 2, fs);
    Picture picture = worksheet.getPictures().get(picIndex);
    picture.setUpperLeftRow(5);
    picture.setUpperLeftColumn(2);
    picture.setLowerRightRow(6);
    picture.setLowerRightColumn(3);
    picture.setPlacement(PlacementType.MOVE_AND_SIZE);
}

workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Approccio 2: Incorporare un'immagine direttamente in una cella**

Aspose.Cells espone anche un meccanismo più semplice per le immagini legate alle celle: il metodo `Cell.setEmbeddedImage(byte[])`. L'assegnazione dei byte dell'immagine a questa proprietà collega l'immagine alla cella stessa, come se fosse contenuto inline.

### **Come funzionano le immagini incorporate**

- L'immagine viene memorizzata come parte del contenuto della cella anziché come forma sul livello di disegno.
- L'immagine si ridimensiona automaticamente per adattarsi ai confini resi della cella. Non sono richieste coordinate di ancoraggio né impostazioni di posizionamento.
- La cella rimane una cella reale con un indirizzo reale che può essere referenziato da formule, ordinato come parte di una riga o utilizzato in altre operazioni a livello di cella.

Questo rende `setEmbeddedImage()` l'opzione più concisa quando il tuo obiettivo è semplicemente "un'immagine che vive all'interno di questa cella".

### **Istruzioni passo passo**

1. Crea un nuovo `Workbook` (o aprine uno esistente).
2. Accedi al `Worksheet` di destinazione da `workbook.getWorksheets().get(0)`.
3. Leggi il file immagine dal disco in un array `byte[]` (ad esempio, leggendo il file tramite `Files.readAllBytes()` da `java.nio.file`).
4. Ottieni un riferimento alla cella di destinazione — tramite `worksheet.getCells().get("C6")` o `worksheet.getCells().get(5, 2)`.
5. Assegna l'array di byte alla cella usando `cell.setEmbeddedImage(bytes)`.
6. Facoltativamente, regola l'altezza della riga e la larghezza della colonna della riga e della colonna di destinazione per dare all'immagine incorporata un aspetto più prominente.
7. Salva la cartella di lavoro su disco come file `.xlsx`.

Il codice seguente dimostra l'approccio completo.

```java
import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Ottieni la cella di destinazione C6
Cell cell = worksheet.getCells().get("C6");

// Leggi il file immagine in un array di byte
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));

// Incorpora l'immagine direttamente nella cella
cell.setEmbeddedImage(imageData);

// Facoltativamente, regola l'altezza della riga e la larghezza della colonna in modo che l'immagine incorporata sia più visibile
worksheet.getCells().setColumnWidth(2, 30);   // Colonna C (indice 2)
worksheet.getCells().setRowHeight(5, 100);     // Riga 6 (indice 5)

// Salva la cartella di lavoro risultante come file .xlsx
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Scegliere l'approccio giusto**

Entrambi gli approcci producono un'immagine che si adatta a una singola cella, ma differiscono nel modo in cui l'immagine viene memorizzata e nel suo comportamento:

- **Usa un'immagine mobile (Approccio 1) quando:**
  - Hai bisogno di un controllo più fine sul posizionamento, sulla stratificazione o sull'allineamento con altri oggetti di disegno.
  - Vuoi che l'immagine si comporti come una forma che può essere selezionata, riordinata o raggruppata con altre forme.
  - Richiedi la compatibilità con codice legacy che già funziona con `PictureCollection`.
  - Hai bisogno di calcolare dinamicamente le coordinate di ancoraggio in base al layout del foglio di lavoro.

- **Usa un'immagine incorporata (Approccio 2) quando:**
  - Vuoi il modo più semplice possibile per inserire un'immagine in una cella.
  - L'immagine deve spostarsi con la cella come qualsiasi altro contenuto della cella.
  - Non hai bisogno di manipolare l'immagine come una forma.

{{% alert color="primary" %}}

Entrambi gli approcci possono coesistere nella stessa cartella di lavoro. Puoi posizionare immagini mobili sopra un insieme di celle e incorporare immagini direttamente in altre celle, poiché i due meccanismi utilizzano diversi livelli di archiviazione nel file.

{{% /alert %}}



{{< app/cells/assistant language="java" >}}