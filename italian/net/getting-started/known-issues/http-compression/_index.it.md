---
title: Compressione HTTP
type: docs
weight: 10
url: /it/net/http-compression/
---

## **Problema di compressione HTTP**
Alcuni utenti segnalano che se configurano la compressione HTTP in IIS, trovano errori durante l'invio dei file generati ai browser dei client.
### **Spiegazione**
Utilizziamo l'intestazione **"Content-disposition", "inline; filename=test.xls"** per forzare il browser ad aprire il file e l'intestazione **"Content-disposition", "attachment; filename=test.xls"** per forzare il browser ad aprire il dialogo di **Salva come** e utilizzare Microsoft Excel per aprire il file. Tuttavia, ci sono alcune eccezioni che esistono.
### **Eccezioni**
È possibile utilizzare il seguente codice per verificare che NON si tratti di un bug di Aspose.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **Soluzioni**
Puoi utilizzare uno dei seguenti workaround per risolvere questo problema:

- Spostare quei file ASP.NET specificati (che contengono codice che chiama Aspose.Cells) in un'altra cartella, che non è compressa.
- Disabilitare la compressione HTTP per i contenuti dinamici.
- Salvare il file generato nel proprio server e fornire un collegamento ai propri utenti.

Se si desidera utilizzare la compressione HTTP, utilizzare sempre l'opzione *OpenInExcel* anziché l'opzione *OpenInBrowser* quando si sa di aver abilitato la compressione di IIS.
{{< app/cells/assistant language="csharp" >}}
