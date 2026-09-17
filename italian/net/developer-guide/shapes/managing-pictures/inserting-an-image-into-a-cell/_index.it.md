---
title: Inserimento di un'immagine in una cella
linktitle: Inserimento di un'immagine in una cella
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo. Questo articolo spiega come adattare un'immagine esattamente a una singola cella, sia posizionando un'immagine mobile sopra la cella sia incorporando l'immagine direttamente nella cella.
keywords: Aspose.Cells, libreria .NET, foglio di calcolo, inserisci immagine, incorpora immagine, immagine nella cella, adatta immagine alla cella, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /it/net/inserting-an-image-into-a-cell/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre due modi distinti per associare un'immagine a una singola cella. Un'immagine mobile è una forma sul livello di disegno del foglio di lavoro che si sovrappone visivamente a un intervallo di celle, mentre un'immagine incorporata è memorizzata all'interno della cella stessa e si ridimensiona automaticamente all'area di visualizzazione della cella. Scegli l'approccio che meglio soddisfa le tue esigenze di layout.

## **Introduzione**
Adattare un'immagine esattamente a una singola cella è un requisito comune quando si progettano fogli di calcolo che fungono da report visivi, cataloghi di prodotti, elenchi di dipendenti, dashboard o elenchi di inventario. Piuttosto che estendere un'immagine su molte celle o posizionarla in modo approssimativo su un foglio di lavoro, potresti volere un'immagine pulita e legata alla cella che rimane allineata con la cella che la contiene.
Aspose.Cells supporta questo scenario in due modi complementari:
- **Approccio 1 — Posizionare un'immagine mobile sopra una cella.** Aggiungi una `Picture` al foglio di lavoro, imposta il suo `Placement` su `MoveAndSize` e regola le sue celle di ancoraggio (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) in modo che l'immagine copra esattamente una cella.
- **Approccio 2 — Incorporare un'immagine direttamente in una cella.** Assegna i byte dell'immagine alla proprietà `EmbeddedImage` della cella. L'immagine si ridimensiona automaticamente per adattarsi all'area di visualizzazione della cella e viaggia insieme alla cella.
Il resto di questo articolo illustra entrambi gli approcci, spiega le API pertinenti e mostra come utilizzarle nel codice.

## **Approccio 1: Posizionare un'immagine sopra una cella**
Un'immagine mobile è un oggetto `Picture` che risiede sul livello di disegno del foglio di lavoro. Sebbene non faccia parte di nessuna singola cella, è ancorata a un intervallo di celle. Le celle di ancoraggio dell'immagine — i suoi angoli in alto a sinistra e in basso a destra — determinano la sua estensione visiva sul foglio di lavoro. Per impostazione predefinita, un'immagine appena aggiunta si estende su più celle.
Per fare in modo che un'immagine mobile copra **esattamente una cella**, devi:
1. Aggiungi l'immagine usando `Worksheet.Pictures.Add(int row, int column, Stream stream)`, che ancora la nuova immagine alla cella specificata.
2. Imposta le quattro proprietà di ancoraggio in modo che il rettangolo di delimitazione dell'immagine coincida con la cella di destinazione.
3. Imposta `Picture.Placement` su `PlacementType.MoveAndSize` in modo che l'immagine si sposti e si ridimensioni con la cella sottostante quando l'utente modifica la larghezza della colonna o l'altezza della riga.

### **Ancorare l'immagine a una singola cella**
L'ancoraggio dell'immagine è definito da quattro proprietà di indice a base zero:
- `Picture.UpperLeftRow` — l'indice di riga del bordo superiore dell'immagine.
- `Picture.UpperLeftColumn` — l'indice di colonna del bordo sinistro dell'immagine.
- `Picture.LowerRightRow` — l'indice di riga del bordo inferiore dell'immagine. Per fare in modo che il bordo inferiore dell'immagine si trovi alla base della riga `r`, imposta questo valore su `r + 1`.
- `Picture.LowerRightColumn` — l'indice di colonna del bordo destro dell'immagine. Per fare in modo che il bordo destro dell'immagine si trovi alla destra della colonna `c`, imposta questo valore su `c + 1`.

{{% alert color="primary" %}}
Gli indici di riga e colonna in Aspose.Cells sono **a base zero**. La cella C6 ha indice di riga 5 e indice di colonna 2. Gli errori di off-by-one sull'ancoraggio in basso a destra sono la causa più comune di immagini che sembrano sovrapporsi a una cella adiacente.

### **Controllo del comportamento di posizionamento**
`Picture.Placement` è un enum di tipo `PlacementType` che controlla come si comporta l'immagine quando l'utente ridimensiona la riga o la colonna sottostante. Il valore consigliato per un'immagine a cella singola è `PlacementType.MoveAndSize`, che fa sì che l'immagine si sposti e si ridimensioni insieme alla cella sottostante, preservando l'adattamento esatto.

### **Istruzioni passo per passo**
1. Crea un nuovo `Workbook` (o aprine uno esistente).
2. Accedi al `Worksheet` di destinazione da `workbook.Worksheets[0]`.
3. Apri il file immagine dal disco in un `FileStream` utilizzando un blocco `using` in modo che lo stream venga eliminato correttamente.
4. Chiama `worksheet.Pictures.Add(5, 2, stream)` per aggiungere un'immagine ancorata alla cella C6. Cattura il riferimento `Picture` restituito.
5. Imposta le quattro coordinate di ancoraggio in modo che l'immagine copra solo la cella C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Imposta `picture.Placement = PlacementType.MoveAndSize` per mantenere l'immagine allineata con C6 quando la colonna o la riga viene ridimensionata.
7. Facoltativamente aggiungi del testo di esempio alle celle circostanti per dimostrare che solo la cella C6 contiene l'immagine.
8. Salva la cartella di lavoro su disco come file `.xlsx`.
Il codice seguente dimostra l'approccio completo.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Drawing;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
using (FileStream fs = new FileStream("logo.png", FileMode.Open, FileAccess.Read))
{
    int picIndex = worksheet.Pictures.Add(5, 2, fs);
    Picture picture = worksheet.Pictures[picIndex];
    picture.UpperLeftRow = 5;
    picture.UpperLeftColumn = 2;
    picture.LowerRightRow = 6;
    picture.LowerRightColumn = 3;
    picture.Placement = PlacementType.MoveAndSize;
}
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Approccio 2: Incorporare un'immagine direttamente in una cella**
Aspose.Cells espone anche un meccanismo più semplice per le immagini legate alle celle: la proprietà `Cell.EmbeddedImage`. Assegnando i byte dell'immagine a questa proprietà, l'immagine viene collegata alla cella stessa, come se fosse contenuto inline.

### **Come funzionano le immagini incorporate**
- L'immagine viene memorizzata come parte del contenuto della cella piuttosto che come forma sul livello di disegno.
- L'immagine si ridimensiona automaticamente per adattarsi ai confini resi della cella. Non sono richieste coordinate di ancoraggio o impostazioni di posizionamento.
- La cella rimane una vera cella con un vero indirizzo che può essere referenziato da formule, ordinato come parte di una riga o utilizzato in altre operazioni a livello di cella.
Questo rende `Cell.EmbeddedImage` l'opzione più concisa quando il tuo obiettivo è semplicemente "un'immagine che vive all'interno di questa cella".

### **Istruzioni passo per passo**
1. Crea un nuovo `Workbook` (o aprine uno esistente).
2. Accedi al `Worksheet` di destinazione da `workbook.Worksheets[0]`.
3. Leggi il file immagine dal disco in un array `byte[]` (ad esempio, utilizzando `File.ReadAllBytes`).
4. Ottieni un riferimento alla cella di destinazione — tramite `worksheet.Cells["C6"]` o `worksheet.Cells[5, 2]`.
5. Assegna l'array di byte alla proprietà `EmbeddedImage` della cella.
6. Facoltativamente regola l'altezza della riga e la larghezza della colonna della riga e della colonna di destinazione per dare all'immagine incorporata un aspetto più prominente.
7. Salva la cartella di lavoro su disco come file `.xlsx`.
Il codice seguente dimostra l'approccio completo.

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Ottieni la cella di destinazione C6
var cell = worksheet.Cells["C6"];
// Leggi il file immagine in un array di byte
byte[] imageData = File.ReadAllBytes("logo.png");
// Incorpora l'immagine direttamente nella cella
cell.EmbeddedImage = imageData;
// Opzionalmente regola l'altezza della riga e la larghezza della colonna in modo che l'immagine incorporata sia più visibile
worksheet.Cells.SetColumnWidth(2, 30);   // Colonna C (indice 2)
worksheet.Cells.SetRowHeight(5, 100);     // Riga 6 (indice 5)
// Salva la cartella di lavoro risultante come file .xlsx
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Scegliere l'approccio giusto**
Entrambi gli approcci producono un'immagine che si adatta all'interno di una singola cella, ma differiscono nel modo in cui l'immagine viene memorizzata e nel suo comportamento:
- **Usa un'immagine mobile (Approccio 1) quando:**
  - Hai bisogno di un controllo più preciso sul posizionamento, sulla disposizione a strati o sull'allineamento con altri oggetti di disegno.
  - Vuoi che l'immagine si comporti come una forma che può essere selezionata, riordinata o raggruppata con altre forme.
  - Richiedi compatibilità legacy con codice che funziona già con `PictureCollection`.
  - Hai bisogno di calcolare dinamicamente le coordinate di ancoraggio in base al layout del foglio di lavoro.
- **Usa un'immagine incorporata (Approccio 2) quando:**
  - Vuoi l'inserimento più semplice possibile di un'immagine in una cella.
  - L'immagine deve viaggiare con la cella come qualsiasi altro contenuto della cella.
  - Non hai bisogno di manipolare l'immagine come una forma.
{{% /alert %}}

{{% /alert %}}

## Related Articles
- [Excel Camera in Aspose.Cells for .NET](/cells/it/net/excel-camera/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for .NET](/cells/it/net/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for .NET](/cells/it/net/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/it/net/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for .NET](/cells/it/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}