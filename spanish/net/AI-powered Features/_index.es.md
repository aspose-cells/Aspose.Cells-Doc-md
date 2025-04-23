---
title: Características potenciadas por IA
type: docs
weight: 200
url: /es/net/ai-powered-features/
keywords: IA, hoja de cálculo, funciones IA, poder IA, Excel con IA, OpenAI, IA en celdas.
description: Este artículo es una guía paso a paso para usar funciones habilitadas por IA para procesar archivos de hojas de cálculo.
---


# Guía para Nuevos Usuarios: Trabajar con Cells AI

¡Bienvenido a Cells AI! Esta guía te llevará por los pasos básicos para configurar y usar la biblioteca Cells AI.

## Tabla de Contenidos
1. [Configurar Modelo AI](#configure-ai-model)
2. [Crear Instancia de IA](#create-ai-instance)
3. [Procesar Archivos con IA](#process-files-with-ai)
4. [Usar Configuración Proxy](#use-proxy-settings-if-you-can-not-access-the-ai-server-directly)

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
#### Usar modelo de IA predefinido
```csharp
Config.Model = Model.Gpt4OMini;
```

## Crear Instancia de IA

Necesitas inicializar una instancia de CellsAI proporcionando la URL raíz de la API y tu clave de API. Alternativamente, puedes proporcionar la URL completa de la API si es necesario.

### Ejemplo:
#### Inicializar con URL raíz de chat de IA
```csharp
String APIKey = "sk-xxxxx";
String APIRootUrl = "https://api.openai.com/";
CellsAI cellsAI = new CellsAI(APIRootUrl, APIKey);
```
#### Inicializar con URL completa de chat de IA
```csharp
String APIKey = "sk-xxxxx";
String FullAPIRootUrl = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions";
CellsAI cellsAI = new CellsAI(FullAPIRootUrl, true, APIKey);
```

## Procesar Archivos con IA

Una vez que hayas configurado el modelo de IA y creado una instancia de IA, puedes usar las capacidades de IA para procesar archivos de hojas de cálculo.

### Resumir una Hoja de Cálculo::
#### Obtener resumen de la hoja de cálculo
```csharp
// Get summary of the spreadsheet
string summary = cellsAI.SpreadsheetSummarize("c:/student.xlsx");
```

#### También puedes mostrar el resumen en un TextWriter:
```csharp
// Use TextWriter way, Output summary to a TextWriter (Console)
TextWriter writer = Console.Out;
await cellsAI.SpreadsheetSummarize("c:/student.xlsx", writer);
```
### Hacer Preguntas sobre una Hoja de Cálculo:
#### Puedes hacer preguntas sobre el contenido de una hoja de cálculo:
```csharp
// Ask a question about the spreadsheet
await cellsAI.SpreadsheetQuestion("c:/student.xlsx", "Who is the best student?", writer);
```
### Crear una Hoja de Cálculo basada en solicitudes del usuario:
#### Ejemplo:

Puedes crear una nueva hoja de cálculo basada en una solicitud específica. Por ejemplo, generando un plan de comidas semanal:
```csharp
await cellsAI.BuildSpreadsheet("Provide weekly daily three-meal recipes, including nutritional value, preparation methods, ingredients, and cost, one day per row, and add total cost at last row.", null, "c:/foodsweekly.xlsx");
```

También puedes pronosticar ventas basadas en datos históricos:

```csharp
await cellsAI.BuildSpreadsheet("Based on the sales history data from row 3 to row 10, predict the sales situation for the next year. Add it in row 11.", "c:/Sales Report Year.xlsx", "c:/Sales Report Forcast.xlsx");

```
O, actualizar las puntuaciones de los estudiantes con un ranking:
```csharp
await cellsAI.BuildSpreadsheet("Add a new column named \"Ranking\" and fill in the content of this column based on the students' total scores ranking", "c:\\student_score.xlsx", "c:\\student_score_with_rank.xlsx");
```
Uso del Modelo de IA con Solicitudes Localizadas:

Puedes usar el modelo de IA Qianwen de Alibaba u otros modelos de IA localizados. Aquí te mostramos cómo especificar una región:
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

### Obtener Fórmulas de Excel:
#### Puedes consultar fórmulas de Excel directamente desde la hoja de cálculo:
```csharp
// Get formula from the spreadsheet
string formula = cellsAI.GetExcelFormula("c:/student.xlsx", "get the total score for Xiaomin");
```
## Usa configuración de proxy si no puedes acceder directamente al servidor de IA

Si estás trabajando detrás de un proxy, puedes configurar la configuración del proxy para permitir que Cells AI se conecte al servidor.

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

## Funciones y personalizaciones adicionales
Cells AI permite varias personalizaciones, como ajustar el modelo de IA, establecer países, y modificar salidas de datos. Asegúrate de explorar la API y experimentar con diferentes configuraciones para tu caso de uso específico.

## Conclusión
Cells AI te permite procesar hojas de cálculo, automatizar tareas y aprovechar la IA para tus aplicaciones basadas en Excel.  

Para más detalles, consulta la [documentación de la API](https://reference.aspose.com/cells/net/aspose.cells.ai/) o el [foros de soporte](https://forum.aspose.com/c/cells/9).

¡Feliz codificación!
