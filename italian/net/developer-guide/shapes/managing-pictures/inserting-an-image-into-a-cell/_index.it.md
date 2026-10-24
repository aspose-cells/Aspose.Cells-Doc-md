---
title: Inserimento di un'immagine in una cella
linktitle: Inserimento di un'immagine in una cella
description: Aspose.Cells è una libreria .NET per lavorare con i file di fogli di calcolo. Questo articolo spiega come adattare esattamente un'immagine a una singola cella, sia collocando un'immagine fluttuante sopra la cella sia incorporandola direttamente nella cella.
keywords: Aspose.Cells, libreria .NET, foglio di calcolo, inserimento di immagine, incorporamento di immagine, immagine in una cella, adattamento dell'immagine alla cella, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /it/net/inserting-an-image-into-a-cell/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre due modi distinti per associare un'immagine a una singola cella. Un'immagine fluttuante è una forma sul livello di disegno del foglio di lavoro che si sovrappone visivamente a un intervallo di celle, mentre un'immagine incorporata viene memorizzata nella cella stessa e ridimensionata automaticamente per adattarsi all'area visualizzata della cella. Scegliere l'approccio che meglio soddisfa i requisiti di layout.
{{% /alert %}}

## **Introduzione**
L'adattamento esatto di un'immagine a una singola cella è un requisito comune quando si progettano fogli di calcolo che fungono da report visivi, cataloghi di prodotti, directory del personale, dashboard o elenchi di inventario. Invece di estendere un'immagine su più celle o di disporla liberamente su un foglio di lavoro, si potrebbe preferire un'immagine nitida e strettamente legata alla cella, che rimanga allineata alla cella contenitore.
Aspose.Cells supporta questo scenario in due modi complementari:
- **Approccio 1 — Collocare un'immagine fluttuante sopra una cella.** Aggiungere un `Picture` al foglio di lavoro, impostare `Placement` su `MoveAndSize` e regolare le celle di ancoraggio (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) in modo che l'immagine copra esattamente una cella.
- **Approccio 2 — Incorporare un'immagine direttamente in una cella.** Assegnare i byte dell'immagine alla proprietà `EmbeddedImage` della cella. L'immagine viene ridimensionata automaticamente per adattarsi all'area visualizzata della cella e si sposta con essa.
Il resto di questo articolo illustra entrambi gli approcci, spiega le API pertinenti e mostra come usarli nel codice.

## **Approccio 1: Collocare un'immagine fluttuante sopra una cella**
Un'immagine fluttuante è un oggetto `Picture` che risiede nel livello di disegno del foglio di lavoro. Sebbene non faccia parte di alcuna singola cella, è ancorata a un intervallo di celle. Le celle di ancoraggio dell'immagine, corrispondenti agli angoli superiore sinistro e inferiore destro, ne determinano l'estensione visiva sul foglio di lavoro. Per impostazione predefinita, un'immagine appena aggiunta si estende su più celle.
Per far coprire **esattamente una cella** a un'immagine fluttuante, è necessario:
1. Aggiungere l'immagine utilizzando `Worksheet.Pictures.Add(int row, int column, Stream stream)`, che ancora la nuova immagine alla cella indicata.
2. Impostare le quattro proprietà di ancoraggio in modo che il rettangolo delimitante dell'immagine coincida con la cella di destinazione.
3. Impostare `Picture.Placement` su `PlacementType.MoveAndSize`, in modo che l'immagine si sposti e venga ridimensionata con la cella sottostante quando l'utente modifica la larghezza della colonna o l'altezza della riga.

### **Ancoraggio dell'immagine a una singola cella**
L'ancoraggio dell'immagine è definito da quattro proprietà che restituiscono indici a base zero:
- `Picture.UpperLeftRow` — l'indice di riga del bordo superiore dell'immagine.
- `Picture.UpperLeftColumn` — l'indice di colonna del bordo sinistro dell'immagine.
- `Picture.LowerRightRow` — l'indice di riga del bordo inferiore dell'immagine. Per fare in modo che il bordo inferiore dell'immagine sia allineato al bordo inferiore della riga `r`, impostare questo valore su `r + 1`.
- `Picture.LowerRightColumn` — l'indice di colonna del bordo destro dell'immagine. Per fare in modo che il bordo destro dell'immagine sia allineato al bordo destro della colonna `c`, impostare questo valore su `c + 1`.

{{% alert color="primary" %}}
Gli indici di riga e colonna in Aspose.Cells sono **a base zero**. La cella C6 ha indice di riga 5 e indice di colonna 2. Gli errori di scostamento di un'unità nell'ancoraggio dell'angolo inferiore destro sono la causa più comune di immagini che sembrano sovrapporsi alla cella adiacente.
{{% /alert %}}

### **Controllo del comportamento di posizionamento**
`Picture.Placement` è una proprietà di tipo enumerazione `PlacementType` che controlla il comportamento dell'immagine quando l'utente ridimensiona la riga o la colonna sottostanti. Il valore consigliato per un'immagine contenuta in una singola cella è `PlacementType.MoveAndSize`, che fa sì che l'immagine si sposti e venga ridimensionata insieme alla cella sottostante, preservandone l'adattamento esatto.

### **Istruzioni dettagliate**
1. Creare un nuovo `Workbook` (o aprirne uno esistente).
2. Accedere al `Worksheet` di destinazione tramite `workbook.Worksheets[0]`.
3. Aprire il file di immagine dal disco in un `FileStream` utilizzando un blocco `using`, in modo che lo stream venga correttamente rilasciato.
4. Chiamare `worksheet.Pictures.Add(5, 2, stream)` per aggiungere un'immagine ancorata alla cella C6. Memorizzare il riferimento `Picture` restituito.
5. Impostare le quattro coordinate di ancoraggio in modo che l'immagine copra solo la cella C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Impostare `picture.Placement = PlacementType.MoveAndSize` per mantenere l'immagine allineata a C6 quando vengono ridimensionate la colonna o la riga.
7. Se desiderato, aggiungere testo di esempio alle celle circostanti per dimostrare che l'immagine copre solo la cella C6.
8. Salvare la cartella di lavoro su disco come file `.xlsx`.
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
Aspose.Cells espone anche un meccanismo più semplice per le immagini associate alle celle: la proprietà `Cell.EmbeddedImage`. L'assegnazione dei byte dell'immagine a questa proprietà associa l'immagine alla cella stessa, come se fosse un contenuto in linea.

### **Come funzionano le immagini incorporate**
- L'immagine viene memorizzata come parte del contenuto della cella anziché come forma sul livello di disegno.
- L'immagine viene ridimensionata automaticamente per adattarsi all'interno dell'area visualizzata della cella. Non sono necessarie coordinate di ancoraggio né impostazioni di posizionamento.
- La cella rimane una cella a tutti gli effetti: mantiene un indirizzo valido, può essere referenziata da formule, ordinata insieme alle altre celle della riga e utilizzata in altre operazioni a livello di cella.
Questo rende `Cell.EmbeddedImage` l'opzione più concisa quando l'obiettivo è semplicemente «un'immagine contenuta in questa cella».

### **Istruzioni dettagliate**
1. Creare un nuovo `Workbook` (o aprirne uno esistente).
2. Accedere al `Worksheet` di destinazione tramite `workbook.Worksheets[0]`.
3. Leggere il file di immagine dal disco in un array `byte[]` (ad esempio, utilizzando `File.ReadAllBytes`).
4. Ottenere un riferimento alla cella di destinazione — tramite `worksheet.Cells["C6"]` oppure `worksheet.Cells[5, 2]`.
5. Assegnare l'array di byte alla proprietà `EmbeddedImage` della cella.
6. Se desiderato, regolare l'altezza della riga di destinazione e la larghezza della colonna di destinazione per rendere l'immagine incorporata più visibile.
7. Salvare la cartella di lavoro su disco come file `.xlsx`.
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
// Facoltativamente, regola l'altezza della riga e la larghezza della colonna per rendere l'immagine incorporata più visibile
worksheet.Cells.SetColumnWidth(2, 30);   // Colonna C (indice 2)
worksheet.Cells.SetRowHeight(5, 100);     // Riga 6 (indice 5)
// Salva la cartella di lavoro risultante come file .xlsx
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Scelta dell'approccio corretto**
Entrambi gli approcci consentono di ottenere un'immagine adattata a una singola cella, ma differiscono per la modalità di memorizzazione dell'immagine e per il relativo comportamento:
- **Utilizzare un'immagine fluttuante (Approccio 1) quando:**
  - È necessario un controllo più preciso del posizionamento, della stratificazione o dell'allineamento con altri oggetti di disegno.
  - Si desidera che l'immagine si comporti come una forma che può essere selezionata, riordinata o raggruppata con altre forme.
  - È necessario mantenere la compatibilità con il codice legacy che già utilizza `PictureCollection`.
  - È necessario calcolare dinamicamente le coordinate di ancoraggio in base al layout del foglio di lavoro.
- **Utilizzare un'immagine incorporata (Approccio 2) quando:**
  - Si desidera l'inserimento più semplice possibile di un'immagine in una cella.
  - L'immagine deve spostarsi con la cella come qualsiasi altro contenuto della cella.

## Articoli correlati
- [Fotocamera di Excel in Aspose.Cells for .Net](/cells/it/net/excel-camera/)
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells for .Net](/cells/it/net/add-page-field-in-pivot-table/)
- [Applicare stili alle tabelle pivot in Aspose.Cells for .Net](/cells/it/net/apply-style-to-pivot-table/)
- [Modificare il layout dei campi pagina in una tabella pivot](/cells/it/net/change-page-field-layout/)
- [Convertire Sparkline in immagine e HTML in Aspose.Cells for .Net](/cells/it/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}