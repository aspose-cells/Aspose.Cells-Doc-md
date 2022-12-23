---
title: Einstieg
type: docs
weight: 10
url: /de/cpp/getting-started/
description: So installieren Sie Aspose Cells for C++ und erstellen eine Hello World-Anwendung.
---
{{% alert color="primary" %}} 

Auf dieser Seite erfahren Sie, wie Sie Aspose Cells for C++ installieren und eine Hello World-Anwendung erstellen.

{{% /alert %}}

## **Installation**

### **Installieren Sie Aspose Cells bis NuGet**

 NuGet ist der einfachste Weg, Aspose.Cells for C++ herunterzuladen und zu installieren.
1. Erstellen Sie ein Microsoft Visual Studio-Projekt for C++.
2. Header-Datei "Aspose.Cells.h" einbinden.
3. Öffnen Sie Microsoft Visual Studio und NuGet Paket-Manager.
4. Suchen Sie „aspose.cells.cpp“, um die gewünschte Aspose.Cells for C++ zu finden.
5. Klicken Sie auf „Installieren“, Aspose.Cells for C++ wird heruntergeladen und in Ihrem Projekt referenziert.

**![Installieren Sie Aspose Cells bis NuGet](InstallThroughNuget.png)**

 Sie können es auch von der nuget-Webseite für aspose.cells herunterladen:
[Aspose.Cells for C++ NuGet Paket](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Mehr Schritt für Details](/cells/de/cpp/installation/)

### **Eine Demo für die Verwendung von Aspose.Cells for C++ auf Windows**

1. Download Aspose.Cells for C++ von folgender Seite:
[Herunterladen Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Entpacken Sie das Paket und Sie finden eine Demo zur Verwendung von Aspose.Cells for C++.
3. Öffnen Sie die Demo.sln mit Visual Studio 2017 oder einer höheren Version
4. main.cpp: Diese Datei zeigt, wie man codiert, um Aspose.Cells for C++ zu testen
 5. sourceFile/resultFile: Diese beiden Ordner sind Speicherverzeichnisse, die in main.cpp verwendet werden

### **So verwenden Sie Aspose.Cells for C++ unter Linux OS**

1. Download Aspose.Cells for C++ von folgender Seite:
[Herunterladen Aspose.Cells for C++ (Linux)](https://downloads.aspose.com/cells/cpp/)
2. Entpacken Sie das Paket und Sie finden eine Demo, die zeigt, wie Sie Aspose.Cells for C++ für Linux verwenden.
3. Führen Sie „cd Demo“ in Ihrer Linux-Befehlszeile aus
4. Führen Sie "rm -rf build;mkdir build;cd build" aus
5. Führen Sie „cmake ..“ aus, um ein Makefile von CMakeLists.txt im Demo-Ordner zu erstellen
6. Führen Sie "make" zum Kompilieren aus
 7. Führen Sie „./demo“ aus, Sie werden das Ergebnis sehen

## **Erstellen der Hello World-Anwendung**

Die folgenden Schritte erstellen die Hello World-Anwendung unter Verwendung der Aspose.Cells API:

1.  Erstellen Sie eine Instanz der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse.
1.  Wenn Sie eine Lizenz haben, dann[Wende es an](/cells/de/cpp/licensing/).
 Wenn Sie die Evaluierungsversion verwenden, überspringen Sie die lizenzbezogenen Codezeilen.
1. Greifen Sie in der Excel-Datei auf eine beliebige Zelle eines Arbeitsblatts zu.
1. Fügen Sie die Wörter ein "**Hello World!**" in eine Zelle, auf die zugegriffen wird.
1. Generieren Sie die geänderte Excel-Datei Microsoft.

Die Implementierung der obigen Schritte wird in den folgenden Beispielen demonstriert.

### **Codebeispiel: Erstellen einer neuen Arbeitsmappe**

Das folgende Beispiel erstellt eine neue Arbeitsmappe von Grund auf, fügt "**Hello World!**" in die Zelle A1 auf dem ersten Arbeitsblatt und speichert die Excel-Datei.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1.cpp" >}}

### **Codebeispiel: Öffnen einer vorhandenen Datei**

Das folgende Beispiel öffnet eine vorhandene Excel-Vorlagendatei Microsoft, ruft eine Zelle ab und überprüft den Wert in Zelle A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1.cpp" >}}
