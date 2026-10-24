---
title: Proteggere e rimuovere la protezione
linktitle: Crittografia e protezione
type: docs
weight: 68
url: /it/net/protect-and-unprotect/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/net/security-features/]
description: Questa sezione illustra come crittografare e decrittografare i file Excel e proteggere i dati Excel, trattando la crittografia dei file, la protezione in sola lettura, la protezione della struttura della cartella di lavoro, la protezione dei fogli di lavoro e le firme digitali tramite codice C#
keywords: Aspose.Cells, .NET, crittografare, decrittografare, password, proteggere, rimuovere la protezione, protezione cartella di lavoro, protezione foglio di lavoro, sola lettura, firma digitale, C#
---

Le cartelle di lavoro Excel spesso contengono informazioni finanziarie, aziendali o personali sensibili che devono essere protette dagli accessi non autorizzati. Aspose.Cells for .NET fornisce un set completo di funzionalità di protezione che rispecchia le capacità di Microsoft Excel, consentendo di proteggere i dati a livello di file, a livello di cartella di lavoro e a livello di foglio di lavoro.

{{% alert color="primary" %}}
Aspose.Cells for .NET offre un'ampia gamma di funzionalità di protezione, dal livello di file al livello di dati, simile a MS Excel. Queste funzionalità includono la crittografia dei file con una password, l'applicazione dell'accesso in sola lettura tramite una password per modificare, la protezione della struttura della cartella di lavoro, la protezione dei fogli di lavoro e la firma digitale delle cartelle di lavoro.
{{% /alert %}}

## Crittografare e decrittografare i file Excel
Una password impostata su un file Excel impedisce agli utenti non autorizzati di aprire o visualizzare il contenuto della cartella di lavoro. Per crittografare una cartella di lavoro, assegnare una stringa di password a `Workbook.Settings.Password` e quindi salvare la cartella di lavoro. Aspose.Cells scrive il file in forma crittografata. Per aprire una cartella di lavoro crittografata per la decrittografia, creare un'istanza di un oggetto `LoadOptions`, impostare `LoadOptions.Password` sulla stessa password utilizzata durante la crittografia e passarlo al costruttore `Workbook`. Aspose.Cells applica la password fornita in modo trasparente, consentendo al resto del codice di interagire con il contenuto decrittografato come se il file fosse una normale cartella di lavoro.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cell cell = sheet.Cells["A1"];
cell.PutValue("Confidential Data");
workbook.Settings.Password = "OpenPassword123";
workbook.Save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.Password = "OpenPassword123";
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
Console.WriteLine("Decrypted cell A1 value: " + decryptedWorkbook.Worksheets[0].Cells["A1"].StringValue);
```

## Protezione in sola lettura (password per modificare)
Excel supporta due livelli distinti di password. Il primo è una password per aprire, che crittografa il file stesso ed è trattato nella sezione precedente. Il secondo è una password per modificare, che non impedisce agli utenti di aprire la cartella di lavoro; Excel consiglia invece di aprire il file in modalità di sola lettura a meno che non venga fornita la password per modificare. Configurare questo comportamento in Aspose.Cells tramite `Workbook.Settings.WriteProtection`. Impostare la sua proprietà `Password` sulla password per modificare e la sua proprietà `Author` per identificare chi ha applicato la protezione. Utilizzare il metodo `WriteProtection.ValidatePassword(string)` per verificare se una password per modificare fornita è corretta, restituendo `true` in caso di corrispondenza e `false` altrimenti.

```csharp
using System;
using Aspose.Cells;
// Crea una nuova cartella di lavoro da zero
Workbook workbook = new Workbook();
// Scrivi un valore di esempio nella cella A1 del primo foglio di lavoro
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Data");
// Configura la protezione in scrittura: imposta la password per modificare e l'autore
workbook.Settings.WriteProtection.Password = "ModifyPwd";
workbook.Settings.WriteProtection.Author = "AuthorName";
// Salva la cartella di lavoro in modo che la protezione in scrittura venga mantenuta
workbook.Save("WriteProtectedWorkbook.xlsx");
// Convalida la password per modificare utilizzando la password corretta
bool isCorrectValid = workbook.Settings.WriteProtection.ValidatePassword("ModifyPwd");
Console.WriteLine("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Convalida la password per modificare utilizzando una password errata per dimostrare l'altro ramo
bool isWrongValid = workbook.Settings.WriteProtection.ValidatePassword("WrongPwd");
Console.WriteLine("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Proteggere e rimuovere la protezione della struttura della cartella di lavoro
La protezione della struttura della cartella di lavoro impedisce ad altri utenti di visualizzare fogli di lavoro nascosti, aggiungere nuovi fogli di lavoro, spostare fogli di lavoro, eliminare fogli di lavoro, nascondere fogli di lavoro o rinominare fogli di lavoro. Lo stato protetto si applica alla struttura del foglio anziché al contenuto delle celle all'interno di qualsiasi foglio. Per applicare la protezione della struttura, chiamare `workbook.Protect(ProtectionType.Structure, "password")`. Per rimuovere la protezione, chiamare `workbook.Unprotect("password")` e fornire la password corretta. Il valore enum `ProtectionType.Structure` viene utilizzato qui ed è distinto da altri tipi di protezione come `ProtectionType.Windows`.

```csharp
using System;
using Aspose.Cells;
// Crea una nuova cartella di lavoro
Workbook workbook = new Workbook();
// Aggiungi un secondo foglio di lavoro
workbook.Worksheets.Add();
// Scrivi un valore di esempio nella cella A1 del primo foglio di lavoro
workbook.Worksheets[0].Cells[0, 0].PutValue("Sample Data");
// Proteggi la struttura della cartella di lavoro
workbook.Protect(ProtectionType.Structure, "StructPwd");
// Salva la cartella di lavoro come structure_protected.xlsx
string filePath = "structure_protected.xlsx";
workbook.Save(filePath);
// Ricarica il file in una nuova istanza di Workbook
Workbook loadedWorkbook = new Workbook(filePath);
// Rimuovi la protezione della struttura
loadedWorkbook.Unprotect("StructPwd");
// Stampa il messaggio di conferma
Console.WriteLine("Structure protection has been successfully removed from the workbook.");
```

## Proteggere e rimuovere la protezione dei fogli di lavoro
La protezione del foglio di lavoro blocca le celle di un foglio di lavoro contro modifiche accidentali o intenzionali. Gli utenti non possono modificare le celle bloccate senza fornire la password. Questa è la protezione tipica utilizzata per proteggere formule, intestazioni o aree di immissione dati designate nei fogli di calcolo condivisi. Per proteggere un foglio di lavoro, chiamare `worksheet.Protect(ProtectionType.All, "password")`. L'uso di `ProtectionType.All` abilita ogni opzione di protezione disponibile come la selezione di celle bloccate, la formattazione delle celle, l'inserimento di righe e colonne e l'eliminazione di righe e colonne. Per rimuovere la protezione, chiamare `worksheet.Unprotect("password")` con la password corretta. Un controllo più granulare è disponibile combinando altri tipi di protezione come `Contents`, `Objects` e `Scenarios` utilizzando l'OR bit per bit.

```csharp
using System;
using Aspose.Cells;
var workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
sheet.Cells["A1"].PutValue("Sample Data");
sheet.Protect(ProtectionType.All, "SheetPwd");
workbook.Save("sheet_protected.xlsx");
var workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.Worksheets[0];
sheetReloaded.Unprotect("SheetPwd");
Console.WriteLine("Worksheet protection removed successfully.");
```

## Aggiungere e convalidare le firme digitali
Una firma digitale garantisce ai destinatari che il contenuto della cartella di lavoro sia autentico e non sia stato alterato da quando è stato firmato. Aspose.Cells fornisce il supporto per le firme digitali tramite il namespace `Aspose.Cells.DigitalSignatures`. Il flusso di lavoro tipico carica un file di certificato `.pfx` tramite `System.Security.Cryptography.X509Certificates.X509Certificate2`, lo racchiude in un `Aspose.Cells.DigitalSignatures.DigitalSignature`, aggiunge la firma a un `DigitalSignatureCollection` e applica la raccolta alla cartella di lavoro tramite `Workbook.AddDigitalSignature(DigitalSignatureCollection)`. La proprietà `DigitalSignature.Comments` può registrare il contesto della firma come l'ora e lo scopo della firma. Qualsiasi modifica apportata alla cartella di lavoro dopo la firma invalida la firma, quindi un passaggio di convalida sul lato ricevente può rilevare le manomissioni.

```csharp
using System;
using System.IO;
using System.Security.Cryptography.X509Certificates;
using Aspose.Cells;
using Aspose.Cells.DigitalSignatures;
X509Certificate2 certificate = new X509Certificate2("signature.pfx", "pfx-password");
DigitalSignature signature = new DigitalSignature(certificate, "Signed by Aspose.Cells", DateTime.Now);
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.Add(signature);
Workbook workbook = new Workbook();
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Value");
workbook.AddDigitalSignature(signatures);
workbook.Save("signed_workbook.xlsx");
Console.WriteLine("The workbook has been digitally signed.");
```

## Articoli correlati
- [Crittografare e decrittografare i file Excel](/cells/it/net/encrypt-and-decrypt-excel-files/)
- [Proteggere e rimuovere la protezione della struttura della cartella di lavoro](/cells/it/net/protect-and-unprotect-workbook-structure/)
- [Proteggere e rimuovere la protezione del foglio di lavoro](/cells/it/net/protect-and-unprotect-worksheets/)
- [Proteggere con password o rimuovere la protezione della cartella di lavoro condivisa](/cells/it/net/password-protect-or-unprotect-the-shared-workbook/)
- [Assegnare e convalidare le firme digitali](/cells/it/net/assign-and-validate-digital-signatures/)
- [Verificare la password per modificare utilizzando Aspose.Cells](/cells/it/net/check-password-to-modify-using-aspose-cells/)
- [Rilevare il formato di file di Office Open XML crittografati - file OOXML](/cells/it/net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Crittografia dei file Excel](/cells/it/net/encrypting-excel-files/)
- [Come rilevare un formato di file e verificare se il file è crittografato](/cells/it/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="csharp" >}}