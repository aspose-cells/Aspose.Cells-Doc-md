---
title: Arbeitsmappe mit Golang über C++ verwalten
linktitle: Arbeitsmappe
type: docs
weight: 60
url: /de/go-cpp/managing-workbooks-and-worksheets/
description: Erfahren Sie, wie Sie die API Aspose.Cells for C++ verwenden, um Arbeitsmappen zu verwalten.
keywords: Wie man in C++ eine Arbeitsmappe verwaltet, Arbeitsmappe und Arbeitsblätter mit C++ verwaltet, Arbeitsmappen und Arbeitsblätter in C++ betreibt.
---

{{% alert color="primary" %}}

Die API Aspose.Cells for C++ bietet eine leistungsstarke und flexible API zur Verwaltung von Arbeitsmappen und Arbeitsblättern. Dieser Abschnitt erklärt, wie man Arbeitsmappen und Arbeitsblätter programmatisch erstellt, öffnet und bearbeitet.

{{% /alert %}}

## **Neue Arbeitsmappe erstellen**
Um eine neue Arbeitsmappe zu erstellen:

1. Erstellen Sie eine Instanz der Klasse [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).
2. Fügen Sie Arbeitsblätter mit der Klasse [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) hinzu.
3. Speichern Sie die Arbeitsmappe mit der Methode [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook.go" >}}
## **Vorhandene Arbeitsmappe öffnen**
Um eine vorhandene Arbeitsmappe zu öffnen:

1. Erstellen Sie eine Instanz der Klasse [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) und übergeben Sie den Dateipfad an den Konstruktor.
2. Greifen Sie auf die Arbeitsblätter mit der Klasse [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) zu.
3. Bearbeiten Sie die Arbeitsmappe bei Bedarf.
4. Speichern Sie die Arbeitsmappe mit der Methode [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-1.go" >}}
## **Arbeitsblätter verwalten**
Die API Aspose.Cells for C++ bietet eine Vielzahl an Methoden zum Verwalten von Arbeitsblättern, inklusive Hinzufügen, Entfernen und Umbenennen.

### **Ein Arbeitsblatt hinzufügen**
Um ein neues Arbeitsblatt hinzuzufügen:

1. Greifen Sie auf die Klasse [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) der Arbeitsmappe zu.
2. Verwenden Sie die Methode [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_sheettype/) zum Hinzufügen eines neuen Arbeitsblatts.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-2.go" >}}
### **Arbeitsblatt entfernen**
Um ein Arbeitsblatt zu entfernen:

1. Greifen Sie auf die Klasse [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) der Arbeitsmappe zu.
2. Verwenden Sie die Methode [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat_string/) zum Entfernen eines Arbeitsblatts nach Index.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-3.go" >}}
### **Arbeitsblatt umbenennen**
Um ein Arbeitsblatt umzubenennen:

1. Greifen Sie auf die Klasse [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) der Arbeitsmappe zu.
2. Verwenden Sie die Methode [SetName](https://reference.aspose.com/cells/go-cpp/worksheet/setname/) zum Umbenennen des Arbeitsblatts.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-4.go" >}}
## **Fazit**
Aspose.Cells for C++ bietet eine umfassende Sammlung von Werkzeugen zur Verwaltung von Arbeitsmappen und Arbeitsblättern. Egal, ob Sie eine neue Arbeitsmappe erstellen, eine bestehende öffnen oder Arbeitsblätter manipulieren möchten, Aspose.Cells macht es einfach, programmatisch mit Excel-Dateien zu arbeiten.
