---
title: Impostare intestazioni e piè di pagina con C++
linktitle: Impostazione Intestazioni e piè di pagina
type: docs
weight: 30
url: /it/cpp/setting-headers-and-footers/
description: Questo articolo spiega come inserire programmativamente un immagine nell intestazione e nel piè di pagina dei fogli di lavoro Excel impostando le intestazioni e i piè di pagina con comandi script utilizzando l API o la libreria C++.
keywords: inserire immagine intestazione piè di pagina Excel C++, impostare comandi script intestazione piè di pagina C++
---

{{% alert color="primary" %}}

Le intestazioni e i piè di pagina sono le linee di testo visualizzate sotto il margine superiore o sopra il margine inferiore rispettivamente. È possibile aggiungere intestazioni e piè di pagina anche ai fogli di lavoro. Le intestazioni e i piè di pagina possono essere utilizzati per visualizzare informazioni utili come il numero di pagina, il nome dell'autore, il nome del tema o la data e l'ora. Le intestazioni e i piè di pagina sono gestiti utilizzando le impostazioni della pagina di setup.

{{% /alert %}}

## **Impostazione di intestazioni e piè di pagina**

Aspose.Cells consente di aggiungere intestazioni e piè di pagina ai fogli di lavoro in fase di esecuzione, ma consigliamo di impostare manualmente le intestazioni e i piè di pagina in un file pre-progettato per la stampa. È possibile utilizzare Microsoft Excel come strumento GUI per impostare le intestazioni e i piè di pagina per risparmiare sforzi e tempo di sviluppo. Aspose.Cells può importare il file e salvare le impostazioni.

Per aggiungere intestazioni e piè di pagina in fase di esecuzione, Aspose.Cells fornisce chiamate API speciali e comandi di script per formattare intestazioni e piè di pagina.

### **Comandi di script**

I comandi di script sono comandi speciali che consentono di impostare la formattazione di intestazioni e piè di pagina.

|**Comandi di script**|**Descrizione**|
| :- | :- |
|&P|Numero di pagina corrente|
|&G|Un'immagine|
|&N|Il numero totale di pagine|
|&D|La data corrente|
|&T|L'orario corrente|
|&A|Il nome del foglio di lavoro|
|&F|Il nome del file senza percorso|
|&&Testo|Mostra &Testo. Per esempio: &&WO sarà visualizzato come &WO|
|&"\<FontName>"|Rappresenta un nome di carattere. Ad esempio: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Rappresenta il nome del carattere con lo stile. Ad esempio: &"Arial,Grassetto"|
|&\<FontSize>|Rappresenta la dimensione del carattere. Ad esempio: “&14abc”. Ma, se questo comando è seguito da un numero normale da stampare nell'intestazione, questo dovrebbe essere separato da un carattere spazio dalla dimensione del carattere. Ad esempio: “&14 123”.|

### **Imposta Intestazioni e Piè di Pagina**

La classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) fornisce due metodi, [**SetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheader/) e [**SetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooter/), utilizzati per aggiungere un'intestazione e un piè di pagina a un foglio di lavoro. Questi metodi richiedono solo due parametri:

- **Sezione** – la sezione in cui dovrebbe essere posizionata l'intestazione o il piè di pagina. Ci sono tre sezioni: sinistra, centro e destra, rappresentate rispettivamente da 0, 1 e 2.
- **Script** – lo script da utilizzare per l'intestazione o il piè di pagina. Questo script contiene comandi di script per formattare l'intestazione o il piè di pagina.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook excel;

    // Get the first worksheet's PageSetup
    PageSetup pageSetup = excel.GetWorksheets().Get(0).GetPageSetup();

    // Set worksheet name at the left section of the header
    pageSetup.SetHeader(0, u"&A");

    // Set current date and time at the central section of the header with custom font
    pageSetup.SetHeader(1, u"&\"Times New Roman,Bold\"&D-&T");

    // Set current file name at the right section of the header with custom font
    pageSetup.SetHeader(2, u"&\"Times New Roman,Bold\"&12&F");

    // Set a string at the left section of the footer with custom font for part of the string
    pageSetup.SetFooter(0, u"Hello World! &\"Courier New\"&14 123");

    // Set the current page number at the central section of the footer
    pageSetup.SetFooter(1, u"&P");

    // Set page count at the right section of the footer
    pageSetup.SetFooter(2, u"&N");

    // Save the workbook
    excel.Save(u"SetHeadersAndFooters_out.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Inserire un'immagine nell'intestazione o nel piè di pagina**

La classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) ha due metodi aggiuntivi, [**SetHeaderPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheaderpicture/) e [**SetFooterPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooterpicture/), utilizzati per aggiungere immagini all'intestazione e al piè di pagina. Questi metodi accettano i parametri:

- **Sezione** – la sezione dell'intestazione o del piè di pagina in cui verrà posizionata l'immagine. Ci sono tre sezioni, sinistra, centro e destra, rappresentate dai valori 0, 1 e 2 rispettivamente.
- **Array di byte** – i dati grafici (i dati binari devono essere scritti nel buffer di un array di byte).

Dopo aver eseguito il codice sottostante e aperto il file, controlla l'intestazione del foglio di lavoro:

1. Nel menu **File**, seleziona **Imposta pagina**. Verrà visualizzata una finestra di dialogo.
1. Seleziona la scheda **Intestazione/Piè di pagina**.

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Creating a Workbook object
    Workbook workbook;

    // Creating a string variable to store the url of the logo/picture
    U16String logo_url = srcDir + u"aspose-logo.jpg";

    // Declaring a FileStream object
    ifstream inFile;

    // Declaring a byte array
    vector<uint8_t> binaryData;

    // Opening the logo/picture in the stream
    inFile.open(logo_url.ToUtf8(), ios::binary);

    if (inFile.is_open())
    {
        // Get the size of the file
        inFile.seekg(0, ios::end);
        size_t fileSize = inFile.tellg();
        inFile.seekg(0, ios::beg);

        // Resize the byte array to the size of the file
        binaryData.resize(fileSize);

        // Read the file into the byte array
        inFile.read(reinterpret_cast<char*>(binaryData.data()), fileSize);

        // Creating a PageSetup object to get the page settings of the first worksheet of the workbook
        PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

        // Convert std::vector to Aspose::Cells::Vector
        Aspose::Cells::Vector<uint8_t> asposeBinaryData(binaryData.data(), static_cast<int32_t>(binaryData.size()));

        // Setting the logo/picture in the central section of the page header
        pageSetup.SetHeaderPicture(1, asposeBinaryData);

        // Setting the script for the logo/picture
        pageSetup.SetHeader(1, u"&G");

        // Setting the Sheet's name in the right section of the page header with the script
        pageSetup.SetHeader(2, u"&A");

        // Saving the workbook
        workbook.Save(outDir + u"InsertImageInHeaderFooter_out.xls");

        // Closing the FileStream object
        inFile.close();
    }
    else
    {
        cerr << "Failed to open the image file." << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
