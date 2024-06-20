---
title: Configurazione ordinamento tabella
type: docs
weight: 90
url: /it/reportingservices/table-sorting-configuration/
---

La configurazione include 5 tipi di proprietà. Queste includono nome rapporto, nome tabella, valore compensazione riga, indice colonna e tipo ordine.

- **nome** rappresenta il nome del rapporto e della tabella. nome rappresenta l'intero rapporto quando il nome è vuoto.
- **valore** rappresenta la compensazione riga.
- **Indice** rappresenta la posizione della colonna nella tabella.
- **Ordine** rappresenta il tipo di ordine di ordinamento.

Esempio configurazione tabella ordinata:

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
