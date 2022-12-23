---
title: Controlla se la cartella di lavoro contiene collegamenti esterni nascosti
type: docs
weight: 950
url: /it/java/check-if-workbook-contains-hidden-external-links/
---
## **Possibili scenari di utilizzo**
 volte, la cartella di lavoro contiene collegamenti esterni che sono nascosti e non possono essere visualizzati in Microsoft Excel. Aspose.Cells recupera tutti i collegamenti esterni se sono visibili o nascosti. Tuttavia, puoi controllare il[ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible)proprietà per verificare se il collegamento esterno è visibile o meno
## **Controlla se la cartella di lavoro contiene collegamenti esterni nascosti**
 Il codice di esempio seguente carica il file[file excel di origine](5472525.xlsx) che contiene collegamenti esterni nascosti. Questi collegamenti non possono essere visualizzati in Microsoft Excel ma sono presenti all'interno della cartella di lavoro. Dopo la stampa[ExternalLink.DataSource](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#DataSource) e[ExternalLink.IsReference](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsReferred) proprietà, stampa il file[ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible)proprietà. Nell'output della console di seguito, vedi, tutti i suoi collegamenti esterni non sono visibili.
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **Uscita console**
 Ecco l'output della console del codice di esempio precedente quando eseguito con il file given[file excel di esempio](5472525.xlsx).



{{< highlight "java" >}}

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
