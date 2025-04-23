---
title: Utilizzo della classe GlobalizationSettings per etichette subtotali personalizzate e altre etichette del grafico a torta
type: docs
weight: 70
url: /it/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Possibili Scenari di Utilizzo**

Le API di Aspose.Cells hanno esposto la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) per gestire gli scenari in cui l'utente desidera utilizzare etichette personalizzate per le subtotali in un foglio di calcolo. Inoltre, la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) può anche essere utilizzata per modificare l'etichetta **Altro** per il grafico a torta durante la visualizzazione del foglio di lavoro o del grafico.

## **Introduzione alla classe GlobalizationSettings**

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) offre attualmente i seguenti 3 metodi che possono essere sovrascritti in una classe personalizzata per ottenere etichette desiderate per le subtotali o per creare testo personalizzato per l'etichetta **Altro** di un grafico a torta.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): Ottiene il nome totale della funzione.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): Ottiene il nome del totale generale della funzione.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): Ottiene il nome delle etichette "Altro" per i grafici a torta.

### **Etichette personalizzate per le subtotali**

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) può essere utilizzata per personalizzare le etichette delle subtotali sovra-ridendo i metodi [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) e [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname) come dimostrato di seguito.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

Per iniettare etichette personalizzate, è necessario assegnare la proprietà [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) a un'istanza della classe **CustomSettings** definita sopra prima di aggiungere le subtotali al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) funziona solo per l'aggiunta di nuove subtotali. Se un foglio di calcolo contiene già delle subtotali, le loro etichette non possono essere modificate.

{{% /alert %}}

### **Testo personalizzato per l'etichetta Altro del grafico a torta**

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) offre il metodo [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) che è utile per dare un valore personalizzato all'etichetta "Altro" dei grafici a torta. Il seguente snippet definisce una classe personalizzata e sovrascrive il metodo [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) per ottenere un'etichetta personalizzata in base all'identificatore della cultura del sistema.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

Il seguente snippet carica un foglio di calcolo esistente contenente un grafico a torta e visualizza il grafico come un'immagine utilizzando la classe **CustomSettings** creata in precedenza.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
