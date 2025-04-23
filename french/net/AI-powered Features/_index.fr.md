---
title: Fonctionnalités alimentées par l IA
type: docs
weight: 200
url: /fr/net/ai-powered-features/
keywords: IA, tableur, fonctionnalités IA, puissance IA, Excel IA, OpenAI, Cells IA.
description: Cet article est un guide étape par étape pour utiliser les fonctionnalités alimentées par l IA pour traiter les fichiers de feuille de calcul.
---


# Guide pour les nouveaux utilisateurs : Travailler avec Cells AI

Bienvenue dans Cells AI ! Ce guide vous guidera à travers les étapes de base pour configurer et utiliser la bibliothèque Cells AI.

## Table des matières
1. [Configurer le modèle AI](#configure-ai-model)
2. [Créer une instance AI](#create-ai-instance)
3. [Traiter des fichiers avec l'IA](#process-files-with-ai)
4. [Utiliser les paramètres du proxy](#use-proxy-settings-if-you-can-not-access-the-ai-server-directly)

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
#### Utiliser un modèle AI prédéfini
```csharp
Config.Model = Model.Gpt4OMini;
```

## Créer une instance AI

Vous devez initialiser une instance de CellsAI en fournissant l'URL racine de l'API et votre clé API. Alternativement, vous pouvez fournir l'URL complète de l'API si nécessaire.

### Exemple :
#### Initialiser avec l'URL racine de l'IA de chat
```csharp
String APIKey = "sk-xxxxx";
String APIRootUrl = "https://api.openai.com/";
CellsAI cellsAI = new CellsAI(APIRootUrl, APIKey);
```
#### Initialiser avec l'URL complète de l'IA de chat
```csharp
String APIKey = "sk-xxxxx";
String FullAPIRootUrl = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions";
CellsAI cellsAI = new CellsAI(FullAPIRootUrl, true, APIKey);
```

## Traiter des fichiers avec l'IA

Une fois que vous avez configuré le modèle AI et créé une instance AI, vous pouvez utiliser les capacités de l'IA pour traiter des fichiers de feuilles de calcul.

### Résumer une feuille de calcul :
#### Obtenir le résumé de la feuille de calcul
```csharp
// Get summary of the spreadsheet
string summary = cellsAI.SpreadsheetSummarize("c:/student.xlsx");
```

#### Vous pouvez également exporter le résumé vers un TextWriter :
```csharp
// Use TextWriter way, Output summary to a TextWriter (Console)
TextWriter writer = Console.Out;
await cellsAI.SpreadsheetSummarize("c:/student.xlsx", writer);
```
### Poser des questions sur une feuille de calcul :
#### Vous pouvez poser des questions sur le contenu d'une feuille de calcul :
```csharp
// Ask a question about the spreadsheet
await cellsAI.SpreadsheetQuestion("c:/student.xlsx", "Who is the best student?", writer);
```
### Construire une feuille de calcul en fonction des demandes de l'utilisateur :
#### Exemple :

Vous pouvez créer une nouvelle feuille de calcul en fonction d'une demande spécifique. Par exemple, générer un plan de repas hebdomadaire :
```csharp
await cellsAI.BuildSpreadsheet("Provide weekly daily three-meal recipes, including nutritional value, preparation methods, ingredients, and cost, one day per row, and add total cost at last row.", null, "c:/foodsweekly.xlsx");
```

Vous pouvez également prévoir les ventes en fonction des données historiques :

```csharp
await cellsAI.BuildSpreadsheet("Based on the sales history data from row 3 to row 10, predict the sales situation for the next year. Add it in row 11.", "c:/Sales Report Year.xlsx", "c:/Sales Report Forcast.xlsx");

```
Ou, mettre à jour les scores des étudiants avec un classement :
```csharp
await cellsAI.BuildSpreadsheet("Add a new column named \"Ranking\" and fill in the content of this column based on the students' total scores ranking", "c:\\student_score.xlsx", "c:\\student_score_with_rank.xlsx");
```
Utilisation du modèle AI avec des demandes localisées :

Vous pouvez utiliser le modèle AI Qianwen d'Alibaba ou d'autres modèles AI localisés. Voici comment spécifier une région :
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

### Obtenir des formules Excel :
#### Vous pouvez interroger directement des formules Excel à partir de la feuille de calcul :
```csharp
// Get formula from the spreadsheet
string formula = cellsAI.GetExcelFormula("c:/student.xlsx", "get the total score for Xiaomin");
```
## Utiliser les paramètres proxy si vous ne pouvez pas accéder directement au serveur AI

Si vous travaillez derrière un proxy, vous pouvez configurer les paramètres proxy pour permettre à Cells AI de se connecter au serveur.

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

## Fonctionnalités supplémentaires et personnalisations
Cells AI permet diverses personnalisations, telles que l'ajustement du modèle AI, la définition des locales et la modification des sorties de données. Assurez-vous d'explorer l'API et d'expérimenter avec différentes configurations pour votre cas d'utilisation spécifique.

## Conclusion
Cells AI vous permet de traiter des feuilles de calcul, d'automatiser des tâches et d'utiliser l'IA pour vos applications basées sur Excel.  

Pour plus de détails, consultez la [documentation de l’API](https://reference.aspose.com/cells/net/aspose.cells.ai/) ou le [forum de support](https://forum.aspose.com/c/cells/9).

Bon codage !
