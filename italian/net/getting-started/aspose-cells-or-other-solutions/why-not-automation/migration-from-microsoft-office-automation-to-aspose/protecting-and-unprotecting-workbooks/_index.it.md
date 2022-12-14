---
title: Protezione e rimozione della protezione delle cartelle di lavoro
type: docs
weight: 20
url: /it/net/protecting-and-unprotecting-workbooks/
---
{{% alert color="primary" %}} 

Per impedire a qualcuno di modificare, spostare o eliminare accidentalmente o deliberatamente i fogli di lavoro, è possibile proteggere gli elementi della cartella di lavoro con o senza password. Per proteggere la struttura di una cartella di lavoro in modo che i fogli di lavoro nella cartella di lavoro non possano essere spostati, eliminati, nascosti, scoperti o rinominati e non possano essere inseriti nuovi fogli di lavoro, specificare ProtectionType come Structure.

 Per proteggere Windows in modo che abbiano le stesse dimensioni e posizione ogni volta che viene aperta la cartella di lavoro, specificare il ProtectionType come Windows. In questo articolo viene mostrato come[proteggere](/cells/it/net/protecting-and-unprotecting-workbooks/) e[Non protetto](/cells/it/net/protecting-and-unprotecting-workbooks/) cartelle di lavoro che utilizzano VSTO e Aspose.Cells for .NET per confrontare i due metodi.

Aspose.Cells funziona indipendentemente da Microsoft Office Automation ed è sviluppato per essere facile da usare e produrre codice ordinato.

La protezione di una cartella di lavoro non impedisce agli utenti di modificare le celle. Per proteggere i dati, è necessario proteggere i fogli di lavoro.

{{% /alert %}} 
## **Protezione di una cartella di lavoro**
Per aprire un file Excel Microsoft esistente, proteggere la cartella di lavoro con la struttura e gli attributi Windows e salvare il file.

Di seguito sono riportati frammenti di codice paralleli per VSTO (C#, VB) e Aspose.Cells for .NET (C#, VB) che mostrano come proteggere una cartella di lavoro.
### **VSTO**
**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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
## **Rimozione della protezione di una cartella di lavoro**
Per rimuovere la protezione di una cartella di lavoro, utilizzare le seguenti righe di codice per VSTO (C#, VB) e Aspose.Cells for .NET (C#, VB).
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

excelApp.ActiveWorkbook.Unprotect("007");



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

workbook.Unprotect("007");



{{< /highlight >}}
