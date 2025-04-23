---
title: Caratteristiche alimentate dall AI
type: docs
weight: 200
url: /it/net/ai-powered-features/
keywords: AI,Foglio di calcolo,funzionalità AI,potenza AI,Excel AI,OpenAI,Celle AI.
description: Questo articolo è una guida passo passo all uso delle funzionalità alimentate dall IA per l elaborazione di file di fogli di calcolo.
---


# Guida per Nuovi Utenti: Lavorare con Cells AI

Benvenuto in Cells AI! Questa guida ti accompagnerà attraverso i passaggi base per configurare e usare la libreria Cells AI.

## Indice dei Contenuti
1. [Configura Modello AI](#configure-ai-model)
2. [Crea Istanza AI](#create-ai-instance)
3. [Elabora File con AI](#process-files-with-ai)
4. [Utilizzo delle Impostazioni Proxy](#use-proxy-settings-if-you-can-not-access-the-ai-server-directly)

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
#### Usa modello AI predefinito
```csharp
Config.Model = Model.Gpt4OMini;
```

## Crea Istanza AI

Devi inizializzare un'istanza di CellsAI fornendo l'URL di base dell'API e la tua chiave API. In alternativa, puoi fornire l'URL completo dell'API se necessario.

### Esempio:
#### Inizializza con URL di base di AI chat
```csharp
String APIKey = "sk-xxxxx";
String APIRootUrl = "https://api.openai.com/";
CellsAI cellsAI = new CellsAI(APIRootUrl, APIKey);
```
#### Inizializza con URL completo di AI chat
```csharp
String APIKey = "sk-xxxxx";
String FullAPIRootUrl = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions";
CellsAI cellsAI = new CellsAI(FullAPIRootUrl, true, APIKey);
```

## Elabora File con AI

Una volta configurato il modello di AI e creata un'istanza di AI, puoi utilizzare le capacità dell'IA per elaborare file di fogli di calcolo.

### Riepilogo di un Foglio di Calcolo::
#### Ottieni il riepilogo del foglio di calcolo
```csharp
// Get summary of the spreadsheet
string summary = cellsAI.SpreadsheetSummarize("c:/student.xlsx");
```

#### Puoi anche esportare il riepilogo su un TextWriter:
```csharp
// Use TextWriter way, Output summary to a TextWriter (Console)
TextWriter writer = Console.Out;
await cellsAI.SpreadsheetSummarize("c:/student.xlsx", writer);
```
### Fai Domande su un Foglio di Calcolo:
#### Puoi fare domande sul contenuto di un foglio di calcolo:
```csharp
// Ask a question about the spreadsheet
await cellsAI.SpreadsheetQuestion("c:/student.xlsx", "Who is the best student?", writer);
```
### Crea un Foglio di Calcolo basato sulle Richieste degli Utenti:
#### Esempio:

Puoi creare un nuovo foglio di calcolo basato su una richiesta specifica. Ad esempio, generare un piano alimentare settimanale:
```csharp
await cellsAI.BuildSpreadsheet("Provide weekly daily three-meal recipes, including nutritional value, preparation methods, ingredients, and cost, one day per row, and add total cost at last row.", null, "c:/foodsweekly.xlsx");
```

Puoi anche prevedere le vendite basandoti su dati storici:

```csharp
await cellsAI.BuildSpreadsheet("Based on the sales history data from row 3 to row 10, predict the sales situation for the next year. Add it in row 11.", "c:/Sales Report Year.xlsx", "c:/Sales Report Forcast.xlsx");

```
Oppure, aggiornare i punteggi degli studenti con una classifica:
```csharp
await cellsAI.BuildSpreadsheet("Add a new column named \"Ranking\" and fill in the content of this column based on the students' total scores ranking", "c:\\student_score.xlsx", "c:\\student_score_with_rank.xlsx");
```
Utilizzo del Modello AI con Richieste Localizzate:

Puoi usare il modello AI Qianwen di Alibaba o altri modelli AI localizzati. Ecco come puoi specificare una località:
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

### Ottenere formule Excel:
#### Puoi interrogare le formule di Excel direttamente dal foglio di calcolo:
```csharp
// Get formula from the spreadsheet
string formula = cellsAI.GetExcelFormula("c:/student.xlsx", "get the total score for Xiaomin");
```
## Usa le impostazioni proxy se non puoi accedere direttamente al server AI

Se lavori dietro un proxy, puoi configurare le impostazioni proxy per consentire a Cells AI di connettersi al server.

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

##  Funzionalità e personalizzazioni aggiuntive
Cells AI consente varie personalizzazioni, come regolare il modello AI, impostare le località e modificare le uscite dei dati. Assicurati di esplorare l'API e sperimentare con diverse configurazioni per il tuo caso d'uso specifico.

## Conclusione
Cells AI ti permette di elaborare fogli di calcolo, automatizzare attività e sfruttare l'AI per le tue applicazioni basate su Excel.  

Per ulteriori dettagli, consulta la [documentazione API](https://reference.aspose.com/cells/net/aspose.cells.ai/) o il [forum di supporto](https://forum.aspose.com/c/cells/9).

Buona programmazione!
