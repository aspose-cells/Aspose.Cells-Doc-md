---
title: Implementa le etichette Subtotale o Totale complessivo in altre lingue
type: docs
weight: 50
url: /it/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---
## **Possibili scenari di utilizzo**

 volte, vuoi mostrare le etichette del totale parziale e del totale complessivo in lingue diverse dall'inglese come cinese, giapponese, arabo, hindi ecc. Aspose.Cells ti consente di farlo utilizzando il[**Impostazioni di globalizzazione**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)classe e[**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) proprietà. Si prega di consultare questo articolo su come utilizzare[**Impostazioni di globalizzazione**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)classe

- [Utilizzo della classe GlobalizationSettings per le etichette di totale parziale personalizzate e altre etichette del grafico a torta](/cells/it/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implementa le etichette Subtotale o Totale complessivo in altre lingue**

 Il codice di esempio seguente carica il file[file excel di esempio](5115151.xlsx) e implementa i nomi dei subtotali e dei totali complessivi in lingua cinese. Si prega di controllare[file Excel di output](5115152.xlsx) generato da questo codice per riferimento. Per prima cosa creiamo una classe di[**Impostazioni di globalizzazione**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)e poi usalo nel nostro codice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Ora usa la classe sopra creata nel codice come di seguito:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
