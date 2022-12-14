---
title: Carica o importa file CSV con formule
type: docs
weight: 500
url: /it/java/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 Il file CSV contiene principalmente dati testuali e non contengono formule. Tuttavia a volte capita che i file CSV contengano anche formule. Tali file CSV devono essere caricati impostando l'estensione[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) a**VERO** . Una volta impostata questa proprietà su**VERO**, Aspose.Cells non considererà la formula come semplice testo. Saranno trattati come formula e il motore di calcolo della formula Aspose.Cells li elaborerà come al solito.

{{% /alert %}} 
## **Carica o importa file CSV con formule**
 Il codice seguente illustra come caricare e importare un file CSV con formule. Puoi utilizzare qualsiasi file CSV. A scopo illustrativo, utilizziamo il[semplice file csv](5472505.csv) che contiene questi dati. Come vedi contiene una formula.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

 Il codice carica prima il file CSV, quindi lo importa nuovamente nella cella D4. Infine, salva l'oggetto cartella di lavoro in formato XSLX. Il[file XLSX di output](5472503.xlsx) Somiglia a questo. Come vedi la cella C3 e F4 contiene la formula e il suo risultato 800.

![cose da fare:immagine_alt_testo](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
