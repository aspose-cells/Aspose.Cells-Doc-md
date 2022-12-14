---
title: Specificare il percorso in cui GridWeb archivia i file di sessione temporanei
type: docs
weight: 50
url: /it/net/specify-the-path-where-gridweb-stores-temporary-session-files/
---
{{% alert color="primary" %}} 

Quando la modalità di sessione di GridWeb è ViewState, archivia i file di sessione temporanei all'interno della directory di base dell'applicazione. A volte, non è corretto archiviare lì i file di sessione temporanei perché la directory di base dell'applicazione potrebbe non disporre delle autorizzazioni di scrittura su di essa. In tali casi, GridWeb genera un'eccezione di questo tipo

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]{{< /highlight >}}

La soluzione al problema precedente è concedere l'accesso in scrittura alla directory di base dell'applicazione o modificare il percorso dei file della sessione temporanea di GridWeb con accesso in scrittura utilizzando la proprietà GridWeb.SessionStorePath. Questo percorso dovrebbe essere relativo alla directory di base dell'applicazione.

{{% /alert %}} 
## **Specificare il percorso in cui GridWeb archivia i file di sessione temporanei**
Il codice di esempio seguente specifica il percorso in cui GridWeb archivia i file di sessione temporanei.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}
