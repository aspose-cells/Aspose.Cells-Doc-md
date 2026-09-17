---
title: Inserimento di un'immagine in una cella
linktitle: Inserimento di un'immagine in una cella
description: Aspose.Cells è una libreria Java per lavorare con file di fogli di calcolo. Questo articolo spiega come adattare un'immagine esattamente a una singola cella, sia posizionando un'immagine mobile sopra la cella sia incorporando l'immagine direttamente nella cella.
keywords: Aspose.Cells, libreria Java, foglio di calcolo, inserire immagine, incorporare immagine, immagine nella cella, adattare immagine alla cella, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /it/java/inserting-an-image-into-a-cell/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre due modalità distinte per associare un'immagine a una singola cella. Un'immagine mobile è una forma sul livello di disegno del foglio di lavoro che si sovrappone visivamente a un intervallo di celle, mentre un'immagine incorporata è memorizzata all'interno della cella stessa e si adatta automaticamente all'area di visualizzazione della cella. Scegli l'approccio che meglio soddisfa i requisiti del tuo layout.

## **Introduzione**
Adattare un'immagine esattamente a una singola cella è un requisito comune quando si progettano fogli di calcolo che fungono da report visivi, cataloghi prodotti, elenchi dipendenti, dashboard o liste di inventario. Piuttosto che allungare un'immagine su molte celle o posizionarla liberamente su un foglio di lavoro, potresti volere un'immagine pulita, legata alla cella, che rimane allineata alla cella che la contiene.
Aspose.Cells supporta questo scenario in due modi complementari:
- **Approccio 1 — Posizionare un'immagine mobile sopra una cella.** Aggiungere un `Picture` al foglio di lavoro, impostare il suo `Placement` su `MOVE_AND_SIZE` e regolare le sue celle di ancoraggio (`getUpperLeftRow`, `getUpperLeftColumn`, `getLowerRightRow`, `getLowerRightColumn`) in modo che l'immagine copra esattamente una cella.
- **Approccio 2 — Incorporare un'immagine direttamente in una cella.** Assegnare i byte dell'immagine al setter `getEmbeddedImage()` della cella. L'immagine si ridimensiona automaticamente per adattarsi all'area di visualizzazione della cella e viaggia con la cella.
Il resto di questo articolo illustra entrambi gli approcci, spiega le API pertinenti e mostra come utilizzarle nel codice.

## **Approccio 1: Posizionare un'immagine sopra una cella**
Un'immagine mobile è un oggetto `Picture` che risiede sul livello di disegno del foglio di lavoro. Sebbene non faccia parte di una singola cella, è ancorata a un intervallo di celle. Le celle di ancoraggio dell'immagine — i suoi angoli in alto a sinistra e in basso a destra — ne determinano l'estensione visiva sul foglio di lavoro. Per impostazione predefinita, un'immagine appena aggiunta si estende su più celle.
Per fare in modo che un'immagine mobile copra **esattamente una cella**, è necessario:
1. Aggiungere l'immagine utilizzando `Worksheet.getPictures().add(int row, int column, InputStream stream)`, che ancora la nuova immagine alla cella specificata.
2. Impostare le quattro proprietà di ancoraggio in modo che il rettangolo di delimitazione dell'immagine coincida con la cella di destinazione.
3. Impostare `Picture.setPlacement()` su `PlacementType.MOVE_AND_SIZE` in modo che l'immagine si sposti e si ridimensioni con la cella sottostante quando l'utente modifica la larghezza della colonna o l'altezza della riga.

### **Ancoraggio dell'immagine a una singola cella**
L'ancoraggio dell'immagine è definito da quattro proprietà di indice a base zero:
- `Picture.getUpperLeftRow()` — l'indice di riga del bordo superiore dell'immagine.
- `Picture.getUpperLeftColumn()` — l'indice di colonna del bordo sinistro dell'immagine.
- `Picture.getLowerRightRow()` — l'indice di riga del bordo inferiore dell'immagine. Per fare in modo che il bordo inferiore dell'immagine si trovi alla fine della riga `r`, impostare questo valore su `r + 1`.
- `Picture.getLowerRightColumn()` — l'indice di colonna del bordo destro dell'immagine. Per fare in modo che il bordo destro dell'immagine si trovi alla destra della colonna `c`, impostare questo valore su `c + 1`.

{{% alert color="primary" %}}
Gli indici di riga e colonna in Aspose.Cells sono **a base zero**. La cella C6 ha indice di riga 5 e indice di colonna 2. Gli errori di off-by-one sull'ancoraggio in basso a destra sono la causa più comune di immagini che sembrano sovrapporsi a una cella adiacente.

### **Controllo del comportamento di posizionamento**
`Picture.getPlacement()` restituisce un'enumerazione di tipo `PlacementType` che controlla il comportamento dell'immagine quando l'utente ridimensiona la riga o la colonna sottostante. Il valore consigliato per un'immagine a cella singola è `PlacementType.MOVE_AND_SIZE`, che fa sì che l'immagine si sposti e si ridimensioni insieme alla cella sottostante, preservando l'adattamento esatto.

### **Istruzioni passo per passo**
1. Creare un nuovo `Workbook` (o aprirne uno esistente).
2. Accedere al `Worksheet` di destinazione da `workbook.getWorksheets().get(0)`.
3. Aprire il file immagine dal disco in un `InputStream` (come un `FileInputStream`) utilizzando un blocco try-with-resources in modo che lo stream venga chiuso correttamente.
4. Chiamare `worksheet.getPictures().add(5, 2, stream)` per aggiungere un'immagine ancorata alla cella C6. Acquisire il riferimento `Picture` restituito.
5. Impostare le quattro coordinate di ancoraggio in modo che l'immagine copra solo la cella C6: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Impostare `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` per mantenere l'immagine allineata con C6 quando la colonna o la riga viene ridimensionata.
7. Facoltativamente, aggiungere testo di esempio alle cella circostanti per dimostrare che solo la cella C6 contiene l'immagine.
8. Salvare la cartella di lavoro su disco come file `.xlsx`.
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
- L'immagine è memorizzata come parte del contenuto della cella anziché come forma sul livello di disegno.
- L'immagine si ridimensiona automaticamente per adattarsi ai confini resi della cella. Non sono richieste coordinate di ancoraggio né impostazioni di posizionamento.
- La cella rimane una vera cella con un vero indirizzo che può essere referenziato dalle formule, ordinato come parte di una riga o utilizzato in altre operazioni a livello di cella.
Ciò rende `setEmbeddedImage()` l'opzione più concisa quando il tuo obiettivo è semplicemente "un'immagine che vive all'interno di questa cella".

### **Istruzioni passo per passo**
1. Creare un nuovo `Workbook` (o aprirne uno esistente).
2. Accedere al `Worksheet` di destinazione da `workbook.getWorksheets().get(0)`.
3. Leggere il file immagine dal disco in un array `byte[]` (ad esempio, leggendo il file tramite `Files.readAllBytes()` da `java.nio.file`).
4. Ottenere un riferimento alla cella di destinazione — tramite `worksheet.getCells().get("C6")` oppure `worksheet.getCells().get(5, 2)`.
5. Assegnare l'array di byte alla cella utilizzando `cell.setEmbeddedImage(bytes)`.
6. Facoltativamente, regolare l'altezza della riga e la larghezza della colonna di destinazione per dare all'immagine incorporata un aspetto più prominente.
7. Salvare la cartella di lavoro su disco come file `.xlsx`.
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
// Facoltativamente regola l'altezza della riga e la larghezza della colonna in modo che l'immagine incorporata sia più visibile
worksheet.getCells().setColumnWidth(2, 30);   // Colonna C (indice 2)
worksheet.getCells().setRowHeight(5, 100);     // Riga 6 (indice 5)
// Salva la cartella di lavoro risultante come file .xlsx
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Scegliere l'approccio giusto**
Entrambi gli approcci producono un'immagine che si adatta all'interno di una singola cella, ma differiscono nel modo in cui l'immagine viene memorizzata e nel suo comportamento:
- **Utilizzare un'immagine mobile (Approccio 1) quando:**
  - Hai bisogno di un controllo più fine sul posizionamento, la stratificazione o l'allineamento con altri oggetti di disegno.
  - Vuoi che l'immagine si comporti come una forma che può essere selezionata, riordinata o raggruppata con altre forme.
  - Richiedi compatibilità legacy con codice che già funziona con `PictureCollection`.
  - Hai bisogno di calcolare dinamicamente le coordinate di ancoraggio in base al layout del foglio di lavoro.
- **Utilizzare un'immagine incorporata (Approccio 2) quando:**
  - Vuoi l'inserimento più semplice possibile di un'immagine in una cella.
  - L'immagine deve viaggiare con la cella come qualsiasi altro contenuto della cella.
  - Non hai bisogno di manipolare l'immagine come una forma.
{{% /alert %}}

{{% /alert %}}

## Articoli correlati
- [Fotocamera di Excel in Aspose.Cells for Java](/cells/it/java/excel-camera/)
- [Aggiungere campi filtro a una Tabella Pivot in Aspose.Cells for Java](/cells/it/java/add-page-field-in-pivot-table/)
- [Applicare stili alle Tabelle Pivot in Aspose.Cells for Java](/cells/it/java/apply-style-to-pivot-table/)
- [Modificare il layout dei campi pagina nella Tabella Pivot](/cells/it/java/change-page-field-layout/)
- [Convertire Sparkline in immagine e HTML in Aspose.Cells for Java](/cells/it/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}