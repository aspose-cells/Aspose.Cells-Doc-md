---
title: Proteggi e Rimuovi protezione con C++
linktitle: Crittografia e protezione
type: docs
weight: 68
url: /it/cpp/protect-and-unprotect/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/cpp/security-features/]
description: Questa sezione illustra come crittografare e decrittografare i file Excel e proteggere i dati Excel, trattando la crittografia dei file, la protezione in sola lettura, la protezione della struttura della cartella di lavoro, la protezione del foglio di lavoro e le firme digitali tramite codice C++
keywords: Aspose.Cells, Aspose.Cells for C++, crittografare, decrittografare, password, proteggere, rimuovere la protezione, protezione cartella di lavoro, protezione foglio di lavoro, sola lettura, firma digitale, C++
---

Le cartelle di lavoro Excel spesso archiviano informazioni finanziarie, aziendali o personali sensibili che devono essere protette dall'accesso non autorizzato. Aspose.Cells for C++ fornisce un set completo di funzionalità di protezione che rispecchia le capacità di Microsoft Excel, consentendo di proteggere i dati a livello di file, di cartella di lavoro e di foglio di lavoro.

{{% alert color="primary" %}}
Aspose.Cells for C++ offre un'ampia gamma di funzionalità di protezione, dal livello di file al livello di dati, simile a MS Excel. Queste funzionalità includono la crittografia dei file con una password, l'applicazione dell'accesso in sola lettura tramite una password per modificare, la protezione della struttura della cartella di lavoro, la protezione dei fogli di lavoro e la firma digitale delle cartelle di lavoro.
{{% /alert %}}

## Crittografare e decrittografare i file Excel
Una password impostata su un file Excel impedisce agli utenti non autorizzati di aprire o visualizzare il contenuto della cartella di lavoro. Per crittografare una cartella di lavoro, assegnare una stringa di password a `workbook.GetSettings().SetPassword()` e quindi salvare la cartella di lavoro. Aspose.Cells scrive il file in forma crittografata. Per aprire una cartella di lavoro crittografata per la decrittografia, istanziare un oggetto `LoadOptions`, impostare `LoadOptions.SetPassword()` sulla stessa password utilizzata durante la crittografia e passarlo al costruttore `Workbook`. Aspose.Cells applica la password fornita in modo trasparente, così che il resto del codice possa interagire con il contenuto decrittografato come se il file fosse una normale cartella di lavoro.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(u"Confidential Data");
    workbook.GetSettings().SetPassword(U16String("OpenPassword123"));
    workbook.Save(u"encrypted.xlsx");
    LoadOptions loadOptions;
    loadOptions.SetPassword(U16String("OpenPassword123"));
    Workbook decryptedWorkbook(u"encrypted.xlsx", loadOptions);
    U16String cellValue = decryptedWorkbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue();
    std::cout << "Decrypted cell A1 value: " << cellValue.ToUtf8() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Protezione in sola lettura (password per modificare)
Excel supporta due distinti livelli di password. Il primo è la password di apertura, che crittografa il file stesso ed è trattato nella sezione precedente. Il secondo è la password per modificare, che non impedisce agli utenti di aprire la cartella di lavoro; Excel consiglia invece di aprire il file in modalità di sola lettura a meno che non venga fornita la password per modificare. Configurare questo comportamento in Aspose.Cells tramite `workbook.GetSettings().GetWriteProtection()`. Impostare la sua proprietà `Password` sulla password per modificare e la proprietà `Author` per identificare chi ha applicato la protezione. Usare il metodo `WriteProtection.ValidatePassword()` per verificare se una password per modificare fornita è corretta, restituendo `true` in caso di corrispondenza e `false` altrimenti.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    Cell a1 = cells.Get(u"A1");
    a1.PutValue(u"Sample Data");
    workbook.GetSettings().GetWriteProtection().SetPassword(u"ModifyPwd");
    workbook.GetSettings().GetWriteProtection().SetAuthor(u"AuthorName");
    workbook.Save(u"WriteProtectedWorkbook.xlsx");
    bool isCorrectValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"ModifyPwd");
    std::cout << "ValidatePassword(\"ModifyPwd\") returned: " << (isCorrectValid ? "True" : "False") << std::endl;
    bool isWrongValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"WrongPwd");
    std::cout << "ValidatePassword(\"WrongPwd\") returned: " << (isWrongValid ? "True" : "False") << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Proteggere e rimuovere la protezione della struttura della cartella di lavoro
La protezione della struttura della cartella di lavoro impedisce ad altri utenti di visualizzare fogli di lavoro nascosti, aggiungere nuovi fogli di lavoro, spostare fogli di lavoro, eliminare fogli di lavoro, nascondere fogli di lavoro o rinominare fogli di lavoro. Lo stato protetto si applica alla struttura dei fogli piuttosto che al contenuto delle celle all'interno di qualsiasi foglio. Per applicare la protezione della struttura, chiamare `workbook.Protect(ProtectionType::Structure, "password")`. Per rimuovere la protezione, chiamare `workbook.Unprotect("password")` e fornire la password corretta. Il valore enum `ProtectionType::Structure` è usato qui ed è distinto da altri tipi di protezione come `ProtectionType::Windows`.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Crea una nuova cartella di lavoro
    Workbook workbook;
    // Aggiungi un secondo foglio di lavoro
    workbook.GetWorksheets().Add();
    // Scrivi un valore di esempio nella cella A1 del primo foglio di lavoro
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(u"Sample Data");
    // Proteggi la struttura della cartella di lavoro
    workbook.Protect(ProtectionType::Structure, u"StructPwd");
    // Salva la cartella di lavoro come structure_protected.xlsx
    U16String filePath = u"structure_protected.xlsx";
    workbook.Save(filePath);
    // Ricarica il file in una nuova istanza di Workbook
    Workbook loadedWorkbook(filePath);
    // Rimuovi la protezione della struttura
    loadedWorkbook.Unprotect(u"StructPwd");
    // Stampa il messaggio di conferma
    std::cout << "Structure protection has been successfully removed from the workbook." << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Proteggere e rimuovere la protezione dei fogli di lavoro
La protezione del foglio di lavoro blocca le celle di un foglio di lavoro contro modifiche accidentali o deliberate. Gli utenti non possono modificare le celle bloccate senza fornire la password. Questa è la protezione tipica utilizzata per salvaguardare formule, intestazioni o aree designate per l'immissione di dati in fogli di calcolo condivisi. Per proteggere un foglio di lavoro, chiamare `worksheet.Protect(ProtectionType::All, "password")`. L'uso di `ProtectionType::All` abilita ogni opzione di protezione disponibile come la selezione di celle bloccate, la formattazione delle celle, l'inserimento di righe e colonne e l'eliminazione di righe e colonne. Per rimuovere la protezione, chiamare `worksheet.Unprotect("password")` con la password corretta. Un controllo più granulare è disponibile combinando altri tipi di protezione come `Contents`, `Objects` e `Scenarios` tramite OR bit a bit.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Data");
    sheet.Protect(ProtectionType::All, u"SheetPwd");
    workbook.Save(u"sheet_protected.xlsx");
    Workbook workbookReloaded(u"sheet_protected.xlsx");
    Worksheet sheetReloaded = workbookReloaded.GetWorksheets().Get(0);
    sheetReloaded.Unprotect(u"SheetPwd");
    std::cout << "Worksheet protection removed successfully.\n";
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Aggiungere e convalidare le firme digitali
Una firma digitale assicura ai destinatari che il contenuto della cartella di lavoro sia autentico e non sia stato alterato da quando è stato firmato. Aspose.Cells fornisce supporto per le firme digitali tramite il namespace `Aspose::Cells::DigitalSignatures`. Il flusso di lavoro tipico carica un file di certificato `.pfx`, lo racchiude in un `Aspose::Cells::DigitalSignatures::DigitalSignature`, aggiunge la firma a un `DigitalSignatureCollection` e applica la raccolta alla cartella di lavoro tramite `workbook.AddDigitalSignature(DigitalSignatureCollection)`. La proprietà `DigitalSignature.GetComments()` può registrare il contesto della firma come l'ora e lo scopo della firma. Qualsiasi modifica apportata alla cartella di lavoro dopo la firma invalida la firma, quindi un passaggio di convalida sul lato ricevente può rilevare manomissioni.

```cpp
#include "Aspose.Cells.h"
#include <chrono>
#include <ctime>
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;
int main() {
    Aspose::Cells::Startup();
    std::time_t t = std::time(nullptr);
    std::tm tm{};
    localtime_s(&tm, &t);
    Date currentDate{0};
    currentDate.year = tm.tm_year + 1900;
    currentDate.month = tm.tm_mon + 1;
    currentDate.day = tm.tm_mday;
    currentDate.hour = tm.tm_hour;
    currentDate.minute = tm.tm_min;
    currentDate.second = tm.tm_sec;
    DigitalSignature signature(u"signature.pfx", u"pfx-password", u"Signed by Aspose.Cells", currentDate);
    DigitalSignatureCollection signatures;
    signatures.Add(signature);
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Value");
    workbook.AddDigitalSignature(signatures);
    workbook.Save(u"signed_workbook.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Articoli correlati
- [Crittografare e decrittografare i file Excel](/cells/it/cpp/encrypt-and-decrypt-excel-files/)
- [Proteggere e rimuovere la protezione della struttura della cartella di lavoro](/cells/it/cpp/protect-and-unprotect-workbook-structure/)
- [Proteggere e rimuovere la protezione del foglio di lavoro](/cells/it/cpp/protect-and-unprotect-worksheets/)
- [Proteggere con password o rimuovere la protezione della cartella di lavoro condivisa](/cells/it/cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Verificare la password per modificare usando Aspose.Cells](/cells/it/cpp/check-password-to-modify-using-aspose-cells/)
- [Rilevare il formato file dei file Office Open XML crittografati - File OOXML](/cells/it/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Crittografia dei file Excel](/cells/it/cpp/encrypting-excel-files/)
- [Come rilevare un formato di file e verificare se il file è crittografato](/cells/it/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="cpp" >}}