---
title: Carica o importa file CSV con formule
type: docs
weight: 500
url: /it/java/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

Il file CSV contiene principalmente dati testuali e non contiene formule. Tuttavia, a volte i file CSV contengono anche formule. Tali file CSV devono essere caricati impostando [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) su **true**. Una volta impostata questa proprietà su **true**, Aspose.Cells non tratterà le formule come semplice testo. Saranno trattati come formule e il motore di calcolo delle formule di Aspose.Cells le elaborerà come al solito.

{{% /alert %}} 
## **Carica o importa file CSV con formule**
Il codice seguente illustra come è possibile caricare e importare un file CSV con formule. È possibile utilizzare qualsiasi file CSV. A scopo illustrativo, utilizziamo il [file CSV semplice](5472505.csv) che contiene questi dati. Come puoi vedere, contiene una formula.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

Il codice carica prima il file CSV, quindi lo importa nuovamente nella cella D4. Infine, salva l'oggetto workbook in formato XSLX. Il [file XLSX di output](5472503.xlsx) appare come questo. Come puoi vedere, la cella C3 e la F4 contengono una formula e il suo risultato 800.

![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
