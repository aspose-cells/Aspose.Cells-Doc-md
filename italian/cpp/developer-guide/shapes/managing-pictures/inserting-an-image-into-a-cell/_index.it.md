---
title: Inserimento di un'immagine in una cella
linktitle: Inserimento di un'immagine in una cella
description: Aspose.Cells è una libreria C++ per lavorare con i file di fogli di calcolo. Questo articolo spiega come adattare esattamente un'immagine a una singola cella, sia posizionando un'immagine mobile sulla cella sia incorporando l'immagine direttamente nella cella.
keywords: Aspose.Cells, libreria C++, foglio di calcolo, inserimento di immagini, incorporazione di immagini, immagine in una cella, adattare l'immagine alla cella, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /it/cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre due modi distinti per associare un'immagine a una singola cella. Un'immagine mobile è una forma sul livello di disegno del foglio di lavoro che si sovrappone visivamente a un intervallo di celle, mentre un'immagine incorporata è memorizzata nella cella stessa e viene ridimensionata automaticamente per adattarsi all'area di visualizzazione della cella. Scegli l'approccio che meglio soddisfa i requisiti di layout.
{{% /alert %}}

## **Introduzione**
Adattare esattamente un'immagine a una singola cella è un requisito comune quando si progettano fogli di calcolo che fungono da report visivi, cataloghi di prodotti, elenchi del personale, dashboard o inventari. Invece di estendere un'immagine su più celle o di posizionarla liberamente su un foglio di lavoro, potrebbe essere necessaria un'immagine pulita e associata a una cella, che rimanga allineata alla cella di proprietà.
Aspose.Cells supporta questo scenario in due modi complementari:
- **Approccio 1 — Posizionare un'immagine mobile su una cella.** Aggiungi un `Picture` al foglio di lavoro, imposta `Placement` su `MoveAndSize` e regola le celle di ancoraggio (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) in modo che l'immagine copra esattamente una cella.
- **Approccio 2 — Incorporare un'immagine direttamente in una cella.** Assegna i byte dell'immagine alla proprietà `EmbeddedImage` della cella. L'immagine viene ridimensionata automaticamente per adattarsi all'area di visualizzazione della cella e si sposta con essa.
La parte restante di questo articolo illustra entrambi gli approcci, spiega le API pertinenti e mostra come usarle nel codice.

## **Approccio 1: Posizionare un'immagine su una cella**
Un'immagine mobile è un oggetto `Picture` che risiede sul livello di disegno del foglio di lavoro. Sebbene non faccia parte di alcuna singola cella, è ancorata a un intervallo di celle. Le celle di ancoraggio dell'immagine, ossia gli angoli superiore sinistro e inferiore destro, determinano la sua estensione visiva sul foglio di lavoro. Per impostazione predefinita, un'immagine appena aggiunta si estende su più celle.
Per fare in modo che un'immagine mobile copra **esattamente una cella**, è necessario:
1. Aggiungere l'immagine utilizzando `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)`, che ancora la nuova immagine alla cella specificata.
2. Impostare le quattro proprietà di ancoraggio in modo che il rettangolo delimitatore dell'immagine coincida con la cella di destinazione.
3. Impostare `Picture.Placement` su `PlacementType.MoveAndSize`, in modo che l'immagine si sposti e venga ridimensionata insieme alla cella sottostante quando l'utente modifica la larghezza della colonna o l'altezza della riga.

### **Ancoraggio dell'immagine a una singola cella**
L'ancoraggio dell'immagine è definito da quattro proprietà con indice a base zero:
- `Picture.UpperLeftRow` — l'indice di riga del bordo superiore dell'immagine.
- `Picture.UpperLeftColumn` — l'indice di colonna del bordo sinistro dell'immagine.
- `Picture.LowerRightRow` — l'indice di riga del bordo inferiore dell'immagine. Per posizionare il bordo inferiore dell'immagine al fondo della riga `r`, impostare questo valore a `r + 1`.
- `Picture.LowerRightColumn` — l'indice di colonna del bordo destro dell'immagine. Per posizionare il bordo destro dell'immagine sul margine destro della colonna `c`, impostare questo valore a `c + 1`.

{{% alert color="primary" %}}
Gli indici di riga e colonna in Aspose.Cells sono **a base zero**. La cella C6 ha indice di riga 5 e indice di colonna 2. Gli errori di un'unità nelle coordinate dell'angolo inferiore destro sono la causa più comune di immagini che sembrano sovrapporsi alla cella adiacente.
{{% /alert %}}

### **Controllo del comportamento di posizionamento**
`Picture.Placement` è un'enumerazione di tipo `PlacementType` che controlla il comportamento dell'immagine quando l'utente ridimensiona la riga o la colonna sottostante. Il valore consigliato per un'immagine in una singola cella è `PlacementType.MoveAndSize`, che fa sì che l'immagine si sposti e venga ridimensionata insieme alla cella sottostante, mantenendo l'adattamento preciso.

### **Istruzioni passo per passo**
1. Creare un nuovo `Workbook` o aprirne uno esistente.
2. Accedere al `Worksheet` di destinazione da `workbook.GetWorksheets().Get(0]`.
3. Leggere il file immagine dal disco in un buffer di byte `Vector<uint8_t>`, in modo che i byte dell'immagine siano disponibili all'API.
4. Chiamare `worksheet.Pictures.Add(5, 2, imageData)` per aggiungere un'immagine ancorata alla cella C6. Memorizzare il riferimento `Picture` restituito.
5. Impostare le quattro coordinate di ancoraggio in modo che l'immagine copra solo la cella C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Impostare `picture.Placement = PlacementType.MoveAndSize` per mantenere l'immagine allineata a C6 quando la colonna o la riga viene ridimensionata.
7. Se necessario, aggiungere testo di esempio alle celle circostanti per dimostrare che solo la cella C6 contiene l'immagine.
8. Salvare la cartella di lavoro su disco come file `.xlsx`.
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
Aspose.Cells espone anche un meccanismo più semplice per le immagini associate a una cella: la proprietà `Cell.EmbeddedImage`. Assegnando i byte dell'immagine a questa proprietà, l'immagine viene associata alla cella stessa, come se fosse contenuto al suo interno.

### **Come funzionano le immagini incorporate**
- L'immagine viene memorizzata come parte del contenuto della cella anziché come forma sul livello di disegno.
- L'immagine viene ridimensionata automaticamente per adattarsi ai limiti visualizzati della cella. Non sono necessarie coordinate di ancoraggio né impostazioni di posizionamento.
- La cella rimane una cella reale, con un indirizzo reale, che può essere richiamata da formule, ordinata come parte di una riga o utilizzata in altre operazioni a livello di cella.
Questo rende `Cell.EmbeddedImage` l'opzione più semplice quando l'obiettivo è soltanto «un'immagine che vive all'interno di questa cella».

### **Istruzioni passo per passo**
1. Creare un nuovo `Workbook` o aprirne uno esistente.
2. Accedere al `Worksheet` di destinazione da `workbook.GetWorksheets().Get(0]`.
3. Leggere il file immagine dal disco in un array di byte `Vector<uint8_t>`.
4. Ottenere un riferimento alla cella di destinazione, tramite `worksheet.GetCells().Get("C6"]` oppure `worksheet.GetCells().Get(5, 2]`.
5. Assegnare l'array di byte alla proprietà `EmbeddedImage` della cella.
6. Se necessario, regolare l'altezza della riga e la larghezza della colonna di destinazione per dare maggiore evidenza all'immagine incorporata.
7. Salvare la cartella di lavoro su disco come file `.xlsx`.
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
    // Leggere il file immagine in un array di byte
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();
    // Convertire std::vector in Aspose::Cells::Vector usando il costruttore puntatore+dimensione
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());
    // Incorporare l'immagine direttamente nella cella
    cell.SetEmbeddedImage(imageData);
    // Se necessario, regolare l'altezza della riga e la larghezza della colonna per rendere più visibile l'immagine incorporata
    worksheet.GetCells().SetColumnWidth(2, 30);   // Colonna C (indice 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // Riga 6 (indice 5)
    // Salvare la cartella di lavoro risultante come file .xlsx
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Scelta dell'approccio corretto**
Entrambi gli approcci producono un'immagine adattata a una singola cella, ma differiscono per il modo in cui l'immagine viene memorizzata e per il suo comportamento:
- **Utilizzare un'immagine mobile (Approccio 1) quando:**
  - È necessario un controllo più preciso sul posizionamento, sulla stratificazione o sull'allineamento con altri oggetti di disegno.
  - Si desidera che l'immagine si comporti come una forma selezionabile, riordinabile o raggruppabile con altre forme.
  - È necessaria la compatibilità con codice esistente che già utilizza `PictureCollection`.
  - È necessario calcolare dinamicamente le coordinate di ancoraggio in base alla disposizione del foglio di lavoro.
- **Utilizzare un'immagine incorporata (Approccio 2) quando:**
  - Si desidera il modo più semplice possibile per inserire un'immagine in una cella.
  - L'immagine deve spostarsi con la cella come qualsiasi altro contenuto di cella.

## Articoli correlati
- [Telecamera di Excel in Aspose.Cells for C++](/cells/it/cpp/excel-camera/)

{{< app/cells/assistant language="cpp" >}}