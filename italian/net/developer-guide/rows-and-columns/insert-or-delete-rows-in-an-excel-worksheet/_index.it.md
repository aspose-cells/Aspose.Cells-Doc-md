---
title: Inserisci o elimina righe in un foglio Excel
type: docs
weight: 20
url: /it/net/insert-or-delete-rows-in-an-excel-worksheet/
description: Questo articolo fornisce il codice C# per inserire ed eliminare righe in un foglio di lavoro di Excel
keywords: c# inserire o eliminare righe in un foglio di lavoro di excel, c# inserire o eliminare righe in excel, c# inserire righe in excel, c# eliminare righe in excel, inserire o eliminare righe in un foglio di lavoro di excel con c#, inserire o eliminare righe in excel con c#, inserire righe in excel con c#, eliminare righe in excel con c#
---

{{% alert color="primary" %}}

Quando si crea un nuovo foglio di lavoro, o si lavora con un foglio di lavoro esistente, potresti aver bisogno di aggiungere righe o colonne aggiuntive per ospitare i dati. Altre volte, potresti dover eliminare righe o colonne da posizioni specifiche nel foglio di lavoro.

{{% /alert %}}

Aspose.Cells offre due metodi per inserire ed eliminare righe: [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) e [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Questi metodi sono ottimizzati per le prestazioni e svolgono il lavoro molto rapidamente.

Per inserire o rimuovere un numero di righe, ti consigliamo di utilizzare sempre i metodi [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) e [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) invece di usare i metodi [**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) o [**DeleteRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow) in un loop.

Aspose.Cells funziona allo stesso modo di Microsoft Excel. Quando vengono aggiunte righe o colonne, i contenuti del foglio di lavoro vengono spostati verso il basso e verso destra. Quando vengono rimosse righe o colonne, i contenuti del foglio di lavoro vengono spostati verso l'alto o verso sinistra. Eventuali riferimenti in altri fogli di lavoro e celle vengono aggiornati quando vengono aggiunte o rimosse righe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
