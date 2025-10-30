---
title: Gestione dei controlli con C++
linktitle: Gestione dei controlli
type: docs
weight: 150
url: /it/cpp/managing-controls/
description: Impara come aggiungere e gestire vari controlli come linee, rettangoli, archi, ovali, spinner, barre di scorrimento e gruppi di caselle in fogli di lavoro usando Aspose.Cells con C++.
---

## **Introduzione**

Gli sviluppatori possono aggiungere diversi oggetti di disegno come caselle di testo, caselle di controllo, pulsanti di opzione, caselle combinate, etichette, pulsanti, linee, rettangoli, archi, ovali, spinner, barre di scorrimento, gruppi, ecc. Aspose.Cells offre il namespace `Aspose::Cells::Drawing` che contiene tutti gli oggetti di disegno. Tuttavia, ci sono alcuni oggetti di disegno o forme ancora non supportati. Crea questi oggetti di disegno in un foglio di calcolo progettato usando Microsoft Excel e poi importa il foglio di calcolo di progetto in Aspose.Cells. Aspose.Cells ti permette di caricare questi oggetti di disegno da un foglio di calcolo di progettazione e di scriverli in un file generato.

## **Aggiunta di un controllo casella di testo a un foglio di calcolo**

Un modo per evidenziare informazioni importanti in un report è utilizzare una casella di testo. Ad esempio, aggiungere testo per evidenziare il nome dell'azienda o per indicare la regione geografica con le vendite più alte, ecc. Aspose.Cells fornisce la classe [**TextBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textboxcollection/), utilizzata per aggiungere una nuova casella di testo alla collezione. C'è anche un'altra classe, [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/), che rappresenta una casella di testo utilizzata per definire tutti i tipi di impostazioni. Ha alcuni membri importanti:

- La proprietà [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) specifica il tipo di posizionamento.
- La proprietà [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) specifica gli attributi del font.
- Il metodo [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) aggiunge un collegamento ipertestuale per la casella di testo.
- La proprietà [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) restituisce un oggetto [**MsoFillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msofillformat/) utilizzato per impostare il formato di riempimento per la casella di testo.
- La proprietà [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) restituisce l'oggetto [**MsoLineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msolineformat/) di solito usato per lo stile e lo spessore della linea della casella di testo.
- La proprietà [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) specifica il testo di input per la casella di testo.

Nell'esempio seguente vengono create due caselle di testo nel primo foglio di lavoro del documento. La prima casella di testo è ben arredata con diverse impostazioni di formato. La seconda è semplice.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // The path to the documents directory.
    U16String dataDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get the first worksheet in the book.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a new textbox to the collection.
    int32_t textboxIndex = worksheet.GetTextBoxes().Add(2, 1, 160, 200);

    // Get the textbox object.
    TextBox textbox0 = worksheet.GetTextBoxes().Get(textboxIndex);

    // Fill the text.
    textbox0.SetText(u"ASPOSE______The .NET & JAVA Component Publisher!");

    // Set the placement.
    textbox0.SetPlacement(PlacementType::FreeFloating);

    // Set the font color.
    textbox0.GetFont().SetColor(Color::Blue());

    // Set the font to bold.
    textbox0.GetFont().SetIsBold(true);

    // Set the font size.
    textbox0.GetFont().SetSize(14);

    // Set font attribute to italic.
    textbox0.GetFont().SetIsItalic(true);

    // Add a hyperlink to the textbox.
    textbox0.AddHyperlink(u"http://www.aspose.com/");

    // Get the fill format of the textbox.
    FillFormat fillFormat = textbox0.GetFill();

    // Get the line format type of the textbox.
    LineFormat lineFormat = textbox0.GetLine();

    // Set the line weight.
    lineFormat.SetWeight(6.0);

    // Set the dash style to squaredot.
    lineFormat.SetDashStyle(MsoLineDashStyle::SquareDot);

    // Add another textbox.
    textboxIndex = worksheet.GetTextBoxes().Add(15, 4, 85, 120);

    // Get the second textbox.
    TextBox textbox1 = worksheet.GetTextBoxes().Get(textboxIndex);

    // Input some text to it.
    textbox1.SetText(u"This is another simple text box");

    // Set the placement type as the textbox will move and resize with cells.
    textbox1.SetPlacement(PlacementType::MoveAndSize);

    // Save the excel file.
    workbook.Save(dataDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Manipolazione dei controlli casella di testo nei fogli di calcolo progettati**

Aspose.Cells consente anche di accedere alle caselle di testo nei fogli di lavoro del designer e manipolarle. Utilizzare la proprietà [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/) per ottenere la raccolta delle caselle di testo nel foglio.

Nell'esempio seguente viene utilizzato il file Microsoft Excel che abbiamo creato nell'esempio precedente. Ottiene le stringhe di testo delle due caselle di testo e modifica il testo della seconda casella di testo per salvare il file.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // The path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file.
    Workbook workbook(srcDir + u"book1.xls");

    // Get the first worksheet in the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first textbox object.
    TextBox textbox0 = worksheet.GetTextBoxes().Get(0);

    // Obtain the text in the first textbox.
    U16String text0 = textbox0.GetText();

    // Get the second textbox object.
    TextBox textbox1 = worksheet.GetTextBoxes().Get(1);

    // Obtain the text in the second textbox.
    U16String text1 = textbox1.GetText();

    // Change the text of the second textbox.
    textbox1.SetText(u"This is an alternative text");

    // Save the excel file.
    workbook.Save(srcDir + u"output.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Aggiunta di un controllo casella di controllo a un foglio di calcolo**

Le caselle di controllo sono utili se si desidera fornire un modo per consentire all'utente di scegliere tra due opzioni, ad esempio vero o falso; sì o no. Aspose.Cells consente di utilizzare caselle di controllo nei fogli di lavoro. Ad esempio, è possibile avere sviluppato un foglio di lavoro di proiezione finanziaria nel quale è possibile contabilizzare o meno un'acquisizione specifica. In questo caso, potrebbe essere opportuno posizionare una casella di controllo nella parte superiore del foglio di lavoro. È quindi possibile collegare lo stato di questa casella di controllo a un'altra cella, in modo che se la casella di controllo è selezionata, il valore della cella è Vero; se non è selezionata, il valore della cella è Falso.

### **Utilizzando Microsoft Excel**

Per inserire un controllo casella di controllo nel foglio di lavoro, seguire questi passaggi:

1. Assicurarsi che la barra degli strumenti Moduli sia visualizzata.
1. Fare clic sul pulsante **Casella di controllo** sulla barra degli strumenti Moduli.
1. Nella tua area di lavoro, fare clic e trascinare per definire il rettangolo che conterrà la casella di controllo e l'etichetta accanto alla casella di controllo.
1. Una volta inserita la casella di controllo, spostare il cursore del mouse nell'area dell'etichetta e modificare l'etichetta.
1. Nel campo **Collegamento cella**, specificare l'indirizzo della cella a cui questa casella di controllo dovrebbe essere collegata.
1. Fare clic su **OK**.

### **Usare Aspose.Cells**

Aspose.Cells fornisce la classe [**CheckBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkboxcollection/), che viene utilizzata per aggiungere una nuova casella di controllo alla raccolta. C'è un'altra classe, [**Aspose::Cells::Drawing::CheckBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/), che rappresenta una casella di controllo. Ha alcuni membri importanti:

- La proprietà [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) specifica una cella che è collegata alla casella di controllo.
- La proprietà [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) specifica la stringa di testo associata alla casella di controllo. È l'etichetta della casella di controllo.
- La proprietà [**GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/getvalue/) specifica se la casella di controllo è selezionata o meno.

L'esempio seguente mostra come aggiungere una casella di controllo al foglio di lavoro.

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a new Workbook instance
    Workbook excelbook = Workbook();

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Add a checkbox to the first worksheet in the workbook
    int32_t index = worksheet.GetCheckBoxes().Add(5, 5, 100, 120);

    // Get the checkbox object
    Drawing::CheckBox checkbox = worksheet.GetCheckBoxes().Get(index);

    // Set its text string
    checkbox.SetText(u"Click it!");

    // Get cells collection and set B1 cell value
    Cells cells = worksheet.GetCells();
    Cell cellB1 = cells.Get(u"B1");
    cellB1.PutValue(u"LnkCell");

    // Set B1 cell as a linked cell for the checkbox
    checkbox.SetLinkedCell(u"B1");

    // Check the checkbox by default
    checkbox.SetValue(true);

    // Save the excel file
    excelbook.Save(u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Aggiungere un controllo pulsante di opzione al foglio di lavoro**

Un pulsante radio, o un pulsante di opzione, è un controllo composto da una casella rotonda. L'utente prende la sua decisione selezionando la casella rotonda. Un pulsante radio è di solito, se non sempre, accompagnato da altri. Tali pulsanti radio appaiono e si comportano come un gruppo. L'utente decide quale pulsante è valido selezionandone solo uno. Quando l'utente fa clic su un pulsante, viene riempito. Quando un pulsante nel gruppo è selezionato, i pulsanti dello stesso gruppo sono vuoti.

### **Utilizzando Microsoft Excel**

Per inserire un controllo Radio Button nel tuo foglio di lavoro, segui questi passaggi:

1. Assicurati che la barra degli strumenti **Form** sia visualizzata.
1. Clicca sullo strumento **Pulsante di Opzione**.
1. Nel foglio di lavoro, clicca e trascina per definire il rettangolo che conterrà il pulsante di opzione e l'etichetta accanto al pulsante di opzione.
1. Una volta che il pulsante radio è stato posizionato nel foglio di lavoro, sposta il cursore del mouse nell'area dell'etichetta e cambia l'etichetta.
1. Nel campo **Collegamento cella**, specifica l'indirizzo della cella a cui questo radio button dovrebbe essere collegato.
1. Fai clic su **OK**.

### **Usare Aspose.Cells**

La classe [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddRadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addradiobutton/), utilizzato per aggiungere un controllo pulsante di opzione a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/). La classe [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) rappresenta un pulsante di opzione. Ha alcuni membri importanti:

- La proprietà [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) specifica una cella che è collegata al pulsante di opzione.
- La proprietà [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) specifica la stringa di testo associata al pulsante di opzione. È l'etichetta del pulsante di opzione.
- La proprietà [**IsChecked**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/ischecked/) specifica se il pulsante di opzione è selezionato o meno.
- La proprietà [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) specifica il formato di riempimento del pulsante di opzione.
- La proprietà [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) specifica gli stili di formato della linea del pulsante di opzione.

L'esempio seguente mostra come aggiungere pulsanti di opzione a un foglio di lavoro. L'esempio aggiunge tre pulsanti di opzione che rappresentano gruppi di età.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a new Workbook.
    Workbook excelbook;

    // Get the first worksheet
    Worksheet sheet = excelbook.GetWorksheets().Get(0);

    // Get cells collection
    Cells cells = sheet.GetCells();

    // Insert a value in C2
    Cell cellC2 = cells.Get(u"C2");
    cellC2.PutValue(u"Age Groups");

    // Set the font text bold.
    Style style = cellC2.GetStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);

    // Apply the style back
    cellC2.SetStyle(style);

    // Add radio buttons to the first sheet.
    ShapeCollection shapes = sheet.GetShapes();

    // Create first radio button
    RadioButton radio1= shapes.AddRadioButton(3, 0, 2, 0, 30, 110);


    // Set its text string.
    radio1.SetText(u"20-29");
    // Set A1 cell as a linked cell for the radio button.
    radio1.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio1.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line1 = radio1.GetLine();
    line1.SetWeight(4);
    // Set the dash style of the radio button.
    line1.SetDashStyle(MsoLineDashStyle::Solid);

    // Create second radio button
    RadioButton radio2 = shapes.AddRadioButton(6, 0, 2, 0, 30, 110);
    // Set its text string.
    radio2.SetText(u"30-39");
    // Set A1 cell as a linked cell for the radio button.
    radio2.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio2.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line2 = radio2.GetLine();
    line2.SetWeight(4);
    // Set the dash style of the radio button.
    line2.SetDashStyle(MsoLineDashStyle::Solid);

    // Create third radio button
    RadioButton radio3=shapes.AddRadioButton(9, 0, 2, 0, 30, 110);

    // Set its text string.
    radio3.SetText(u"40-49");
    // Set A1 cell as a linked cell for the radio button.
    radio3.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio3.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line3 = radio3.GetLine();
    line3.SetWeight(4);
    // Set the dash style of the radio button.
    line3.SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file.
    excelbook.Save(srcDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Aggiungere un Controllo Combo Box a un Foglio di Lavoro**

Per rendere più semplice l'inserimento dei dati, o per limitare le voci a determinati elementi definiti da te, puoi creare una casella combinata, o una lista a discesa di voci valide che è compilata da celle altrove nel foglio di lavoro. Quando crei una lista a discesa per una cella, viene visualizzata una freccia accanto a quella cella. Per inserire informazioni in quella cella, clicca sulla freccia e poi sulla voce che desideri.

### **Utilizzando Microsoft Excel**

Per inserire un controllo casella combinata nel tuo foglio di lavoro, segui questi passaggi:

1. Assicurati che la barra degli strumenti **Form** sia visualizzata.
1. Clicca sullo strumento **Casella Combinata**.
1. Nella tua area di lavoro, clicca e trascina per definire il rettangolo che conterrà la casella combinata.
1. Una volta che la casella combinata è posizionata nel foglio di lavoro, fare clic con il pulsante destro del mouse sul controllo per fare clic su **Formato Controllo** e specificare l'intervallo di input.
1. Nel campo **Collegamento Cella**, specificare l'indirizzo della cella a cui questa casella combinata dovrebbe essere collegata.
1. Fare clic su **OK**.

### **Usare Aspose.Cells**

La classe [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcombobox/), che serve per aggiungere un controllo casella combinata a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/). La classe [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) rappresenta una casella combinata. Ha alcuni membri importanti:

- La proprietà [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) specifica una cella collegata alla casella combinata.
- La proprietà [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) specifica l'intervallo di celle del foglio di lavoro utilizzato per riempire la casella combinata.
- La proprietà [**GetDropDownLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getdropdownlines/) specifica il numero di righe dell'elenco visualizzate nella parte a discesa di una casella combinata.
- La proprietà [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getshadow/) indica se la casella combinata ha una ombreggiatura 3D.

L'esempio seguente mostra come aggiungere una casella combinata al foglio di lavoro.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook.
    Workbook workbook;

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the worksheet cells collection.
    Cells cells = sheet.GetCells();

    // Input a value.
    Cell cellB3 = cells.Get(u"B3");
    cellB3.PutValue(u"Employee:");

    // Set it bold.
    Style style = cellB3.GetStyle();
    style.SetIsBorderApplied(true);
    cellB3.SetStyle(style);

    // Input some values that denote the input range for the combo box.
    cells.Get(u"A2").PutValue(u"Emp001");
    cells.Get(u"A3").PutValue(u"Emp002");
    cells.Get(u"A4").PutValue(u"Emp003");
    cells.Get(u"A5").PutValue(u"Emp004");
    cells.Get(u"A6").PutValue(u"Emp005");
    cells.Get(u"A7").PutValue(u"Emp006");

    // Add a new combo box.
    ComboBox comboBox = sheet.GetShapes().AddComboBox(2, 0, 2, 0, 22, 100);

    // Cleanup Aspose resources
    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Aggiunta del Controllo Etichetta a un Foglio di Lavoro**

Le etichette sono un modo per fornire informazioni agli utenti sui contenuti di un foglio di calcolo. Aspose.Cells rende possibile aggiungere e manipolare etichette in un foglio di lavoro. La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddLabel**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabel/), utilizzato per aggiungere un controllo etichetta al foglio di lavoro. Il metodo restituisce un oggetto [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/). La classe [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) rappresenta un'etichetta nel foglio di lavoro. Ha alcuni membri importanti:

- Il metodo [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) specifica una stringa di didascalia dell'etichetta.
- Il metodo [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) specifica il [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), il modo in cui l'etichetta è collegata alle celle nel foglio di lavoro.

Nell'esempio seguente viene mostrato come aggiungere un'etichetta al foglio di lavoro.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a new label to the worksheet
    Label label = sheet.GetShapes().AddLabel(2, 0, 2, 0, 60, 120);

    // Set the caption of the label
    label.SetText(u"This is a Label");

    // Set the Placement Type, the way the Label is attached to the cells
    label.SetPlacement(PlacementType::FreeFloating);

    // Save the file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Label added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aggiunta di un Controllo Casella Elenco a un Foglio di Lavoro**

Un controllo casella elenco crea un controllo elenco che consente la selezione di uno o più elementi.

### **Utilizzando Microsoft Excel**

Per posizionare un controllo casella elenco in un foglio di lavoro:

1. Assicurati che la barra degli strumenti **Form** sia visualizzata.
1. Fare clic sullo strumento **Casella Elenco**.
1. Nella tua area di lavoro, fare clic e trascinare per definire il rettangolo che conterrà la casella di selezione.
1. Una volta posizionata la casella di selezione nel foglio di lavoro, fare clic con il tasto destro sul controllo per fare clic su **Formato controllo** e specificare l'intervallo di input.
1. Nel campo **Collegamento cella**, specificare l'indirizzo della cella a cui questa casella di selezione deve essere collegata e impostare l'attributo del tipo di selezione (Singola, Multipla, Estesa).
1. Fai clic su **OK**.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlistbox/), che viene utilizzato per aggiungere un controllo casella di selezione a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose::Cells::Drawing::ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/). La classe [**ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) rappresenta una casella di selezione. Ha alcuni membri importanti:

- Il metodo [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) specifica una cella collegata alla casella di selezione.
- Il metodo [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) specifica l'intervallo di celle nel foglio di lavoro utilizzato per riempire la casella di selezione.
- Il metodo [**SelectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/selectiontype/) specifica la modalità di selezione della casella di selezione.
- Il metodo [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/getshadow/) indica se la casella di selezione ha un'ombreggiatura 3D.

Nell'esempio seguente viene mostrato come aggiungere una casella di selezione al foglio di lavoro.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the worksheet cells collection
    Cells cells = sheet.GetCells();

    // Input a value
    cells.Get(U16String(u"B3")).PutValue(U16String(u"Choose Dept:"));

    // Set it bold
    Style style = cells.Get(U16String(u"B3")).GetStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    cells.Get(U16String(u"B3")).SetStyle(style);

    // Input some values that denote the input range for the list box
    cells.Get(U16String(u"A2")).PutValue(U16String(u"Sales"));
    cells.Get(U16String(u"A3")).PutValue(U16String(u"Finance"));
    cells.Get(U16String(u"A4")).PutValue(U16String(u"MIS"));
    cells.Get(U16String(u"A5")).PutValue(U16String(u"R&D"));
    cells.Get(U16String(u"A6")).PutValue(U16String(u"Marketing"));
    cells.Get(U16String(u"A7")).PutValue(U16String(u"HRA"));

    // Add a new list box
    ListBox listBox = sheet.GetShapes().AddListBox(2, 0, 3, 0, 122, 100);

    // Set the placement type
    listBox.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell
    listBox.SetLinkedCell(U16String(u"A1"));

    // Set the input range
    listBox.SetInputRange(U16String(u"A2:A7"));

    // Set the selection type
    listBox.SetSelectionType(SelectionType::Single);

    // Set the list box with 3-D shading
    listBox.SetShadow(true);

    // Save the file
    workbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Aggiunta del controllo Pulsante a un foglio di lavoro**

I pulsanti sono utili per eseguire alcune azioni. A volte è utile assegnare un Macro VBA al pulsante o assegnare un collegamento ipertestuale per aprire una pagina web.

### **Utilizzando Microsoft Excel**

Per inserire un controllo pulsante nel tuo foglio di lavoro:

1. Assicurati che la barra degli strumenti **Form** sia visualizzata.
1. Fare clic sullo strumento **Pulsante**.
1. Nella tua area di lavoro, fare clic e trascinare per definire il rettangolo che conterrà il pulsante.
1. Una volta posizionata la casella di selezione nel foglio di lavoro, fare clic con il tasto destro sul controllo e selezionare **Formato controllo**, quindi specificare un Macro VBA e attributi relativi al carattere, all'allineamento, alla dimensione, al margine, ecc.
1. Fare clic su **OK**.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addbutton/), utilizzato per aggiungere un controllo pulsante al foglio di lavoro. Il metodo restituisce un oggetto [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/). La classe [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) rappresenta un pulsante. Ha alcuni membri importanti:

- La proprietà [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) specifica la didascalia del pulsante.
- La proprietà [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) specifica gli attributi del carattere per l'etichetta del controllo del pulsante.
- La proprietà [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) specifica il [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), il modo in cui il pulsante è collegato alle celle nel foglio di lavoro.
- La proprietà [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) aggiunge un collegamento ipertestuale per il controllo del pulsante. Facendo clic sul pulsante si passerà all'URL correlato.

L'esempio seguente mostra come aggiungere un pulsante al foglio di lavoro.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a new button to the worksheet
    Drawing::Button button = sheet.GetShapes().AddButton(2, 0, 2, 0, 28, 80);

    // Set the caption of the button
    button.SetText(u"Aspose");

    // Set the Placement Type, the way the Button is attached to the cells
    button.SetPlacement(PlacementType::FreeFloating);

    // Set the font name
    Font font = button.GetFont();
    font.SetName(u"Tahoma");

    // Set the caption string bold
    font.SetIsBold(true);

    // Set the color to blue
    font.SetColor(Color::Blue());

    // Set the hyperlink for the button
    button.AddHyperlink(u"http://www.aspose.com/");

    // Save the file
    workbook.Save(srcDir + u"book1.out.xls");

    std::cout << "Button added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aggiunta del controllo linea al foglio di lavoro**

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Forme automatiche**, puntare su **Linee** e selezionare lo stile della linea desiderato.
1. Trascinare per disegnare la linea.
1. Eseguire una o entrambe le seguenti azioni:
   1. Per vincolare la linea a disegnare a angoli di 15 gradi dal punto di inizio, tenere premuto SHIFT mentre si trascina.
   1. Per allungare la linea in direzioni opposte dal primo punto di estremità, tenere premuto CTRL mentre si trascina.

### **Usare Aspose.Cells**

 La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addline/), utilizzato per aggiungere una forma linea al foglio di lavoro. Il metodo restituisce un oggetto [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/). La classe [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) rappresenta una linea. Ha alcuni membri importanti:

- Il metodo [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) specifica il formato di una riga.
- Il metodo [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) specifica il [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), il modo in cui la riga è collegata alle celle nel foglio di lavoro.

L'esempio seguente mostra come aggiungere righe al foglio di lavoro. Crea tre righe con stili diversi.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a new line to the worksheet
    LineShape line1 = worksheet.GetShapes().AddLine(5, 0, 1, 0, 0, 250);

    // Set the line dash style
    line1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Set the placement
    line1.SetPlacement(PlacementType::FreeFloating);

    // Add another line to the worksheet
    LineShape line2 = worksheet.GetShapes().AddLine(7, 0, 1, 0, 85, 250);

    // Set the line dash style
    line2.GetLine().SetDashStyle(MsoLineDashStyle::DashLongDash);

    // Set the weight of the line
    line2.GetLine().SetWeight(4);

    // Set the placement
    line2.SetPlacement(PlacementType::FreeFloating);

    // Add the third line to the worksheet
    LineShape line3 = worksheet.GetShapes().AddLine(13, 0, 1, 0, 0, 250);

    // Set the line dash style
    line3.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Set the placement
    line3.SetPlacement(PlacementType::FreeFloating);

    // Make the gridlines invisible in the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Lines added successfully to the worksheet!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Aggiunta di una testa di freccia a una linea**

Aspose.Cells ti consente anche di disegnare linee con punta a freccia. È possibile aggiungere una punta a freccia a una linea e formattare la linea. Ad esempio, puoi cambiare il colore della linea o specificare lo spessore e lo stile della linea.

L'esempio seguente mostra come aggiungere una testa di freccia a una linea.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a line to the worksheet
    LineShape line2 = worksheet.GetShapes().AddLine(7, 0, 1, 0, 85, 250);

    // Set the line color
    line2.GetLine().SetFillType(FillType::Solid);
    line2.GetLine().GetSolidFill().SetColor(Color::Blue());

    // Set the weight of the line
    line2.GetLine().SetWeight(3);

    // Set the placement
    line2.SetPlacement(PlacementType::FreeFloating);

    // Set the line arrows
    line2.GetLine().SetEndArrowheadWidth(MsoArrowheadWidth::Medium);
    line2.GetLine().SetEndArrowheadStyle(MsoArrowheadStyle::Arrow);
    line2.GetLine().SetEndArrowheadLength(MsoArrowheadLength::Medium);
    line2.GetLine().SetBeginArrowheadStyle(MsoArrowheadStyle::ArrowDiamond);
    line2.GetLine().SetBeginArrowheadLength(MsoArrowheadLength::Medium);

    // Make the gridlines invisible in the first worksheet
    workbook.GetWorksheets().Get(0).SetIsGridlinesVisible(false);

    // Save the excel file
    workbook.Save(outDir + u"book1.out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Aggiunta del controllo Rettangolo in un foglio di lavoro**

Aspose.Cells ti consente di disegnare forme rettangolari nei tuoi fogli di lavoro. Puoi creare un rettangolo, un quadrato, ecc. Ti è anche consentito formattare il colore di riempimento e il colore della linea di bordo del controllo. Ad esempio, puoi cambiare il colore del rettangolo, impostare il colore di sfondo, specificare lo spessore e lo stile del rettangolo per le tue esigenze.

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Rettangolo**.
1. Trascina per disegnare il rettangolo.
1. Eseguire una o entrambe le seguenti azioni:
   1. Per vincolare il rettangolo e disegnare un quadrato dal suo punto iniziale, premere il tasto MAIUSC mentre trascini.
   1. Per disegnare un rettangolo da un punto centrale, premere il tasto CTRL mentre trascini.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddRectangle**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addrectangle/), che viene utilizzato per aggiungere una forma rettangolare a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/). La classe [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) rappresenta un rettangolo. Ha alcuni membri importanti:

- La proprietà [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) specifica gli attributi del formato della linea di un rettangolo.
- La proprietà [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) specifica il [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), il modo in cui il rettangolo è collegato alle celle nel foglio di lavoro.
- La proprietà [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) specifica gli stili di formato del riempimento di un rettangolo.

L'esempio seguente mostra come aggiungere un rettangolo al foglio di lavoro.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add a rectangle control to the first worksheet
    RectangleShape rectangle = excelbook.GetWorksheets().Get(0).GetShapes().AddRectangle(3, 0, 2, 0, 70, 130);

    // Set the placement of the rectangle
    rectangle.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    rectangle.GetLine().SetWeight(4);

    // Set the dash style of the rectangle
    rectangle.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the Excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "Rectangle shape added and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aggiunta del controllo Arco al foglio di lavoro**

Aspose.Cells ti consente di disegnare forme ad arco nei tuoi fogli di lavoro. Puoi creare archi semplici e riempiti. Ti è consentito formattare il colore di riempimento e il colore della linea di bordo del controllo. Ad esempio, puoi specificare/cambiare il colore dell'arco, impostare il colore di sfondo, specificare lo spessore e lo stile della forma per le tue esigenze.

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Arco** in **Forme automatiche**.
1. Trascina per disegnare l'arco.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddArc**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addarc/), che viene utilizzato per aggiungere una forma ad arco a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/). La classe [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) rappresenta un arco. Ha alcuni membri importanti:

- La proprietà [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) specifica gli attributi del formato della linea di una forma ad arco.
- La proprietà [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) specifica il [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), il modo in cui l'arco è collegato alle celle nel foglio di lavoro.
- La proprietà [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) specifica gli stili del formato di riempimento della forma.
- La proprietà [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) specifica l'indice della riga dell'angolo in basso a destra.
- La proprietà [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) specifica l'indice della colonna dell'angolo in basso a destra.

L'esempio seguente mostra come aggiungere forme ad arco al foglio di lavoro. L'esempio crea due forme ad arco: una è riempita e l'altra è semplice.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Add an arc shape
    ArcShape arc1 = worksheet.GetShapes().AddArc(2, 0, 2, 0, 130, 130);

    // Set the fill shape color
    arc1.GetFill().SetFillType(FillType::Solid);
    arc1.GetFill().GetSolidFill().SetColor(Color::Blue());

    // Set the placement of the arc
    arc1.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    arc1.GetLine().SetWeight(1);

    // Set the dash style of the arc
    arc1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another arc shape
    ArcShape arc2 = worksheet.GetShapes().AddArc(9, 0, 2, 0, 130, 130);

    // Set the line color
    arc2.GetLine().SetFillType(FillType::Solid);
    arc2.GetLine().GetSolidFill().SetColor(Color::Blue());

    // Set the placement of the arc
    arc2.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    arc2.GetLine().SetWeight(1);

    // Set the dash style of the arc
    arc2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    U16String outputPath = outDir + u"book1.out.xls";
    excelbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aggiunta del controllo ovale a un foglio di lavoro**

Aspose.Cells consente di disegnare forme ovali nei fogli di lavoro. Creare forme ovali semplici e riempite e formattare il colore di riempimento e il colore della linea di bordo del controllo. Ad esempio, è possibile specificare / cambiare il colore dell'ovale, impostare il colore dell'ombreggiatura, specificare il peso e lo stile della forma.

### **Utilizzando Microsoft Excel**

- Nella barra degli strumenti *Disegno*, fare clic su *Ovale*.
- Trascina per disegnare l'ovale.
- Fare uno o entrambi i seguenti:
- Per vincolare l'ovale nel disegnare un cerchio dal suo punto di partenza, tenere premuto SHIFT mentre trascini.
- Per disegnare un ovale da un punto centrale, tenere premuto CTRL mentre trascini.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddOval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addoval/), che viene utilizzato per aggiungere una forma ovale a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/). La classe [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) rappresenta una forma ovale. Ha alcuni membri importanti:

- La proprietà [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) specifica gli attributi del formato della linea di una forma ovale.
- La proprietà [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) specifica il [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), il modo in cui l'ovale è collegato alle celle nel foglio di lavoro.
- La proprietà [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) specifica gli stili del formato di riempimento della forma.
- La proprietà [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) specifica l'indice della riga dell'angolo in basso a destra.
- La proprietà [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) specifica l'indice della colonna dell'angolo in basso a destra.

L'esempio seguente mostra come aggiungere forme ovali al foglio di lavoro. L'esempio crea due forme ovali: una è una forma ovale piena, l'altra è un semplice cerchio.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add an oval shape
    Oval oval1 = excelbook.GetWorksheets().Get(0).GetShapes().AddOval(2, 0, 2, 0, 130, 160);

    // Set the placement of the oval
    oval1.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    oval1.GetLine().SetWeight(1);

    // Set the dash style of the oval
    oval1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another oval (circle) shape
    Oval oval2 = excelbook.GetWorksheets().Get(0).GetShapes().AddOval(9, 0, 2, 15, 130, 130);

    // Set the placement of the oval
    oval2.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    oval2.GetLine().SetWeight(1);

    // Set the dash style of the oval
    oval2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Aggiunta del controllo Spinner al foglio di lavoro**

Una casella di testo è un riquadro di testo collegato a un pulsante (chiamato pulsante di scorrimento) composto da una freccia su e una freccia giù che è possibile fare clic per modificare incrementalmente il valore nella casella di testo. Utilizzando le caselle di testo, è possibile vedere come le modifiche all'input del modello finanziario altereranno gli output del modello. È possibile collegare un pulsante di scorrimento a una cella di input specifica. Quando si fa clic sulla freccia su o giù sul pulsante di scorrimento, il valore intero nella cella di input mirata aumenta o diminuisce. *Aspose.Cells* consente di creare spinner nei fogli di lavoro.

### **Utilizzando Microsoft Excel**

Per inserire un controllo casella di scorrimento nel tuo foglio di lavoro:

- Assicurati che la barra degli strumenti *Forme* sia visualizzata.
- Fare clic sull'opzione *Spinner*.
- Nell'area del foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà lo spinner.
- Una volta inserito lo spinner nel foglio di lavoro, fare clic con il pulsante destro del mouse sul controllo e fare clic su *Formatta controllo* e specificare i valori massimo, minimo e incrementale.
- Nel campo *Collegamento cella* specificare l'indirizzo della cella a cui dovrebbe essere collegata questa casella di scorrimento.
- Fare clic su *OK*.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddSpinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addspinner/), che viene utilizzato per aggiungere un controllo casella di scorrimento a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/). La classe [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) rappresenta una casella di scorrimento. Ha alcuni membri importanti:

- La proprietà [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) specifica una cella collegata alla casella di scorrimento.
- La proprietà [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmax/) specifica il valore massimo per l'intervallo della casella di scorrimento.
- La proprietà [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmin/) specifica il valore minimo per l'intervallo della casella di scorrimento.
- La proprietà [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getincrementalchange/) specifica l'importo del valore con cui viene incrementato uno spinner a una riga di scorrimento.
- La proprietà [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getshadow/) indica se la casella di scorrimento ha ombreggiature 3D.
- La proprietà [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getcurrentvalue/) specifica il valore corrente della casella di scorrimento.

L'esempio seguente mostra come aggiungere una casella di scorrimento al foglio di lavoro.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Get the worksheet cells
    Cells cells = worksheet.GetCells();

    // Input a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Select Value:");

    // Set the font color of the cell
    Style styleA1 = cells.Get(u"A1").GetStyle();
    styleA1.GetFont().SetColor(Color::Red());

    // Set the font text bold
    styleA1.GetFont().SetIsBold(true);

    // Input value into A2 cell
    cells.Get(u"A2").PutValue(0);

    // Set the shading color to black with solid background
    Style styleA2 = cells.Get(u"A2").GetStyle();
    styleA2.SetForegroundColor(Color::Black());
    styleA2.SetPattern(BackgroundType::Solid);

    // Set the font color of the cell
    styleA2.GetFont().SetColor(Color::White());

    // Set the font text bold
    styleA2.GetFont().SetIsBold(true);

    // Add a spinner control
    Spinner spinner = worksheet.GetShapes().AddSpinner(1, 0, 1, 0, 20, 18);

    // Set the placement type of the spinner
    spinner.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell for the control
    spinner.SetLinkedCell(u"A2");

    // Set the maximum value
    spinner.SetMax(10);

    // Set the minimum value
    spinner.SetMin(0);

    // Set the incremental change for the control
    spinner.SetIncrementalChange(2);

    // Set it 3-D shading
    spinner.SetShadow(true);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aggiunta di un controllo barra di scorrimento a un foglio di lavoro**

Un controllo barra di scorrimento viene utilizzato per aiutare a selezionare dati in un foglio di lavoro in modo simile a un controllo spin box. Aggiungendo il controllo a un foglio di lavoro e collegandolo a una cella, è possibile restituire un valore numerico per la posizione corrente del controllo.

### **Utilizzando Microsoft Excel**

- Per aggiungere una barra di scorrimento in Excel 2003 e nelle versioni precedenti, fare clic sul pulsante *Barra di scorrimento* nella barra degli strumenti *Forme*, e quindi creare una barra di scorrimento che copra le celle da B2 a B6 in altezza e sia larga circa un quarto della larghezza della colonna.
- Per aggiungere una barra di scorrimento in Excel 2007, fare clic sulla scheda *Sviluppatore*, fare clic su *Inserisci* e quindi fare clic su *Barra di scorrimento* nella sezione Controlli modulo.
- Fare clic con il pulsante destro del mouse sulla barra di scorrimento e quindi fare clic su *Formato controllo*.
- Immettere le seguenti informazioni e fare clic su *OK*:
  - Nella casella *Valore corrente*, digitare 1.
  - Nella casella *Valore minimo*, digitare 1. Questo valore limita la parte superiore della barra di scorrimento al primo elemento nella lista.
  - Nella casella *Valore massimo*, digitare 20. Questo numero specifica il numero massimo di voci nella lista.
  - Nella casella *Cambiamento incrementale*, digitare 1. Questo valore controlla quanti numeri il controllo barra di scorrimento incrementa il valore corrente.
  - Nella casella *Cambio pagina*, digitare 5. Questa voce controlla di quanto verrà incrementato il valore corrente se si fa clic all'interno della barra di scorrimento su uno dei lati della casella di scorrimento.
  - Per inserire un valore numerico nella cella G1 (a seconda dell'elemento selezionato nell'elenco), digitare G1 nella casella *Collegamento cella*.
- Fare clic su qualsiasi cella in modo che la barra di scorrimento non sia selezionata.

Quando si fa clic sul controllo su o giù nella barra di scorrimento, la cella G1 viene aggiornata con un numero che indica il valore corrente della barra di scorrimento aumentato o diminuito del cambio incrementale della barra di scorrimento.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addscrollbar/), che viene utilizzato per aggiungere un controllo barra di scorrimento al foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/). La classe [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) rappresenta una barra di scorrimento. Ha alcuni membri importanti:

- La proprietà [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) specifica una cella collegata alla barra di scorrimento.
- La proprietà [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmax/) specifica il valore massimo per l'intervallo della barra di scorrimento.
- La proprietà [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmin/) specifica il valore minimo per l'intervallo della barra di scorrimento.
- La proprietà [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getincrementalchange/) specifica l'ammontare del valore per il quale una barra di scorrimento viene incrementata di uno scroll di riga.
- La proprietà [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getshadow/) indica se la barra di scorrimento ha un ombreggiatura 3D.
- La proprietà [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getcurrentvalue/) specifica il valore corrente della barra di scorrimento.
- La proprietà [**GetPageChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getpagechange/) specifica di quanto verrà incrementato il valore corrente se si fa clic all'interno della barra di scorrimento su uno dei due lati della casella di scorrimento.

L'esempio seguente mostra come aggiungere una barra di scorrimento al foglio di lavoro.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Invisible the gridlines of the worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Get the worksheet cells
    Cells cells = worksheet.GetCells();

    // Input a value into A1 cell
    cells.Get(u"A1").PutValue(1);

    // Set the font color of the cell
    cells.Get(u"A1").GetStyle().GetFont().SetColor(Color::Maroon());

    // Set the font text bold
    cells.Get(u"A1").GetStyle().GetFont().SetIsBold(true);

    // Set the number format
    cells.Get(u"A1").GetStyle().SetNumber(1);

    // Add a scrollbar control
    ScrollBar scrollbar = worksheet.GetShapes().AddScrollBar(0, 0, 1, 0, 125, 20);

    // Set the placement type of the scrollbar
    scrollbar.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell for the control
    scrollbar.SetLinkedCell(u"A1");

    // Set the maximum value
    scrollbar.SetMax(20);

    // Set the minimum value
    scrollbar.SetMin(1);

    // Set the incr. change for the control
    scrollbar.SetIncrementalChange(1);

    // Set the page change attribute
    scrollbar.SetPageChange(5);

    // Set it 3-D shading
    scrollbar.SetShadow(true);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "Scrollbar added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aggiunta di un controllo GroupBox ai controlli di gruppo in un foglio di lavoro**

A volte è necessario implementare pulsanti di opzione o altri controlli che appartengono a un certo gruppo, è possibile farlo includendo un controllo group box o un rettangolo. Uno di questi due oggetti funzionerebbe come delimitatore del gruppo. Dopo aver aggiunto una di queste forme, è possibile aggiungere due o più pulsanti di opzione o altri oggetti di gruppo.

### **Utilizzando Microsoft Excel**

Per inserire un controllo di group box nel foglio di lavoro e inserire i controlli al suo interno:

- Per avviare un modulo, nel menu principale, fare clic su *Visualizza*, seguito da *Barre degli strumenti* e *Moduli*.
- Sulla barra degli strumenti *Moduli*, fare clic su *GroupBox* e disegnare un rettangolo sul foglio di lavoro.
- Digitare una stringa di didascalia per la casella.
- Sulla barra degli strumenti *Moduli*, fare clic su *Pulsante di opzione* e fare clic all'interno del *GroupBox* appena sotto la stringa di didascalia.
- Dalla barra degli strumenti *Moduli* nuovamente, fare clic su *Pulsante di opzione* e fare clic all'interno del *GroupBox* sotto il primo pulsante di opzione.
- Ancora una volta sulla barra degli strumenti *Moduli*, fare clic su *Pulsante di opzione* e fare clic all'interno del *GroupBox* sotto il pulsante di opzione precedente.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddGroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addgroupbox/), che viene utilizzato per aggiungere un controllo di group box al foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/). Inoltre, il metodo [**Group**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/group/) della classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) raggruppa le forme, prende un array [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) come parametro e restituisce un oggetto [**GroupShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupshape/). La classe [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/) rappresenta una casella di gruppo. Ha alcuni membri importanti:

- La proprietà [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) specifica la stringa di didascalia della casella di gruppo.
- La proprietà [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/getshadow/) indica se la casella di gruppo ha sfumature in 3D.

L'esempio seguente mostra come aggiungere una casella di gruppo e raggruppare i controlli nel foglio di lavoro.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add a group box to the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);
    GroupBox box = worksheet.GetShapes().AddGroupBox(1, 0, 1, 0, 300, 250);

    // Set the caption of the group box
    box.SetText(u"Age Groups");
    box.SetPlacement(PlacementType::FreeFloating);

    // Make it 2-D box
    box.SetShadow(false);

    // Add a radio button
    RadioButton radio1 = worksheet.GetShapes().AddRadioButton(3, 0, 2, 0, 30, 110);

    // Set its text string
    radio1.SetText(u"20-29");

    // Set A1 cell as a linked cell for the radio button
    radio1.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio1.SetShadow(true);

    // Set the weight of the radio button
    radio1.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another radio button
    RadioButton radio2 = worksheet.GetShapes().AddRadioButton(6, 0, 2, 0, 30, 110);

    // Set its text string
    radio2.SetText(u"30-39");

    // Set A1 cell as a linked cell for the radio button
    radio2.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio2.SetShadow(true);

    // Set the weight of the radio button
    radio2.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another radio button
    RadioButton radio3 = worksheet.GetShapes().AddRadioButton(9, 0, 2, 0, 30, 110);

    // Set its text string
    radio3.SetText(u"40-49");

    // Set A1 cell as a linked cell for the radio button
    radio3.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio3.SetShadow(true);

    // Set the weight of the radio button
    radio3.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio3.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Get the shapes
    Vector<Shape> shapeobjects{ box, radio1, radio2, radio3 };

    // Group the shapes
    GroupShape group = worksheet.GetShapes().Group(shapeobjects);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Aggiungi controlli ActiveX utilizzando Aspose.Cells](/cells/it/cpp/add-activex-controls-using-aspose-cells/)
- [Rimuovi controllo ActiveX](/cells/it/cpp/remove-activex-control/)
- [Aggiorna il controllo ComboBox ActiveX](/cells/it/cpp/update-activex-combobox-control/)
{{< app/cells/assistant language="cpp" >}}
