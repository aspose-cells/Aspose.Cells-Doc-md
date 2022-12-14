---
title: Carica o importa file CSV con formule
type: docs
weight: 350
url: /it/net/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 Il file CSV contiene principalmente dati testuali e non contengono formule. Tuttavia, a volte capita che i file CSV contengano anche formule. Tali file CSV devono essere caricati impostando l'estensione[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) come**VERO** . Una volta impostata questa proprietà**VERO**, Aspose.Cells non considererà la formula come semplice testo. Saranno trattati come formula e il motore di calcolo della formula Aspose.Cells li elaborerà come al solito.

{{% /alert %}} 

 Il codice seguente illustra come caricare e importare un file CSV con formule. Puoi utilizzare qualsiasi file CSV. A scopo illustrativo, utilizziamo il[semplice file csv](5115034.csv) che contiene questi dati. Come vedi contiene una formula.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



 Il codice carica prima il file CSV, quindi lo importa nuovamente nella cella D4. Infine, salva l'oggetto cartella di lavoro in formato XSLX. Il[file XLSX di output](5115052.xlsx) Somiglia a questo. Come vedi le celle C3 e F4 contengono la formula e il suo risultato 800.

|![cose da fare:immagine_alt_testo](load-or-import-csv-file-with-formulas_1.png)|
|:- |

