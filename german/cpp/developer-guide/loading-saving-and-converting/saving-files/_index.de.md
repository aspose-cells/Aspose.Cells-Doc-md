---
title: Dateien speichern
type: docs
weight: 20
url: /de/cpp/saving-files/
---

{{% alert color="primary" %}} 

Mit Aspose.Cells ist es möglich, Dateien zu erstellen und zu speichern sowie vorhandene Dateien zu bearbeiten. In diesem Artikel werden die verschiedenen Möglichkeiten erläutert, wie Dateien gespeichert werden können.

{{% /alert %}} 
## **Verschiedene Möglichkeiten, Dateien zu speichern**
Aspose.Cells stellt die [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bereit, die eine Microsoft Excel-Datei repräsentiert und die erforderlichen Methoden zum Arbeiten mit Excel-Dateien bereitstellt. Die [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse bietet die [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode zum Speichern von Excel-Dateien. Die [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode hat viele Überladungen, die zum Speichern von Dateien auf unterschiedliche Weise verwendet werden. Das Dateiformat, in das die Datei gespeichert wird, wird durch die [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) Aufzählung entschieden.
## **Datei an einem bestimmten Speicherort speichern**
Um Dateien an einem Speicherort zu speichern, geben Sie den Dateinamen (vollständig mit Speicherpfad) und das gewünschte Dateiformat (aus der [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) Aufzählung) an, wenn Sie die [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode des [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Objekts aufrufen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


## **Datei in einen Stream speichern**
Um Dateien in einen Stream zu speichern, erstellen Sie ein MemoryStream- oder FileStream-Objekt und speichern die Datei in diesem Stream-Objekt, indem Sie die [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode des [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Objekts aufrufen. Geben Sie beim Aufrufen der [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode das gewünschte Dateiformat an, indem Sie die [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) Aufzählung verwenden.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}

## **Datei als PDF speichern**
Um den gewünschten Inhalt mithilfe der Bibliothek Aspose.Cells for C++ in eine PDF-Datei zu speichern, erstellen Sie ein neues [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Objekt oder konstruieren Sie ein [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Objekt, indem Sie eine vorhandene Excel-Datei lesen, und speichern dann die Datei als PDF, indem Sie die Save-Methode des [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Objekts aufrufen. Bei Aufruf der Save-Methode verwenden Sie die [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) Aufzählung, um das gewünschte Dateiformat anzugeben.


{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToPdf-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
