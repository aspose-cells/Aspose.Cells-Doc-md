---
title: Versionierung
type: docs
weight: 40
url: /de/go-cpp/versioning/
description: So installieren Sie Aspose Cells for Go über C++ und erstellen eine Hello World Anwendung.
---

**github.com/aspose-cells/aspose-cells-go-cpp/v25** ist ein Go-Modulpfad, der eine bestimmte Version einer Drittanbieterbibliothek angibt. Lassen Sie uns diesen Modulpfad aufschlüsseln und seine Bedeutung erklären:
Aufschlüsselung des Modulpfades

1. **GitHub Repository Adresse**: github.com/aspose-cells/aspose-cells-go-cpp

- Dieser Teil zeigt an, dass die Bibliothek auf GitHub gehostet wird, unter der Organisation oder dem Nutzer aspose-cells, im Repository namens aspose-cells-go-cpp.
- Aspose.Cells ist eine Suite von APIs zur Handhabung und Bearbeitung von Tabellenkalkulationsdateien (wie Excel).

1. **Versionsnummer**: /v25

- /v25 zeigt an, dass dies Version 24 der Bibliothek ist. In Go Modules wird die semantische Versionierung (SemVer) unterstützt, wobei Pfade mit /vN verwendet werden, um die Hauptversion explizit anzugeben.
- Wenn die Hauptversion größer oder gleich 2 ist, muss der Modulpfad die Versionsnummer enthalten, um Kompatibilität und Isolierung zwischen verschiedenen Hauptversionen zu gewährleisten.

### **Bedeutung**

- **aspose-cells-go-cpp**: Dies ist eine Go-Sprachebindung für eine C++-Bibliothek, die es ermöglicht, die Aspose.Cells-Funktionalitäten innerhalb Ihrer Go-Programme zu nutzen, um Excel-Dateien zu lesen, zu schreiben und zu manipulieren, sowie andere Operationen.
- **v25**: Dies zeigt an, dass die Version 24 der Bibliothek referenziert wird. Verschiedene Hauptversionen können inkompatible Änderungen einführen, daher ist die Angabe der Versionsnummer entscheidend, um sicherzustellen, dass Ihr Projekt auf die richtige API und das richtige Verhalten zugreift.

### **Verwendung**

Um aspose-cells-go-cpp v25 in Ihrem Go-Projekt zu verwenden, müssen Sie die folgende Zeile zu Ihrer go.mod-Datei hinzufügen:

```Go
require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.x.x
```

Ersetzen Sie v25.x.x durch die spezifischen Neben- und Patchesversionsnummern, z.B. v25.0.0. Sie können diese Abhängigkeit automatisch mit dem Befehl go get hinzufügen und herunterladen:

```Go
go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.x.x
```
