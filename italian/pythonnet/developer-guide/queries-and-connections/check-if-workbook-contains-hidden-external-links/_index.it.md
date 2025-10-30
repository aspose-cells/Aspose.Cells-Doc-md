---
title: Controllare se il foglio di lavoro contiene collegamenti esterni nascosti
type: docs
weight: 230
url: /it/python-net/check-if-workbook-contains-hidden-external-links/
---

## **Possibili Scenari di Utilizzo**
A volte, il workbook contiene collegamenti esterni nascosti e non visibili in Microsoft Excel. Aspose.Cells per Python via .NET recupera tutti i collegamenti esterni, che siano visibili o nascosti. Tuttavia, puoi verificare la proprietà [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible) per controllare se il collegamento esterno è visibile o meno.

## **Controllare se il foglio di lavoro contiene collegamenti esterni nascosti**
Il seguente esempio di codice carica il [file Excel di origine](5115413.xlsx) che contiene collegamenti esterni nascosti. Questi collegamenti non sono visibili in Microsoft Excel, ma sono presenti all'interno del workbook. Dopo aver stampato le proprietà [ExternalLink.data_source](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/data_source) e [ExternalLink.is_referred](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_referred), viene mostrata la proprietà [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible). Nell'output della console di seguito, si vede che tutti i collegamenti esterni non sono visibili.

### **Codice di Esempio**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-CheckHiddenExternalLinks.py" >}}

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

{{< app/cells/assistant language="python-net" >}}
