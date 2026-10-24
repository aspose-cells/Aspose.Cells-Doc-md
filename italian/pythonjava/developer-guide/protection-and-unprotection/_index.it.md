---
title: Proteggere e rimuovere la protezione
linktitle: Protezione
type: docs
weight: 68
url: /it/python-java/protect-and-unprotect/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/python-java/security-features/]
description: Questa sezione illustra come crittografare e decrittografare file Excel e proteggere i dati Excel, coprendo la crittografia dei file, la protezione di sola lettura, la protezione della struttura della cartella di lavoro, la protezione dei fogli di lavoro e le firme digitali utilizzando codice Python
keywords: Aspose.Cells, Python via Java, crittografare, decrittografare, password, proteggere, rimuovere la protezione, protezione cartella di lavoro, protezione foglio di lavoro, sola lettura, firma digitale, Python
---

Le cartelle di lavoro Excel spesso contengono informazioni finanziarie, aziendali o personali sensibili che devono essere protette dagli accessi non autorizzati. Aspose.Cells for Python via Java fornisce un set completo di funzionalità di protezione che rispecchia le capacità di Microsoft Excel, consentendo di proteggere i dati a livello di file, a livello di cartella di lavoro e a livello di foglio di lavoro.

{{% alert color="primary" %}}
Aspose.Cells for Python via Java offre un'ampia gamma di funzionalità di protezione, dal livello di file al livello di dati, in modo simile a MS Excel. Queste funzionalità includono la crittografia dei file con una password, l'imposizione dell'accesso in sola lettura tramite una password per la modifica, la protezione della struttura della cartella di lavoro, la protezione dei fogli di lavoro e la firma digitale delle cartelle di lavoro.
{{% /alert %}}

## Crittografare e decrittografare file Excel
Una password impostata su un file Excel impedisce agli utenti non autorizzati di aprire o visualizzare il contenuto della cartella di lavoro. Per crittografare una cartella di lavoro, assegnare una stringa di password a `workbook.getSettings().setPassword(...)` e quindi salvare la cartella di lavoro. Aspose.Cells scrive il file in forma crittografata. Per aprire una cartella di lavoro crittografata per la decrittografia, istanziare un oggetto `LoadOptions`, impostare la password tramite `load_options.setPassword(...)` con la stessa password utilizzata durante la crittografia e passarla al costruttore di `Workbook`. Aspose.Cells applica la password fornita in modo trasparente, così che il resto del codice possa interagire con il contenuto decrittografato come se il file fosse una normale cartella di lavoro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cell, LoadOptions
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cell = sheet.getCells().get("A1")
cell.putValue("Confidential Data")
workbook.getSettings().setPassword("OpenPassword123")
workbook.save("encrypted.xlsx")
load_options = LoadOptions()
load_options.setPassword("OpenPassword123")
decrypted_workbook = Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.getWorksheets().get(0).getCells().get("A1").getStringValue())
jpype.shutdownJVM()
```

## Protezione di sola lettura (password per la modifica)
Excel supporta due distinti livelli di password. Il primo è una password di apertura, che crittografa il file stesso ed è trattato nella sezione precedente. Il secondo è una password per la modifica, che non impedisce agli utenti di aprire la cartella di lavoro; invece, Excel consiglia di aprire il file in modalità di sola lettura a meno che non venga fornita la password di modifica. Configurare questo comportamento in Aspose.Cells tramite `workbook.getSettings().getWriteProtection()`. Impostare la password tramite `setPassword(...)` con la password di modifica e l'autore tramite `setAuthor(...)` per identificare chi ha applicato la protezione. Utilizzare il metodo `writeProtection.validatePassword(String)` per verificare se una password di modifica fornita è corretta, restituendo `true` in caso di corrispondenza e `false` altrimenti.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Crea una nuova cartella di lavoro da zero
workbook = Workbook()
# Scrivi un valore di esempio nella cella A1 del primo foglio di lavoro
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data")
# Configura la protezione da scrittura: imposta la password per modificare e l'autore
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd")
workbook.getSettings().getWriteProtection().setAuthor("AuthorName")
# Salva la cartella di lavoro in modo che la protezione da scrittura venga mantenuta
workbook.save("WriteProtectedWorkbook.xlsx")
# Verifica la password per modificare utilizzando la password corretta
is_correct_valid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Verifica la password per modificare utilizzando una password errata per dimostrare l'altro ramo
is_wrong_valid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
jpype.shutdownJVM()
```

## Proteggere e rimuovere la protezione della struttura della cartella di lavoro
La protezione della struttura della cartella di lavoro impedisce ad altri utenti di visualizzare fogli di lavoro nascosti, aggiungere nuovi fogli di lavoro, spostare fogli di lavoro, eliminare fogli di lavoro, nascondere fogli di lavoro o rinominare fogli di lavoro. Lo stato protetto si applica alla struttura dei fogli piuttosto che al contenuto delle celle all'interno di qualsiasi foglio. Per applicare la protezione della struttura, chiamare `workbook.protect(ProtectionType.STRUCTURE, "password")`. Per rimuovere la protezione, chiamare `workbook.unprotect("password")` e fornire la password corretta. Il valore enum `ProtectionType.STRUCTURE` viene utilizzato qui ed è distinto da altri tipi di protezione come `ProtectionType.WINDOWS`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, ProtectionType
# Crea una nuova cartella di lavoro
workbook = Workbook()
# Aggiungi un secondo foglio di lavoro
workbook.getWorksheets().add()
# Scrivi un valore di esempio nella cella A1 del primo foglio di lavoro
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data")
# Proteggi la struttura della cartella di lavoro
workbook.protect(ProtectionType.STRUCTURE, "StructPwd")
# Salva la cartella di lavoro come structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Ricarica il file in una nuova istanza di Workbook
loaded_workbook = Workbook(file_path)
# Rimuovi la protezione della struttura
loaded_workbook.unprotect("StructPwd")
# Stampa messaggio di conferma
print("Structure protection has been successfully removed from the workbook.")
jpype.shutdownJVM()
```

## Proteggere e rimuovere la protezione dei fogli di lavoro
La protezione del foglio di lavoro blocca le celle di un foglio di lavoro contro modifiche accidentali o deliberate. Gli utenti non possono modificare le celle bloccate senza fornire la password. Questa è la protezione tipica utilizzata per proteggere formule, intestazioni o aree designate per l'inserimento dei dati nei fogli di calcolo condivisi. Per proteggere un foglio di lavoro, chiamare `worksheet.protect(ProtectionType.ALL, "password")`. L'utilizzo di `ProtectionType.ALL` abilita ogni opzione di protezione disponibile come la selezione delle celle bloccate, la formattazione delle celle, l'inserimento di righe e colonne e l'eliminazione di righe e colonne. Per rimuovere la protezione, chiamare `worksheet.unprotect("password")` con la password corretta. È possibile un controllo più granulare combinando altri tipi di protezione come `ProtectionType.CONTENTS`, `ProtectionType.OBJECTS` e `ProtectionType.SCENARIOS` utilizzando l'OR bitwise.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, ProtectionType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sample Data")
worksheet.protect(ProtectionType.ALL, "SheetPwd", None)
workbook.save("sheet_protected.xlsx")
workbook_reloaded = Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.getWorksheets().get(0)
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
jpype.shutdownJVM()
```

## Aggiungere e convalidare firme digitali
Una firma digitale garantisce ai destinatari che il contenuto della cartella di lavoro è autentico e non è stato alterato da quando è stato firmato. Aspose.Cells fornisce il supporto per le firme digitali tramite il namespace `Aspose.Cells.DigitalSignatures`. Il flusso di lavoro tipico carica un file di certificato `.pfx` tramite `java.security.KeyStore`, lo avvolge in un `Aspose.Cells.DigitalSignatures.DigitalSignature`, aggiunge la firma a una `DigitalSignatureCollection` e applica la raccolta alla cartella di lavoro tramite `workbook.addDigitalSignature(digitalSignatureCollection)`. La proprietà `digitalSignature.getComments()` può registrare il contesto della firma come l'ora e lo scopo della firma. Qualsiasi modifica apportata alla cartella di lavoro dopo la firma invalida la firma, quindi una fase di convalida sul lato ricevente può rilevare le manomissioni.

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, DigitalSignature, DigitalSignatureCollection
from java.security import KeyStore
from java.io import FileInputStream
from java.util import Date
# Carica il certificato dal file PFX utilizzando Java KeyStore
key_store = KeyStore.getInstance("PKCS12")
fis = FileInputStream("signature.pfx")
key_store.load(fis, "pfx-password")
fis.close()
# Ottieni il certificato
alias = key_store.aliases().nextElement()
certificate = key_store.getCertificate(alias)
# Crea la firma digitale
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", Date())
signatures = DigitalSignatureCollection()
signatures.add(signature)
# Crea la cartella di lavoro e aggiungi la firma
workbook = Workbook()
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value")
workbook.addDigitalSignature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
jpype.shutdownJVM()
```

## Articoli Correlati
- [Crittografare e Decrittografare file Excel](/cells/it/python-java/encrypt-and-decrypt-excel-files/)
- [Proteggere e Rimuovere la Protezione della Struttura della Cartella di Lavoro](/cells/it/python-java/protect-and-unprotect-workbook-structure/)
- [Proteggere e rimuovere la protezione del foglio di lavoro](/cells/it/python-java/protect-and-unprotect-worksheet/)
- [Verificare la Password per la modifica utilizzando Aspose.Cells](/cells/it/python-java/check-password-to-modify-using-aspose-cells/)

{{< app/cells/assistant language="python" >}}