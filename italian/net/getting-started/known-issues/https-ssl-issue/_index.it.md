---
title: Problema SSL HTTPS
type: docs
weight: 20
url: /it/net/https-ssl-issue/
---
## **Problema HTTPS/SSL**
Alcuni utenti hanno segnalato di aver avuto problemi a scaricare i file Excel generati con Aspose.Cells. Quando si apre la finestra di dialogo di salvataggio, il nome del file contiene il nome della pagina aspx invece del file excel e il Tipo di file è vuoto.
### **Spiegazione**
Abbiamo modificato le intestazioni di risposta HTTP per risolvere il problema con la compressione HTTP. Ciò potrebbe causare problemi durante l'invio di file al browser client tramite HTTPS/SSL.
### **Soluzione**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
