---
title: Filtraggio Dati
type: docs
weight: 100
url: /it/net/aspose-cells-griddesktop/filtering-data/
keywords: GridDesktop,filtro,filtro dati,FiltroAutomatico,FiltroRiga
description: Questo articolo introduce come filtrare i dati nel Foglio di Lavoro in GridDesktop.
---

{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** fornisce funzionalità di Filtro Automatico e Filtro Dati Personalizzato per gli utenti. Utilizzando queste funzionalità, è possibile trovare un modo per selezionare solo quegli elementi dal foglio di lavoro che si desidera visualizzare in un elenco. Inoltre, è possibile filtrare gli elementi in un elenco secondo un criterio predefinito. È possibile filtrare testi, numeri o date con la funzionalità Filtro Automatico / Filtro Dati Personalizzato.

Puoi utilizzare l'attributo Booleano **EnableAutoFilter** della classe **RowFilterSettings** per abilitare la funzione di filtro automatico per il controllo GridDesktop. Ci sono altre proprietà della classe che puoi utilizzare, ad esempio **HeaderRow**, **StartRow** e **EndRow** per specificare gli indici della riga di intestazione, inizio e fine. La proprietà **Criteria** viene utilizzata per impostare i criteri di filtro personalizzati. La classe ha anche un metodo chiamato **FilterRows** per ottenere le righe filtrate in base ai criteri forniti.

Anche la ricerca di tipo "contiene" (senza distinzione tra maiuscole e minuscole) nell'attributo RowFilter è supportata da GridDesktop. È possibile utilizzare la proprietà **IgnoreCase** della classe **GridColumn** per specificare l'attributo di sensibilità alle maiuscole e minuscole secondo le tue esigenze. È inoltre possibile utilizzare una proprietà chiamata **IsStartWithCriteria** della classe **GridColumn** per indicare se il RowFilter utilizza i criteri StartWith su una colonna; il valore predefinito della proprietà è impostato su false.

{{% /alert %}} 
## **Filtraggio dei Dati**
Implementiamo entrambe le funzionalità di Auto-Filtro e Filtro Dati Personalizzato in questo esempio. Riempiamo una lista di dati nel GridDesktop, abilitiamo la funzione di Auto-Filtro e quindi cerchiamo le righe filtrate in base a determinati criteri.
### **Auto-Filtro**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **Filtro Dati Personalizzato**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
