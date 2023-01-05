---
title: Pubblico API Modifiche Aspose.Cells 8.3.1
type: docs
weight: 110
url: /it/net/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.3.0 alla 8.3.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni.

{{% /alert %}} 
## **API aggiunte**
### **Proprietà DataLabels.ShowCellRange Aggiunta**
 La proprietà ShowCellRange è stata aggiunta alla classe DataLabels per imitare la funzionalità di Excel di formattazione delle etichette dati del grafico in fase di esecuzione. Si prega di notare che Excel fornisce questa funzione attraverso i seguenti passaggi.

1. Seleziona Etichette dati della serie e fai clic con il pulsante destro del mouse per aprire il menu a comparsa.
1.  Clicca il**Formato etichette dati...** e lo mostrerà**Opzioni etichetta**.
1.  Selezionare o deselezionare la casella di controllo**L'etichetta contiene - Valore da Cells**.

 Il codice di esempio riportato di seguito accede alle etichette dei dati della serie di grafici e quindi imposta il metodo DataLabels.ShowCellRange su true per imitare la funzionalità di Excel di**L'etichetta contiene - Valore da Cells**.

**C#**

{{< highlight "csharp" >}}

 //Create workbook from the source Excel file

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.NSeries[0].DataLabels;

dataLabels.ShowCellRange = true;

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}



'Create workbook from the source Excel file

Dim m_workbook As Workbook = New Workbook("sample.xlsx")

'Access the first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the chart inside the worksheet

Dim m_chart As Chart = m_worksheet.Charts(0)

'Check the "Label Contains - Value From Cells"

Dim m_dataLabels As DataLabels = m_chart.NSeries(0).DataLabels

m_dataLabels.ShowCellRange = True

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo[Visualizzazione dell'intervallo Cell come etichette dati](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels) per maggiori informazioni.

{{% /alert %}} 

### **Metodi Cell.GetTable e ListObject.PutCellValue aggiunti**
metodi Cell.GetTable & ListObject.PutCellValue sono stati aggiunti con Aspose.Cells for .NET 8.3.1 per facilitare agli utenti l'accesso al ListObject da una cella e l'aggiunta di valori al suo interno utilizzando gli offset di riga e colonna. Il codice di esempio seguente carica il foglio di calcolo di origine e aggiunge i valori all'interno della tabella.

**C#**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell D5 which lies inside the table

Cell cell = worksheet.Cells["D5"];

//Put value inside the cell D5

cell.PutValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.GetTable();

//Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access cell D5 which lies inside the table

Dim m_cell As Cell = m_worksheet.Cells("D5")

'Put value inside the cell D5

m_cell.PutValue("D5 Data")

'Access the Table from this cell

Dim table As ListObject = m_cell.GetTable()

'Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]")

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo[Accesso alla tabella da Cell e aggiunta di valori al suo interno utilizzando gli offset di righe e colonne](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets) per maggiori informazioni.

{{% /alert %}} 

### **Proprietà OdsSaveOptions.IsStrictSchema11 Aggiunta**
La proprietà IsStrictSchema11 è stata aggiunta alla classe OdsSaveOptions per consentire agli sviluppatori di salvare il foglio di calcolo in formato conforme alla specifica ODF v1.2. Il valore predefinito della proprietà IsStrictSchema11 è false, significa che dalla versione 8.3.1 delle API Aspose.Cells i file ODS verranno salvati come formato ODF versione 1.2 per impostazione predefinita.

Il frammento di codice fornito di seguito salva il file ODS in formato ODF 1.2.

**C#**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some value in cell A1

Cell cell = worksheet.Cells["A1"];

cell.PutValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.Save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.IsStrictSchema11 = true;

workbook.Save("ODF1.1.ods", options);


{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Create workbook 

Dim m_workbook As Workbook = New Workbook()

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Put some value in cell A1

Dim m_cell As Cell = m_worksheet.Cells("A1")

m_cell.PutValue("Welcome to Aspose!")

'Save ODS in ODF 1.2 version which is default

Dim options As OdsSaveOptions = New OdsSaveOptions()

m_workbook.Save("ODF1.2.ods", options)

'Save ODS in ODF 1.1 version

options.IsStrictSchema11 = True

m_workbook.Save("ODF1.1.ods", options)

{{< /highlight >}}

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo[Salva il file ODS nelle specifiche ODF 1.1 e 1.2](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications) per maggiori informazioni.

{{% /alert %}} 

### **Metodo SparklineCollection.Add Aggiunto**
 Aspose.Cells Le API hanno esposto il metodo SparklineCollection.Add(string dataRange, int row, int column) per specificare l'intervallo di dati e la posizione del gruppo Sparkline. Si noti che Excel fornisce la stessa funzionalità attraverso i seguenti passaggi.

1. Seleziona la cella contenente il tuo Sparkline.
1.  Selezionare**Modifica i dati dalla sparkline** sezione all'interno del**Design** scheda
1.  Scegliere**Modifica la posizione e i dati del gruppo**.
1.  Specificare**Intervallo di dati** & **Posizione**.

 Il seguente codice di esempio carica il foglio di calcolo di origine, accede al primo gruppo sparkline e aggiunge nuovi intervalli di dati e posizioni per il gruppo sparkline.

**C#**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first sparkline group

SparklineGroup group = worksheet.SparklineGroupCollection[0];

//Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15);

group.SparklineCollection.Add("D6:O6", 5, 15);

group.SparklineCollection.Add("D7:O7", 6, 15);

group.SparklineCollection.Add("D8:O8", 7, 15);

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the first sparkline group

Dim group As SparklineGroup = m_worksheet.SparklineGroupCollection(0)

'Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15)

group.SparklineCollection.Add("D6:O6", 5, 15)

group.SparklineCollection.Add("D7:O7", 6, 15)

group.SparklineCollection.Add("D8:O8", 7, 15)

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo[Copia sparkline specificando l'intervallo di dati e la posizione del gruppo sparkline](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) per maggiori informazioni.

{{% /alert %}}
