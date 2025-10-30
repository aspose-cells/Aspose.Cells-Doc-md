---
title: Carica o importa file CSV con formule
type: docs
weight: 350
url: /it/python-net/load-or-import-csv-file-with-formulas/
description: Carica o importa un file CSV con formule utilizzando Aspose.Cells for Python via .NET API.
keywords: Python carica o importa un file CSV con formule, converti CSV con formule in Excel in Python via NET, Python converti CSV con formule in xlsx, Carica CSV con formule nel file Excel.
---

{{% alert color="primary" %}} 

Il file CSV contiene principalmente dati testuali e non contiene formule. Tuttavia, a volte accade che i file CSV contengano anche formule. Tali file CSV devono essere caricati impostando la [TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) su **true**. Una volta impostata questa proprietà su **true**, Aspose.Cells non tratterà la formula come testo semplice. Saranno trattati come formula e il motore di calcolo delle formule di Aspose.Cells le elaborerà come al solito.

{{% /alert %}} 

Il codice seguente illustra come è possibile caricare e importare un file CSV con formule. È possibile utilizzare qualsiasi file CSV. A scopo illustrativo, utilizziamo il [semplice file CSV](5115034.csv) che contiene questi dati. Come puoi vedere contiene una formula.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



Il codice carica prima il file CSV, poi lo importa nuovamente nella cella D4. Infine, salva l'oggetto del foglio di lavoro in formato XSLX. Il [file XLSX in output](5115052.xlsx) appare così. Come si vede, le celle C3 e F4 contengono una formula e il suo risultato è 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

{{< app/cells/assistant language="python-net" >}}
