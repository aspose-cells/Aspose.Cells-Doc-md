---
title: Installa Aspose.Cells su Windows
type: docs
weight: 20
url: /it/net/installing-aspose-cells-on-windows/
---
{{% alert color="primary" %}} 

 A volte potresti incontrare alcuni problemi durante l'installazione**Aspose.Cells** utilizzando il suo pacchetto di installazione (Aspose.Cells.msi...Windows Installer Package) su**Windows Vista** . Questo documento spiega come possiamo affrontarlo e implementare la corretta installazione del componente. In realtà**Aspose.Cells**il programma di installazione deve creare una cartella virtuale su IIS per la distribuzione delle sue Web Demo (Asp.NET Demos) sulla tua macchina, quindi devi disporre di privilegi di amministrazione prima dell'installazione**Aspose.Cells** utilizzando il suo programma di installazione. Il programma di installazione richiede che l'accesso a livello di amministratore al sistema sia esplicitamente autorizzato a farlo.

{{% /alert %}} 
## **Possibili Fattori**
 Normalmente, dentro**Windows Vista** , i prodotti/componenti che installi/utilizzi sono sempre implementati con i permessi di "utente normale", anche se sei un**Amministratore** . Ai programmi è consentito solo un accesso limitato al file system, anche se si è effettuato l'accesso come file system**Amministratore** . Questo ha alcuni sfortunati effetti collaterali che normalmente non incontreresti in Windows XP quando accedi come**Amministratore**.
## **UAC (controllo dell'account utente)**
**UAC** è la parte di**Windows Vista** che ti chiede il permesso. Il**UAC** modalità (nota anche come**Modalità di approvazione dell'amministratore** ) è una modalità operativa che influisce (principalmente) sul modo in cui funzionano gli account amministratore. quando**UAC**è attivato (che è per impostazione predefinita), è necessario concedere esplicitamente il permesso a qualsiasi programma che desideri utilizzare i poteri di "amministratore". Qualsiasi programma che tenta di utilizzare i poteri di amministratore senza la tua autorizzazione verrà negato l'accesso.**UAC** è richiesto anche per altre funzionalità di sicurezza di**Windows Vista** , Compreso**Modalità protetta** nell'Internet Explorer. La modalità protetta di Internet Explorer protegge il computer da pagine Web non autorizzate e altre vulnerabilità correlate al Web, comprese quelle sconosciute.

 quando**UAC** mode è abilitata, a ogni programma eseguito verrà concesso solo l'accesso "utente standard" al sistema, anche quando si è effettuato l'accesso come amministratore.**Windows Vista** ha la capacità integrata di ridurre automaticamente il potenziale di violazioni della sicurezza nel sistema. Lo fa abilitando automaticamente questa funzione chiamata**Controllo dell'account utente** (o**UAC** in breve). Il**UAC**costringe gli utenti che fanno parte del gruppo degli amministratori locali a funzionare come se fossero utenti normali senza privilegi amministrativi. Sebbene**UAC** migliora chiaramente la sicurezza su**Windows Vista** , in alcuni scenari potresti volerlo disabilitare, ad esempio quando fornisci demo di fronte a un pubblico (demo che non sono correlate alla sicurezza, ad esempio). Alcuni utenti domestici potrebbero essere tentati di disabilitare**UAC** a causa dell'utilizzo di risorse aggiuntive del loro sistema.
## **Passaggi coinvolti per una corretta installazione del componente**
-  Assicurati che IIS sia installato su Vista prima dell'installazione**Aspose.Cells** . È obbligatorio perché**Aspose.Cells** il programma di installazione deve creare una cartella virtuale su IIS per la distribuzione delle Web Demo (Asp.NET Demos).
-  Devi disabilitare**UAC** (Controllo dell'account utente). Devi assicurarti di avere un**Privilegi di amministratore** con il pieno controllo del sistema prima dell'installazione**Aspose.Cells** . Altrimenti potresti ricevere un errore # 2869 durante l'installazione**Aspose.Cells**utilizzando il suo programma di installazione.

Di seguito sono riportati alcuni modi per raggiungere questo obiettivo.
### **Utilizzo della riga di comando**
1.  Cerca cmd.exe nella directory di Windows, quindi fai clic destro su di esso e seleziona Esegui come...**Amministratore**
 2. Ora, esegui il seguente comando al prompt dei comandi: msiexec /i<your path>/Aspose.Cells.msi e Invio.
### **Utilizzo del Pannello di controllo**
- Fare clic su Avvia
- Fare clic su Pannello di controllo
- Fai clic su Account utente e Family Safety
- Fare clic su Account utente
- Fare clic su Attiva o disattiva il controllo dell'account utente
- Deseleziona la casella di controllo
- Fare clic su OK

{{% alert color="primary" %}} 

Sarà necessario riavviare il computer affinché la modifica abbia effetto. Questa modifica interessa tutti gli account sul computer, non solo il tuo.

{{% /alert %}}
