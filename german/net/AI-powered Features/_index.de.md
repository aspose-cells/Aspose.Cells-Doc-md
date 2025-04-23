---
title: KI Features
type: docs
weight: 200
url: /de/net/ai-powered-features/
keywords: KI,Tabellenkalkulation,KI Funktionen,KI Power,Excel KI,OpenAI,Zellen KI.
description: Dieser Artikel ist eine Schritt für Schritt Anleitung zur Verwendung KI gestützter Funktionen zur Verarbeitung von Tabellenkalkulationsdateien.
---


# Neuer Benutzerleitfaden: Arbeiten mit Cells AI

Willkommen bei Cells AI! Dieser Leitfaden führt Sie durch die grundlegenden Schritte zur Konfiguration und Nutzung der Cells AI-Bibliothek.

## Inhaltsverzeichnis
1. [Konfigurieren des KI-Modells](#configure-ai-model)
2. [Erstellen einer KI-Instanz](#create-ai-instance)
3. [Verarbeiten von Dateien mit KI](#process-files-with-ai)
4. [Verwendung von Proxy-Einstellungen](#use-proxy-settings-if-you-can-not-access-the-ai-server-directly)

---

## Prerequisites

Before using Cells AI, ensure you have the following:
- A valid **API Key** from OpenAI or the other AI provider of your choice.
- A .NET development environment set up for C# programming.

## Configure AI Model

To start using Cells AI, you need to set up an AI model. You can either create a new model or use one of the predefined models.

### Example:
#### Setup a new AI model
```csharp
Config.Model = new Model("gpt-4-32k");
```
#### Vorgefertigtes KI-Modell verwenden
```csharp
Config.Model = Model.Gpt4OMini;
```

## KI-Instanz erstellen

Sie müssen eine Instanz von CellsAI initialisieren, indem Sie die API-Root-URL und Ihren API-Schlüssel angeben. Alternativ können Sie die vollständige API-URL bereitstellen, falls erforderlich.

### Beispiel:
#### Initialisieren mit API-Chat-Root-URL
```csharp
String APIKey = "sk-xxxxx";
String APIRootUrl = "https://api.openai.com/";
CellsAI cellsAI = new CellsAI(APIRootUrl, APIKey);
```
#### Initialisieren mit vollständiger API-URL
```csharp
String APIKey = "sk-xxxxx";
String FullAPIRootUrl = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions";
CellsAI cellsAI = new CellsAI(FullAPIRootUrl, true, APIKey);
```

## Dateien mit KI verarbeiten

Sobald Sie das KI-Modell konfiguriert und eine KI-Instanz erstellt haben, können Sie die Fähigkeiten der KI nutzen, um Tabellenkalkulationsdateien zu verarbeiten.

### Zusammenfassung einer Tabelle::
#### Zusammenfassung der Tabelle erhalten
```csharp
// Get summary of the spreadsheet
string summary = cellsAI.SpreadsheetSummarize("c:/student.xlsx");
```

#### Sie können die Zusammenfassung auch in einen TextWriter ausgeben:
```csharp
// Use TextWriter way, Output summary to a TextWriter (Console)
TextWriter writer = Console.Out;
await cellsAI.SpreadsheetSummarize("c:/student.xlsx", writer);
```
### Fragen zu einer Tabelle stellen:
#### Sie können Fragen zum Inhalt einer Tabelle stellen:
```csharp
// Ask a question about the spreadsheet
await cellsAI.SpreadsheetQuestion("c:/student.xlsx", "Who is the best student?", writer);
```
### Eine Tabelle basierend auf Benutz !=eranforderungen erstellen:
#### Beispiel:

Sie können eine neue Tabelle basierend auf einer bestimmten Anforderung erstellen. Zum Beispiel die Erstellung eines Wochenessensplans:
```csharp
await cellsAI.BuildSpreadsheet("Provide weekly daily three-meal recipes, including nutritional value, preparation methods, ingredients, and cost, one day per row, and add total cost at last row.", null, "c:/foodsweekly.xlsx");
```

Sie können auch den Verkauf basierend auf historischen Daten prognostizieren:

```csharp
await cellsAI.BuildSpreadsheet("Based on the sales history data from row 3 to row 10, predict the sales situation for the next year. Add it in row 11.", "c:/Sales Report Year.xlsx", "c:/Sales Report Forcast.xlsx");

```
Oder die Punktzahl der Schüler mit einer Rangfolge aktualisieren:
```csharp
await cellsAI.BuildSpreadsheet("Add a new column named \"Ranking\" and fill in the content of this column based on the students' total scores ranking", "c:\\student_score.xlsx", "c:\\student_score_with_rank.xlsx");
```
Verwendung des KI-Modells mit lokalisierten Anforderungen:

Sie können das Qianwen-KI-Modell von Alibaba oder andere lokalisierten KI-Modelle verwenden. Hier erfahren Sie, wie Sie eine Spracheinstellung festlegen können:
```csharp
// Set to use QwenPlus AI model
Config.Model = Model.QwenPlus;
// Set locale info (e.g., Chinese)
Config.Locale = "zh";

// User request in Chinese
string userRequest = "增加新的一列,列名称是\"排名\" 并根据学生的总分大小排名填入这一列的内容";
string outfile = "D:\\学生排行.xlsx";
string inputfile = "D:\\student_score_zh.xlsx";
await cellsAI.BuildSpreadsheet(userRequest, inputfile, outfile);

```

### Excel-Formeln abrufen:
#### Sie können Excel-Formeln direkt aus der Tabelle abfragen:
```csharp
// Get formula from the spreadsheet
string formula = cellsAI.GetExcelFormula("c:/student.xlsx", "get the total score for Xiaomin");
```
## Proxy-Einstellungen verwenden, wenn Sie keinen direkten Zugriff auf den KI-Server haben

Wenn Sie hinter einem Proxy arbeiten, können Sie Proxy-Einstellungen konfigurieren, um Cells AI die Verbindung zum Server zu ermöglichen.

```csharp
// Set up proxy for Cells AI
string proxyAddress = "http://127.0.0.1:58591";
WebProxy proxy = new WebProxy(proxyAddress)
{
    BypassProxyOnLocal = false,  
    UseDefaultCredentials = false,
};

// Apply the proxy setting
cellsAI.Proxy = proxy;
```

## Zusätzliche Funktionen und Anpassungen
Cells AI ermöglicht verschiedene Anpassungen, wie z.B. die Einstellung des KI-Modells, die Festlegung von Spracheinstellungen und die Modifizierung der Daten-Ausgaben. Stellen Sie sicher, dass Sie die API erkunden und mit verschiedenen Konfigurationen für Ihren spezifischen Anwendungsfall experimentieren.

## Fazit
Cells AI befähigt Sie dazu, Tabellenkalkulationen zu verarbeiten, Aufgaben zu automatisieren und KI für Ihre auf Excel basierenden Anwendungen zu nutzen.  

Weitere Details finden Sie in der [API-Dokumentation](https://reference.aspose.com/cells/net/aspose.cells.ai/) oder im [Support-Forum](https://forum.aspose.com/c/cells/9).

Viel Spaß beim Programmieren!
