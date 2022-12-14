---
title: Fornisci il percorso del file html del foglio di lavoro esportato tramite l'interfaccia IFilePathProvider
type: docs
weight: 70
url: /it/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Possibili scenari di utilizzo**
 Supponiamo di avere un file excel con fogli multipli e di voler esportare ogni foglio in un singolo file HTML. Se uno dei tuoi fogli contiene collegamenti ad altri fogli, tali collegamenti verranno interrotti nell'HTML esportato. Per far fronte a questo problema, Aspose.Cells fornisce[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)interfaccia che puoi implementare per correggere i collegamenti interrotti.
## **Fornisci il percorso del file HTML del foglio di lavoro esportato tramite l'interfaccia IFilePathProvider**
 Si prega di scaricare il[file excel di esempio](5115213.zip)utilizzato nel codice seguente e nei relativi file HTML esportati. Tutti questi file si trovano all'interno della directory Temp. Dovresti estrarlo su C: drive. Quindi diventerà la directory C:\Temp. Quindi aprirai il file Sheet1.html nel browser e fai clic sui due collegamenti al suo interno. Questi collegamenti fanno riferimento a questi due fogli di lavoro HTML esportati che si trovano all'interno della directory C:\Temp\OtherSheets.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Lo screenshot seguente mostra l'aspetto di C:\Temp\Sheet1.html e dei relativi collegamenti

![cose da fare:immagine_alt_testo](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 Lo screenshot seguente mostra l'origine HTML. Come puoi vedere, i collegamenti ora fanno riferimento alla directory C:\Temp\OtherSheets. Ciò è stato ottenuto utilizzando il[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)interfaccia.

![cose da fare:immagine_alt_testo](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Codice di esempio**
 Si noti che la directory C:\Temp è solo a scopo illustrativo. Puoi utilizzare qualsiasi directory di tua scelta e posizione[file excel di esempio](5115211.xlsx)lì dentro ed eseguire il codice di esempio fornito. Creerà quindi la sottodirectory OtherSheets all'interno della directory ed esporterà il secondo e il terzo foglio di lavoro HTML al suo interno. Modificare la variabile dirPath all'interno del codice fornito e riferirla alla directory di propria scelta prima dell'esecuzione.

{{% alert color="primary" %}} 

Il codice di esempio funzionerà solo quando imposterai la licenza Aspose.Cells. Se proverai a eseguire il codice senza impostare la licenza, andrà in un ciclo infinito. Pertanto, abbiamo aggiunto un controllo per stampare un messaggio e interrompere l'esecuzione quando la licenza non è impostata. Puoi acquistare una licenza o richiedere una licenza temporanea di 30 giorni dal team Aspose.Purchase.

{{% /alert %}} 

Si prega di notare che commentare queste righe all'interno del codice interromperà i collegamenti in Sheet1.html e Sheet2.html o Sheet3.html non si apriranno quando i loro collegamenti verranno cliccati all'interno di Sheet1.html



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



 Ecco il codice di esempio completo che puoi eseguire con il file fornito[file excel di esempio](5115211.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
