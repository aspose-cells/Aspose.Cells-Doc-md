---
title: Iniziare
type: docs
weight: 10
url: /it/cpp/getting-started/
description: Come installare Aspose Cells for C++ e creare un'applicazione Hello World.
---
{{% alert color="primary" %}} 

Questa pagina ti mostrerà come installare Aspose Cells for C++ e creare un'applicazione Hello World.

{{% /alert %}}

## **Installazione**

### **Installa Aspose Cells tramite NuGet**

 NuGet è il modo più semplice per scaricare e installare Aspose.Cells for C++.
1. Creare un progetto Visual Studio Microsoft for C++.
2. Includere il file di intestazione "Aspose.Cells.h".
3. Aprire Microsoft Visual Studio e NuGet gestore pacchetti.
4. Cerca "aspose.cells.cpp" per trovare il Aspose.Cells for C++ desiderato.
5. Fare clic su "Installa", Aspose.Cells for C++ verrà scaricato e referenziato nel progetto.

**![Installa da Aspose Cells a NuGet](InstallThroughNuget.png)**

 Puoi anche scaricarlo dalla pagina web nuget per aspose.cells:
[Aspose.Cells for C++ NuGet Confezione](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Più passo per i dettagli](/cells/it/cpp/installation/)

### **Una demo per l'utilizzo di Aspose.Cells for C++ su Windows**

1. Scarica Aspose.Cells for C++ dalla seguente pagina:
[Scarica Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Decomprimi il pacchetto e troverai una demo che spiega come utilizzare Aspose.Cells for C++.
3. Aprire Demo.sln con Visual Studio 2017 o versione successiva
4. main.cpp: questo file mostra come codificare per testare Aspose.Cells for C++
 5. sourceFile/resultFile: queste due cartelle sono directory di archiviazione utilizzate in main.cpp

### **Come utilizzare Aspose.Cells for C++ su sistema operativo Linux**

1. Scarica Aspose.Cells for C++ dalla seguente pagina:
[Scarica Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. Decomprimi il pacchetto e troverai una Demo che spiega come usare Aspose.Cells for C++ per Linux.
3. Esegui "cd Demo" nella riga di comando di Linux
4. Esegui "rm -rf build;mkdir build;cd build"
5. Esegui "cmake .." creerà un Makefile da CMakeLists.txt nella cartella Demo
6. Eseguire "make" per compilare
 7. Esegui "./demo" vedrai il risultato

## **Creazione dell'applicazione Hello World**

passaggi seguenti creano l'applicazione Hello World utilizzando Aspose.Cells API:

1.  Crea un'istanza di[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe.
1.  Se hai una licenza, allora[applicarlo](/cells/it/cpp/licensing/).
 Se stai utilizzando la versione di valutazione, salta le righe di codice relative alla licenza.
1. Accedi a qualsiasi cella desiderata di un foglio di lavoro nel file Excel.
1. Inserisci le parole "**Hello World!**" in una cella a cui si accede.
1. Genera il file Excel Microsoft modificato.

L'implementazione dei passaggi precedenti è dimostrata negli esempi seguenti.

### **Esempio di codice: creazione di una nuova cartella di lavoro**

L'esempio seguente crea una nuova cartella di lavoro da zero, inserisce "**Hello World!**" nella cella A1 del primo foglio di lavoro e salva il file Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1.cpp" >}}

### **Esempio di codice: apertura di un file esistente**

L'esempio seguente apre un file modello Excel Microsoft esistente, ottiene una cella e controlla il valore nella cella A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1.cpp" >}}
