---
title: Erste Schritte
type: docs
weight: 10
url: /de/cpp/getting-started/
description: So installieren Sie Aspose Cells for C++ und erstellen eine Hello World-Anwendung.
---
{{% alert color="primary" %}} 

Auf dieser Seite erfahren Sie, wie Sie Aspose Cells for C++ installieren und eine Hello World-Anwendung erstellen.

{{% /alert %}}

##  **Installation**

###  **Installieren Sie Aspose Cells bis NuGet**

 NuGet ist der einfachste Weg, Aspose.Cells for C++ herunterzuladen und zu installieren.
1. Erstellen Sie ein Microsoft Visual Studio-Projekt for C++.
2. Header-Datei „Aspose.Cells.h“ einbinden.
3. Öffnen Sie Microsoft Visual Studio und NuGet Paketmanager.
 4. Durchsuchen Sie „aspose.cells.cpp“, um die gewünschte Aspose.Cells for C++ zu finden.
5. Klicken Sie auf „Installieren“. Aspose.Cells for C++ wird heruntergeladen und in Ihrem Projekt referenziert.

**![Aspose Cells bis NuGet installieren](InstallThroughNuget.png)**

 Sie können es auch von der Webseite nuget für aspose.cells herunterladen:
[Aspose.Cells for C++ NuGet Paket](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Weitere Schritte für Details](/cells/de/cpp/installation/)

###  **Eine Demo für die Verwendung von Aspose.Cells for C++ auf Windows**

1. Laden Sie Aspose.Cells for C++ von der folgenden Seite herunter:
[Herunterladen Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Entpacken Sie das Paket und Sie finden ein Beispiel für die Verwendung von Aspose.Cells for C++.
3. Öffnen Sie die Datei „example.sln“ mit Visual Studio 2017 oder einer höheren Version
4. main.cpp: Diese Datei zeigt, wie man codiert, um Aspose.Cells for C++ zu testen

###  **Eine Demo zur Verwendung von Aspose.Cells for C++ unter Linux**

1. Laden Sie Aspose.Cells for C++ von der folgenden Seite herunter:
[Herunterladen Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. Entpacken Sie das Paket und Sie finden ein Beispiel für die Verwendung von Aspose.Cells for C++ für Linux.
3. Stellen Sie sicher, dass Sie sich im Pfad befinden, in dem sich das Beispiel befindet.
4. Führen Sie „cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release“ aus.
5. Führen Sie „cmake --build example/build“ aus.

###  **Eine Demo zur Verwendung von Aspose.Cells for C++ unter Mac OS**

1. Laden Sie Aspose.Cells for C++ von der folgenden Seite herunter:
[Herunterladen Aspose.Cells for C++(MacOS)](https://downloads.aspose.com/cells/cpp/)
2. Entpacken Sie das Paket und Sie finden ein Beispiel für die Verwendung von Aspose.Cells for C++ für MacOS.
3. Stellen Sie sicher, dass Sie sich im Pfad befinden, in dem sich das Beispiel befindet.
4. Führen Sie „cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release“ aus.
5. Führen Sie „cmake --build example/build“ aus.

##  **Erstellen der Hello World-Anwendung**

Mit den folgenden Schritten wird die Anwendung Hello World unter Verwendung von Aspose.Cells API erstellt:

1.  Erstellen Sie eine Instanz von[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse.
1.  Wenn Sie eine Lizenz haben, dann[Wende es an](/cells/de/cpp/licensing/).
 Wenn Sie die Testversion verwenden, überspringen Sie die lizenzbezogenen Codezeilen.
1. Greifen Sie auf jede gewünschte Zelle eines Arbeitsblatts in der Excel-Datei zu.
1. Fügen Sie die Wörter „**Hello World!**“ in eine Zelle ein, auf die zugegriffen wird.
1. Generieren Sie die geänderte Excel-Datei Microsoft.

Die Umsetzung der oben genannten Schritte wird in den folgenden Beispielen demonstriert.

###  **Codebeispiel: Erstellen einer neuen Arbeitsmappe**

Das folgende Beispiel erstellt eine neue Arbeitsmappe von Grund auf, fügt „**Hello World!**“ in Zelle A1 im ersten Arbeitsblatt ein und speichert die Excel-Datei.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

###  **Codebeispiel: Öffnen einer vorhandenen Datei**

Das folgende Beispiel öffnet eine vorhandene Excel-Vorlagendatei Microsoft, ruft eine Zelle ab und überprüft den Wert in Zelle A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
