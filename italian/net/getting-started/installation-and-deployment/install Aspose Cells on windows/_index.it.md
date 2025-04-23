---
title: Installa Aspose.Cells su Windows
type: docs
weight: 20
url: /it/net/installing-aspose-cells-on-windows/
---

{{% alert color="primary" %}} 

A volte potresti incontrare alcuni problemi nell'installare **Aspose.Cells** utilizzando il suo pacchetto di installazione (Aspose.Cells.msi...Pacchetto dell'Installatore Windows) su **Windows Vista**. Questo documento spiega come affrontare il problema e implementare l'installazione riuscita del componente. In realtà, l'installatore di **Aspose.Cells** ha bisogno di creare una cartella virtuale su IIS per il dispiegamento dei suoi demo web (Demo Asp.NET) sulla tua macchina, quindi è necessario disporre di Privilegi di Amministrazione prima di installare **Aspose.Cells** utilizzando il suo installatore. L'installatore richiede l'accesso a livello di amministratore al sistema che deve essere esplicitamente permesso di farlo.

{{% /alert %}} 
## **Fattori Possibili**
Di solito, in **Windows Vista**, i prodotti/componenti che installi/utilizzi sono sempre implementati con le autorizzazioni di "utente normale", anche se sei un **amministratore**. I programmi hanno solo un accesso limitato al file system, anche se sei loggato come un **amministratore**. Questo ha alcuni effetti collaterali sfortunati che di solito non incontreresti in Windows XP quando sei loggato come **amministratore**.
## **UAC (Controllo account utente)**
**UAC** è la parte di **Windows Vista** che ti chiede il permesso. La modalità **UAC** (nota anche come **Modalità di Approvazione Admin**) è una modalità di funzionamento che (principalmente) influenza il modo in cui funzionano gli account amministrativi. Quando **UAC** è attivato (come impostazione predefinita), devi dare esplicitamente il permesso a qualsiasi programma che vuole utilizzare i privilegi di "amministratore". Qualsiasi programma che cerca di utilizzare i privilegi admin senza il tuo permesso sarà negato l'accesso. **UAC** è anche richiesto per altre funzionalità di sicurezza di **Windows Vista**, incluso **Modalità protetta** in Internet Explorer. La Modalità protetta di Internet Explorer protegge il computer da pagine web non sicure e altre vulnerabilità legate al web, incluse quelle sconosciute.

Quando la modalità **UAC** è attivata, ogni programma che esegui avrà solo accesso da "utente standard" al sistema, anche quando sei loggato come amministratore. **Windows Vista** ha la capacità integrata di ridurre automaticamente il potenziale di violazioni della sicurezza nel sistema. Lo fa abilitando automaticamente questa funzionalità chiamata **Controllo account utente** (o **UAC** per brevità). Il **UAC** costringe gli utenti che fanno parte del gruppo amministratori locali a eseguire come se fossero utenti comuni senza privilegi amministrativi. Anche se **UAC** migliora chiaramente la sicurezza su **Windows Vista**, in alcuni scenari potresti volerlo disattivare, ad esempio durante la presentazione di demo davanti a un pubblico (demo che non riguardano la sicurezza, ad esempio). Alcuni utenti domestici potrebbero essere tentati di disattivare **UAC** a causa dell'utilizzo di risorse aggiuntive del loro sistema.
## **Passaggi necessari per l'installazione riuscita del componente**
- Assicurati che IIS sia installato sul tuo Vista prima di installare **Aspose.Cells**. È obbligatorio perché l'installatore di **Aspose.Cells** ha bisogno di creare una cartella virtuale su IIS per il rilascio dei Web Demo (Demo di Asp.NET).
- Devi disabilitare **UAC** (Controllo Account Utente). Devi essere sicuro di avere i **Privilegi amministrativi** con pieno controllo del sistema prima di installare **Aspose.Cells**. Altrimenti potresti ricevere l'errore n. 2869 durante l'installazione di **Aspose.Cells** usando il suo installatore.

Di seguito sono riportati alcuni modi per raggiungere questo obiettivo.
### **Utilizzo della riga di comando**
1. Cerca cmd.exe nella tua directory di Windows, quindi clicca con il tasto destro e seleziona Esegui come... **Amministratore**
2. Now, Run the following command on command prompt: msiexec /i <your path>/Aspose.Cells.msi and Enter.
### **Utilizzo del Pannello di controllo**
- Clicca su Start
- Clicca su Pannello di controllo
- Clicca su Account utente e protezione familiare
- Clicca su Account utente
- Clicca su Attiva o disattiva il Controllo dell'account utente
- Deseleziona la casella
- Clicca su OK

{{% alert color="primary" %}} 

Dovrai riavviare il computer affinché la modifica abbia effetto. Questa modifica influisce su tutti gli account sul computer, non solo sul tuo.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
