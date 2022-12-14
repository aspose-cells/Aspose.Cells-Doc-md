---
title: Configurazione dell'ordinamento della tabella
type: docs
weight: 90
url: /it/reportingservices/table-sorting-configuration/
---
La configurazione include 5 tipi di proprietà. Questi includono il nome del report, il nome della tabella, il valore di offset della riga, l'indice della colonna e il tipo di ordine.

- **nome** rappresenta il nome del report e il nome della tabella. name rappresenta l'intero report quando name è vuoto.
- **valore** rappresenta l'offset di riga.
- **Indice** rappresenta la posizione della colonna nella tabella.
- **Ordine** rappresenta il tipo di ordinamento.

Esempio di configurazione TableSorted:

*<TableSorted>
<Report name=”report name” >
<Table name="table name">
<RowOffset value="1"/>
<Column Index="1" Order="Descending" />
<Column Index="2" Order="Ascending" />
……
</Table>
<Table name="table name">
<RowOffset value="1"/>
<Column Index="1" Order="Descending" />
<Column Index="2" Order="Ascending" />
……
</Table>
</Report>
</TableSorted>*
