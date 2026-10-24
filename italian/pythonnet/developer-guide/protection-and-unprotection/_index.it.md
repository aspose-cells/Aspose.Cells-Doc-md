---
title: Proteggere e rimuovere la protezione
linktitle: Crittografia e protezione
type: docs
weight: 68
url: /it/python-net/protect-and-unprotect/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/python-net/security-features/]
description: Questa sezione introduce come crittografare e decrittografare i file Excel e proteggere i dati Excel, coprendo la crittografia dei file, la protezione in sola lettura, la protezione della struttura della cartella di lavoro, la protezione dei fogli di lavoro e le firme digitali utilizzando codice Python
keywords: Aspose.Cells, Python via .NET, crittografare, decrittografare, password, proteggere, rimuovere la protezione, protezione cartella di lavoro, protezione foglio di lavoro, sola lettura, firma digitale, Python
---

Le cartelle di lavoro di Excel spesso memorizzano informazioni finanziarie, aziendali o personali sensibili che devono essere protette da accessi non autorizzati. Aspose.Cells for Python via .NET fornisce un set completo di funzionalità di protezione che rispecchiano le capacità di Microsoft Excel, consentendo di proteggere i dati a livello di file, di cartella di lavoro e di foglio di lavoro.

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET offre un'ampia gamma di funzionalità di protezione, dal livello di file al livello di dati, simile a MS Excel. Queste funzionalità includono la crittografia dei file con una password, l'imposizione dell'accesso in sola lettura tramite una password per modificare, la protezione della struttura della cartella di lavoro, la protezione dei fogli di lavoro e la firma digitale delle cartelle di lavoro.
{{% /alert %}}

## Crittografare e decrittografare i file Excel
Una password impostata su un file Excel impedisce agli utenti non autorizzati di aprire o visualizzare il contenuto della cartella di lavoro. Per crittografare una cartella di lavoro, assegnare una stringa di password a `workbook.settings.password` e quindi salvare la cartella di lavoro. Aspose.Cells scrive il file in forma crittografata. Per aprire una cartella di lavoro crittografata per la decrittografia, creare un'istanza di un oggetto `LoadOptions`, impostare `load_options.password` sulla stessa password utilizzata durante la crittografia e passarlo al costruttore `Workbook`. Aspose.Cells applica la password fornita in modo trasparente, così che il resto del codice possa interagire con il contenuto decrittografato come se il file fosse una normale cartella di lavoro.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cell = sheet.cells.get("A1")
cell.put_value("Confidential Data")
workbook.settings.password = "OpenPassword123"
workbook.save("encrypted.xlsx")
load_options = ac.LoadOptions()
load_options.password = "OpenPassword123"
decrypted_workbook = ac.Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.worksheets[0].cells.get("A1").string_value)
```

## Protezione in sola lettura (password per modificare)
Excel supporta due distinti livelli di password. Il primo è una password per aprire, che crittografa il file stesso ed è trattato nella sezione precedente. Il secondo è una password per modificare, che non impedisce agli utenti di aprire la cartella di lavoro; invece, Excel consiglia di aprire il file in modalità di sola lettura a meno che non venga fornita la password di modifica. Configurare questo comportamento in Aspose.Cells tramite `workbook.settings.write_protection`. Impostare la sua proprietà `password` sulla password di modifica e la sua proprietà `author` per identificare chi ha applicato la protezione. Utilizzare il metodo `write_protection.validate_password(string)` per verificare se una password di modifica fornita è corretta, restituendo `true` per una corrispondenza e `false` altrimenti.

```python
import aspose.cells as ac
# Crea una nuova cartella di lavoro da zero
workbook = ac.Workbook()
# Scrivi un valore di esempio nella cella A1 del primo foglio di lavoro
workbook.worksheets[0].cells.get("A1").put_value("Sample Data")
# Configura la protezione da scrittura: imposta la password per modificare e l'autore
workbook.settings.write_protection.password = "ModifyPwd"
workbook.settings.write_protection.author = "AuthorName"
# Salva la cartella di lavoro in modo che la protezione da scrittura venga mantenuta
workbook.save("WriteProtectedWorkbook.xlsx")
# Convalida la password per modificare utilizzando la password corretta
is_correct_valid = workbook.settings.write_protection.validate_password("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Convalida la password per modificare utilizzando una password errata per dimostrare l'altro ramo
is_wrong_valid = workbook.settings.write_protection.validate_password("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
```

## Proteggere e rimuovere la protezione della struttura della cartella di lavoro
La protezione della struttura della cartella di lavoro impedisce ad altri utenti di visualizzare fogli di lavoro nascosti, aggiungere nuovi fogli di lavoro, spostare fogli di lavoro, eliminare fogli di lavoro, nascondere fogli di lavoro o rinominare fogli di lavoro. Lo stato protetto si applica alla struttura del foglio anziché al contenuto delle celle all'interno di qualsiasi foglio. Per applicare la protezione della struttura, chiamare `workbook.protect(ProtectionType.STRUCTURE, "password")`. Per rimuovere la protezione, chiamare `workbook.unprotect("password")` e fornire la password corretta. Il valore enum `ProtectionType.STRUCTURE` viene utilizzato qui ed è distinto da altri tipi di protezione come `ProtectionType.WINDOWS`.

```python
import aspose.cells as ac
# Crea una nuova cartella di lavoro
workbook = ac.Workbook()
# Aggiungi un secondo foglio di lavoro
workbook.worksheets.add()
# Scrivi un valore di esempio nella cella A1 del primo foglio di lavoro
workbook.worksheets[0].cells.get(0, 0).put_value("Sample Data")
# Proteggi la struttura della cartella di lavoro
workbook.protect(ac.ProtectionType.STRUCTURE, "StructPwd")
# Salva la cartella di lavoro come structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Ricarica il file in una nuova istanza della cartella di lavoro
loaded_workbook = ac.Workbook(file_path)
# Rimuovi la protezione della struttura
loaded_workbook.unprotect("StructPwd")
# Stampa il messaggio di conferma
print("Structure protection has been successfully removed from the workbook.")
```

## Proteggere e rimuovere la protezione dei fogli di lavoro
La protezione del foglio di lavoro blocca le celle di un foglio di lavoro contro modifiche accidentali o intenzionali. Gli utenti non possono modificare le celle bloccate senza fornire la password. Questa è la protezione tipica utilizzata per proteggere formule, intestazioni o aree di immissione dati designate in fogli di calcolo condivisi. Per proteggere un foglio di lavoro, chiamare `worksheet.protect(ProtectionType.ALL, "password")`. L'utilizzo di `ProtectionType.ALL` abilita ogni opzione di protezione disponibile come la selezione di celle bloccate, la formattazione di celle, l'inserimento di righe e colonne e l'eliminazione di righe e colonne. Per rimuovere la protezione, chiamare `worksheet.unprotect("password")` con la password corretta. Un controllo più granulare è disponibile combinando altri tipi di protezione come `Contents`, `Objects` e `Scenarios` utilizzando l'OR bit a bit.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
sheet.cells.get("A1").put_value("Sample Data")
sheet.protect(ac.ProtectionType.ALL, "SheetPwd")
workbook.save("sheet_protected.xlsx")
workbook_reloaded = ac.Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.worksheets[0]
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
```

## Aggiungere e convalidare le firme digitali
Una firma digitale assicura ai destinatari che il contenuto della cartella di lavoro è autentico e non è stato alterato da quando è stato firmato. Aspose.Cells fornisce supporto per le firme digitali attraverso il namespace `aspose.cells.digital_signatures`. Il flusso di lavoro tipico carica un file di certificato `.pfx` attraverso `System.Security.Cryptography.X509Certificates.X509Certificate2`, lo avvolge in un `aspose.cells.digital_signatures.DigitalSignature`, aggiunge la firma a una `DigitalSignatureCollection` e applica la raccolta alla cartella di lavoro attraverso `workbook.add_digital_signature(DigitalSignatureCollection)`. La proprietà `digital_signature.comments` può registrare il contesto della firma come l'ora e lo scopo della firma. Qualsiasi modifica apportata alla cartella di lavoro dopo la firma invalida la firma, quindi una fase di validazione sul lato ricevente può rilevare manomissioni.

```python
from datetime import datetime
import aspose.cells as ac
from aspose.cells.digitalsignatures import DigitalSignature, DigitalSignatureCollection
with open("signature.pfx", "rb") as certificate_file:
    certificate = certificate_file.read()
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", datetime.now())
signatures = DigitalSignatureCollection()
signatures.add(signature)
workbook = ac.Workbook()
workbook.worksheets[0].cells.get("A1").put_value("Sample Value")
workbook.add_digital_signature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
```

## Articoli correlati
- [Crittografare e decrittografare i file Excel](/cells/it/python-net/encrypt-and-decrypt-excel-files/)
- [Proteggere e rimuovere la protezione della struttura della cartella di lavoro](/cells/it/python-net/protect-and-unprotect-workbook-structure/)
- [Proteggere e rimuovere la protezione del foglio di lavoro](/cells/it/python-net/protect-and-unprotect-worksheets/)
- [Proteggere con password o rimuovere la protezione della cartella di lavoro condivisa](/cells/it/python-net/password-protect-or-unprotect-the-shared-workbook/)
- [Assegnare e convalidare le firme digitali](/cells/it/python-net/assign-and-validate-digital-signatures/)
- [Verificare la password per modificare utilizzando Aspose.Cells](/cells/it/python-net/check-password-to-modify-using-aspose-cells/)
- [Rilevare il formato di file di Office Open XML crittografati - file OOXML](/cells/it/python-net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Crittografia dei file Excel](/cells/it/python-net/encrypting-excel-files/)
- [Come rilevare un formato di file e verificare se il file è crittografato](/cells/it/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="python-net" >}}