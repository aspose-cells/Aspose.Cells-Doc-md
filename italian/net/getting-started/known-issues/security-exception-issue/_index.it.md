---
title: Problema di eccezione di sicurezza
type: docs
weight: 30
url: /it/net/security-exception-issue/
---
## **Problema di eccezione di sicurezza**
Alcuni utenti potrebbero ricevere l'errore "Eccezione di sicurezza" durante il tentativo di utilizzare Aspose.Cells. Questo problema si verifica generalmente in un'applicazione web.
### **Spiegazione**
 Aspose.Cells deve chiamare alcuni**API Win32 GDI** per fornire alcune caratteristiche importanti. Se il server Web ha un livello di attendibilità rigoroso, potrebbe essere generata questa eccezione di sicurezza.
### **Soluzione**
Prova a creare un nuovo set di autorizzazioni per concedere l'autorizzazione di sicurezza Aspose.Cells.dll con "Consenti chiamate ad assembly non gestiti" abilitato.
