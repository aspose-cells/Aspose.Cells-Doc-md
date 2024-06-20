---
title: Come impostare la proprietà AutoRecupero del Workbook
type: docs
weight: 160
url: /it/java/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

È possibile utilizzare Aspose.Cells per impostare la proprietà AutoRecover del workbook. Il valore predefinito di questa proprietà è **true**. Quando si imposta su **false** su un workbook, Microsoft Excel disabilita il ripristino automatico (Autosave) su quel file di Excel.

Aspose.Cells fornisce la proprietà [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) per abilitare o disabilitare questa opzione.

{{% /alert %}}

## Codice Java per impostare la proprietà AutoRecover del Workbook

Il codice seguente spiega come utilizzare la proprietà [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) del workbook. Il codice legge prima il valore predefinito di questa proprietà che è **true**, quindi la imposta su **false** e salva il workbook. Poi legge di nuovo il workbook e legge il valore di questa proprietà che è falso in quel momento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Output generato dal codice di esempio

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
