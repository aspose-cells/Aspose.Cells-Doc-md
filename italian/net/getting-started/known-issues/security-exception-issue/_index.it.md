---
title: Problema di eccezione di sicurezza
type: docs
weight: 30
url: /it/net/security-exception-issue/
---

## **Problema di eccezione di sicurezza**
Alcuni utenti potrebbero ricevere un errore "Security Exception" mentre cercano di utilizzare Aspose.Cells. Questo problema si verifica generalmente in un'applicazione web.
### **Spiegazione**
Aspose.Cells deve chiamare alcuni **API GDI Win32** per fornire alcune importanti funzionalità. Se il server web ha un livello di attendibilità rigoroso, questa eccezione di sicurezza potrebbe essere generata.
### **Soluzione**
Si prega di provare a creare un nuovo set di autorizzazioni per concedere il permesso di sicurezza ad Aspose.Cells.dll con "Consenti chiamate a assembly non gestiti" abilitato.
{{< app/cells/assistant language="csharp" >}}
