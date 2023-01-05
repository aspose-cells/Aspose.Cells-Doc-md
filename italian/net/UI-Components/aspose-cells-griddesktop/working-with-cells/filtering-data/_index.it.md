---
title: Filtraggio dei dati
type: docs
weight: 100
url: /it/net/filtering-data/
---
{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** fornisce funzionalità di filtro automatico e filtro dati personalizzato per gli utenti. Utilizzando queste funzionalità, potresti trovare un modo per selezionare solo gli elementi dal foglio di lavoro che desideri visualizzare in un elenco. Inoltre, puoi filtrare gli elementi in un elenco in base a criteri prestabiliti. Puoi filtrare testo, numeri o date con la funzione Filtro automatico / Filtro dati personalizzato.

 Puoi usare**Abilita filtro automatico** Attributo booleano di**RowFilterSettings** class per abilitare la funzionalità di filtro automatico per il controllo GridDesktop. Ci sono alcune altre proprietà della classe che puoi usare, ad es**Riga di intestazione** , **StartRow** e**EndRow**per specificare gli indici di intestazione, inizio e fine riga. Il**Criteri** La proprietà viene utilizzata per impostare i criteri di filtro personalizzati. La classe ha anche un metodo chiamato**FiltroRighe** per ottenere le righe filtrate in base ai criteri specificati.

 L'attributo di ricerca del tipo "contiene" (senza distinzione tra maiuscole e minuscole) in RowFilter è supportato anche da GridDesktop. Puoi usare**IgnoraCase** proprietà di**Griglia Colonna** class per specificare l'attributo di distinzione tra maiuscole e minuscole per le tue necessità. Puoi anche usare una proprietà denominata**IsStartWithCriteria** di**Griglia Colonna** class per indicare se RowFilter utilizza i criteri StartWith su una colonna; il valore predefinito della proprietà è impostato su false.

{{% /alert %}} 
## **Filtraggio dei dati**
In questo esempio implementiamo le funzionalità di filtro automatico e filtro dati personalizzato. Compiliamo alcuni elenchi di dati nel GridDesktop, abilitiamo la funzione di filtro automatico e quindi cerchiamo le righe filtrate in base ad alcuni criteri.
### **Filtro automatico**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **Filtro dati personalizzato**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
