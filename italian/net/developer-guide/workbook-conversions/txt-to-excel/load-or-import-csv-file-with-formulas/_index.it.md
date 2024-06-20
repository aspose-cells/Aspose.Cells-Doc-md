---
title: Carica o importa file CSV con formule
type: docs
weight: 350
url: /it/net/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

Il file CSV contiene principalmente dati testuali e non contiene formule. Tuttavia, a volte succede che i file CSV contengano anche formule. Tali file CSV dovrebbero essere caricati impostando [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) su **true**. Una volta impostata questa proprietà su **true**, Aspose.Cells non tratterà la formula come semplice testo. Saranno trattati come formula e il motore di calcolo delle formule di Aspose.Cells le elaborerà come al solito.

{{% /alert %}} 

Il codice seguente illustra come è possibile caricare e importare un file CSV con formule. È possibile utilizzare qualsiasi file CSV. A scopo illustrativo, utilizziamo il [semplice file CSV](5115034.csv) che contiene questi dati. Come puoi vedere contiene una formula.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



Il codice carica prima il file CSV, poi lo importa nuovamente nella cella D4. Infine, salva l'oggetto del foglio di lavoro in formato XSLX. Il [file XLSX in output](5115052.xlsx) appare così. Come si vede, le celle C3 e F4 contengono una formula e il suo risultato è 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

