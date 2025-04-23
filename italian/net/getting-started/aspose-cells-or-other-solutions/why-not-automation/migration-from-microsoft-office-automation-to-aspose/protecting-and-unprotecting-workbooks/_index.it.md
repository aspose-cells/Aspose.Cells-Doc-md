---
title: Protezione e rimozione della protezione dei file di lavoro
type: docs
weight: 20
url: /it/net/protecting-and-unprotecting-workbooks/
---

{{% alert color="primary" %}} 

Per impedire a qualcuno di modificare, spostare o eliminare accidentalmente o deliberatamente i fogli di lavoro, è possibile proteggere gli elementi del libro con o senza una password. Per proteggere la struttura di un libro in modo che i fogli di lavoro nel libro non possano essere spostati, eliminati, nascosti, resi visibili o rinominati e nuovi fogli di lavoro non possano essere inseriti, specificare il tipo di protezione come Struttura.

Per proteggere le finestre in modo che siano delle stesse dimensioni e posizione ogni volta che il libro viene aperto, specificare il tipo di protezione come Finestre. In questo articolo, mostriamo come [proteggere](/cells/it/net/protecting-and-unprotecting-workbooks/) e [sbloccare](/cells/it/net/protecting-and-unprotecting-workbooks/) i libri utilizzando VSTO e Aspose.Cells for .NET per consentirti di confrontare i due metodi.

Aspose.Cells funziona indipendentemente dall'automazione di Microsoft Office ed è sviluppato per essere facile da usare e produrre del codice pulito.

Proteggere un libro non impedisce agli utenti di modificare le celle. Per proteggere i dati, è necessario proteggere i fogli di lavoro.

{{% /alert %}} 
## **Proteggere un Libro**
Per aprire un file esistente di Microsoft Excel, proteggere il libro con attributi di struttura e finestre e salvare il file.

Di seguito sono riportati frammenti di codice paralleli per VSTO (C#, VB) e Aspose.Cells for .NET (C#, VB) che mostrano come proteggere un libro.
### **VSTO**
**C#**

{{< highlight csharp >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath = @"d:\test\MyBook.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Protect the workbook specifying a password with Structure and Windows attributes.

excelApp.ActiveWorkbook.Protect("007", true, true);

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......


//Specify the template excel file path.

string myPath = @"d:\test\MyBook.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Protect the workbook specifying a password with Structure and Windows attributes.

workbook.Protect(ProtectionType.All,"007");

//Save As the excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}
## **Sbloccare un Libro**
Per sbloccare un libro, utilizzare le seguenti righe di codice per VSTO (C#, VB) e Aspose.Cells for .NET (C#, VB).
### **VSTO**
**C#**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

excelApp.ActiveWorkbook.Unprotect("007");



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

workbook.Unprotect("007");



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
