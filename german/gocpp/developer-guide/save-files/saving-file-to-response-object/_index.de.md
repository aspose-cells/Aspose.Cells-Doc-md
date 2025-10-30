---
title: Datei an Response Objekt speichern mit Golang über C++
linktitle: Datei im Antwortobjekt speichern
type: docs
weight: 50
url: /de/go-cpp/saving-file-to-response-object/
description: Lernen Sie, wie man Dateien dynamisch speichert und sie direkt an einen Browser Client sendet mit Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Mit Aspose.Cells ist es möglich, Dateien zu manipulieren. In diesem Artikel werden die verschiedenen Möglichkeiten erläutert, wie Dateien in einem Antwortobjekt gespeichert werden können.

{{% /alert %}}

## **Speichern der Datei im Antwortobjekt**

Es ist auch möglich, eine Datei dynamisch zu generieren und direkt an den Client-Browser zu senden. Verwenden Sie dazu eine spezielle überladene Version der [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/) Methode, die die folgenden Parameter akzeptiert:

- **HttpResponse**-Objekt.
- Dateiname.
- [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/), der Inhalt-Dispositionstyp der Ausgabedatei.
- [**SaveOptions**](https://reference.aspose.com/cells/go-cpp/saveoptions/), der Dateiformat-Typ.

Die [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/) Enumeration bestimmt, ob die Datei, die an den Browser gesendet wird, die Option bietet, direkt im Browser oder in einer Anwendung mit der Erweiterung .xls/.xlsx oder einer anderen geöffnet zu werden.

Die Enumeration enthält die folgenden vordefinierten Speichertypen:

|**Typ**|**Beschreibung**|
| :- | :- |
|Anhang|Sendet die Tabelle an den Browser und öffnet sie in einer Anwendung als Anhang, der mit .xls/.xlsx oder anderen Erweiterungen verknüpft ist|
|Inline|Sendet das Dokument an den Browser und bietet die Option, die Tabelle auf der Festplatte zu speichern oder im Browser zu öffnen|

### **XLS-Dateien**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject.go" >}}
### **XLSX-Dateien**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-1.go" >}}
### **PDF-Dateien**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-2.go" >}}
### **Hinweis**

Aufgrund des Objekts "System.Web.HttpResponse", das nicht in .NET5 und .Netstandard enthalten ist,
Existiert diese Funktion nicht in Aspose.Cells .NET5 und .Netstandard Version, Sie können sich auf den folgenden Code beziehen, um die Datei im Stream zu speichern und dann den Stream zu bearbeiten.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-3.go" >}}
