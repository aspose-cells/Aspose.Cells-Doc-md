---
title: Come impostare la proprietà AutoRecover della cartella di lavoro
type: docs
weight: 160
url: /it/java/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

 È possibile utilizzare Aspose.Cells per impostare la proprietà AutoRecover della cartella di lavoro. Il valore predefinito di questa proprietà è**VERO** . Quando lo imposti**falso**su una cartella di lavoro, Microsoft Excel disabilita il ripristino automatico (salvataggio automatico) su quel file Excel.

 Aspose.Cells fornisce[**Cartella di lavoro.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) property per abilitare o disabilitare questa opzione.

{{% /alert %}}

## Codice Java per impostare la proprietà AutoRecover della cartella di lavoro

 Il codice seguente spiega come utilizzare[**Cartella di lavoro.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) proprietà della cartella di lavoro. Il codice prima legge il valore predefinito di questa proprietà che è**VERO** , quindi lo imposta come**falso** e salva la cartella di lavoro. Quindi legge nuovamente la cartella di lavoro e legge il valore di questa proprietà che è falsa in questo momento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Output generato dal codice di esempio

Ecco l'output della console del codice di esempio precedente.

{{< highlight "java" >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
