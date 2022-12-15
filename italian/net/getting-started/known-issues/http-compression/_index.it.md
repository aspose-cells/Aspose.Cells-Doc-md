---
title: Compressione HTTP
type: docs
weight: 10
url: /it/net/http-compression/
---
## **Problema di compressione HTTP**
Alcuni utenti segnalano che se configurano la compressione HTTP in IIS, trovano errori durante l'invio di file generati ai browser client.
### **Spiegazione**
 Noi usiamo**"Content-disposition", "inline; filename=test.xls"** header per forzare il browser ad aprire il file e**"Content-disposition", "allegato; filename=test.xls"** header per forzare il browser ad aprire il file**Salva come** finestra di dialogo e utilizzare Microsoft Excel per aprire il file. Tuttavia, ci sono alcune eccezioni che esistono.
### **Eccezioni**
È possibile utilizzare il seguente codice per verificare che NON si tratti di un bug di Aspose.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **Soluzioni**
È possibile utilizzare una delle seguenti soluzioni alternative per risolvere questo problema:

- Sposta i file ASP.NET specificati (che contengono il codice che chiama Aspose.Cells) in un'altra cartella, che non è compressa.
- Disabilita la compressione HTTP per i contenuti dinamici.
- Salva il file generato nel tuo server e fornisci un link ai tuoi utenti.

 Se desideri utilizzare la compressione HTTP, utilizzala sempre*ApriInExcel* opzione invece di*Apri nel browser* opzione quando sai di aver abilitato la compressione IIS.
