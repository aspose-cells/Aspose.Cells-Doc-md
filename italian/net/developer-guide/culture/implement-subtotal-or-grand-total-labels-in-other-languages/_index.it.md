---
title: Implementa le etichette Subtotal o Grand Total in altre lingue
type: docs
weight: 50
url: /it/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **Possibili Scenari di Utilizzo**

A volte, si desidera mostrare le etichette subtotali e totali globali in lingue non inglesi come cinese, giapponese, arabo, hindi, ecc. Aspose.Cells ti consente di farlo utilizzando la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) e la proprietà [**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings). Consulta questo articolo su come utilizzare la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)

- [Utilizzo della classe GlobalizationSettings per le etichette Subtotali personalizzate e altre etichette del grafico a torta](/cells/it/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implementa le etichette Subtotal o Grand Total in altre lingue**

Il seguente codice di esempio carica il [file Excel di esempio](5115151.xlsx) e implementa i nomi delle subtotali e dei totali globali nella lingua cinese. Controlla il [file Excel di output](5115152.xlsx) generato da questo codice a titolo di riferimento. Prima creiamo una classe di [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) e poi la utilizziamo nel nostro codice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Ora utilizza la classe creata sopra nel codice come mostrato di seguito:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
