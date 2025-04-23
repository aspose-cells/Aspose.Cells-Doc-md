---
title: Controllare se il foglio di lavoro contiene collegamenti esterni nascosti
type: docs
weight: 950
url: /it/java/check-if-workbook-contains-hidden-external-links/
---

## **Possibili Scenari di Utilizzo**
A volte, il cartella di lavoro contiene collegamenti esterni che sono nascosti e non possono essere visualizzati in Microsoft Excel. Aspose.Cells recupera tutti i collegamenti esterni che siano visibili o nascosti. Tuttavia, puoi verificare la proprietà ExternalLink.IsVisible per verificare se il collegamento esterno è visibile o meno.
## **Controllare se il foglio di lavoro contiene collegamenti esterni nascosti**
Il seguente codice di esempio carica il file excel di origine (5472525.xlsx) che contiene collegamenti esterni nascosti. Questi collegamenti non possono essere visualizzati in Microsoft Excel ma sono presenti all'interno del cartella di lavoro. Dopo aver stampato l'ExternalLink.DataSource e la proprietà ExternalLink.IsReferred, stampa la proprietà ExternalLink.IsVisible. Nell'output della console qui sotto, si vede, tutti i suoi collegamenti esterni non sono visibili.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **Output della console**
Ecco l'output della console del codice di esempio sopra quando eseguito con il relativo file excel di esempio (5472525.xlsx).



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
{{< app/cells/assistant language="java" >}}
