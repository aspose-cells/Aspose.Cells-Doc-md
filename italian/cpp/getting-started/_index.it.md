---
title: Iniziare
type: docs
weight: 10
url: /it/cpp/getting-started/
description: Come installare Aspose Cells per C++ e creare un applicazione Hello World.
---

{{% alert color="primary" %}} 

Questa pagina ti mostrerà come installare Aspose Cells per C++ e creare un'applicazione Hello World.

{{% /alert %}}

## **Installazione**

### **Installa Aspose Cells tramite NuGet**

NuGet è il modo più semplice per scaricare e installare Aspose.Cells for C++. 
1. Crea un progetto Microsoft Visual Studio per C++.
2. Includi il file di intestazione "Aspose.Cells.h".
3. Apre Microsoft Visual Studio e il gestore dei pacchetti NuGet.
4. Cerca "aspose.cells.cpp" per trovare il desiderato Aspose.Cells for C++. 
5. Fai clic su "Installa", verrà scaricato e referenziato nel tuo progetto il Aspose.Cells for C++.

**![Installa Aspose Cells tramite NuGet](InstallThroughNuget.png)**

Puoi anche scaricarlo dalla pagina web di NuGet per aspose.cells: 
[Pacchetto NuGet Aspose.Cells for C++](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Ulteriori passaggi per i dettagli](/cells/it/cpp/installation/)

### **Un esempio per l'uso di Aspose.Cells for C++ su Windows**

1. Scarica Aspose.Cells for C++ dalla seguente pagina:
[Scarica Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Decomprimi il pacchetto e troverai un esempio su come utilizzare il Aspose.Cells for C++.
3. Apri il file example.sln con Visual Studio 2017 o versioni successive
4. main.cpp: questo file mostra come codificare per testare il Aspose.Cells for C++

### **Un esempio per l'uso di Aspose.Cells for C++ su Linux**

1. Scarica Aspose.Cells for C++ dalla seguente pagina:
[Scarica Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. Decomprimi il pacchetto e troverai un esempio su come utilizzare il Aspose.Cells for C++ per Linux.
3. Assicurati di trovarti nel percorso in cui si trova l'esempio.
4. Esegui "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Esegui "cmake --build example/build"

### **Un esempio per l'uso di Aspose.Cells for C++ su Mac OS**

1. Scarica Aspose.Cells for C++ dalla seguente pagina:
[Scarica Aspose.Cells for C++ (MacOS)](https://downloads.aspose.com/cells/cpp/)
2. Decomprimi il pacchetto e troverai un esempio su come utilizzare Aspose.Cells for C++ per MacOS.
3. Assicurati di trovarti nel percorso in cui si trova l'esempio.
4. Esegui "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Esegui "cmake --build example/build"

## **Creazione dell'applicazione Hello World**

I passi seguenti creano l'applicazione Hello World utilizzando l'API Aspose.Cells:

1. Crea un'istanza della classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. Se hai una licenza, [applicala](/cells/it/cpp/licensing/).
   Se stai utilizzando la versione di valutazione, salta le righe di codice relative alla licenza.
1. Accedi a qualsiasi cella desiderata di un foglio di lavoro nel file di Excel.
1. Inserisci le parole "**Hello World!**" in una cella accessibile.
1. Genera il file modificato di Microsoft Excel.

L'implementazione dei passaggi sopra è dimostrata negli esempi seguenti.

### **Esempio di codice: Creazione di un nuovo workbook**

Nell'esempio seguente viene creato un nuovo workbook da zero, inserisce "**Hello World!**" nella cella A1 del primo foglio di lavoro e salva il file di Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

### **Esempio di codice: Apertura di un file esistente**

Nell'esempio seguente viene aperto un modello di file di Excel esistente, viene presa una cella e viene controllato il valore nella cella A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
