---
title: Zugriff auf und Aktualisierung der Teile des Rich Text Inhalts einer Zelle mit Golang via C++
linktitle: Rich Text Formatierung
type: docs
weight: 40
url: /de/go-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Lernen Sie, wie Sie die Abschnitte von Rich Text einer Zelle über die API Aspose.Cells for C++ zugreifen und aktualisieren.
keywords: Zugriff und Aktualisierung des Rich Texts einer Zelle, Abrufen des Rich Texts einer Zelle, Rich Text einer Zelle bearbeiten, Rich Text einer Zelle abrufen, Rich Text einer Zelle aktualisieren, Rich Text einer Zelle ändern
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie auf die Teile des Rich-Texts einer Zelle zugreifen und diese aktualisieren. Hierfür können Sie die [**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/) und [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) Methoden verwenden. Diese Methoden geben ein Array von [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)-Objekten zurück und akzeptieren dieses, mit dem Sie verschiedene Eigenschaften der Schriftart wie Schriftartname, Schriftfarbe, Fettgedrucktheit usw. ändern können.

{{% /alert %}}

## **Teile des Rich-Texts der Zelle zugreifen und aktualisieren**

Der folgende Code demonstriert die Verwendung der [**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/)- und [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/)-Methoden mit der [Quell-Excel-Datei](5112369.xlsx). Die Quell-Excel-Datei enthält einen Rich-Text in Zelle A1 mit 3 Abschnitten, die jeweils eine andere Schriftart haben. Der Code greift auf diese Abschnitte zu und aktualisiert die Schriftart des ersten Abschnitts auf **"Arial"**. Die modifizierte Arbeitsmappe wird als [Ausgabe-Excel-Datei](5112366.xlsx) gespeichert.

### C++-Code zum Zugriff und zur Aktualisierung von Rich-Text-Abschnitten

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RichFormattingText.go" >}}
### Von der Beispiellösung generierte Konsolenausgabe

Hier ist die Konsolenausgabe beim Verwenden der [Quell-Excel-Datei](5112369.xlsx):

{{< highlight java >}}

Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana

{{< /highlight >}}
