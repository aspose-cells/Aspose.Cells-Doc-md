---
title: Iniziare
type: docs
weight: 10
url: /it/net/getting-started/
---

{{% alert color="primary" %}} 

Questa pagina ti mostrerà come installare Aspose Cells e creare un'applicazione Hello World.

{{% /alert %}}

## **Installazione**

### **Installa Aspose.Cells tramite NuGet**

NuGet è il modo più semplice per scaricare e installare Aspose.Cells for .NET. 

1. Apri Microsoft Visual Studio e il gestore dei pacchetti NuGet. 
1. Cerca "aspose.cells" per trovare il Aspose.Cells for .NET desiderato. 
1. Fai clic su "Installa", Aspose.Cells for .NET verrà scaricato e referenziato nel tuo progetto.
**![Installa Aspose Cells tramite NuGet](install-through-nuget.png)**

Puoi anche scaricarlo dalla pagina web di NuGet per aspose.cells: 
[Pacchetto NuGet Aspose.Cells for .NET](https://www.nuget.org/packages/Aspose.Cells/)

[Ulteriori dettagli passo passo](/cells/it/net/installation/)

### **Installa Aspose.Cells su Windows**

1. Scarica Aspose.Cells.msi dalla seguente pagina:
[Scarica Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. Fai doppio clic su Aspose Cells msi e segui le istruzioni per installarlo:

**![Installa Aspose Cells su Windows](install-on-windows.png)**

[Ulteriori dettagli passo passo](/cells/it/net/installing-aspose-cells-on-windows/)

### **Installa Aspose.Cells su Linux**

In questo esempio, uso Ubuntu per mostrare come iniziare a utilizzare Aspose.Cells su Linux.

1. Crea un'applicazione .NET Core, chiamata "AsposeCellsTest".
2. Apri il file "AsposeCellsTest.csproj" e aggiungi le seguenti righe come riferimenti al pacchetto Aspose.Cells:
{{< highlight plain >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="25.10" />
  </ItemGroup>
{{< /highlight >}}
3. Apri il progetto con VSCode su Ubuntu:
**![Installa Aspose Cells su Linux](install-on-linux.png)**
4. esegui il test con il codice seguente:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Nota: Aspose.Cells per .NetStandard può supportare la tua richiesta su Linux.

Si applica a: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 e versioni avanzate.

### **Installa Aspose.Cells su MAC OS**

In questo esempio, utilizzo macOS High Sierra per mostrare come iniziare a utilizzare Aspose.Cells su MAC OS.

1. Crea un'applicazione .NET Core, chiamata "AsposeCellsTest".
2. Apri l'applicazione con Visual Studio for Mac, quindi installa Aspose Cells tramite NuGet:
**![Installa Aspose Cells su macOS](install-on-mac-os.png)**
3. esegui il test con il codice seguente:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Se hai bisogno di utilizzare funzionalità relative ai disegni, installa libgdiplus su macOS, vedi:
[Come installare libgdiplus su macOS](/cells/it/net/how-to-install-libgdiplus-in-macos/)

Nota: Aspose.Cells per .NetStandard può supportare la tua richiesta su MAC OS.

Si applica a: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 e versioni avanzate.

### [**Run Aspose Cells in Docker**](/cells/it/net/how-to-run-aspose-cells-in-docker/)

### **Come utilizzare la libreria grafica su piattaforme non Windows con Net6**

Aspose.Cells per Net6 ora utilizza SkiaSharp come libreria grafica, come consigliato nella [dichiarazione ufficiale di Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md). Per ulteriori dettagli sull'utilizzo di Aspose.Cells con NET6, consulta [Come eseguire Aspose.Cells per .Net6](/cells/it/net/how-to-run-aspose-cells-for-net6/).

## **Creazione dell'applicazione Hello World**

I passi seguenti creano l'applicazione Hello World utilizzando l'API Aspose.Cells:

1. Se hai una licenza, quindi [applicala](/cells/it/net/licensing/).
   Se stai utilizzando la versione di valutazione, salta le righe di codice relative alla licenza.
1. Crea un'istanza della classe [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) per creare un nuovo file Excel, o apri un file Excel esistente.
1. Accedi a qualsiasi cella desiderata di un foglio di lavoro nel file di Excel.
1. Inserisci le parole **Hello World!** in una cella accessibile.
1. Genera il file modificato di Microsoft Excel.

L'implementazione dei passaggi sopra è dimostrata negli esempi seguenti.

### **Esempio di codice: Creazione di un nuovo workbook**

Nell'esempio seguente si crea un nuovo workbook da zero, si inserisce "Hello World!" nella cella A1 nel primo foglio di lavoro e si salva come file Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Esempio di codice: Apertura di un file esistente**

L'esempio seguente apre un file modello esistente di Microsoft Excel "Sample.xlsx", inserisce "Ciao mondo!" nella cella A1 nel primo foglio di lavoro e salva come file Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
