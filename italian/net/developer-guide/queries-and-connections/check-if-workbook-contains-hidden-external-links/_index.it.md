---
title: Controllare se il foglio di lavoro contiene collegamenti esterni nascosti
type: docs
weight: 230
url: /it/net/check-if-workbook-contains-hidden-external-links/
---

## **Possibili Scenari di Utilizzo**
A volte, il foglio di lavoro contiene collegamenti esterni nascosti che non possono essere visualizzati in Microsoft Excel. Aspose.Cells recupera tutti i collegamenti esterni, che siano visibili o nascosti. Tuttavia, è possibile controllare la proprietà [ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) per verificare se il collegamento esterno è visibile o no
## **Controllare se il foglio di lavoro contiene collegamenti esterni nascosti**
Il seguente codice di esempio carica il [file di Excel di origine](5115413.xlsx) che contiene collegamenti esterni nascosti. Questi collegamenti non possono essere visualizzati in Microsoft Excel ma sono presenti all'interno del foglio di lavoro. Dopo la stampa di [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) e [ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred), stampa la proprietà [ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible). Nell'output della console qui sotto, si vede che tutti i suoi collegamenti esterni non sono visibili.
### **Codice di Esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **Output della console**
Ecco l'output della console del codice di esempio sopra quando eseguito con il [file di Excel di esempio](5115413.xlsx).



{{< highlight java >}}

 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
