---
title: Crittografia, decrittografia, protezione e protezione dei file di Excel
linktitle: Crittografia e Protezione
type: docs
weight: 68
url: /it/java/protect-and-unprotect/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/java/security-features/]
description: Questa sezione introduce come crittografare e decrittografare i file Excel e proteggere i dati Excel, coprendo la crittografia dei file, la protezione in sola lettura, la protezione della struttura della cartella di lavoro, la protezione dei fogli di lavoro e le firme digitali utilizzando codice Java
keywords: Aspose.Cells, Java, crittografare, decrittografare, password, proteggere, rimuovere la protezione, protezione cartella di lavoro, protezione foglio di lavoro, sola lettura, firma digitale
---

Le cartelle di lavoro di Excel spesso memorizzano informazioni finanziarie, aziendali o personali sensibili che devono essere protette da accessi non autorizzati. Aspose.Cells for Java fornisce un set completo di funzionalità di protezione che rispecchia le capacità di Microsoft Excel, consentendo di proteggere i dati a livello di file, di cartella di lavoro e di foglio di lavoro.

{{% alert color="primary" %}}
Aspose.Cells for Java offre una vasta gamma di funzionalità di protezione, dal livello di file al livello di dati, simile a MS Excel. Queste funzionalità includono la crittografia dei file con una password, l'imposizione dell'accesso in sola lettura tramite una password per modificare, la protezione della struttura della cartella di lavoro, la protezione dei fogli di lavoro e la firma digitale delle cartelle di lavoro.
{{% /alert %}}

## Crittografa e decrittografa i file Excel
Una password impostata su un file Excel impedisce agli utenti non autorizzati di aprire o visualizzare il contenuto della cartella di lavoro. Per crittografare una cartella di lavoro, assegnare una stringa di password a `Workbook.Settings.Password` (accessibile tramite `workbook.getSettings().setPassword(...)`) e poi salvare la cartella di lavoro. Aspose.Cells scrive il file in forma crittografata. Per aprire una cartella di lavoro crittografata per la decrittografia, istanziare un oggetto `LoadOptions`, impostare `LoadOptions.Password` (tramite `loadOptions.setPassword(...)`) sulla stessa password utilizzata durante la crittografia e passarlo al costruttore di `Workbook`. Aspose.Cells applica la password fornita in modo trasparente, così che il resto del codice possa interagire con il contenuto decrittografato come se il file fosse una normale cartella di lavoro.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cell cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.setPassword("OpenPassword123");
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
System.out.println("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Protezione in sola lettura (password per modificare)
Excel supporta due diversi livelli di password. Il primo è una password di apertura, che crittografa il file stesso ed è trattato nella sezione precedente. Il secondo è una password per modificare, che non impedisce agli utenti di aprire la cartella di lavoro; Excel consiglia invece di aprire il file in modalità di sola lettura a meno che non venga fornita la password per modificare. Configurare questo comportamento in Aspose.Cells tramite `Workbook.Settings.WriteProtection` (accessibile tramite `workbook.getSettings().getWriteProtection()`). Impostare la sua proprietà `Password` (tramite `writeProtection.setPassword(...)`) sulla password per modificare e la sua proprietà `Author` (tramite `writeProtection.setAuthor(...)`) per identificare chi ha applicato la protezione. Usare il metodo `WriteProtection.validatePassword(String)` per verificare se una password per modificare fornita è corretta, restituendo `true` in caso di corrispondenza e `false` altrimenti.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
workbook.save("WriteProtectedWorkbook.xlsx");
boolean isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
System.out.println("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
boolean isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
System.out.println("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Proteggi e rimuovi la protezione della struttura della cartella di lavoro
Proteggere la struttura della cartella di lavoro impedisce ad altri utenti di visualizzare fogli di lavoro nascosti, aggiungere nuovi fogli di lavoro, spostare fogli di lavoro, eliminare fogli di lavoro, nascondere fogli di lavoro o rinominare fogli di lavoro. Lo stato protetto si applica alla struttura del foglio anziché al contenuto delle celle all'interno di qualsiasi foglio. Per applicare la protezione della struttura, chiamare `workbook.protect(ProtectionType.STRUCTURE, "password")`. Per rimuovere la protezione, chiamare `workbook.unprotect("password")` e fornire la password corretta. Il valore enum `ProtectionType.STRUCTURE` viene utilizzato qui ed è distinto da altri tipi di protezione come `ProtectionType.WINDOWS`.

```java
import com.aspose.cells.*;
// Crea una nuova cartella di lavoro
Workbook workbook = new Workbook();
// Aggiungi un secondo foglio di lavoro
workbook.getWorksheets().add();
// Scrivi un valore di esempio nella cella A1 del primo foglio di lavoro
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Proteggi la struttura della cartella di lavoro
workbook.protect(ProtectionType.STRUCTURE, "StructPwd");
// Salva la cartella di lavoro come structure_protected.xlsx
String filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Ricarica il file in una nuova istanza di Workbook
Workbook loadedWorkbook = new Workbook(filePath);
// Rimuovi la protezione della struttura
loadedWorkbook.unprotect("StructPwd");
// Stampa il messaggio di conferma
System.out.println("Structure protection has been successfully removed from the workbook.");
```

## Proteggi e rimuovi la protezione dei fogli di lavoro
La protezione del foglio di lavoro blocca le celle di un foglio di lavoro contro modifiche accidentali o intenzionali. Gli utenti non possono modificare le celle bloccate senza fornire la password. Questa è la protezione tipica utilizzata per salvaguardare formule, intestazioni o aree designate per l'inserimento dei dati nei fogli di calcolo condivisi. Per proteggere un foglio di lavoro, chiamare `worksheet.protect(ProtectionType.ALL, "password")`. L'utilizzo di `ProtectionType.ALL` abilita ogni opzione di protezione disponibile come la selezione delle celle bloccate, la formattazione delle celle, l'inserimento di righe e colonne e l'eliminazione di righe e colonne. Per rimuovere la protezione, chiamare `worksheet.unprotect("password")` con la password corretta. Un controllo più granulare è disponibile combinando altri tipi di protezione come `CONTENTS`, `OBJECTS` e `SCENARIOS` utilizzando l'OR bit a bit.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(ProtectionType.ALL, "SheetPwd", "SheetPwd");
workbook.save("sheet_protected.xlsx");
Workbook workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
System.out.println("Worksheet protection removed successfully.");
```

## Aggiungi e convalida le firme digitali
Una firma digitale garantisce ai destinatari che il contenuto della cartella di lavoro sia autentico e non sia stato alterato da quando è stato firmato. Aspose.Cells fornisce il supporto per le firme digitali attraverso il pacchetto `com.aspose.cells.DigitalSignatures`. Il flusso di lavoro tipico carica un file di certificato `.pfx` attraverso le API di sicurezza Java (come `java.security.KeyStore` e `java.security.cert.X509Certificate`), lo avvolge in una `com.aspose.cells.DigitalSignatures.DigitalSignature`, aggiunge la firma a una `DigitalSignatureCollection` e applica la raccolta alla cartella di lavoro tramite `workbook.addDigitalSignature(DigitalSignatureCollection)`. La proprietà `DigitalSignature.getComments()` può registrare il contesto della firma come l'ora e lo scopo della firma. Qualsiasi modifica apportata alla cartella di lavoro dopo la firma invalida la firma, quindi una fase di convalida sul lato ricevente può rilevare manomissioni.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
import java.security.KeyStore;
KeyStore pfxKeyStore = KeyStore.getInstance("PKCS12");
pfxKeyStore.load(new FileInputStream("signature.pfx"), "pfx-password".toCharArray());
DigitalSignature signature = new DigitalSignature(pfxKeyStore, "pfx-password", "Signed by Aspose.Cells", new DateTime());
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.add(signature);
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
System.out.println("The workbook has been digitally signed.");
```

## Articoli correlati
- [Crittografa e decrittografa i file Excel](/cells/it/java/encrypt-and-decrypt-excel-files/)
- [Proteggi e rimuovi la protezione della struttura della cartella di lavoro](/cells/it/java/protect-and-unprotect-workbook-structure/)
- [Proteggere e rimuovere la protezione del foglio di lavoro](/cells/it/java/protect-and-unprotect-worksheet/)
- [Proteggi con password o rimuovi protezione la cartella di lavoro condivisa](/cells/it/java/password-protect-or-unprotect-the-shared-workbook/)
- [Assegna e convalida le firme digitali](/cells/it/java/assign-and-validate-digital-signatures/)
- [Rileva il formato file dei file Office Open XML crittografati - OOXML](/cells/it/java/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Come rilevare un formato file e verificare se il file è crittografato](/cells/it/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="java" >}}