---
title: Dateien speichern
type: docs
weight: 20
url: /de/go-cpp/saving-files/
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es, Dateien zu erstellen und zu speichern sowie bestehende Dateien zu manipulieren. Dieser Artikel erklärt die verschiedenen Möglichkeiten, wie Dateien gespeichert werden können.

{{% /alert %}}

## **Verschiedene Möglichkeiten, Dateien zu speichern**

Aspose.Cells bietet die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)-Klasse, die eine Microsoft Excel-Datei darstellt und Methoden bereitstellt, um mit Excel-Dateien zu arbeiten. Die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse bietet die [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) Methode zum Speichern von Excel-Dateien. Diese [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) Methode hat viele Überladungen, die verwendet werden, um Dateien auf unterschiedliche Weise zu speichern. Das Dateiformat, in das die Datei gespeichert wird, wird durch die [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) Aufzählung festgelegt.

## **Datei an einem bestimmten Speicherort speichern**

Um Dateien an einem Speicherort zu speichern, geben Sie beim Aufruf der [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) Methode den Dateinamen (inklusive Speicherpfad) und das gewünschte Dateiformat (aus der [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) Aufzählung) an.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToSomeLocation.go" >}}

## **Datei in einen Stream speichern**

Um Dateien in einen Stream zu speichern, erstellen Sie ein MemoryStream- oder FileStream-Objekt und speichern die Datei in dieses Stream-Objekt durch Aufruf der [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) Methode. Geben Sie das gewünschte Dateiformat mit der [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) Aufzählung an, wenn Sie die [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_saveFormat/) Methode aufrufen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToStream.go" >}}

## **Datei als PDF speichern**

Um den gewünschten Inhalt mit der Bibliothek Aspose.Cells for Go via C++ in eine PDF-Datei zu speichern, erstellen Sie ein neues [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)-Objekt oder laden ein bestehendes Excel-File, und speichern es dann als PDF, indem Sie die Save-Methode des [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) -Objekts aufrufen. Beim Aufrufen der Save-Methode verwenden Sie die [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) Aufzählung, um das gewünschte Dateiformat festzulegen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToPdf.go" >}}
