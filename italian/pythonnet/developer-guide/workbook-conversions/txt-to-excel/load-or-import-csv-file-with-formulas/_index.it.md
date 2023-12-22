---
title: Carica o importa il file CSV con le formule
type: docs
weight: 350
url: /it/python-net/load-or-import-csv-file-with-formulas/
description: Carica o importa il file CSV con le formule utilizzando Aspose.Cells for Python via .NET API.
keywords: Python Load or Import CSV file with Formulas, Convert CSV with Formulas to Excel in Python via NET, Python convert CSV with Formulas to xlsx, Load CSV with Formulas to Excel file.
---
{{% alert color="primary" %}} 

 CSV il file contiene principalmente dati testuali e non contengono formule. Tuttavia, a volte capita che i file CSV contengano anche formule. Tali file CSV devono essere caricati impostando l'estensione[TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) come *vero**. Una volta impostata questa proprietà *true**, Aspose.Cells non tratterà la formula come testo semplice. Verranno trattati come formule e il motore di calcolo delle formule Aspose.Cells li elaborerà come al solito.

{{% /alert %}} 

 Il codice seguente illustra come caricare e importare un file CSV con formule. È possibile utilizzare qualsiasi file CSV. A scopo illustrativo, utilizziamo il file[semplice file CSV](5115034.csv)che contiene questi dati. Come vedi contiene una formula.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



 Il codice carica prima il file CSV, quindi lo importa nuovamente nella cella D4. Infine, salva l'oggetto cartella di lavoro in formato XSLX. IL[file di output XLSX](5115052.xlsx) Somiglia a questo. Come vedi, le celle C3 e F4 contengono la formula e il suo risultato 800.

|![cose da fare:immagine_alt_testo](load-or-import-csv-file-with-formulas_1.png)|
| :- |

