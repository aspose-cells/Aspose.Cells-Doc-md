---
title: Inserimento di un'immagine in una cella
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo. Questo articolo spiega come adattare un'immagine esattamente alla dimensione di una singola cella utilizzando due approcci diversi: posizionare un'immagine mobile sopra la cella oppure incorporare l'immagine direttamente nella cella.
keywords: Aspose.Cells, libreria C++, foglio di calcolo, inserire immagine, incorporare immagine, immagine in cella, adattare immagine a cella, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /it/cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells offre due modi distinti per associare un'immagine a una singola cella. Un'immagine mobile è una forma sul livello di disegno del foglio di lavoro che si sovrappone visivamente a un intervallo di celle, mentre un'immagine incorporata è memorizzata all'interno della cella stessa e si ridimensiona automaticamente all'area di visualizzazione della cella. Scegli l'approccio che meglio si adatta alle tue esigenze di layout.

{{% /alert %}}

## **Introduzione**

Adattare un'immagine esattamente a una singola cella è un requisito comune quando si progettano fogli di calcolo che fungono da report visivi, cataloghi di prodotti, rubriche di dipendenti, dashboard o elenchi di inventario. Piuttosto che estendere un'immagine su molte celle o posizionarla liberamente su un foglio di lavoro, potresti volere un'immagine pulita, legata alla cella, che rimanga allineata con la cella che la possiede.

Aspose.Cells supporta questo scenario in due modi complementari:

- **Approccio 1 — Posizionare un'immagine mobile sopra una cella.** Aggiungere una `Picture` al foglio di lavoro, impostare il suo `Placement` su `MoveAndSize` e regolare le sue celle di ancoraggio (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) in modo che l'immagine copra esattamente una cella.
- **Approccio 2 — Incorporare un'immagine direttamente in una cella.** Assegnare i byte dell'immagine alla proprietà `EmbeddedImage` della cella. L'immagine si ridimensiona automaticamente per adattarsi all'area di visualizzazione della cella e si sposta con essa.

Il resto di questo articolo illustra entrambi gli approcci, spiega le API pertinenti e mostra come utilizzarle nel codice.

## **Approccio 1: Posizionare un'immagine sopra una cella**

Un'immagine mobile è un oggetto `Picture` che risiede sul livello di disegno del foglio di lavoro. Sebbene non faccia parte di una singola cella, è ancorata a un intervallo di celle. Le celle di ancoraggio dell'immagine — i suoi angoli in alto a sinistra e in basso a destra — ne determinano l'estensione visiva sul foglio di lavoro. Per impostazione predefinita, un'immagine appena aggiunta si estende su più celle.

Per fare in modo che un'immagine mobile copra **esattamente una cella**, è necessario:

1. Aggiungere l'immagine utilizzando `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)`, che ancora la nuova immagine alla cella specificata.
2. Impostare le quattro proprietà di ancoraggio in modo che il rettangolo di delimitazione dell'immagine coincida con la cella di destinazione.
3. Impostare `Picture.Placement` su `PlacementType.MoveAndSize` in modo che l'immagine si sposti e si ridimensioni con la cella sottostante quando l'utente modifica la larghezza della colonna o l'altezza della riga.

### **Ancoraggio dell'immagine a una singola cella**

L'ancoraggio dell'immagine è definito da quattro proprietà di indice a base zero:

- `Picture.UpperLeftRow` — l'indice di riga del bordo superiore dell'immagine.
- `Picture.UpperLeftColumn` — l'indice di colonna del bordo sinistro dell'immagine.
- `Picture.LowerRightRow` — l'indice di riga del bordo inferiore dell'immagine. Per fare in modo che il bordo inferiore dell'immagine si trovi alla fine della riga `r`, impostare questo valore su `r + 1`.
- `Picture.LowerRightColumn` — l'indice di colonna del bordo destro dell'immagine. Per fare in modo che il bordo destro dell'immagine si trovi alla fine della colonna `c`, impostare questo valore su `c + 1`.

Ad esempio, per adattare l'immagine esattamente alla cella **C6** (indice di riga `5`, indice di colonna `2`), impostare `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` e `LowerRightColumn = 3`.

{{% alert color="primary" %}}

Gli indici di riga e colonna in Aspose.Cells sono **a base zero**. La cella C6 ha indice di riga 5 e indice di colonna 2. Gli errori di uno sull'ancoraggio inferiore-destro sono la fonte più comune di immagini che sembrano sovrapporsi a una cella adiacente.

{{% /alert %}}

### **Controllo del comportamento di posizionamento**

`Picture.Placement` è un'enumerazione di tipo `PlacementType` che controlla come si comporta l'immagine quando l'utente ridimensiona la riga o la colonna sottostante. Il valore consigliato per un'immagine a cella singola è `PlacementType.MoveAndSize`, che fa sì che l'immagine si sposti e si ridimensioni insieme alla cella sottostante, preservando l'adattamento esatto.

### **Istruzioni passo-passo**

1. Crea una nuova `Workbook` (o aprine una esistente).
2. Accedi al `Worksheet` di destinazione da `workbook.Worksheets[0]`.
3. Leggi il file immagine dal disco in un buffer di byte `Vector<uint8_t>` in modo che i byte dell'immagine siano disponibili per l'API.
4. Chiama `worksheet.Pictures.Add(5, 2, imageData)` per aggiungere un'immagine ancorata alla cella C6. Cattura il riferimento `Picture` restituito.
5. Imposta le quattro coordinate di ancoraggio in modo che l'immagine copra solo la cella C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Imposta `picture.Placement = PlacementType.MoveAndSize` per mantenere l'immagine allineata con C6 quando la colonna o la riga viene ridimensionata.
7. Facoltativamente, aggiungi del testo di esempio alle celle circostanti per dimostrare che solo la cella C6 contiene l'immagine.
8. Salva la cartella di lavoro su disco come file `.xlsx`.

Il codice seguente dimostra l'approccio completo.

```cpp
#include "Aspose.Cells.h"
#include <fstream>
#include <vector>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::ifstream fs("logo.png", std::ios::binary);
    std::vector<uint8_t> stdData((std::istreambuf_iterator<char>(fs)),
                                  std::istreambuf_iterator<char>());
    fs.close();

    Vector<uint8_t> imageData(reinterpret_cast<const uint8_t*>(stdData.data()),
                              static_cast<int32_t>(stdData.size()));

    int picIndex = worksheet.GetPictures().Add(5, 2, imageData);
    Picture picture = worksheet.GetPictures().Get(picIndex);
    picture.SetUpperLeftRow(5);
    picture.SetUpperLeftColumn(2);
    picture.SetLowerRightRow(6);
    picture.SetLowerRightColumn(3);
    picture.SetPlacement(PlacementType::MoveAndSize);

    workbook.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Approccio 2: Incorporare un'immagine direttamente in una cella**

Aspose.Cells espone anche un meccanismo più semplice per immagini legate a celle: la proprietà `Cell.EmbeddedImage`. Assegnare i byte dell'immagine a questa proprietà collega l'immagine alla cella stessa, come se fosse contenuto inline.

### **Come funzionano le immagini incorporate**

- L'immagine viene memorizzata come parte del contenuto della cella piuttosto che come forma sul livello di disegno.
- L'immagine si ridimensiona automaticamente per adattarsi ai confini resi della cella. Non sono richieste coordinate di ancoraggio o impostazioni di posizionamento.
- La cella rimane una vera cella con un vero indirizzo che può essere referenziato da formule, ordinato come parte di una riga o utilizzato in altre operazioni a livello di cella.

Questo rende `Cell.EmbeddedImage` l'opzione più concisa quando il tuo obiettivo è semplicemente "un'immagine che vive all'interno di questa cella".

### **Istruzioni passo-passo**

1. Crea una nuova `Workbook` (o aprine una esistente).
2. Accedi al `Worksheet` di destinazione da `workbook.Worksheets[0]`.
3. Leggi il file immagine dal disco in un array di byte `Vector<uint8_t>`.
4. Ottieni un riferimento alla cella di destinazione — tramite `worksheet.Cells["C6"]` oppure `worksheet.Cells[5, 2]`.
5. Assegna l'array di byte alla proprietà `EmbeddedImage` della cella.
6. Facoltativamente, regola l'altezza della riga e la larghezza della colonna della riga e colonna di destinazione per dare all'immagine incorporata un aspetto più prominente.
7. Salva la cartella di lavoro su disco come file `.xlsx`.

Il codice seguente dimostra l'approccio completo.

```cpp
#include "Aspose.Cells.h"
#include <vector>
#include <fstream>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(u"C6");

    // Legge il file immagine in un array di byte
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    // Converte std::vector in Aspose::Cells::Vector usando il costruttore con puntatore e dimensione
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());

    // Incorpora l'immagine direttamente nella cella
    cell.SetEmbeddedImage(imageData);

    // Opzionalmente regola l'altezza della riga e la larghezza della colonna per rendere più visibile l'immagine incorporata
    worksheet.GetCells().SetColumnWidth(2, 30);   // Colonna C (indice 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // Riga 6 (indice 5)

    // Salva la cartella di lavoro risultante come file .xlsx
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Scegliere l'approccio giusto**

Entrambi gli approcci producono un'immagine che si adatta a una singola cella, ma differiscono nel modo in cui l'immagine viene memorizzata e nel suo comportamento:

- **Usa un'immagine mobile (Approccio 1) quando:**
  - Hai bisogno di un controllo più fine sul posizionamento, sulla stratificazione o sull'allineamento con altri oggetti di disegno.
  - Vuoi che l'immagine si comporti come una forma che può essere selezionata, riordinata o raggruppata con altre forme.
  - Richiedi compatibilità legacy con codice che già funziona con `PictureCollection`.
  - Hai bisogno di calcolare le coordinate di ancoraggio dinamicamente in base al layout del foglio di lavoro.

- **Usa un'immagine incorporata (Approccio 2) quando:**
  - Vuoi il modo più semplice possibile per inserire un'immagine in una cella.
  - L'immagine deve spostarsi con la cella come qualsiasi altro contenuto della cella.
  - Non hai bisogno di manipolare l'immagine come una forma.

{{% alert color="primary" %}}

Entrambi gli approcci possono coesistere nella stessa cartella di lavoro. Puoi posizionare immagini mobili sopra un insieme di celle e incorporare immagini direttamente in altre celle, poiché i due meccanismi utilizzano livelli di archiviazione diversi nel file.

{{% /alert %}}

## **Articoli correlati**

- [Come inserire un'immagine in una cella](/cells/it/cpp/how-to-place-image-to-cell/)
- [Aggiungere collegamenti ipertestuali alle immagini](/cells/it/cpp/add-image-hyperlinks/)
- [Caricare un'immagine Web da un URL in un foglio di lavoro Excel](/cells/it/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipolare posizione, dimensione e grafico del designer](/cells/it/cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="cpp" >}}