---
title: Fornire il percorso del file del foglio di lavoro esportato HTML tramite l'interfaccia IFilePathProvider
type: docs
weight: 870
url: /it/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Possibili scenari di utilizzo**
 Supponiamo di avere un file excel con fogli multipli e di voler esportare ogni foglio in un singolo file HTML. Se uno dei tuoi fogli ha collegamenti ad altri fogli, tali collegamenti verranno interrotti nel HTML esportato. Per affrontare questo problema, Aspose.Cells fornisce[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)interfaccia che puoi implementare per correggere i collegamenti interrotti.
## **Fornire il percorso del file del foglio di lavoro esportato HTML tramite l'interfaccia IFilePathProvider**
 Si prega di scaricare il[file excel di esempio](5473417.zip) utilizzato nel codice seguente e nei suoi file HTML esportati. Tutti questi file sono all'interno del file*temp* directory. Dovresti estrarlo su*C:* guidare. Allora diventerà*C:\Temp* directory. Quindi aprirai il file*Foglio1.html* file nel browser e fare clic sui due collegamenti al suo interno. Questi collegamenti si riferiscono a questi due fogli di lavoro HTML esportati che si trovano all'interno del file*C:\Temp\Altri fogli*directory.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Lo screenshot seguente mostra come il file*C:\Temp\Foglio1.html*e i suoi collegamenti sembrano

![cose da fare:immagine_alt_testo](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 Lo screenshot seguente mostra la fonte HTML. Come puoi vedere che i collegamenti ora fanno riferimento a*C:\Temp\Altri fogli* directory. Ciò è stato ottenuto utilizzando il[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)interfaccia.

![cose da fare:immagine_alt_testo](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Codice d'esempio**
 notare che*C:\Temp* directory è solo a scopo illustrativo. Puoi utilizzare qualsiasi directory di tua scelta e posizione[file excel di esempio](5473414.xlsx) lì dentro ed eseguire il codice di esempio fornito. Quindi creerà*AltroFogli* sottodirectory all'interno della tua directory ed esporta il secondo e il terzo foglio di lavoro HTML al suo interno. Si prega di modificare il*dirPath*variabile all'interno del codice fornito e riferirlo alla directory di tua scelta prima dell'esecuzione.

{{% alert color="primary" %}} 

Il codice di esempio funzionerà solo quando imposterai la licenza Aspose.Cells. Se proverai a eseguire il codice senza impostare la licenza, andrà in un ciclo infinito. Pertanto, abbiamo aggiunto un controllo per stampare un messaggio e interrompere l'esecuzione quando la licenza non è impostata. Puoi acquistare una licenza o richiedere una licenza temporanea di 30 giorni dal team Aspose.Purchase.

{{% /alert %}} 

 Si prega di vedere che commentare queste righe all'interno del codice interromperà i collegamenti*Foglio1.html* e*Foglio2.html* o*Foglio3.html*non si aprirà quando i loro collegamenti verranno cliccati all'interno del*Foglio1.html*



{{< highlight "java" >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



 Ecco il codice di esempio completo che puoi eseguire con il file fornito[file excel di esempio](5473414.xlsx).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
