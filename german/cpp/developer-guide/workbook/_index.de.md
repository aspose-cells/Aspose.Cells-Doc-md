---
title: Arbeitsmappe mit C++ verwalten
linktitle: Arbeitsmappe
type: docs
weight: 60
url: /de/cpp/managing-workbooks-and-worksheets/
description: Erfahren Sie, wie Sie die API Aspose.Cells for C++ verwenden, um Arbeitsmappen zu verwalten.
keywords: Wie man in C++ eine Arbeitsmappe verwaltet, Arbeitsmappe und Arbeitsblätter mit C++ verwaltet, Arbeitsmappen und Arbeitsblätter in C++ betreibt.
---

{{% alert color="primary" %}}

Die API Aspose.Cells for C++ bietet eine leistungsstarke und flexible API zur Verwaltung von Arbeitsmappen und Arbeitsblättern. Dieser Abschnitt erklärt, wie man Arbeitsmappen und Arbeitsblätter programmatisch erstellt, öffnet und bearbeitet.

{{% /alert %}}

## **Neue Arbeitsmappe erstellen**
Um eine neue Arbeitsmappe zu erstellen:

1. Erstellen Sie eine Instanz der [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-Klasse.
2. Fügen Sie Arbeitsblätter mit der [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Klasse hinzu.
3. Speichern Sie die Arbeitsmappe mit der [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

## **Vorhandene Arbeitsmappe öffnen**
Um eine vorhandene Arbeitsmappe zu öffnen:

1. Erstellen Sie eine Instanz der [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse und übergeben Sie den Dateipfad an den Konstruktor.
2. Greifen Sie auf die Arbeitsblätter mit der [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Klasse zu.
3. Bearbeiten Sie die Arbeitsmappe bei Bedarf.
4. Speichern Sie die Arbeitsmappe mit der [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).SetValue("Hello, World!");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Arbeitsblätter verwalten**
Die API Aspose.Cells for C++ bietet eine Vielzahl an Methoden zum Verwalten von Arbeitsblättern, inklusive Hinzufügen, Entfernen und Umbenennen.

### **Ein Arbeitsblatt hinzufügen**
Um ein neues Arbeitsblatt hinzuzufügen:

1. Zugriff auf die [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Klasse aus der Arbeitsmappe.
2. Verwenden Sie die [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) Methode, um ein neues Arbeitsblatt hinzuzufügen.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a new worksheet
    workbook.GetWorksheets().Add("NewSheet");

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **Arbeitsblatt entfernen**
Um ein Arbeitsblatt zu entfernen:

1. Zugriff auf die [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Klasse aus der Arbeitsmappe.
2. Verwenden Sie die [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat/) Methode, um ein Arbeitsblatt nach Index zu entfernen.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Open an existing workbook
    Aspose::Cells::Workbook workbook("input.xlsx");

    // Remove the first worksheet
    workbook.GetWorksheets().RemoveAt(0);

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **Arbeitsblatt umbenennen**
Um ein Arbeitsblatt umzubenennen:

1. Zugriff auf die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse aus der Arbeitsmappe.
2. Verwenden Sie die [SetName](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setname/) Methode, um das Arbeitsblatt umzubenennen.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName("RenamedSheet");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Fazit**
Aspose.Cells for C++ bietet eine umfassende Sammlung von Werkzeugen zur Verwaltung von Arbeitsmappen und Arbeitsblättern. Egal, ob Sie eine neue Arbeitsmappe erstellen, eine bestehende öffnen oder Arbeitsblätter manipulieren möchten, Aspose.Cells macht es einfach, programmatisch mit Excel-Dateien zu arbeiten.
