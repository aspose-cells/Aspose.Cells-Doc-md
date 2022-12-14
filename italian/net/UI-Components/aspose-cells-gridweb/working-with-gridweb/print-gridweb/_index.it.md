---
title: Stampa GrigliaWeb
type: docs
weight: 90
url: /it/net/print-gridweb/
---
{{% alert color="primary" %}} 

Ci sono momenti in cui gli sviluppatori devono stampare i contenuti di GridWeb da una pagina web senza salvare il risultato come file di foglio di calcolo Excel Microsoft. Il controllo Aspose.Cells.GridWeb supporta questa funzionalità tramite la funzione lato client.

{{% /alert %}} 
## **Stampa GridWeb**
Per stampare i contenuti, Aspose.Cells.GridWeb for .NET ha esposto la funzione lato client GridWeb.Print che può essere utilizzata in una chiamata JavaScript come illustrato di seguito.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-PrintGridWeb-PrintGridWebJS.aspx" >}}



Una volta che la funzione JavaScript è a posto, può essere attivata su qualsiasi evento di scelta. Controlla il seguente frammento ASP.NET che utilizza la funzione JavaScript sopra definita su un evento di clic del pulsante.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-PrintGridWeb-PrintGridWeb.aspx" >}}
