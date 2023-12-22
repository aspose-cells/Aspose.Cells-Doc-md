---
title: Iniziare
type: docs
weight: 10
url: /it/net/getting-started/
---
{{% alert color="primary" %}} 

Questa pagina ti mostrerà come installare Aspose Cells e creare un'applicazione Hello World.

{{% /alert %}}

##  **Installazione**

###  **Installare da Aspose.Cells a NuGet**

 NuGet è il modo più semplice per scaricare e installare Aspose.Cells for .NET.

1.  Apri Microsoft Visual Studio e NuGet gestore pacchetti.
1.  Cerca "aspose.cells" per trovare lo Aspose.Cells for .NET desiderato.
1. Fai clic su "Installa", Aspose.Cells for .NET verrà scaricato e referenziato nel tuo progetto.
**![Installa da Aspose a Cells fino a NuGet](install-through-nuget.png)**

 Puoi anche scaricarlo dalla pagina web nuget per aspose.cells:
[Aspose.Cells for .NET NuGet Pacchetto](https://www.nuget.org/packages/Aspose.Cells/)

[Ulteriori passaggi per i dettagli](/cells/it/net/installation/)

###  **Installa Aspose.Cells su Windows**

1. Scaricare Aspose.Cells.msi dalla seguente pagina:
[Scarica Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. Fare doppio clic su Aspose Cells msi e seguire le istruzioni per installarlo:

**![Installa Aspose Cells su Windows](install-on-windows.png)**

[Ulteriori passaggi per i dettagli](/cells/it/net/installing-aspose-cells-on-windows/)

###  **Installa Aspose.Cells su Linux**

In questo esempio, utilizzo Ubuntu per mostrare come iniziare a utilizzare Aspose.Cells su Linux.

1. Crea un'applicazione .netcore, denominata "AsposeCellsTest".
2. Apri il file "AsposeCellsTest.csproj", aggiungi le seguenti righe per i riferimenti al pacchetto Aspose.Cells:
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="23.12" />
  </ItemGroup>
{{< /highlight >}}
3. Apri il progetto con VSCode su Ubuntu:
**![Installa Aspose Cells su linux](install-on-linux.png)**
4. eseguire il test con il seguente codice:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Nota: Aspose.Cells per .NetStandard può supportare i tuoi requisiti su Linux.

Si applica a: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 e versione avanzata.

###  **Installa Aspose.Cells su MAC OS**

In questo esempio utilizzo macOS High Sierra per mostrare come iniziare a utilizzare Aspose.Cells su MAC OS.

1. Crea un'applicazione .netcore, denominata "AsposeCellsTest".
2. Apri l'applicazione con Visual Studio per Mac, quindi installa da Aspose a Cells fino a NuGet:
**![Installa Aspose Cells su macOS](install-on-mac-os.png)**
3. eseguire il test con il seguente codice:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Se è necessario utilizzare funzionalità relative al disegno, installare libgdiplus in macOS, vedere:
[Come installare libgdiplus su macOS](/cells/it/net/how-to-install-libgdiplus-in-macos/)

Nota: Aspose.Cells Per .NetStandard può supportare i tuoi requisiti su MAC OS.

Si applica a: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 e versione avanzata.

###  **[Esegui Aspose Cells in Docker](/cells/net/how-to-run-aspose-cells-in-docker/)**

###  **Come utilizzare la libreria grafica su piattaforme non Windows con Net6**

 Aspose.Cells per Net6 ora utilizza SkiaSharp come libreria grafica, come consigliato in[comunicato ufficiale del Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) . Per ulteriori dettagli sull'utilizzo di Aspose.Cells con NET6, vedere[Come eseguire Aspose.Cells per .Net6](/cells/it/net/how-to-run-aspose-cells-for-net6/).

##  **Creazione dell'applicazione Hello World**

I passaggi seguenti creano l'applicazione Hello World utilizzando Aspose.Cells API:

1.  Se hai la licenza, allora[applicarlo](/cells/it/net/licensing/).
 Se stai utilizzando la versione di valutazione, salta le righe di codice relative alla licenza.
1.  Crea un'istanza di[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook) class per creare un nuovo file Excel o aprire un file Excel esistente.
1. Accedi a qualsiasi cella desiderata di un foglio di lavoro nel file Excel.
1.  Inserisci le parole**Hello World!** in una cella a cui si accede.
1. Genera il file Excel Microsoft modificato.

L'implementazione dei passaggi precedenti è dimostrata negli esempi seguenti.

###  **Esempio di codice: creazione di una nuova cartella di lavoro**

L'esempio seguente crea una nuova cartella di lavoro da zero, inserisce "Hello World!" nella cella A1 nel primo foglio di lavoro e salva come file Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **Esempio di codice: apertura di un file esistente**

L'esempio seguente apre un file modello Excel Microsoft esistente "Sample.xlsx", inserisce "Hello World!" nella cella A1 nel primo foglio di lavoro e salva come file Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
