---
title: Fornire il percorso del file HTML del foglio esportato tramite l interfaccia IFilePathProvider
type: docs
weight: 870
url: /it/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Possibili Scenari di Utilizzo**
Supponiamo di avere un file Excel con più fogli e si desidera esportare ciascun foglio in un file HTML individuale. Se alcuni dei fogli hanno collegamenti ad altri fogli, allora quei collegamenti saranno interrotti nell'HTML esportato. Per affrontare questo problema, Aspose.Cells fornisce l'interfaccia [IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider) che è possibile implementare per correggere i collegamenti interrotti.
## **Fornire il percorso del file HTML del foglio di lavoro esportato tramite l'interfaccia IFilePathProvider**
Si prega di scaricare il [file Excel di esempio](5473417.zip) utilizzato nel codice seguente e i relativi file HTML esportati. Tutti questi file si trovano nella cartella *Temp*. Si consiglia di estrarli sull'unità *C:*. Quindi diventerà la cartella *C:\Temp*. Successivamente si aprirà il file *Sheet1.html* nel browser e si cliccheranno i due collegamenti al suo interno. Questi collegamenti si riferiscono ai due fogli HTML esportati che si trovano nella cartella *C:\Temp\AltriFogli*.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Lo screenshot seguente mostra come appaiono il *C:\Temp\Sheet1.html* e i relativi collegamenti

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Lo screenshot seguente mostra la sorgente HTML. Come si può vedere, i collegamenti adesso si riferiscono alla cartella *C:\Temp\AltriFogli*. Ciò è stato ottenuto utilizzando l'interfaccia [IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Codice di Esempio**
Si noti che la cartella *C:\Temp* è solo a scopo illustrativo. È possibile utilizzare qualsiasi cartella a scelta e posizionare il [file Excel di esempio](5473414.xlsx) al suo interno ed eseguire il codice di esempio fornito. Si creerà quindi una sub-cartella *AltriFogli* all'interno della propria cartella e verranno esportati il secondo e il terzo foglio HTML al suo interno. Si prega di modificare la variabile *dirPath* all'interno del codice fornito e far riferimento alla propria cartella di scelta prima dell'esecuzione.

{{% alert color="primary" %}} 

Il codice di esempio funzionerà solo se verrà impostata la licenza di Aspose.Cells. Se si cercherà di eseguire il codice senza impostare la licenza, entrerà in un loop infinito. Di conseguenza, è stato aggiunto un controllo per stampare un messaggio e interrompere l'esecuzione quando la licenza non è impostata. È possibile acquistare una licenza oppure richiederne una temporanea di 30 giorni al team di vendite di Aspose.

{{% /alert %}} 

Si prega di notare che commentare queste righe all'interno del codice causerà la rottura dei collegamenti in *Sheet1.html* e *Sheet2.html* o *Sheet3.html* non verranno aperti quando si cliccheranno i relativi collegamenti all'interno di *Sheet1.html*



{{< highlight java >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



Qui è riportato il codice completo di esempio che è possibile eseguire con il [file Excel di esempio](5473414.xlsx) fornito.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
{{< app/cells/assistant language="java" >}}
