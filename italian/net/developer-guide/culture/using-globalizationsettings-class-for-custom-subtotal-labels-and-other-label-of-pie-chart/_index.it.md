---
title: Utilizzo della classe GlobalizationSettings per le etichette di totale parziale personalizzate e altre etichette del grafico a torta
type: docs
weight: 70
url: /it/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Possibili scenari di utilizzo**

 Aspose.Cells API hanno esposto il file[**Impostazioni di globalizzazione**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)class per gestire gli scenari in cui l'utente desidera utilizzare etichette personalizzate per i subtotali in un foglio di calcolo. Inoltre, il[**Impostazioni di globalizzazione**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) class può essere utilizzata anche per modificare il file**Altro** etichetta per il grafico a torta durante il rendering del foglio di lavoro o del grafico.

## **Introduzione alla classe GlobalizationSettings**

 Il[**Impostazioni di globalizzazione**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) class attualmente offre i seguenti 3 metodi che possono essere sovrascritti in una classe personalizzata per ottenere le etichette desiderate per i subtotali o per rendere il testo personalizzato per il**Altro** etichetta di un grafico a torta.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): Ottiene il nome totale della funzione.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): Ottiene il nome del totale complessivo della funzione.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): Ottiene il nome delle etichette "Altro" per i grafici a torta.

### **Etichette personalizzate per subtotali**

 Il[**Impostazioni di globalizzazione**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)può essere utilizzata per personalizzare le etichette Subtotale sovrascrivendo il[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)metodi come dimostrato in precedenza.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

 Per iniettare etichette personalizzate, è necessario assegnare il file[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) proprietà a un'istanza di**Impostazioni personalizzate**class definita sopra prima di aggiungere i subtotali al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

 Il[**Impostazioni di globalizzazione**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)class funziona solo per l'aggiunta di nuovi subtotali. Se un foglio di calcolo contiene già subtotali, le relative etichette non possono essere modificate.

{{% /alert %}}

### **Testo personalizzato per altra etichetta del grafico a torta**

 Il[**Impostazioni di globalizzazione**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) offerte di classe[**Ottieni altro nome**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)metodo utile per assegnare un valore personalizzato all'etichetta "Altro" dei grafici a torta. Il frammento di codice seguente definisce una classe personalizzata ed esegue l'override di[**Ottieni altro nome**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)metodo per ottenere un'etichetta personalizzata basata sull'identificatore di cultura del sistema.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

 Il seguente frammento carica un foglio di calcolo esistente contenente un grafico a torta e visualizza il grafico in un'immagine mentre utilizza il file**Impostazioni personalizzate**classe creata sopra.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
