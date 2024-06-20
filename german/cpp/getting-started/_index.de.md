---
title: Erste Schritte
type: docs
weight: 10
url: /de/cpp/getting-started/
description: Anleitung zur Installation von Aspose Cells für C++ und Erstellung einer Hello World Anwendung.
---

{{% alert color="primary" %}} 

Diese Seite zeigt Ihnen, wie Sie Aspose Cells für C++ installieren und eine Hello World-Anwendung erstellen können.

{{% /alert %}}

## **Installation**

### **Installieren Sie Aspose Cells über NuGet.**

NuGet ist der einfachste Weg, um Aspose.Cells for C++ herunterzuladen und zu installieren. 
1. Erstellen Sie ein Microsoft Visual Studio-Projekt für C++.
2. Binden Sie die Header-Datei "Aspose.Cells.h" ein.
3. Öffnen Sie Microsoft Visual Studio und den NuGet-Paket-Manager.
4. Suchen Sie nach "aspose.cells.cpp", um den gewünschten Aspose.Cells for C++ zu finden. 
5. Klicken Sie auf "Installieren", Aspose.Cells for C++ wird heruntergeladen und in Ihrem Projekt referenziert.

**![Aspose Cells über NuGet installieren](InstallThroughNuget.png)**

Sie können es auch von der NuGet-Webseite für aspose.cells herunterladen: 
[Aspose.Cells for C++ NuGet-Paket](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Weitere Schritte für Details](/cells/de/cpp/installation/)

### **Eine Demo zur Verwendung von Aspose.Cells for C++ unter Windows**

1. Laden Sie Aspose.Cells for C++ von der folgenden Seite herunter:
[Aspose.Cells for C++ herunterladen (Windows)](https://downloads.aspose.com/cells/cpp/)
2. Entpacken Sie das Paket, und Sie finden ein Beispiel, wie man Aspose.Cells for C++ verwendet.
3. Öffnen Sie die example.sln mit Visual Studio 2017 oder einer höheren Version.
4. main.cpp: Diese Datei zeigt, wie man den Code zum Testen von Aspose.Cells for C++ schreibt.

### **Eine Demo zur Verwendung von Aspose.Cells for C++ unter Linux.**

1. Laden Sie Aspose.Cells for C++ von der folgenden Seite herunter:
[Aspose.Cells for C++(Linux) herunterladen](https://downloads.aspose.com/cells/cpp/)
2. Entpacken Sie das Paket, und Sie finden ein Beispiel, wie man Aspose.Cells for C++ für Linux verwendet.
3. Stellen Sie sicher, dass Sie sich im Pfad befinden, in dem das Beispiel liegt.
4. Führen Sie "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release" aus.
5. Führen Sie "cmake --build example/build" aus.

### **Eine Demo zur Verwendung von Aspose.Cells for C++ unter Mac OS.**

1. Laden Sie Aspose.Cells for C++ von der folgenden Seite herunter:
[Aspose.Cells for C++(MacOS) herunterladen](https://downloads.aspose.com/cells/cpp/)
2. Entpacken Sie das Paket, und Sie finden ein Beispiel, wie man Aspose.Cells for C++ für MacOS verwendet.
3. Stellen Sie sicher, dass Sie sich im Pfad befinden, in dem das Beispiel liegt.
4. Führen Sie "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release" aus.
5. Führen Sie "cmake --build example/build" aus.

## **Erstellen der Hello World-Anwendung**

Die folgenden Schritte erstellen die Hello World-Anwendung unter Verwendung der Aspose.Cells API:

1. Erstellen Sie eine Instanz der [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-Klasse.
1. Wenn Sie eine Lizenz haben, [wenden Sie sie an](/cells/de/cpp/licensing/).
   Wenn Sie die Evaluierungsversion verwenden, überspringen Sie die Lizenz-bezogenen Codezeilen.
1. Greifen Sie auf eine beliebige Zelle einer Arbeitsmappe in der Excel-Datei zu.
1. Fügen Sie die Wörter "**Hallo Welt!**" in eine aufgerufene Zelle ein.
1. Generieren Sie die modifizierte Microsoft Excel-Datei.

Die Implementierung der obigen Schritte wird in den folgenden Beispielen demonstriert.

### **Codesample: Erstellen einer neuen Arbeitsmappe**

In folgendem Beispiel wird eine neue Arbeitsmappe von Grund auf erstellt, "**Hallo Welt!**" in Zelle A1 im ersten Arbeitsblatt eingefügt und die Excel-Datei gespeichert.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

### **Codesample: Öffnen einer vorhandenen Datei**

Im folgenden Beispiel wird eine vorhandene Microsoft Excel-Vorlagendatei geöffnet, eine Zelle abgerufen und der Wert in der Zelle A1 überprüft.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
