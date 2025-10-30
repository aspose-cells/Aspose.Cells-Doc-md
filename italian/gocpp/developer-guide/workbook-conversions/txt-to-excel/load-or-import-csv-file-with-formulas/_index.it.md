---
title: Carica o importa un file CSV con formule usando C++
linktitle: Carica o importa file CSV con formule
type: docs
weight: 350
url: /it/go-cpp/load-or-import-csv-file-with-formulas/
description: Carica o importa un file CSV contenente formule usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}} 

I file CSV contengono principalmente dati testuali e di solito non includono formule. Tuttavia, ci sono casi in cui i file CSV potrebbero contenere formule. Questi file CSV dovrebbero essere caricati impostando [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/go-cpp/txtloadoptions/gethasformula/) su **true**. Una volta impostata questa proprietà su **true**, Aspose.Cells non tratterà le formule come testo semplice. Verranno trattate come formule e il motore di calcolo delle formule di Aspose.Cells le elaborerà normalmente.

{{% /alert %}} 

Il seguente esempio illustra come puoi caricare e importare un file CSV con formule. Puoi usare qualsiasi file CSV. Per scopi esemplificativi, utilizziamo il [semplice file csv](5115034.csv) che contiene questi dati. Come puoi vedere, contiene una formula.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadOrImportCsvFileWithFormulas.go" >}}
Il codice prima carica il file CSV, poi lo importa di nuovo in cella D4. Infine, salva l'oggetto workbook in formato XLSX. Il [file XLSX di output](5115052.xlsx) risulta così. Come puoi vedere, le celle C3 e F4 contengono formule e il loro risultato è 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
