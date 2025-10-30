---
title: Schriftarteinstellungen mit Golang via C++
linktitle: Schriftart Einstellungen
type: docs
weight: 30
url: /de/go-cpp/cells-font-settings/
description: Aspose.Cells ist eine C++ Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien. Es unterstützt das Festlegen der Schriftarteinstellungen von Zellen, um den Schriftstil und die Eigenschaften der Zellen anzupassen. Dieser Artikel zeigt, wie man die Aspose.Cells Bibliothek zum Einstellen der Zellenschriftart verwendet.
keywords: Aspose.Cells, Zellen, Schriftarteinstellungen, Stile, Eigenschaften
---

{{% alert color="primary" %}}

Das Aussehen und Gefühl eines Textes kann durch Ändern der Schriftarteinstellungen gesteuert werden. Die Schriftarteinstellungen können Name, Stil, Größe, Farbe und andere Effekte der Schrift umfassen. Genau wie Microsoft Excel unterstützt Aspose.Cells auch die Konfiguration der Schriftarteinstellungen der Zellen.

{{% /alert %}}

## **Konfigurieren von Schriftarteinstellungen**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die den Zugriff auf jede Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse stellt eine [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung bereit. Jedes Element in der [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells bietet die [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/)-Klasse' [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) und [**SetStyle**](https://reference.aspose.com/cells/go-cpp/cell/setstyle/)-Methoden, die verwendet werden, um den Formatierungsstil einer Zelle abzurufen und festzulegen. Die Klasse [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) bietet Eigenschaften zur Konfiguration der Schriftarteinstellungen.

### **Schriftartname festlegen**

Entwickler können jede Schriftart auf den Text in einer Zelle anwenden, indem sie die [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) Eigenschaft des [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)-Objekts verwenden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings.go" >}}
### **Schriftschnitt auf Fett setzen**

Entwickler können den Text fett machen, indem sie die Eigenschaft [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) des Objekts [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) auf **true** setzen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-1.go" >}}
### **Schriftgröße festlegen**

Setzen Sie die Schriftgröße mit der [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/)-Eigenschaft des Objekts [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-2.go" >}}
### **Schriftfarbe festlegen**

Verwenden Sie die [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)-Objekt’s [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/)-Eigenschaft, um die Schriftfarbe festzulegen. Wählen Sie eine Farbe aus der Enum- (Farb-)Liste (Teil des C++-Frameworks) und weisen Sie sie der [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/)-Eigenschaft zu.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-3.go" >}}
### **Schriftart-Unterstrich-Typ festlegen**

Verwenden Sie die Eigenschaft [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) des Objekts [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/), um Text zu unterstreichen. Aspose.Cells bietet verschiedene vordefinierte Schriftarten-Unterstreichungstypen in der [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/) Enumeration.

|**Schriftart-Unterstreichungstypen**|**Beschreibung**|
| :- | :- |
|Accounting|Einzelne Buchhaltungsunterstreichung|
|Double|Doppelte Unterstreichung|
|DoubleAccounting|Doppelte Buchhaltungsunterstreichung|
|None|Keine Unterstreichung|
|Single|Einfache Unterstreichung|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-4.go" >}}
### **Einstellung des Durchgestrichen-Effekts**

Wenden Sie den Durchgestrichen-Effekt an, indem Sie die Eigenschaft [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) des Objekts [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) auf **true** setzen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-5.go" >}}
### **Einstellen des Tiefgestellt-Effekts**

Wenden Sie den Tiefgestellt-Effekt an, indem Sie die Eigenschaft [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) des Objekts [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) auf **true** setzen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-6.go" >}}
### **Einstellen des Hochgestellt-Effekts auf Schriftart**

Entwickler können den Hochgestellt-Effekt auf die Schriftart anwenden, indem sie die [**IsSuperscript**](https://reference.aspose.com/cells/go-cpp/font/issuperscript/)-Eigenschaft des [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)-Objekts auf **true** setzen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-7.go" >}}
## **Erweiterte Themen**
- [Hoch- und Tiefgestellt-Effekte auf Schriftarten anwenden](/cells/de/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Eine Liste der in einer Arbeitsmappe oder einem Arbeitsblatt verwendeten Schriftarten abrufen](/cells/de/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
