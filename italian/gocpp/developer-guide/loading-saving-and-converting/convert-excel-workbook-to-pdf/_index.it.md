---
title: Convertire un Workbook Excel in PDF
type: docs
weight: 80
url: /it/go-cpp/convert-excel-workbook-to-pdf/
---

## **Conversione di un Workbook Excel in PDF**

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{% alert color="primary" %}}

Aspose.Cells scrive direttamente le informazioni sull'API e il Numero di Versione nei documenti di output. Ad esempio, durante la conversione del Documento in PDF, Aspose.Cells for Go via C++ popola il campo **Applicazione** con il valore 'Aspose.Cells' e il campo **Produttore PDF** con il valore, ad esempio, 'Aspose.Cells v24.12.0'.

Si noti che non è possibile istruire Aspose.Cells for Go via C++ a modificare o rimuovere queste informazioni dai Documenti di output.

{{% /alert %}}

### **Conversione Diretta**

Seguire i seguenti passi per convertire direttamente i fogli di calcolo Excel in formato PDF:

1. Istanziare un oggetto della classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) chiamando il suo costruttore vuoto.
2. È possibile aprire/caricare un file di modello esistente o saltare questo passo se si sta creando il workbook da zero.
3. Eseguire qualsiasi lavoro (inserire dati, applicare formattazione, inserire formule, inserire immagini o altri oggetti grafici, ecc.) sul foglio di calcolo utilizzando le API di Aspose.Cells.
1. Quando il codice del foglio di calcolo è completo, chiamare il metodo [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) della classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) per salvare il foglio di calcolo.

Il formato del file dovrebbe essere PDF, quindi selezionare il formato PDF rilevante (un valore predefinito) dall'enumerazione SaveFormat per generare il documento PDF finale.

Vedere il seguente esempio di codice, il [file Excel di esempio](67338368.xlsx) e il [PDF di output](67338369.pdf) come riferimento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookAsPDF.go" >}}
