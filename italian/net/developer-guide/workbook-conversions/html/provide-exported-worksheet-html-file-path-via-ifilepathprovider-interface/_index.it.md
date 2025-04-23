---
title: Fornire il percorso del file HTML del foglio di lavoro esportato tramite l interfaccia IFilePathProvider
type: docs
weight: 70
url: /it/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Possibili Scenari di Utilizzo**
Supponiamo che tu abbia un file di Excel con più fogli e vuoi esportare ogni foglio in un file HTML individuale. Se alcuni dei tuoi fogli hanno collegamenti ad altri fogli, allora quei collegamenti saranno interrotti nell'HTML esportato. Per affrontare questo problema, Aspose.Cells fornisce l'interfaccia [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider) che è possibile implementare per correggere i collegamenti interrotti.
## **Fornire il percorso del file HTML del foglio di lavoro esportato tramite l'interfaccia IFilePathProvider**
Si prega di scaricare il [file di Excel di esempio](5115213.zip) utilizzato nel codice seguente e i relativi file HTML esportati. Tutti questi file sono all'interno della directory Temp. Dovresti estrarli sull'unità C:. Quindi diventerà la directory C:\Temp. Quindi aprirai il file Sheet1.html nel browser e cliccherai sui due collegamenti al suo interno. Questi collegamenti si riferiscono ai due fogli di lavoro HTML esportati che si trovano nella directory C:\Temp\OtherSheets.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Lo screenshot seguente mostra come appaiono il C:\Temp\Sheet1.html e i suoi collegamenti

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Lo screenshot seguente mostra il sorgente HTML. Come si può vedere, i collegamenti ora si riferiscono alla directory C:\Temp\OtherSheets. Questo è stato ottenuto utilizzando l'interfaccia [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Codice di Esempio**
Si noti che la directory C:\Temp è solo a scopo illustrativo. È possibile utilizzare qualsiasi directory a scelta personale e inserire il [file di Excel di esempio](5115211.xlsx) all'interno e eseguire il codice di esempio fornito. Creerà quindi la sotto-directory OtherSheets nella directory selezionata ed esporterà i fogli di lavoro HTML del secondo e del terzo foglio di lavoro al suo interno. Si prega di modificare la variabile dirPath all'interno del codice fornito e farvi riferimento alla directory a scelta prima dell'esecuzione.

{{% alert color="primary" %}} 

Il codice di esempio funzionerà solo se verrà impostata la licenza di Aspose.Cells. Se si cercherà di eseguire il codice senza impostare la licenza, entrerà in un loop infinito. Di conseguenza, è stato aggiunto un controllo per stampare un messaggio e interrompere l'esecuzione quando la licenza non è impostata. È possibile acquistare una licenza oppure richiederne una temporanea di 30 giorni al team di vendite di Aspose.

{{% /alert %}} 

Si prega di notare che commentare queste righe all'interno del codice interromperà i collegamenti in Sheet1.html e Sheet2.html o Sheet3.html non si apriranno quando verranno cliccati i relativi collegamenti all'interno di Sheet1.html



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



Di seguito è riportato il codice di esempio completo che è possibile eseguire con il [file di Excel di esempio](5115211.xlsx) fornito.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
{{< app/cells/assistant language="csharp" >}}
