---
title: Problemi SSL HTTPS
type: docs
weight: 20
url: /it/net/https-ssl-issue/
---

## **Problema HTTPS/SSL**
Alcuni utenti hanno segnalato di avere problemi nel scaricare file Excel generati con Aspose.Cells. Quando si apre il dialogo di salvataggio, il nome del file contiene il nome della pagina aspx anziché il file Excel e il tipo di file è vuoto.
### **Spiegazione**
Abbiamo modificato gli intestazioni di risposta HTTP per risolvere il problema con la compressione HTTP. Questo potrebbe causare problemi durante l'invio dei file ai browser dei client tramite HTTPS/SSL.
### **Soluzione**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
{{< app/cells/assistant language="csharp" >}}
