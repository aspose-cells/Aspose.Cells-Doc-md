---
title: AI drivna funktioner
type: docs
weight: 200
url: /sv/net/ai-powered-features/
keywords: AI, kalkylblad, AI funktioner, AI kraft, Excel AI, OpenAI, Cells AI.
description: Den här artikeln är en steg för steg guide för att använda AI driven funktionalitet för att bearbeta kalkylbladsfiler.
---


# Ny användarguide: Arbeta med Cells AI

Välkommen till Cells AI! Den här guiden leder dig genom de grundläggande stegen för att konfigurera och använda Cells AI-biblioteket.

## Innehållsförteckning
1. [Konfigurera AI-modell](#konfigurera-ai-modell)
2. [Skapa AI-instans](#skapa-ai-instans)
3. [Bearbeta filer med AI](#bearbeta-filer-med-ai)
4. [Använd Proxy-inställningar](#anvand-proxy-installningar-om-du-inte-kan-atkomst-till-ai-servern-direkt)

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
#### Använd fördefinierad AI-modell
```csharp
Config.Model = Model.Gpt4OMini;
```

## Skapa AI-instans

Du måste initiera en instans av CellsAI genom att ange API-röturlen och din API-nyckel. Alternativt kan du tillhandahålla den fullständiga API-URL:en vid behov.

### Exempel:
#### Initiera med AI-chat huvud-URL
```csharp
String APIKey = "sk-xxxxx";
String APIRootUrl = "https://api.openai.com/";
CellsAI cellsAI = new CellsAI(APIRootUrl, APIKey);
```
#### Initiera med AI-chat fullständig URL
```csharp
String APIKey = "sk-xxxxx";
String FullAPIRootUrl = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions";
CellsAI cellsAI = new CellsAI(FullAPIRootUrl, true, APIKey);
```

## Bearbeta filer med AI

När du har konfigurerat AI-modellen och skapat en AI-instans kan du använda AI:ns funktioner för att bearbeta kalkylbladfiler.

### Sammanfatta ett kalkylblad::
#### Få sammanfattning av kalkylbladet
```csharp
// Get summary of the spreadsheet
string summary = cellsAI.SpreadsheetSummarize("c:/student.xlsx");
```

#### Du kan också skriva ut sammanfattningen till en TextWriter:
```csharp
// Use TextWriter way, Output summary to a TextWriter (Console)
TextWriter writer = Console.Out;
await cellsAI.SpreadsheetSummarize("c:/student.xlsx", writer);
```
### Ställ frågor om ett kalkylblad:
#### Du kan ställa frågor om innehållet i ett kalkylblad:
```csharp
// Ask a question about the spreadsheet
await cellsAI.SpreadsheetQuestion("c:/student.xlsx", "Who is the best student?", writer);
```
### Bygg ett kalkylblad baserat på användarens begäran:
#### Exempel:

Du kan skapa ett nytt kalkylblad baserat på en specifik förfrågan. Till exempel, generera en veckovis måltidsplan:
```csharp
await cellsAI.BuildSpreadsheet("Provide weekly daily three-meal recipes, including nutritional value, preparation methods, ingredients, and cost, one day per row, and add total cost at last row.", null, "c:/foodsweekly.xlsx");
```

Du kan även prognostisera försäljning baserat på historisk data:

```csharp
await cellsAI.BuildSpreadsheet("Based on the sales history data from row 3 to row 10, predict the sales situation for the next year. Add it in row 11.", "c:/Sales Report Year.xlsx", "c:/Sales Report Forcast.xlsx");

```
Eller, uppdatera elevpoäng med en ranking:
```csharp
await cellsAI.BuildSpreadsheet("Add a new column named \"Ranking\" and fill in the content of this column based on the students' total scores ranking", "c:\\student_score.xlsx", "c:\\student_score_with_rank.xlsx");
```
Använd AI-modell med lokaliserade förfrågningar:

Du kan använda Alibabas Qianwen AI-modell eller andra lokaliserade AI-modeller. Så här kan du ange en lokal:
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

### Hämta Excelformler:
#### Du kan fråga Excel-formler direkt från kalkylbladet:
```csharp
// Get formula from the spreadsheet
string formula = cellsAI.GetExcelFormula("c:/student.xlsx", "get the total score for Xiaomin");
```
## Använd proxyinställningar om du inte kan komma åt AI-servern direkt

Om du arbetar bakom en proxy kan du konfigurera proxyinställningar för att tillåta Cells AI att ansluta till servern.

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

## Ytterligare funktioner och anpassningar
Cells AI tillåter olika anpassningar, såsom att justera AI-modellen, sätta lokaler och ändra datoutgångar. Se till att utforska API:et och experimentera med olika konfigurationer för ditt specifika användningsområde.

## Slutsats
Cells AI ger dig möjlighet att bearbeta kalkylblad, automatisera uppgifter och utnyttja AI för dina Excel-baserade applikationer.  

För ytterligare information, hänvisa till [api-dokumentationen](https://reference.aspose.com/cells/net/aspose.cells.ai/) eller [supportforumet](https://forum.aspose.com/c/cells/9).

Glad kodning!
